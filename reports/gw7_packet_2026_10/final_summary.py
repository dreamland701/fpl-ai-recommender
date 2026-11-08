"""Write <PACKET_DIR>/README.md for the GW7 final refresh from the JSON outputs.

Compares against the 2026-10-04 packet (statuses, news and forecasts that moved),
lists the fixed-pipeline options and lineups, the shadow adapter reads, and the
E20 holdout verdict lines from logs/e20_chain.log.
"""
import json
import os
from pathlib import Path

ROOT = Path("/home/wescheng/projects/fpl/fpl")
FIRST = Path(__file__).resolve().parent
PACKET = Path(os.environ.get("PACKET_DIR", FIRST / "final"))
TARGETS = ("Haaland", "De Cuyper", "E.Le Fée", "Xhaka", "Rogers", "Hall")


def read_json(path):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError):
        return None


def read_forecasts(path):
    try:
        return {r["player_id"]: r for r in map(json.loads, open(path)) if r}
    except OSError:
        return {}


def main() -> None:
    manifest = read_json(PACKET / "snapshot" / "manifest.json") or {}
    state = read_json(PACKET / "entry_state.json") or {}
    sheet = (read_json(PACKET / "decision_sheet.json") or {}).get("new", {})
    lineups = read_json(PACKET / "route_lineups.json") or {}
    now = read_forecasts(PACKET / "forecasts_new_pipeline.jsonl")
    before = read_forecasts(FIRST / "forecasts_new_pipeline.jsonl")
    lines = ["# GW7 final packet (fixed pipeline)", ""]
    lines.append(f"- **Snapshot:** {manifest.get('retrieved_at_utc', '?')} UTC; deadline {manifest.get('deadline_time', '?')}.")
    if state:
        pending = state.get("pending_transfers") or []
        lines.append(f"- **Entry 6535607:** bank £{state.get('bank')}m, free transfers {state.get('free_transfers')}, "
                     f"chips used: {', '.join(state.get('chips_used') or []) or 'none'}. "
                     f"Transfers already made for GW7: {', '.join(f'{t['out']} → {t['in']}' for t in pending) or 'none'}.")
        lines.append(f"- **Selling prices vs the 10-04 app values:** {state.get('selling_price_check')}.")
    lines += ["", "## What moved since 2026-10-04", "",
              "| Player | Status now | News now | GW7 (10-04 → now) | GW7–11 (10-04 → now) |", "|---|---|---|---|---|"]
    squad_ids = [s["player_id"] for s in state.get("squad", [])]
    by_name = {r["name"]: pid for pid, r in now.items()}
    for pid in squad_ids + [by_name[n] for n in TARGETS if n in by_name]:
        r, b = now.get(pid), before.get(pid)
        if not r:
            continue
        changed = (not b) or b["status"] != r["status"] or b["news"] != r["news"] or abs(b["p5"] - r["p5"]) >= 0.5
        if changed:
            lines.append(f"| {r['name']} | {r['status']} | {r['news'][:60] or '—'} | "
                         f"{(b or {}).get('p1', float('nan')):.2f} → {r['p1']:.2f} | {(b or {}).get('p5', float('nan')):.1f} → {r['p5']:.1f} |")
    if sheet:
        lines += ["", "## Options (GW7–11 gain vs holding, net of hits; route scorer from the 10-04 packet)", "",
                  "| Option | Gain now | If rolled to GW7 | Bank after |", "|---|---|---|---|"]
        for key, value in sheet.get("routes", {}).items():
            if value.get("now"):
                r = value["now"][0]
                roll = value["roll"][0]["gain_roll"] if value.get("roll") else float("nan")
                lines.append(f"| {' + '.join(r['out'])} → {' + '.join(r['in'])} | {r['gain_now']:+.1f} | {roll:+.1f} | {r['itb']} |")
        for chip, info in (sheet.get("chips") or {}).items():
            lines.append(f"| {chip.replace('_', ' ').title()} ({info['horizon']}) | {info['gain']:+.1f} | — | {info['bank_after']} |")
        lines += ["", f"Hold: XI {', '.join(sheet.get('starting_xi', []))}; bench {' > '.join(sheet.get('bench_order', []))}; "
                  f"captain {sheet.get('captain')}, vice {sheet.get('vice_captain')}."]
    if lineups:
        lines += ["", "## Lineups for the leading routes (bench order = entry order, GK first)", ""]
        for label, info in lineups.items():
            lines.append(f"- **{label}** (bank after {info['bank_after']}): XI {', '.join(info['xi'])}; "
                         f"bench {' > '.join(info['bench_order'])}; C {info['captain']}, VC {info['vice']}; "
                         f"GW7 XI forecast {info['gw7_xi_points_incl_captain']} before hits.")
    for label in ("e11full", "e20"):
        shadow = read_json(PACKET / f"shadow_{label}.json")
        if not shadow:
            continue
        lines += ["", f"## Shadow read: {label} (not used for the decision)", "",
                  f"Parsed {shadow['parsed']}/{shadow['examples']} responses."]
        for row in shadow["rows"]:
            c, a = row["classic"], row["adapter"]
            if abs(a["p1"] - c["p1"]) >= 0.3 or abs(a["papp"] - c["papp"]) >= 0.1:
                lines.append(f"- {row['player']}: GW7 {c['p1']:.2f} → {a['p1']:.2f}, P(appear) {c['papp']:.2f} → {a['papp']:.2f}")
        dis = shadow.get("availability_disagreements") or []
        if dis:
            lines.append("- Availability disagreements among likely starters: "
                         + ", ".join(f"{d['player']} {d['classic_papp']}→{d['adapter_papp']}" for d in dis[:12]))
        for side, d in shadow.get("decisions", {}).items():
            moves = "; ".join(f"{'+'.join(t['out'])} → {'+'.join(t['in'])} ({t['gain']:+.1f})" for t in d["transfers"][:2])
            lines.append(f"- Decision layer on {side} forecasts: C {d['captain']}, VC {d['vice']}; top moves: {moves or 'none'}")
    sheets = sorted(PACKET.glob("sft_side_by_side_*.md"))
    if sheets:
        lines += ["", "## Classic vs classic + SFT, with the text behind each move", ""]
        lines += [f"- [{sheet.stem.replace('sft_side_by_side_', '')}]({sheet.name})" for sheet in sheets]
    log = ROOT / "logs" / "e20_chain.log"
    if log.exists():
        keep = [l.split(" ", 2)[-1].rstrip() for l in log.read_text().splitlines()
                if any(k in l for k in ("MAE:", "availability AUC", "TOTAL:", "GW27-30", "GW31-34", "GW35-38", "FAILED"))]
        if keep:
            lines += ["", "## E20 holdout (2025-26 GW27–38, fixed pipeline)", ""] + [f"- {k}" for k in keep]
    lines += ["", "Classic + F6 on the fixed pipeline makes the decision; adapters are logged in shadow. "
              "See ../README.md for how to read the route gains and their uncertainty."]
    (PACKET / "README.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {PACKET / 'README.md'}")


if __name__ == "__main__":
    main()

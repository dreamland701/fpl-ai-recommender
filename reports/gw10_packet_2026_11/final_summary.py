"""Write <PACKET_DIR>/README.md for a GW10 packet run from the JSON outputs.

Compares against the interim packet at the packet root (GW10: built Wed 2026-11-04 evening PST) (statuses, news and forecasts that moved) when PACKET_DIR is
the final/ subfolder, lists the fixed-pipeline options, the exact optimizer's routes, the lineups, the role-override
sheet and the H5 side-by-side sheet when present.
"""
import json
import os
from pathlib import Path

ROOT = Path("/home/wescheng/projects/fpl/fpl")
FIRST = Path(__file__).resolve().parent
PACKET = Path(os.environ.get("PACKET_DIR", FIRST))
TARGETS = ("Rice", "Raya", "Gabriel", "Calafiori", "Verbruggen", "Mbeumo", "Thiago", "Tavernier", "N.Jackson", "Rayan", "Van Hecke", "Saka")


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
    milp = read_json(PACKET / "milp_transfers.json") or {}
    lineups = read_json(PACKET / "route_lineups.json") or {}
    now = read_forecasts(PACKET / "forecasts_new_pipeline.jsonl")
    stage = "final" if PACKET != FIRST else "interim"
    before = read_forecasts(FIRST / "forecasts_new_pipeline.jsonl") if stage == "final" else {}
    lines = [f"# GW10 {stage} packet (fixed pipeline)", ""]
    lines.append(f"- **Snapshot:** {manifest.get('retrieved_at_utc', '?')} UTC; deadline {manifest.get('deadline_time', '?')}.")
    if state:
        pending = state.get("pending_transfers") or []
        lines.append(f"- **Entry 6535607:** bank £{state.get('bank')}m, free transfers {state.get('free_transfers')}, "
                     f"chips used: {', '.join(state.get('chips_used') or []) or 'none'}. "
                     f"Transfers already made for GW10: {', '.join(f'{t['out']} → {t['in']}' for t in pending) or 'none'}.")
        lines.append(f"- **Selling prices vs the app values pasted 2026-10-04:** {state.get('selling_price_check')}.")
    squad_ids = [s["player_id"] for s in state.get("squad", [])]
    by_name = {r["name"]: pid for pid, r in now.items()}
    lines += ["", "## Squad and targets as the model sees them", "",
              "| Player | Status | Chance | News | GW10 | GW10–14 | P(appear) | min |", "|---|---|---|---|---|---|---|---|"]
    for pid in squad_ids + [by_name[n] for n in TARGETS if n in by_name and by_name[n] not in squad_ids]:
        r = now.get(pid)
        if r:
            lines.append(f"| {r['name']} | {r['status']} | {r.get('chance') if r.get('chance') is not None else '—'} | "
                         f"{r['news'][:50] or '—'} | {r['p1']:.2f} | {r['p5']:.1f} | {r['papp']:.2f} | {r['mins']:.0f} |")
    if before:
        lines += ["", "## What moved since the interim packet", "",
                  "| Player | Status now | News now | GW10 (interim → now) | GW10–14 (interim → now) |", "|---|---|---|---|---|"]
        for pid in squad_ids + [by_name[n] for n in TARGETS if n in by_name]:
            r, b = now.get(pid), before.get(pid)
            if not r:
                continue
            changed = (not b) or b["status"] != r["status"] or b["news"] != r["news"] or abs(b["p5"] - r["p5"]) >= 0.5
            if changed:
                lines.append(f"| {r['name']} | {r['status']} | {r['news'][:60] or '—'} | "
                             f"{(b or {}).get('p1', float('nan')):.2f} → {r['p1']:.2f} | {(b or {}).get('p5', float('nan')):.1f} → {r['p5']:.1f} |")
    if milp:
        lines += ["", "## Exact optimizer (GW10–14 value vs holding, net of hits)", "",
                  "| Route | Gain | Hit | Bank after | Captain |", "|---|---|---|---|---|"]
        for key, r in milp.items():
            if "squad" in r:
                lines.append(f"| {key.replace('_', ' ')} | {r['net_gain']:+.1f} | — | {r['itb']} | {r['captain']} |")
            else:
                lines.append(f"| {key.replace('_max', ', max ')}: {' + '.join(r['out']) or 'hold'} → {' + '.join(r['in']) or '—'} | "
                             f"{r['net_gain']:+.1f} | {r['hit']} | {r['itb']} | {r['captain']} |")
    if sheet:
        lines += ["", "## Enumerated routes (decision sheet, GW10–14 gain vs holding, net of hits)", "",
                  "| Option | Gain now | If rolled | Bank after |", "|---|---|---|---|"]
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
                         f"GW10 XI forecast {info['gw10_xi_points_incl_captain']} before hits.")
    for extra, title in (("role_override_sheet.md", "Role-override sheet (new signings / role changes the ridge cannot see)"),
                         ("side_by_side_h5.md", "Classic vs classic + SFT (H5), with the text behind each move"),
                         ("f16_shadow.md", "F16 Guardian-lineup shadow (classic+F6+F16, not deciding)")):
        if (PACKET / extra).exists():
            lines += ["", f"## {title}", "", f"See [{extra}]({extra})."]
    lines += ["", "Classic + F6 on the fixed pipeline makes the decision; the SFT arm is logged in shadow. "
              "See ../README.md for how to read the route gains and their uncertainty."]
    (PACKET / "README.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {PACKET / 'README.md'}")


if __name__ == "__main__":
    main()

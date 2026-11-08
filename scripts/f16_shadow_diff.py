#!/usr/bin/env python3
"""F16 live shadow sheet (2026-10-28): classic+F6 (production) vs classic+F6+F16 (team-news table + this week's Guardian
predicted-lineups categories) on the same snapshot. Shows the entry squad with its category and both forecasts, the
largest movers among the top forecasts, and the XI each forecast would pick from the squad (same 0.1-bench/captain
rules as the exact optimizer, no transfers). Decision stays with the production forecast; this is the live evidence
for whether F16 earns a ship.
usage: f16_shadow_diff.py --packet-dir <dir> [--base forecasts_new_pipeline.jsonl] [--shadow forecasts_f16_shadow.jsonl]
         --categories reports/team_news_f16/gn_feat_live_gw9.json --event 9 --out <dir>/f16_shadow.md
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.squad_milp import optimize  # noqa: E402

UNAVAILABLE_MIN_CHANCE = 25


def load(path: Path) -> dict[int, dict]:
    rows = {}
    for line in open(path):
        r = json.loads(line)
        if r["status"] in ("i", "s", "u", "n") and (r.get("chance") is None or float(r["chance"]) < UNAVAILABLE_MIN_CHANCE):
            for k in ("p1", "p3", "p5", "mins", "papp"):
                r[k] = 0.0
        rows[int(r["player_id"])] = r
    return rows


def pick(F: dict[int, dict], state: dict, key: str) -> dict:
    sell = {int(s["player_id"]): float(s["selling_price"]) for s in state["squad"]}
    value = {pid: float(r[key]) for pid, r in F.items()}
    return optimize(F, value, sell, bank=float(state["bank"]), free_transfers=int(state["free_transfers"]), max_transfers=0)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--packet-dir", required=True)
    ap.add_argument("--base", default="forecasts_new_pipeline.jsonl")
    ap.add_argument("--shadow", default="forecasts_f16_shadow.jsonl")
    ap.add_argument("--categories", required=True)
    ap.add_argument("--event", type=int, required=True)
    ap.add_argument("--season", default="2026-27")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    P = Path(args.packet_dir)
    base, shadow = load(P / args.base), load(P / args.shadow)
    state = json.loads((P / "entry_state.json").read_text())
    try:
        cats = json.loads(Path(args.categories).read_text())
    except (OSError, ValueError):
        cats = {}
    cat = lambda pid: cats.get(f"{args.season}|{args.event}|{pid}", "no article")  # noqa: E731
    lines = [f"# F16 live shadow, GW{args.event}", "",
             f"Categories file: {args.categories} ({len(cats)} players; {'EMPTY: no predicted-lineups article yet, the shadow is the no-article model' if not cats else 'article present'}).",
             "Base = classic+F6 (decides). Shadow = classic+F6+F16 with the live Guardian categories. Out/suspended players zeroed in both.", "",
             "## Entry squad", "", "| Player | Pos | Guardian | base GW / 5GW / mins / P | shadow GW / 5GW / mins / P | Δ GW | Δ 5GW |", "|---|---|---|---|---|---|---|"]
    for s in state["squad"]:
        pid = int(s["player_id"]); b, h = base.get(pid), shadow.get(pid)
        if not b or not h:
            continue
        lines.append(f"| {b['name']} | {b['pos']} | {cat(pid)} | {b['p1']:.2f} / {b['p5']:.1f} / {b['mins']:.0f} / {b['papp']:.2f} | "
                     f"{h['p1']:.2f} / {h['p5']:.1f} / {h['mins']:.0f} / {h['papp']:.2f} | {h['p1'] - b['p1']:+.2f} | {h['p5'] - b['p5']:+.1f} |")
    xb, xh = pick(base, state, "p1"), pick(shadow, state, "p1")
    nb = {pid: base[pid]["name"] for pid in base}
    lines += ["", f"XI (base, {xb['net']:.1f}): {', '.join(nb[p] for p in xb['xi'])}; C {nb[xb['captain']]}",
              f"XI (shadow, {xh['net']:.1f}): {', '.join(nb[p] for p in xh['xi'])}; C {nb[xh['captain']]}",
              "XI differences: " + (", ".join(sorted({nb[p] for p in set(xb['xi']) ^ set(xh['xi'])})) or "none"), ""]
    top = sorted((pid for pid in base if pid in shadow), key=lambda p: -max(base[p]["p1"], shadow[p]["p1"]))[:150]
    movers = sorted(top, key=lambda p: -abs(shadow[p]["p1"] - base[p]["p1"]))[:25]
    lines += ["## Largest movers among the top 150 forecasts", "", "| Player | Pos | Guardian | base GW | shadow GW | Δ GW | Δ mins | status |", "|---|---|---|---|---|---|---|---|"]
    for pid in movers:
        b, h = base[pid], shadow[pid]
        lines.append(f"| {b['name']} | {b['pos']} | {cat(pid)} | {b['p1']:.2f} | {h['p1']:.2f} | {h['p1'] - b['p1']:+.2f} | {h['mins'] - b['mins']:+.1f} | {b['status']}/{b.get('chance')} |")
    import collections
    agg = collections.defaultdict(list)
    for pid in top:
        agg[cat(pid)].append(shadow[pid]["p1"] - base[pid]["p1"])
    lines += ["", "Mean Δ GW by category (top 150): " + "; ".join(f"{k} {sum(v) / len(v):+.3f} (n {len(v)})" for k, v in sorted(agg.items()))]
    Path(args.out).write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

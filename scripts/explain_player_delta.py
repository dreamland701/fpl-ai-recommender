#!/usr/bin/env python3
"""Explain WHY the adapter moved a player: evidence in, delta out.

The GW4 2026-27 Calafiori case took an hour to diagnose by hand (he looked
"unfairly" cut vs other Arsenal defenders; the model had actually read a
substitution report and pinned his minutes delta to the bound). This makes
that a 30-second check, and it belongs in the weekly routine whenever a
forecast looks wrong.

  python3 scripts/explain_player_delta.py --examples ... --predictions ... --player Calafiori
  python3 scripts/explain_player_delta.py ... --position DEF --top 12   # scan a position
"""
from __future__ import annotations
import argparse, json, re

def load(examples, predictions):
    ex = [json.loads(l) for l in open(examples)]
    pr = [json.loads(l) for l in open(predictions)]
    out = []
    for e, p in zip(ex, pr):
        md = e["metadata"]; bf = md["baseline_forecast"]
        try: d = json.loads((p.get("response") or "").strip())
        except Exception: d = {}
        out.append({
            "name": md["player_name"], "pos": md["position"], "prompt": e["prompt"],
            "c1": bf["baseline_points_1gw"], "c5": bf["baseline_points_5gw"],
            "cmin": bf["baseline_minutes_1gw"], "capp": bf["baseline_appearance_probability"],
            "d": d,
        })
    return out

def evidence_block(prompt: str, max_chars: int) -> str:
    i = prompt.find("Timestamp-safe text evidence")
    if i < 0: return "   (no timestamp-safe evidence attached)"
    block = prompt[i:].split("<|turn>")[0]
    return "\n".join("   " + ln for ln in block.splitlines()[1:] if ln.strip())[:max_chars]

def show(r, max_chars):
    d = r["d"]
    g = lambda k: float(d.get(k) or 0.0)
    print(f"\n=== {r['name']}  ({r['pos']}) ===")
    print(f"  classic : 1gw {r['c1']:.2f}  5gw {r['c5']:.2f}  minutes {r['cmin']:.0f}  P(app) {r['capp']:.2f}")
    print(f"  delta   : 1gw {g('delta_points_1gw'):+.2f}  5gw {g('delta_points_5gw'):+.2f}  "
          f"minutes {g('delta_minutes_1gw'):+.0f}  P(app) {g('delta_appearance_probability'):+.2f}")
    print(f"  final   : 1gw {max(0, r['c1']+g('delta_points_1gw')):.2f}  5gw {max(0, r['c5']+g('delta_points_5gw')):.2f}")
    flags = []
    if abs(g("delta_minutes_1gw")) >= 20: flags.append("MINUTES DELTA AT BOUND -> model sees a rotation/injury signal")
    if abs(g("delta_appearance_probability")) >= 0.25: flags.append("P(APP) DELTA AT BOUND")
    if g("delta_points_1gw") <= -1.0: flags.append("large points downgrade")
    if g("delta_points_1gw") >= 1.0: flags.append("large points upgrade")
    for f in flags: print(f"  !! {f}")
    print("  evidence the model read:")
    print(evidence_block(r["prompt"], max_chars))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--examples", required=True); ap.add_argument("--predictions", required=True)
    ap.add_argument("--player", action="append", default=[])
    ap.add_argument("--position"); ap.add_argument("--top", type=int, default=0)
    ap.add_argument("--max-evidence-chars", type=int, default=1200)
    a = ap.parse_args()
    rows = load(a.examples, a.predictions)
    picked = [r for r in rows if r["name"] in a.player] if a.player else []
    if a.position or a.top:
        pool = [r for r in rows if not a.position or r["pos"] == a.position]
        pool.sort(key=lambda r: -abs(float(r["d"].get("delta_points_1gw") or 0)))
        picked += [r for r in pool[: a.top or 10] if r not in picked]
    if not picked:
        print("no players matched"); return
    for r in picked: show(r, a.max_evidence_chars)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Standing premium-calibration report (the Haaland-exclusion metric).

Two modes, both cheap enough to run every week as a gate alongside the
evidence audit:

  --mode eval   price-band table (classic / +adapter / realized) from an
                eval-rows JSON + its eval.jsonl, prices joined from the
                training table. This is the table that surfaced the
                premium band realizing 5.64 pts/GW against a 4.07
                prediction on the E11 GW35-38 holdout.

  --mode live   top-K adjusted ranking for a live week's examples +
                predictions, reporting where every premium (>=8.5) sits.
                GW2 2026-27: Haaland ranked 43rd — this mode makes that
                visible BEFORE the deadline, not after the haul.
"""
from __future__ import annotations

import argparse
import csv
import json
import statistics
from collections import defaultdict

BANDS = ((0.0, 5.0, "budget <5.0"), (5.0, 6.5, "mid 5.0-6.4"), (6.5, 8.5, "upper 6.5-8.4"),
         (8.5, 11.5, "premium 8.5-11.4"), (11.5, 99.0, "elite 11.5+"))


def band_label(price: float) -> str | None:
    for lo, hi, label in BANDS:
        if lo <= price < hi:
            return label
    return None


def mode_eval(args) -> None:
    ev = [json.loads(l) for l in open(args.examples)]
    rows = json.load(open(args.rows))["sft_rows"]
    price = {}
    for r in csv.DictReader(open(args.training_data)):
        try:
            price[(r["season"], int(float(r["player_id"])), int(float(r["week"])))] = float(r["price"])
        except (ValueError, KeyError):
            continue
    agg = defaultdict(lambda: {"base": [], "final": [], "tgt": []})
    for e, r in zip(ev, rows):
        md = e["metadata"]
        p = price.get((md["season"], md["player_id"], md["week"]))
        tgt = r.get("target_points_1gw")
        if p is None or tgt is None:
            continue
        label = band_label(p)
        if label is None:
            continue
        agg[label]["base"].append(r["baseline_points_1gw"])
        agg[label]["final"].append(r["final_points_1gw"])
        agg[label]["tgt"].append(tgt)
    print(f"{'price band':18s} {'n':>4s} {'classic':>8s} {'+adapter':>8s} {'realized':>8s} {'class gap':>9s} {'adpt gap':>8s}")
    for _, _, label in BANDS:
        a = agg[label]
        n = len(a["tgt"])
        if not n:
            continue
        base, final, tgt = (statistics.mean(a[k]) for k in ("base", "final", "tgt"))
        print(f"{label:18s} {n:4d} {base:8.2f} {final:8.2f} {tgt:8.2f} {base - tgt:+9.2f} {final - tgt:+8.2f}")


def mode_live(args) -> None:
    ex = [json.loads(l) for l in open(args.examples)]
    pr = [json.loads(l) for l in open(args.predictions)]
    boot = json.load(open(args.bootstrap_json))
    price = {int(e["id"]): e["now_cost"] / 10.0 for e in boot["elements"]}
    ranked = []
    for e, p in zip(ex, pr):
        md = e["metadata"]
        bf = md["baseline_forecast"]
        try:
            d = json.loads((p.get("response") or "").strip())
        except Exception:
            d = {}
        f1 = max(0.0, bf["baseline_points_1gw"] + float(d.get("delta_points_1gw") or 0))
        f3 = max(0.0, bf["baseline_points_3gw"] + float(d.get("delta_points_3gw") or 0))
        f5 = max(0.0, bf["baseline_points_5gw"] + float(d.get("delta_points_5gw") or 0))
        blend = f5 + 0.6 * f3 + 0.35 * f1
        ranked.append((blend, md["player_name"], md["position"], price.get(md["player_id"], 0.0), f1))
    ranked.sort(reverse=True)
    # Position-aware premium thresholds: no defender reaches £8.5, so a
    # flat cutoff made the alarm blind to elite DEFs (Gabriel £8.0 ranked
    # 29th among DEFs in GW2 2026-27 while being FPL's top defender).
    PREMIUM_MIN = {"GK": 5.5, "DEF": 5.5, "MID": 8.5, "FWD": 8.5}
    premiums = [
        (i + 1, r) for i, r in enumerate(ranked) if r[3] >= PREMIUM_MIN.get(r[2], 8.5)
    ]
    print(f"premium (>=8.5) count: {len(premiums)} | ranks: {[i for i, _ in premiums[:12]]}")
    worst = [i for i, _ in premiums[:6] if i > args.premium_rank_alarm]
    for i, (blend, name, pos, pz, f1) in premiums[:12]:
        flag = "  <-- ALARM" if i > args.premium_rank_alarm else ""
        print(f"  rank {i:3d}: {name:16s} {pos:3s} £{pz:4.1f} 1gw {f1:.2f} blend {blend:.1f}{flag}")
    if worst:
        print(f"ALARM: {len(worst)} of the top-6 premiums rank below {args.premium_rank_alarm} — check band calibration before shipping the sheet")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["eval", "live"], required=True)
    parser.add_argument("--examples", required=True)
    parser.add_argument("--rows", help="eval mode: eval-rows JSON")
    parser.add_argument("--training-data", default="data/fpl_training_rows.csv")
    parser.add_argument("--predictions", help="live mode: decode JSONL")
    parser.add_argument("--bootstrap-json", help="live mode: cached bootstrap")
    parser.add_argument("--premium-rank-alarm", type=int, default=25)
    args = parser.parse_args()
    if args.mode == "eval":
        mode_eval(args)
    else:
        mode_live(args)


if __name__ == "__main__":
    main()

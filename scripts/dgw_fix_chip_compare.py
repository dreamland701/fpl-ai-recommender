#!/usr/bin/env python3
"""Closed-loop half-season totals: standard forecasts (reports/chip_timing) vs the per-fixture variant
(reports/dgw_fix/chip_timing_pf). Same actual points and starting squads; only the forecasts differ, so the
planner column is the decision value of the fix over a whole half (transfers, captain and chips together).

usage: dgw_fix_chip_compare.py [--out reports/dgw_fix/chip_tables.md]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HALVES = [f"{s}:{h}" for s in ("2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26") for h in (1, 2)]


def doubles(d):
    base = next((t for t in d["trajectories"] if t["wc"] is None and t["fh"] is None), None)
    return [w["week"] for w in base["weeks"] if w["league_double"][0] >= 0.2] if base else []


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default=str(ROOT / "reports" / "chip_timing"))
    ap.add_argument("--variant", default=str(ROOT / "reports" / "dgw_fix" / "chip_timing_pf"))
    ap.add_argument("--out", default=str(ROOT / "reports" / "dgw_fix" / "chip_tables.md"))
    args = ap.parse_args()
    lines = ["# Double-gameweek fix: closed-loop half-season totals", "",
             "Planner = disciplined auto transfer + the 5-week chip rule, closed loop over the half. Chips = (week, chip) the planner played. "
             "Hindsight = best chip weeks knowing outcomes (TC+BB only / all four). DGW = weeks with >=20% of players doubling.", "",
             "| half | DGW weeks | planner base | planner fix | Δ | no-chips base | no-chips fix | base chips | fix chips | hindsight TC+BB base / fix | hindsight all base / fix |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    deltas = []
    for item in HALVES:
        season, half = item.split(":")
        pb, pv = Path(args.base) / f"{season}_h{half}.json", Path(args.variant) / f"{season}_h{half}.json"
        if not pb.exists():
            continue
        b = json.load(open(pb)); cb = b["ceilings"]
        if not pv.exists():
            lines.append(f"| {item} | {doubles(b)} | {cb['planner']:.0f} | pending | | {cb['no_chips']:.0f} | | {cb['planner_chips']} | | {cb['hindsight_tc_bb_only']:.0f} / | {cb['hindsight_all_chips']:.0f} / |")
            continue
        v = json.load(open(pv)); cv = v["ceilings"]
        deltas.append((cv["planner"] - cb["planner"], cv["no_chips"] - cb["no_chips"]))
        lines.append(f"| {item} | {doubles(b)} | {cb['planner']:.0f} | {cv['planner']:.0f} | {cv['planner'] - cb['planner']:+.0f} | "
                     f"{cb['no_chips']:.0f} | {cv['no_chips']:.0f} | {cb['planner_chips']} | {cv['planner_chips']} | "
                     f"{cb['hindsight_tc_bb_only']:.0f} / {cv['hindsight_tc_bb_only']:.0f} | {cb['hindsight_all_chips']:.0f} / {cv['hindsight_all_chips']:.0f} |")
    # TC + BB value, additive on the no-chip trajectory (captain_points at the TC week + bench_extra at the BB
    # week): the planner's 5-week rule vs the schedule rule (TC in the biggest double, BB in the next biggest,
    # otherwise the planner's week) vs hindsight. Shows whether the fixed forecasts move the chips into the doubles.
    lines += ["", "## Triple captain + bench boost, additive on the no-chip path", "",
              "| half | variant | planner weeks | planner TC+BB | schedule-rule weeks | schedule-rule TC+BB | hindsight TC+BB |", "|---|---|---|---|---|---|---|"]
    for item in HALVES:
        season, half = item.split(":")
        for name, root in (("base", args.base), ("fix", args.variant)):
            path = Path(root) / f"{season}_h{half}.json"
            if not path.exists():
                continue
            d = json.load(open(path))
            base = next(t for t in d["trajectories"] if t["wc"] is None and t["fh"] is None)
            weeks = {w["week"]: w for w in base["weeks"]}
            chips = dict((c, w) for w, c in d["ceilings"]["planner_chips"])
            tc, bb = chips.get("triple_captain"), chips.get("bench_boost")
            planner_gain = (weeks[tc]["captain_points"] if tc in weeks else 0) + (weeks[bb]["bench_extra"] if bb in weeks else 0)
            dbl = sorted(((w["league_double"][0], w["week"]) for w in base["weeks"] if w["league_double"][0] >= 0.2), reverse=True)
            r_tc = dbl[0][1] if dbl else tc
            r_bb = dbl[1][1] if len(dbl) > 1 else (bb if bb != r_tc else tc)
            rule_gain = (weeks[r_tc]["captain_points"] if r_tc in weeks else 0) + (weeks[r_bb]["bench_extra"] if r_bb in weeks else 0)
            best = max((a["captain_points"] + b["bench_extra"] for a in base["weeks"] for b in base["weeks"] if a["week"] != b["week"]), default=0)
            lines.append(f"| {item} | {name} | TC {tc}, BB {bb} | {planner_gain:.0f} | TC {r_tc}, BB {r_bb} | {rule_gain:.0f} | {best:.0f} |")
    if deltas:
        n = len(deltas)
        lines += ["", f"Halves built: {n}. Planner Δ total {sum(d[0] for d in deltas):+.0f} (mean {sum(d[0] for d in deltas) / n:+.1f}, "
                  f"{sum(1 for d in deltas if d[0] > 0)} up / {sum(1 for d in deltas if d[0] < 0)} down); "
                  f"no-chips Δ total {sum(d[1] for d in deltas):+.0f} (transfers + captain only)."]
    out = "\n".join(lines) + "\n"
    Path(args.out).write_text(out)
    print(out)


if __name__ == "__main__":
    main()

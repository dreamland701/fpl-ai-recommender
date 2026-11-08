#!/usr/bin/env python3
"""Double-gameweek forecast calibration: standard states vs a forecast variant (2026-10-13).

For every double gameweek in the chip-timing states (>=20% of forecast rows with two fixtures) and,
for scale, every normal week: regular starters (>=60 predicted minutes in the previous week's
standard forecast, same set for both variants) split by this week's fixture count. Reports
P(appear), forecast p1 and realised points, and the forecast-best captain's forecast vs actual.

usage: dgw_calibration.py [--variant reports/dgw_fix/states_pf] [--out reports/dgw_fix/calibration.md]
"""
from __future__ import annotations

import argparse
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.grpo_env import load_states  # noqa: E402

KEYS = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26-train", "2025-26-holdout"]


def m(x):
    return st.mean(x) if x else float("nan")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default=str(ROOT / "reports" / "grpo_states_v2"))
    ap.add_argument("--variant", default=str(ROOT / "reports" / "dgw_fix" / "states_pf"))
    ap.add_argument("--out", default=str(ROOT / "reports" / "dgw_fix" / "calibration.md"))
    args = ap.parse_args()
    rows = []  # (season, week, kind(x2/x1/normal), variant, papp, p1, actual)
    caps = []  # (season, week, double?, variant, cap p1, cap actual)
    for key in KEYS:
        base = {s.week: s for s in load_states(Path(args.base) / f"{key}.jsonl")}
        var = {s.week: s for s in load_states(Path(args.variant) / f"{key}.jsonl")}
        for w in sorted(base):
            if w - 1 not in base or w not in var:
                continue
            prev = {f.player_id: f for f in base[w - 1].forecasts}
            regular = {pid for pid, f in prev.items() if f.predicted_minutes >= 60 and f.fixture_count == 1}
            fc = base[w].forecasts
            double_week = sum(1 for f in fc if f.fixture_count == 2) >= 0.2 * len(fc)
            for name, s in (("base", base[w]), ("fix", var[w])):
                for f in s.forecasts:
                    if f.player_id not in regular or f.fixture_count not in (1, 2):
                        continue
                    kind = ("x2" if f.fixture_count == 2 else "x1") if double_week else "normal"
                    rows.append((key, w, kind, name, f.appearance_probability, f.predicted_points_1gw, s.actual_points.get(f.player_id, 0.0)))
                cap = max(s.forecasts, key=lambda f: f.predicted_points_1gw)
                caps.append((key, w, double_week, name, cap.predicted_points_1gw, s.actual_points.get(cap.player_id, 0.0), cap.fixture_count))
    lines = ["# Double-gameweek calibration: standard forecasts vs per-fixture heads", "",
             f"Regular starters (>=60 predicted minutes the week before, single fixture then). Variant: `{args.variant}`.", "",
             "| rows | variant | n | P(appear) | forecast p1 | actual | forecast − actual |", "|---|---|---|---|---|---|---|"]
    for kind in ("x2", "x1", "normal"):
        for name in ("base", "fix"):
            r = [x for x in rows if x[2] == kind and x[3] == name]
            lines.append(f"| {'doublers in a DGW' if kind == 'x2' else 'singles in a DGW' if kind == 'x1' else 'normal weeks'} | {name} | {len(r)} | "
                         f"{m([x[4] for x in r]):.2f} | {m([x[5] for x in r]):.2f} | {m([x[6] for x in r]):.2f} | {m([x[5] - x[6] for x in r]):+.2f} |")
    lines += ["", "## Forecast-best captain", "", "| weeks | variant | n | captain forecast | captain actual | doubles chosen |", "|---|---|---|---|---|---|"]
    for dbl in (True, False):
        for name in ("base", "fix"):
            c = [x for x in caps if x[2] == dbl and x[3] == name]
            lines.append(f"| {'double gameweeks' if dbl else 'normal weeks'} | {name} | {len(c)} | {m([x[4] for x in c]):.2f} | {m([x[5] for x in c]):.2f} | "
                         f"{sum(1 for x in c if x[6] == 2)} |")
    lines += ["", "## Per double gameweek (doublers)", "", "| season | GW | variant | n | P(appear) | forecast | actual |", "|---|---|---|---|---|---|---|"]
    for key, w in sorted({(x[0], x[1]) for x in rows if x[2] == "x2"}):
        for name in ("base", "fix"):
            r = [x for x in rows if x[0] == key and x[1] == w and x[2] == "x2" and x[3] == name]
            lines.append(f"| {key} | {w} | {name} | {len(r)} | {m([x[4] for x in r]):.2f} | {m([x[5] for x in r]):.2f} | {m([x[6] for x in r]):.2f} |")
    out = "\n".join(lines) + "\n"
    Path(args.out).write_text(out)
    print(out)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Per-window table for the double-gameweek fix backtests (scripts/run_dgw_fix_backtests.sh) against the
fixed classic+F6 baseline (reports/review_fixes_2026_10/bt, config N_F). Paired deltas with t statistics.

usage: dgw_fix_summary.py [--out reports/dgw_fix/backtest.md]
"""
from __future__ import annotations

import argparse
import json
import math
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reports" / "review_fixes_2026_10" / "bt"
VAR = ROOT / "reports" / "dgw_fix" / "bt"
WINDOWS = [("2025-26", a, a + 3) for a in (2, 6, 10, 14, 18, 22, 27, 31, 35)] + \
          [(s, a, a + 3) for s in ("2023-24", "2024-25") for a in (12, 16, 20, 24, 28, 32)]


def total(path: Path):
    if not path.exists():
        return None
    d = json.loads(path.read_text())
    return d["total_actual_points"], d["total_transfer_hits"], sum(1 for w in d["weeks"] if w.get("chip_used"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--configs", nargs="*", default=["P_F", "A_F"])
    ap.add_argument("--out", default=str(ROOT / "reports" / "dgw_fix" / "backtest.md"))
    args = ap.parse_args()
    lines = ["# Double-gameweek fix: 21-window decision backtest", "",
             "Baseline N_F = fixed classic+F6 (flags off). P_F = FPL_PER_FIXTURE=1 (per-fixture minutes/1GW heads + P(appear) fix). "
             "A_F = FPL_DGW_PAPP=1 (P(appear) fix only). Points = realised squad points over the 4-week window.", "",
             "| window | N_F | " + " | ".join(f"{c} | Δ" for c in args.configs) + " |", "|---|---|" + "---|---|" * len(args.configs)]
    deltas = {c: [] for c in args.configs}
    for season, a, b in WINDOWS:
        base = total(BASE / f"N_F_{season}_{a}_{b}" / "rolling_squad_backtest.json")
        cells = [f"{season} GW{a}-{b}", f"{base[0]:.0f}" if base else "?"]
        for c in args.configs:
            v = total(VAR / f"{c}_{season}_{a}_{b}" / "rolling_squad_backtest.json")
            if v and base:
                deltas[c].append(v[0] - base[0])
                cells += [f"{v[0]:.0f}", f"{v[0] - base[0]:+.0f}"]
            else:
                cells += ["pending", ""]
        lines.append("| " + " | ".join(cells) + " |")
    lines += ["", "| config | windows | total Δ | mean Δ | sd | t | wins / ties / losses |", "|---|---|---|---|---|---|---|"]
    for c in args.configs:
        d = deltas[c]
        if len(d) >= 2:
            sd = st.stdev(d); t = st.mean(d) / (sd / math.sqrt(len(d))) if sd else float("inf")
            lines.append(f"| {c} | {len(d)} | {sum(d):+.0f} | {st.mean(d):+.1f} | {sd:.1f} | {t:.2f} | "
                         f"{sum(1 for x in d if x > 0)} / {sum(1 for x in d if x == 0)} / {sum(1 for x in d if x < 0)} |")
    out = "\n".join(lines) + "\n"
    Path(args.out).write_text(out)
    print(out)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Paired per-window comparison of decision-backtest configs on the 21-window bench.

usage: bt_compare.py --base-dir reports/dgw_fix/bt --base MP1_F --var-dir reports/market_f14/bt --configs MK1_F \
                     [--out reports/market_f14/backtest.md] [--title "..."]
"""
from __future__ import annotations

import argparse
import json
import math
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WINDOWS = [("2025-26", a, a + 3) for a in (2, 6, 10, 14, 18, 22, 27, 31, 35)] + \
          [(s, a, a + 3) for s in ("2023-24", "2024-25") for a in (12, 16, 20, 24, 28, 32)]


def total(path: Path):
    if not path.exists():
        return None
    d = json.loads(path.read_text())
    return d["total_actual_points"], d["total_transfer_hits"], sum(1 for w in d["weeks"] if w.get("chip_used"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base-dir", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--var-dir", required=True)
    ap.add_argument("--configs", nargs="+", required=True)
    ap.add_argument("--out")
    ap.add_argument("--title", default="Decision backtest, 21 windows")
    args = ap.parse_args()
    base_dir, var_dir = ROOT / args.base_dir, ROOT / args.var_dir
    lines = [f"# {args.title}", "", f"Baseline {args.base} ({args.base_dir}); variants in {args.var_dir}. Points = realised squad points over the 4-week window.", "",
             f"| window | {args.base} | " + " | ".join(f"{c} | Δ" for c in args.configs) + " |", "|---|---|" + "---|---|" * len(args.configs)]
    deltas = {c: [] for c in args.configs}
    for season, a, b in WINDOWS:
        base = total(base_dir / f"{args.base}_{season}_{a}_{b}" / "rolling_squad_backtest.json")
        cells = [f"{season} GW{a}-{b}", f"{base[0]:.0f}" if base else "?"]
        for c in args.configs:
            v = total(var_dir / f"{c}_{season}_{a}_{b}" / "rolling_squad_backtest.json")
            if v and base:
                deltas[c].append(v[0] - base[0]); cells += [f"{v[0]:.0f}", f"{v[0] - base[0]:+.0f}"]
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
    if args.out:
        Path(args.out).write_text(out)
    print(out)


if __name__ == "__main__":
    main()

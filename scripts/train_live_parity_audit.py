#!/usr/bin/env python3
"""Train/live feature parity audit (2026-10-14).

The two decision wins of the last three weeks were pipeline bugs, and the worst of them (ownership
in percent live vs counts in training) could not be seen in any backtest because only the LIVE frame
was wrong. This audit builds the live frame exactly as the weekly refresh does and compares every
model feature's distribution against the training rows of the same gameweek in past seasons. A
feature whose live median sits outside the historical interquartile range, whose zero-share jumps,
or whose scale differs by more than 2x is flagged for a human look.

usage: FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 PYTHONPATH=src python scripts/train_live_parity_audit.py \
         --deadline-ts 2026-10-17T10:00:00Z --training-data data/fpl_training_rows_v3_contract_f6.csv \
         --seasons 2023-24 2024-25 2025-26 --out reports/gw7_packet_2026_10/parity_audit.md
"""
from __future__ import annotations

import argparse
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.api import OfficialSnapshotService  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402


def stats(values: pd.Series) -> dict:
    v = pd.to_numeric(values, errors="coerce")
    return {"n": int(v.notna().sum()), "nan": float(v.isna().mean()), "zero": float((v.fillna(0) == 0).mean()),
            "mean": float(v.mean()), "p10": float(v.quantile(0.1)), "median": float(v.median()),
            "p90": float(v.quantile(0.9)), "q1": float(v.quantile(0.25)), "q3": float(v.quantile(0.75))}


def flag(live: dict, hist: dict) -> str:
    reasons = []
    iqr = hist["q3"] - hist["q1"]
    if iqr > 0 and not (hist["q1"] - iqr <= live["median"] <= hist["q3"] + iqr):
        reasons.append("median outside hist IQR±1")
    if abs(live["zero"] - hist["zero"]) > 0.25:
        reasons.append(f"zero share {live['zero']:.2f} vs {hist['zero']:.2f}")
    if hist["mean"] != 0 and live["mean"] != 0 and not (0.5 <= abs(live["mean"] / hist["mean"]) <= 2.0):
        reasons.append(f"mean ratio {live['mean'] / hist['mean']:.2f}")
    if live["nan"] > 0.05:
        reasons.append(f"nan share {live['nan']:.2f}")
    return "; ".join(reasons)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--deadline-ts", required=True)
    ap.add_argument("--training-data", default="data/fpl_training_rows_v3_contract_f6.csv")
    ap.add_argument("--history-root", default="data/fpl_history")
    ap.add_argument("--seasons", nargs="+", default=["2023-24", "2024-25", "2025-26"])
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    dataset = CanonicalDataset.from_csv(args.training_data)
    official = OfficialSnapshotService().build_current_week_frame(args.deadline_ts)
    live = dataset.build_live_week_frame(official, history_root=args.history_root)
    week = int(pd.to_numeric(live["week"], errors="coerce").mode().iloc[0])
    hist = dataset.training_frame
    hist = hist[hist["season"].isin(args.seasons) & (hist["week"] == week)]
    lines = [f"# Train/live parity audit: live GW{week} ({args.deadline_ts}) vs GW{week} of {', '.join(args.seasons)}", "",
             f"Live rows {len(live)}; historical rows {len(hist)}. Subsets: all players, and regulars (minutes_avg_5 > 45).", ""]
    flagged_total = 0
    for subset_name, live_mask, hist_mask in (
            ("all players", pd.Series(True, index=live.index), pd.Series(True, index=hist.index)),
            ("regulars", pd.to_numeric(live["minutes_avg_5"], errors="coerce") > 45, pd.to_numeric(hist["minutes_avg_5"], errors="coerce") > 45)):
        lines += [f"## {subset_name} (live n {int(live_mask.sum())}, hist n {int(hist_mask.sum())})", "",
                  "| feature | live median | hist median | live mean | hist mean | live zero | hist zero | flag |", "|---|---|---|---|---|---|---|---|"]
        for column in dataset.feature_columns:
            if column not in live.columns or column not in hist.columns:
                lines.append(f"| {column} | missing | | | | | | MISSING |"); flagged_total += 1
                continue
            l, h = stats(live.loc[live_mask, column]), stats(hist.loc[hist_mask, column])
            f = flag(l, h)
            flagged_total += bool(f)
            lines.append(f"| {column} | {l['median']:.3f} | {h['median']:.3f} | {l['mean']:.3f} | {h['mean']:.3f} | "
                         f"{l['zero']:.2f} | {h['zero']:.2f} | {('**' + f + '**') if f else ''} |")
        lines.append("")
    lines.append(f"Flags: {flagged_total} (a flag is a prompt to look, not a verdict; schedule-driven features legitimately differ by week).")
    Path(args.out).write_text("\n".join(lines) + "\n")
    print("\n".join(l for l in lines if "**" in l or l.startswith("#") or l.startswith("Flags")))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Attach defensive-contribution context to each corpus row.

Spot-checked 2026-08-21: DefCon was structurally INVISIBLE to the
forecast adapter — no numeric DefCon input anywhere in the prompt and
only 0.6% of training rows even mention tackles/clearances in evidence
text. Both E9 and E10 are measurably WORSE than classic on DefCon-bonus
weeks (−0.30 / −0.42 MAE) — the model can't adjust for a scoring
mechanism it can't see. This adds `metadata.defcon` per row from the
canonical training table:

  {"avg_3": float, "avg_5": float, "tracked": bool}

avg_* are the player's lagged per-GW defensive-contribution counts
(timestamp-safe pre-deadline features). tracked=False for 2022-24 rows —
the stat didn't exist before 2025-26, and the split builder renders
nothing in that case (absence == pre-DefCon era, matching reality).

Usage:
  PYTHONPATH=src python3 scripts/attach_defcon_to_corpus.py \
    --corpus <corpus>.jsonl --training-data data/fpl_training_rows.csv \
    --output <corpus>_defcon.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pandas as pd  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--training-data", default="data/fpl_training_rows.csv")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    frame = pd.read_csv(
        args.training_data,
        usecols=["season", "week", "player_id", "defensive_contribution_avg_3",
                 "defensive_contribution_avg_5", "defensive_data_source_available"],
        low_memory=False,
    )
    lookup = {
        (str(r.season), int(r.week), int(r.player_id)): (
            float(r.defensive_contribution_avg_3),
            float(r.defensive_contribution_avg_5),
            bool(r.defensive_data_source_available),
        )
        for r in frame.itertuples()
    }

    attached = missing = 0
    with Path(args.corpus).open() as src, Path(args.output).open("w") as dst:
        for line in src:
            row = json.loads(line)
            md = row["metadata"]
            key = (str(md["season"]), int(md["week"]), int(md["player_id"]))
            hit = lookup.get(key)
            if hit:
                avg3, avg5, tracked = hit
                md["defcon"] = {"avg_3": round(avg3, 1), "avg_5": round(avg5, 1), "tracked": tracked}
                attached += 1
            else:
                missing += 1
            dst.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"done: defcon attached {attached}, missing {missing} -> {args.output}")


if __name__ == "__main__":
    main()

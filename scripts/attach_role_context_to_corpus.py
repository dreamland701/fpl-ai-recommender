#!/usr/bin/env python3
"""Attach per-row role context: recent starting pattern vs usual role.

The baseline decomposition shows *how much* the minutes component contributes;
this layer shows *why* — is the player a nailed starter, or starting lately
only because a regular is absent? Short-window (3 GW) vs long-window (8 GW)
appearance and 60-minute rates expose "recently promoted" and "losing role"
patterns, letting the LLM reason about role fragility (e.g., a returning
starter reclaiming the spot after injury or international duty).

All values are lagged pre-deadline features from the canonical dataset —
timestamp-safe by construction.

Usage:
  python3 scripts/attach_role_context_to_corpus.py \
    --corpus reports/<corpus>.jsonl \
    --training-data data/fpl_training_rows.csv \
    --output reports/<corpus>_role.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fpl_ai.dataset import CanonicalDataset  # noqa: E402

ROLE_FEATURES = {
    "appearance_rate_3": "app_3",
    "appearance_rate_8": "app_8",
    "played_60_rate_3": "p60_3",
    "played_60_rate_8": "p60_8",
    "minutes_avg_3": "minutes_3",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--training-data", default="data/fpl_training_rows.csv")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    dataset = CanonicalDataset.from_csv(args.training_data)
    frame = dataset.training_frame
    lookup: dict[tuple[str, int, int], dict[str, float]] = {}
    columns = [column for column in ROLE_FEATURES if column in frame.columns]
    for record in frame[["season", "week", "player_id", *columns]].to_dict(orient="records"):
        lookup[(str(record["season"]), int(record["week"]), int(record["player_id"]))] = {
            ROLE_FEATURES[column]: round(float(record[column] or 0.0), 2) for column in columns
        }

    rows_written = 0
    rows_with_role = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.corpus.open() as corpus_handle, args.output.open("w") as output_handle:
        for line in corpus_handle:
            row = json.loads(line)
            metadata = row["metadata"]
            key = (str(row["season"]), int(row["week"]), int(metadata.get("player_id") or 0))
            role = lookup.get(key)
            if role:
                metadata["role_context"] = role
                rows_with_role += 1
            output_handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            rows_written += 1

    print(f"done: {rows_written} rows -> {args.output} (with role context: {rows_with_role})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Attach an exact per-row decomposition of the classic 1GW baseline.

The classic forecaster is ridge regression, so each prediction is exactly
`intercept + sum(coef_i * (x_i - mean_i) / scale_i)`. This script re-runs the
corpus's rolling protocol (fit on strictly-prior weeks, alpha 1.0 — identical
to llm_data.build_multiseason_player_forecast_examples) and stores grouped
feature contributions per row as `metadata.baseline_decomposition`, so the
residual-SFT prompt can show the model *why* the base is high or low and let
the text evidence model the residual against it.

Each row's group contributions sum (with the intercept) back to the stored
`baseline_points_1gw`; rows where the recomputed prediction drifts more than
0.02 from the stored baseline are counted and reported.

Usage:
  python3 scripts/attach_baseline_decomposition_to_corpus.py \
    --corpus reports/<corpus>.jsonl \
    --training-data data/fpl_training_rows.csv \
    --output reports/<corpus>_decomp.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import RidgeRegressor  # noqa: E402
from fpl_ai.config import parse_season_start_year  # noqa: E402

# SAFE_FEATURE_COLUMNS grouped into prompt-sized buckets.
GROUP_PREFIXES = [
    ("recent_form", ("points_avg_", "bonus_avg_", "bps_avg_")),
    ("minutes", ("minutes_avg_", "appearance_rate_", "played_60_rate_", "starts_avg_")),
    (
        "attack_threat",
        ("influence_avg_", "creativity_avg_", "threat_avg_", "ict_index_avg_",
         "expected_goals_avg_", "expected_assists_avg_", "expected_goal_involvements_avg_"),
    ),
    ("defence", ("expected_goals_conceded_avg_", "defensive_contribution_avg_")),
    ("team_vs_opponent", ("team_goals_", "opponent_goals_")),
    (
        "fixture_context",
        ("primary_opponent_team_id", "home_fixture_count", "away_fixture_count", "fixture_count",
         "fixture_difficulty_", "home_fixture_ratio", "blank_gw", "double_gw"),
    ),
    (
        "market",
        ("price_pre_deadline", "selected_by_percent_", "transfers_", "transfer_balance_",
         "price_change_", "selected_change_"),
    ),
    ("status_flags", ("status_flag_", "news_flag_", "expected_data_source_", "defensive_data_source_")),
]


def group_of(feature: str) -> str:
    for group, prefixes in GROUP_PREFIXES:
        if any(feature.startswith(prefix) for prefix in prefixes):
            return group
    return "other"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--training-data", default="data/fpl_training_rows.csv")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    dataset = CanonicalDataset.from_csv(args.training_data)
    frame = dataset.training_frame.loc[dataset.training_frame["eligible_for_training"]].copy()
    frame["_key"] = frame["season"].astype(str).map(parse_season_start_year) * 100 + frame["week"].astype(int)
    features = dataset.feature_columns
    group_names = [name for name, _ in GROUP_PREFIXES]
    feature_groups = np.array([group_of(feature) for feature in features])

    # Row lookup: (season, week, player_id) -> feature vector.
    frame_index = {
        (str(record["season"]), int(record["week"]), int(record["player_id"])): idx
        for idx, record in enumerate(frame[["season", "week", "player_id"]].to_dict(orient="records"))
    }
    x_all = frame[list(features)].fillna(0.0).to_numpy(dtype=float)

    models: dict[int, RidgeRegressor | None] = {}

    def model_for(cutoff_key: int) -> RidgeRegressor | None:
        if cutoff_key not in models:
            train = frame.loc[frame["_key"] < cutoff_key]
            models[cutoff_key] = (
                RidgeRegressor(feature_names=features, alpha=1.0).fit(train, "label_points_1gw")
                if len(train)
                else None
            )
        return models[cutoff_key]

    rows_written = 0
    rows_decomposed = 0
    drifted = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.corpus.open() as corpus_handle, args.output.open("w") as output_handle:
        for line in corpus_handle:
            row = json.loads(line)
            metadata = row["metadata"]
            season, week = str(row["season"]), int(row["week"])
            player_id = int(metadata.get("player_id") or 0)
            stored = float((metadata.get("baseline_forecast") or {}).get("baseline_points_1gw") or 0.0)
            cutoff_key = parse_season_start_year(season) * 100 + week
            model = model_for(cutoff_key)
            idx = frame_index.get((season, week, player_id))
            if model is not None and idx is not None and stored:
                contributions = (
                    np.asarray(model.coefficients_)
                    * (x_all[idx] - np.asarray(model.feature_means_))
                    / np.asarray(model.feature_scales_)
                )
                grouped = {
                    name: round(float(contributions[feature_groups == name].sum()), 2)
                    for name in group_names
                }
                predicted = model.intercept_ + float(contributions.sum())
                if abs(predicted - stored) > 0.02:
                    drifted += 1
                metadata["baseline_decomposition"] = {
                    "intercept": round(float(model.intercept_), 2),
                    **grouped,
                    "recomputed_points_1gw": round(predicted, 3),
                }
                rows_decomposed += 1
            output_handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            rows_written += 1

    print(
        f"done: {rows_written} rows -> {args.output} "
        f"(decomposed: {rows_decomposed}, drift>0.02: {drifted})"
    )


if __name__ == "__main__":
    main()

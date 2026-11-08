#!/usr/bin/env python3
"""Precompute weekly decision states for GRPO training/eval.

For each (season, week) in the window, serialize everything WeeklyBanditEnv
needs so the GRPO training loop never refits ridge models:

- squad state at W from the classic baseline backtest trajectory
  (pre-move squad, bank, free transfers) — reset-to-baseline transitions,
- the full rolling classic forecast pool for W (fit on strictly-prior weeks,
  alpha 1.0 — the standard protocol),
- realized points/minutes for every forecast player (the reward signal).

Output: reports/grpo_states/{season}.jsonl, one row per week.

Train seasons (2022-23..2024-25) are the GRPO training set; 2025-26 GW12-30
stays the untouched held-out gate.

Usage:
  python3 scripts/build_grpo_state_cache.py \
    --training-data data/fpl_training_rows.csv \
    --output-dir reports/grpo_states
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fpl_ai.backtest import _lookup_frame_by_player, _training_frame_for_week  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

# cache key -> (season, classic backtest report holding the squad trajectory).
# Train keys use wide windows (all fittable GWs; 2022-23 starts GW6 because
# the first season has no prior data before that; 2025-26-early covers GW2-11,
# which is strictly before the held-out gate so it is timestamp-clean for
# training). The "2025-26" key is the untouched GW12-30 eval window.
TRAJECTORY_REPORTS = {
    "2022-23": ("2022-23", "reports/backtest_2223_wide_decision_baseline/rolling_squad_backtest.json"),
    "2023-24": ("2023-24", "reports/backtest_2324_wide_decision_baseline/rolling_squad_backtest.json"),
    "2024-25": ("2024-25", "reports/backtest_2425_wide_decision_baseline/rolling_squad_backtest.json"),
    "2025-26-early": ("2025-26", "reports/backtest_2526_early_wide_decision_baseline/rolling_squad_backtest.json"),
    "2025-26": ("2025-26", "reports/backtest_gw12_30_decision_baseline/rolling_squad_backtest.json"),
    # G4 held-out decision window (Wes, 2026-09-04): 2025-26 GW30-38.
    "2025-26-late": ("2025-26", "reports/backtest_2526_late_wide_decision_baseline/rolling_squad_backtest.json"),
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--training-data", default="data/fpl_training_rows.csv")
    parser.add_argument("--output-dir", default="reports/grpo_states", type=Path)
    parser.add_argument("--seasons", nargs="*", default=list(TRAJECTORY_REPORTS))
    args = parser.parse_args()

    dataset = CanonicalDataset.from_csv(args.training_data)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for cache_key in args.seasons:
        season, trajectory_report = TRAJECTORY_REPORTS[cache_key]
        trajectory_path = Path(trajectory_report)
        if not trajectory_path.exists():
            print(f"skip {cache_key}: missing trajectory {trajectory_path}")
            continue
        trajectory = json.loads(trajectory_path.read_text())
        week_states = {int(week["week"]): week for week in trajectory["weeks"]}

        output_path = args.output_dir / f"{cache_key}.jsonl"
        rows_written = 0
        with output_path.open("w") as handle:
            for week in sorted(week_states):
                state = week_states[week]
                train_frame = _training_frame_for_week(dataset, test_season=season, week=week)
                if train_frame.empty:
                    continue
                suite = fit_model_suite_from_frame(
                    train_frame=train_frame, feature_names=dataset.feature_columns, alpha=1.0
                )
                week_frame = dataset.week_frame((season, week))
                forecasts = suite.predict_frame(week_frame)
                week_rows = _lookup_frame_by_player(week_frame)

                forecast_payload = [
                    {
                        "player_id": f.player_id,
                        "player_name": f.player_name,
                        "team_id": f.team_id,
                        "position": f.position,
                        "price": round(float(f.price), 1),
                        "predicted_minutes": round(float(f.predicted_minutes), 1),
                        "predicted_points_1gw": round(float(f.predicted_points_1gw), 3),
                        "predicted_points_3gw": round(float(f.predicted_points_3gw), 3),
                        "predicted_points_5gw": round(float(f.predicted_points_5gw), 3),
                        "appearance_probability": round(float(f.appearance_probability), 3),
                        "fixture_count": int(f.fixture_count),
                        "uncertainty": round(float(f.uncertainty), 3),
                    }
                    for f in forecasts
                    if f.price > 0
                ]
                actual_points = {}
                actual_minutes = {}
                for f in forecast_payload:
                    row = week_rows.get(f["player_id"], {})
                    actual_points[str(f["player_id"])] = float(row.get("label_points_1gw", 0.0) or 0.0)
                    actual_minutes[str(f["player_id"])] = float(row.get("label_minutes_1gw", 0.0) or 0.0)

                handle.write(
                    json.dumps(
                        {
                            "season": season,
                            "week": week,
                            "bank": float(state["bank_before"]),
                            "free_transfers": int(state["free_transfers_before"]),
                            "squad": [
                                {
                                    "player_id": int(p["player_id"]),
                                    "player_name": p["player_name"],
                                    "team_id": int(p["team_id"]),
                                    "position": p["position"],
                                    "sell_price": float(p["price"]),
                                }
                                for p in state["pre_move_squad"]
                            ],
                            "forecasts": forecast_payload,
                            "actual_points": actual_points,
                            "actual_minutes": actual_minutes,
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
                rows_written += 1
        print(f"{cache_key}: {rows_written} weekly states -> {output_path}")


if __name__ == "__main__":
    main()

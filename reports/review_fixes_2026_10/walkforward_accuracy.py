"""Walk-forward forecast accuracy on the decision-backtest weeks.

For every test week, fit the classic suite exactly as the squad backtest does
(backtest._training_frame_for_week) and score that week's forecasts for all
backtest-eligible players. Works against either code tree (PYTHONPATH picks
it), so pre-fix and fixed pipelines are scored identically.

3GW/5GW errors are reported only on rows whose label window lies inside the
season (week + H - 1 <= last week), so season-end truncation does not blur
the comparison.

usage: walkforward_accuracy.py <training.csv> <out.json>
"""
import json
import sys
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from fpl_ai.backtest import _training_frame_for_week  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

WINDOWS = [
    ("2025-26", 2, 5), ("2025-26", 6, 9), ("2025-26", 10, 13), ("2025-26", 14, 17), ("2025-26", 18, 21),
    ("2025-26", 22, 25), ("2025-26", 27, 30), ("2025-26", 31, 34), ("2025-26", 35, 38),
    ("2023-24", 12, 15), ("2023-24", 16, 19), ("2023-24", 20, 23), ("2023-24", 24, 27), ("2023-24", 28, 31),
    ("2023-24", 32, 35),
    ("2024-25", 12, 15), ("2024-25", 16, 19), ("2024-25", 20, 23), ("2024-25", 24, 27), ("2024-25", 28, 31),
    ("2024-25", 32, 35),
]


def main() -> None:
    table, out_path = sys.argv[1], sys.argv[2]
    dataset = CanonicalDataset.from_csv(table)
    frame = dataset.training_frame
    last_week = frame.groupby("season")["week"].max().to_dict()
    results = []
    for season, first, last in WINDOWS:
        for week in range(first, last + 1):
            train = _training_frame_for_week(dataset, test_season=season, week=week)
            suite = fit_model_suite_from_frame(train_frame=train, feature_names=dataset.feature_columns)
            week_frame = dataset.week_frame((season, week))
            week_frame = week_frame.loc[week_frame["eligible_for_backtest"].astype(bool)]
            if week_frame.empty:
                continue
            forecasts = {f.player_id: f for f in suite.predict_frame(week_frame)}
            rows = week_frame.drop_duplicates("player_id").set_index("player_id")
            ids = [pid for pid in rows.index if pid in forecasts]
            entry = {"season": season, "week": week, "window": f"{season}:{first}-{last}", "n": len(ids)}
            for horizon, attr, label in (
                (1, "predicted_points_1gw", "label_points_1gw"),
                (3, "predicted_points_3gw", "label_points_3gw"),
                (5, "predicted_points_5gw", "label_points_5gw"),
            ):
                if week + horizon - 1 > int(last_week[season]):
                    continue
                predicted = np.array([getattr(forecasts[pid], attr) for pid in ids], dtype=float)
                actual = rows.loc[ids, label].to_numpy(dtype=float)
                errors = predicted - actual
                entry[f"mae_{horizon}"] = float(np.mean(np.abs(errors)))
                entry[f"rmse_{horizon}"] = float(np.sqrt(np.mean(errors ** 2)))
                entry[f"bias_{horizon}"] = float(np.mean(errors))
                # Accuracy where decisions live: the 60 highest-forecast players.
                top = np.argsort(-predicted)[:60]
                entry[f"top60_mae_{horizon}"] = float(np.mean(np.abs(errors[top])))
                entry[f"top60_bias_{horizon}"] = float(np.mean(errors[top]))
                # Premiums (the GW2 "Haaland ranked 43rd" complaint): price >= 10.0.
                price = rows.loc[ids, "price_pre_deadline"].to_numpy(dtype=float)
                premium = price >= 10.0
                if premium.any():
                    entry[f"premium_bias_{horizon}"] = float(np.mean(errors[premium]))
                    entry[f"premium_n_{horizon}"] = int(premium.sum())
            results.append(entry)
            print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in entry.items()}), flush=True)
    with open(out_path, "w") as handle:
        json.dump(results, handle, indent=1)


if __name__ == "__main__":
    main()

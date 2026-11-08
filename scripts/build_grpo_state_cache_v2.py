#!/usr/bin/env python3
"""Weekly RL states on the fixed pipeline (G5).

For each (season, week): the starting squad, bank and free transfers from a
fixed-pipeline classic+F6 baseline trajectory (backtest-squad), the full
forecast pool fit only on rows available before that week
(training_rows_asof, as the backtest does), and realised points/minutes.

Train keys: 2022-23, 2023-24, 2024-25 (GW2-38) and 2025-26-train (GW2-26).
Eval key: 2025-26-holdout (GW27-38), the same holdout as E19/E20.

usage: build_grpo_state_cache_v2.py [--keys ...]   (runs the trajectory backtests if missing)
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.backtest import _lookup_frame_by_player, _training_frame_for_week  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

TABLE = "data/fpl_training_rows_v3_contract_f6.csv"
OUT = ROOT / "reports" / "grpo_states_v2"
KEYS = {  # key -> (season, first week, last week)
    "2020-21": ("2020-21", 2, 38),
    "2021-22": ("2021-22", 2, 38),
    "2022-23": ("2022-23", 2, 38),
    "2023-24": ("2023-24", 2, 38),
    "2024-25": ("2024-25", 2, 38),
    "2025-26-train": ("2025-26", 2, 26),
    "2025-26-holdout": ("2025-26", 27, 38),
}


def trajectory(key: str, trajectories: Path) -> Path:
    season, first, last = KEYS[key]
    out_dir = trajectories / key
    report = out_dir / "rolling_squad_backtest.json"
    if not report.exists():
        env = dict(os.environ, PYTHONPATH=str(ROOT / "src"), FPL_PRIOR_BLEND="1", FPL_OPPONENT_INTERACTION="1",
                   PYTHONDONTWRITEBYTECODE="1")
        subprocess.run([sys.executable, "-m", "fpl_ai.cli", "backtest-squad", "--training-data", TABLE,
                        "--test-season", season, "--initial-train-week-max", str(first - 1),
                        "--start-week", str(first), "--end-week", str(last), "--output-dir", str(out_dir),
                        "--skip-league-average-fetch"], check=True, cwd=ROOT, env=env,
                       stdout=subprocess.DEVNULL)
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--keys", nargs="*", default=list(KEYS))
    ap.add_argument("--out", default=str(OUT), help="states directory (a forecast variant, e.g. FPL_PER_FIXTURE=1, "
                    "writes next to the standard states and reuses their squad trajectories via --trajectories)")
    ap.add_argument("--trajectories", default=None, help="backtest trajectories dir (default <out>/trajectories)")
    args = ap.parse_args()
    out = Path(args.out)
    trajectories = Path(args.trajectories) if args.trajectories else out / "trajectories"
    out.mkdir(parents=True, exist_ok=True)
    dataset = CanonicalDataset.from_csv(ROOT / TABLE)
    for key in args.keys:
        season, first, last = KEYS[key]
        weeks = {int(w["week"]): w for w in json.loads(trajectory(key, trajectories).read_text())["weeks"]}
        path = out / f"{key}.jsonl"
        written = 0
        with path.open("w") as handle:
            for week in sorted(weeks):
                state = weeks[week]
                train = _training_frame_for_week(dataset, test_season=season, week=week)
                suite = fit_model_suite_from_frame(train_frame=train, feature_names=dataset.feature_columns)
                frame = dataset.week_frame((season, week))
                forecasts = [f for f in suite.predict_frame(frame) if f.price > 0]
                rows = _lookup_frame_by_player(frame)
                # The backtest's first week reports the pre-build budget (100.0) as bank_before next to the
                # already-built squad: a free £100m (found 2026-10-10). Bank = budget minus squad value there.
                # Only the first week: later team values legitimately exceed £100m after price rises.
                squad_value = sum(float(p["price"]) for p in state["pre_move_squad"])
                bank = float(state["bank_before"])
                if week == min(weeks) and bank >= 99.9 and squad_value > 90:
                    bank = round(max(0.0, 100.0 - squad_value), 1)
                handle.write(json.dumps({
                    "season": season, "week": week,
                    "bank": bank, "free_transfers": int(state["free_transfers_before"]),
                    "squad": [{"player_id": int(p["player_id"]), "player_name": p["player_name"],
                               "team_id": int(p["team_id"]), "position": p["position"], "sell_price": float(p["price"])}
                              for p in state["pre_move_squad"]],
                    "forecasts": [{"player_id": f.player_id, "player_name": f.player_name, "team_id": f.team_id,
                                   "position": f.position, "price": round(float(f.price), 1),
                                   "predicted_minutes": round(float(f.predicted_minutes), 1),
                                   "predicted_points_1gw": round(float(f.predicted_points_1gw), 3),
                                   "predicted_points_3gw": round(float(f.predicted_points_3gw), 3),
                                   "predicted_points_5gw": round(float(f.predicted_points_5gw), 3),
                                   "appearance_probability": round(float(f.appearance_probability), 3),
                                   "fixture_count": int(f.fixture_count), "uncertainty": round(float(f.uncertainty), 3)}
                                  for f in forecasts],
                    "actual_points": {str(f.player_id): float(rows.get(f.player_id, {}).get("label_points_1gw", 0.0) or 0.0)
                                      for f in forecasts},
                    "actual_minutes": {str(f.player_id): float(rows.get(f.player_id, {}).get("label_minutes_1gw", 0.0) or 0.0)
                                       for f in forecasts},
                }, ensure_ascii=False) + "\n")
                written += 1
        print(f"{key}: {written} weekly states -> {path}", flush=True)


if __name__ == "__main__":
    main()

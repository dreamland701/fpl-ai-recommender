"""GW6 classic+F6 forecasts for every player from the frozen snapshot.

usage: PYTHONPATH=<code>/src forecast.py <old|new> <training.csv> <out.jsonl>

old = the pre-fix live runbook: fit on every training-eligible row, so the
      live season's unfinished 3/5-week labels are read as if complete.
new = the fixed path: fit on training_rows_asof(table, 2026-27, 6).
"""
import json
import os
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = "/home/wescheng/projects/fpl/fpl"
os.chdir(ROOT)
os.environ["FPL_PRIOR_BLEND"] = "1"
os.environ["FPL_OPPONENT_INTERACTION"] = "1"

from fpl_ai.api import OfficialSnapshotService  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

SNAPSHOT = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent)) / "snapshot"


class FrozenClient:
    def __init__(self) -> None:
        self._bootstrap = json.loads((SNAPSHOT / "bootstrap_static.json").read_text())
        self._fixtures = json.loads((SNAPSHOT / "fixtures.json").read_text())

    def bootstrap_static(self):
        return self._bootstrap

    def fixtures(self):
        return self._fixtures


def main() -> None:
    mode, table, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    deadline = json.loads((SNAPSHOT / "manifest.json").read_text())["deadline_time"]
    dataset = CanonicalDataset.from_csv(table)
    if mode == "new":
        from fpl_ai.dataset import training_rows_asof

        train_frame = training_rows_asof(dataset.training_frame, "2026-27", 6)
    else:
        train_frame = dataset.training_frame.loc[dataset.training_frame["eligible_for_training"]].copy()
    suite = fit_model_suite_from_frame(train_frame=train_frame, feature_names=dataset.feature_columns)
    official = OfficialSnapshotService(client=FrozenClient()).build_current_week_frame(deadline)
    live = dataset.build_live_week_frame(official, history_root="data/fpl_history")
    forecasts = suite.predict_frame(live)
    live_by_id = live.set_index("player_id")
    official_by_id = official.set_index("player_id")
    with open(out_path, "w") as handle:
        for f in forecasts:
            o = official_by_id.loc[f.player_id]
            row = live_by_id.loc[f.player_id]
            handle.write(json.dumps({
                "player_id": int(f.player_id), "name": f.player_name, "team_id": int(f.team_id), "pos": f.position,
                "price": float(o.get("price") or 0), "own": float(o.get("selected_by_percent") or 0),
                "status": str(o.get("status") or "a"), "news": str(o.get("news") or ""),
                "p1": round(f.predicted_points_1gw, 3), "p3": round(f.predicted_points_3gw, 3),
                "p5": round(f.predicted_points_5gw, 3), "mins": round(f.predicted_minutes, 1),
                "papp": round(f.appearance_probability, 3), "unc": round(f.uncertainty, 3),
                "fixtures": int(f.fixture_count),
                "feat_selected_pct": float(row.get("selected_by_percent_pre_deadline", 0) or 0),
                "feat_selected_change": float(row.get("selected_change_1", 0) or 0),
                "feat_points_avg_3": float(row.get("points_avg_3", 0) or 0),
            }, ensure_ascii=False) + "\n")
    print(f"{mode}: {len(forecasts)} forecasts, train rows {len(train_frame)} -> {out_path}")


if __name__ == "__main__":
    main()

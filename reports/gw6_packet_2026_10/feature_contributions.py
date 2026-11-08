"""Per-feature contributions to selected players' GW6 forecasts.

usage: PYTHONPATH=<code>/src feature_contributions.py <old|new> <training.csv> <out.json>
Contribution = scaled coefficient x standardized live value (clipped to the fit
range, as predict() does), per head, so two
pipelines can be compared feature by feature (intercepts reported separately).
"""
import json
import os
import sys
import warnings

warnings.filterwarnings("ignore")
os.chdir("/home/wescheng/projects/fpl/fpl")
os.environ["FPL_PRIOR_BLEND"] = "1"
os.environ["FPL_OPPONENT_INTERACTION"] = "1"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from forecast import SNAPSHOT, FrozenClient  # noqa: E402
from fpl_ai.api import OfficialSnapshotService  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

PLAYERS = (411, 426, 165, 12, 124, 399, 379, 428)


def main() -> None:
    mode, table, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    dataset = CanonicalDataset.from_csv(table)
    if mode == "new":
        from fpl_ai.dataset import training_rows_asof

        train = training_rows_asof(dataset.training_frame, "2026-27", 6)
    else:
        train = dataset.training_frame.loc[dataset.training_frame["eligible_for_training"]]
    suite = fit_model_suite_from_frame(train_frame=train, feature_names=dataset.feature_columns)
    deadline = json.loads((SNAPSHOT / "manifest.json").read_text())["deadline_time"]
    official = OfficialSnapshotService(client=FrozenClient()).build_current_week_frame(deadline)
    live = dataset.build_live_week_frame(official, history_root="data/fpl_history").set_index("player_id")
    out = {}
    for pid in PLAYERS:
        row = live.loc[pid]
        entry = {"name": str(row["player_name"])}
        for head, model in (("p1", suite.points_1gw_model), ("p5", suite.points_5gw_model)):
            contributions = {}
            for j, name in enumerate(model.feature_names):
                value = float(row[name]) if name in row.index else 0.0
                clipped = min(max(value, float(model.feature_mins_[j])), float(model.feature_maxs_[j]))
                contributions[name] = {
                    "value": value,
                    "clipped": clipped,
                    "contribution": float(model.coefficients_[j])
                    * (clipped - float(model.feature_means_[j])) / float(model.feature_scales_[j]),
                }
            entry[head] = {"intercept": float(model.intercept_), "features": contributions}
        out[str(pid)] = entry
    with open(out_path, "w") as handle:
        json.dump(out, handle)
    print(f"{mode}: contributions for {len(out)} players -> {out_path}")


if __name__ == "__main__":
    main()

"""How much of the pre-fix live forecast came from mismatched ownership units.

Run with the PRE-FIX code on PYTHONPATH. Fits the pre-fix suite exactly as the
old live runbook did, builds the live frame from the frozen snapshot, and for
selected players reports each ownership feature's contribution to the 1GW and
5GW forecasts:
  live  = what the old pipeline actually added (percent-scale live value)
  train = what the same coefficient adds at the player's own last training row
          (count-scale, the units the coefficient was fit on)
"""
import json
import os
import sys
import warnings

import numpy as np

warnings.filterwarnings("ignore")
os.chdir("/home/wescheng/projects/fpl/fpl")
os.environ["FPL_PRIOR_BLEND"] = "1"
os.environ["FPL_OPPONENT_INTERACTION"] = "1"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from forecast import FrozenClient, SNAPSHOT  # noqa: E402
from fpl_ai.api import OfficialSnapshotService  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

FEATURES = ("selected_by_percent_pre_deadline", "selected_change_1")
PLAYERS = (411, 426, 165, 12, 124, 399, 379, 428, 31)  # Haaland, Bruno, João Pedro, Saka, Groß, Cherki, Isak, Cunha, Konsa


def contribution(model, name, value):
    """What predict() adds for this feature: input clipped to the fit range, then standardized."""
    j = list(model.feature_names).index(name)
    clipped = min(max(value, float(model.feature_mins_[j])), float(model.feature_maxs_[j]))
    return float(model.coefficients_[j]) * (clipped - float(model.feature_means_[j])) / float(model.feature_scales_[j])


def main() -> None:
    dataset = CanonicalDataset.from_csv("data/fpl_training_rows_blend_f6.csv")
    train = dataset.training_frame.loc[dataset.training_frame["eligible_for_training"]]
    suite = fit_model_suite_from_frame(train_frame=train, feature_names=dataset.feature_columns)
    deadline = json.loads((SNAPSHOT / "manifest.json").read_text())["deadline_time"]
    official = OfficialSnapshotService(client=FrozenClient()).build_current_week_frame(deadline)
    live = dataset.build_live_week_frame(official, history_root="data/fpl_history").set_index("player_id")
    history = dataset.training_frame.sort_values(["season", "week"]).groupby("code").tail(1).set_index("code")
    for horizon, model in (("1gw", suite.points_1gw_model), ("5gw", suite.points_5gw_model)):
        for name in FEATURES:
            j = list(model.feature_names).index(name)
            print(f"{horizon} {name}: scaled coef {model.coefficients_[j]:+.4f}, "
                  f"train mean {model.feature_means_[j]:.1f}, sd {model.feature_scales_[j]:.1f}, "
                  f"range [{model.feature_mins_[j]:,.0f}, {model.feature_maxs_[j]:,.0f}]")
    rows = []
    for pid in PLAYERS:
        live_row = live.loc[pid]
        train_row = history.loc[int(live_row["code"])]
        entry = {"player_id": pid, "name": str(live_row["player_name"])}
        for horizon, model in (("1gw", suite.points_1gw_model), ("5gw", suite.points_5gw_model)):
            for name in FEATURES:
                entry[f"{horizon}:{name}:live_value"] = float(live_row[name])
                entry[f"{horizon}:{name}:live"] = contribution(model, name, float(live_row[name]))
                entry[f"{horizon}:{name}:train"] = contribution(model, name, float(train_row[name]))
        rows.append(entry)
        total_1 = sum(entry[f"1gw:{n}:live"] - entry[f"1gw:{n}:train"] for n in FEATURES)
        total_5 = sum(entry[f"5gw:{n}:live"] - entry[f"5gw:{n}:train"] for n in FEATURES)
        print(f"{entry['name']:14s} sel_change live value {entry['1gw:selected_change_1:live_value']:>14,.0f} | "
              f"unit-mismatch shift vs own training row: 1GW {total_1:+.2f}, 5GW {total_5:+.2f}")
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ownership_units_decomposition.json")
    with open(out, "w") as handle:
        json.dump(rows, handle, indent=1)


if __name__ == "__main__":
    main()

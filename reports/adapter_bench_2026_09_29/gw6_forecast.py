"""GW6 2026-27 classic(+F6) forecasts for every player, written to job tmp only.

Mirrors build_live_gw_examples.py --stage corpus's forecasting path but
never touches data/ or reports/ (that stage rewrites fixtures.csv/teams.csv).
"""
import json
import os
import sys
import warnings

warnings.filterwarnings("ignore")
ROOT = "/home/wescheng/projects/fpl/fpl"
sys.path.insert(0, f"{ROOT}/src")
os.chdir(ROOT)

variant = sys.argv[1]  # "f6" or "base"
out_path = sys.argv[2]
os.environ["FPL_PRIOR_BLEND"] = "1"
if variant == "f6":
    os.environ["FPL_OPPONENT_INTERACTION"] = "1"
    table = "data/fpl_training_rows_blend_f6.csv"
else:
    os.environ.pop("FPL_OPPONENT_INTERACTION", None)
    table = "data/fpl_training_rows_blend_f6.csv"

from fpl_ai.api import OfficialSnapshotService  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

dataset = CanonicalDataset.from_csv(table)
features = list(dataset.feature_columns)
if variant != "f6":
    features = [f for f in features if "opp_weakness" not in f and "opp_def_weakness" not in f]
print(f"variant={variant} table={table} n_features={len(features)} "
      f"f6_feats={[f for f in features if 'weakness' in f]}")
train_frame = dataset.training_frame.loc[dataset.training_frame["eligible_for_training"]].copy()
print("train rows", len(train_frame), "max season/week",
      train_frame[["season", "week"]].sort_values(["season", "week"]).tail(1).to_dict("records"))
suite = fit_model_suite_from_frame(train_frame=train_frame, feature_names=features)

snap = OfficialSnapshotService()
official = snap.build_current_week_frame("2026-10-10T10:00:00Z")
live = dataset.build_live_week_frame(official, history_root="data/fpl_history")
forecasts = suite.predict_frame(live)

status = dict(zip(official["player_id"], official["status"].fillna("a")))
news = dict(zip(official["player_id"], official["news"].fillna("")))
price = dict(zip(official["player_id"], official["price"]))
own = dict(zip(official["player_id"], official["selected_by_percent"]))
with open(out_path, "w") as handle:
    for f in forecasts:
        handle.write(json.dumps({
            "player_id": f.player_id, "name": f.player_name, "team_id": f.team_id, "pos": f.position,
            "price": float(price.get(f.player_id, 0) or 0), "own": float(own.get(f.player_id, 0) or 0),
            "status": status.get(f.player_id, "a"), "news": news.get(f.player_id, ""),
            "p1": round(f.predicted_points_1gw, 3), "p3": round(f.predicted_points_3gw, 3),
            "p5": round(f.predicted_points_5gw, 3), "mins": round(f.predicted_minutes, 1),
            "papp": round(f.appearance_probability, 3), "unc": round(f.uncertainty, 3),
        }, ensure_ascii=False) + "\n")
print("wrote", len(forecasts), "->", out_path)

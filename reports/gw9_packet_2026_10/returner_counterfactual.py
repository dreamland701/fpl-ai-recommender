#!/usr/bin/env python3
"""Returner counterfactual (2026-10-28, the Isak case): the minutes/appearance heads are current-season rolling
features, so a returner's injury blank (GW6: 0 min) reads as rotation and depresses his P(appear) for weeks. This
re-forecasts ONE player with that blank replaced by a normal start in his rolling availability features only
(minutes_avg_k, appearance_rate_k, starts_avg_k, observed_* ); points form is left as it is, so it is a conservative
"fit and nailed" read. Same fitted model and snapshot as forecasts_new_pipeline.jsonl.
usage: PACKET_DIR=<dir> python3 returner_counterfactual.py <web_name> <blank_week> <minutes_for_that_week> [<table>]"""
import json, os, sys, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
ROOT = Path("/home/wescheng/projects/fpl/fpl"); os.chdir(ROOT); sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("FPL_PRIOR_BLEND", "1"); os.environ.setdefault("FPL_OPPONENT_INTERACTION", "1")
import pandas as pd
from fpl_ai.api import OfficialSnapshotService
from fpl_ai.dataset import CanonicalDataset, training_rows_asof
from fpl_ai.models import fit_model_suite_from_frame
P = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent)); SNAP = P / "snapshot"
who, blank_week, fill_min = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
table = sys.argv[4] if len(sys.argv) > 4 else "data/fpl_training_rows_v3_contract_f6.csv"
class Frozen:
    def bootstrap_static(self): return json.loads((SNAP / "bootstrap_static.json").read_text())
    def fixtures(self): return json.loads((SNAP / "fixtures.json").read_text())
deadline = json.loads((SNAP / "manifest.json").read_text())["deadline_time"]
ds = CanonicalDataset.from_csv(table)
week = int(json.loads((SNAP / "manifest.json").read_text()).get("event", 0) or 0)
official = OfficialSnapshotService(client=Frozen()).build_current_week_frame(deadline)
live = ds.build_live_week_frame(official, history_root="data/fpl_history")
season = str(live["season"].mode().iloc[0]); week = int(pd.to_numeric(live["week"], errors="coerce").mode().iloc[0])
suite = fit_model_suite_from_frame(train_frame=training_rows_asof(ds.training_frame, season, week), feature_names=ds.feature_columns)
pid = int(official.loc[official["player_name"].str.lower() == who.lower(), "player_id"].iloc[0]) if "player_name" in official.columns else None
if pid is None:
    pid = int(official.loc[official["web_name"].str.lower() == who.lower(), "player_id"].iloc[0])
g = pd.read_csv(f"data/fpl_history/{season}/merged_gw.csv", low_memory=False)
gw = next(c for c in ("round", "GW", "gw", "event") if c in g.columns)
rows = g[(g["element"] == pid) & (g[gw] < week)].sort_values(gw)
mins = rows.set_index(gw)["minutes"].astype(float).to_dict(); mins_cf = dict(mins); mins_cf[blank_week] = fill_min
def feats(m):
    ks = sorted(m); out = {}
    for k in (1, 3, 5, 8):
        last = [m[w] for w in ks[-k:]]
        out[f"minutes_avg_{k}"] = sum(last) / len(last); out[f"appearance_rate_{k}"] = sum(x > 0 for x in last) / len(last)
    for k in (3, 5):
        last = [m[w] for w in ks[-k:]]; out[f"starts_avg_{k}"] = sum(x >= 60 for x in last) / len(last)
    out["observed_minutes"] = sum(m.values()); out["observed_appearances"] = sum(x > 0 for x in m.values()); out["observed_starts"] = sum(x >= 60 for x in m.values())
    return out
f0, f1 = feats(mins), feats(mins_cf)
print(f"{who} (id {pid}) minutes by week: {mins}")
live_cf = live.copy(); idx = live_cf.index[live_cf["player_id"] == pid]
changed = {}
for c, v in f1.items():
    if c in live_cf.columns:
        before = float(live_cf.loc[idx, c].iloc[0]); live_cf.loc[idx, c] = v; changed[c] = (round(before, 2), round(v, 2))
print("features changed (live value -> counterfactual):", changed)
a = {f.player_id: f for f in suite.predict_frame(live)}[pid]; b = {f.player_id: f for f in suite.predict_frame(live_cf)}[pid]
print(f"standard:        GW {a.predicted_points_1gw:.2f} / 3GW {a.predicted_points_3gw:.2f} / 5GW {a.predicted_points_5gw:.2f}, {a.predicted_minutes:.0f} min, P(app) {a.appearance_probability:.2f}")
print(f"blank -> {fill_min:.0f} min: GW {b.predicted_points_1gw:.2f} / 3GW {b.predicted_points_3gw:.2f} / 5GW {b.predicted_points_5gw:.2f}, {b.predicted_minutes:.0f} min, P(app) {b.appearance_probability:.2f}")

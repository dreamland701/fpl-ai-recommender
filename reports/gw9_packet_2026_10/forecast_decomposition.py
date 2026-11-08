#!/usr/bin/env python3
"""Feature-family decomposition of the classic ridge forecast for named players (2026-10-28, the Isak question: where
does his gap to Thiago / N.Jackson come from?). The ridge is linear in standardised features, so each feature's
contribution is coef * (x - mean) / scale; features are grouped into families by name. Same fitted model and snapshot
as forecasts_new_pipeline.jsonl. usage: PACKET_DIR=<dir> python3 forecast_decomposition.py <ref_name> <other_name> [<other_name> ...]"""
import json, os, re, sys, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
ROOT = Path("/home/wescheng/projects/fpl/fpl"); os.chdir(ROOT); sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("FPL_PRIOR_BLEND", "1"); os.environ.setdefault("FPL_OPPONENT_INTERACTION", "1")
import numpy as np, pandas as pd
from fpl_ai.api import OfficialSnapshotService
from fpl_ai.dataset import CanonicalDataset, training_rows_asof
from fpl_ai.models import fit_model_suite_from_frame
P = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent)); SNAP = P / "snapshot"
names = sys.argv[1:]
class Frozen:
    def bootstrap_static(self): return json.loads((SNAP / "bootstrap_static.json").read_text())
    def fixtures(self): return json.loads((SNAP / "fixtures.json").read_text())
deadline = json.loads((SNAP / "manifest.json").read_text())["deadline_time"]
ds = CanonicalDataset.from_csv("data/fpl_training_rows_v3_contract_f6.csv")
official = OfficialSnapshotService(client=Frozen()).build_current_week_frame(deadline)
live = ds.build_live_week_frame(official, history_root="data/fpl_history")
season = str(live["season"].mode().iloc[0]); week = int(pd.to_numeric(live["week"], errors="coerce").mode().iloc[0])
suite = fit_model_suite_from_frame(train_frame=training_rows_asof(ds.training_frame, season, week), feature_names=ds.feature_columns)
col = "player_name" if "player_name" in official.columns else "web_name"
pids = {n: int(official.loc[official[col].str.lower() == n.lower(), "player_id"].iloc[0]) for n in names}
FAM = [("availability", r"^(minutes_avg|appearance_rate|starts_avg|played_60_rate|observed_(minutes|appearances|starts)|status|chance|news_flag)"),
       ("points form", r"^(points_avg|bps_avg|bonus|ict_index_avg|influence|threat_avg|creativity_avg|goals|assists|clean|saves|defensive_)"),
       ("xG form", r"^(expected_|xg|xa|npxg)"),
       ("fixtures / F6", r"(opponent|opp_|fixture|home|away|difficulty|team_goals|interaction|_x_|strength|team_|blank_gw|double_gw)"),
       ("market", r"(price|cost|owner|selected|transfer)"),
       ("prior season", r"(prior|blend|last_season|prev_season)"),
       ("position", r"^(position|is_|pos_)")]
def fam(f):
    for name, rx in FAM:
        if re.search(rx, f): return name
    return "other"
def contrib(model, row):
    x = row[list(model.feature_names)].fillna(0.0).to_numpy(dtype=float)
    if model.feature_mins_ and model.feature_maxs_:
        x = np.clip(x, np.asarray(model.feature_mins_), np.asarray(model.feature_maxs_))
    z = (x - np.asarray(model.feature_means_)) / np.asarray(model.feature_scales_)
    c = z * np.asarray(model.coefficients_)
    return pd.Series(c, index=list(model.feature_names)), model.intercept_
heads = {"GW9 points": suite.points_1gw_model, "GW9-13 points": suite.points_5gw_model, "minutes": suite.availability_model}
L = live.set_index("player_id")
ref = names[0]
out = [f"# Forecast decomposition, {season} GW{week}: {ref} vs {', '.join(names[1:])}", "",
       "Contribution = coef × standardised feature (clipped to the training range). Positive = raises the forecast. Rows are the OTHER player's contribution minus the reference's, i.e. where the reference LOSES (negative) or gains (positive) relative to each.", ""]
for hname, model in heads.items():
    C = {n: contrib(model, L.loc[pids[n]])[0] for n in names}
    icpt = contrib(model, L.loc[pids[ref]])[1]
    out += [f"## {hname} (intercept {icpt:.2f})", "", "| family | " + " | ".join(f"{n}" for n in names) + " | " + " | ".join(f"{ref} − {n}" for n in names[1:]) + " |",
            "|---|" + "---|" * (2 * len(names) - 1)]
    fams = sorted({fam(f) for f in C[ref].index}, key=lambda s: ["availability", "points form", "xG form", "fixtures / F6", "market", "prior season", "position", "other"].index(s))
    for fm in fams:
        idx = [f for f in C[ref].index if fam(f) == fm]
        vals = {n: C[n][idx].sum() for n in names}
        out.append(f"| {fm} ({len(idx)}) | " + " | ".join(f"{vals[n]:+.2f}" for n in names) + " | " + " | ".join(f"{vals[ref] - vals[n]:+.2f}" for n in names[1:]) + " |")
    out.append(f"| **total forecast** | " + " | ".join(f"{icpt + C[n].sum():.2f}" for n in names) + " | " + " | ".join(f"{C[ref].sum() - C[n].sum():+.2f}" for n in names[1:]) + " |")
    for n in names[1:]:
        d = (C[ref] - C[n]).sort_values()
        out += ["", f"Largest single features, {ref} − {n}: " + "; ".join(f"{f} {v:+.2f} ({L.loc[pids[ref], f]:.3g} vs {L.loc[pids[n], f]:.3g})" for f, v in list(d.head(6).items()) + list(d.tail(4).items()))]
    out.append("")
others = sorted({f for f in C[ref].index if fam(f) == "other"})
out += ["Ungrouped features: " + (", ".join(others) if others else "none"), ""]
txt = "\n".join(out); print(txt); (P / f"forecast_decomposition_{ref.lower().replace(' ', '_')}.md").write_text(txt + "\n")

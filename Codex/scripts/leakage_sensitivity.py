"""Measure sensitivity to target-horizon purging in the EXISTING simulator.

This is an exploratory diagnostic, not a repaired official-rules backtest.
Everything is patched in memory; source and existing artifacts stay untouched.
"""
import json
import os
from pathlib import Path
import sys
from unittest.mock import patch
from dataclasses import asdict
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"src"))
from fpl_ai.dataset import CanonicalDataset
from fpl_ai import backtest
from fpl_ai.models import RidgeRegressor, ForecastModelSuite

OUT=ROOT/"Codex/analysis"
frame=pd.read_csv(ROOT/"data/fpl_training_rows_blend_f6.csv",low_memory=False)
data=CanonicalDataset(frame)
records=[]
cutoff={}
original_training=backtest._training_frame_for_week


def training(dataset,test_season,week):
    cutoff.update(season=test_season,week=week)
    return original_training(dataset,test_season,week)


def purged_fit(train_frame,feature_names,alpha=1.):
    season,week=cutoff["season"],cutoff["week"]
    heads={}
    for h in (1,3,5):
        # Label at origin t contains t..t+h-1. Require its final GW < W.
        mask=(train_frame.season!=season)|(train_frame.week+h-1<week)
        heads[h]=RidgeRegressor(feature_names,alpha=alpha).fit(train_frame.loc[mask],f"label_points_{h}gw")
    minutes=RidgeRegressor(feature_names,alpha=alpha).fit(train_frame,"label_minutes_1gw")
    return ForecastModelSuite(feature_names,minutes,heads[1],heads[3],heads[5])


for start,end in [(27,30),(31,34),(35,38)]:
    for mode in ("existing","purged"):
        print(f"Running {mode} 2025-26 GW{start}-{end}",flush=True)
        kwargs=dict(dataset=data,test_season="2025-26",initial_train_week_max=start-1,start_week=start,end_week=end)
        if mode=="purged":
            with patch.object(backtest,"_training_frame_for_week",side_effect=training),patch.object(backtest,"fit_model_suite_from_frame",side_effect=purged_fit):
                report=backtest.run_rolling_squad_backtest(**kwargs)
        else:
            report=backtest.run_rolling_squad_backtest(**kwargs)
        (OUT/f"sensitivity_{mode}_{start}_{end}.json").write_text(json.dumps(asdict(report),indent=2))
        records.append({"start":start,"end":end,"mode":mode,"total_actual":report.total_actual_points,
                        "total_predicted":report.total_predicted_points,"hits":report.total_transfer_hits})
        print(records[-1],flush=True)
(OUT/"leakage_sensitivity.json").write_text(json.dumps({"warning":"Same existing simulator defects, final historical tables and window reset conditions in both arms. Purging is only a partial correction. Do not use these totals as clean performance estimates.","results":records},indent=2)+"\n")

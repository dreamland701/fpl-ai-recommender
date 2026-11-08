#!/usr/bin/env python
"""Programme item 1 mechanism check: walk-forward 1GW forecast bias / RMSE by position on the 2025-26 bench windows,
fitted exactly as the decision backtest fits (refit every week on training_rows_asof), for whatever env flags are set.
usage: FPL_REGIME_TERM=1 python scripts/regime_accuracy_check.py --label RG1_F [--season 2025-26]
"""
import argparse, os, sys
from pathlib import Path
import numpy as np, pandas as pd
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.dataset import CanonicalDataset, training_rows_asof  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

WINDOWS = {"2025-26": [(2, 5), (6, 9), (10, 13), (14, 17), (18, 21), (22, 25), (27, 30), (31, 34), (35, 38)],
           "2024-25": [(12, 15), (16, 19), (20, 23), (24, 27), (28, 31), (32, 35)]}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--label", required=True); ap.add_argument("--season", default="2025-26")
    ap.add_argument("--table", default=str(ROOT / "data/fpl_training_rows_v3_contract_f6_status.csv")); a = ap.parse_args()
    ds = CanonicalDataset.from_csv(a.table)
    rows = []
    for (lo, hi) in WINDOWS[a.season]:
        for week in range(lo, hi + 1):
            train = training_rows_asof(ds.training_frame, a.season, week)
            suite = fit_model_suite_from_frame(train, feature_names=ds.feature_columns, alpha=1.0)
            wf = ds.week_frame(f"{a.season}:{week}") if False else ds.training_frame.loc[(ds.training_frame.season == a.season) & (ds.training_frame.week == week)].copy().reset_index(drop=True)
            wf = wf.loc[wf["eligible_for_backtest"].astype(bool)].reset_index(drop=True)
            fc = suite.predict_frame(wf)
            pred = np.array([f.predicted_points_1gw for f in fc]); pmin = np.array([f.predicted_minutes for f in fc])
            y = pd.to_numeric(wf["label_points_1gw"], errors="coerce").to_numpy(float)
            for pos, p, m, yy in zip(wf["position"].astype(str), pred, pmin, y):
                rows.append({"week": week, "position": pos, "pred": p, "pmin": m, "y": yy})
    df = pd.DataFrame(rows).dropna()
    def summarise(d, tag):
        g = d.groupby("position").agg(n=("y", "size"), pred=("pred", "mean"), actual=("y", "mean"))
        g["bias"] = g.pred - g.actual; g["rmse"] = d.groupby("position").apply(lambda x: np.sqrt(np.mean((x.pred - x.y) ** 2)))
        print(f"{a.label} {a.season} {tag}: " + " | ".join(f"{pos} n {int(r.n)} pred {r.pred:.2f} act {r.actual:.2f} bias {r.bias:+.2f} rmse {r.rmse:.3f}" for pos, r in g.iterrows()) + f" || all bias {(d.pred - d.y).mean():+.3f} rmse {np.sqrt(np.mean((d.pred - d.y) ** 2)):.3f}")
    summarise(df, "all eligible")
    summarise(df[df.pmin >= 60], "predicted starters (>=60 min)")

if __name__ == "__main__":
    main()

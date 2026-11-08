"""Is the linear classic model leaving nonlinear signal on the table? Ridge vs gradient-boosted trees.

Wes (2026-10-10): "the classic model is still fairly linear, but this game could have a lot of
nonlinearity". For each of the 84 decision-backtest weeks (21 windows), both models are fitted on
the identical walk-forward training frame (backtest._training_frame_for_week, label embargo
included) and scored on that week's backtest-eligible players: error by horizon, calibration by
forecast decile (where a linear model's compression would show), the top-60 and premiums, and
appearance AUC. Per-row predictions are saved for later slicing.

usage: nonlinear_check.py <training.csv> <out_prefix>
"""
import json
import os
import sys
import warnings

import numpy as np

warnings.filterwarnings("ignore")
from fpl_ai.backtest import _training_frame_for_week  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

sys.path.insert(0, os.path.dirname(__file__))
from walkforward_accuracy import WINDOWS  # noqa: E402


def auc(score, label):
    order = np.argsort(score); ranks = np.empty(len(score)); ranks[order] = np.arange(1, len(score) + 1)
    pos = label.astype(bool); n1, n0 = pos.sum(), (~pos).sum()
    return float((ranks[pos].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def main() -> None:
    table, prefix = sys.argv[1], sys.argv[2]
    dataset = CanonicalDataset.from_csv(table)
    last_week = dataset.training_frame.groupby("season")["week"].max().to_dict()
    rows = []
    for season, first, last in WINDOWS:
        for week in range(first, last + 1):
            train = _training_frame_for_week(dataset, test_season=season, week=week)
            suites = {}
            for cls in ("ridge", "hgb"):
                os.environ["FPL_MODEL_CLASS"] = cls
                suites[cls] = fit_model_suite_from_frame(train_frame=train, feature_names=dataset.feature_columns)
            wf = dataset.week_frame((season, week))
            wf = wf.loc[wf["eligible_for_backtest"].astype(bool)].drop_duplicates("player_id")
            if wf.empty:
                continue
            preds = {cls: {f.player_id: f for f in s.predict_frame(wf)} for cls, s in suites.items()}
            for rec in wf.to_dict(orient="records"):
                pid = int(rec["player_id"])
                row = {"season": season, "week": week, "pid": pid, "position": rec["position"],
                       "price": float(rec.get("price_pre_deadline") or 0.0),
                       "actual_1": float(rec["label_points_1gw"]), "minutes": float(rec["label_minutes_1gw"])}
                for h in (3, 5):
                    row[f"actual_{h}"] = float(rec[f"label_points_{h}gw"]) if week + h - 1 <= int(last_week[season]) else None
                for cls in ("ridge", "hgb"):
                    f = preds[cls][pid]
                    row[f"{cls}_1"], row[f"{cls}_3"], row[f"{cls}_5"] = f.predicted_points_1gw, f.predicted_points_3gw, f.predicted_points_5gw
                    row[f"{cls}_papp"] = f.appearance_probability
                rows.append(row)
            print(f"{season} GW{week}: {len(wf)} players", flush=True)
    json.dump(rows, open(f"{prefix}_rows.json", "w"))

    lines = ["# Ridge (current classic) vs gradient-boosted trees, 84 walk-forward weeks", ""]
    for h in (1, 3, 5):
        sel = [r for r in rows if r[f"actual_{h}"] is not None]
        y = np.array([r[f"actual_{h}"] for r in sel])
        out = []
        for cls in ("ridge", "hgb"):
            p = np.array([r[f"{cls}_{h}"] for r in sel]); e = p - y
            top = np.argsort(-p)[:max(1, len(p) // 10)]
            out.append(f"{cls}: RMSE {np.sqrt(np.mean(e ** 2)):.3f}, MAE {np.mean(np.abs(e)):.3f}, bias {e.mean():+.2f}, top-decile bias {e[top].mean():+.2f}")
        lines.append(f"- {h}GW (n {len(sel)}): " + " | ".join(out))
    y = np.array([r["actual_1"] for r in rows]); played = np.array([r["minutes"] > 0 for r in rows])
    lines.append(f"- Appearance AUC: ridge {auc(np.array([r['ridge_papp'] for r in rows]), played):.3f} | "
                 f"hgb {auc(np.array([r['hgb_papp'] for r in rows]), played):.3f}")
    ridge = np.array([r["ridge_1"] for r in rows]); hgb = np.array([r["hgb_1"] for r in rows])
    lines += ["", "Calibration by ridge-forecast decile (1GW): mean forecast vs mean actual", "",
              "| Decile | Ridge forecast | Trees forecast | Actual |", "|---|---|---|---|"]
    edges = np.quantile(ridge, np.linspace(0, 1, 11))
    for i in range(10):
        m = (ridge >= edges[i]) & (ridge <= edges[i + 1] if i == 9 else ridge < edges[i + 1])
        lines.append(f"| {i + 1} | {ridge[m].mean():.2f} | {hgb[m].mean():.2f} | {y[m].mean():.2f} |")
    for label, m in (("price >= 10 (premiums)", np.array([r["price"] >= 10 for r in rows])),
                     ("price 7.5-10", np.array([7.5 <= r["price"] < 10 for r in rows]))):
        lines.append(f"\n{label}: n {m.sum()} | ridge bias {(ridge[m] - y[m]).mean():+.2f} | trees bias {(hgb[m] - y[m]).mean():+.2f}")
    open(f"{prefix}.md", "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

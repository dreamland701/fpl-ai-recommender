"""F14 bookmaker market: paired walk-forward accuracy, ridge with vs without the mkt_* features.

Same 84 decision weeks as the nonlinear check (21 windows), identical training frames (label embargo
included); the only difference is the feature list. Reports error by horizon, appearance AUC, the
clean-sheet slice (GK/DEF) and the top decile, plus the standardized ridge coefficients of the
market columns, so a null here is informative before any decision backtest is read.

usage: FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 PYTHONPATH=src python reports/market_f14/market_accuracy.py \
          data/fpl_training_rows_v3_contract_f6_mkt.csv reports/market_f14/accuracy
"""
import json
import os
import sys
import warnings
from unittest import mock

import numpy as np

warnings.filterwarnings("ignore")
from fpl_ai import market  # noqa: E402
from fpl_ai.backtest import _training_frame_for_week  # noqa: E402
from fpl_ai.dataset import CanonicalDataset  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "review_fixes_2026_10"))
from walkforward_accuracy import WINDOWS  # noqa: E402


def auc(score, label):
    order = np.argsort(score); ranks = np.empty(len(score)); ranks[order] = np.arange(1, len(score) + 1)
    pos = label.astype(bool); n1, n0 = pos.sum(), (~pos).sum()
    return float((ranks[pos].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def main() -> None:
    table, prefix = sys.argv[1], sys.argv[2]
    dataset = CanonicalDataset.from_csv(table)
    with_mkt = list(dataset.feature_columns)
    # ACC_DROP: comma-separated feature names that define the "base" model (default: the market columns)
    drop = [c for c in os.environ.get("ACC_DROP", ",".join(market.FEATURES)).split(",") if c]
    without = [c for c in with_mkt if c not in drop]
    assert len(with_mkt) - len(without) == len(drop), f"columns missing from the table: {set(drop) - set(with_mkt)}"
    last_week = dataset.training_frame.groupby("season")["week"].max().to_dict()
    rows, coefs = [], []
    for season, first, last in WINDOWS:
        for week in range(first, last + 1):
            train = _training_frame_for_week(dataset, test_season=season, week=week)
            # ACC_VARIANT_ENV="K=V,K=V": env set only while fitting the variant suite (model-class A/Bs)
            variant_env = dict(kv.split("=", 1) for kv in os.environ.get("ACC_VARIANT_ENV", "").split(",") if kv)
            suites = {"base": fit_model_suite_from_frame(train_frame=train, feature_names=without)}
            with mock.patch.dict(os.environ, variant_env):
                suites["mkt"] = fit_model_suite_from_frame(train_frame=train, feature_names=with_mkt)
            head = suites["mkt"].points_1gw_model
            coefs.append({n: float(c) for n, c in zip(head.feature_names, head.coefficients_) if n in drop})
            wf = dataset.week_frame((season, week))
            wf = wf.loc[wf["eligible_for_backtest"].astype(bool)].drop_duplicates("player_id")
            if wf.empty:
                continue
            preds = {k: {f.player_id: f for f in s.predict_frame(wf)} for k, s in suites.items()}
            for rec in wf.to_dict(orient="records"):
                pid = int(rec["player_id"])
                row = {"season": season, "week": week, "pid": pid, "position": rec["position"],
                       "price": float(rec.get("price_pre_deadline") or 0.0), "cs_prob": float(rec.get("mkt_cs_prob") or 0.0),
                       "actual_1": float(rec["label_points_1gw"]), "minutes": float(rec["label_minutes_1gw"])}
                for h in (3, 5):
                    row[f"actual_{h}"] = float(rec[f"label_points_{h}gw"]) if week + h - 1 <= int(last_week[season]) else None
                for k in ("base", "mkt"):
                    f = preds[k][pid]
                    row[f"{k}_1"], row[f"{k}_3"], row[f"{k}_5"], row[f"{k}_papp"] = (
                        f.predicted_points_1gw, f.predicted_points_3gw, f.predicted_points_5gw, f.appearance_probability)
                rows.append(row)
            print(f"{season} GW{week}: {len(wf)} players", flush=True)
    json.dump(rows, open(f"{prefix}_rows.json", "w"))

    lines = [f"# Classic ridge with vs without {drop}, 84 walk-forward weeks", ""]
    for h in (1, 3, 5):
        sel = [r for r in rows if r[f"actual_{h}"] is not None]
        y = np.array([r[f"actual_{h}"] for r in sel]); out = []
        for k in ("base", "mkt"):
            p = np.array([r[f"{k}_{h}"] for r in sel]); e = p - y
            top = np.argsort(-p)[:max(1, len(p) // 10)]
            out.append(f"{k}: RMSE {np.sqrt(np.mean(e ** 2)):.4f}, MAE {np.mean(np.abs(e)):.4f}, bias {e.mean():+.3f}, "
                       f"top-decile actual {y[top].mean():.3f}")
        lines.append(f"- {h}GW (n {len(sel)}): " + " | ".join(out))
    y = np.array([r["actual_1"] for r in rows]); played = np.array([r["minutes"] > 0 for r in rows])
    lines.append(f"- Appearance AUC: base {auc(np.array([r['base_papp'] for r in rows]), played):.4f} | "
                 f"mkt {auc(np.array([r['mkt_papp'] for r in rows]), played):.4f}")
    for label, m in (("GK+DEF", np.array([r["position"] in ("GK", "DEF") for r in rows])),
                     ("MID+FWD", np.array([r["position"] in ("MID", "FWD") for r in rows])),
                     ("price >= 10", np.array([r["price"] >= 10 for r in rows])),
                     ("minutes_avg high (played 60+ this week)", np.array([r["minutes"] >= 60 for r in rows]))):
        b = np.array([r["base_1"] for r in rows])[m]; k = np.array([r["mkt_1"] for r in rows])[m]; yy = y[m]
        lines.append(f"- 1GW {label} (n {m.sum()}): RMSE base {np.sqrt(np.mean((b - yy) ** 2)):.4f} | mkt {np.sqrt(np.mean((k - yy) ** 2)):.4f}")
    # per-week paired RMSE: how often the market model wins
    wins = 0; weeks = 0
    for (s, w) in sorted({(r["season"], r["week"]) for r in rows}):
        sel = [r for r in rows if r["season"] == s and r["week"] == w]
        yy = np.array([r["actual_1"] for r in sel])
        eb = np.sqrt(np.mean((np.array([r["base_1"] for r in sel]) - yy) ** 2))
        ek = np.sqrt(np.mean((np.array([r["mkt_1"] for r in sel]) - yy) ** 2))
        weeks += 1; wins += ek < eb
    lines.append(f"- 1GW RMSE: market model better in {wins}/{weeks} weeks")
    # clean-sheet slice: GK/DEF by market clean-sheet probability tercile, forecast vs actual
    gkdef = [r for r in rows if r["position"] in ("GK", "DEF") and r["minutes"] >= 60]
    cs = np.array([r["cs_prob"] for r in gkdef]); edges = np.quantile(cs, [0, 1 / 3, 2 / 3, 1])
    lines += ["", "GK/DEF who played 60+, by market clean-sheet probability tercile: mean forecast (base / mkt) vs actual", "",
              "| tercile | n | cs prob | base | mkt | actual |", "|---|---|---|---|---|---|"]
    for i in range(3):
        m = (cs >= edges[i]) & (cs <= edges[i + 1] if i == 2 else cs < edges[i + 1])
        sel = [r for r, keep in zip(gkdef, m) if keep]
        lines.append(f"| {i + 1} | {len(sel)} | {np.mean([r['cs_prob'] for r in sel]):.2f} | {np.mean([r['base_1'] for r in sel]):.2f} | "
                     f"{np.mean([r['mkt_1'] for r in sel]):.2f} | {np.mean([r['actual_1'] for r in sel]):.2f} |")
    if coefs:
        lines += ["", "Mean standardized 1GW ridge coefficient of each market column across the 84 fits:", ""]
        for name in drop:
            vals = [c[name] for c in coefs if name in c]
            if vals:
                lines.append(f"- {name}: {np.mean(vals):+.4f}")
    open(f"{prefix}.md", "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

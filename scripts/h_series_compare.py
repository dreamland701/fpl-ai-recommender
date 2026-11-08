"""Compare regression-head arms (H1, H3, H31, ...) on the shared E22 holdout/live rows.
usage: h_series_compare.py <arm> <arm> [...] [--out file.md]
Reads reports/h_series/<arm>_{holdout,live}_pred.jsonl (decoder record shape: response = deltas, metadata = baseline +
labels), reports/h_series/bt_<arm>/<window>/rolling_squad_backtest.json (decision windows, vs bt_classic) and the
xPts re-score summary in reports/h_series/xpts/summary.md when present. Every accuracy number is recomputed from the
prediction files, so the arms are scored on identical rows with identical code."""
import json
import os
import sys

import numpy as np
from sklearn.metrics import brier_score_loss, roc_auc_score

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HS = os.path.join(ROOT, "reports", "h_series")
WINDOWS = ("2025-26_27_30", "2025-26_31_34", "2025-26_35_38", "2026-27_2_6")


def load(arm, split):
    path = os.path.join(HS, f"{arm}_{split}_pred.jsonl")
    if not os.path.exists(path):
        return None
    out = {}
    for line in open(path):
        if not line.strip():
            continue
        q = json.loads(line); m = q["metadata"]; d = json.loads(q["response"])
        key = (m["season"], int(m["week"]), int(m["player_id"]))
        out[key] = (m, d)
    return out


def auc(y, p):
    return roc_auc_score(y, p) if len(y) > 10 and 0 < y.mean() < 1 else float("nan")


def metrics(rows):
    """rows: list of (meta, deltas) -> dict of classic/arm accuracy on 1/3/5GW points and availability."""
    b1 = np.array([float(m["baseline_forecast"]["baseline_points_1gw"]) for m, _ in rows])
    y1 = np.array([float(m["labels"]["points_1gw"]) for m, _ in rows])
    p1 = b1 + np.array([float(d["delta_points_1gw"]) for _, d in rows])
    res = {"n": len(rows)}
    for h in (1, 3, 5):
        b = np.array([float(m["baseline_forecast"][f"baseline_points_{h}gw"]) for m, _ in rows])
        y = np.array([float(m["labels"][f"points_{h}gw"]) for m, _ in rows])
        p = b + np.array([float(d[f"delta_points_{h}gw"]) for _, d in rows])
        res[f"rmse{h}_classic"] = float(np.sqrt(np.mean((b - y) ** 2))); res[f"rmse{h}_arm"] = float(np.sqrt(np.mean((p - y) ** 2)))
        if h == 1:
            res["mae1_classic"] = float(np.mean(np.abs(b - y))); res["mae1_arm"] = float(np.mean(np.abs(p - y)))
            res["bias1_classic"] = float(np.mean(b - y)); res["bias1_arm"] = float(np.mean(p - y))
            res["closer"] = float(np.mean(np.abs(p - y) < np.abs(b - y)))
            res["delta1_mean"] = float(np.mean(p - b)); res["delta1_abs"] = float(np.mean(np.abs(p - b))); res["delta1_sd"] = float(np.std(p - b))
    ya = np.array([float(m["labels"]["appearance_probability"] > 0.5) for m, _ in rows])
    ba = np.array([float(m["baseline_forecast"]["baseline_appearance_probability"]) for m, _ in rows])
    pa = np.clip(ba + np.array([float(d["delta_appearance_probability"]) for _, d in rows]), 0, 1)
    unc = (ba > 0.15) & (ba < 0.95)
    res.update(auc_classic=auc(ya, ba), auc_arm=auc(ya, pa), brier_classic=float(brier_score_loss(ya, ba)), brier_arm=float(brier_score_loss(ya, pa)),
               n_unc=int(unc.sum()), auc_unc_classic=auc(ya[unc], ba[unc]), auc_unc_arm=auc(ya[unc], pa[unc]),
               brier_unc_classic=float(brier_score_loss(ya[unc], ba[unc])) if unc.sum() else float("nan"),
               brier_unc_arm=float(brier_score_loss(ya[unc], pa[unc])) if unc.sum() else float("nan"),
               deltaa_abs=float(np.mean(np.abs(pa - ba))))
    return res


def subsets(data):
    rows = list(data.values())
    yield "all", rows
    yield "with text", [r for r in rows if r[0].get("evidence_present")]
    yield "no text", [r for r in rows if not r[0].get("evidence_present")]
    yield "classic >= 4", [r for r in rows if float(r[0]["baseline_forecast"]["baseline_points_1gw"]) >= 4]
    yield "flagged (P<0.95)", [r for r in rows if float(r[0]["baseline_forecast"]["baseline_appearance_probability"]) < 0.95]


def fmt(x, nd=3):
    return "nan" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{nd}f}"


def main():
    out_path = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    arms = [a for a in sys.argv[1:] if not a.startswith("--") and a != out_path]
    lines = []
    P = lines.append
    P(f"# H-series comparison: {' vs '.join(arms)}\n")
    P("Recomputed from the prediction files on identical rows. RMSE on the 1/3/5GW points labels (classic / arm); bias = forecast − actual; closer = share of rows where the arm lands strictly nearer the actual than classic; |Δ| = mean absolute change the arm makes to the classic forecast.\n")
    for split in ("holdout", "live"):
        datas = {a: load(a, split) for a in arms}
        datas = {a: d for a, d in datas.items() if d}
        if not datas:
            continue
        P(f"## {split}\n")
        P("| arm | subset | n | RMSE 1GW classic / arm | RMSE 3GW | RMSE 5GW | MAE 1GW | bias 1GW | closer | Δ1 mean / abs / sd |")
        P("|---|---|---|---|---|---|---|---|---|---|")
        for a, d in datas.items():
            for name, rows in subsets(d):
                if len(rows) < 10:
                    continue
                r = metrics(rows)
                P(f"| {a} | {name} | {r['n']} | {fmt(r['rmse1_classic'])} / {fmt(r['rmse1_arm'])} | {fmt(r['rmse3_classic'])} / {fmt(r['rmse3_arm'])} | {fmt(r['rmse5_classic'])} / {fmt(r['rmse5_arm'])} | {fmt(r['mae1_classic'])} / {fmt(r['mae1_arm'])} | {fmt(r['bias1_classic'], 2)} / {fmt(r['bias1_arm'], 2)} | {r['closer']:.0%} | {fmt(r['delta1_mean'], 2)} / {fmt(r['delta1_abs'], 2)} / {fmt(r['delta1_sd'], 2)} |")
        P("")
        P("| arm | subset | n | AUC classic / arm | Brier classic / arm | uncertain n | AUC unc classic / arm | Brier unc classic / arm | |ΔP| mean |")
        P("|---|---|---|---|---|---|---|---|---|")
        for a, d in datas.items():
            for name, rows in subsets(d):
                if len(rows) < 10:
                    continue
                r = metrics(rows)
                P(f"| {a} | {name} | {r['n']} | {fmt(r['auc_classic'])} / {fmt(r['auc_arm'])} | {fmt(r['brier_classic'], 4)} / {fmt(r['brier_arm'], 4)} | {r['n_unc']} | {fmt(r['auc_unc_classic'])} / {fmt(r['auc_unc_arm'])} | {fmt(r['brier_unc_classic'], 4)} / {fmt(r['brier_unc_arm'], 4)} | {fmt(r['deltaa_abs'], 3)} |")
        P("")
        if len(datas) >= 2:
            P("Head to head on matched rows (arm A vs arm B): correlation of the deltas, share of rows with the same sign, RMSE of A and B on 1GW points, and share of rows where A is strictly closer than B.\n")
            P("| A | B | n | corr Δ1 | corr ΔP(app) | same sign Δ1 | RMSE A / B | A closer than B |")
            P("|---|---|---|---|---|---|---|---|")
            keys = list(datas)
            for i in range(len(keys)):
                for j in range(i + 1, len(keys)):
                    A, B = datas[keys[i]], datas[keys[j]]
                    common = [k for k in A if k in B]
                    if len(common) < 10:
                        continue
                    da = np.array([float(A[k][1]["delta_points_1gw"]) for k in common]); db = np.array([float(B[k][1]["delta_points_1gw"]) for k in common])
                    pa = np.array([float(A[k][1]["delta_appearance_probability"]) for k in common]); pb = np.array([float(B[k][1]["delta_appearance_probability"]) for k in common])
                    y = np.array([float(A[k][0]["labels"]["points_1gw"]) for k in common]); b = np.array([float(A[k][0]["baseline_forecast"]["baseline_points_1gw"]) for k in common])
                    ea, eb = np.abs(b + da - y), np.abs(b + db - y)
                    corr = lambda u, v: float(np.corrcoef(u, v)[0, 1]) if u.std() > 0 and v.std() > 0 else float("nan")
                    P(f"| {keys[i]} | {keys[j]} | {len(common)} | {fmt(corr(da, db))} | {fmt(corr(pa, pb))} | {np.mean(np.sign(da) == np.sign(db)):.0%} | {fmt(float(np.sqrt(np.mean(ea ** 2))))} / {fmt(float(np.sqrt(np.mean(eb ** 2))))} | {np.mean(ea < eb):.0%} |")
            P("")
    # decision windows
    P("## Decision windows (realised squad points, same engine, `--llm-fields all`)\n")
    tags = ["classic"] + arms
    P("| window | " + " | ".join(tags) + " | " + " | ".join(f"{a} − classic" for a in arms) + " |")
    P("|---|" + "---|" * (len(tags) + len(arms)))
    totals = {t: 0.0 for t in tags}; have = {t: 0 for t in tags}
    for w in WINDOWS:
        vals = {}
        for t in tags:
            p = os.path.join(HS, f"bt_{t}", w, "rolling_squad_backtest.json")
            vals[t] = json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
            if vals[t] is not None:
                totals[t] += vals[t]; have[t] += 1
        P(f"| {w} | " + " | ".join("—" if vals[t] is None else f"{vals[t]:.0f}" for t in tags) + " | " + " | ".join("—" if vals[a] is None or vals["classic"] is None else f"{vals[a] - vals['classic']:+.0f}" for a in arms) + " |")
    P("| total | " + " | ".join(f"{totals[t]:.0f} ({have[t]}w)" for t in tags) + " | " + " | ".join(f"{totals[a] - totals['classic']:+.0f}" if have[a] == have["classic"] else "—" for a in arms) + " |")
    P("")
    xp = os.path.join(HS, "xpts", "summary.md")
    if os.path.exists(xp):
        P("## xPts re-score (reports/h_series/xpts/summary.md)\n")
        P(open(xp).read().strip())
        P("")
    text = "\n".join(lines)
    print(text)
    if out_path:
        with open(out_path, "w") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()

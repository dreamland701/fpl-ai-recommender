"""Why does E20 forecast better (MAE) but pick worse squads? Holdout diagnosis + variants.

1. Median vs mean: within bins of the classic 1GW forecast, compare the mean and
   median realised points with the classic and adapter forecasts. MAE rewards
   the median; squad selection needs the mean; FPL points are right-skewed.
2. Where the shrink lands: adapter delta by position and price band.
3. Decision-relevant ranking, per week: Spearman among the top 60, realised
   points of the top-11 picks and of the top-1 (captain) pick.
4. Variant prediction files for backtest-squad (same rows, rewritten responses):
   deshrunk   per-week linear shrink on the baseline removed, remainder kept
   shrinkonly only that per-week linear shrink
   demean     per-week mean delta removed (keeps relative re-ranking)
   availnorm  only relative availability routed into points (09-29 "V3")

usage: e20_diagnosis.py <eval.jsonl> <sft_predictions.jsonl> <out_dir>
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.llm_adjust import parse_delta_response  # noqa: E402

H = ("1gw", "3gw", "5gw")


def spearman(a, b):
    ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def main() -> None:
    eval_path, pred_path, out_dir = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    out_dir.mkdir(parents=True, exist_ok=True)
    examples = [json.loads(l) for l in open(eval_path) if l.strip()]
    preds = {}
    for l in open(pred_path):
        if l.strip():
            p = json.loads(l)
            preds[(p["metadata"]["season"], int(p["week"]), int(p["metadata"]["player_id"]))] = p
    rows = []
    for e in examples:
        m = e["metadata"]; b = m["baseline_forecast"]; lab = m["labels"]
        key = (m["season"], int(e["week"]), int(m["player_id"]))
        d = parse_delta_response(str(preds[key].get("response") or "")) or {}
        rows.append({"key": key, "week": int(e["week"]), "pos": m["position"], "pred": preds[key],
                     **{f"b{h}": float(b[f"baseline_points_{h}"]) for h in H},
                     **{f"d{h}": float(d.get(f"delta_points_{h}", 0.0)) for h in H},
                     **{f"y{h}": float(lab[f"points_{h}"]) for h in H},
                     "bapp": float(b["baseline_appearance_probability"]), "dapp": float(d.get("delta_appearance_probability", 0.0)),
                     "price": float((m.get("market") or {}).get("price") or 0.0)})
    report = {}
    b1 = np.array([r["b1gw"] for r in rows]); d1 = np.array([r["d1gw"] for r in rows]); y1 = np.array([r["y1gw"] for r in rows])
    edges = np.quantile(b1, np.linspace(0, 1, 9))
    bins = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        sel = (b1 >= lo) & (b1 <= hi)
        bins.append({"classic_range": [round(float(lo), 2), round(float(hi), 2)], "n": int(sel.sum()),
                     "actual_mean": round(float(y1[sel].mean()), 2), "actual_median": round(float(np.median(y1[sel])), 2),
                     "classic_mean": round(float(b1[sel].mean()), 2), "adapter_mean": round(float((b1 + d1)[sel].mean()), 2)})
    report["median_vs_mean_by_classic_bin"] = bins
    by_pos = defaultdict(list)
    for r in rows:
        by_pos[r["pos"]].append(r)
    report["delta_by_position"] = {
        pos: {"n": len(v), "mean_delta_1gw": round(float(np.mean([r["d1gw"] for r in v])), 3),
              "actual_mean_minus_median": round(float(np.mean([r["y1gw"] for r in v]) - np.median([r["y1gw"] for r in v])), 3),
              "classic_bias": round(float(np.mean([r["b1gw"] - r["y1gw"] for r in v])), 3),
              "adapter_bias": round(float(np.mean([r["b1gw"] + r["d1gw"] - r["y1gw"] for r in v])), 3)}
        for pos, v in sorted(by_pos.items())}
    weekly = defaultdict(list)
    for r in rows:
        weekly[r["week"]].append(r)
    ranking = {"spearman_top60": [], "top11_points": [], "captain_points": []}
    for w, v in sorted(weekly.items()):
        b = np.array([r["b1gw"] for r in v]); a = b + np.array([r["d1gw"] for r in v]); y = np.array([r["y1gw"] for r in v])
        top = np.argsort(-b)[:60]
        ranking["spearman_top60"].append((spearman(b[top], y[top]), spearman(a[top], y[top])))
        ranking["top11_points"].append((float(y[np.argsort(-b)[:11]].sum()), float(y[np.argsort(-a)[:11]].sum())))
        ranking["captain_points"].append((float(y[np.argmax(b)]), float(y[np.argmax(a)])))
    report["ranking"] = {k: {"classic": round(float(np.mean([x[0] for x in v])), 3), "adapter": round(float(np.mean([x[1] for x in v])), 3),
                             "adapter_better_weeks": int(sum(x[1] > x[0] for x in v)), "weeks": len(v)}
                         for k, v in ranking.items()}
    # variants
    fits = {}
    for w, v in weekly.items():
        for h in H:
            x = np.array([r[f"b{h}"] for r in v]); d = np.array([r[f"d{h}"] for r in v])
            slope, intercept = np.polyfit(x, d, 1)
            fits[(w, h)] = (slope, intercept)
    shrink_share = []
    for w, v in weekly.items():
        x = np.array([r["b1gw"] for r in v]); d = np.array([r["d1gw"] for r in v])
        s, c = fits[(w, "1gw")]
        resid = d - (s * x + c)
        shrink_share.append(1 - resid.var() / d.var() if d.var() > 0 else 0)
    report["share_of_1gw_delta_variance_explained_by_weekly_linear_shrink"] = round(float(np.mean(shrink_share)), 3)
    week_mean = {(w, h): float(np.mean([r[f"d{h}"] for r in v])) for w, v in weekly.items() for h in H}
    ratio_mean = {}
    for w, v in weekly.items():
        ratios = [min(1.4, max(0.6, min(1.0, max(0.0, r["bapp"] + r["dapp"])) / max(r["bapp"], 1e-6))) for r in v]
        ratio_mean[w] = float(np.mean(ratios))
    writers = {name: open(out_dir / f"e20_pred_{name}.jsonl", "w") for name in ("deshrunk", "shrinkonly", "demean", "availnorm")}
    for r in rows:
        w = r["week"]
        base = {"delta_appearance_probability": r["dapp"]}
        variants = {
            "deshrunk": {**base, **{f"delta_points_{h}": r[f"d{h}"] - (fits[(w, h)][0] * r[f"b{h}"] + fits[(w, h)][1]) for h in H}},
            "shrinkonly": {f"delta_points_{h}": fits[(w, h)][0] * r[f"b{h}"] + fits[(w, h)][1] for h in H},
            "demean": {**base, **{f"delta_points_{h}": r[f"d{h}"] - week_mean[(w, h)] for h in H}},
        }
        ratio = min(1.4, max(0.6, min(1.0, max(0.0, r["bapp"] + r["dapp"])) / max(r["bapp"], 1e-6)))
        scale = ratio / ratio_mean[w]
        variants["availnorm"] = {f"delta_points_{h}": r[f"b{h}"] * (scale - 1.0) for h in H}
        for name, deltas in variants.items():
            q = dict(r["pred"]); q["response"] = json.dumps(deltas)
            writers[name].write(json.dumps(q, ensure_ascii=False) + "\n")
    for handle in writers.values():
        handle.close()
    (out_dir / "e20_diagnosis.json").write_text(json.dumps(report, indent=1))
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()

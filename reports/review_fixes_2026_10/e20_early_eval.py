"""Holdout read for an adapter without waiting for the base-model decode.

usage: e20_early_eval.py <eval.jsonl> <sft_predictions.jsonl> <label>

Forecast error (1GW, 5GW) of classic vs classic + adapter delta against the
realised labels, per 4-week window, and the availability AUC among likely
starters (classic P(appear) >= 0.5), the metric in the live promotion rule.
Deltas go through fpl_ai.llm_adjust (same parser, bounds and join as backtests).
"""
import json
import sys

import numpy as np

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.llm_adjust import load_llm_delta_lookup  # noqa: E402


def auc(scores, labels):
    pairs = sorted(zip(scores, labels))
    pos = sum(labels)
    neg = len(labels) - pos
    if not pos or not neg:
        return float("nan")
    rank_sum, i = 0.0, 0
    while i < len(pairs):
        j = i
        while j < len(pairs) and pairs[j][0] == pairs[i][0]:
            j += 1
        rank_sum += sum(1 for k in range(i, j) if pairs[k][1]) * (i + j + 1) / 2.0
        i = j
    return (rank_sum - pos * (pos + 1) / 2.0) / (pos * neg)


def main() -> None:
    eval_path, pred_path, label = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = [json.loads(line) for line in open(eval_path) if line.strip()]
    lookup = load_llm_delta_lookup(eval_path, pred_path)
    windows = {"27-30": (27, 30), "31-34": (31, 34), "35-38": (35, 38), "all": (27, 38)}
    out = {"label": label, "parsed": len(lookup), "rows": len(rows)}
    for name, (lo, hi) in windows.items():
        sel = [r for r in rows if lo <= int(r["week"]) <= hi]
        acc = {"c1": [], "a1": [], "c5": [], "a5": [], "y1": [], "y5": [], "cp": [], "ap": [], "app": [], "d1": [], "b1": []}
        for r in sel:
            m = r["metadata"]
            b = m["baseline_forecast"]
            labels = m["labels"]
            key = (str(r.get("season") or m["season"]), int(r["week"]), int(m["player_id"]))
            d = lookup.get(key, {})
            c1, c5, cp = float(b["baseline_points_1gw"]), float(b["baseline_points_5gw"]), float(b["baseline_appearance_probability"])
            acc["c1"].append(c1); acc["a1"].append(c1 + d.get("delta_points_1gw", 0.0))
            acc["c5"].append(c5); acc["a5"].append(c5 + d.get("delta_points_5gw", 0.0))
            acc["y1"].append(float(labels["points_1gw"])); acc["y5"].append(float(labels["points_5gw"]))
            acc["cp"].append(cp); acc["ap"].append(min(1.0, max(0.0, cp + d.get("delta_appearance_probability", 0.0))))
            acc["app"].append(float(labels["minutes_1gw"]) > 0)
            acc["d1"].append(d.get("delta_points_1gw", 0.0)); acc["b1"].append(c1)
        a = {k: np.asarray(v, dtype=float) for k, v in acc.items()}
        starters = a["cp"] >= 0.5
        out[name] = {
            "n": int(len(sel)),
            "mae_1gw": {"classic": round(float(np.mean(np.abs(a["c1"] - a["y1"]))), 4),
                        "adapter": round(float(np.mean(np.abs(a["a1"] - a["y1"]))), 4)},
            "rmse_1gw": {"classic": round(float(np.sqrt(np.mean((a["c1"] - a["y1"]) ** 2))), 4),
                         "adapter": round(float(np.sqrt(np.mean((a["a1"] - a["y1"]) ** 2))), 4)},
            "mae_5gw": {"classic": round(float(np.mean(np.abs(a["c5"] - a["y5"]))), 4),
                        "adapter": round(float(np.mean(np.abs(a["a5"] - a["y5"]))), 4)},
            "bias_1gw": {"classic": round(float(np.mean(a["c1"] - a["y1"])), 4),
                         "adapter": round(float(np.mean(a["a1"] - a["y1"])), 4)},
            "availability_auc_likely_starters": {
                "classic": round(auc(list(a["cp"][starters]), list(a["app"][starters].astype(bool))), 3),
                "adapter": round(auc(list(a["ap"][starters]), list(a["app"][starters].astype(bool))), 3),
                "n": int(starters.sum())},
            "mean_delta_1gw": round(float(np.mean(a["d1"])), 3),
            "corr_delta_baseline_1gw": round(float(np.corrcoef(a["d1"], a["b1"])[0, 1]), 3) if np.std(a["d1"]) > 0 else None,
        }
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()

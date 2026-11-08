#!/usr/bin/env python3
"""Turn an availability read into decision inputs (2026-10-15, H1 follow-up).

Why: the production optimizer is nearly inert to P(appear) (threshold penalty below 0.65 only), and the classic
P(appear) is under-confident on regular starters (0.72 said, 0.92 played), so "replace P and rescale points"
inflates everyone. The principled coupling: unconditional points = P x conditional points, so the LLM's P should
rescale the classic points by P_llm / P_classic_calibrated, where the calibration is a Platt fit of the classic
P(appear) on training rows. Writes two prediction files in the decoder record shape:
  <out_coupled>: delta_points_{1,3,5}gw = baseline x (P_llm / P_cal - 1) (x1, x1/3, x1/5: this-week information),
                 delta_appearance_probability = P_llm - P_classic         -> use with --llm-fields points (or all)
  <out_platt>:   delta_appearance_probability = P_cal - P_classic only    -> calibration-only control
usage: avail_couple_preds.py <examples> <preds> <out_coupled> <out_platt> --platt P.json [--fit-from train.jsonl]
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np


def logit(p):
    p = min(max(p, 1e-4), 1 - 1e-4)
    return math.log(p / (1 - p))


def sig(x):
    return 1 / (1 + math.exp(-x))


def fit_platt(train_path):
    xs, ys = [], []
    for line in open(train_path):
        if not line.strip():
            continue
        m = json.loads(line)["metadata"]
        p = m["baseline_forecast"]["baseline_appearance_probability"]
        if p is None or p <= 0.0 or p >= 1.0:
            continue
        xs.append(logit(float(p))); ys.append(1.0 if m["labels"]["minutes_1gw"] > 0 else 0.0)
    x = np.array(xs); y = np.array(ys); a, b = 0.0, 1.0
    for _ in range(200):  # Newton on the 2-parameter logistic
        z = a + b * x; p = 1 / (1 + np.exp(-z)); w = p * (1 - p)
        g = np.array([np.sum(p - y), np.sum((p - y) * x)])
        H = np.array([[np.sum(w), np.sum(w * x)], [np.sum(w * x), np.sum(w * x * x)]]) + 1e-6 * np.eye(2)
        step = np.linalg.solve(H, g); a -= step[0]; b -= step[1]
        if np.abs(step).max() < 1e-8:
            break
    return {"a": float(a), "b": float(b), "n": int(len(x)), "played": float(y.mean()), "mean_p": float((1 / (1 + np.exp(-x))).mean())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("examples"); ap.add_argument("preds"); ap.add_argument("out_coupled"); ap.add_argument("out_platt")
    ap.add_argument("--platt", required=True, help="JSON with a, b (fitted here with --fit-from when missing)")
    ap.add_argument("--fit-from"); ap.add_argument("--ratio-clamp", type=float, nargs=2, default=(0.1, 1.5))
    args = ap.parse_args()
    pp = Path(args.platt)
    if args.fit_from and not pp.exists():
        pp.write_text(json.dumps(fit_platt(args.fit_from), indent=1))
    cal = json.loads(pp.read_text())
    ex = [json.loads(l) for l in open(args.examples) if l.strip()]
    pr = [json.loads(l) for l in open(args.preds) if l.strip()]
    assert len(ex) == len(pr), (len(ex), len(pr))
    stats = []
    with open(args.out_coupled, "w") as fc, open(args.out_platt, "w") as fp:
        for e, p in zip(ex, pr):
            m = e["metadata"]; bf = m["baseline_forecast"]; d = json.loads(p["response"]) if isinstance(p.get("response"), str) else p["response"]
            p0 = float(bf["baseline_appearance_probability"]); p0c = min(max(p0, 1e-4), 1 - 1e-4)
            p_cal = sig(cal["a"] + cal["b"] * logit(p0c)) if 0.0 < p0 < 1.0 else p0
            p_llm = min(1.0, max(0.0, p0 + float(d.get("delta_appearance_probability", 0.0))))
            ratio = min(args.ratio_clamp[1], max(args.ratio_clamp[0], p_llm / max(p_cal, 1e-4))) if 0.0 < p0 < 1.0 else 1.0
            coupled = {"delta_points_1gw": round(bf["baseline_points_1gw"] * (ratio - 1), 4),
                       "delta_points_3gw": round(bf["baseline_points_3gw"] * (ratio - 1) / 3, 4),
                       "delta_points_5gw": round(bf["baseline_points_5gw"] * (ratio - 1) / 5, 4),
                       "delta_minutes_1gw": 0.0, "delta_appearance_probability": round(p_llm - p0, 4)}
            platt = {"delta_points_1gw": 0.0, "delta_points_3gw": 0.0, "delta_points_5gw": 0.0, "delta_minutes_1gw": 0.0,
                     "delta_appearance_probability": round(p_cal - p0, 4)}
            for f, dd in ((fc, coupled), (fp, platt)):
                f.write(json.dumps({"season": e["season"], "week": e["week"], "response": json.dumps(dd), "metadata": m}, ensure_ascii=False) + "\n")
            stats.append((p0, p_cal, p_llm, ratio, coupled["delta_points_1gw"]))
    s = np.array(stats)
    print(f"platt a {cal['a']:+.3f} b {cal['b']:.3f} (n {cal.get('n')}); rows {len(s)}; mean P classic {s[:,0].mean():.3f} cal {s[:,1].mean():.3f} llm {s[:,2].mean():.3f}; "
          f"ratio mean {s[:,3].mean():.3f} sd {s[:,3].std():.3f} [{s[:,3].min():.2f},{s[:,3].max():.2f}]; delta1 mean {s[:,4].mean():+.3f} sd {s[:,4].std():.3f}; rows ratio<0.7: {(s[:,3]<0.7).sum()}")


if __name__ == "__main__":
    main()

"""Availability AUC/Brier of classic vs an adapter's deltas, from prediction files in the decoder's format."""
import json
import sys
import numpy as np
from sklearn.metrics import brier_score_loss, roc_auc_score


def auc(y, p):
    return roc_auc_score(y, p) if len(y) > 10 and 0 < y.mean() < 1 else float("nan")


for path in sys.argv[1:]:
    y, b, p = [], [], []
    for l in open(path):
        q = json.loads(l); m = q["metadata"]; d = json.loads(q["response"])
        y.append(float(m["labels"]["appearance_probability"] > 0.5)); b0 = float(m["baseline_forecast"]["baseline_appearance_probability"])
        b.append(b0); p.append(min(1, max(0, b0 + d.get("delta_appearance_probability", 0.0))))
    y, b, p = map(np.array, (y, b, p)); unc = (b > 0.15) & (b < 0.95)
    print(f"AVAIL {path.split('/')[-1]}: n {len(y)} played {y.mean():.3f} | AUC classic {auc(y, b):.4f} adapter {auc(y, p):.4f} | Brier classic {brier_score_loss(y, b):.4f} "
          f"adapter {brier_score_loss(y, p):.4f} | uncertain {unc.sum()}: AUC {auc(y[unc], b[unc]):.4f} -> {auc(y[unc], p[unc]):.4f}")

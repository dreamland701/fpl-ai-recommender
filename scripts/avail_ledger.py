#!/usr/bin/env python3
"""Availability ledger for a regression-head read: AUC / Brier of classic vs Platt-calibrated classic vs head, overall
and on the decision-relevant subsets, per season-window. usage: avail_ledger.py <examples> <preds> --platt P.json [--windows 4]"""
import argparse, json, math
import numpy as np
from sklearn.metrics import roc_auc_score

ap = argparse.ArgumentParser(); ap.add_argument("examples"); ap.add_argument("preds"); ap.add_argument("--platt"); ap.add_argument("--windows", type=int, default=4)
ap.add_argument("--label", default="head"); a = ap.parse_args()
E = [json.loads(l) for l in open(a.examples) if l.strip()]; P = [json.loads(l) for l in open(a.preds) if l.strip()]
assert len(E) == len(P)
cal = json.load(open(a.platt)) if a.platt else None
def lg(p): p = min(max(p, 1e-4), 1 - 1e-4); return math.log(p / (1 - p))
y = np.array([1.0 if e["metadata"]["labels"]["minutes_1gw"] > 0 else 0.0 for e in E])
b = np.array([float(e["metadata"]["baseline_forecast"]["baseline_appearance_probability"]) for e in E])
pc = np.array([1 / (1 + math.exp(-(cal["a"] + cal["b"] * lg(x)))) if cal else x for x in b])
h = np.clip(b + np.array([float((json.loads(p["response"]) if isinstance(p["response"], str) else p["response"])["delta_appearance_probability"]) for p in P]), 0, 1)
st = np.array([e["prompt"].split("Status pre-deadline: ", 1)[1].split("\n", 1)[0].strip() if "Status pre-deadline: " in e["prompt"] else "?" for e in E])
news = np.array(["Official player news pre-deadline: none" not in e["prompt"] for e in E]); ev = np.array([bool(e["metadata"].get("evidence_present")) for e in E])
wk = np.array([int(e["week"]) for e in E]); season = np.array([e["season"] for e in E])
def auc(m, p): return roc_auc_score(y[m], p[m]) if 0 < y[m].sum() < m.sum() else float("nan")
def row(name, m):
    if m.sum() < 20: return
    print(f"| {name} | {int(m.sum())} | {y[m].mean():.3f} | {auc(m, b):.3f} / {auc(m, pc):.3f} / {auc(m, h):.3f} | "
          f"{np.mean((y[m]-b[m])**2):.4f} / {np.mean((y[m]-pc[m])**2):.4f} / {np.mean((y[m]-h[m])**2):.4f} | {b[m].mean():.3f} / {pc[m].mean():.3f} / {h[m].mean():.3f} |")
print(f"| Set | Rows | Played | AUC classic / Platt / {a.label} | Brier classic / Platt / {a.label} | Mean P classic / Platt / {a.label} |")
print("|---|---|---|---|---|---|")
allm = np.ones(len(E), bool); row("All", allm); row("Classic P < 0.8", b < 0.8); row("Classic P 0.8-0.95", (b >= 0.8) & (b < 0.95))
row("Status flagged (not a/none)", ~np.isin(st, ["a", "none", "?"])); row("Status a", st == "a"); row("Status none", st == "none")
row("News line present", news); row("Evidence present", ev); row("No evidence", ~ev)
for s in sorted(set(season)):
    ws = sorted(set(wk[season == s]))
    for i in range(0, len(ws), a.windows):
        chunk = ws[i:i + a.windows]; row(f"{s} GW{chunk[0]}-{chunk[-1]}", (season == s) & np.isin(wk, chunk))

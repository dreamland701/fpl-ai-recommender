"""Decompose E19 adapter deltas into a baseline-proportional shrink and a
player-specific remainder, and score each piece on the GW27-38 holdout.

Writes de-shrunk prediction files (same row order/schema as the E19 SFT
predictions) so backtest-squad can consume them via --llm-predictions.
"""
import json
import sys

import numpy as np

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.llm_adjust import parse_delta_response  # noqa: E402

ROOT = "/home/wescheng/projects/fpl/fpl"
T = "/home/wescheng/projects/fpl/fpl/reports/adapter_bench_2026_09_29"
EX = f"{ROOT}/reports/llm_residual_v2_e19_wideholdout_top256_thru_2526_26_eval_2526_27_38/eval.jsonl"
PR = f"{ROOT}/reports/gemma4_e4b_residual_e19_gw27_38_sft_predictions.jsonl"

examples = [json.loads(line) for line in open(EX)]
preds = [json.loads(line) for line in open(PR)]
assert len(examples) == len(preds)

H = ["1gw", "3gw", "5gw"]
rows = []
for e, p in zip(examples, preds):
    m = e["metadata"]
    d = parse_delta_response(str(p.get("response") or "")) or {}
    b = m["baseline_forecast"]
    lab = m["labels"]
    rows.append({
        "week": int(e["week"]), "pid": m["player_id"], "name": m["player_name"],
        "evid": bool(m.get("evidence_present")),
        **{f"b{h}": b[f"baseline_points_{h}"] for h in H},
        **{f"d{h}": d.get(f"delta_points_{h}", 0.0) for h in H},
        **{f"y{h}": lab[f"points_{h}"] for h in H},
        "bapp": b["baseline_appearance_probability"], "dapp": d.get("delta_appearance_probability", 0.0),
        "yapp": lab["appearance_probability"],
        "bmin": b["baseline_minutes_1gw"], "dmin": d.get("delta_minutes_1gw", 0.0),
    })


def col(key, subset=None):
    source = rows if subset is None else [r for r in rows if subset(r)]
    return np.array([r[key] for r in source], dtype=float)


# Per-week linear shrink fit: d = a + s*b (no labels used -> deployable live).
weeks = sorted({r["week"] for r in rows})
for h in H:
    for w in weeks:
        idx = [i for i, r in enumerate(rows) if r["week"] == w]
        x = np.array([rows[i][f"b{h}"] for i in idx])
        y = np.array([rows[i][f"d{h}"] for i in idx])
        s, a = np.polyfit(x, y, 1)
        for i in idx:
            fit = a + s * rows[i][f"b{h}"]
            rows[i][f"shr{h}"] = fit
            rows[i][f"res{h}"] = rows[i][f"d{h}"] - fit

print(f"rows={len(rows)} weeks={weeks[0]}-{weeks[-1]} evidence_present={sum(r['evid'] for r in rows)}")
print("\n== how much of the delta is a baseline-proportional shrink? (pooled) ==")
for h in H:
    b, d = col(f"b{h}"), col(f"d{h}")
    r = np.corrcoef(b, d)[0, 1]
    s, a = np.polyfit(b, d, 1)
    print(f"  {h}: corr(delta, baseline) {r:+.3f}  R2 {r*r:.3f}  slope {s:+.3f}  intercept {a:+.3f}  "
          f"mean delta {d.mean():+.3f}  share at bound {np.mean(np.isclose(np.abs(d), np.abs(d).max())):.3f}")


def mae(pred, y):
    return float(np.mean(np.abs(pred - y)))


print("\n== MAE decomposition (lower is better) ==")
print(f"  {'subset':28s} {'h':4s} {'classic':>8s} {'+delta':>8s} {'+shrink':>8s} {'+resid':>8s}   n")
subsets = {
    "all": None,
    "evidence present": lambda r: r["evid"],
    "no evidence": lambda r: not r["evid"],
    "top-10% baseline (picked)": None,  # filled below per horizon
}
for h in H:
    thr = np.quantile(col(f"b{h}"), 0.9)
    for label, fn in subsets.items():
        if label.startswith("top-10%"):
            fn = (lambda r, h=h, thr=thr: r[f"b{h}"] >= thr)
        b, d, y = col(f"b{h}", fn), col(f"d{h}", fn), col(f"y{h}", fn)
        shr, res = col(f"shr{h}", fn), col(f"res{h}", fn)
        print(f"  {label:28s} {h:4s} {mae(b, y):8.4f} {mae(b + d, y):8.4f} {mae(b + shr, y):8.4f} {mae(b + res, y):8.4f}   {len(b)}")

print("\n== does the player-specific remainder RANK better? (per-week Spearman of forecast vs realized, top-50 by classic) ==")
from scipy.stats import spearmanr  # noqa: E402
for h in H:
    out = {"classic": [], "+delta": [], "+resid": []}
    for w in weeks:
        wr = sorted([r for r in rows if r["week"] == w], key=lambda r: -r[f"b{h}"])[:50]
        y = [r[f"y{h}"] for r in wr]
        out["classic"].append(spearmanr([r[f"b{h}"] for r in wr], y).correlation)
        out["+delta"].append(spearmanr([r[f"b{h}"] + r[f"d{h}"] for r in wr], y).correlation)
        out["+resid"].append(spearmanr([r[f"b{h}"] + r[f"res{h}"] for r in wr], y).correlation)
    print("  " + h + ": " + "  ".join(f"{k} {np.nanmean(v):+.3f}" for k, v in out.items()))

print("\n== appearance probability (Brier, lower is better) ==")
for label, fn in [("all", None), ("evidence present", lambda r: r["evid"]), ("classic P<0.9", lambda r: r["bapp"] < 0.9)]:
    b, d, y = col("bapp", fn), col("dapp", fn), col("yapp", fn)
    adj = np.clip(b + d, 0, 1)
    print(f"  {label:18s} classic {np.mean((b-y)**2):.4f}  +delta {np.mean((adj-y)**2):.4f}   n={len(b)}")

# Write de-shrunk prediction files in the E19 schema.
def write_variant(path, transform):
    with open(path, "w") as handle:
        for p, r in zip(preds, rows):
            d = parse_delta_response(str(p.get("response") or "")) or {}
            d = transform(dict(d), r)
            q = dict(p)
            q["response"] = json.dumps(d)
            handle.write(json.dumps(q, ensure_ascii=False) + "\n")


def deshrink(d, r):
    for h in H:
        if f"delta_points_{h}" in d:
            d[f"delta_points_{h}"] = r[f"res{h}"]
    return d


def shrink_only(d, r):
    for h in H:
        if f"delta_points_{h}" in d:
            d[f"delta_points_{h}"] = r[f"shr{h}"]
    return d


def evidence_gated(d, r):
    return d if r["evid"] else {}


write_variant(f"{T}/e19_pred_deshrunk.jsonl", deshrink)
write_variant(f"{T}/e19_pred_shrinkonly.jsonl", shrink_only)
write_variant(f"{T}/e19_pred_evidgated.jsonl", evidence_gated)
print("\nwrote variant prediction files to", T)

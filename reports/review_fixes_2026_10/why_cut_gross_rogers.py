"""Why did E20 cut Groß and Rogers beyond the generic shrink despite positive text?

1. GW6 decode: is the "player-specific" part just an artefact of a straight-line
   shrink fit (a curved shrink would leave negative residuals at the top), and
   how unusual are -0.36 / -0.41 against the spread of residuals?
2. Training data (E20 split): did rows whose evidence reads as praise or
   international duty carry negative targets (relative to similar baselines)?
   That is what the adapter could have learned.
3. Holdout (2025-26 GW27-38): when E20 saw such text, did outcomes back the cut?
"""
import json
import re
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.llm_adjust import parse_delta_response  # noqa: E402

ROOT = "/home/wescheng/projects/fpl/fpl"
SPLIT = f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38"
PATTERNS = {
    "praise / award": re.compile(r"player of the month|potm|player of the season|team of the week|outstanding|brilliant|superb|man of the match", re.I),
    "international duty": re.compile(r"nations league|world cup qualif|international (duty|break)|england|for (his|their) country|euro 20\d\d qualif", re.I),
    "transfer frenzy": re.compile(r"most.?bought|most transfers in|most-transferred|transfers in", re.I),
}


def evidence_text(prompt):
    part = prompt.split("Timestamp-safe text evidence:", 1)
    if len(part) < 2 or "No timestamp-safe text evidence is available" in part[1][:200]:
        return ""
    return part[1].split("<|turn>", 1)[0]


def detrend(base, y):
    slope, intercept = np.polyfit(base, y, 1)
    return y - (slope * base + intercept)


def main() -> None:
    # 1. GW6
    ex = [json.loads(l) for l in open(f"{ROOT}/reports/live_gw6_2627_f6_examples.jsonl")]
    pr = {int(json.loads(l)["metadata"]["player_id"]): json.loads(l) for l in open(f"{ROOT}/reports/live_gw6_2627_e20_predictions.jsonl")}
    names, base, delta, texts = [], [], [], []
    for e in ex:
        m = e["metadata"]; pid = int(m["player_id"])
        d = parse_delta_response(pr[pid]["response"]) or {}
        names.append(m["player_name"]); base.append(m["baseline_forecast"]["baseline_points_1gw"])
        delta.append(d.get("delta_points_1gw", 0.0)); texts.append(evidence_text(e["prompt"]))
    base, delta = np.array(base), np.array(delta)
    resid = detrend(base, delta)
    print("GW6: raw deltas are coarse, the adapter writes one decimal:", sorted(set(np.round(delta, 2)))[:12], "...")
    order = np.argsort(base)
    print("mean straight-line residual by classic-forecast band (curvature check):")
    for chunk in np.array_split(order[-200:], 5):
        print(f"  baseline {base[chunk].min():.2f}-{base[chunk].max():.2f}: mean residual {resid[chunk].mean():+.2f} "
              f"(sd {resid[chunk].std():.2f}, n {len(chunk)})")
    top = order[-60:]
    for nm in ("Groß", "Rogers", "B.Fernandes", "De Cuyper", "Haaland", "Saka", "Hall", "Mbeumo"):
        i = names.index(nm)
        pct = (resid[top] < resid[i]).mean() * 100
        print(f"  {nm:12s} baseline {base[i]:.2f} raw delta {delta[i]:+.1f} residual {resid[i]:+.2f} "
              f"(percentile among top-60 forecasts: {pct:.0f})")
    # among top-60 by baseline: does praise text get lower residuals?
    for label, pat in PATTERNS.items():
        hit = [i for i in top if pat.search(texts[i])]
        miss = [i for i in top if i not in hit]
        if hit:
            print(f"  GW6 top-60, {label}: residual {resid[hit].mean():+.2f} (n {len(hit)}) vs others {resid[miss].mean():+.2f} (n {len(miss)})")

    # 2. training targets
    rows = [json.loads(l) for l in open(f"{SPLIT}/train.jsonl")]
    tb, tt, tx = [], [], []
    for r in rows:
        b = r["metadata"]["baseline_forecast"]["baseline_points_1gw"]
        target = json.loads(r["completion"]).get("delta_points_1gw", 0.0) if r.get("completion") else 0.0
        tb.append(b); tt.append(target); tx.append(evidence_text(r["prompt"]))
    tb, tt = np.array(tb), np.array(tt)
    tres = detrend(tb, tt)
    high = tb >= np.quantile(tb, 0.8)
    print(f"\nE20 training rows: {len(rows)}; target = the clipped residual the adapter learns to output")
    for label, pat in PATTERNS.items():
        hit = np.array([bool(pat.search(t)) for t in tx])
        for name, mask in (("all", np.ones_like(hit)), ("top-20% forecasts", high)):
            h, o = hit & mask, (~hit) & mask & np.array([bool(t) for t in tx])
            if h.sum() >= 30:
                print(f"  {label:20s} [{name}]: target residual {tres[h].mean():+.3f} (n {h.sum()}) vs other evidence rows "
                      f"{tres[o].mean():+.3f} (n {o.sum()})")

    # 3. holdout: E20 deltas vs realised residuals for the same text classes
    hx = [json.loads(l) for l in open(f"{SPLIT}/eval.jsonl")]
    hp = {}
    for l in open(f"{ROOT}/reports/gemma4_e4b_residual_e20_gw27_38_sft_predictions.jsonl"):
        p = json.loads(l); hp[(int(p["week"]), int(p["metadata"]["player_id"]))] = p
    hb, hd, hy, htxt = [], [], [], []
    for r in hx:
        m = r["metadata"]
        d = parse_delta_response(hp[(int(r["week"]), int(m["player_id"]))]["response"]) or {}
        hb.append(m["baseline_forecast"]["baseline_points_1gw"]); hd.append(d.get("delta_points_1gw", 0.0))
        hy.append(m["labels"]["points_1gw"]); htxt.append(evidence_text(r["prompt"]))
    hb, hd, hy = np.array(hb), np.array(hd), np.array(hy)
    hres_pred, hres_real = detrend(hb, hd), detrend(hb, hy - hb)
    print("\nHoldout (2025-26 GW27-38): adapter's residual cut vs what actually happened (both net of the baseline trend)")
    for label, pat in PATTERNS.items():
        hit = np.array([bool(pat.search(t)) for t in htxt])
        if hit.sum() >= 20:
            print(f"  {label:20s}: adapter {hres_pred[hit].mean():+.2f} | realised {hres_real[hit].mean():+.2f} (n {hit.sum()})")


if __name__ == "__main__":
    main()

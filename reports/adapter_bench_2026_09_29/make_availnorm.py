"""Variant V3 (pre-registered primary hypothesis, 2026-09-29, written before
any decision backtest of it was run):

The E19 adapter's genuinely player-specific signal is AVAILABILITY
(appearance AUC 0.613 -> 0.734 on GW27-38) while the decision layer consumes
mostly its points shrink. Route the availability signal into points:

    points_h' = classic_points_h * ratio_i / mean_week(ratio)

ratio_i = clip(P_llm / P_classic, 0.6, 1.4). Dividing by the week's mean
ratio removes the global level shift (classic P(app) runs 0.14 low on this
holdout), so only relative availability information re-ranks players.
Expressed as points deltas so backtest-squad --llm-fields points applies it.
"""
import json
import sys
from collections import defaultdict

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.llm_adjust import parse_delta_response  # noqa: E402

ROOT = "/home/wescheng/projects/fpl/fpl"
T = "/home/wescheng/projects/fpl/fpl/reports/adapter_bench_2026_09_29"
EX = sys.argv[1] if len(sys.argv) > 1 else f"{ROOT}/reports/llm_residual_v2_e19_wideholdout_top256_thru_2526_26_eval_2526_27_38/eval.jsonl"
PR = sys.argv[2] if len(sys.argv) > 2 else f"{ROOT}/reports/gemma4_e4b_residual_e19_gw27_38_sft_predictions.jsonl"
OUT = sys.argv[3] if len(sys.argv) > 3 else f"{T}/e19_pred_availnorm.jsonl"

examples = [json.loads(line) for line in open(EX)]
preds = [json.loads(line) for line in open(PR)]
assert len(examples) == len(preds)

ratios = []
by_week = defaultdict(list)
for i, (e, p) in enumerate(zip(examples, preds)):
    b = e["metadata"]["baseline_forecast"]
    d = parse_delta_response(str(p.get("response") or "")) or {}
    old = max(b["baseline_appearance_probability"], 1e-6)
    new = min(1.0, max(0.0, old + d.get("delta_appearance_probability", 0.0)))
    ratio = min(1.4, max(0.6, new / old))
    ratios.append(ratio)
    by_week[int(e["week"])].append(ratio)
mean_by_week = {w: sum(v) / len(v) for w, v in by_week.items()}

with open(OUT, "w") as handle:
    for e, p, ratio in zip(examples, preds, ratios):
        b = e["metadata"]["baseline_forecast"]
        scale = ratio / mean_by_week[int(e["week"])]
        deltas = {
            f"delta_points_{h}": b[f"baseline_points_{h}"] * (scale - 1.0)
            for h in ("1gw", "3gw", "5gw")
        }
        q = dict(p)
        q["response"] = json.dumps(deltas)
        handle.write(json.dumps(q, ensure_ascii=False) + "\n")
print("weekly mean ratio:", {w: round(v, 3) for w, v in sorted(mean_by_week.items())})
print("wrote", OUT)

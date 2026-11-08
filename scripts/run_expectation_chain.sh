#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# Expectation decoding for E20 (inference only), then release the GPU to G5.
# Greedy decoding writes the most likely value of a skewed distribution, which
# turns near-zero expected deltas into cuts (Groß: written -1.2, expected -0.34).
#   1. expected points deltas for the 2025-26 GW27-38 holdout, 2026-27 GW2-5
#      and the GW6 live rows (scripts/expectation_decode.py)
#   2. remove logs/gpu_hold so the waiting G5 launcher starts training
#   3. accuracy and squad backtests vs classic+F6 and greedy E20 (CPU)
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/expectation_chain.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
ADAPTER=artifacts/gemma4_e4b_lora_residual_v2_e20_contract
HOLD_SPLIT=reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38
LIVE_SPLIT=reports/llm_residual_v2_e20_contract_top256_eval_2627_2_5
HOLD_G=reports/gemma4_e4b_residual_e20_gw27_38_sft_predictions.jsonl
LIVE_G=reports/gemma4_e4b_residual_e20_2627_gw2_5_sft_predictions.jsonl
HOLD_E=reports/gemma4_e4b_residual_e20_gw27_38_expectation_predictions.jsonl
LIVE_E=reports/gemma4_e4b_residual_e20_2627_gw2_5_expectation_predictions.jsonl
GW6_E=reports/live_gw6_2627_e20_expectation_predictions.jsonl
OUT=reports/review_fixes_2026_10/bt_expectation; mkdir -p "$OUT"

decode(){ # examples greedy out
  python -u scripts/expectation_decode.py "$1" "$2" "$ADAPTER" "$3" 2 >> logs/expectation_decode.log 2>&1
}
log "=== expectation decode: holdout ==="
decode "$HOLD_SPLIT/eval.jsonl" "$HOLD_G" "$HOLD_E" || { log "holdout decode FAILED"; rm -f logs/gpu_hold; exit 1; }
log "=== expectation decode: 2026-27 GW2-5 ==="
decode "$LIVE_SPLIT/eval.jsonl" "$LIVE_G" "$LIVE_E" || log "live decode FAILED"
log "=== expectation decode: GW6 ==="
decode reports/live_gw6_2627_f6_examples.jsonl reports/live_gw6_2627_e20_predictions.jsonl "$GW6_E" || log "GW6 decode FAILED"
rm -f logs/gpu_hold
log "GPU released to G5"

export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
bt(){ # tag season a b examples preds fields
  local dir="$OUT/$1_$2_$3_$4"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  PYTHONPATH=src nice -n 10 python -m fpl_ai.cli backtest-squad --training-data data/fpl_training_rows_v3_contract_f6.csv \
    --test-season "$2" --initial-train-week-max $(($3 - 1)) --start-week "$3" --end-week "$4" --output-dir "$dir" \
    --llm-examples "$5" --llm-predictions "$6" --llm-fields "$7" --skip-league-average-fetch > "$dir.log" 2>&1
}
log "=== backtests ==="
for W in "27 30" "31 34" "35 38"; do
  set -- $W
  bt exp_points 2025-26 $1 $2 "$HOLD_SPLIT/eval.jsonl" "$HOLD_E" points &
  bt exp_all 2025-26 $1 $2 "$HOLD_SPLIT/eval.jsonl" "$HOLD_E" all &
done
[ -s "$LIVE_E" ] && bt exp_all 2026-27 2 5 "$LIVE_SPLIT/eval.jsonl" "$LIVE_E" all &
wait
log "$(python3 - <<'PYEOF'
import json, os
import numpy as np
O = "reports/review_fixes_2026_10/bt_expectation"
def tot(d):
    f = f"{d}/rolling_squad_backtest.json"
    return json.load(open(f))["total_actual_points"] if os.path.exists(f) else None
lines = ["holdout squad points (classic+F6 266/229/258 = 753; greedy E20 points 225/216/263 = 704):"]
for tag in ("exp_points", "exp_all"):
    w = [tot(f"{O}/{tag}_2025-26_{a}_{b}") for a, b in ((27, 30), (31, 34), (35, 38))]
    lines.append(f"  {tag}: {w} = {sum(x for x in w if x is not None)}")
lines.append(f"live 2026-27 GW2-5 (classic+F6 242, greedy E20 all 247): exp_all {tot(f'{O}/exp_all_2026-27_2_5')}")
for name, ex, g, e in (("holdout", "reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/eval.jsonl",
                        "reports/gemma4_e4b_residual_e20_gw27_38_sft_predictions.jsonl", "reports/gemma4_e4b_residual_e20_gw27_38_expectation_predictions.jsonl"),
                       ("live", "reports/llm_residual_v2_e20_contract_top256_eval_2627_2_5/eval.jsonl",
                        "reports/gemma4_e4b_residual_e20_2627_gw2_5_sft_predictions.jsonl", "reports/gemma4_e4b_residual_e20_2627_gw2_5_expectation_predictions.jsonl")):
    if not os.path.exists(e):
        continue
    lab = {}
    for l in open(ex):
        r = json.loads(l); m = r["metadata"]; b = m["baseline_forecast"]
        lab[(int(r["week"]), int(m["player_id"]))] = (b["baseline_points_1gw"], b["baseline_points_3gw"], b["baseline_points_5gw"],
                                                       m["labels"]["points_1gw"], m["labels"].get("points_3gw"), m["labels"].get("points_5gw"))
    def deltas(path):
        out = {}
        for l in open(path):
            p = json.loads(l); r = p["response"]
            try:
                d = json.loads(r[: r.index("}") + 1])
            except Exception:
                continue
            out[(int(p["week"]), int(p["metadata"]["player_id"]))] = d
        return out
    G, E = deltas(g), deltas(e)
    keys = [k for k in lab if k in G and k in E]
    for h, j in (("1gw", 0), ("3gw", 1), ("5gw", 2)):
        rows = [(lab[k][j], G[k].get(f"delta_points_{h}", 0.0), E[k].get(f"delta_points_{h}", 0.0), lab[k][3 + j]) for k in keys if lab[k][3 + j] is not None]
        b, dg, de, y = map(np.array, zip(*rows))
        f = lambda pred: f"RMSE {np.sqrt(np.mean((pred - y) ** 2)):.3f} MAE {np.mean(np.abs(pred - y)):.3f} bias {np.mean(pred - y):+.2f}"
        lines.append(f"{name} {h} (n {len(y)}): classic {f(b)} | greedy {f(b + dg)} | expectation {f(b + de)}")
print("\n".join(lines))
PYEOF
)"
log "EXPECTATION CHAIN DONE"

#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# Queued behind G5b (2026-10-10). Wes: "data leakage, making sure data is clean,
# is very important" and "let's try to get [RL] to work".
#   1. Late-article test (inference): E20 re-decoded on holdout and live-season
#      prompts with articles from the final 24 h removed (live decisions never
#      see them), then accuracy and squad backtests against the originals.
#   2. GW6 final: expected deltas for all 667 rows, so GW6 can be scored in the
#      accuracy ledger once it settles.
#   3. G6 = imitation then RL: SFT on the same-chips planner's plans (starts RL
#      at planner level instead of 17 points behind), closed-loop eval of the
#      imitation policy, GRPO from it (lr 5e-5, temperature 1.0, no KL), eval.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/after_g5b.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
E20=artifacts/gemma4_e4b_lora_residual_v2_e20_contract
LA=reports/review_fixes_2026_10/late_articles
HOLD=reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/eval.jsonl
LIVE=reports/llm_residual_v2_e20_contract_top256_eval_2627_2_5/eval.jsonl
STATES=reports/grpo_states_v2/2025-26-holdout.jsonl

until grep -aq "G5B CHAIN DONE\|G5b TRAINING FAILED" logs/g5_chain.log || ! pgrep -f "^bash scripts/run_g5b.sh" >/dev/null; do sleep 300; done
log "G5b finished: $(grep -a 'RESULT' logs/g5_chain.log | tail -1 | cut -c21-)"

log "=== 1. late-article test ==="
for set in holdout live; do
  python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$LA/${set}_changed.jsonl" \
    --output "$LA/${set}_changed_greedy.jsonl" --adapter-path "$E20" --max-new-tokens 96 --no-4bit --batch-size 16 >> "$LOG" 2>&1 \
    && python -u scripts/expectation_decode.py "$LA/${set}_changed.jsonl" "$LA/${set}_changed_greedy.jsonl" "$E20" \
       "$LA/${set}_changed_expected.jsonl" 0 >> "$LOG" 2>&1 || log "$set late-article decode FAILED"
done
python3 reports/review_fixes_2026_10/late_article_test.py merge "$HOLD" reports/gemma4_e4b_residual_e20_gw27_38_sft_predictions.jsonl "$LA/holdout_changed_greedy.jsonl" "$LA/holdout_greedy.jsonl" >> "$LOG"
python3 reports/review_fixes_2026_10/late_article_test.py merge "$HOLD" reports/gemma4_e4b_residual_e20_gw27_38_expectation_predictions.jsonl "$LA/holdout_changed_expected.jsonl" "$LA/holdout_expected.jsonl" >> "$LOG"
python3 reports/review_fixes_2026_10/late_article_test.py merge "$LIVE" reports/gemma4_e4b_residual_e20_2627_gw2_5_sft_predictions.jsonl "$LA/live_changed_greedy.jsonl" "$LA/live_greedy.jsonl" >> "$LOG"
python3 reports/review_fixes_2026_10/late_article_test.py merge "$LIVE" reports/gemma4_e4b_residual_e20_2627_gw2_5_expectation_predictions.jsonl "$LA/live_changed_expected.jsonl" "$LA/live_expected.jsonl" >> "$LOG"
python3 scripts/track_sft_accuracy.py \
  --set "Holdout, articles up to the deadline (as trained)" "$HOLD" reports/gemma4_e4b_residual_e20_gw27_38_sft_predictions.jsonl reports/gemma4_e4b_residual_e20_gw27_38_expectation_predictions.jsonl \
  --set "Holdout, no articles from the last 24 h" "$HOLD" "$LA/holdout_greedy.jsonl" "$LA/holdout_expected.jsonl" \
  --set "Live GW2-5, articles up to the deadline" "$LIVE" reports/gemma4_e4b_residual_e20_2627_gw2_5_sft_predictions.jsonl reports/gemma4_e4b_residual_e20_2627_gw2_5_expectation_predictions.jsonl \
  --set "Live GW2-5, no articles from the last 24 h" "$LIVE" "$LA/live_greedy.jsonl" "$LA/live_expected.jsonl" \
  --out-md "$LA/accuracy.md" > /dev/null 2>&1 || log "late-article accuracy FAILED"
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
bt(){ # tag season a b examples preds
  local dir="$LA/bt_$1_$2_$3_$4"
  PYTHONPATH=src nice -n 10 python -m fpl_ai.cli backtest-squad --training-data data/fpl_training_rows_v3_contract_f6.csv \
    --test-season "$2" --initial-train-week-max $(($3 - 1)) --start-week "$3" --end-week "$4" --output-dir "$dir" \
    --llm-examples "$5" --llm-predictions "$6" --llm-fields all --skip-league-average-fetch > "$dir.log" 2>&1
}
for W in "27 30" "31 34" "35 38"; do set -- $W; bt exp24h 2025-26 $1 $2 "$HOLD" "$LA/holdout_expected.jsonl" & done
bt exp24h 2026-27 2 5 "$LIVE" "$LA/live_expected.jsonl" &
wait
log "late-article squad points (SFT average, all fields; with late articles: holdout 224/248/264 = 736, live 256): $(python3 - <<'PYEOF'
import json, os
d = "reports/review_fixes_2026_10/late_articles"
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
w = [tot(f"{d}/bt_exp24h_2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
print(f"holdout {w} = {sum(x for x in w if x is not None)}, live {tot(f'{d}/bt_exp24h_2026-27_2_5/rolling_squad_backtest.json')}")
PYEOF
)"

log "=== 2. GW6 final: expected deltas for all rows ==="
python -u scripts/expectation_decode.py reports/live_gw6final_2627_f6_examples.jsonl reports/live_gw6final_2627_e20_predictions.jsonl \
  "$E20" reports/live_gw6final_2627_e20_expectation_predictions.jsonl 0 >> "$LOG" 2>&1 || log "GW6 final expectation FAILED"

log "=== 3. G6: imitation of the planner ==="
IL=artifacts/gemma4_e4b_plan_imitation_g6
FPL_GEMMA_MODEL_PATH=google/gemma-4-E4B-it FPL_GEMMA_LOAD_IN_4BIT=false FPL_GEMMA_DATA_DIR=reports/grpo_states_v2/g6_imitation \
FPL_GEMMA_OUTPUT_DIR="$IL" FPL_GEMMA_NUM_EPOCHS=2 FPL_GEMMA_LEARNING_RATE=1e-4 FPL_GEMMA_TRAIN_BATCH_SIZE=1 FPL_GEMMA_GRAD_ACCUM=8 \
FPL_GEMMA_EVAL_STEPS=30 FPL_GEMMA_SAVE_STEPS=30 FPL_GEMMA_LORA_DROPOUT=0.0 FPL_GEMMA_MAX_SEQ_LENGTH=2048 \
FPL_GEMMA_TARGET_SUFFIXES=self_attn.q_proj.weight,self_attn.k_proj.weight,self_attn.v_proj.weight,self_attn.o_proj.weight \
  python train_gemma_sft.py >> logs/train_g6_imitation.log 2>&1
[ -s "$IL/adapter_model.safetensors" ] || { log "G6 IMITATION FAILED (no adapter)"; exit 1; }
python3 scripts/run_grpo_plan_eval_v2.py --states "$STATES" --adapter-path "$IL" --output reports/grpo_states_v2/eval_holdout_g6_il.json >> "$LOG" 2>&1 \
  || log "imitation eval FAILED"
log "imitation policy: $(python3 -c "import json; d=json.load(open('reports/grpo_states_v2/eval_holdout_g6_il.json')); print(d['summary'], 'invalid', d['invalid_weeks'])" 2>/dev/null)"

log "=== 3b. G6: GRPO from the imitation policy ==="
G6=artifacts/gemma4_e4b_grpo_plan_g6
rm -rf "$G6"
FPL_GRPO_INIT_ADAPTER="$IL" FPL_GRPO_KL_BETA=0 FPL_GRPO_LEARNING_RATE=5e-5 FPL_GRPO_TEMPERATURE=1.0 FPL_GRPO_NUM_EPOCHS=3 \
FPL_GRPO_OUTPUT_DIR="$G6" python train_gemma_grpo_plan_v2.py >> logs/train_g6.log 2>&1 &
TRAIN_PID=$!
echo 800 > "/proc/$TRAIN_PID/oom_score_adj" 2>/dev/null || true
wait "$TRAIN_PID"
[ -s "$G6/adapter_model.safetensors" ] || { log "G6 GRPO FAILED (no adapter)"; exit 1; }
python3 scripts/run_grpo_plan_eval_v2.py --states "$STATES" --adapter-path "$G6" --output reports/grpo_states_v2/eval_holdout_g6.json >> "$LOG" 2>&1 \
  || log "G6 eval FAILED"
log "RESULT: $(python3 - <<'PYEOF'
import json, os
out = []
for tag, f in (("G6 (imitation + RL)", "eval_holdout_g6.json"), ("imitation only", "eval_holdout_g6_il.json"), ("G5b", "eval_holdout_g5b.json"),
               ("untrained", "eval_holdout_g5_base.json")):
    p = f"reports/grpo_states_v2/{f}"
    if os.path.exists(p):
        d = json.load(open(p)); s = d["summary"]
        out.append(f"{tag} {s.get('policy')} (invalid {len(d['invalid_weeks'])})")
        planner, classic = s["planner"], s["classic_no_chips"]
print(" | ".join(out) + f" | same-chips planner {planner} | classic no chips {classic}")
PYEOF
)"
log "AFTER-G5B CHAIN DONE"

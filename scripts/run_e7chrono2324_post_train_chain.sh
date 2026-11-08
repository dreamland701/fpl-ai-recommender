#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after chrono-2324 training (the approved sequence, 2026-07-21):
#   1. chrono-2324 SFT inference on its two legal surfaces:
#        - its own eval (2023-24 GW12-38, 6,912 rows)
#        - evalext_2425gw2_11 (2024-25 GW2-11 early, 2,560 rows)
#   2. build the remaining adjusted G2 state caches (2023-24, 2024-25)
#      with snippet-mode=llm from the condensation summaries
#   3. G2-v2 dry-run (reward-path + episode-count sanity on the real caches)
#   4. launch G2-v2 plan-GRPO on the full deployment-regime states
# Artifact-verified at every stage; any failure aborts before G2 launch.

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_e4b_residual_e7chrono2324_top256_scout.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e7chrono2324_top256_scout"
CHAINLOG="$ROOT/logs/e7chrono2324_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for chrono-2324 final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: trainer log static for 30 min and no train_runtime"
  fi
done
log "chrono-2324 training complete — starting SFT inference"

MODEL="google/gemma-4-E4B-it"
run_predict() {
  # $1 = examples path, $2 = output path, $3 = label
  python -u "$ROOT/eval_gemma_responses.py" \
    --model-path "$MODEL" \
    --examples "$1" \
    --output "$2" \
    --adapter-path "$ADAPTER" \
    --max-new-tokens 96 \
    --no-4bit \
    --batch-size 16 \
    --resume >> "$CHAINLOG.inference" 2>&1
  local status=$?
  local want got
  want=$(wc -l < "$1")
  got=$(wc -l < "$2" 2>/dev/null || echo 0)
  if [ "$status" -eq 0 ] && [ "$got" = "$want" ]; then
    log "predict done: $3 -> $2 ($got rows)"
  else
    log "PREDICT FAILED: $3 (exit $status, $got/$want rows) — aborting chain"
    exit 1
  fi
}

run_predict \
  "$ROOT/reports/llm_residual_v2_e7chrono2324_top256_scout_thru_2324gw11_eval_2324gw12_38/eval.jsonl" \
  "$ROOT/reports/gemma4_e4b_residual_e7chrono2324_2324gw12_38_sft_predictions.jsonl" \
  "eval_2324gw12_38"

run_predict \
  "$ROOT/reports/llm_residual_v2_e7chrono2324_evalext_2425gw2_11/eval.jsonl" \
  "$ROOT/reports/gemma4_e4b_residual_e7chrono2324_evalext_2425gw2_11_sft_predictions.jsonl" \
  "evalext_2425gw2_11"

log "inference done — building adjusted state caches (2023-24, 2024-25)"
python3 scripts/build_adjusted_grpo_states.py \
  --seasons "2023-24,2024-25" \
  --snippet-mode llm \
  --summaries reports/grpo_condense_summaries.jsonl >> "$CHAINLOG.inference" 2>&1 \
  && log "adjusted caches built: 2023-24, 2024-25" \
  || { log "CACHE BUILD FAILED — aborting chain"; exit 1; }

# G2-v2 configuration (deployment-regime training):
#   - adjusted states only, seasons with a legal adapter
#   - REQUIRE_DELTAS drops 2023-24 GW2-11 (no legal adapter -> off-regime)
#   - 2025-26 GW12-30 stays untouched as the composed-stack eval
export FPL_GRPO_STATES_DIR="$ROOT/reports/grpo_states_adjusted"
export FPL_GRPO_TRAIN_SEASONS="2023-24,2024-25,2025-26-early"
export FPL_GRPO_REQUIRE_DELTAS=1
export FPL_GRPO_MAX_PROMPT_LENGTH=2816
export FPL_GRPO_OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_grpo_plan_v2"

log "running G2-v2 dry-run"
python3 train_gemma_grpo_plan.py --dry-run > "$ROOT/logs/grpo_plan_v2_dryrun.log" 2>&1 \
  && log "dry-run OK: $(grep -E '^episodes:' "$ROOT/logs/grpo_plan_v2_dryrun.log")" \
  || { log "DRY-RUN FAILED — aborting chain (see logs/grpo_plan_v2_dryrun.log)"; exit 1; }

log "launching G2-v2 plan-GRPO"
echo 900 > /proc/self/oom_score_adj 2>/dev/null || true
nohup python3 train_gemma_grpo_plan.py > "$ROOT/logs/train_grpo_plan_v2.log" 2>&1 &
sleep 90
TRAINER_PID=$(ps -ef | grep "python3 train_gemma_grpo_plan.py" | grep -v grep | awk '{print $2}' | head -1)
if [ -n "$TRAINER_PID" ] && readlink /proc/$TRAINER_PID/exe 2>/dev/null | grep -q python; then
  echo 800 > /proc/$TRAINER_PID/oom_score_adj 2>/dev/null || true
  log "G2-v2 trainer verified, pid $TRAINER_PID (oom guard 800)"
else
  log "G2-V2 LAUNCH FAILED — no verified python trainer process (see logs/train_grpo_plan_v2.log)"
fi
log "CHAIN COMPLETE"

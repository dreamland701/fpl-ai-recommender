#!/usr/bin/env bash
set -uo pipefail

# Chrono-2425 SFT-only inference batch (deployment-regime G2 states):
#   1. evalext_2425gw12_38  (2024-25 GW12-38, legal for chrono-2425)
#   2. evalext_2526gw2_11   (2025-26 GW2-11 early, legal for chrono-2425)
#   3. condensation pass: base model summarizes each scout article to
#      <=30 words for the G2 evidence snippets (Wes's idea, 2026-07-19)
# Then auto-launches chrono-2324 training on the freed GPU (next approved
# stage regardless of these results). Artifact-verified throughout.

ROOT="/home/wescheng/projects/fpl/fpl"
LOG="$ROOT/logs/e7chrono2425_inference_batch.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
log "inference batch starting"

MODEL="google/gemma-4-E4B-it"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e7chrono2425_top256_scout"

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
    --resume >> "$LOG" 2>&1 \
    && log "predict done: $3 -> $2 ($(wc -l < "$2") rows)" \
    || log "PREDICT FAILED: $3"
}

run_predict \
  "$ROOT/reports/llm_residual_v2_e7chrono2425_evalext_2425gw12_38/eval.jsonl" \
  "$ROOT/reports/gemma4_e4b_residual_e7chrono2425_evalext_2425gw12_38_sft_predictions.jsonl" \
  "evalext_2425gw12_38"

run_predict \
  "$ROOT/reports/llm_residual_v2_e7chrono2425_evalext_2526gw2_11/eval.jsonl" \
  "$ROOT/reports/gemma4_e4b_residual_e7chrono2425_evalext_2526gw2_11_sft_predictions.jsonl" \
  "evalext_2526gw2_11"

log "predictions done — running condensation pass (base model, no adapter)"
python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL" \
  --examples "$ROOT/reports/grpo_condense_prompts.jsonl" \
  --output "$ROOT/reports/grpo_condense_summaries.jsonl" \
  --max-new-tokens 64 \
  --no-4bit \
  --batch-size 16 \
  --resume >> "$LOG" 2>&1 \
  && log "condensation done -> reports/grpo_condense_summaries.jsonl ($(wc -l < "$ROOT/reports/grpo_condense_summaries.jsonl") rows)" \
  || log "CONDENSATION FAILED"

log "inference batch complete — launching chrono-2324 training"
chmod +x "$ROOT/scripts/run_gemma_e4b_residual_e7chrono2324.sh"
nohup "$ROOT/scripts/run_gemma_e4b_residual_e7chrono2324.sh" > "$ROOT/logs/e7chrono2324_train_nohup.log" 2>&1 &
sleep 120
TRAINER_PID=$(ps -ef | grep "python train_gemma_sft.py" | grep -v grep | awk '{print $2}' | head -1)
if [ -n "$TRAINER_PID" ] && readlink /proc/$TRAINER_PID/exe 2>/dev/null | grep -q python; then
  echo 800 > /proc/$TRAINER_PID/oom_score_adj 2>/dev/null || true
  log "chrono-2324 trainer verified, pid $TRAINER_PID (oom guard 800)"
else
  log "CHRONO-2324 LAUNCH FAILED — no verified python trainer process"
fi
log "BATCH CHAIN COMPLETE"

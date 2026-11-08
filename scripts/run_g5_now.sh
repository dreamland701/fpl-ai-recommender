#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# G5 training started immediately (Wes 2026-10-08: "the GPU is free right now,
# so if you want to launch something"), with a guard so it can never delay the
# GW6 final packet: if training is still running at 2026-10-09 16:30 UTC it is
# stopped (checkpoints every 50 steps), the E20 chain builds the packet, and
# training resumes from the latest checkpoint. Then the closed-loop eval.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/g5_chain.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
OUT=artifacts/gemma4_e4b_grpo_plan_g5
export FPL_GRPO_OUTPUT_DIR="$OUT" FPL_GRPO_NUM_EPOCHS=6
PAUSE_AT=$(date -d '2026-10-09T16:30:00Z' +%s)

# logs/gpu_hold: an interactive GPU job (interpretability scoring) asked for the GPU first.
while [ -e logs/gpu_hold ] || pgrep -f "^python.*(eval_gemma_responses|train_gemma|sft_interpret|decode_check)" >/dev/null 2>&1; do sleep 60; done
python3 train_gemma_grpo_plan_v2.py --dry-run >> "$LOG" 2>&1 || { log "GATE FAILED: dry run"; exit 1; }
log "dry run passed; G5 training starts now"

train(){ # [checkpoint]
  if [ -n "${1:-}" ]; then export FPL_GRPO_RESUME_FROM_CHECKPOINT="$1"; fi
  ( echo 800 > /proc/self/oom_score_adj ) 2>/dev/null
  python train_gemma_grpo_plan_v2.py >> logs/train_g5.log 2>&1 &
  TRAIN_PID=$!
}
latest_checkpoint(){ ls -d "$OUT"/checkpoint-* 2>/dev/null | sort -t- -k2 -n | tail -1; }

train ""
while kill -0 "$TRAIN_PID" 2>/dev/null; do
  if [ "$(date +%s)" -ge "$PAUSE_AT" ] && ! grep -aq "E20 CHAIN DONE" logs/e20_chain.log 2>/dev/null; then
    log "pausing G5 for the GW6 final refresh (latest checkpoint: $(latest_checkpoint))"
    kill "$TRAIN_PID"; wait "$TRAIN_PID" 2>/dev/null
    until grep -aq "E20 CHAIN DONE" logs/e20_chain.log 2>/dev/null; do sleep 300; done
    while pgrep -f "^python.*(eval_gemma_responses|train_gemma)" >/dev/null 2>&1; do sleep 60; done
    CKPT=$(latest_checkpoint)
    log "GW6 packet done; resuming G5 from ${CKPT:-scratch}"
    train "$CKPT"
  fi
  sleep 60
done
wait "$TRAIN_PID"; rc=$?
log "G5 training exited rc=$rc"
[ -s "$OUT/adapter_model.safetensors" ] || { log "G5 TRAINING FAILED (no adapter)"; exit 1; }

log "=== closed-loop holdout eval (2025-26 GW27-38) ==="
python3 scripts/run_grpo_plan_eval_v2.py --states reports/grpo_states_v2/2025-26-holdout.jsonl \
  --adapter-path "$OUT" --output reports/grpo_states_v2/eval_holdout_g5.json >> "$LOG" 2>&1 || { log "eval FAILED"; exit 1; }
log "RESULT: $(python3 -c "
import json; d = json.load(open('reports/grpo_states_v2/eval_holdout_g5.json'))
s = d['summary']; print(f\"policy {s.get('policy')} | same-chips planner {s['planner']} | classic no chips {s['classic_no_chips']} | invalid weeks {d['invalid_weeks']}\")")"
log "G5 CHAIN DONE"

#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# G5: RL decision layer retrained on the rebuilt environment (approved by Wes
# 2026-10-07: "the RL will need env rebuild ... pls proceed when ready / GPU
# has cycles"). Starts only after the E20 chain has produced the GW6 final
# packet, so it can never delay a deadline sheet.
#
#   1. wait for "E20 CHAIN DONE" and a free GPU
#   2. gate: state caches present + CPU dry-run of the reward path
#   3. train G5 (train_gemma_grpo_plan_v2.py)
#   4. closed-loop holdout eval (2025-26 GW27-38) vs the same-chips planner
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/g5_chain.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1
OUT=artifacts/gemma4_e4b_grpo_plan_g5

log "armed; waiting for the E20 chain to finish (GW6 final packet first)"
until grep -aq "E20 CHAIN DONE" logs/e20_chain.log 2>/dev/null; do sleep 300; done
while pgrep -f "^python.*(eval_gemma_responses|train_gemma)" >/dev/null 2>&1; do sleep 120; done
log "E20 chain done and GPU free"

for key in 2022-23 2023-24 2024-25 2025-26-train 2025-26-holdout; do
  [ -s "reports/grpo_states_v2/$key.jsonl" ] || { log "GATE FAILED: missing state cache $key"; exit 1; }
done
python3 train_gemma_grpo_plan_v2.py --dry-run >> "$LOG" 2>&1 || { log "GATE FAILED: dry run"; exit 1; }
log "dry run passed"

export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GRPO_OUTPUT_DIR="$OUT"
export FPL_GRPO_NUM_EPOCHS=6
echo 800 > /proc/self/oom_score_adj 2>/dev/null || true
log "=== G5 training -> $OUT ==="
python train_gemma_grpo_plan_v2.py 2>&1 | tee logs/train_g5.log
rc=${PIPESTATUS[0]}
log "G5 training exited rc=$rc"
[ "$rc" -eq 0 ] && [ -s "$OUT/adapter_model.safetensors" ] || { log "G5 TRAINING FAILED"; exit 1; }

log "=== closed-loop holdout eval (2025-26 GW27-38) ==="
python3 scripts/run_grpo_plan_eval_v2.py --states reports/grpo_states_v2/2025-26-holdout.jsonl \
  --adapter-path "$OUT" --output reports/grpo_states_v2/eval_holdout_g5.json >> "$LOG" 2>&1 || { log "eval FAILED"; exit 1; }
log "RESULT: $(python3 -c "
import json; d = json.load(open('reports/grpo_states_v2/eval_holdout_g5.json'))
s = d['summary']; print(f\"policy {s.get('policy')} | same-chips planner {s['planner']} | classic no chips {s['classic_no_chips']} | invalid weeks {d['invalid_weeks']}\")")"
log "G5 CHAIN DONE"

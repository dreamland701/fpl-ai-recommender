#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after G1 GRPO training: run the decision eval on the held-out
# 2025-26 GW12-30 states as soon as the final adapter lands. Aborts loudly
# if the trainer dies before saving. Same rationale as the E6 chain:
# approved mechanical successors fire on disk, monitors only inform.

ROOT="/home/wescheng/projects/fpl/fpl"
ADAPTER="$ROOT/artifacts/gemma4_e4b_grpo_decision_v1"
TRAINLOG="$ROOT/logs/train_grpo_v1.log"
CHAINLOG="$ROOT/logs/g1_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for G1 final adapter"

while [ ! -s "$ADAPTER/adapter_model.safetensors" ] || ! grep -q "train_runtime" "$TRAINLOG"; do
  if ! pgrep -f "python3 train_gemma_grpo.py" > /dev/null; then
    sleep 30  # grace for the save racing the exit
    if [ ! -s "$ADAPTER/adapter_model.safetensors" ]; then
      log "CHAIN ABORTED: G1 exited without saving the adapter"
      exit 1
    fi
    break
  fi
  sleep 300
done
log "G1 adapter present — launching decision eval"

echo 900 > /proc/self/oom_score_adj 2>/dev/null || true
python3 scripts/run_grpo_decision_eval.py \
  --adapter-path "$ADAPTER" \
  --output reports/grpo_decision_eval_v1.json \
  > logs/grpo_decision_eval_v1.log 2>&1 \
  && log "G1 DECISION EVAL DONE: $(python3 -c "import json; d=json.load(open('reports/grpo_decision_eval_v1.json')); print({k: v for k, v in d.items() if not isinstance(v, (list, dict))})" 2>/dev/null | head -c 300)" \
  || log "G1 DECISION EVAL FAILED (see logs/grpo_decision_eval_v1.log)"

log "CHAIN COMPLETE"

#!/usr/bin/env bash
set -uo pipefail
# Auto-launch E14 (wider quality windows) once the G4 gate chain completes
# and the GPU is free. Approved stage (Wes 2026-09-04: "more context").
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
LOG="logs/e14_launch_chain.log"; log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
log "armed; waiting for G4 CHAIN COMPLETE/FAILED"
until grep -qE "G4 CHAIN COMPLETE|G4 CHAIN FAILED" logs/g4_post_train_chain.log 2>/dev/null; do sleep 900; done
until ! pgrep -f "eval_gemma_responses|train_gemma_grpo_forecast" >/dev/null; do sleep 120; done
log "GPU free — launching E14 training + its post-train eval chain"
setsid nohup bash scripts/run_gemma_e4b_residual_e14_wide.sh > logs/e14_train_launcher.log 2>&1 < /dev/null &
setsid nohup bash scripts/run_e14_post_train_chain.sh > logs/e14_post_chain_launcher.log 2>&1 < /dev/null &
sleep 300
if grep -qiE "traceback|error" logs/train_e4b_residual_e14_wide.log 2>/dev/null || ! pgrep -f train_gemma_sft.py >/dev/null; then
  log "E14 LAUNCH FAILED — check logs/train_e4b_residual_e14_wide.log"; exit 1
fi
log "E14 TRAINING LAUNCHED — pid $(pgrep -f train_gemma_sft.py | head -1); ~75h (seq 2048)"

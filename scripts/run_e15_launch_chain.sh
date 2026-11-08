#!/usr/bin/env bash
set -uo pipefail
# Launch E15 once E14 finishes and its eval releases the GPU.
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
LOG=logs/e15_launch_chain.log; log(){ echo "$(date '+%F %T') $*" >> $LOG; }
log "armed; waiting for E14 train_runtime"
until tr '\r' '\n' < logs/train_e4b_residual_e14_wide.log 2>/dev/null | grep -q train_runtime; do
  ps -eo args | grep -q "[t]rain_gemma_sft.py" || { sleep 300; tr '\r' '\n' < logs/train_e4b_residual_e14_wide.log 2>/dev/null | grep -q train_runtime || { log "E14 DIED without finishing — not launching E15"; exit 1; }; }
  sleep 900
done
log "E14 done; waiting for GPU to clear (its eval chain runs first)"
until ! ps -eo args | grep -qE "[t]rain_gemma_sft.py|[e]val_gemma_responses"; do sleep 300; done
log "GPU free — launching E15 + eval chain"
setsid nohup bash scripts/run_gemma_e4b_residual_e15_selection.sh > logs/e15_train_launcher.log 2>&1 < /dev/null &
setsid nohup bash scripts/run_e15_post_train_chain.sh > logs/e15_post_chain_launcher.log 2>&1 < /dev/null &
sleep 300
ps -eo args | grep -q "[t]rain_gemma_sft.py" && log "E15 TRAINING LAUNCHED" || log "E15 LAUNCH FAILED — check logs/train_e4b_residual_e15_selection.log"

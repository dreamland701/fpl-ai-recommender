#!/usr/bin/env bash
set -uo pipefail
# Serial GPU queue: wait for the GW4 decode to finish, then resume E14
# from checkpoint-1000 (reboot 2026-09-08 killed it at 1045/2368).
cd /home/wescheng/projects/fpl/fpl
LOG=logs/gw4_then_e14_chain.log
log() { echo "$(date '+%F %T') $*" >> $LOG; }
log "armed: waiting for GW4 decode to reach 654 rows"
until [ "$(wc -l < reports/live_gw4_2627_e11full_predictions.jsonl 2>/dev/null || echo 0)" -ge 654 ]; do
  ps -eo args | grep -q "[e]val_gemma_responses.*live_gw4" || { sleep 60; [ "$(wc -l < reports/live_gw4_2627_e11full_predictions.jsonl 2>/dev/null || echo 0)" -ge 654 ] || { log "GW4 DECODE DIED EARLY at $(wc -l < reports/live_gw4_2627_e11full_predictions.jsonl 2>/dev/null || echo 0)/654"; exit 1; }; }
  sleep 120
done
log "GW4 decode complete — resuming E14 from checkpoint-1000"
until ! ps -eo args | grep -q "[e]val_gemma_responses"; do sleep 60; done
export FPL_GEMMA_RESUME_FROM_CHECKPOINT="/home/wescheng/projects/fpl/fpl/artifacts/gemma4_e4b_lora_residual_v2_e14_wide/checkpoint-1000"
setsid nohup bash scripts/run_gemma_e4b_residual_e14_wide.sh > logs/e14_resume_launcher.log 2>&1 < /dev/null &
sleep 300
ps -eo args | grep -q "[t]rain_gemma_sft.py" && log "E14 RESUMED from checkpoint-1000" || log "E14 RESUME FAILED — check logs/train_e4b_residual_e14_wide.log"
setsid nohup bash scripts/run_e14_post_train_chain.sh > logs/e14_post_chain_launcher.log 2>&1 < /dev/null &
log "E14 post-train eval chain re-armed"

#!/usr/bin/env bash
# H3 launcher (2026-10-15): waits for the queue tail (R4 -> GW7 shadow read -> R5) to finish, then runs the H3 chain
# unless logs/SKIP_H3 exists, then the H1 shadow read on the GW7 final corpus if Friday's refresh has built it.
cd /home/wescheng/projects/fpl/fpl; LOG=logs/gpu_queue_1015.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
log "H3 launcher armed (pid $$): waits for QUEUE DONE"
until grep -q "^.*QUEUE DONE" logs/gpu_queue_1015.log 2>/dev/null; do sleep 120; done
while pgrep -f "avail_policy_eval|train_gemma|reghead_predict" >/dev/null; do sleep 60; done
if [ -f logs/SKIP_H3 ]; then log "H3 skipped (flag)"; else
  log "H3 start"; /usr/bin/bash scripts/run_h3_avail_chain.sh; log "H3 end: $(grep -a RESULT logs/h3_chain.log | tail -1)"; fi
if [ -s reports/live_gw7final_2627_f6_examples.jsonl ] && [ ! -s reports/h_series/h1_gw7final_pred.jsonl ]; then
  log "H1 shadow read gw7final start"
  ( source /home/wescheng/venvs/fpl-gemma-lite/bin/activate; export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
    python3 -u scripts/reghead_predict.py reports/live_gw7final_2627_f6_examples.jsonl artifacts/gemma4_e4b_h1_reghead_e22 reports/h_series/h1_gw7final_pred.jsonl 8 ) >> logs/h1_shadow_gw7final.log 2>&1 \
    && log "H1 shadow read gw7final end: $(tail -1 logs/h1_shadow_gw7final.log)" || log "H1 shadow read gw7final FAILED"
fi
log "H3 QUEUE DONE"

#!/usr/bin/env bash
# GPU queue C (2026-10-15 22:00 PDT): ONE sequential poller replacing run_gpu_queue_1015b.sh and run_h3_queue.sh.
# (The H3 launcher's own "armed ... waits for QUEUE DONE" log line matched the sentinel it grepped for, so H3 started
# while the queue tail launched the GW7 shadow read: two GPU jobs at once. Never log the sentinel you wait for.)
# Order: wait for the running H1 GW7-interim shadow read (pid 194729) -> R5 31B reads -> H3 availability head on all
# players -> wait for Friday's GW7 final corpus (refresh log marker, until 14:00 PDT) -> H1 shadow read on it -> R4
# availability GRPO with the TRL 1.0 config fix. Flags: logs/SKIP_R5, logs/SKIP_H3, logs/SKIP_R4. One GPU job at a time.
cd /home/wescheng/projects/fpl/fpl; LOG=logs/gpu_queue_1015.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
SHADOW_PID=${SHADOW_PID:-194729}
gpu_idle(){ while pgrep -f "avail_policy_eval|train_gemma|reghead_predict|expectation_decode|decode_live" >/dev/null; do sleep 60; done; }
log "queue C armed (pid $$): R5 -> H3 -> GW7 final read -> R4, after the interim shadow read (pid $SHADOW_PID)"
while kill -0 "$SHADOW_PID" 2>/dev/null; do sleep 30; done
gpu_idle
n=$(wc -l < reports/h_series/h1_gw7interim_pred.jsonl 2>/dev/null || echo 0)
log "H1 shadow read gw7interim end: $n rows ($(tail -c 200 logs/h1_shadow_gw7interim.log | tr '\r' '\n' | tail -1))"
if [ -f logs/SKIP_R5 ]; then log "R5 skipped (flag)"; else
  log "R5 start"; /usr/bin/bash scripts/run_r5_31b_reader.sh; log "R5 end: $(grep -a RESULT logs/r5_chain.log | tail -1)"; gpu_idle; fi
if [ -f logs/SKIP_H3 ]; then log "H3 skipped (flag)"; else
  log "H3 start"; /usr/bin/bash scripts/run_h3_avail_chain.sh; log "H3 end: $(grep -a RESULT logs/h3_chain.log | tail -1)"; gpu_idle; fi
CORPUS=reports/live_gw7final_2627_f6_examples.jsonl; DEADLINE=$(date -d '2026-10-16 14:00' +%s)
log "waiting for the GW7 final refresh (marker in logs/gw7_final_refresh.log) until $(date -d @$DEADLINE '+%F %T')"
until { grep -q "GW7 FINAL REFRESH DONE\|f6 examples FAILED\|past the GW7 deadline" logs/gw7_final_refresh.log 2>/dev/null && [ -s "$CORPUS" ]; } \
      || [ "$(date +%s)" -ge "$DEADLINE" ]; do sleep 120; done
if [ -s "$CORPUS" ] && [ ! -s reports/h_series/h1_gw7final_pred.jsonl ]; then
  log "H1 shadow read gw7final start ($(wc -l < "$CORPUS") rows)"
  ( source /home/wescheng/venvs/fpl-gemma-lite/bin/activate; export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
    python3 -u scripts/reghead_predict.py "$CORPUS" artifacts/gemma4_e4b_h1_reghead_e22 reports/h_series/h1_gw7final_pred.jsonl 8 ) >> logs/h1_shadow_gw7final.log 2>&1 \
    && log "H1 shadow read gw7final end: $(wc -l < reports/h_series/h1_gw7final_pred.jsonl) rows" || log "H1 shadow read gw7final FAILED"
  gpu_idle
else log "GW7 final corpus not available by the deadline (or already read); skipping the final shadow read"; fi
if [ -f logs/SKIP_R4 ]; then log "R4 skipped (flag)"; else
  log "R4 start (TRL 1.0 fix, 4 gens x accum 3)"; /usr/bin/bash scripts/run_r4_avail_chain.sh; log "R4 end: $(grep -a RESULT logs/r4_chain.log | tail -1)"; fi
log "GPU QUEUE C COMPLETE"

#!/usr/bin/env bash
# GPU queue D (2026-10-16 01:15 PDT): replaces queue C. R5's Gemma-4-31B 4-bit reads ran at 41 s/row (batch 4), not the
# planned ~5 s, i.e. ~14 h for its 1,443 rows, so it was stopped at 284/480 live rows (resumable: avail_policy_eval.py
# --resume appends) and moved last. Order: H3 availability head -> wait for Friday's GW7 final refresh marker (until
# 14:00 PDT) -> H1 shadow read on the final corpus -> R4 availability GRPO (TRL 1.0 fix) -> R5 resume.
# Flags: logs/SKIP_H3, logs/SKIP_R4, logs/SKIP_R5. One GPU job at a time; the only queue poller (queue C was killed 01:13).
cd /home/wescheng/projects/fpl/fpl; LOG=logs/gpu_queue_1015.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
gpu_idle(){ while pgrep -f "avail_policy_eval|train_gemma|reghead_predict|expectation_decode|decode_live" >/dev/null; do sleep 60; done; }
log "queue D armed (pid $$): H3 -> GW7 final read -> R4 -> R5 resume (R5 paused at $(wc -l < reports/r4_avail/r5_31b_live.jsonl)/480 live rows at 41 s/row)"
gpu_idle
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
  log "R4 start (TRL 1.0 fix, 4 gens x accum 3)"; /usr/bin/bash scripts/run_r4_avail_chain.sh; log "R4 end: $(grep -a RESULT logs/r4_chain.log | tail -1)"; gpu_idle; fi
if [ -f logs/SKIP_R5 ]; then log "R5 skipped (flag)"; else
  log "R5 resume"; /usr/bin/bash scripts/run_r5_31b_reader.sh; log "R5 end: $(grep -a RESULT logs/r5_chain.log | tail -1)"; fi
log "GPU QUEUE D COMPLETE"

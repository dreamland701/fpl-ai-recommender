#!/usr/bin/env bash
# GPU queue 2026-10-15 (Wes: 5-6 runs without asking): after H1 -> R4 availability GRPO -> R5 31B reader -> H2 (head on the E21 corpus).
cd /home/wescheng/projects/fpl/fpl; LOG=logs/gpu_queue_1015.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
log "queue armed; waiting for H1"
until grep -q "H1 CHAIN DONE\|H1 FAILED" logs/h1_chain.log 2>/dev/null; do sleep 120; done
while pgrep -f "train_gemma_reghead|reghead_predict" >/dev/null; do sleep 60; done
log "R4 start"; /usr/bin/bash scripts/run_r4_avail_chain.sh; log "R4 end: $(grep -a RESULT logs/r4_chain.log | tail -1)"
log "R5 start"; /usr/bin/bash scripts/run_r5_31b_reader.sh; log "R5 end: $(grep -a RESULT logs/r5_chain.log | tail -1)"
log "H2 start"; TAG=h2 SPLIT=reports/llm_residual_v2_e21_clean_top96_thru_2526_26_eval_2526_27_38 LSPLIT=reports/llm_residual_v2_e21_clean_top96_eval_2627_2_5 \
  LIVE_END=5 BATCH=1 CKPT=1 DATA_LABEL="E21 corpus: no official news, old baseline" /usr/bin/bash scripts/run_hx_chain.sh; log "H2 end: $(grep -a RESULT logs/h2_chain.log | tail -1)"
log "QUEUE DONE"

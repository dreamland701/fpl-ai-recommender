#!/usr/bin/env bash
# GPU queue tail 2026-10-15 20:30 PDT: replaces run_gpu_queue_1015.sh from R4 onwards. That script's bash (pid 176477) was
# stopped so the H1 GW7 shadow read could be slotted between R4 and R5; the R4 chain it had started (pid 189691) was left
# running. Order: R4 (running) -> H1 shadow read on the GW7 interim corpus -> R5 31B reader -> H2 (head on the E21 corpus)
# -> H1 shadow read on the GW7 final corpus if Friday's refresh has built it. One GPU job at a time throughout.
cd /home/wescheng/projects/fpl/fpl; LOG=logs/gpu_queue_1015.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
R4PID=${R4PID:-189691}
log "queue tail armed (pid $$): waiting for the R4 chain (pid $R4PID)"
while kill -0 "$R4PID" 2>/dev/null; do sleep 60; done
while pgrep -f "avail_policy_eval|train_gemma_grpo_avail" >/dev/null; do sleep 60; done
log "R4 end: $(grep -a RESULT logs/r4_chain.log | tail -1)"
shadow(){ # tag examples
  local tag=$1 ex=$2; [ -s "$ex" ] || { log "H1 shadow read $tag: no corpus at $ex"; return 0; }
  log "H1 shadow read $tag start"
  ( source /home/wescheng/venvs/fpl-gemma-lite/bin/activate; export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
    python3 -u scripts/reghead_predict.py "$ex" artifacts/gemma4_e4b_h1_reghead_e22 "reports/h_series/h1_${tag}_pred.jsonl" 8 ) >> "logs/h1_shadow_${tag}.log" 2>&1 \
    && log "H1 shadow read $tag end: $(tail -1 "logs/h1_shadow_${tag}.log")" || log "H1 shadow read $tag FAILED"
}
shadow gw7interim reports/live_gw7interim_2627_f6_examples.jsonl
log "R5 start"; /usr/bin/bash scripts/run_r5_31b_reader.sh; log "R5 end: $(grep -a RESULT logs/r5_chain.log | tail -1)"
if [ "${SKIP_H2:-0}" = "1" ] || [ -f logs/SKIP_H2 ]; then log "H2 skipped (flag)"; else
log "H2 start"; TAG=h2 SPLIT=reports/llm_residual_v2_e21_clean_top96_thru_2526_26_eval_2526_27_38 LSPLIT=reports/llm_residual_v2_e21_clean_top96_eval_2627_2_5 \
  LIVE_END=5 BATCH=1 CKPT=1 DATA_LABEL="E21 corpus: no official news, old baseline" /usr/bin/bash scripts/run_hx_chain.sh; log "H2 end: $(grep -a RESULT logs/h2_chain.log | tail -1)"
fi
shadow gw7final reports/live_gw7final_2627_f6_examples.jsonl
log "QUEUE DONE"

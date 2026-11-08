#!/usr/bin/env bash
set -uo pipefail
# GPU queue after the 2026-10-11 OOM (a 31B in bf16 next to E21 training exhausted RAM; systemd then
# stopped the whole session scope, E21 included). Strictly one GPU job at a time, run as its own
# memory-capped systemd user unit (systemd-run --user -p MemoryMax=...), so a runaway job is the
# only thing killed.
#   1. 31B expert reader (Wes: can articles carry a hidden pattern beyond classic and the market?)
#   2. 31B zero-shot chip advisor (Wes: would a bigger policy help?)
#   3. E21 training from scratch (it was at step 94/840, before its first checkpoint)
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/gpu_queue_1011.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
OUT=reports/review_fixes_2026_10/expert_reader; mkdir -p "$OUT"
log "=== 1. 31B expert reader ==="
python3 reports/review_fixes_2026_10/expert_reader.py rate "$OUT/ratings_31b.jsonl" >> logs/expert_reader.log 2>&1 \
  && python3 reports/review_fixes_2026_10/expert_reader.py score "$OUT/ratings_31b.jsonl" "$OUT/result_31b.md" >> logs/expert_reader.log 2>&1 \
  && log "expert reader done: $OUT/result_31b.md" || log "expert reader FAILED"
log "=== 2. 31B zero-shot chip advisor ==="
FPL_GEN_4BIT=1 FPL_GEN_DEVICE_MAP=gpu FPL_PLANNER_DISCIPLINE=1 FPL_PLANNER_MIN_GAIN=1.0 python3 scripts/run_chip_advisor_eval.py \
  --model-path /home/wescheng/models/gemma-4-31b-it --halves 2025-26:2,2023-24:2,2024-25:2 \
  --output reports/grpo_states_v2/eval_g7b_zeroshot_31b.json >> logs/g7b_zeroshot_31b.log 2>&1 \
  && log "31B chip advisor done: $(grep -a 'TOTAL' logs/g7b_zeroshot_31b.log | tail -1)" || log "31B chip advisor FAILED"
log "=== 3. E21 ==="
bash scripts/run_e21_clean_focused.sh
log "GPU QUEUE DONE"

#!/usr/bin/env bash
# R5 (2026-10-15): Gemma-4-31B-it (4-bit) zero-shot availability reads on the same rows as R4 (ceiling for text reading).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/r5_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
SPLIT=reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38; LSPLIT=reports/llm_residual_v2_e22_top96_eval_2627_2_6
OUT=reports/r4_avail; M=/home/wescheng/models/gemma-4-31b-it
log "=== R5: 31B reads ==="
python3 -u scripts/avail_policy_eval.py "$LSPLIT/eval.jsonl" "$OUT/r5_31b_live.jsonl" --subset all --batch 4 --model "$M" --4bit --resume >> "$LOG" 2>&1 || log "31B live FAILED"
python3 -u scripts/avail_policy_eval.py "$SPLIT/eval.jsonl" "$OUT/r5_31b_holdout.jsonl" --subset matter --batch 4 --model "$M" --4bit --resume >> "$LOG" 2>&1 || log "31B holdout FAILED"
log "RESULT: $(grep -a "AVAIL-POLICY" "$LOG" | sed 's/^.*AVAIL-POLICY/AVAIL-POLICY/' | tr '\n' ' ')"
log "R5 DONE"

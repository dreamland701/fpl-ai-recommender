#!/usr/bin/env bash
# R4 (2026-10-15): zero-shot availability read (base E4B) -> GRPO with the Brier-improvement reward -> trained read.
# 22:00 fix: TRL 1.0 dropped max_prompt_length (first run died at the config); 4 generations x accum 3 (12 completions per
# step, planned peak < 40 GB with checkpointing); the zero-shot reads from the first run are kept.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/r4_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "R4 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
SPLIT=reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38; LSPLIT=reports/llm_residual_v2_e22_top96_eval_2627_2_6
OUT=reports/r4_avail; mkdir -p "$OUT"; ADAPTER=artifacts/gemma4_e4b_r4_avail_grpo
log "=== R4: zero-shot base reads ==="
[ -s "$OUT/zeroshot_holdout.jsonl" ] || python3 -u scripts/avail_policy_eval.py "$SPLIT/eval.jsonl" "$OUT/zeroshot_holdout.jsonl" --subset matter --batch 8 >> "$LOG" 2>&1 || log "zero-shot holdout FAILED"
[ -s "$OUT/zeroshot_live.jsonl" ] || python3 -u scripts/avail_policy_eval.py "$LSPLIT/eval.jsonl" "$OUT/zeroshot_live.jsonl" --subset all --batch 8 >> "$LOG" 2>&1 || log "zero-shot live FAILED"
log "=== R4: GRPO training ==="
FPL_R4_SPLIT=$SPLIT FPL_R4_OUTPUT=$ADAPTER FPL_R4_MAX_PROMPTS=1200 FPL_R4_NUM_GEN=4 FPL_R4_GRAD_ACCUM=3 FPL_R4_TRACE=logs/r4_reward_trace.jsonl \
  python3 -u train_gemma_grpo_avail.py >> logs/train_r4.log 2>&1
[ -s "$ADAPTER/adapter_model.safetensors" ] || die "training"
log "=== R4: trained reads ==="
python3 -u scripts/avail_policy_eval.py "$SPLIT/eval.jsonl" "$OUT/r4_holdout.jsonl" --subset matter --batch 8 --adapter "$ADAPTER" >> "$LOG" 2>&1 || die "trained holdout"
python3 -u scripts/avail_policy_eval.py "$LSPLIT/eval.jsonl" "$OUT/r4_live.jsonl" --subset all --batch 8 --adapter "$ADAPTER" >> "$LOG" 2>&1 || die "trained live"
log "RESULT: $(grep -a "AVAIL-POLICY" "$LOG" | sed 's/^.*AVAIL-POLICY/AVAIL-POLICY/' | tr '\n' ' ')"
log "R4 CHAIN DONE"

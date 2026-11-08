#!/usr/bin/env bash
set -uo pipefail
# Fires the 16-doc extraction pilot the moment E11's post-train chain
# frees the GPU (never alongside training — the trainer's oom_score_adj
# makes IT the kernel's first kill target if a second model load OOMs).
ROOT="/home/wescheng/projects/fpl/fpl"
LOG="$ROOT/logs/evidence_pilot_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
log "armed; waiting for E11 chain CHAIN COMPLETE"
until grep -q "CHAIN COMPLETE" "$ROOT/logs/e11_post_train_chain.log" 2>/dev/null; do sleep 600; done
log "E11 chain done — running extraction pilot (base Gemma, 16 prompts)"
python -u eval_gemma_responses.py \
  --model-path google/gemma-4-E4B-it \
  --examples reports/evidence_extraction_pilot_prompts.jsonl \
  --output reports/evidence_extraction_pilot_predictions.jsonl \
  --max-new-tokens 120 --no-4bit --batch-size 4 >> "$LOG.gen" 2>&1 \
  && log "generation done" || { log "GENERATION FAILED (see $LOG.gen)"; exit 1; }
python -u eval_gemma_responses.py \
  --model-path google/gemma-4-E4B-it \
  --examples reports/article_digest_pilot_prompts.jsonl \
  --output reports/article_digest_pilot_predictions_gemma.jsonl \
  --max-new-tokens 700 --no-4bit --batch-size 2 >> "$LOG.gen" 2>&1 \
  && log "digest generation done (3 articles)" || log "DIGEST GENERATION FAILED (non-blocking)"
python3 scripts/report_evidence_extraction_pilot.py >> "$LOG" 2>&1
log "PILOT COMPLETE — report at reports/evidence_extraction_pilot_report.json"

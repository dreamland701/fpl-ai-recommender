#!/usr/bin/env bash
set -euo pipefail

# E8-podcast: identical recipe to E7-scout (E6 schema + scout evidence,
# --prefer-scout, 2 docs x 260 chars) except corpus v8 adds Whisper
# large-v3 transcripts of the Sky Sports Fantasy Podcast (2024-08 to
# present) as an additional evidence source alongside PL Scout + Sky
# written tips. Labels byte-identical to E4-E7 -> isolates the added
# podcast-evidence signal, same as every other rung comparison.
# Same token budget as E7 (max-evidence-docs/chars unchanged) -> same
# seq 1536 + grad checkpointing settings carry over unmodified.

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_e8_top256_podcast_evidence_thru_gw11_eval_gw12_30"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e8_top256_podcast_evidence"
LOG="$ROOT/logs/train_e4b_residual_e8_top256_podcast_evidence.log"

cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_MODEL_PATH="google/gemma-4-E4B-it"
export FPL_GEMMA_LOAD_IN_4BIT=false
export FPL_GEMMA_DATA_DIR="$DATA_DIR"
export FPL_GEMMA_OUTPUT_DIR="$OUTPUT_DIR"
export FPL_GEMMA_MAX_SEQ_LENGTH=1536
export FPL_GEMMA_TRUNCATION_MODE=keep_start
export FPL_GEMMA_MAX_STEPS=-1
export FPL_GEMMA_NUM_EPOCHS=1
export FPL_GEMMA_LEARNING_RATE=5e-5
export FPL_GEMMA_TRAIN_BATCH_SIZE=1
export FPL_GEMMA_EVAL_BATCH_SIZE=2
export FPL_GEMMA_GRAD_ACCUM=16
export FPL_GEMMA_LOGGING_STEPS=10
export FPL_GEMMA_EVAL_STRATEGY=no
export FPL_GEMMA_SAVE_STEPS=100
export FPL_GEMMA_SAVE_TOTAL_LIMIT=3
export FPL_GEMMA_WARMUP_STEPS=30
export FPL_GEMMA_GRADIENT_CHECKPOINTING=true
export FPL_GEMMA_LORA_DROPOUT=0.0

mkdir -p "$ROOT/logs"
python train_gemma_sft.py 2>&1 | tee "$LOG"

#!/usr/bin/env bash
set -euo pipefail

# E11-defcon: rate-normalized labels + DefCon-visible prompts. Byte-identical
# hyperparameters to E7/E9 (same corpus schema, same evidence recipe) —
# only the split changes: trained through 2025-26 GW34 inclusive (not
# held out this time), small 4-week holdout GW35-38 for a sanity check.

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_e11full_top256_thru_2526_38"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e11_full"
LOG="$ROOT/logs/train_e4b_residual_e11_full.log"

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
echo 800 > /proc/self/oom_score_adj 2>/dev/null || true
python train_gemma_sft.py 2>&1 | tee "$LOG"

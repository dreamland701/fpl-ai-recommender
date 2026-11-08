#!/usr/bin/env bash
set -euo pipefail

# E14-wide: identical recipe to E11 except ONE variable — evidence budget
# 3 docs x 700 chars (was 2 x 260), seq budget 2048 (was 1536). Wes's
# 'more context of quality text' question, single-variable vs E11 (train
# thru 2025-26:34, eval 35-38).

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_e14_wide_top256_thru_2526_34_eval_2526_35_38"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e14_wide"
LOG="$ROOT/logs/train_e4b_residual_e14_wide.log"

cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_MODEL_PATH="google/gemma-4-E4B-it"
export FPL_GEMMA_LOAD_IN_4BIT=false
export FPL_GEMMA_DATA_DIR="$DATA_DIR"
export FPL_GEMMA_OUTPUT_DIR="$OUTPUT_DIR"
export FPL_GEMMA_MAX_SEQ_LENGTH=2048
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

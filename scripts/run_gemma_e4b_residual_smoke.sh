#!/usr/bin/env bash
set -euo pipefail

# Smoke train for google/gemma-4-E4B-it on the existing GW1-25 residual dataset.
# Goal: establish real step-time on the DGX Spark and confirm the trainer works
# with the E4B architecture before building the multi-season dataset.

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_dev_thru_gw11_eval_gw12_30"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_smoke"
LOG="$ROOT/logs/train_e4b_residual_smoke.log"

cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_MODEL_PATH="google/gemma-4-E4B-it"
# bf16 LoRA without 4-bit quantization: the 8B raw model fits comfortably in
# unified memory and full-precision compute is faster than bnb dequant.
export FPL_GEMMA_LOAD_IN_4BIT=false
export FPL_GEMMA_DATA_DIR="$DATA_DIR"
export FPL_GEMMA_OUTPUT_DIR="$OUTPUT_DIR"
# v2 rows measure max 899 tokens (prompt+completion) for evidence-bearing
# rows, 683 for evidence-free ones; 1024 trains with zero truncation and
# half the padding of the old 2048 setting.
export FPL_GEMMA_MAX_SEQ_LENGTH=1024
export FPL_GEMMA_TRUNCATION_MODE=keep_start
export FPL_GEMMA_MAX_STEPS="${FPL_GEMMA_MAX_STEPS:-100}"
export FPL_GEMMA_NUM_EPOCHS=1
export FPL_GEMMA_LEARNING_RATE=5e-5
export FPL_GEMMA_TRAIN_BATCH_SIZE="${FPL_GEMMA_TRAIN_BATCH_SIZE:-8}"
export FPL_GEMMA_EVAL_BATCH_SIZE=8
export FPL_GEMMA_GRAD_ACCUM="${FPL_GEMMA_GRAD_ACCUM:-2}"
export FPL_GEMMA_LOGGING_STEPS=1
export FPL_GEMMA_EVAL_STRATEGY=no
export FPL_GEMMA_SAVE_STEPS=50
export FPL_GEMMA_SAVE_TOTAL_LIMIT=3
export FPL_GEMMA_WARMUP_STEPS=10
export FPL_GEMMA_GRADIENT_CHECKPOINTING=false
# peft's ParamWrapper (target_parameters path) rejects lora_dropout != 0 on
# this architecture; regularization comes from the small LoRA rank instead.
export FPL_GEMMA_LORA_DROPOUT=0.0

mkdir -p "$ROOT/logs"
python train_gemma_sft.py 2>&1 | tee "$LOG"

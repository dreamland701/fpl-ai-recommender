#!/usr/bin/env bash
set -euo pipefail

# E7-chrono-2425: identical recipe to E7-scout but trained only through
# 2023-24 GW11 (12,544 rows), eval 2023-24 GW12-38. Purpose: out-of-window
# validation of the E7 gate win (needed for leak-free E7-adjusted G2 states on 2023-24; also a
# third gate window.)
# Same memory profile as E7: seq 1536, batch 1 x accum 16, grad ckpt.
# 1,392 steps at ~92s/step ~= 36h.

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_e7chrono2324_top256_scout_thru_2324gw11_eval_2324gw12_38"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e7chrono2324_top256_scout"
LOG="$ROOT/logs/train_e4b_residual_e7chrono2324_top256_scout.log"

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
# peft's ParamWrapper (target_parameters path) rejects lora_dropout != 0 on
# this architecture; regularization comes from the small LoRA rank instead.
export FPL_GEMMA_LORA_DROPOUT=0.0

mkdir -p "$ROOT/logs"
python train_gemma_sft.py 2>&1 | tee "$LOG"

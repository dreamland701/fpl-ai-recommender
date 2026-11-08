#!/usr/bin/env bash
set -euo pipefail

# E3a: E2 recipe with richer evidence packets (2 docs x 450 chars vs 260).
# Identical to E1 (same rows, same labels, same hyperparameters) except the
# prompts carry player-mention evidence, so E2-vs-E1 isolates the text signal.
# Batch 2 x grad-accum 8: batch 8 OOM-kills the GB10 (see E1 runner).

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_e3a_rich_packets_thru_gw11_eval_gw12_30"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e3a_rich_packets"
LOG="$ROOT/logs/train_e4b_residual_e3a_rich_packets.log"

cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_MODEL_PATH="google/gemma-4-E4B-it"
export FPL_GEMMA_LOAD_IN_4BIT=false
export FPL_GEMMA_DATA_DIR="$DATA_DIR"
export FPL_GEMMA_OUTPUT_DIR="$OUTPUT_DIR"
export FPL_GEMMA_MAX_SEQ_LENGTH=1024
export FPL_GEMMA_TRUNCATION_MODE=keep_start
export FPL_GEMMA_MAX_STEPS=-1
export FPL_GEMMA_NUM_EPOCHS=1
export FPL_GEMMA_LEARNING_RATE=5e-5
export FPL_GEMMA_TRAIN_BATCH_SIZE=1
export FPL_GEMMA_EVAL_BATCH_SIZE=1
export FPL_GEMMA_GRAD_ACCUM=16
export FPL_GEMMA_LOGGING_STEPS=10
export FPL_GEMMA_EVAL_STRATEGY=no
export FPL_GEMMA_SAVE_STEPS=200
export FPL_GEMMA_SAVE_TOTAL_LIMIT=3
export FPL_GEMMA_WARMUP_STEPS=30
# Rich packets at seq 1024 OOM without checkpointing (0GB free at step 50);
# ~30-40% slower steps but activations shrink severalfold.
export FPL_GEMMA_GRADIENT_CHECKPOINTING=true
# peft's ParamWrapper (target_parameters path) rejects lora_dropout != 0 on
# this architecture; regularization comes from the small LoRA rank instead.
export FPL_GEMMA_LORA_DROPOUT=0.0

mkdir -p "$ROOT/logs"
python train_gemma_sft.py 2>&1 | tee "$LOG"

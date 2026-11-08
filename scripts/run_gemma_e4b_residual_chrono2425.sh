#!/usr/bin/env bash
set -euo pipefail

# Chronological retrain for multi-window LLM validation: train only on data
# available before 2024-25 GW12 (2022-24 + 2024-25 GW1-11, 22,272 rows),
# eval 2024-25 GW12-30. E4 prompt format (fixtures, no congestion). ~15h.
# post-break flags). Labels byte-identical to E4 -> isolates the congestion
# signal. Max prompt 772 tokens (E4: 753).
# Article packets dropped: E1~E2~E3a showed they do not move metrics.
# Isolates whether text evidence contributes anything when E2 adds it back.
# Dataset: multi-season 2022-23..2025-26:11 train, 2025-26 GW12-30 eval.
# Batch 2 x grad-accum 8: batch 8 OOM-kills the GB10's 119GB unified memory
# (measured 2026-07-05); this config peaks with ~26GB free at ~41s/step.

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_chrono2425_top256_fixtures_thru_gw11_eval_gw12_30"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_chrono2425_top256_fixtures"
LOG="$ROOT/logs/train_e4b_residual_chrono2425_top256_fixtures.log"

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
export FPL_GEMMA_TRAIN_BATCH_SIZE=2
export FPL_GEMMA_EVAL_BATCH_SIZE=2
export FPL_GEMMA_GRAD_ACCUM=8
export FPL_GEMMA_LOGGING_STEPS=10
export FPL_GEMMA_EVAL_STRATEGY=no
export FPL_GEMMA_SAVE_STEPS=100
export FPL_GEMMA_SAVE_TOTAL_LIMIT=3
export FPL_GEMMA_WARMUP_STEPS=30
export FPL_GEMMA_GRADIENT_CHECKPOINTING=false
# peft's ParamWrapper (target_parameters path) rejects lora_dropout != 0 on
# this architecture; regularization comes from the small LoRA rank instead.
export FPL_GEMMA_LORA_DROPOUT=0.0

mkdir -p "$ROOT/logs"
python train_gemma_sft.py 2>&1 | tee "$LOG"

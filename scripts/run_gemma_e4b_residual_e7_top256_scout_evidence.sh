#!/usr/bin/env bash
set -euo pipefail

# E7-scout: E6 full base-anatomy schema + expert scout evidence (corpus v7,
# PL Scout + Sky weekly tips; --prefer-scout, 2 docs x 260 chars). 84% of
# train rows carry evidence (vs 24% for old article packets). Labels
# byte-identical to E4/E5/E6 -> isolates the scout-evidence signal.
# Max prompt+completion 1,502 tokens -> seq 1536 (5.5% of rows exceed 1280
# and keep_start truncation would cut the JSON completion). New memory
# territory: batch 1 x accum 16 + gradient checkpointing from the start
# (E3a precedent at >1024 tokens; "fits at launch != survives").

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_e7_top256_scout_evidence_thru_gw11_eval_gw12_30"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e7_top256_scout_evidence"
LOG="$ROOT/logs/train_e4b_residual_e7_top256_scout_evidence.log"

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

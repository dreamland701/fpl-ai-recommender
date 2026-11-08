#!/usr/bin/env bash
set -euo pipefail

# E9-cleansplit: byte-identical recipe to E7-scout (corpus v7: E6 schema +
# PL Scout + Sky tips evidence, --prefer-scout, 2 docs x 260 chars) except
# the train/eval split changes to match the real GW1 2026-27 deployment
# condition: train ONLY on complete prior seasons (2022-23/2023-24/2024-25,
# zero 2025-26 rows at all) and eval on ALL currently-available 2025-26
# weeks (GW2-30, not just GW12-30) — the widest genuinely clean held-out
# test we can build today. Wes's idea (2026-07-30): this is what he can
# actually deploy when 2026-27 starts in ~3 weeks, since there will be no
# same-season data to train on then either.
#
# Same seq/memory footprint as E7 (same corpus content, same schema) so
# reusing E7's exact hyperparameters: seq 1536, batch 1 x accum 16, grad
# checkpointing from the start, lr 5e-5, 1 epoch.

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_residual_v2_e9_cleansplit_top256_thru_2425_eval_2526_gw2_30"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e9_cleansplit"
LOG="$ROOT/logs/train_e4b_residual_e9_cleansplit.log"

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

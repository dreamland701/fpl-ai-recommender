#!/usr/bin/env bash
set -uo pipefail

# G3b: extend the G3 run by one epoch (2 -> 3, +118 steps) resuming from
# its latest checkpoint, WITH the completion cap raised 512 -> 640 — the
# 2-epoch leg saw ~65% of sampled completions truncated at 512 after the
# transfer_pick field grew the JSON schema, muting the training signal.
# Wes approved the extra day (2026-08-18). Comparing the g3b eval against
# the 2-epoch g3 eval gives a real more-training/full-completions
# attribution point rather than one bigger blob.

ROOT="/home/wescheng/projects/fpl/fpl"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

CKPT=$(ls -d "$ROOT"/artifacts/gemma4_e4b_grpo_plan_g3/checkpoint-* 2>/dev/null | sort -V | tail -1)
if [ -z "$CKPT" ]; then
  echo "FATAL: no G3 checkpoint found to resume from" >&2
  exit 1
fi
echo "resuming from: $CKPT"

export FPL_GRPO_STATES_DIR="reports/grpo_states_adjusted"
export FPL_GRPO_TRAIN_SEASONS="2023-24,2024-25,2025-26-early"
export FPL_GRPO_REQUIRE_DELTAS=1
export FPL_GRPO_MAX_PROMPT_LENGTH=2816
export FPL_GRPO_MAX_COMPLETION_LENGTH=640
export FPL_GRPO_AUGMENT_VARIANTS=3
export FPL_GRPO_NUM_EPOCHS=3
export FPL_GRPO_OUTPUT_DIR="artifacts/gemma4_e4b_grpo_plan_g3"
export FPL_GRPO_RESUME_FROM_CHECKPOINT="$CKPT"

echo 800 > /proc/self/oom_score_adj 2>/dev/null || true
python3 -u train_gemma_grpo_plan.py

#!/usr/bin/env bash
set -uo pipefail

# G2-v3: same recipe as G2-v2 (adjusted deployment-regime states, fresh
# LoRA, horizon 6 / stride 1, 59 episodes across 2023-24 + 2024-25 +
# 2025-26-early) except train_gemma_grpo_plan.py now assigns each episode
# a sampled chip-availability budget instead of always both chips fresh —
# fixes the season-level chip-budget bug (see
# fpl-g2-v3-chip-budget memory / docs/experiment_log entry). One-variable
# change from v2, so this is a clean ablation of the curriculum fix alone.

ROOT="/home/wescheng/projects/fpl/fpl"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

export FPL_GRPO_STATES_DIR="reports/grpo_states_adjusted"
export FPL_GRPO_TRAIN_SEASONS="2023-24,2024-25,2025-26-early"
export FPL_GRPO_REQUIRE_DELTAS=1
export FPL_GRPO_MAX_PROMPT_LENGTH=2688
export FPL_GRPO_OUTPUT_DIR="artifacts/gemma4_e4b_grpo_plan_v3"

echo 800 > /proc/self/oom_score_adj 2>/dev/null || true
python3 -u train_gemma_grpo_plan.py

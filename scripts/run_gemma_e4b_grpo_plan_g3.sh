#!/usr/bin/env bash
set -uo pipefail

# G3: first rung where the policy chooses squad COMPOSITION, not just
# gates it. Bundle vs G2-v3 (attribution tradeoff accepted, Wes approved
# 2026-08-16): (1) transfer_pick action — index into the recommender's
# top-3 legal candidate transfers per week (0 = old behavior); first-week
# proposals shown in the prompt; (2) squad-diversity augmentation — 3
# perturbed-start variants per base episode (59 -> 236 episodes);
# (3) v3's half-season chip-budget curriculum retained. 2 epochs = 472
# samples, compute-matched to v3's total but 4x the distinct states.
# Compare against v3's corrected baseline: classic +23, adjusted +20.

ROOT="/home/wescheng/projects/fpl/fpl"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

export FPL_GRPO_STATES_DIR="reports/grpo_states_adjusted"
export FPL_GRPO_TRAIN_SEASONS="2023-24,2024-25,2025-26-early"
export FPL_GRPO_REQUIRE_DELTAS=1
export FPL_GRPO_MAX_PROMPT_LENGTH=2816
export FPL_GRPO_AUGMENT_VARIANTS=3
export FPL_GRPO_NUM_EPOCHS=2
export FPL_GRPO_OUTPUT_DIR="artifacts/gemma4_e4b_grpo_plan_g3"

echo 800 > /proc/self/oom_score_adj 2>/dev/null || true
python3 -u train_gemma_grpo_plan.py

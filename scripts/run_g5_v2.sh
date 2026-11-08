#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# G5 training, take 3 (2026-10-09). Fixes since take 2, all found at step 0:
#   - chat-templated prompts (untemplated: 0/8 samples parsed; templated: 24/24)
#   - generation stops at <turn|> (TRL's default <eos> ran samples to the cap)
#   - an unparseable plan always scores worst in its group (flat -5 beat bad valid plans)
#   - merged-weight generation (unmerged target_parameters LoRA: ~1.4 s per call)
# 3 epochs = 180 steps. No pause for the GW6 final refresh: merged decoding makes
# it short, so the two share the GPU. The trainer runs as g5_grpo_train.py (a copy
# of train_gemma_grpo_plan_v2.py) because the E20 chain's GPU wait matches any
# "train_gemma" process and would hold the GW6 final packet behind this run. The
# trainer gets oom_score_adj 800, so if memory runs out it dies first.
# Then the closed-loop holdout eval for the trained policy and the untrained one.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/g5_chain.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
OUT=artifacts/gemma4_e4b_grpo_plan_g5
export FPL_GRPO_OUTPUT_DIR="$OUT" FPL_GRPO_NUM_EPOCHS=3
STATES=reports/grpo_states_v2/2025-26-holdout.jsonl

python3 train_gemma_grpo_plan_v2.py --dry-run >> "$LOG" 2>&1 || { log "GATE FAILED: dry run"; exit 1; }
cp train_gemma_grpo_plan_v2.py g5_grpo_train.py
rm -rf "$OUT"
log "dry run passed; G5 take 3 training starts (180 steps)"
python g5_grpo_train.py >> logs/train_g5.log 2>&1 &
TRAIN_PID=$!
echo 800 > "/proc/$TRAIN_PID/oom_score_adj" 2>/dev/null || true
wait "$TRAIN_PID"; rc=$?
log "G5 training exited rc=$rc"
[ -s "$OUT/adapter_model.safetensors" ] || { log "G5 TRAINING FAILED (no adapter)"; exit 1; }

log "=== closed-loop holdout eval (2025-26 GW27-38): trained policy, then the untrained base ==="
python3 scripts/run_grpo_plan_eval_v2.py --states "$STATES" --adapter-path "$OUT" \
  --output reports/grpo_states_v2/eval_holdout_g5.json >> "$LOG" 2>&1 || log "trained eval FAILED"
python3 scripts/run_grpo_plan_eval_v2.py --states "$STATES" --adapter-path none \
  --output reports/grpo_states_v2/eval_holdout_g5_base.json >> "$LOG" 2>&1 || log "base eval FAILED"
log "RESULT: $(python3 - <<'PYEOF'
import json, os
out = []
for tag, f in (("trained", "reports/grpo_states_v2/eval_holdout_g5.json"), ("untrained", "reports/grpo_states_v2/eval_holdout_g5_base.json")):
    if os.path.exists(f):
        d = json.load(open(f)); s = d["summary"]
        out.append(f"{tag} policy {s.get('policy')} (invalid weeks {len(d['invalid_weeks'])})")
        planner, classic = s["planner"], s["classic_no_chips"]
print(" | ".join(out) + f" | same-chips planner {planner} | classic no chips {classic}")
PYEOF
)"
log "G5 CHAIN DONE"

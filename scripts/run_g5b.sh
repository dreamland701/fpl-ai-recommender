#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# G5b (take 4, 2026-10-10): take 3 with learning rate 1e-5 -> 5e-5 and sampling temperature
# 0.8 -> 1.0, nothing else. Take 3 was flat: trained = untrained (749 = 749, identical
# decisions in all 12 holdout weeks), KL <= 0.0016, 26-33% of groups with zero reward spread.
# The untrained policy's eval (749) is not re-run.
# Take 3's fixes, all found at step 0:
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
OUT=artifacts/gemma4_e4b_grpo_plan_g5b
export FPL_GRPO_OUTPUT_DIR="$OUT" FPL_GRPO_NUM_EPOCHS=3 FPL_GRPO_LEARNING_RATE=5e-5 FPL_GRPO_TEMPERATURE=1.0
STATES=reports/grpo_states_v2/2025-26-holdout.jsonl

python3 train_gemma_grpo_plan_v2.py --dry-run >> "$LOG" 2>&1 || { log "GATE FAILED: dry run"; exit 1; }
cp train_gemma_grpo_plan_v2.py g5_grpo_train.py
rm -rf "$OUT"
log "dry run passed; G5b training starts (180 steps, lr 5e-5, temperature 1.0)"
python g5_grpo_train.py >> logs/train_g5b.log 2>&1 &
TRAIN_PID=$!
echo 800 > "/proc/$TRAIN_PID/oom_score_adj" 2>/dev/null || true
wait "$TRAIN_PID"; rc=$?
log "G5b training exited rc=$rc"
[ -s "$OUT/adapter_model.safetensors" ] || { log "G5b TRAINING FAILED (no adapter)"; exit 1; }

log "=== closed-loop holdout eval (2025-26 GW27-38): G5b ==="
python3 scripts/run_grpo_plan_eval_v2.py --states "$STATES" --adapter-path "$OUT" \
  --output reports/grpo_states_v2/eval_holdout_g5b.json >> "$LOG" 2>&1 || log "G5b eval FAILED"
log "RESULT: $(python3 - <<'PYEOF'
import json, os
out = []
for tag, f in (("G5b", "reports/grpo_states_v2/eval_holdout_g5b.json"), ("G5 take 3", "reports/grpo_states_v2/eval_holdout_g5.json"), ("untrained", "reports/grpo_states_v2/eval_holdout_g5_base.json")):
    if os.path.exists(f):
        d = json.load(open(f)); s = d["summary"]
        out.append(f"{tag} policy {s.get('policy')} (invalid weeks {len(d['invalid_weeks'])})")
        planner, classic = s["planner"], s["classic_no_chips"]
print(" | ".join(out) + f" | same-chips planner {planner} | classic no chips {classic}")
PYEOF
)"
log "G5B CHAIN DONE"

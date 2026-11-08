#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after G2-v2b (E7-merged-init ablation): the same two-way
# composed-stack eval as v2, with two differences:
#   - --base-adapter: the v2b policy is a delta on base+E7-merged weights
#   - --min-new-tokens 8: block the GRPO empty-EOS decode attractor
# Verdict = v2b deltas vs v2's (+47 classic / +27 adjusted, min8).

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_grpo_plan_v2b.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_grpo_plan_v2b"
E7="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e7_top256_scout_evidence"
CHAINLOG="$ROOT/logs/g2v2b_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for G2-v2b final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: G2-v2b trainer log static for 30 min and no train_runtime"
  fi
done
log "G2-v2b training complete — running composed-stack eval (min8, E7-stacked)"

run_eval() {
  # $1 = states file, $2 = output json, $3 = label
  python3 scripts/run_grpo_plan_eval.py \
    --adapter-path "$ADAPTER" \
    --base-adapter "$E7" \
    --min-new-tokens 8 \
    --states "$1" \
    --output "$2" >> "$CHAINLOG.eval" 2>&1 \
    && log "eval done: $3 -> $(python3 -c "
import json
s = json.load(open('$2'))
print(f\"policy {s['policy_total']:.0f} vs baseline {s['baseline_total']:.0f} ({s['delta_total']:+.0f}; {s['wins']}W/{s['losses']}L/{s['ties']}T; {s['unparseable']} unparseable)\")" 2>/dev/null)" \
    || log "EVAL FAILED: $3 (see $CHAINLOG.eval)"
}

run_eval reports/grpo_states/2025-26.jsonl          reports/grpo_plan_eval_2526_classic_v2b_min8.json  classic
run_eval reports/grpo_states_adjusted/2025-26.jsonl reports/grpo_plan_eval_2526_adjusted_v2b_min8.json adjusted

log "CHAIN COMPLETE — v2b ablation verdict ready for review"

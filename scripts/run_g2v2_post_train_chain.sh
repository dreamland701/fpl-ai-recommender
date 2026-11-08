#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after G2-v2 plan-GRPO: the two-way composed-stack eval on the
# untouched 2025-26 GW12-30 gate window (approved sequence step 8).
#   - classic states:  does the plan policy add value over all-defaults
#                      on raw classic forecasts?
#   - adjusted states: the full deployment stack (classic + E7 deltas +
#                      snippets + plan policy) — the configuration that
#                      would actually ship.
# Totals land in this chain log; verdict left for review (no further
# stage auto-launches — v2b ablation needs a code change first).

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_grpo_plan_v2.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_grpo_plan_v2"
CHAINLOG="$ROOT/logs/g2v2_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for G2-v2 final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: G2-v2 trainer log static for 30 min and no train_runtime"
  fi
done
log "G2-v2 training complete — running composed-stack eval"

run_eval() {
  # $1 = states file, $2 = output json, $3 = label
  python3 scripts/run_grpo_plan_eval.py \
    --adapter-path "$ADAPTER" \
    --states "$1" \
    --output "$2" >> "$CHAINLOG.eval" 2>&1 \
    && log "eval done: $3 -> $(python3 -c "
import json
s = json.load(open('$2'))
print(f\"policy {s['policy_total']:.0f} vs baseline {s['baseline_total']:.0f} ({s['delta_total']:+.0f}; {s['wins']}W/{s['losses']}L/{s['ties']}T; {s['unparseable']} unparseable)\")" 2>/dev/null)" \
    || log "EVAL FAILED: $3 (see $CHAINLOG.eval)"
}

run_eval reports/grpo_states/2025-26.jsonl          reports/grpo_plan_eval_2526_classic.json  classic
run_eval reports/grpo_states_adjusted/2025-26.jsonl reports/grpo_plan_eval_2526_adjusted.json adjusted

log "CHAIN COMPLETE — composed-stack verdict ready for review"

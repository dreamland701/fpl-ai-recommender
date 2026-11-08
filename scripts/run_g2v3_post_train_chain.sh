#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after G2-v3: composed-stack eval on the untouched 2025-26
# GW12-30 gate, same protocol as v2 (scripts/run_g2v2_post_train_chain.sh)
# but with --min-new-tokens 8 baked in from the start (the empty-EOS decode
# attractor is a known GRPO issue, no need to rediscover it) and using the
# season-level chip-budget-aware eval script (run_grpo_plan_eval.py, fixed
# 2026-07-30). Honest "before" baseline for comparison: the existing v2
# adapter re-evaluated under this same corrected script scored classic +23
# (3W/0L/0T), adjusted +20 (2W/0L/1T) — down from the buggy +47/+27 that
# let a chip replay once per window instead of once per season.

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_grpo_plan_v3.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_grpo_plan_v3"
CHAINLOG="$ROOT/logs/g2v3_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for G2-v3 final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: G2-v3 trainer log static for 30 min and no train_runtime"
  fi
done
log "G2-v3 training complete — running composed-stack eval (season-chip-aware, min8)"

echo 800 > /proc/self/oom_score_adj 2>/dev/null || true

run_eval() {
  # $1 = states file, $2 = output json, $3 = label
  python3 scripts/run_grpo_plan_eval.py \
    --adapter-path "$ADAPTER" \
    --states "$1" \
    --min-new-tokens 8 \
    --output "$2" >> "$CHAINLOG.eval" 2>&1 \
    && log "eval done: $3 -> $(python3 -c "
import json
s = json.load(open('$2'))
print(f\"policy {s['policy_total']:.0f} vs baseline {s['baseline_total']:.0f} ({s['delta_total']:+.0f}; {s['wins']}W/{s['losses']}L/{s['ties']}T; {s['unparseable']} unparseable)\")" 2>/dev/null)" \
    || log "EVAL FAILED: $3 (see $CHAINLOG.eval)"
}

run_eval reports/grpo_states/2025-26.jsonl          reports/grpo_plan_eval_2526_classic_v3_min8.json  classic
run_eval reports/grpo_states_adjusted/2025-26.jsonl reports/grpo_plan_eval_2526_adjusted_v3_min8.json adjusted

log "CHAIN COMPLETE — G2-v3 verdict ready for review (compare vs v2-corrected: classic +23, adjusted +20)"

#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after G3b (the +1-epoch, 640-completion-cap extension):
# same composed-stack eval as g3's chain, writing _g3b_ outputs so the
# 2-epoch vs 3-epoch comparison is preserved side by side. NOTE the
# adapter file already exists from the 2-epoch save, so completion is
# gated on train_runtime appearing in G3b's OWN log.

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_grpo_plan_g3b.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_grpo_plan_g3"
CHAINLOG="$ROOT/logs/g3b_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for G3b (resumed) train_runtime"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: G3b trainer log static for 30 min and no train_runtime"
  fi
done
log "G3b training complete — running composed-stack eval (season-chip-aware, min8)"

echo 800 > /proc/self/oom_score_adj 2>/dev/null || true

run_eval() {
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

run_eval reports/grpo_states/2025-26.jsonl          reports/grpo_plan_eval_2526_classic_g3b_min8.json  classic
run_eval reports/grpo_states_adjusted/2025-26.jsonl reports/grpo_plan_eval_2526_adjusted_g3b_min8.json adjusted

log "CHAIN COMPLETE — G3b verdict ready (compare: v3 corrected +23/+20, and g3 2-epoch eval jsons)"

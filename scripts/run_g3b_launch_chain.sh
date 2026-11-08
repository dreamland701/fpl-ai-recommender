#!/usr/bin/env bash
set -uo pipefail

# Bridges G3 -> G3b unattended: waits for G3's post-train chain to finish
# its evals (CHAIN COMPLETE in its log — the GPU is free at that point),
# then launches the G3b extension trainer + its chain, both detached.
# Verification is artifact-based (log growth), per chain conventions.

ROOT="/home/wescheng/projects/fpl/fpl"
G3CHAIN="$ROOT/logs/g3_post_train_chain.log"
LOG="$ROOT/logs/g3b_launch_chain.log"
cd "$ROOT"

log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
log "armed; waiting for G3 chain CHAIN COMPLETE"

until grep -q "CHAIN COMPLETE" "$G3CHAIN" 2>/dev/null; do
  sleep 300
done
log "G3 chain complete — launching G3b extension"

chmod +x "$ROOT/scripts/run_gemma_e4b_grpo_plan_g3b_extend.sh" "$ROOT/scripts/run_g3b_post_train_chain.sh"
setsid nohup "$ROOT/scripts/run_gemma_e4b_grpo_plan_g3b_extend.sh" > "$ROOT/logs/train_grpo_plan_g3b.log" 2>&1 < /dev/null &
setsid nohup "$ROOT/scripts/run_g3b_post_train_chain.sh" > "$ROOT/logs/g3b_post_train_chain_nohup.log" 2>&1 < /dev/null &

sleep 180
size=$(stat -c %s "$ROOT/logs/train_grpo_plan_g3b.log" 2>/dev/null || echo 0)
if [ "$size" -gt 200 ]; then
  log "G3b trainer log growing (${size}B after 3 min) — launch verified"
else
  log "G3b LAUNCH SUSPECT — log only ${size}B after 3 min, check logs/train_grpo_plan_g3b.log"
fi
log "DONE"

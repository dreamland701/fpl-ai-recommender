#!/usr/bin/env bash
set -uo pipefail

# Auto-launch E7-scout once the G1 chain (adapter save + decision eval)
# frees the GPU. Decision by Wes 2026-07-15: E7 next regardless of G1 eval
# outcome; G2 stays after E7. Triggers on CHAIN COMPLETE or CHAIN ABORTED
# in the G1 chain log — either way the GPU is idle.

ROOT="/home/wescheng/projects/fpl/fpl"
G1LOG="$ROOT/logs/g1_post_train_chain.log"
CHAINLOG="$ROOT/logs/e7_launch_chain.log"
cd "$ROOT"

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "E7 launch chain armed; waiting for G1 chain to finish"

until grep -qE "CHAIN COMPLETE|CHAIN ABORTED" "$G1LOG" 2>/dev/null; do
  sleep 300
done
log "G1 chain finished — launching E7-scout training"

nohup scripts/run_gemma_e4b_residual_e7_top256_scout_evidence.sh \
  > logs/e7_nohup.log 2>&1 &
sleep 60
TRAINER_PID=$(pgrep -f "python train_gemma_sft.py" | head -1)
if [ -n "$TRAINER_PID" ]; then
  echo 800 > /proc/$TRAINER_PID/oom_score_adj 2>/dev/null || true
  log "E7 trainer python pid $TRAINER_PID (oom_score_adj 800)"
else
  log "E7 LAUNCH FAILED — no trainer process found (see logs/e7_nohup.log)"
  exit 1
fi
log "CHAIN COMPLETE"

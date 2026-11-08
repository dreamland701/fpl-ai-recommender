#!/usr/bin/env bash
set -uo pipefail
# Launches the E11-full consolidation trainer once the evidence pilot
# frees the GPU, then arms a smoke check (no eval exists — quality was
# certified by E11's GW35-38 run; smoke = decode 48 train rows, verify
# strict-JSON rate + sane delta magnitudes).
ROOT="/home/wescheng/projects/fpl/fpl"
LOG="$ROOT/logs/e11full_launch_chain.log"
cd "$ROOT"
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
log "armed; waiting for PILOT COMPLETE"
until grep -q "PILOT COMPLETE\|GENERATION FAILED" "$ROOT/logs/evidence_pilot_chain.log" 2>/dev/null; do sleep 120; done
log "pilot done — launching E11-full trainer"
chmod +x scripts/run_gemma_e4b_residual_e11_full.sh
setsid nohup scripts/run_gemma_e4b_residual_e11_full.sh > logs/e11full_train_nohup.log 2>&1 < /dev/null &
sleep 240
if tr -d '\000' < logs/train_e4b_residual_e11_full.log 2>/dev/null | grep -qE "Traceback|Error"; then
  log "E11-FULL LAUNCH FAILED — traceback in first 4 min, check logs/train_e4b_residual_e11_full.log"
  exit 1
fi
size=$(stat -c %s logs/train_e4b_residual_e11_full.log 2>/dev/null || echo 0)
log "trainer log at ${size}B after 4 min — launch looks healthy"
TRAINER_PID=$(pgrep -f "python train_gemma_sft.py" | head -1)
[ -n "$TRAINER_PID" ] && echo 800 > /proc/$TRAINER_PID/oom_score_adj 2>/dev/null && log "trainer pid $TRAINER_PID oom 800"
log "DONE — smoke check runs manually/next session after train_runtime appears"

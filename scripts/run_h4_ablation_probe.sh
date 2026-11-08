#!/usr/bin/env bash
# H4 ablation probe (2026-10-25): re-predict the own-fact rows of the H4 holdout/live evals with the team sheet intact,
# without the player's own line, without the team line, without the Guardian line, and without the sheet, to see what
# the adapter actually reads (why Gakpo/Isak GW6 went up). CPU builds reports/h_series/h4_ablation/examples.jsonl first.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h4_ablation.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTORCH_ALLOC_CONF=expandable_segments:True
watchdog(){ local pid=$1 used; while kill -0 "$pid" 2>/dev/null; do used=$(free -g | awk '/Mem:/{print $3}'); if [ "${used:-0}" -gt 100 ]; then log "WATCHDOG: used ${used} GB > 100, killing $pid"; kill "$pid"; fi; sleep 10; done; }
log "=== H4 ablation probe: $(wc -l < reports/h_series/h4_ablation/examples.jsonl) rows ==="
python3 -u scripts/reghead_predict.py reports/h_series/h4_ablation/examples.jsonl artifacts/gemma4_e4b_h4_teamsheet reports/h_series/h4_ablation/pred.jsonl 8 >> "$LOG" 2>&1 &
P=$!; watchdog "$P"; wait "$P" || log "predict exited non-zero"
[ -s reports/h_series/h4_ablation/pred.jsonl ] && log "H4 ABLATION DONE" || log "H4 ABLATION FAILED"

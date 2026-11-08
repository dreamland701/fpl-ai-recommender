#!/usr/bin/env bash
# Queue the availability-fact backfill behind the v2 extractor pilot (one GPU job at a time, 2026-10-23 01:00):
# waits for the pid in logs/pids/extract_pilot_v2.pid to exit, then runs scripts/run_extract_backfill.sh with the
# pilot-chosen settings (Gemma-4-31B-it nf4, prompt v2, availability-class documents first, 5,000-char article cap,
# batch 12, caps 320 then 768). Abort before it starts: kill the pid in logs/pids/queue_extract_backfill.pid; abort
# after: touch logs/stop_extract (the extractor exits cleanly at the next batch and the chain logs PAUSED).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
LOG=logs/extract_backfill.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
PREV=$(cat logs/pids/extract_pilot_v2.pid 2>/dev/null || echo "")
if [ -n "$PREV" ]; then log "backfill queued behind pilot v2 (pid $PREV)"; while kill -0 "$PREV" 2>/dev/null; do sleep 30; done; fi
if [ -e logs/stop_extract ]; then log "stop file present before start; not launching the backfill"; exit 0; fi
export FPL_EXTRACT_MODEL=/home/wescheng/models/gemma-4-31b-it FPL_EXTRACT_4BIT=1 FPL_EXTRACT_BATCH=${FPL_EXTRACT_BATCH:-12}
export FPL_EXTRACT_LABEL=${FPL_EXTRACT_LABEL:-31b_v2} FPL_EXTRACT_PROMPT=${FPL_EXTRACT_PROMPT:-v2}
export FPL_EXTRACT_DOCS=${FPL_EXTRACT_DOCS:-reports/extract_facts/docs_avail.jsonl} FPL_EXTRACT_MAXCHARS=${FPL_EXTRACT_MAXCHARS:-5000}
export FPL_EXTRACT_CAP1=${FPL_EXTRACT_CAP1:-320} FPL_EXTRACT_CAP2=${FPL_EXTRACT_CAP2:-768}
exec /usr/bin/bash "$ROOT/scripts/run_extract_backfill.sh"

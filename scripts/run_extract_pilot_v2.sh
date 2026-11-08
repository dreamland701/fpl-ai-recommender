#!/usr/bin/env bash
# Extractor pilot, prompt v2 (2026-10-22 23:20): same 90 pilot documents, the stricter prompt (explicit "not facts":
# past matches, praise, contracts) through Gemma-4-E4B-it (bf16) then Gemma-4-31B-it (nf4). Queued behind the v1
# pilot (waits for the pid in logs/pids/extract_pilot.pid to exit) so there is one GPU job at a time; the 31B load
# runs under the 100 GB watchdog. Log logs/extract_pilot_v2.log, sentinel "EXTRACT PILOT V2 DONE" (printed once).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/extract_pilot_v2.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTORCH_ALLOC_CONF=expandable_segments:True
DOCS=reports/extract_facts/pilot_docs.jsonl; OUT=reports/extract_facts; M31=/home/wescheng/models/gemma-4-31b-it
B31=${FPL_EXTRACT_B31:-8}
watchdog(){ local pid=$1 used
  while kill -0 "$pid" 2>/dev/null; do
    used=$(free -g | awk '/Mem:/{print $3}')
    if [ "${used:-0}" -gt 100 ]; then log "WATCHDOG: used ${used} GB > 100, killing $pid"; kill "$pid"; fi
    sleep 5
  done; }
PREV=$(cat logs/pids/extract_pilot.pid 2>/dev/null || echo "")
if [ -n "$PREV" ]; then log "queued behind pilot v1 (pid $PREV)"; while kill -0 "$PREV" 2>/dev/null; do sleep 30; done; fi
log "=== pilot v2 E4B bf16 (batch 8) ==="
python3 -u scripts/extract_availability_facts.py --docs "$DOCS" --out "$OUT/pilot_pred_e4b_v2.jsonl" --model google/gemma-4-E4B-it \
  --label e4b_v2 --prompt-version v2 --batch 8 --max-new-tokens 768 --stop-file logs/stop_extract >> "$LOG" 2>&1 || log "E4B v2 FAILED"
log "=== pilot v2 31B nf4 (batch $B31) ==="
python3 -u scripts/extract_availability_facts.py --docs "$DOCS" --out "$OUT/pilot_pred_31b_v2.jsonl" --model "$M31" \
  --label 31b_v2 --prompt-version v2 --4bit --batch "$B31" --max-new-tokens 768 --stop-file logs/stop_extract >> "$LOG" 2>&1 &
P=$!; watchdog "$P"; wait "$P" || log "31B v2 FAILED"
log "rows: e4b_v2 $(wc -l < "$OUT/pilot_pred_e4b_v2.jsonl" 2>/dev/null) 31b_v2 $(wc -l < "$OUT/pilot_pred_31b_v2.jsonl" 2>/dev/null)"
log "EXTRACT PILOT V2 DONE"

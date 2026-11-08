#!/usr/bin/env bash
# Extractor pilot (2026-10-22, Wes: "load my Gemma 31B model (no SFT) to get the extraction ... compare using some
# 10-100 examples against Haiku"): the same 90 pilot documents (60 prose + 30 Guardian predicted-lineups fixture
# segments with parser truth, reports/extract_facts/pilot_docs.jsonl) through Gemma-4-E4B-it (bf16) and then
# Gemma-4-31B-it (bitsandbytes nf4), zero-shot, shared prompt (scripts/extract_availability_facts.py). Haiku runs
# the same prompts through subagents (reports/extract_facts/haiku/). Score: scripts/score_extract_pilot.py.
# One GPU job at a time; the 31B load transient (~75-80 GB system used) runs under a watchdog that kills it above
# 100 GB. Logs logs/extract_pilot.log, sentinel "EXTRACT PILOT DONE" (printed once, at the end).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/extract_pilot.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTORCH_ALLOC_CONF=expandable_segments:True
DOCS=reports/extract_facts/pilot_docs.jsonl; OUT=reports/extract_facts
M31=/home/wescheng/models/gemma-4-31b-it
B31=${FPL_EXTRACT_B31:-8}
watchdog(){ # kill $1 if system used memory exceeds 100 GB
  local pid=$1 used
  while kill -0 "$pid" 2>/dev/null; do
    used=$(free -g | awk '/Mem:/{print $3}')
    if [ "${used:-0}" -gt 100 ]; then log "WATCHDOG: used ${used} GB > 100, killing $pid"; kill "$pid"; fi
    sleep 5
  done; }
log "=== pilot E4B bf16 (batch 8) ==="
python3 -u scripts/extract_availability_facts.py --docs "$DOCS" --out "$OUT/pilot_pred_e4b.jsonl" --model google/gemma-4-E4B-it \
  --label e4b --batch 8 --max-new-tokens 768 --stop-file logs/stop_extract >> "$LOG" 2>&1 || log "E4B pilot FAILED"
log "=== pilot 31B nf4 (batch $B31) ==="
python3 -u scripts/extract_availability_facts.py --docs "$DOCS" --out "$OUT/pilot_pred_31b.jsonl" --model "$M31" \
  --label 31b --4bit --batch "$B31" --max-new-tokens 768 --stop-file logs/stop_extract >> "$LOG" 2>&1 &
P=$!; watchdog "$P"; wait "$P" || log "31B pilot FAILED"
log "rows: e4b $(wc -l < "$OUT/pilot_pred_e4b.jsonl" 2>/dev/null) 31b $(wc -l < "$OUT/pilot_pred_31b.jsonl" 2>/dev/null)"
log "EXTRACT PILOT DONE"

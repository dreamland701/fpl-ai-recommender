#!/usr/bin/env bash
# Availability-fact backfill (2026-10-22): the routed 2022-27 documents (reports/extract_facts/docs_all.jsonl, priority
# order) through a local Gemma zero-shot extractor (scripts/extract_availability_facts.py), then the facts become
# ridge features (scripts/build_extract_features.py) and go through the 21-window decision bench + xPts re-score.
# Env: FPL_EXTRACT_MODEL (default Gemma-4-31B-it, Wes: "load my Gemma 31B model (no SFT)"), FPL_EXTRACT_4BIT (1),
# FPL_EXTRACT_BATCH (8), FPL_EXTRACT_LABEL (31b). Resumable: re-launch after a stop (touch logs/stop_extract) or the
# GW8 Friday pause (window 2026-10-23 13:45-17:30 UTC while logs/gw8_gpu_ok exists); the bench runs only once every
# document has a row. Watchdog kills the extractor above 100 GB system used (31B load transient is 75-80 GB).
# Log logs/extract_backfill.log; sentinels "EXTRACT BACKFILL PAUSED" / "EXTRACT BACKFILL DONE" (each printed once).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/extract_backfill.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PLANNER_DISCIPLINE=1 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
MODEL=${FPL_EXTRACT_MODEL:-/home/wescheng/models/gemma-4-31b-it}; FOUR=${FPL_EXTRACT_4BIT:-1}; B=${FPL_EXTRACT_BATCH:-8}
LABEL=${FPL_EXTRACT_LABEL:-31b}; DOCS=${FPL_EXTRACT_DOCS:-reports/extract_facts/docs_all.jsonl}; OUT=reports/extract_facts/backfill_${LABEL}.jsonl
MAXCHARS=${FPL_EXTRACT_MAXCHARS:-9000}
FLAG=(); [ "$FOUR" = "1" ] && FLAG=(--4bit)
watchdog(){ local pid=$1 used
  while kill -0 "$pid" 2>/dev/null; do
    used=$(free -g | awk '/Mem:/{print $3}')
    if [ "${used:-0}" -gt 100 ]; then log "WATCHDOG: used ${used} GB > 100, killing $pid"; kill "$pid"; fi
    sleep 5
  done; }
CAP1=${FPL_EXTRACT_CAP1:-320}; CAP2=${FPL_EXTRACT_CAP2:-768}; PV=${FPL_EXTRACT_PROMPT:-v1}
log "=== backfill $LABEL ($MODEL, 4bit=$FOUR, batch $B, caps $CAP1 then $CAP2, prompt $PV) over $(wc -l < "$DOCS") docs; done so far $(wc -l < "$OUT" 2>/dev/null || echo 0) ==="
# Pass 1: short cap (a batch decodes until its longest output ends, so the cap bounds every batch); pass 2 re-does
# only the rows that hit the cap with the long cap, in their own batches.
python3 -u scripts/extract_availability_facts.py --docs "$DOCS" --out "$OUT" --model "$MODEL" "${FLAG[@]}" --label "$LABEL" --batch "$B" \
  --max-new-tokens "$CAP1" --max-chars "$MAXCHARS" --prompt-version "$PV" --stop-file logs/stop_extract \
  --pause-window 2026-10-23T13:45:00Z/2026-10-23T17:30:00Z --pause-flag logs/gw8_gpu_ok >> "$LOG" 2>&1 &
P=$!; watchdog "$P"; wait "$P" || log "extractor pass 1 exited non-zero"
NDOC=$(wc -l < "$DOCS"); NOUT=$(wc -l < "$OUT" 2>/dev/null || echo 0)
if [ "$NOUT" -lt "$NDOC" ]; then log "rows $NOUT / $NDOC; EXTRACT BACKFILL PAUSED (re-launch to resume)"; exit 0; fi
log "=== pass 2: truncated rows at cap $CAP2 ==="
python3 -u scripts/extract_availability_facts.py --docs "$DOCS" --out "$OUT" --model "$MODEL" "${FLAG[@]}" --label "$LABEL" --batch "$B" \
  --max-new-tokens "$CAP2" --max-chars "$MAXCHARS" --prompt-version "$PV" --redo-truncated --stop-file logs/stop_extract \
  --pause-window 2026-10-23T13:45:00Z/2026-10-23T17:30:00Z --pause-flag logs/gw8_gpu_ok >> "$LOG" 2>&1 &
P=$!; watchdog "$P"; wait "$P" || log "extractor pass 2 exited non-zero"
NOUT=$(wc -l < "$OUT" 2>/dev/null || echo 0)
if [ "$NOUT" -lt "$NDOC" ]; then log "rows $NOUT / $NDOC after pass 2; EXTRACT BACKFILL PAUSED (re-launch to resume)"; exit 0; fi
log "=== features ($NOUT rows) ==="
python3 scripts/build_extract_features.py --docs "$DOCS" --facts "$OUT" --table data/fpl_training_rows_v3_contract_f6_teamnews.csv \
  --out data/fpl_training_rows_v3_contract_f6_extract.csv --feat-json reports/extract_facts/facts_by_player_week_${LABEL}.json >> "$LOG" 2>&1 || log "features FAILED"
log "=== 21-window bench EX0_F / EX1_F / EX2_F ==="
CONFIGS="EX0_F EX1_F EX2_F" JOBS=6 TABLE=data/fpl_training_rows_v3_contract_f6_extract.csv OUT=reports/extract_facts/bt \
  /usr/bin/bash scripts/run_market_backtests.sh >> "$LOG" 2>&1 || log "bench FAILED"
python3 scripts/bt_compare.py --base-dir reports/extract_facts/bt --base EX0_F --var-dir reports/extract_facts/bt --configs EX1_F EX2_F \
  --out reports/extract_facts/backtest.md >> "$LOG" 2>&1 || log "compare FAILED"
for c in EX1_F EX2_F; do
  python3 scripts/xpts_rescore.py --baseline reports/extract_facts/bt/EX0_F --test "reports/extract_facts/bt/$c" --label "$c" \
    --out reports/extract_facts/xpts >> "$LOG" 2>&1 || log "xpts $c FAILED"
done
log "EXTRACT BACKFILL DONE"

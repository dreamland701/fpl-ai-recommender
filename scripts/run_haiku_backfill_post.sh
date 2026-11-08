#!/usr/bin/env bash
# Post-process the Haiku subagent extraction arm (2026-10-23): once every worker batch under
# reports/extract_facts/haiku_backfill has its .out.json files, merge them into one facts jsonl (same record shape as
# the 31B extractor's), score both readers against played/started outcomes over the full availability-document scope,
# build the ex_* ridge features from the Haiku facts, run the 21-window decision bench (EX0_F / EX1_F / EX2_F) on that
# table and re-score it in xPts. CPU only; runs alongside the 31B backfill. Log logs/haiku_backfill_post.log, sentinel
# "HAIKU BACKFILL POST DONE". Outputs: reports/extract_facts/backfill_haiku_v2.jsonl, backfill_compare.md,
# facts_by_player_week_haiku_v2.json, data/fpl_training_rows_v3_contract_f6_extract_haiku.csv, bt_haiku/, backtest_haiku.md, xpts_haiku/.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/haiku_backfill_post.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src
TREE=reports/extract_facts/haiku_backfill; DOCS=reports/extract_facts/docs_avail.jsonl; OUT=reports/extract_facts/backfill_haiku_v2.jsonl
log "=== Haiku backfill post-processing ==="
python3 scripts/haiku_batch_status.py "$TREE" | tail -1 | tee -a "$LOG"
python3 scripts/haiku_batch_status.py "$TREE" > /dev/null || { log "tree incomplete; HAIKU BACKFILL POST ABORTED"; exit 1; }
python3 - <<PY >> "$LOG" 2>&1 || { log "merge FAILED"; exit 1; }
import sys; sys.path.insert(0, "scripts")
from pathlib import Path
from score_extract_pilot import merge_haiku
rows = merge_haiku(Path("$TREE"), Path("$OUT"))
ok = sum(r["parse_ok"] for r in rows.values()); n = sum(r["n_facts"] for r in rows.values())
print(f"merged {len(rows)} docs, {ok} parse ok, {n} facts -> $OUT")
PY
log "=== scope-wide outcome scoring (Haiku full scope, 31B partial) ==="
python3 scripts/score_extract_pilot.py --docs "$DOCS" --pred haiku_v2="$OUT" --pred 31b_v2=reports/extract_facts/backfill_31b_v2.jsonl \
  --out reports/extract_facts/backfill_compare.md --show 12 >> "$LOG" 2>&1 || log "scoring FAILED"
log "=== features ==="
python3 scripts/build_extract_features.py --docs "$DOCS" --facts "$OUT" --table data/fpl_training_rows_v3_contract_f6_teamnews.csv \
  --out data/fpl_training_rows_v3_contract_f6_extract_haiku.csv --feat-json reports/extract_facts/facts_by_player_week_haiku_v2.json >> "$LOG" 2>&1 || { log "features FAILED"; exit 1; }
log "=== 21-window bench EX0_F / EX1_F / EX2_F on the Haiku table ==="
CONFIGS="EX0_F EX1_F EX2_F" JOBS=6 TABLE=data/fpl_training_rows_v3_contract_f6_extract_haiku.csv OUT=reports/extract_facts/bt_haiku \
  /usr/bin/bash scripts/run_market_backtests.sh >> "$LOG" 2>&1 || log "bench FAILED"
python3 scripts/bt_compare.py --base-dir reports/extract_facts/bt_haiku --base EX0_F --var-dir reports/extract_facts/bt_haiku --configs EX1_F EX2_F \
  --out reports/extract_facts/backtest_haiku.md >> "$LOG" 2>&1 || log "compare FAILED"
for c in EX1_F EX2_F; do
  python3 scripts/xpts_rescore.py --baseline reports/extract_facts/bt_haiku/EX0_F --test "reports/extract_facts/bt_haiku/$c" --label "haiku_$c" \
    --out reports/extract_facts/xpts_haiku >> "$LOG" 2>&1 || log "xpts $c FAILED"
done
log "HAIKU BACKFILL POST DONE"

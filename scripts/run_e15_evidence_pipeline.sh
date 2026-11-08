#!/usr/bin/env bash
set -uo pipefail
# E15: evidence-SELECTION rebuild (Wes 2026-09-10 — "the Scout thing is super
# important; seeing 2 of 10 is an issue; a 25,000-word article can't be used
# directly"). Four changes, all in the evidence path, adapter I/O unchanged:
#   1. attach --analysis-first : FPL/Scout-genre titles outrank match reports
#   2. attach --max-docs 5     : more candidates reach the corpus (was 3)
#   3. split  3 docs x 700ch   : more shown, wider (was 2 x 260)
#   4. multi-mention windowing : long articles contribute up to 3 passages
# Corpus base = the E11-full corpus (fixtures/congestion/defcon attached).
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/e15_pipeline.log; log(){ echo "$(date '+%F %T') $*" | tee -a $LOG; }
BASE="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11.jsonl"
OUT="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e15_sel.jsonl"
SPLIT="reports/llm_residual_v2_e15_selection_top256_thru_2526_34_eval_2526_35_38"

log "E15 attach (analysis-first, max-docs 5)"
PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py \
  --corpus "$BASE" \
  --evidence reports/evidence_guardian_football_2022_23.jsonl \
  --evidence reports/evidence_guardian_football_2023_24.jsonl \
  --evidence reports/evidence_guardian_football_2024_25.jsonl \
  --evidence reports/evidence_guardian_football_2025_26.jsonl \
  --evidence reports/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl \
  --evidence reports/evidence_pl_scout_2022_26.jsonl \
  --evidence reports/evidence_sky_fpl_expert_tips_2022_26.jsonl \
  --include-non-curated --max-docs 5 --analysis-first \
  --output reports/_e15_ev.jsonl >> $LOG 2>&1
PYTHONPATH=src python3 scripts/attach_fixture_outlook_to_corpus.py --corpus reports/_e15_ev.jsonl --history-dir data/fpl_history --output reports/_e15_fx.jsonl >> $LOG 2>&1
PYTHONPATH=src python3 scripts/attach_congestion_to_corpus.py --corpus reports/_e15_fx.jsonl --euro-fixtures data/competition_fixtures/european_fixtures.jsonl --history-dir data/fpl_history --output reports/_e15_cg.jsonl >> $LOG 2>&1
PYTHONPATH=src python3 scripts/attach_defcon_to_corpus.py --corpus reports/_e15_cg.jsonl --training-data data/fpl_training_rows.csv --output "$OUT" >> $LOG 2>&1
[ -s "$OUT" ] || { log "GATE FAILED: attach chain produced nothing"; exit 1; }

log "E15 split (3 docs x 700, multi-window)"
python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus "$OUT" --output-dir "$SPLIT" \
  --include-fixtures --include-congestion --include-provenance --include-defcon --compact-context \
  --prefer-scout --preferred-chars 800 --max-evidence-docs 3 --max-evidence-chars 700 \
  --train-through 2025-26:34 --eval-weeks 2025-26:35-38 --top-n 256 >> $LOG 2>&1
[ -s "$SPLIT/summary.json" ] || { log "GATE FAILED: split build produced nothing"; exit 1; }

python3 - <<PYEOF >> $LOG 2>&1
import json
s=json.load(open("$SPLIT/summary.json"))
cov=s["train_evidence_present"]/max(s["train_count"],1)
multi=analysis=0
for l in open("$SPLIT/train.jsonl"):
    p=json.loads(l)["prompt"]
    if " … " in p: multi+=1
    if any(k in p.lower() for k in ("scout selection","transfer radar","ones to watch","lessons from","fpl")): analysis+=1
print(f"train {s['train_count']} eval {s['eval_count']} coverage {cov:.1%} multi_window_rows {multi} analysis_evidence_rows {analysis}")
assert s["train_count"]>35000 and s["eval_count"]==1024 and cov>0.80
assert multi>2000, f"multi-window barely firing: {multi}"
assert analysis>3000, f"analysis-genre evidence barely present: {analysis}"
PYEOF
[ $? -eq 0 ] || { log "GATE FAILED: sanity asserts"; exit 1; }
python3 scripts/audit_evidence_quality.py --examples "$SPLIT/train.jsonl" >> $LOG 2>&1 || true
log "E15 GATES PASSED — split ready at $SPLIT (training waits for E14)"

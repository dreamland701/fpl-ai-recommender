#!/usr/bin/env bash
set -euo pipefail

# E11 (Wes chose option 3, 2026-08-21): retrain on ALL GWs' data with the
# season-end label fix (rate-normalized 3/5GW labels — corr(PPG, 5gw/5)
# went 0.20 -> 0.40, Gabriel's internal ratio 0.54 -> 0.89) + DefCon made
# VISIBLE to the adapter for the first time (numeric L3/L5 averages +
# rule text in the prompt; spot-check showed no DefCon channel existed —
# 0.6% of rows mentioned it in article text, zero numeric input; E9/E10
# both measurably worse than classic on DefCon-bonus weeks).
#
# Schema note: fixtures + congestion + provenance + defcon, NO
# decomposition/role — deliberate: the live weekly pipeline can produce
# exactly these blocks, so training and deployment see the same schema
# (E10 accidentally trained with none of the attach blocks; live then
# showed it fixture outlooks it had never seen).
#
# Split mirrors E10 (train thru 2025-26:34, eval 35-38, top-256) so the
# DefCon-slice gate is an apples-ish comparison — but labels are the NEW
# rate-normalized ones, so MAEs are only comparable within this run
# (E11 vs freshly-refit classic), not to E10's old-label numbers.

ROOT="/home/wescheng/projects/fpl/fpl"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

BASE="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11.jsonl"
STEP1="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11_ev.jsonl"
STEP2="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11_fx.jsonl"
STEP3="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11_cg.jsonl"
STEP4="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11_full.jsonl"
SPLIT="reports/llm_residual_v2_e11_defcon_top256_thru_2526_34_eval_2526_35_38"

log() { echo "$(date '+%F %T') $*"; }

log "waiting for base corpus export"
until [ -s "$BASE" ] && grep -q '"examples"' logs/e11_corpus_export.log 2>/dev/null; do sleep 60; done
log "base corpus ready ($(wc -l < "$BASE") rows) — attaching evidence"

PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py \
  --corpus "$BASE" \
  --evidence reports/evidence_guardian_football_2022_23.jsonl \
  --evidence reports/evidence_guardian_football_2023_24.jsonl \
  --evidence reports/evidence_guardian_football_2024_25.jsonl \
  --evidence reports/evidence_guardian_football_2025_26.jsonl \
  --evidence reports/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl \
  --evidence reports/evidence_pl_scout_2022_26.jsonl \
  --evidence reports/evidence_sky_fpl_expert_tips_2022_26.jsonl \
  --include-non-curated \
  --output "$STEP1"
PYTHONPATH=src python3 scripts/attach_fixture_outlook_to_corpus.py \
  --corpus "$STEP1" --history-dir data/fpl_history --output "$STEP2"
PYTHONPATH=src python3 scripts/attach_congestion_to_corpus.py \
  --corpus "$STEP2" --euro-fixtures data/competition_fixtures/european_fixtures.jsonl \
  --history-dir data/fpl_history --output "$STEP3"
PYTHONPATH=src python3 scripts/attach_defcon_to_corpus.py \
  --corpus "$STEP3" --training-data data/fpl_training_rows.csv --output "$STEP4"

python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus "$STEP4" \
  --output-dir "$SPLIT" \
  --include-fixtures --include-congestion --include-provenance --include-defcon --compact-context \
  --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 \
  --train-through 2025-26:34 \
  --eval-weeks 2025-26:35-38 \
  --top-n 256

log "split built — sanity gate"
python3 - <<PYEOF
import json
s = json.load(open("$SPLIT/summary.json"))
train_n, eval_n = s["train_count"], s["eval_count"]
cov = s["train_evidence_present"] / max(train_n, 1)
defcon_lines = sum(1 for l in open("$SPLIT/train.jsonl") if "Defensive contribution (rule since 2025-26" in json.loads(l)["prompt"])
fixture_lines = sum(1 for l in open("$SPLIT/train.jsonl") if "Fixture outlook" in json.loads(l)["prompt"])
print(f"train {train_n} eval {eval_n} coverage {cov:.1%} defcon_lines {defcon_lines} fixture_lines {fixture_lines}")
assert train_n > 35000, train_n
assert eval_n == 1024, eval_n
assert cov > 0.80, cov
assert defcon_lines > 7000, f"DefCon lines missing: {defcon_lines}"
assert fixture_lines > 30000, f"fixture outlook missing: {fixture_lines}"
print("SANITY GATE PASSED")
PYEOF

log "launching E11 training + chain"
chmod +x scripts/run_gemma_e4b_residual_e11_defcon.sh scripts/run_e11_post_train_chain.sh
setsid nohup scripts/run_gemma_e4b_residual_e11_defcon.sh > logs/e11_train_nohup.log 2>&1 < /dev/null &
sleep 5
TRAINER_PID=$(pgrep -f "python train_gemma_sft.py" | head -1)
if [ -n "$TRAINER_PID" ]; then
  echo 800 > /proc/$TRAINER_PID/oom_score_adj 2>/dev/null || true
  log "E11 trainer pid $TRAINER_PID (oom 800)"
else
  log "E11 LAUNCH FAILED"; exit 1
fi
setsid nohup scripts/run_e11_post_train_chain.sh > logs/e11_post_train_chain_nohup.log 2>&1 < /dev/null &
log "PIPELINE COMPLETE — training + chain detached"

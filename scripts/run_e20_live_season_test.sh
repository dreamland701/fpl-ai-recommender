#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# Out-of-sample test of E20 on the live season (2026-27 GW2-5), requested by
# Wes on 2026-10-06 ("run a backtest for the SFT").
#
# E20 trained through 2025-26:26, so 2026-27 is unseen, and its prompts carry
# real pre-deadline statuses (E20's training prompts had none). The holdout
# said the points deltas hurt (-49) while routing availability into points
# helped (+45 / +36, 3/3 windows, but those windows also generated the idea).
# This checks both on four fresh weeks.
#
# Steps: corpus (E20 recipe, fixed table) -> split eval 2026-27:2-5 -> wait for
# a free GPU -> decode with E20 -> variants -> backtests vs classic+F6.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/e20_live_season_test.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
TABLE=data/fpl_training_rows_v3_contract_f6.csv
BASE=reports/llm_player_forecast_2627_e20_base.jsonl
FULL=reports/llm_player_forecast_2627_e20_full.jsonl
SPLIT=reports/llm_residual_v2_e20_contract_top256_eval_2627_2_5
PRED=reports/gemma4_e4b_residual_e20_2627_gw2_5_sft_predictions.jsonl
ADAPTER=artifacts/gemma4_e4b_lora_residual_v2_e20_contract
OUT=reports/review_fixes_2026_10/bt_e20_live_season

# GW1 rows are exported only because the split builder needs a non-empty
# train set; nothing is trained on them.
log "=== corpus for 2026-27 GW1-5 (E20 recipe) ==="
if [ ! -s "$FULL" ]; then
  PYTHONPATH=src python3 -m fpl_ai.cli export-llm-player-forecast-corpus --training-data "$TABLE" --output "$BASE" \
    --seasons 2026-27 --start-week 1 --end-week 5 --prompt-style baseline_adjustment >> "$LOG" 2>&1 || { log "export FAILED"; exit 1; }
  PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py --corpus "$BASE" \
    --evidence reports/evidence_guardian_football_2627_gw2.jsonl --evidence reports/evidence_guardian_football_2627_gw3.jsonl \
    --evidence reports/evidence_guardian_football_2627_gw4.jsonl --evidence reports/evidence_guardian_football_2627_gw5.jsonl \
    --evidence reports/evidence_pl_scout_2627_gw2.jsonl --evidence reports/evidence_pl_scout_2627_gw3.jsonl \
    --evidence reports/evidence_pl_scout_2627_gw4.jsonl --evidence reports/evidence_pl_scout_2627_gw5.jsonl \
    --include-non-curated --output reports/_e20live_ev.jsonl >> "$LOG" 2>&1 || { log "evidence FAILED"; exit 1; }
  PYTHONPATH=src python3 scripts/attach_fixture_outlook_to_corpus.py --corpus reports/_e20live_ev.jsonl \
    --history-dir data/fpl_history --output reports/_e20live_fx.jsonl >> "$LOG" 2>&1 || { log "fixtures FAILED"; exit 1; }
  PYTHONPATH=src python3 scripts/attach_congestion_to_corpus.py --corpus reports/_e20live_fx.jsonl \
    --euro-fixtures data/competition_fixtures/european_fixtures.jsonl --history-dir data/fpl_history \
    --output reports/_e20live_cg.jsonl >> "$LOG" 2>&1 || { log "congestion FAILED"; exit 1; }
  PYTHONPATH=src python3 scripts/attach_defcon_to_corpus.py --corpus reports/_e20live_cg.jsonl --training-data "$TABLE" \
    --output "$FULL" >> "$LOG" 2>&1 || { log "defcon FAILED"; exit 1; }
fi
unset FPL_PROMPT_V17
python3 scripts/build_residual_player_forecast_split_v2.py --corpus "$FULL" --output-dir "$SPLIT" \
  --include-fixtures --include-congestion --include-provenance --include-defcon --compact-context \
  --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 \
  --train-through 2026-27:1 --eval-weeks 2026-27:2-5 --top-n 256 >> "$LOG" 2>&1 || { log "split FAILED"; exit 1; }
log "split ready: $(wc -l < "$SPLIT/eval.jsonl") eval rows; real status lines: $(grep -c 'Status pre-deadline: [adisu]\b' "$SPLIT/eval.jsonl")"

log "waiting for a free GPU"
while pgrep -f "^python.*(eval_gemma_responses|train_gemma)" >/dev/null 2>&1; do sleep 120; done
log "=== E20 decode of 2026-27 GW2-5 ==="
python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$SPLIT/eval.jsonl" --output "$PRED" \
  --adapter-path "$ADAPTER" --max-new-tokens 96 --no-4bit --batch-size 16 --resume >> logs/e20_live_season_decode.log 2>&1 \
  || { log "decode FAILED"; exit 1; }

log "=== variants + backtests (2026-27 GW2-5, fixed classic+F6) ==="
python3 reports/review_fixes_2026_10/e20_diagnosis.py "$SPLIT/eval.jsonl" "$PRED" "$OUT/variants" > "$OUT.diagnosis.log" 2>&1 \
  || log "(diagnosis failed)"
python3 reports/review_fixes_2026_10/e20_early_eval.py "$SPLIT/eval.jsonl" "$PRED" E20_2627 > "$OUT.accuracy.json" 2>&1 \
  || log "(accuracy failed)"
mkdir -p "$OUT"
run(){ # tag preds fields
  PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season 2026-27 \
    --initial-train-week-max 1 --start-week 2 --end-week 5 --output-dir "$OUT/$1" --llm-examples "$SPLIT/eval.jsonl" \
    --llm-predictions "$2" --llm-fields "$3" --skip-league-average-fetch > "$OUT/$1.log" 2>&1
}
PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season 2026-27 \
  --initial-train-week-max 1 --start-week 2 --end-week 5 --output-dir "$OUT/classic" --skip-league-average-fetch > "$OUT/classic.log" 2>&1 &
run all "$PRED" all &
run availscaled "$PRED" availability_scaled &
run availnorm "$OUT/variants/e20_pred_availnorm.jsonl" points &
wait
log "$(python3 - <<PYEOF
import json
def p(t):
    try: return json.load(open("$OUT/" + t + "/rolling_squad_backtest.json"))["total_actual_points"]
    except Exception: return None
c = p("classic")
parts = [f"classic+F6 {c}"] + [f"{t} {p(t)} ({(p(t) or 0) - (c or 0):+.0f})" for t in ("all", "availscaled", "availnorm")]
print("2026-27 GW2-5 (out of sample): " + " | ".join(parts))
PYEOF
)"
log "E20 LIVE-SEASON TEST DONE"

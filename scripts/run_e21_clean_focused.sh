#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# E21: clean, focused SFT (Wes 2026-10-10: fix the deadline cutoff, focus on
# helpful articles and fewer players, "see if it eventually leads to a better
# outcome"). Everything else is E20's recipe, so the comparison is clean.
#   - articles only up to 12 h before the deadline, in training AND evaluation.
#     The live refresh moves to ~12 h before the deadline to match. (A 24 h cutoff
#     would drop ~95% of the Guardian's Friday team-news pieces, the most useful
#     type; they come out ~17 h before a Saturday deadline.)
#   - article types that hurt in the out-of-sample source study are dropped
#     (price-change/transfer-trend and transfer-news articles); team news ranks first
#   - the 96 most relevant players per week instead of 256 (training ~20 h, not ~55 h)
# CPU corpus builds start now; GPU training waits for the G6 chain.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/e21.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
die(){ log "E21 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_DEPTH_CHART=0
export FPL_EVIDENCE_DROP='price (rise|fall|change)s?|risers|fallers|most.?bought|most.?sold|transfers in|transfer (window|news|rumou?rs?|gossip|deadline|verdict|latest)|deadline day'
export FPL_EVIDENCE_PRIORITY='team news|predicted line'
TABLE=data/fpl_training_rows_v3_contract_f6.csv
CUTOFF=12
SPLIT=reports/llm_residual_v2_e21_clean_top96_thru_2526_26_eval_2526_27_38
LSPLIT=reports/llm_residual_v2_e21_clean_top96_eval_2627_2_5
ADAPTER=artifacts/gemma4_e4b_lora_residual_v2_e21_clean_top96
SPLIT_FLAGS=(--include-fixtures --include-congestion --include-provenance --include-defcon --compact-context
             --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 --top-n 96)
unset FPL_PROMPT_V17

attach(){ # base out tag evidence...
  local base=$1 out=$2 tag=$3; shift 3
  local ev=(); for f in "$@"; do ev+=(--evidence "$f"); done
  PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py --corpus "$base" "${ev[@]}" --include-non-curated \
    --cutoff-hours "$CUTOFF" --output "reports/_e21${tag}_ev.jsonl" >> "$LOG" 2>&1 || return 1
  PYTHONPATH=src python3 scripts/attach_fixture_outlook_to_corpus.py --corpus "reports/_e21${tag}_ev.jsonl" \
    --history-dir data/fpl_history --output "reports/_e21${tag}_fx.jsonl" >> "$LOG" 2>&1 || return 1
  PYTHONPATH=src python3 scripts/attach_congestion_to_corpus.py --corpus "reports/_e21${tag}_fx.jsonl" \
    --euro-fixtures data/competition_fixtures/european_fixtures.jsonl --history-dir data/fpl_history \
    --output "reports/_e21${tag}_cg.jsonl" >> "$LOG" 2>&1 || return 1
  PYTHONPATH=src python3 scripts/attach_defcon_to_corpus.py --corpus "reports/_e21${tag}_cg.jsonl" --training-data "$TABLE" \
    --output "$out" >> "$LOG" 2>&1
}

log "=== E21 corpora (12 h cutoff) ==="
FULL=reports/llm_player_forecast_2022_26_e21_full.jsonl
[ -s "$FULL" ] || attach reports/llm_player_forecast_2022_26_e20_base.jsonl "$FULL" train \
  reports/evidence_guardian_football_2022_23.jsonl reports/evidence_guardian_football_2023_24.jsonl \
  reports/evidence_guardian_football_2024_25.jsonl reports/evidence_guardian_football_2025_26.jsonl \
  reports/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl reports/evidence_pl_scout_2022_26.jsonl \
  reports/evidence_sky_fpl_expert_tips_2022_26.jsonl || die "training corpus"
LFULL=reports/llm_player_forecast_2627_e21_full.jsonl
[ -s "$LFULL" ] || attach reports/llm_player_forecast_2627_e20_base.jsonl "$LFULL" live \
  reports/evidence_guardian_football_2627_gw2.jsonl reports/evidence_guardian_football_2627_gw3.jsonl \
  reports/evidence_guardian_football_2627_gw4.jsonl reports/evidence_guardian_football_2627_gw5.jsonl \
  reports/evidence_pl_scout_2627_gw2.jsonl reports/evidence_pl_scout_2627_gw3.jsonl \
  reports/evidence_pl_scout_2627_gw4.jsonl reports/evidence_pl_scout_2627_gw5.jsonl || die "live corpus"
python3 scripts/build_residual_player_forecast_split_v2.py --corpus "$FULL" --output-dir "$SPLIT" "${SPLIT_FLAGS[@]}" \
  --train-through 2025-26:26 --eval-weeks 2025-26:27-38 >> "$LOG" 2>&1 || die "split"
python3 scripts/build_residual_player_forecast_split_v2.py --corpus "$LFULL" --output-dir "$LSPLIT" "${SPLIT_FLAGS[@]}" \
  --train-through 2026-27:1 --eval-weeks 2026-27:2-5 >> "$LOG" 2>&1 || die "live split"

log "=== prompt gate ==="
python3 - "$SPLIT" "$LSPLIT" <<'PYEOF' >> "$LOG" 2>&1 || die "prompt gate"
import json, os, re, sys
from datetime import datetime
DOC = re.compile(r"\n\[(\d+)\] ([^|\n]+)\| (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\nTitle: ([^\n]*)")
drop = re.compile(os.environ["FPL_EVIDENCE_DROP"], re.I); prio = re.compile(os.environ["FPL_EVIDENCE_PRIORITY"], re.I)
problems = []
for path in (f"{sys.argv[1]}/train.jsonl", f"{sys.argv[1]}/eval.jsonl", f"{sys.argv[2]}/eval.jsonl"):
    n = ev = late = dropped = misordered = team = 0
    for line in open(path):
        r = json.loads(line); n += 1
        dl = datetime.fromisoformat(str(r["deadline_ts"]).replace("Z", "+00:00")) if r.get("deadline_ts") not in (None, "", "nan") else None
        docs = DOC.findall("\n" + r["prompt"].split("Timestamp-safe text evidence:", 1)[-1])
        ev += bool(docs)
        for i, (idx, src, ts, title) in enumerate(docs):
            if dl and (dl - datetime.fromisoformat(ts.replace("Z", "+00:00"))).total_seconds() < 12 * 3600 - 1:
                late += 1
            dropped += bool(drop.search(title)); team += bool(prio.search(title))
            if i > 0 and prio.search(title) and not prio.search(docs[0][3]):
                misordered += 1
    print(f"{path}: {n} rows, {ev} with evidence, team-news docs {team}, docs <12h {late}, dropped types {dropped}, misordered {misordered}")
    if n == 0 or late or dropped or misordered:
        problems.append(path)
print("problems:", problems or "none")
sys.exit(1 if problems else 0)
PYEOF
log "GATE PASSED: $(wc -l < $SPLIT/train.jsonl) train / $(wc -l < $SPLIT/eval.jsonl) holdout / $(wc -l < $LSPLIT/eval.jsonl) live rows"

log "waiting for the G6 chain to free the GPU"
until grep -aq "AFTER-G5B CHAIN DONE\|G6 IMITATION FAILED\|G6 GRPO FAILED" logs/after_g5b.log 2>/dev/null || ! pgrep -f "^bash scripts/run_after_g5b.sh" >/dev/null; do sleep 300; done
while pgrep -f "^python.*(eval_gemma_responses|train_gemma|g5_grpo_train|expectation_decode)" >/dev/null 2>&1; do sleep 120; done

log "=== E21 training (E20 hyperparameters) ==="
FPL_GEMMA_MODEL_PATH=google/gemma-4-E4B-it FPL_GEMMA_LOAD_IN_4BIT=false FPL_GEMMA_DATA_DIR="$SPLIT" FPL_GEMMA_OUTPUT_DIR="$ADAPTER" \
FPL_GEMMA_MAX_SEQ_LENGTH=1536 FPL_GEMMA_TRUNCATION_MODE=keep_start FPL_GEMMA_MAX_STEPS=-1 FPL_GEMMA_NUM_EPOCHS=1 \
FPL_GEMMA_LEARNING_RATE=5e-5 FPL_GEMMA_TRAIN_BATCH_SIZE=1 FPL_GEMMA_EVAL_BATCH_SIZE=2 FPL_GEMMA_GRAD_ACCUM=16 \
FPL_GEMMA_LOGGING_STEPS=10 FPL_GEMMA_EVAL_STRATEGY=no FPL_GEMMA_SAVE_STEPS=100 FPL_GEMMA_SAVE_TOTAL_LIMIT=3 \
FPL_GEMMA_WARMUP_STEPS=30 FPL_GEMMA_GRADIENT_CHECKPOINTING=true FPL_GEMMA_LORA_DROPOUT=0.0 \
  python train_gemma_sft.py >> logs/train_e21.log 2>&1
[ -s "$ADAPTER/adapter_model.safetensors" ] || die "training (no adapter)"

log "=== E21 decodes: holdout and live, written and average ==="
for pair in "holdout:$SPLIT/eval.jsonl" "live:$LSPLIT/eval.jsonl"; do
  tag=${pair%%:*}; ex=${pair#*:}
  python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$ex" --output "reports/e21_${tag}_greedy.jsonl" \
    --adapter-path "$ADAPTER" --max-new-tokens 96 --no-4bit --batch-size 16 >> "$LOG" 2>&1 || die "$tag decode"
  python -u scripts/expectation_decode.py "$ex" "reports/e21_${tag}_greedy.jsonl" "$ADAPTER" "reports/e21_${tag}_expected.jsonl" 0 >> "$LOG" 2>&1 \
    || die "$tag expectation"
done
python3 scripts/track_sft_accuracy.py \
  --set "E21 holdout (12 h cutoff, focused articles, top 96)" "$SPLIT/eval.jsonl" reports/e21_holdout_greedy.jsonl reports/e21_holdout_expected.jsonl \
  --set "E21 live 2026-27 GW2-5" "$LSPLIT/eval.jsonl" reports/e21_live_greedy.jsonl reports/e21_live_expected.jsonl \
  --out-md reports/review_fixes_2026_10/e21_accuracy.md > /dev/null 2>&1 || log "accuracy ledger FAILED"
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
bt(){ # tag season a b examples preds
  local dir="reports/review_fixes_2026_10/bt_e21/$1_$2_$3_$4"; mkdir -p "$(dirname "$dir")"
  PYTHONPATH=src nice -n 10 python -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$2" \
    --initial-train-week-max $(($3 - 1)) --start-week "$3" --end-week "$4" --output-dir "$dir" \
    --llm-examples "$5" --llm-predictions "$6" --llm-fields all --skip-league-average-fetch > "$dir.log" 2>&1
}
for W in "27 30" "31 34" "35 38"; do set -- $W; bt exp 2025-26 $1 $2 "$SPLIT/eval.jsonl" reports/e21_holdout_expected.jsonl & done
bt exp 2026-27 2 5 "$LSPLIT/eval.jsonl" reports/e21_live_expected.jsonl &
wait
log "RESULT: $(python3 - <<'PYEOF'
import json, os
d = "reports/review_fixes_2026_10/bt_e21"
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
w = [tot(f"{d}/exp_2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
print(f"E21 average, squad points: holdout {w} = {sum(x for x in w if x is not None)} (classic+F6 753, E20 average 736), "
      f"live {tot(f'{d}/exp_2026-27_2_5/rolling_squad_backtest.json')} (classic+F6 242, E20 average 256); accuracy in e21_accuracy.md")
PYEOF
)"
log "E21 DONE"

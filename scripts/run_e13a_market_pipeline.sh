#!/usr/bin/env bash
set -uo pipefail

# E13a-market pipeline: single-variable prompt change vs E11 — every
# player-context block gains "Market: £X.Xm, owned by Y.Y% of managers"
# (attach_market_to_corpus.py joins deadline-time price + ownership from
# the training table). Evidence stays E11's windows; corpus base is the
# E11-full final corpus (fixtures/congestion/defcon already attached).
# Decision metric: the premium-band slice (adapter currently makes the
# £8.5-11.4 band WORSE: 3.45 vs realized 5.64 on the GW35-38 holdout).

ROOT="/home/wescheng/projects/fpl/fpl"
CORPUS_IN="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11_full.jsonl"
CORPUS_OUT="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e13a_market.jsonl"
SPLIT="reports/llm_residual_v2_e13a_market_top256_thru_2526_34_eval_2526_35_38"
CHAINLOG="$ROOT/logs/e13a_pipeline.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" | tee -a "$CHAINLOG"; }
log "E13a pipeline start — attaching market fields"

python3 scripts/attach_market_to_corpus.py \
  --corpus "$CORPUS_IN" --training-data data/fpl_training_rows.csv \
  --output "$CORPUS_OUT" >> "$CHAINLOG" 2>&1
if [ ! -s "$CORPUS_OUT" ]; then log "GATE FAILED — market attach produced no corpus"; exit 1; fi

python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus "$CORPUS_OUT" \
  --output-dir "$SPLIT" \
  --include-fixtures --include-congestion --include-provenance --include-defcon --include-market --compact-context \
  --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 \
  --train-through 2025-26:34 \
  --eval-weeks 2025-26:35-38 \
  --top-n 256 >> "$CHAINLOG" 2>&1
if [ ! -s "$SPLIT/summary.json" ]; then log "GATE FAILED — split build produced no summary"; exit 1; fi

log "split built — sanity gates"
python3 - <<PYEOF >> "$CHAINLOG" 2>&1
import json
s = json.load(open("$SPLIT/summary.json"))
train_n, eval_n = s["train_count"], s["eval_count"]
cov = s["train_evidence_present"] / max(train_n, 1)
market_lines = defcon_lines = 0
for l in open("$SPLIT/train.jsonl"):
    p = json.loads(l)["prompt"]
    if "- Market: £" in p: market_lines += 1
    if "Defensive contribution (rule since 2025-26" in p: defcon_lines += 1
print(f"train {train_n} eval {eval_n} coverage {cov:.1%} market_lines {market_lines} defcon_lines {defcon_lines}")
assert train_n > 35000, train_n
assert eval_n == 1024, eval_n
assert cov > 0.80, cov
assert defcon_lines > 7000, f"DefCon lines missing: {defcon_lines}"
assert market_lines > 0.95 * train_n, f"market lines missing from prompts: {market_lines}/{train_n}"
ev_market = sum(1 for l in open("$SPLIT/eval.jsonl") if "- Market: £" in json.loads(l)["prompt"])
assert ev_market > 0.95 * 1024, f"market lines missing from eval prompts: {ev_market}"
PYEOF
if [ $? -ne 0 ]; then log "GATE FAILED — sanity asserts (see above)"; exit 1; fi
log "gates PASSED — launching E13a training"

setsid nohup bash scripts/run_gemma_e4b_residual_e13a_market.sh > logs/e13a_train_launcher.log 2>&1 < /dev/null &
sleep 240
if grep -qiE "traceback|error" logs/train_e4b_residual_e13a_market.log 2>/dev/null; then
  log "TRAINING LAUNCH FAILED — traceback in first 4 min"
  exit 1
fi
if ! pgrep -f "train_gemma_sft.py" > /dev/null; then
  log "TRAINING LAUNCH FAILED — no trainer process after 4 min"
  exit 1
fi
log "E13a TRAINING LAUNCHED — pid $(pgrep -f train_gemma_sft.py | head -1); eval gated on reports/E13A_EVAL_GO"

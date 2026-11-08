#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after E9-cleansplit training: eval -> top-128 subset scoring
# (ladder comparability) -> 3 gate backtests, widened to GW2-30 (not
# GW12-30) since this split trains on zero 2025-26 rows and can validly
# test the whole available season. Stops after the gate for review.

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_e4b_residual_e9_cleansplit.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e9_cleansplit"
SUMMARY="$ROOT/reports/e4b_residual_e9_cleansplit_gw2_30_eval_summary.json"
CHAINLOG="$ROOT/logs/e9_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
mkdir -p logs/decision_sweep

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for E9 final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: trainer log static for 30 min and no train_runtime — trainer dead or hung?"
  fi
done
log "E9 training complete — launching eval"

chmod +x "$ROOT/scripts/run_gemma_e4b_residual_e9_eval.sh"
nohup "$ROOT/scripts/run_gemma_e4b_residual_e9_eval.sh" > logs/e9_eval_nohup.log 2>&1 &
sleep 120
if [ ! -s "$ROOT/logs/e9_eval_nohup.log" ] && [ ! -s "$ROOT/reports/gemma4_e4b_residual_e9_cleansplit_gw2_30_sft_predictions.jsonl" ]; then
  log "E9 EVAL LAUNCH FAILED — no output after 120s (see logs/e9_eval_nohup.log)"
  exit 1
fi
log "eval running; waiting for summary"

until [ -s "$SUMMARY" ]; do
  size1=$(stat -c %s "$ROOT/logs/e9_eval_nohup.log" 2>/dev/null || echo 0)
  sleep 900
  size2=$(stat -c %s "$ROOT/logs/e9_eval_nohup.log" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && [ ! -s "$SUMMARY" ]; then
    log "EVAL STALLED OR DIED — log static 15 min without summary; aborting chain"
    exit 1
  fi
done
log "eval summary present — running subset scoring + gate"

echo 900 > /proc/self/oom_score_adj 2>/dev/null || true

python3 - <<'EOF' >> "$CHAINLOG" 2>&1
import json, os
from collections import defaultdict

def load(p): return [json.loads(l) for l in open(p) if l.strip()]
ex = load('reports/llm_residual_v2_e9_cleansplit_top256_thru_2425_eval_2526_gw2_30/eval.jsonl')
sft = load('reports/gemma4_e4b_residual_e9_cleansplit_gw2_30_sft_predictions.jsonl')
base = load('reports/gemma4_e4b_residual_e9_cleansplit_gw2_30_base_predictions.jsonl')
assert len(ex)==len(sft)==len(base), (len(ex),len(sft),len(base))

def bscore(row):
    b = row.get('metadata', {}).get('baseline_forecast', {}) or {}
    g = lambda k: float(b.get(k) or 0.0)
    return g('baseline_points_5gw')+0.75*g('baseline_points_3gw')+1.5*g('baseline_points_1gw')+0.02*g('baseline_minutes_1gw')+2.0*g('baseline_appearance_probability')

by_week = defaultdict(list)
for i,row in enumerate(ex): by_week[(row['season'],row['week'])].append((bscore(row),i))
keep=set()
for entries in by_week.values():
    entries.sort(key=lambda t:-t[0]); keep |= {i for _,i in entries[:128]}
os.makedirs('reports/e9_top128_subset', exist_ok=True)
for name,rows in (('eval.jsonl',ex),('sft_predictions.jsonl',sft),('base_predictions.jsonl',base)):
    with open(f'reports/e9_top128_subset/{name}','w') as h:
        for i in range(len(rows)):
            if i in keep: h.write(json.dumps(rows[i],ensure_ascii=False)+'\n')
print('subset rows:', len(keep))
EOF
python3 score_player_forecast_residual_eval.py \
  --examples reports/e9_top128_subset/eval.jsonl \
  --base-predictions reports/e9_top128_subset/base_predictions.jsonl \
  --sft-predictions reports/e9_top128_subset/sft_predictions.jsonl \
  --output reports/e4b_residual_e9_top128subset_gw2_30_eval_summary.json \
  >> "$CHAINLOG" 2>&1 \
  && log "top-128 subset scored" || log "SUBSET SCORING FAILED"

EX=reports/llm_residual_v2_e9_cleansplit_top256_thru_2425_eval_2526_gw2_30/eval.jsonl
PRED=reports/gemma4_e4b_residual_e9_cleansplit_gw2_30_sft_predictions.jsonl
run() { PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows.csv \
  --test-season 2025-26 --initial-train-week-max 1 --start-week 2 --end-week 30 \
  --output-dir reports/backtest_gw2_30_llm_e9_$1 \
  --llm-examples $EX --llm-predictions $PRED --llm-fields $2 --decision-variant $3 \
  --skip-league-average-fetch > logs/decision_sweep/e9_gate_$1.log 2>&1 \
  && log "gate done: $1 -> $(python3 -c "import json; d=json.load(open('reports/backtest_gw2_30_llm_e9_$1/rolling_squad_backtest.json')); print(d['total_actual_points'])" 2>/dev/null)" \
  || log "GATE FAILED: $1"; }
run all_baselineopt all baseline
run availscaled_baselineopt availability_scaled baseline
run avail_softopt availability avail_soft

# The old 1,058/1,069 anchors were computed on GW12-30 only — not a fair
# comparison against this GW2-30 window (different week count). Rerun the
# classic-only anchor on the SAME GW2-30 window so the verdict is
# apples-to-apples.
PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows.csv \
  --test-season 2025-26 --initial-train-week-max 1 --start-week 2 --end-week 30 \
  --output-dir reports/backtest_gw2_30_classic_only \
  --skip-league-average-fetch > logs/decision_sweep/e9_gate_classic_only.log 2>&1 \
  && log "gate done: classic_only (GW2-30 anchor) -> $(python3 -c "import json; d=json.load(open('reports/backtest_gw2_30_classic_only/rolling_squad_backtest.json')); print(d['total_actual_points'])" 2>/dev/null)" \
  || log "GATE FAILED: classic_only"

log "CHAIN COMPLETE — E9 verdict ready for review. Compare each E9 config against THIS run's classic_only (GW2-30), not the old GW12-30-only 1,058 anchor."

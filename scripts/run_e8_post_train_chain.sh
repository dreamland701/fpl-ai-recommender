#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after E8-podcast training: eval -> top-128 subset scoring ->
# 3 gate backtests, same protocol as E7 (mirrors run_e7_post_train_chain.sh).
# Stops after the gate: comparing E8 vs E7 (1,069) vs classic (1,058) is a
# judgment point (ship config, whether podcast evidence earns its GPU cost).

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_e4b_residual_e8_top256_podcast_evidence.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e8_top256_podcast_evidence"
SUMMARY="$ROOT/reports/e4b_residual_e8_top256_gw12_30_eval_summary.json"
CHAINLOG="$ROOT/logs/e8_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
mkdir -p logs/decision_sweep

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for E8 final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: trainer log static for 30 min and no train_runtime — trainer dead or hung?"
  fi
done
log "E8 training complete — launching eval"

chmod +x "$ROOT/scripts/run_gemma_e4b_residual_e8_eval.sh"
nohup "$ROOT/scripts/run_gemma_e4b_residual_e8_eval.sh" > logs/e8_eval_nohup.log 2>&1 &
sleep 120
if [ ! -s "$ROOT/logs/e8_eval_nohup.log" ] && [ ! -s "$ROOT/reports/gemma4_e4b_residual_e8_top256_gw12_30_sft_predictions.jsonl" ]; then
  log "E8 EVAL LAUNCH FAILED — no output after 120s (see logs/e8_eval_nohup.log)"
  exit 1
fi
log "eval running; waiting for summary"

until [ -s "$SUMMARY" ]; do
  size1=$(stat -c %s "$ROOT/logs/e8_eval_nohup.log" 2>/dev/null || echo 0)
  sleep 900
  size2=$(stat -c %s "$ROOT/logs/e8_eval_nohup.log" 2>/dev/null || echo 0)
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
ex = load('reports/llm_residual_v2_e8_top256_podcast_evidence_thru_gw11_eval_gw12_30/eval.jsonl')
sft = load('reports/gemma4_e4b_residual_e8_top256_gw12_30_sft_predictions.jsonl')
base = load('reports/gemma4_e4b_residual_e8_top256_gw12_30_base_predictions.jsonl')
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
os.makedirs('reports/e8_top128_subset', exist_ok=True)
for name,rows in (('eval.jsonl',ex),('sft_predictions.jsonl',sft),('base_predictions.jsonl',base)):
    with open(f'reports/e8_top128_subset/{name}','w') as h:
        for i in range(len(rows)):
            if i in keep: h.write(json.dumps(rows[i],ensure_ascii=False)+'\n')
print('subset rows:', len(keep))
EOF
python3 score_player_forecast_residual_eval.py \
  --examples reports/e8_top128_subset/eval.jsonl \
  --base-predictions reports/e8_top128_subset/base_predictions.jsonl \
  --sft-predictions reports/e8_top128_subset/sft_predictions.jsonl \
  --output reports/e4b_residual_e8_top128subset_gw12_30_eval_summary.json \
  >> "$CHAINLOG" 2>&1 \
  && log "top-128 subset scored" || log "SUBSET SCORING FAILED"

EX=reports/llm_residual_v2_e8_top256_podcast_evidence_thru_gw11_eval_gw12_30/eval.jsonl
PRED=reports/gemma4_e4b_residual_e8_top256_gw12_30_sft_predictions.jsonl
run() { PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows.csv \
  --test-season 2025-26 --initial-train-week-max 11 --start-week 12 --end-week 30 \
  --output-dir reports/backtest_gw12_30_llm_e8_$1 \
  --llm-examples $EX --llm-predictions $PRED --llm-fields $2 --decision-variant $3 \
  --skip-league-average-fetch > logs/decision_sweep/e8_gate_$1.log 2>&1 \
  && log "gate done: $1 -> $(python3 -c "import json; d=json.load(open('reports/backtest_gw12_30_llm_e8_$1/rolling_squad_backtest.json')); print(d['total_actual_points'])" 2>/dev/null)" \
  || log "GATE FAILED: $1"; }
run all_baselineopt all baseline
run availscaled_baselineopt availability_scaled baseline
run avail_softopt availability avail_soft

log "CHAIN COMPLETE — E8 verdict ready for review (compare vs E7 1,069 and classic 1,058)"

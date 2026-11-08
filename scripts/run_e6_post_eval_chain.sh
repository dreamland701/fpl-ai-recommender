#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after the E6 eval: launch G1 (GRPO) on the freed GPU, then run
# the CPU-side E6 analysis (top-128 subset scoring + 3 gate backtests).
# Waits for the eval summary JSON; aborts loudly if the eval died first.
# Rationale: idle-GPU gaps between approved stages wasted hours on 07-13;
# monitors inform, this script is the trigger.

ROOT="/home/wescheng/projects/fpl/fpl"
SUMMARY="$ROOT/reports/e4b_residual_e6_top256_gw12_30_eval_summary.json"
CHAINLOG="$ROOT/logs/e6_post_eval_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
mkdir -p logs/decision_sweep

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for eval summary"

while [ ! -s "$SUMMARY" ]; do
  if ! pgrep -f "run_gemma_e4b_residual_e6_eval" > /dev/null; then
    sleep 30  # grace for the summary write racing the process exit
    if [ ! -s "$SUMMARY" ]; then
      log "CHAIN ABORTED: eval exited without writing summary"
      exit 1
    fi
    break
  fi
  sleep 120
done
log "eval summary present — launching chain"

# Stage 1: G1 GRPO on the freed GPU (approved queue; config via env defaults)
nohup python3 train_gemma_grpo.py > logs/train_grpo_v1.log 2>&1 &
GRPO_PID=$!
echo 800 > /proc/$GRPO_PID/oom_score_adj 2>/dev/null || true
log "G1 GRPO launched pid $GRPO_PID (oom_score_adj 800)"

# Stage 2 (CPU, oom 900 so gate work dies before the trainer under pressure):
echo 900 > /proc/self/oom_score_adj 2>/dev/null || true

# 2a: top-128 subset + ladder-comparable scoring
python3 - <<'EOF' >> "$CHAINLOG" 2>&1
import json, os
from collections import defaultdict

def load(p): return [json.loads(l) for l in open(p) if l.strip()]
ex = load('reports/llm_residual_v2_e6_top256_full_schema_thru_gw11_eval_gw12_30/eval.jsonl')
sft = load('reports/gemma4_e4b_residual_e6_top256_gw12_30_sft_predictions.jsonl')
base = load('reports/gemma4_e4b_residual_e6_top256_gw12_30_base_predictions.jsonl')
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
os.makedirs('reports/e6_top128_subset', exist_ok=True)
for name,rows in (('eval.jsonl',ex),('sft_predictions.jsonl',sft),('base_predictions.jsonl',base)):
    with open(f'reports/e6_top128_subset/{name}','w') as h:
        for i in range(len(rows)):
            if i in keep: h.write(json.dumps(rows[i],ensure_ascii=False)+'\n')
print('subset rows:', len(keep))
EOF
python3 score_player_forecast_residual_eval.py \
  --examples reports/e6_top128_subset/eval.jsonl \
  --base-predictions reports/e6_top128_subset/base_predictions.jsonl \
  --sft-predictions reports/e6_top128_subset/sft_predictions.jsonl \
  --output reports/e4b_residual_e6_top128subset_gw12_30_eval_summary.json \
  >> "$CHAINLOG" 2>&1 \
  && log "top-128 subset scored" || log "SUBSET SCORING FAILED"

# 2b: gate backtests (same three configs as the E4 gate re-run)
EX=reports/llm_residual_v2_e6_top256_full_schema_thru_gw11_eval_gw12_30/eval.jsonl
PRED=reports/gemma4_e4b_residual_e6_top256_gw12_30_sft_predictions.jsonl
run() { PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows.csv \
  --test-season 2025-26 --initial-train-week-max 11 --start-week 12 --end-week 30 \
  --output-dir reports/backtest_gw12_30_llm_e6_$1 \
  --llm-examples $EX --llm-predictions $PRED --llm-fields $2 --decision-variant $3 \
  --skip-league-average-fetch > logs/decision_sweep/e6_gate_$1.log 2>&1 \
  && log "gate done: $1" || log "GATE FAILED: $1"; }
run all_baselineopt all baseline
run availscaled_baselineopt availability_scaled baseline
run avail_softopt availability avail_soft

log "CHAIN COMPLETE"

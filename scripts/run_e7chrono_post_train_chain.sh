#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after E7-chrono training: eval on 2024-25 GW12-30 -> gate on
# 2024-25 (classic baseline + 3 LLM configs) -> launch G2 plan-GRPO on the
# freed GPU (Wes approved G2 next, 2026-07-18). Artifact-based verification
# throughout; the chrono verdict itself is left for review.

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_e4b_residual_e7chrono2425_top256_scout.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e7chrono2425_top256_scout"
SUMMARY="$ROOT/reports/e4b_residual_e7chrono_2425gw12_30_eval_summary.json"
CHAINLOG="$ROOT/logs/e7chrono_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
mkdir -p logs/decision_sweep

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for E7-chrono final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: trainer log static for 30 min and no train_runtime"
  fi
done
log "E7-chrono training complete — launching eval"

nohup scripts/run_gemma_e4b_residual_e7chrono_eval.sh > logs/e7chrono_eval_nohup.log 2>&1 &
sleep 120
if [ ! -s "$ROOT/logs/e7chrono_eval_nohup.log" ]; then
  log "CHRONO EVAL LAUNCH FAILED — empty nohup log after 120s"
  exit 1
fi
log "eval running; waiting for summary"

until [ -s "$SUMMARY" ]; do
  size1=$(stat -c %s "$ROOT/logs/e7chrono_eval_nohup.log" 2>/dev/null || echo 0)
  sleep 900
  size2=$(stat -c %s "$ROOT/logs/e7chrono_eval_nohup.log" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && [ ! -s "$SUMMARY" ]; then
    log "CHRONO EVAL STALLED OR DIED — aborting chain (G2 NOT launched)"
    exit 1
  fi
done
log "eval summary present — running 2024-25 gate"

echo 900 > /proc/self/oom_score_adj 2>/dev/null || true
EX=reports/llm_residual_v2_e7chrono2425_top256_scout_thru_2425gw11_eval_2425gw12_30/eval.jsonl
PRED=reports/gemma4_e4b_residual_e7chrono_2425gw12_30_sft_predictions.jsonl

# Classic-only baseline on the same window first (the comparison anchor).
PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows.csv \
  --test-season 2024-25 --initial-train-week-max 11 --start-week 12 --end-week 30 \
  --output-dir reports/backtest_2425gw12_30_classic_only \
  --skip-league-average-fetch > logs/decision_sweep/e7chrono_gate_classic.log 2>&1 \
  && log "gate done: classic_only -> $(python3 -c "import json; print(json.load(open('reports/backtest_2425gw12_30_classic_only/rolling_squad_backtest.json'))['total_actual_points'])" 2>/dev/null)" \
  || log "GATE FAILED: classic_only"

run() { PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows.csv \
  --test-season 2024-25 --initial-train-week-max 11 --start-week 12 --end-week 30 \
  --output-dir reports/backtest_2425gw12_30_llm_e7chrono_$1 \
  --llm-examples $EX --llm-predictions $PRED --llm-fields $2 --decision-variant $3 \
  --skip-league-average-fetch > logs/decision_sweep/e7chrono_gate_$1.log 2>&1 \
  && log "gate done: $1 -> $(python3 -c "import json; print(json.load(open('reports/backtest_2425gw12_30_llm_e7chrono_$1/rolling_squad_backtest.json'))['total_actual_points'])" 2>/dev/null)" \
  || log "GATE FAILED: $1"; }
run all_baselineopt all baseline
run availscaled_baselineopt availability_scaled baseline
run avail_softopt availability avail_soft

log "chrono gate done — launching G2 plan-GRPO"
FPL_GRPO_MAX_PROMPT_LENGTH=1536 nohup python3 train_gemma_grpo_plan.py > logs/train_grpo_plan_v1.log 2>&1 &
sleep 90
if [ -s logs/train_grpo_plan_v1.log ]; then
  TRAINER_PID=$(ps -ef | grep "python3 train_gemma_grpo_plan.py" | grep -v grep | awk '{print $2}' | head -1)
  if [ -n "$TRAINER_PID" ] && readlink /proc/$TRAINER_PID/exe 2>/dev/null | grep -q python; then
    echo 800 > /proc/$TRAINER_PID/oom_score_adj 2>/dev/null || true
    log "G2 trainer verified, pid $TRAINER_PID (oom guard 800)"
  else
    log "G2 LAUNCH FAILED — log exists but no python process"
  fi
else
  log "G2 LAUNCH FAILED — no log output after 90s"
fi
log "CHAIN COMPLETE — chrono verdict + G2 status ready for review"

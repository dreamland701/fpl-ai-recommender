#!/usr/bin/env bash
set -uo pipefail
# G4 gates, auto-run after training: decision value (E11 ref vs G4) on the
# held-out 2025-26 GW30-38 states, MAE non-regression on GW35-38, premium
# slice. Never loads a model while the trainer is alive (oom rule).
ROOT="/home/wescheng/projects/fpl/fpl"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
MERGED="artifacts/gemma4_e4b_merged_e11_defcon"
ADAPTER="artifacts/gemma4_e4b_g4_forecast_v2"
SPLIT="reports/llm_residual_v2_e11_defcon_top256_thru_2526_34_eval_2526_35_38"
LOG="logs/g4_post_train_chain.log"
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
log "armed; waiting for $ADAPTER/adapter_model.safetensors + trainer exit"
until [ -s "$ADAPTER/adapter_model.safetensors" ] && ! pgrep -f train_gemma_grpo_forecast >/dev/null; do
  if ! pgrep -f train_gemma_grpo_forecast >/dev/null && [ ! -s "$ADAPTER/adapter_model.safetensors" ]; then
    sleep 300
    [ -s "$ADAPTER/adapter_model.safetensors" ] || { log "G4 CHAIN FAILED — trainer exited without saving an adapter (see logs/train_g4_forecast_v2.log)"; exit 1; }
  fi
  sleep 600
done
log "training complete — gate 1: decision value (E11 reference decode, then G4)"
PYTHONPATH=src python3 scripts/run_g4_decision_eval.py --model-path "$MERGED" --tag e11ref >> "$LOG" 2>&1
PYTHONPATH=src python3 scripts/run_g4_decision_eval.py --model-path "$MERGED" --adapter-path "$ADAPTER" --tag g4 >> "$LOG" 2>&1
log "gate 2: MAE on GW35-38"
python -u eval_gemma_responses.py --model-path "$MERGED" --adapter-path "$ADAPTER" --examples "$SPLIT/eval.jsonl" \
  --output reports/gemma4_e4b_g4_forecast_v2_gw35_38_sft_predictions.jsonl --max-new-tokens 96 --no-4bit --batch-size 16 --resume >> logs/g4_eval_nohup.log 2>&1
python score_player_forecast_residual_eval.py --examples "$SPLIT/eval.jsonl" \
  --base-predictions reports/gemma4_e4b_residual_e11_defcon_gw35_38_base_predictions.jsonl \
  --sft-predictions reports/gemma4_e4b_g4_forecast_v2_gw35_38_sft_predictions.jsonl \
  --output reports/e4b_g4_forecast_v2_gw35_38_eval_summary.json \
  --examples-out reports/e4b_g4_forecast_v2_gw35_38_eval_rows.json >> "$LOG" 2>&1
log "gate 4: premium slice"
python3 scripts/report_premium_calibration.py --mode eval --examples "$SPLIT/eval.jsonl" --rows reports/e4b_g4_forecast_v2_gw35_38_eval_rows.json >> "$LOG" 2>&1
python3 - <<PYEOF >> "$LOG" 2>&1
import json
s = json.load(open("reports/e4b_g4_forecast_v2_gw35_38_eval_summary.json"))
m = s["sft_gemma_delta"]
e11 = json.load(open("reports/g4_decision_eval_e11ref.json")); g4 = json.load(open("reports/g4_decision_eval_g4.json"))
tot = lambda rows, k: sum(r[k] for r in rows)
print(f"GATE TABLE | MAE 1gw {m['final_points_1gw_mae']:.3f} (E11 2.060, bar <=2.110) | strict {m['strict_json_predictions']}/{m['total_examples']}")
print(f"decision GW30-38: classic {tot(e11,'classic'):.0f} | E11 {tot(e11,'e11ref'):.0f} | G4 {tot(g4,'g4'):.0f}")
wins = sum(1 for a, b in zip(e11, g4) if b['g4'] > a['e11ref']); ties = sum(1 for a, b in zip(e11, g4) if b['g4'] == a['e11ref'])
print(f"G4 vs E11 per week: wins {wins} ties {ties} losses {len(g4)-wins-ties}")
PYEOF
log "G4 CHAIN COMPLETE — verdict ready for review"

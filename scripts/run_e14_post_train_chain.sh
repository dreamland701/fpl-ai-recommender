#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after E14-defcon: eval on the GW35-38 holdout + the DefCon
# slice — the decision metric. Gate question: does E14 finally beat the
# freshly-refit classic on DefCon-bonus weeks (E9 was −0.30, E10 −0.42,
# both WORSE)? All MAEs are on the NEW rate-normalized labels — compare
# only within this run, not to E10's old-label numbers. Stops for review.

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_e4b_residual_e14_wide.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e14_wide"
DATA_DIR="$ROOT/reports/llm_residual_v2_e14_wide_top256_thru_2526_34_eval_2526_35_38"
SUMMARY="$ROOT/reports/e4b_residual_e14_wide_gw35_38_eval_summary.json"
CHAINLOG="$ROOT/logs/e14_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for E14 final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: E14 trainer log static for 30 min and no train_runtime"
  fi
done
log "E14 training complete — launching eval"

SFT_OUT="$ROOT/reports/gemma4_e4b_residual_e14_wide_gw35_38_sft_predictions.jsonl"
BASE_OUT="$ROOT/reports/gemma4_e4b_residual_e14_wide_gw35_38_base_predictions.jsonl"
(
python -u "$ROOT/eval_gemma_responses.py" \
  --model-path google/gemma-4-E4B-it --examples "$DATA_DIR/eval.jsonl" --output "$SFT_OUT" \
  --adapter-path "$ADAPTER" --max-new-tokens 96 --no-4bit --batch-size 16 --resume \
&& python -u "$ROOT/eval_gemma_responses.py" \
  --model-path google/gemma-4-E4B-it --examples "$DATA_DIR/eval.jsonl" --output "$BASE_OUT" \
  --max-new-tokens 96 --no-4bit --batch-size 16 --resume \
&& python "$ROOT/score_player_forecast_residual_eval.py" \
  --examples "$DATA_DIR/eval.jsonl" --base-predictions "$BASE_OUT" --sft-predictions "$SFT_OUT" \
  --output "$SUMMARY" --examples-out "$ROOT/reports/e4b_residual_e14_wide_gw35_38_eval_rows.json"
) > logs/e14_eval_nohup.log 2>&1
if [ ! -s "$SUMMARY" ]; then
  log "EVAL FAILED — no summary (see logs/e14_eval_nohup.log)"
  exit 1
fi
log "eval summary present: $(python3 -c "
import json
d = json.load(open('$SUMMARY'))
c, s = d['classic_ml'], d['sft_gemma_delta']
print(f\"classic 1gw MAE {c['final_points_1gw_mae']:.3f} vs E14 {s['final_points_1gw_mae']:.3f}; 5gw {c['final_points_5gw_mae']:.3f} vs {s['final_points_5gw_mae']:.3f}; strict_json {s['strict_json_predictions']}/{s['total_examples']}\")" 2>/dev/null)"

python3 - <<'EOF' >> "$CHAINLOG" 2>&1
import csv, json
defcon = {}
for row in csv.DictReader(open('data/fpl_history/2025-26/merged_gw.csv')):
    try: defcon[(int(row['element']), int(row['round']))] = int(row['defensive_contribution'])
    except (ValueError, KeyError): pass
examples = [json.loads(l) for l in open('reports/llm_residual_v2_e14_wide_top256_thru_2526_34_eval_2526_35_38/eval.jsonl')]
rows = json.load(open('reports/e4b_residual_e14_wide_gw35_38_eval_rows.json'))['sft_rows']
THRESH = {'DEF':10,'MID':12,'FWD':12,'GK':999}
from collections import defaultdict
bucket = defaultdict(lambda: {'c':[], 's':[]})
for ex, sft in zip(examples, rows):
    md = ex['metadata']
    dc = defcon.get((md['player_id'], ex['week']))
    if dc is None: continue
    qual = dc >= THRESH.get(md['position'], 999)
    t = sft['target_points_1gw']
    bucket[qual]['c'].append(abs(sft['baseline_points_1gw'] - t))
    bucket[qual]['s'].append(abs(sft['final_points_1gw'] - t))
for qual in (True, False):
    d = bucket[qual]; n = len(d['c'])
    if not n: continue
    cm, sm = sum(d['c'])/n, sum(d['s'])/n
    label = 'DEFCON-BONUS weeks' if qual else 'other weeks'
    print(f'{label}: n={n} classic MAE {cm:.3f} E14 MAE {sm:.3f} improvement {cm-sm:+.3f}  (E9 was -0.299, E10 -0.424 on old labels)')
EOF
log "CHAIN COMPLETE — E14 verdict ready for review (DefCon slice above is the decision metric)"

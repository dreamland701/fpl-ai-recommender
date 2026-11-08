#!/usr/bin/env bash
# H5 (2026-10-25): the H4 team-sheet recipe with two changes aimed at the POINTS channel, which every adapter so far has
# answered with a constant median-like shrink: (1) mean-targeting loss on the regression head (FPL_RH_LOSS=mse instead of
# Huber delta 1, the "median defect" H1 diagnosed and nobody fixed), (2) the pre-deadline sheet now also carries the
# role-class documents' facts (1,425 docs read by Haiku: position/penalty/new-signing/rotation statements) on top of the
# 31B availability facts. Same rows, eval sets, classic reference backtests and ledgers as H1/H4 so H5 - H4 isolates the
# two changes; attribution via scripts/team_sheet_mechanism_check.py (points section: does the 1GW delta stop being a
# constant, does it correlate with the realised residual, does it move on own-role-fact rows?). READ THAT FIRST.
# Log logs/h5_chain.log, sentinel "H5 CHAIN DONE" / "H5 FAILED". Env: FPL_H5_LOSS (mse), FPL_H5_BATCH (1), FPL_H5_ACCUM (16).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h5_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H5 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1
TABLE=data/fpl_training_rows_v3_contract_f6.csv
SPLIT=reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38; LSPLIT=reports/llm_residual_v2_e22_top96_eval_2627_2_6
TSPLIT=reports/llm_residual_v2_e22_top96_ts2_thru_2526_26_eval_2526_27_38; TLSPLIT=reports/llm_residual_v2_e22_top96_ts2_eval_2627_2_6
EX=reports/extract_facts; FACTS=$EX/facts_by_player_week_combined.json; GN=reports/team_news_f16/gn_feat.json
ADAPTER=artifacts/gemma4_e4b_h5_teamsheet_mse; OUT=reports/h_series
LOSS=${FPL_H5_LOSS:-mse}; BATCH=${FPL_H5_BATCH:-1}; ACCUM=${FPL_H5_ACCUM:-16}
watchdog(){ local pid=$1 used
  while kill -0 "$pid" 2>/dev/null; do
    used=$(free -g | awk '/Mem:/{print $3}')
    if [ "${used:-0}" -gt 100 ]; then log "WATCHDOG: used ${used} GB > 100, killing $pid"; kill "$pid"; fi
    sleep 10
  done; }
bt(){ local dir=$1 season=$2 a=$3 b=$4; shift 4; mkdir -p "$(dirname "$dir")"
  [ -s "$dir/rolling_squad_backtest.json" ] && return 0
  local extra=(); [ $# -ge 2 ] && extra=(--llm-examples "$1" --llm-predictions "$2" --llm-fields all)
  nice -n 10 python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week "$a" --end-week "$b" --output-dir "$dir" --skip-league-average-fetch "${extra[@]}" > "$dir.log" 2>&1; }

log "=== H5: role facts (Haiku) + availability facts (31B) -> combined facts json ==="
python3 scripts/haiku_batch_status.py $EX/haiku_role >> "$LOG" 2>&1 || die "haiku_role tree incomplete (see log)"
[ -s $EX/backfill_role_haiku_v2.jsonl ] || python3 -c "
import sys; sys.path.insert(0,'scripts'); from pathlib import Path; from score_extract_pilot import merge_haiku
merge_haiku(Path('$EX/haiku_role'), Path('$EX/backfill_role_haiku_v2.jsonl'))" >> "$LOG" 2>&1 || die "merge_haiku"
cat $EX/backfill_31b_v2.jsonl $EX/backfill_role_haiku_v2.jsonl > $EX/backfill_combined.jsonl
log "combined rows: $(wc -l < $EX/backfill_combined.jsonl) (avail 31B $(wc -l < $EX/backfill_31b_v2.jsonl) + role Haiku $(wc -l < $EX/backfill_role_haiku_v2.jsonl))"
python3 scripts/build_extract_features.py --docs $EX/docs_all.jsonl --facts $EX/backfill_combined.jsonl --table data/fpl_training_rows_v3_contract_f6_teamnews.csv \
  --out data/fpl_training_rows_v3_contract_f6_extract_combined.csv --feat-json "$FACTS" >> "$LOG" 2>&1 || die "features"
[ -s "$FACTS" ] || die "facts json missing: $FACTS"
log "=== H5 splits with the team sheet (availability + role facts) ==="
python3 scripts/attach_team_sheet_to_split.py --split "$SPLIT" --out "$TSPLIT" --facts-json "$FACTS" --teamnews-json "$GN" --table "$TABLE" >> "$LOG" 2>&1 || die "team sheet (holdout split)"
python3 scripts/attach_team_sheet_to_split.py --split "$LSPLIT" --out "$TLSPLIT" --facts-json "$FACTS" --teamnews-json "$GN" --table "$TABLE" >> "$LOG" 2>&1 || die "team sheet (live split)"
[ -s "$TSPLIT/train.jsonl" ] && [ -s "$TSPLIT/eval.jsonl" ] && [ -s "$TLSPLIT/eval.jsonl" ] || die "split files"
while pgrep -f "reghead_predict.py|train_gemma_reghead.py|extract_availability_facts.py" > /dev/null; do sleep 30; done   # one GPU job at a time
log "=== H5 training (E4B, H1 recipe, loss $LOSS, batch $BATCH x accum $ACCUM, ckpt on) ==="
if [ ! -s "$ADAPTER/head.pt" ]; then
FPL_RH_DATA_DIR=$TSPLIT FPL_RH_OUTPUT_DIR=$ADAPTER FPL_RH_LORA_MODE=modules FPL_RH_BATCH=$BATCH FPL_RH_ACCUM=$ACCUM FPL_RH_CKPT=1 FPL_RH_LOSS=$LOSS \
FPL_RH_LR=5e-5 FPL_RH_HEAD_LR=5e-4 FPL_RH_EPOCHS=1 FPL_RH_SAVE_STEPS=100 FPL_RH_COMPACT=1 FPL_RH_MAX_ROWS=0 \
  python3 -u train_gemma_reghead.py >> logs/train_h5.log 2>&1 &
P=$!; watchdog "$P"; wait "$P" || log "trainer exited non-zero"
fi
[ -s "$ADAPTER/head.pt" ] && [ -s "$ADAPTER/adapter_model.safetensors" ] || die "training (no adapter/head)"
log "=== H5 predictions ==="
[ -s "$OUT/h5_holdout_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$TSPLIT/eval.jsonl" "$ADAPTER" "$OUT/h5_holdout_pred.jsonl" 8 >> "$LOG" 2>&1 || die "holdout predict"
[ -s "$OUT/h5_live_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$TLSPLIT/eval.jsonl" "$ADAPTER" "$OUT/h5_live_pred.jsonl" 8 >> "$LOG" 2>&1 || die "live predict"
log "=== H5 ledgers + mechanism checks (vs H4 and vs H1) ==="
python3 scripts/track_sft_accuracy.py --set "H5 holdout 2025-26 GW27-38 (E22 + team sheet + role, mse)" "$TSPLIT/eval.jsonl" "$OUT/h5_holdout_pred.jsonl" "$OUT/h5_holdout_pred.jsonl" \
  --set "H5 live 2026-27 GW2-6" "$TLSPLIT/eval.jsonl" "$OUT/h5_live_pred.jsonl" "$OUT/h5_live_pred.jsonl" --out-md "$OUT/h5_accuracy.md" >> "$LOG" 2>&1 || log "accuracy ledger FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$TSPLIT/eval.jsonl" --base h4=$OUT/h4_holdout_pred.jsonl --test h5=$OUT/h5_holdout_pred.jsonl --out "$OUT/h5_mechanism_holdout.md" >> "$LOG" 2>&1 || log "mechanism check (holdout) FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$TLSPLIT/eval.jsonl" --base h4=$OUT/h4_live_pred.jsonl --test h5=$OUT/h5_live_pred.jsonl --out "$OUT/h5_mechanism_live.md" >> "$LOG" 2>&1 || log "mechanism check (live) FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$TSPLIT/eval.jsonl" --base h1=$OUT/h1_holdout_pred.jsonl --test h5=$OUT/h5_holdout_pred.jsonl --out "$OUT/h5_mechanism_holdout_vs_h1.md" >> "$LOG" 2>&1 || log "mechanism check (holdout vs h1) FAILED"
log "=== H5 decision backtests (4 windows vs bt_classic / bt_h1 / bt_h4) ==="
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"; do set -- $W; bt "$OUT/bt_h5/$1_$2_$3" $1 $2 $3 "$TSPLIT/eval.jsonl" "$OUT/h5_holdout_pred.jsonl" & done
bt "$OUT/bt_h5/2026-27_2_6" 2026-27 2 6 "$TLSPLIT/eval.jsonl" "$OUT/h5_live_pred.jsonl" &
wait
python3 scripts/xpts_rescore.py --label h5_arms --out reports/h_series/xpts --baseline reports/h_series/bt_classic --test reports/h_series/bt_h1 --test reports/h_series/bt_h4 --test reports/h_series/bt_h5 >> "$LOG" 2>&1 || log "xpts rescore FAILED"
python3 scripts/h_series_compare.py h4 h5 --out "$OUT/h5_vs_h4.md" >> "$LOG" 2>&1 || log "compare h4 h5 FAILED"
python3 scripts/h_series_compare.py h1 h5 --out "$OUT/h5_vs_h1.md" >> "$LOG" 2>&1 || log "compare h1 h5 FAILED"
log "RESULT: $(python3 - <<'PY'
import json, os
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
def s(tag):
    w = [tot(f"reports/h_series/{tag}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
    return w, sum(x for x in w if x is not None), tot(f"reports/h_series/{tag}/2026-27_2_6/rolling_squad_backtest.json")
c, h4, h = s("bt_classic"), s("bt_h4"), s("bt_h5")
print(f"H5 squad points: holdout {h[0]} = {h[1]} vs classic {c[1]} ({h[1] - c[1]:+.0f}) vs H4 {h4[1]}; live GW2-6 {h[2]} vs classic {c[2]} vs H4 {h4[2]}")
PY
)"
log "H5 CHAIN DONE"

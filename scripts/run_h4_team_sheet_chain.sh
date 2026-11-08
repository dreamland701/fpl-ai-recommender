#!/usr/bin/env bash
# H4 (2026-10-23): the H1 regression-head recipe on Gemma-4-E4B-it with a dense pre-deadline TEAM SHEET in every prompt
# (facts read by the 31B extractor from the Guardian/Scout stores + the Guardian predicted-lineup categories), the
# step-3 test of the "read facts, not snippets" path Wes approved. Queued behind the extraction backfill (waits for
# "EXTRACT BACKFILL DONE" in logs/extract_backfill.log); one GPU job at a time. Same split rows, eval rows, classic
# reference backtests (reports/h_series/bt_classic) and ledgers as H1, so H4 vs H1 isolates the team sheet.
# Gate before any decision reading: scripts/team_sheet_mechanism_check.py (does P(appear) move where the sheet carries a
# fact, toward the truth on surprise rows?). Log logs/h4_chain.log, sentinel "H4 CHAIN DONE" / "H4 FAILED".
# Env: FPL_H4_BATCH (1), FPL_H4_ACCUM (16), FPL_H4_CKPT (1), FPL_H4_FACTS (facts json), FPL_H4_MAX_ROWS (0 = all).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h4_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H4 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1
TABLE=data/fpl_training_rows_v3_contract_f6.csv
SPLIT=reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38; LSPLIT=reports/llm_residual_v2_e22_top96_eval_2627_2_6
TSPLIT=reports/llm_residual_v2_e22_top96_ts_thru_2526_26_eval_2526_27_38; TLSPLIT=reports/llm_residual_v2_e22_top96_ts_eval_2627_2_6
FACTS=${FPL_H4_FACTS:-reports/extract_facts/facts_by_player_week_31b_v2.json}; GN=reports/team_news_f16/gn_feat.json
ADAPTER=artifacts/gemma4_e4b_h4_teamsheet; OUT=reports/h_series
BATCH=${FPL_H4_BATCH:-1}; ACCUM=${FPL_H4_ACCUM:-16}; CKPT=${FPL_H4_CKPT:-1}; MAX_ROWS=${FPL_H4_MAX_ROWS:-0}
watchdog(){ local pid=$1 used
  while kill -0 "$pid" 2>/dev/null; do
    used=$(free -g | awk '/Mem:/{print $3}')
    if [ "${used:-0}" -gt 100 ]; then log "WATCHDOG: used ${used} GB > 100, killing $pid"; kill "$pid"; fi
    sleep 10
  done; }
bt(){ # dir season a b [examples preds]
  local dir=$1 season=$2 a=$3 b=$4; shift 4; mkdir -p "$(dirname "$dir")"
  [ -s "$dir/rolling_squad_backtest.json" ] && return 0
  local extra=(); [ $# -ge 2 ] && extra=(--llm-examples "$1" --llm-predictions "$2" --llm-fields all)
  nice -n 10 python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week "$a" --end-week "$b" --output-dir "$dir" --skip-league-average-fetch "${extra[@]}" > "$dir.log" 2>&1; }

log "=== H4 queued: waiting for the extraction backfill (logs/extract_backfill.log) ==="
until grep -q "EXTRACT BACKFILL DONE" logs/extract_backfill.log 2>/dev/null; do
  if [ -e logs/stop_h4 ]; then log "stop file logs/stop_h4 present; leaving the queue"; exit 0; fi
  sleep 120
done
[ -s "$FACTS" ] || die "facts json missing: $FACTS"
log "=== H4 splits with the team sheet ==="
python3 scripts/attach_team_sheet_to_split.py --split "$SPLIT" --out "$TSPLIT" --facts-json "$FACTS" --teamnews-json "$GN" --table "$TABLE" >> "$LOG" 2>&1 || die "team sheet (holdout split)"
python3 scripts/attach_team_sheet_to_split.py --split "$LSPLIT" --out "$TLSPLIT" --facts-json "$FACTS" --teamnews-json "$GN" --table "$TABLE" >> "$LOG" 2>&1 || die "team sheet (live split)"
[ -s "$TSPLIT/train.jsonl" ] && [ -s "$TSPLIT/eval.jsonl" ] && [ -s "$TLSPLIT/eval.jsonl" ] || die "split files"
log "=== H4 training (E4B, H1 recipe, batch $BATCH x accum $ACCUM, ckpt $CKPT, max rows $MAX_ROWS) ==="
if [ ! -s "$ADAPTER/head.pt" ]; then
FPL_RH_DATA_DIR=$TSPLIT FPL_RH_OUTPUT_DIR=$ADAPTER FPL_RH_LORA_MODE=modules FPL_RH_BATCH=$BATCH FPL_RH_ACCUM=$ACCUM FPL_RH_CKPT=$CKPT \
FPL_RH_LR=5e-5 FPL_RH_HEAD_LR=5e-4 FPL_RH_EPOCHS=1 FPL_RH_SAVE_STEPS=100 FPL_RH_COMPACT=1 FPL_RH_MAX_ROWS=$MAX_ROWS \
  python3 -u train_gemma_reghead.py >> logs/train_h4.log 2>&1 &
P=$!; watchdog "$P"; wait "$P" || log "trainer exited non-zero"
fi
[ -s "$ADAPTER/head.pt" ] && [ -s "$ADAPTER/adapter_model.safetensors" ] || die "training (no adapter/head)"
log "=== H4 predictions ==="
[ -s "$OUT/h4_holdout_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$TSPLIT/eval.jsonl" "$ADAPTER" "$OUT/h4_holdout_pred.jsonl" 8 >> "$LOG" 2>&1 || die "holdout predict"
[ -s "$OUT/h4_live_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$TLSPLIT/eval.jsonl" "$ADAPTER" "$OUT/h4_live_pred.jsonl" 8 >> "$LOG" 2>&1 || die "live predict"
log "=== H4 ledgers + mechanism check ==="
python3 scripts/track_sft_accuracy.py --set "H4 holdout 2025-26 GW27-38 (E22 + team sheet)" "$TSPLIT/eval.jsonl" "$OUT/h4_holdout_pred.jsonl" "$OUT/h4_holdout_pred.jsonl" \
  --set "H4 live 2026-27 GW2-6" "$TLSPLIT/eval.jsonl" "$OUT/h4_live_pred.jsonl" "$OUT/h4_live_pred.jsonl" --out-md "$OUT/h4_accuracy.md" >> "$LOG" 2>&1 || log "accuracy ledger FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$TSPLIT/eval.jsonl" --base h1=$OUT/h1_holdout_pred.jsonl --test h4=$OUT/h4_holdout_pred.jsonl --out "$OUT/h4_mechanism_holdout.md" >> "$LOG" 2>&1 || log "mechanism check (holdout) FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$TLSPLIT/eval.jsonl" --base h1=$OUT/h1_live_pred.jsonl --test h4=$OUT/h4_live_pred.jsonl --out "$OUT/h4_mechanism_live.md" >> "$LOG" 2>&1 || log "mechanism check (live) FAILED"
log "=== H4 decision backtests (4 windows vs bt_classic / bt_h1) ==="
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"; do set -- $W; bt "$OUT/bt_h4/$1_$2_$3" $1 $2 $3 "$TSPLIT/eval.jsonl" "$OUT/h4_holdout_pred.jsonl" & done
bt "$OUT/bt_h4/2026-27_2_6" 2026-27 2 6 "$TLSPLIT/eval.jsonl" "$OUT/h4_live_pred.jsonl" &
wait
python3 scripts/xpts_rescore.py --label h4_arms --out reports/h_series/xpts --baseline reports/h_series/bt_classic --test reports/h_series/bt_h1 --test reports/h_series/bt_h4 >> "$LOG" 2>&1 || log "xpts rescore FAILED"
python3 scripts/h_series_compare.py h1 h4 --out "$OUT/h4_vs_h1.md" >> "$LOG" 2>&1 || log "compare FAILED"
log "RESULT: $(python3 - <<'PY'
import json, os
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
def s(tag):
    w = [tot(f"reports/h_series/{tag}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
    return w, sum(x for x in w if x is not None), tot(f"reports/h_series/{tag}/2026-27_2_6/rolling_squad_backtest.json")
c, h1, h = s("bt_classic"), s("bt_h1"), s("bt_h4")
print(f"H4 squad points: holdout {h[0]} = {h[1]} vs classic {c[1]} ({h[1] - c[1]:+.0f}) vs H1 {h1[1]}; live GW2-6 {h[2]} vs classic {c[2]} vs H1 {h1[2]}")
PY
)"
log "H4 CHAIN DONE"

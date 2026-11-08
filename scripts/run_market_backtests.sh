#!/usr/bin/env bash
# F14 bookmaker-market features (2026-10-14): the 21-window decision backtest on the market table
# data/fpl_training_rows_v3_contract_f6_mkt.csv (same rows and columns as the F6 table plus mkt_*).
#   MK1_F  = FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_MARKET_FEATS=1
#            (baseline MP1_F in reports/dgw_fix/bt: the ship-candidate forecaster without the market)
#   MKN_F  = FPL_DRAFT_MILP=1 FPL_MARKET_FEATS=1          (baseline MN_F in reports/dgw_fix/bt)
#   MKB_F  = MK1_F with only the base market columns (no crosses), via FPL_MARKET_BASE_ONLY=1
# usage: CONFIGS="MK1_F MKN_F" JOBS=6 scripts/run_market_backtests.sh
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=${OUT:-$ROOT/reports/market_f14/bt}
mkdir -p "$OUT"
TABLE=${TABLE:-data/fpl_training_rows_v3_contract_f6_mkt.csv}

run_one() { # cfg season a b
  local cfg=$1 season=$2 a=$3 b=$4 flag extra="" table=""
  case $cfg in
    # F17 prior-season availability features + corrected F13 (2026-10-27, OUT=reports/prior_f17/bt; the table is per config):
    # PB_F = production F6 table (base), PI_F = F13 injury history re-keyed on `code` (the 10-11 run keyed on the per-season
    # player_id), PP_F = prior_pl_games/no_prior_pl_season/prior_start_share/prior_minutes_share/prior_unknown,
    # PN_F = PP_F without the two share columns
    PB_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0"; table=data/fpl_training_rows_v3_contract_f6.csv ;;
    # minutes-band calibration (2026-10-28, the Isak case; OUT=reports/minutes_band_cal/bt, baseline PB_F in reports/f16_f17_combo/bt)
    MB1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_MINUTES_BAND_CAL=1"; table=data/fpl_training_rows_v3_contract_f6.csv ;;
    MB2_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_MINUTES_BAND_CAL=unflagged"; table=data/fpl_training_rows_v3_contract_f6.csv ;;
    MB3_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_MINUTES_BAND_CAL=low"; table=data/fpl_training_rows_v3_contract_f6.csv ;;
    PI_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0"; table=data/fpl_training_rows_v3_contract_f6_injc.csv ;;
    PP_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0"; table=data/fpl_training_rows_v3_contract_f6_prior.csv ;;
    # F19 team-level baselines (2026-10-31, Wes: up-and-coming teams; OUT=reports/team_level_f19/bt, baseline PB_F in reports/f16_f17_combo/bt)
    TL1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_TEAM_LEVEL_FEATS=1"; table=data/fpl_training_rows_v3_contract_f6_teamlevel.csv ;;
    PN_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0"; table=data/fpl_training_rows_v3_contract_f6_priorn.csv ;;
    # F16 + F17 together (2026-10-28, OUT=reports/f16_f17_combo/bt): TP_F = team-news categories + prior-season shares on one table
    TP_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_TEAM_NEWS_FEATS=1"; table=data/fpl_training_rows_v3_contract_f6_teamnews_prior.csv ;;
    MK1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_MARKET_FEATS=1" ;;
    MKN_F) flag="FPL_DRAFT_MILP=1 FPL_MARKET_FEATS=1" ;;
    MKB_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_MARKET_FEATS=1 FPL_MARKET_BASE_ONLY=1" ;;
    MKR_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_MARKET_FEATS=1 FPL_MARKET_REPLACE_FDR=1" ;;
    # reconstructed weekly status (TABLE=data/fpl_training_rows_v3_contract_f6_status.csv, OUT=reports/status_backfill/bt)
    ST1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0" ;;
    STN_F) flag="FPL_DRAFT_MILP=1" ;;
    # + chance-of-playing feature (TABLE=data/fpl_training_rows_v3_contract_f6_chance.csv)
    CH1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_CHANCE_FEAT=1" ;;
    # F7 depth chart re-test on the status history (TABLE=..._f6_depth.csv) and F15 news horizon (TABLE=..._f6_newsh.csv)
    DC1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DEPTH_CHART=1" ;;
    NH1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_NEWS_HORIZON=1" ;;
    # logistic P(appear) head on the production (status) table, baseline ST1_F
    AP1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_APPEARANCE_LOGISTIC=1" ;;
    # per-position ridge suites on the production (status) table, baseline ST1_F
    PP1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PER_POSITION=1" ;;
    PP2_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PER_POSITION=points" ;;
    # logistic P(appear) + per-position points heads together
    AP2_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_APPEARANCE_LOGISTIC=1 FPL_PER_POSITION=points" ;;
    # hit policy (2026-10-15 transfer-gain calibration): allow a second transfer at -4 when its net projected gain is the best option
    HT2_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0"; extra="--max-transfers-per-week 2" ;;
    HT2G_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0"; extra="--max-transfers-per-week 2 --min-projected-gain 2" ;;
    # F16 Guardian team-news categories (TABLE=data/fpl_training_rows_v3_contract_f6_teamnews.csv, OUT=reports/team_news_f16/bt); TN0_F = same table, flag off
    TN0_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0" ;;
    TN1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_TEAM_NEWS_FEATS=1" ;;
    TN2_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_TEAM_NEWS_FEATS=1 FPL_TEAM_NEWS_OVERRIDE=1" ;;
    TN3_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_TEAM_NEWS_FEATS=1 FPL_TEAM_NEWS_OVERRIDE=minutes" ;;
    TN4_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_TEAM_NEWS_OVERRIDE=1" ;;
    # Extracted availability facts (2026-10-22; TABLE=data/fpl_training_rows_v3_contract_f6_extract.csv, which also carries the
    # gn_ columns; OUT=reports/extract_facts/bt): EX0_F = control, EX1_F = ex_ features, EX2_F = ex_ + Guardian team news
    EX0_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0" ;;
    EX1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_EXTRACT_FEATS=1" ;;
    EX2_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_EXTRACT_FEATS=1 FPL_TEAM_NEWS_FEATS=1" ;;
  esac
  local dir="$OUT/${cfg}_${season}_${a}_${b}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  env $flag PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 \
    $PY -m fpl_ai.cli backtest-squad --training-data ${table:-$TABLE} --test-season "$season" \
    --initial-train-week-max $((a - 1)) --start-week $a --end-week $b \
    --output-dir "$dir" --skip-league-average-fetch $extra > "$dir.log" 2>&1
}
export -f run_one
export ROOT PY OUT TABLE

WINDOWS=(
  "2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25"
  "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"
  "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31" "2023-24 32 35"
  "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35"
)
for cfg in ${CONFIGS:-MK1_F MKN_F}; do
  for w in "${WINDOWS[@]}"; do echo "$cfg $w"; done
done | xargs -P "${JOBS:-6}" -L 1 bash -c 'run_one "$@"' _
echo "$(date '+%F %T') ALL DONE"

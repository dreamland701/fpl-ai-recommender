#!/usr/bin/env bash
# Refresh football-data.co.uk odds: the current season's results file (closing odds for played matches)
# and fixtures.csv (odds for the coming matches), then rebuild data/market_odds/*.csv.
# football-data serves a 302 to a plain urllib/curl UA, so send a browser UA.
# usage: scripts/fetch_market_odds.sh [season_code=2627]
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
CODE="${1:-2627}"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
mkdir -p data/market_odds/raw
curl -sL -m 60 -A "$UA" "https://www.football-data.co.uk/mmz4281/$CODE/E0.csv" -o "data/market_odds/raw/E0_$CODE.csv.tmp" \
  && [ "$(wc -l < data/market_odds/raw/E0_$CODE.csv.tmp)" -gt 1 ] && mv "data/market_odds/raw/E0_$CODE.csv.tmp" "data/market_odds/raw/E0_$CODE.csv"
curl -sL -m 60 -A "$UA" "https://www.football-data.co.uk/fixtures.csv" -o data/market_odds/raw/fixtures.csv.tmp \
  && [ "$(wc -l < data/market_odds/raw/fixtures.csv.tmp)" -gt 1 ] && mv data/market_odds/raw/fixtures.csv.tmp data/market_odds/raw/fixtures.csv
echo "$(date '+%F %T') E0_$CODE: $(wc -l < data/market_odds/raw/E0_$CODE.csv) lines; fixtures.csv E0 rows: $(grep -c '^E0' data/market_odds/raw/fixtures.csv)"
/home/wescheng/venvs/fpl-gemma-lite/bin/python scripts/build_market_odds.py

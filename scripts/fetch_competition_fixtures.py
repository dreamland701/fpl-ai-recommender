#!/usr/bin/env python3
"""Fetch European competition fixtures (UCL/UEL/UECL) from fixturedownload.com.

Feeds verified 2026-07-09: champions-league/europa-league back to 2022,
conference-league from 2024 only (gap: West Ham 2022-23, Villa 2023-24 UECL
runs are not available). A browser User-Agent is required — the default
urllib/curl UA gets 403.

Output: one normalized JSONL with rows
  {"competition": "UCL", "season_start_year": 2025,
   "date_utc": "2025-09-16 18:45:00Z", "home": "...", "away": "..."}

Usage:
  python3 scripts/fetch_competition_fixtures.py \
    --output data/competition_fixtures/european_fixtures.jsonl \
    --start-year 2022 --end-year 2025
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.request
from pathlib import Path

FEED_URL = "https://fixturedownload.com/feed/json/{slug}-{year}"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
COMPETITIONS = {
    "champions-league": "UCL",
    "europa-league": "UEL",
    "conference-league": "UECL",
}


def fetch_feed(slug: str, year: int) -> list[dict] | None:
    request = urllib.request.Request(
        FEED_URL.format(slug=slug, year=year), headers={"User-Agent": USER_AGENT}
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read())
    except Exception as error:
        print(f"  skip {slug}-{year}: {error}")
        return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--start-year", type=int, default=2022)
    parser.add_argument("--end-year", type=int, default=2025)
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []
    for slug, competition in COMPETITIONS.items():
        for year in range(args.start_year, args.end_year + 1):
            matches = fetch_feed(slug, year)
            time.sleep(1.0)
            if not matches:
                continue
            for match in matches:
                rows.append(
                    {
                        "competition": competition,
                        "season_start_year": year,
                        "date_utc": match["DateUtc"],
                        "home": match["HomeTeam"],
                        "away": match["AwayTeam"],
                    }
                )
            print(f"  {slug}-{year}: {len(matches)} matches")

    with output_path.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row) + "\n")
    print(f"wrote {len(rows)} rows -> {output_path}")


if __name__ == "__main__":
    main()

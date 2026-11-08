#!/usr/bin/env python3
"""Attach fixture-congestion context to each corpus row.

Rotation pressure from non-PL competitions is invisible to both the classic
features and the LLM prompt. This adds `metadata.congestion` per row:

  {"euro_competition": "UCL" | "UEL" | "UECL" | null,
   "euro_days_before_gw": int | null,   # European match N days before the PL kickoff (within 5)
   "euro_days_after_gw": int | null,    # European match N days after (managers rest ahead of it)
   "days_since_last_pl": int | null}    # >= 13 marks the first GW after an international/winter break

European fixtures come from `scripts/fetch_competition_fixtures.py`
(fixturedownload.com; UCL/UEL 2022-, UECL 2024- — West Ham 2022-23 and
Villa 2023-24 UECL runs are a known gap). Schedules are public in advance,
so this is timestamp-safe by construction, with the same final-schedule
caveat as fixture_outlook.

Usage:
  python3 scripts/attach_congestion_to_corpus.py \
    --corpus reports/<corpus>.jsonl \
    --euro-fixtures data/competition_fixtures/european_fixtures.jsonl \
    --output reports/<corpus>_congestion.jsonl
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# fixturedownload team name -> FPL teams.csv name where they differ.
FEED_NAME_ALIASES = {"Tottenham": "Spurs", "Man United": "Man Utd"}
EURO_WINDOW_DAYS = 5
BREAK_GAP_DAYS = 13


def _parse_ts(raw: str) -> datetime | None:
    raw = (raw or "").strip().replace(" ", "T").replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def load_team_ids_by_name(history_dir: Path, season: str) -> dict[str, int]:
    path = history_dir / season / "teams.csv"
    if not path.exists():
        return {}
    with path.open() as handle:
        return {row["name"]: int(row["id"]) for row in csv.DictReader(handle)}


def load_player_teams(history_dir: Path, season: str, name_to_id: dict[str, int]) -> dict[tuple[int, int], int]:
    path = history_dir / season / "merged_gw.csv"
    mapping: dict[tuple[int, int], int] = {}
    if not path.exists():
        return mapping
    with path.open() as handle:
        for row in csv.DictReader(handle):
            element = row.get("element")
            week = row.get("GW") or row.get("round")
            team = (row.get("team") or "").strip()
            if not element or not week or not team:
                continue
            team_id = int(team) if team.isdigit() else name_to_id.get(team, 0)
            if team_id > 0:
                mapping[(int(element), int(float(week)))] = team_id
    return mapping


def load_pl_kickoffs(history_dir: Path, season: str) -> dict[int, list[tuple[int, datetime]]]:
    """team_id -> [(event, kickoff_utc)], sorted by kickoff."""
    path = history_dir / season / "fixtures.csv"
    by_team: dict[int, list[tuple[int, datetime]]] = defaultdict(list)
    if not path.exists():
        return by_team
    with path.open() as handle:
        for row in csv.DictReader(handle):
            event_raw = (row.get("event") or "").strip()
            kickoff = _parse_ts(row.get("kickoff_time") or "")
            if not event_raw or kickoff is None:
                continue
            event = int(float(event_raw))
            by_team[int(row["team_h"])].append((event, kickoff))
            by_team[int(row["team_a"])].append((event, kickoff))
    for entries in by_team.values():
        entries.sort(key=lambda item: item[1])
    return by_team


def load_euro_fixtures_for_season(
    path: Path, season: str, name_to_id: dict[str, int]
) -> dict[int, list[tuple[datetime, str]]]:
    """team_id -> [(match_utc, competition)] for one FPL season, sorted."""
    start_year = int(season[:4])
    by_team: dict[int, list[tuple[datetime, str]]] = defaultdict(list)
    with path.open() as handle:
        for line in handle:
            row = json.loads(line)
            if int(row["season_start_year"]) != start_year:
                continue
            when = _parse_ts(row["date_utc"])
            if when is None:
                continue
            for feed_name in (row["home"], row["away"]):
                fpl_name = FEED_NAME_ALIASES.get(feed_name, feed_name)
                team_id = name_to_id.get(fpl_name, 0)
                if team_id > 0:
                    by_team[team_id].append((when, row["competition"]))
    for entries in by_team.values():
        entries.sort(key=lambda item: item[0])
    return by_team


def congestion_for(
    kickoffs: list[tuple[int, datetime]],
    euro_matches: list[tuple[datetime, str]],
    week: int,
) -> dict:
    week_kickoffs = [kickoff for event, kickoff in kickoffs if event == week]
    if not week_kickoffs:
        return {
            "euro_competition": None,
            "euro_days_before_gw": None,
            "euro_days_after_gw": None,
            "days_since_last_pl": None,
        }
    kickoff = min(week_kickoffs)

    competition = None
    days_before = None
    days_after = None
    for when, comp in euro_matches:
        delta_days = (kickoff - when).total_seconds() / 86400.0
        if 0 < delta_days <= EURO_WINDOW_DAYS:
            candidate = int(round(delta_days))
            if days_before is None or candidate < days_before:
                days_before = candidate
                competition = comp
        elif -EURO_WINDOW_DAYS <= delta_days < 0:
            candidate = int(round(-delta_days))
            if days_after is None or candidate < days_after:
                days_after = candidate
                competition = competition or comp

    previous = [when for _, when in kickoffs if when < kickoff]
    days_since_last_pl = None
    if previous:
        days_since_last_pl = int((kickoff - max(previous)).total_seconds() // 86400)

    return {
        "euro_competition": competition,
        "euro_days_before_gw": days_before,
        "euro_days_after_gw": days_after,
        "days_since_last_pl": days_since_last_pl,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--euro-fixtures", required=True, type=Path)
    parser.add_argument("--history-dir", default=Path("data/fpl_history"), type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    season_kickoffs: dict[str, dict[int, list[tuple[int, datetime]]]] = {}
    season_player_teams: dict[str, dict[tuple[int, int], int]] = {}
    season_euro: dict[str, dict[int, list[tuple[datetime, str]]]] = {}

    rows_written = 0
    rows_with_euro = 0
    rows_post_break = 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.corpus.open() as corpus_handle, args.output.open("w") as output_handle:
        for line in corpus_handle:
            row = json.loads(line)
            season = str(row["season"])
            if season not in season_kickoffs:
                season_kickoffs[season] = load_pl_kickoffs(args.history_dir, season)
                name_to_id = load_team_ids_by_name(args.history_dir, season)
                season_player_teams[season] = load_player_teams(args.history_dir, season, name_to_id)
                season_euro[season] = load_euro_fixtures_for_season(args.euro_fixtures, season, name_to_id)
            week = int(row["week"])
            team_id = int(row["metadata"].get("team_id") or 0)
            if team_id <= 0:
                player_id = int(row["metadata"].get("player_id") or 0)
                team_id = season_player_teams[season].get((player_id, week), 0)

            congestion = congestion_for(
                season_kickoffs[season].get(team_id, []),
                season_euro[season].get(team_id, []),
                week,
            )
            row["metadata"]["congestion"] = congestion
            if congestion["euro_competition"]:
                rows_with_euro += 1
            if (congestion["days_since_last_pl"] or 0) >= BREAK_GAP_DAYS:
                rows_post_break += 1
            output_handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            rows_written += 1

    print(
        f"done: {rows_written} rows -> {args.output} "
        f"(euro-flagged: {rows_with_euro}, post-break: {rows_post_break})"
    )


if __name__ == "__main__":
    main()

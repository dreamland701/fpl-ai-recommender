#!/usr/bin/env python3
"""Attach a next-5-gameweeks fixture outlook to each corpus row.

The classic ML features carry next-GW fixture difficulty, but the LLM prompt
has no schedule context at all — it cannot make schedule-aware adjustments
(fixture swings, blanks/doubles, home/away runs). This adds
`metadata.fixture_outlook`: for the target GW and the 4 after it, the row
team's fixtures as {gw, opponent (short name), venue, difficulty}, with
blank GWs explicit and double GWs appearing as two entries.

Fixture schedules are public well in advance, so this is timestamp-safe by
construction. Caveat: historical fixtures.csv reflects the *final* schedule;
postponed-then-rescheduled matches appear where they were played, not where
they stood at the original deadline. Accepted as minor bias.

Usage:
  python3 scripts/attach_fixture_outlook_to_corpus.py \
    --corpus reports/<corpus>.jsonl \
    --history-dir data/fpl_history \
    --output reports/<corpus>_fixtures.jsonl \
    [--horizon 5]
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


def load_team_names(history_dir: Path, season: str) -> dict[int, str]:
    path = history_dir / season / "teams.csv"
    if not path.exists():
        return {}
    with path.open() as handle:
        return {int(row["id"]): row["short_name"] for row in csv.DictReader(handle)}


def load_team_ids_by_name(history_dir: Path, season: str) -> dict[str, int]:
    path = history_dir / season / "teams.csv"
    if not path.exists():
        return {}
    with path.open() as handle:
        return {row["name"]: int(row["id"]) for row in csv.DictReader(handle)}


def load_player_teams(history_dir: Path, season: str, name_to_id: dict[str, int]) -> dict[tuple[int, int], int]:
    """(element_id, gameweek) -> team_id, from merged_gw.csv.

    Historical corpus rows carry team_id = -1 (the exporter never mapped them);
    merged_gw is the ground truth. The 'team' column holds a numeric id in some
    seasons and a full club name in others — resolve both.
    """
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


def load_fixtures(history_dir: Path, season: str) -> dict[int, list[dict]]:
    """Map team_id -> list of {event, opponent_id, venue, difficulty}, sorted by event."""
    path = history_dir / season / "fixtures.csv"
    by_team: dict[int, list[dict]] = defaultdict(list)
    if not path.exists():
        return by_team
    with path.open() as handle:
        for row in csv.DictReader(handle):
            event_raw = (row.get("event") or "").strip()
            if not event_raw:
                continue  # unscheduled (postponed, not yet rearranged)
            event = int(float(event_raw))
            home = int(row["team_h"])
            away = int(row["team_a"])
            by_team[home].append(
                {"event": event, "opponent": away, "venue": "H", "difficulty": int(row["team_h_difficulty"])}
            )
            by_team[away].append(
                {"event": event, "opponent": home, "venue": "A", "difficulty": int(row["team_a_difficulty"])}
            )
    for fixtures in by_team.values():
        fixtures.sort(key=lambda f: f["event"])
    return by_team


def outlook_for(
    fixtures_by_team: dict[int, list[dict]],
    team_names: dict[int, str],
    team_id: int,
    week: int,
    horizon: int,
) -> list[dict]:
    window = range(week, week + horizon)
    entries: list[dict] = []
    team_fixtures = fixtures_by_team.get(team_id, [])
    for gw in window:
        matches = [f for f in team_fixtures if f["event"] == gw]
        if not matches:
            entries.append({"gw": gw, "opponent": None, "venue": None, "difficulty": None})
        for match in matches:
            entries.append(
                {
                    "gw": gw,
                    "opponent": team_names.get(match["opponent"], f"team{match['opponent']}"),
                    "venue": match["venue"],
                    "difficulty": match["difficulty"],
                }
            )
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--history-dir", default=Path("data/fpl_history"), type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--horizon", type=int, default=5)
    args = parser.parse_args()

    season_fixtures: dict[str, dict[int, list[dict]]] = {}
    season_teams: dict[str, dict[int, str]] = {}
    season_player_teams: dict[str, dict[tuple[int, int], int]] = {}
    rows_written = 0
    missing_outlook = 0

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.corpus.open() as corpus_handle, args.output.open("w") as output_handle:
        for line in corpus_handle:
            row = json.loads(line)
            season = str(row["season"])
            if season not in season_fixtures:
                season_fixtures[season] = load_fixtures(args.history_dir, season)
                season_teams[season] = load_team_names(args.history_dir, season)
                name_to_id = load_team_ids_by_name(args.history_dir, season)
                season_player_teams[season] = load_player_teams(args.history_dir, season, name_to_id)
            week = int(row["week"])
            team_id = int(row["metadata"].get("team_id") or 0)
            if team_id <= 0:
                player_id = int(row["metadata"].get("player_id") or 0)
                team_id = season_player_teams[season].get((player_id, week), 0)
            outlook = outlook_for(
                season_fixtures[season], season_teams[season], team_id, week, args.horizon
            )
            if not any(entry["opponent"] for entry in outlook):
                missing_outlook += 1
            row["metadata"]["fixture_outlook"] = outlook
            output_handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            rows_written += 1

    print(f"done: {rows_written} rows -> {args.output} (rows with empty outlook: {missing_outlook})")


if __name__ == "__main__":
    main()

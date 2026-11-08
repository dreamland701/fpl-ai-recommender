#!/usr/bin/env python3
"""Attach positional depth-chart + opponent-record context to a corpus (E17).

WHY (2026-09-18, Wes's Konsa and Evanilson cases)
-------------------------------------------------
Two decision-relevant facts were unreachable by the model:

* **Who is out at my position.** Konsa carried a cold-start P(app) of 0.74
  while Saliba sat injured. Nothing in a player's OWN history encodes "the
  man ahead of me is out", and the text channel could not carry it either:
  evidence windows are mention-centered, so an article about Saliba
  attaches to Saliba's prompt, never Konsa's. Verified — Konsa's GW5 prompt
  mentioned none of his six positional rivals.
* **How good the opponent's defence actually is.** The anchor weights
  opponent_goals_against_avg_3 at +0.0041 and leans on the coarse FDR
  integer, so Evanilson was not discounted for hosting Liverpool.

Both ship as structured fields. This is the lesson from the four failed
regex team-context attempts: do not mine prose for something the official
feed already states.

Chrono-legal: uses only each player's pre-deadline status/news as archived
in the corpus itself, plus team goal records from weeks strictly before the
target week.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
from pathlib import Path

STATUS_UNAVAILABLE = {"i", "d", "s", "u", "n"}


def build_team_resolver(history_root: Path, season: str):
    """Resolve merged_gw's "team" column to an FPL team id for this season.

    The column is NOT consistent across seasons: 2020-21 through 2025-26
    store a club NAME ("Man Utd", "Sheffield Utd"), while 2026-27 stores the
    numeric id. Accept either, matching names against both `name` and
    `short_name` in that season's teams.csv, since FPL ids are season-local.

    Found the hard way: keying on int(team) alone silently produced zero
    opponent records for every training season, which the E17 prompt gate
    caught before training started.
    """
    by_name: dict[str, int] = {}
    teams_csv = history_root / season / "teams.csv"
    if teams_csv.exists():
        for row in csv.DictReader(open(teams_csv)):
            try:
                team_id = int(row["id"])
            except (KeyError, ValueError, TypeError):
                continue
            for field in ("name", "short_name"):
                value = str(row.get(field) or "").strip()
                if value:
                    by_name[value.casefold()] = team_id

    def resolve(raw) -> int | None:
        text = str(raw or "").strip()
        if not text:
            return None
        try:
            return int(text)
        except ValueError:
            return by_name.get(text.casefold())

    return resolve


def team_defensive_records(history_root: Path, season: str, before_week: int, resolve=None):
    """(team_id -> {goals_against_avg_3/5, goals_for_avg_3, rank}) using weeks < before_week."""
    per_team = collections.defaultdict(dict)
    merged = history_root / season / "merged_gw.csv"
    if not merged.exists():
        return {}
    if resolve is None:
        resolve = build_team_resolver(history_root, season)
    for row in csv.DictReader(open(merged)):
        try:
            week = int(row["round"])
            team = resolve(row.get("team"))
            if team is None or week >= before_week:
                continue
            was_home = str(row.get("was_home", "")).lower() in ("true", "1")
            hs, as_ = int(row["team_h_score"]), int(row["team_a_score"])
        except (KeyError, ValueError, TypeError):
            continue
        per_team[team][week] = (as_ if was_home else hs, hs if was_home else as_)

    out = {}
    for team, weeks in per_team.items():
        ordered = [weeks[w] for w in sorted(weeks)]
        if not ordered:
            continue
        last3, last5 = ordered[-3:], ordered[-5:]
        out[team] = {
            "goals_against_avg_3": sum(g for g, _ in last3) / len(last3),
            "goals_against_avg_5": sum(g for g, _ in last5) / len(last5),
            "goals_for_avg_3": sum(f for _, f in last3) / len(last3),
        }
    for rank, team in enumerate(sorted(out, key=lambda t: out[t]["goals_against_avg_3"]), 1):
        out[team]["defence_rank"] = rank
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--history-root", default="data/fpl_history")
    ap.add_argument("--max-teammates", type=int, default=8)
    args = ap.parse_args()

    records = [json.loads(line) for line in open(args.corpus) if line.strip()]
    if not records:
        print("empty corpus")
        return 1

    # Index every player by (season, week, team, position) so each one sees
    # the unit he was actually competing with THAT week. A multi-season
    # training corpus and a single live gameweek both flow through here.
    by_unit = collections.defaultdict(list)
    weeks_seen = set()
    for rec in records:
        meta = rec.get("metadata", {})
        season_i = str(rec.get("season") or meta.get("season") or "")
        week_i = int(rec.get("week") or meta.get("week") or 0)
        weeks_seen.add((season_i, week_i))
        by_unit[(season_i, week_i, meta.get("team_id"), meta.get("position"))].append(meta)

    # Per (season, week): opponent map, team defensive records, team names.
    # Records use only weeks strictly before the target week, so every value
    # is chrono-legal for the row it is attached to.
    defence_by_week = {}
    opponent_by_week = {}
    resolvers = {}
    team_names_by_season = {}
    for season_i, week_i in sorted(weeks_seen):
        if not season_i or not week_i:
            continue
        defence_by_week[(season_i, week_i)] = team_defensive_records(
            Path(args.history_root), season_i, week_i, resolvers.setdefault(
                season_i, build_team_resolver(Path(args.history_root), season_i)
            )
        )
        opp = {}
        fixtures_csv = Path(args.history_root) / season_i / "fixtures.csv"
        if fixtures_csv.exists():
            for row in csv.DictReader(open(fixtures_csv)):
                try:
                    if int(row["event"]) != week_i:
                        continue
                    home, away = int(row["team_h"]), int(row["team_a"])
                except (KeyError, ValueError, TypeError):
                    continue
                opp[home] = away
                opp[away] = home
        opponent_by_week[(season_i, week_i)] = opp
        if season_i not in team_names_by_season:
            names = {}
            teams_csv = Path(args.history_root) / season_i / "teams.csv"
            if teams_csv.exists():
                for row in csv.DictReader(open(teams_csv)):
                    try:
                        names[int(row["id"])] = str(row["name"])
                    except (KeyError, ValueError):
                        continue
            team_names_by_season[season_i] = names
    print(f"indexed {len(weeks_seen)} season-weeks")

    attached_depth = attached_opp = 0
    for rec in records:
        meta = rec.setdefault("metadata", {})
        season_i = str(rec.get("season") or meta.get("season") or "")
        week_i = int(rec.get("week") or meta.get("week") or 0)
        unit = by_unit.get((season_i, week_i, meta.get("team_id"), meta.get("position")), [])

        mates = []
        for other in unit:
            if other.get("player_id") == meta.get("player_id"):
                continue
            status = str(other.get("status_pre_deadline") or "a").lower()
            baseline = other.get("baseline_forecast") or {}
            minutes = baseline.get("baseline_minutes_1gw")
            mates.append(
                {
                    "name": other.get("player_name"),
                    "status": status,
                    "news": (other.get("news_pre_deadline") or "").strip(),
                    "minutes_avg_3": minutes,
                    "_unavailable": status in STATUS_UNAVAILABLE,
                    "_minutes": float(minutes or 0.0),
                }
            )
        # Show the unavailable rivals first (that is the role-change signal),
        # then the biggest minute-earners, so the window is never wasted on
        # fringe players who never play.
        mates.sort(key=lambda m: (not m["_unavailable"], -m["_minutes"]))
        trimmed = [{k: v for k, v in m.items() if not k.startswith("_")} for m in mates[: args.max_teammates]]
        if trimmed:
            meta["depth_chart"] = trimmed
            attached_depth += 1

        defence = defence_by_week.get((season_i, week_i), {})
        opponent_id = opponent_by_week.get((season_i, week_i), {}).get(meta.get("team_id"))
        if opponent_id is not None and opponent_id in defence:
            context = dict(defence[opponent_id])
            context["name"] = team_names_by_season.get(season_i, {}).get(opponent_id, str(opponent_id))
            meta["opponent_context"] = context
            attached_opp += 1

    with open(args.output, "w") as fh:
        for rec in records:
            fh.write(json.dumps(rec) + "\n")
    print(f"records {len(records):,}  depth_chart attached {attached_depth:,}  opponent_context attached {attached_opp:,}")
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

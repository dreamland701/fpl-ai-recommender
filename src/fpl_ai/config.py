"""Project configuration and default policies."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


TRAINING_CUTOFF_SEASON = "2026-27"
TRAINING_CUTOFF_WEEK = 9
# GW31 was excluded here while the 2025-26 season was still in progress:
# two of its fixtures (Arsenal-Wolves, Man City-Crystal Palace) were
# rearranged into GW26 and GW36 respectively, and mid-season the schedule
# hadn't fully settled. Confirmed post-season (2026-08-06) that the
# underlying data already re-tags each fixture/player-row to the round it
# was actually played in (verified directly: Saka has two separate
# round=26 rows, not a round=31 + round=26 split), and every fixture in
# the season now shows finished=True — no ambiguity remains. No exclusion
# needed.
EXCLUDED_WEEKS: Dict[Tuple[str, int], str] = {}

POSITION_ID_TO_NAME = {
    1: "GK",
    2: "DEF",
    3: "MID",
    4: "FWD",
}

POSITION_NAME_TO_SQUAD_COUNT = {
    "GK": 2,
    "DEF": 5,
    "MID": 5,
    "FWD": 3,
}

STARTING_XI_SIZE = 11
# Official XI rule: exactly one goalkeeper, at least three defenders and at
# least one forward. The squad caps bound everything else (so at least two
# midfielders), which is why formations are derived rather than listed.
STARTING_XI_MINIMUMS = {"GK": 1, "DEF": 3, "MID": 0, "FWD": 1}
STARTING_XI_MAXIMUMS = {
    "GK": 1,
    **{position: POSITION_NAME_TO_SQUAD_COUNT[position] for position in ("DEF", "MID", "FWD")},
}


def _legal_formations() -> Tuple[Dict[str, int], ...]:
    outfield = STARTING_XI_SIZE - STARTING_XI_MINIMUMS["GK"]
    formations = []
    for defenders in range(STARTING_XI_MINIMUMS["DEF"], STARTING_XI_MAXIMUMS["DEF"] + 1):
        for forwards in range(STARTING_XI_MINIMUMS["FWD"], STARTING_XI_MAXIMUMS["FWD"] + 1):
            midfielders = outfield - defenders - forwards
            if STARTING_XI_MINIMUMS["MID"] <= midfielders <= STARTING_XI_MAXIMUMS["MID"]:
                formations.append({"GK": 1, "DEF": defenders, "MID": midfielders, "FWD": forwards})
    return tuple(formations)


STARTING_FORMATIONS = _legal_formations()


@dataclass(frozen=True)
class CuratedSource:
    name: str
    category: str
    url: str
    max_age_days: int


DEFAULT_CURATED_SOURCES: List[CuratedSource] = [
    CuratedSource(
        name="Fantasy Premier League",
        category="official_fpl",
        url="https://fantasy.premierleague.com",
        max_age_days=7,
    ),
    CuratedSource(
        name="Premier League",
        category="official_premier_league",
        url="https://www.premierleague.com",
        max_age_days=7,
    ),
    CuratedSource(
        name="The Scout",
        category="official_scout",
        url="https://www.premierleague.com/news/topic/fpl",
        max_age_days=7,
    ),
    CuratedSource(
        name="Official Club Sites",
        category="official_club",
        url="https://www.premierleague.com/clubs",
        max_age_days=3,
    ),
    CuratedSource(
        name="BBC Sport Football",
        category="trusted_news",
        url="https://www.bbc.com/sport/football",
        max_age_days=3,
    ),
    CuratedSource(
        name="The Guardian Football",
        category="trusted_news",
        url="https://www.theguardian.com/football",
        max_age_days=3,
    ),
    CuratedSource(
        name="r/FantasyPL",
        category="reddit",
        url="https://www.reddit.com/r/FantasyPL/",
        max_age_days=2,
    ),
]


def parse_season_start_year(season: str) -> int:
    return int(season.split("-")[0])


def is_excluded_week(season: str, week: int) -> bool:
    return (season, week) in EXCLUDED_WEEKS


def season_is_after_cutoff(season: str) -> bool:
    return parse_season_start_year(season) > parse_season_start_year(TRAINING_CUTOFF_SEASON)


def week_is_after_cutoff(season: str, week: int) -> bool:
    return season == TRAINING_CUTOFF_SEASON and week > TRAINING_CUTOFF_WEEK


def iter_curated_source_urls() -> Iterable[str]:
    for source in DEFAULT_CURATED_SOURCES:
        yield source.url

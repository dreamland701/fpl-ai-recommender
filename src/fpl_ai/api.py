"""Official FPL API access and live week-state helpers."""

from __future__ import annotations

import hashlib
import os
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Sequence

import pandas as pd
import requests

from . import market, news_horizon
from .config import POSITION_ID_TO_NAME
from .dataset import get_week_eligibility
from .types import WeekState


class OfficialFPLClient:
    BASE_URL = "https://fantasy.premierleague.com/api"

    def __init__(self, cache_dir: Optional[Path] = None, session: Optional[requests.Session] = None, timeout: int = 20):
        self.cache_dir = Path(cache_dir) if cache_dir else None
        self.session = session or requests.Session()
        self.timeout = timeout

    def _cache_path(self, endpoint: str) -> Optional[Path]:
        if self.cache_dir is None:
            return None
        digest = hashlib.sha1(endpoint.encode("utf-8")).hexdigest()[:16]
        return self.cache_dir / f"{digest}.json"

    def _get_json(self, endpoint: str) -> Dict[str, Any]:
        cache_path = self._cache_path(endpoint)
        if cache_path and cache_path.exists():
            return json.loads(cache_path.read_text())

        response = self.session.get(f"{self.BASE_URL}/{endpoint.lstrip('/')}", timeout=self.timeout)
        response.raise_for_status()
        payload = response.json()
        if cache_path:
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_text(json.dumps(payload))
        return payload

    def bootstrap_static(self) -> Dict[str, Any]:
        return self._get_json("bootstrap-static/")

    def average_entry_scores(self) -> Dict[int, float]:
        events = self.bootstrap_static().get("events", [])
        scores: Dict[int, float] = {}
        for event in events:
            if event.get("id") is None or event.get("average_entry_score") is None:
                continue
            scores[int(event["id"])] = float(event["average_entry_score"])
        return scores

    def fixtures(self) -> Sequence[Dict[str, Any]]:
        return self._get_json("fixtures/")

    def event_live(self, event_id: int) -> Dict[str, Any]:
        return self._get_json(f"event/{event_id}/live/")

    def element_summary(self, player_id: int) -> Dict[str, Any]:
        return self._get_json(f"element-summary/{player_id}/")


def _infer_season_from_deadline(deadline: datetime) -> str:
    year = deadline.year if deadline.month >= 7 else deadline.year - 1
    return f"{year}-{str((year + 1) % 100).zfill(2)}"


class OfficialSnapshotService:
    def __init__(self, client: Optional[OfficialFPLClient] = None):
        self.client = client or OfficialFPLClient()

    def build_week_state(self, deadline_ts: str) -> WeekState:
        deadline = datetime.fromisoformat(deadline_ts.replace("Z", "+00:00"))
        if deadline.tzinfo is None:
            deadline = deadline.replace(tzinfo=timezone.utc)
        else:
            deadline = deadline.astimezone(timezone.utc)

        bootstrap = self.client.bootstrap_static()
        fixtures = self.client.fixtures()
        events = bootstrap.get("events", [])
        if not events:
            raise ValueError("bootstrap-static returned no events.")

        def distance(event: Dict[str, Any]) -> float:
            event_deadline = datetime.fromisoformat(event["deadline_time"].replace("Z", "+00:00"))
            return abs((event_deadline - deadline).total_seconds())

        current_event = min(events, key=distance)
        current_event_id = int(current_event["id"])
        current_season = _infer_season_from_deadline(deadline)
        week_fixtures = [fixture for fixture in fixtures if int(fixture.get("event") or 0) == current_event_id]
        player_count = len(bootstrap.get("elements", []))
        eligibility = get_week_eligibility(current_season, current_event_id)
        notes = [eligibility.reason]
        if any(not fixture.get("finished", False) for fixture in week_fixtures):
            notes.append("Includes scheduled but not-yet-finished fixtures.")
        return WeekState(
            season=current_season,
            week=current_event_id,
            deadline_ts=current_event["deadline_time"],
            eligible=eligibility,
            fixture_count=len(week_fixtures),
            player_count=player_count,
            notes=notes,
            source_timestamps={
                "bootstrap_static": datetime.now(timezone.utc).isoformat(),
                "fixtures": datetime.now(timezone.utc).isoformat(),
            },
        )

    def build_current_week_frame(self, deadline_ts: str) -> pd.DataFrame:
        """Create a live player frame for the selected deadline using official endpoints."""

        deadline = datetime.fromisoformat(deadline_ts.replace("Z", "+00:00"))
        if deadline.tzinfo is None:
            deadline = deadline.replace(tzinfo=timezone.utc)
        else:
            deadline = deadline.astimezone(timezone.utc)

        bootstrap = self.client.bootstrap_static()
        fixtures = self.client.fixtures()
        events = bootstrap.get("events", [])
        current_event = min(
            events,
            key=lambda event: abs(
                (
                    datetime.fromisoformat(event["deadline_time"].replace("Z", "+00:00")).astimezone(timezone.utc)
                    - deadline
                ).total_seconds()
            ),
        )
        event_id = int(current_event["id"])

        players = pd.DataFrame(bootstrap.get("elements", []))
        if players.empty:
            return players
        players = players.rename(
            columns={
                "id": "player_id",
                "web_name": "player_name",
                "team": "team_id",
                "element_type": "position_id",
                "now_cost": "price",
                "selected_by_percent": "selected_by_percent",
                "transfers_in_event": "transfers_in_event",
                "transfers_out_event": "transfers_out_event",
                "status": "status",
                "news": "news",
            }
        )
        players["price"] = players["price"] / 10.0
        players["position"] = players["position_id"].map(POSITION_ID_TO_NAME).fillna("")
        players["week"] = event_id
        players["season"] = _infer_season_from_deadline(deadline)
        if "status" not in players.columns:
            players["status"] = "a"
        if "news" not in players.columns:
            players["news"] = ""
        # official 0-100 chance of playing next round (None for most available players) -> -1 = not recorded
        chance_source = players["chance_of_playing_next_round"] if "chance_of_playing_next_round" in players.columns else pd.Series(-1.0, index=players.index)
        players["chance_of_playing"] = pd.to_numeric(chance_source, errors="coerce").fillna(-1.0)
        fixtures_frame = pd.DataFrame([fixture for fixture in fixtures if int(fixture.get("event") or 0) == event_id])
        # Fixtures per team over the next 3 and 5 events, scaled to a full horizon when the season
        # has fewer events left (rate-equivalent, like the 3GW/5GW labels): the multipliers the
        # per-fixture horizon heads use (FPL_PER_FIXTURE=1, models.py). Doubles and blanks a few
        # weeks out are known from the published fixture list, so this is pre-deadline information.
        last_event = max((int(event.get("id") or 0) for event in events), default=event_id)
        for horizon in (3, 5):
            window = range(event_id, min(event_id + horizon, last_event) + 1)
            counts: Dict[int, int] = {}
            for fixture in fixtures:
                if int(fixture.get("event") or 0) in window:
                    for team in (fixture.get("team_h"), fixture.get("team_a")):
                        counts[int(team)] = counts.get(int(team), 0) + 1
            scale = horizon / max(1, len(window))
            players[f"fixtures_next_{horizon}"] = players["team_id"].map(lambda t: counts.get(int(t), 0) * scale).astype(float)
        if fixtures_frame.empty:
            players["fixture_count"] = 0
            players["fixture_difficulty_mean"] = 0.0
            players["home_fixture_count"] = 0
            players["away_fixture_count"] = 0
            return players

        home = fixtures_frame[["team_h", "team_a", "team_h_difficulty"]].rename(
            columns={"team_h": "team_id", "team_a": "opponent_team_id", "team_h_difficulty": "fixture_difficulty"}
        )
        home["was_home"] = True
        away = fixtures_frame[["team_a", "team_h", "team_a_difficulty"]].rename(
            columns={"team_a": "team_id", "team_h": "opponent_team_id", "team_a_difficulty": "fixture_difficulty"}
        )
        away["was_home"] = False
        fixture_lookup = pd.concat([home, away], ignore_index=True)
        team_fixtures = (
            fixture_lookup.groupby("team_id", as_index=False)
            .agg(
                fixture_count=("team_id", "size"),
                fixture_difficulty_mean=("fixture_difficulty", "mean"),
                home_fixture_count=("was_home", "sum"),
            )
            .sort_values("team_id")
        )
        players = players.merge(team_fixtures, on="team_id", how="left")
        players["fixture_count"] = players["fixture_count"].fillna(0).astype(int)
        players["fixture_difficulty_mean"] = pd.to_numeric(players["fixture_difficulty_mean"], errors="coerce").fillna(0.0)
        players["home_fixture_count"] = pd.to_numeric(players["home_fixture_count"], errors="coerce").fillna(0).astype(int)
        players["away_fixture_count"] = players["fixture_count"] - players["home_fixture_count"]
        # F14 (FPL_MARKET_FEATS=1): this week's closing-odds market numbers per team, from
        # data/market_odds/upcoming_odds.csv (scripts/fetch_market_odds.sh), falling back to the
        # season's fitted team strengths when a match has no odds yet.
        # F15 (FPL_NEWS_HORIZON=1): return dates in the news against the next five gameweeks' first kickoffs
        if os.environ.get("FPL_NEWS_HORIZON", "0") == "1":
            kickoffs = []
            for offset in range(5):
                times = [datetime.fromisoformat(f["kickoff_time"].replace("Z", "+00:00")) for f in fixtures
                         if int(f.get("event") or 0) == event_id + offset and f.get("kickoff_time")]
                kickoffs.append(min(times) if times else None)
            horizon = news_horizon.live_news_horizon(players["status"], players["news"].fillna("").astype(str), deadline, kickoffs)
            for column in news_horizon.FEATURES:
                players[column] = horizon[column].to_numpy()
        if market.enabled():
            per_team = market.team_week_market(str(players["season"].iloc[0]), fixtures_frame)
            for column in market.BASE_FEATURES:
                players[column] = players["team_id"].map(lambda t: per_team.get(int(t), {}).get(column, 0.0)).astype(float)
        return players

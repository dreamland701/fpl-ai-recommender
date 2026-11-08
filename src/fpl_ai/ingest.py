"""Historical data download and official-season backfill."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

import pandas as pd
import requests

from .api import OfficialFPLClient
from .dataset import CanonicalDataset


DEFAULT_COMPLETED_SEASONS = (
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
)

VAASTAV_RAW_BASES = (
    "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data",
    "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/main/data",
)


@dataclass
class SyncSeasonSummary:
    season: str
    source: str
    files_written: List[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class SyncHistorySummary:
    history_root: str
    seasons: List[SyncSeasonSummary]
    fetched_at: str


class HistoricalDataIngestor:
    def __init__(
        self,
        history_root: str,
        session: Optional[requests.Session] = None,
        timeout: int = 30,
    ):
        self.history_root = Path(history_root)
        self.session = session or requests.Session()
        self.timeout = timeout
        self.official_client = OfficialFPLClient(session=self.session, timeout=timeout)

    def _request_text(self, url: str) -> str:
        response = self.session.get(url, timeout=self.timeout)
        if getattr(response, "status_code", 200) == 404:
            raise FileNotFoundError(url)
        response.raise_for_status()
        text = getattr(response, "text", None)
        if text is None:
            raise ValueError(f"Expected text response from {url}")
        return text

    def _download_first_available(self, relative_paths: Sequence[str]) -> str:
        errors: List[str] = []
        for base_url in VAASTAV_RAW_BASES:
            for relative_path in relative_paths:
                url = f"{base_url}/{relative_path.lstrip('/')}"
                try:
                    return self._request_text(url)
                except FileNotFoundError:
                    errors.append(url)
                    continue
        raise FileNotFoundError(
            "Could not find any of the expected historical files. Tried: " + ", ".join(errors)
        )

    def _write_text(self, path: Path, content: str) -> str:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return str(path)

    def sync_completed_season(self, season: str) -> SyncSeasonSummary:
        season_dir = self.history_root / season
        files_written = [
            self._write_text(
                season_dir / "players_raw.csv",
                self._download_first_available([f"{season}/players_raw.csv"]),
            ),
            self._write_text(
                season_dir / "fixtures.csv",
                self._download_first_available([f"{season}/fixtures.csv"]),
            ),
            self._write_text(
                season_dir / "merged_gw.csv",
                self._download_first_available(
                    [
                        f"{season}/merged_gw.csv",
                        f"{season}/gws/merged_gw.csv",
                    ]
                ),
            ),
        ]
        return SyncSeasonSummary(
            season=season,
            source="vaastav_github",
            files_written=files_written,
            notes=["Downloaded the minimum files required by the training pipeline."],
        )

    def sync_completed_seasons(self, seasons: Sequence[str]) -> List[SyncSeasonSummary]:
        return [self.sync_completed_season(season) for season in seasons]

    def _backfill_current_players_raw(self, season_dir: Path, bootstrap: Dict[str, object]) -> str:
        players = pd.DataFrame(bootstrap.get("elements", []))
        if players.empty:
            raise ValueError("Official FPL bootstrap-static payload does not contain player data.")
        path = season_dir / "players_raw.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        players.to_csv(path, index=False)
        return str(path)

    def _backfill_current_fixtures(self, season_dir: Path, fixtures: Sequence[Dict[str, object]]) -> str:
        path = season_dir / "fixtures.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(list(fixtures)).to_csv(path, index=False)
        return str(path)

    def _backfill_current_merged_gameweeks(
        self,
        season_dir: Path,
        bootstrap: Dict[str, object],
        fixtures: Sequence[Dict[str, object]],
        max_gw: int,
    ) -> str:
        elements = list(bootstrap.get("elements", []))
        fixture_by_id = {
            int(fixture["id"]): fixture
            for fixture in fixtures
            if fixture.get("id") is not None and int(fixture.get("event") or 0) <= max_gw
        }
        rows: List[Dict[str, object]] = []
        for element in elements:
            player_id = int(element["id"])
            summary = self.official_client.element_summary(player_id)
            for history_row in summary.get("history", []):
                round_number = int(history_row.get("round") or 0)
                if round_number == 0 or round_number > max_gw:
                    continue
                fixture = fixture_by_id.get(int(history_row.get("fixture") or -1), {})
                if history_row.get("was_home"):
                    inferred_team = fixture.get("team_h", element.get("team"))
                else:
                    inferred_team = fixture.get("team_a", element.get("team"))
                row = dict(history_row)
                row["element"] = player_id
                row["name"] = element.get("web_name", "")
                row["team"] = inferred_team
                row["position_id"] = element.get("element_type")
                row["status"] = "a"
                row["news"] = ""
                rows.append(row)

        if not rows:
            raise ValueError("Official FPL backfill produced no player-history rows.")

        merged_gw = pd.DataFrame(rows).sort_values(["round", "element", "fixture"]).reset_index(drop=True)
        path = season_dir / "merged_gw.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        merged_gw.to_csv(path, index=False)
        return str(path)

    def backfill_current_official_season(self, season: str, max_gw: int) -> SyncSeasonSummary:
        season_dir = self.history_root / season
        bootstrap = self.official_client.bootstrap_static()
        fixtures = list(self.official_client.fixtures())

        files_written = [
            self._backfill_current_players_raw(season_dir, bootstrap),
            self._backfill_current_fixtures(season_dir, fixtures),
            self._backfill_current_merged_gameweeks(season_dir, bootstrap, fixtures, max_gw=max_gw),
        ]
        notes = [
            f"Backfilled official FPL data through GW{max_gw}.",
            "Historical status/news were neutralized to avoid leaking current bootstrap availability into past weeks.",
        ]
        return SyncSeasonSummary(
            season=season,
            source="official_fpl_api",
            files_written=files_written,
            notes=notes,
        )

    def write_manifest(self, summary: SyncHistorySummary) -> str:
        path = self.history_root / "source_manifest.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(asdict(summary), indent=2))
        return str(path)

    def sync_history(
        self,
        completed_seasons: Sequence[str] = DEFAULT_COMPLETED_SEASONS,
        current_season: str = "2025-26",
        current_max_gw: int = 30,
        include_completed: bool = True,
        include_current: bool = True,
    ) -> SyncHistorySummary:
        season_summaries: List[SyncSeasonSummary] = []
        if include_completed:
            season_summaries.extend(self.sync_completed_seasons(completed_seasons))
        if include_current:
            season_summaries.append(self.backfill_current_official_season(current_season, current_max_gw))

        summary = SyncHistorySummary(
            history_root=str(self.history_root),
            seasons=season_summaries,
            fetched_at=datetime.now(timezone.utc).isoformat(),
        )
        self.write_manifest(summary)
        return summary

    def bootstrap_training_data(
        self,
        training_output: str,
        completed_seasons: Sequence[str] = DEFAULT_COMPLETED_SEASONS,
        current_season: str = "2025-26",
        current_max_gw: int = 30,
    ) -> SyncHistorySummary:
        summary = self.sync_history(
            completed_seasons=completed_seasons,
            current_season=current_season,
            current_max_gw=current_max_gw,
        )
        dataset = CanonicalDataset.from_history_root(self.history_root)
        dataset.to_csv(training_output)
        return summary

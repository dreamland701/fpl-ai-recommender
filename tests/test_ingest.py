import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from fpl_ai.ingest import HistoricalDataIngestor


class FakeResponse:
    def __init__(self, status_code=200, text=None, json_payload=None):
        self.status_code = status_code
        self.text = text
        self._json_payload = json_payload

    def raise_for_status(self):
        if self.status_code >= 400 and self.status_code != 404:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        if self._json_payload is None:
            raise ValueError("No JSON payload configured.")
        return self._json_payload


class FakeSession:
    def __init__(self, responses):
        self.responses = responses

    def get(self, url, timeout=30):
        return self.responses.get(url, FakeResponse(status_code=404, text=""))


class IngestTestCase(unittest.TestCase):
    def test_sync_completed_season_downloads_minimum_files(self):
        merged_csv = "round,element,name,team,value,selected,transfers_in,transfers_out,opponent_team,was_home,kickoff_time,minutes,total_points,fixture,team_h_score,team_a_score\n1,1,Player A,1,75,10.0,100,20,2,True,2025-08-16T11:30:00Z,90,6,10,2,1\n"
        players_csv = "id,web_name,team,element_type,now_cost,selected_by_percent,status,news\n1,Player A,1,3,75,10.0,a,\n"
        fixtures_csv = "id,event,team_h,team_a,team_h_difficulty,team_a_difficulty\n10,1,1,2,3,3\n"
        session = FakeSession(
            {
                "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/players_raw.csv": FakeResponse(text=players_csv),
                "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/fixtures.csv": FakeResponse(text=fixtures_csv),
                "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2024-25/gws/merged_gw.csv": FakeResponse(text=merged_csv),
            }
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            ingestor = HistoricalDataIngestor(history_root=tmpdir, session=session)
            summary = ingestor.sync_completed_season("2024-25")

            season_dir = Path(tmpdir) / "2024-25"
            self.assertEqual(summary.source, "vaastav_github")
            self.assertTrue((season_dir / "players_raw.csv").exists())
            self.assertTrue((season_dir / "fixtures.csv").exists())
            self.assertTrue((season_dir / "merged_gw.csv").exists())

    def test_backfill_current_official_season_caps_gameweeks_and_neutralizes_status(self):
        session = FakeSession(
            {
                "https://fantasy.premierleague.com/api/bootstrap-static/": FakeResponse(
                    json_payload={
                        "elements": [
                            {
                                "id": 1,
                                "web_name": "Player A",
                                "team": 1,
                                "element_type": 3,
                                "status": "d",
                                "news": "Current knock",
                                "now_cost": 76,
                                "selected_by_percent": "10.0",
                            }
                        ]
                    }
                ),
                "https://fantasy.premierleague.com/api/fixtures/": FakeResponse(
                    json_payload=[
                        {"id": 10, "event": 1, "team_h": 1, "team_a": 2, "team_h_difficulty": 3, "team_a_difficulty": 3},
                        {"id": 20, "event": 2, "team_h": 3, "team_a": 1, "team_h_difficulty": 2, "team_a_difficulty": 4},
                    ]
                ),
                "https://fantasy.premierleague.com/api/element-summary/1/": FakeResponse(
                    json_payload={
                        "history": [
                            {
                                "round": 1,
                                "fixture": 10,
                                "value": 75,
                                "selected": 10.0,
                                "transfers_in": 100,
                                "transfers_out": 20,
                                "opponent_team": 2,
                                "was_home": True,
                                "kickoff_time": "2025-08-16T11:30:00Z",
                                "minutes": 90,
                                "total_points": 6,
                                "team_h_score": 2,
                                "team_a_score": 1,
                            },
                            {
                                "round": 2,
                                "fixture": 20,
                                "value": 76,
                                "selected": 11.0,
                                "transfers_in": 120,
                                "transfers_out": 25,
                                "opponent_team": 3,
                                "was_home": False,
                                "kickoff_time": "2025-08-23T11:30:00Z",
                                "minutes": 80,
                                "total_points": 5,
                                "team_h_score": 1,
                                "team_a_score": 1,
                            },
                        ]
                    }
                ),
            }
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            ingestor = HistoricalDataIngestor(history_root=tmpdir, session=session)
            summary = ingestor.backfill_current_official_season("2025-26", max_gw=1)

            season_dir = Path(tmpdir) / "2025-26"
            merged = pd.read_csv(season_dir / "merged_gw.csv", keep_default_na=False)
            self.assertEqual(summary.source, "official_fpl_api")
            self.assertEqual(merged["round"].max(), 1)
            self.assertEqual(merged.iloc[0]["status"], "a")
            self.assertEqual(merged.iloc[0]["news"], "")
            self.assertEqual(int(merged.iloc[0]["team"]), 1)

    def test_bootstrap_training_data_builds_training_output(self):
        session = FakeSession(
            {
                "https://fantasy.premierleague.com/api/bootstrap-static/": FakeResponse(
                    json_payload={
                        "elements": [
                            {
                                "id": 1,
                                "web_name": "Player A",
                                "team": 1,
                                "element_type": 3,
                                "status": "a",
                                "news": "",
                                "now_cost": 76,
                                "selected_by_percent": "10.0",
                            }
                        ]
                    }
                ),
                "https://fantasy.premierleague.com/api/fixtures/": FakeResponse(
                    json_payload=[
                        {"id": 10, "event": 1, "team_h": 1, "team_a": 2, "team_h_difficulty": 3, "team_a_difficulty": 3},
                        {"id": 11, "event": 2, "team_h": 2, "team_a": 1, "team_h_difficulty": 2, "team_a_difficulty": 4},
                    ]
                ),
                "https://fantasy.premierleague.com/api/element-summary/1/": FakeResponse(
                    json_payload={
                        "history": [
                            {
                                "round": 1,
                                "fixture": 10,
                                "value": 75,
                                "selected": 10.0,
                                "transfers_in": 100,
                                "transfers_out": 20,
                                "opponent_team": 2,
                                "was_home": True,
                                "kickoff_time": "2025-08-16T11:30:00Z",
                                "minutes": 90,
                                "total_points": 6,
                                "team_h_score": 2,
                                "team_a_score": 1,
                            },
                            {
                                "round": 2,
                                "fixture": 11,
                                "value": 76,
                                "selected": 11.0,
                                "transfers_in": 120,
                                "transfers_out": 25,
                                "opponent_team": 2,
                                "was_home": False,
                                "kickoff_time": "2025-08-23T11:30:00Z",
                                "minutes": 80,
                                "total_points": 5,
                                "team_h_score": 1,
                                "team_a_score": 1,
                            },
                        ]
                    }
                ),
            }
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            ingestor = HistoricalDataIngestor(history_root=tmpdir, session=session)
            output_path = Path(tmpdir) / "training.csv"
            summary = ingestor.bootstrap_training_data(
                training_output=str(output_path),
                completed_seasons=[],
                current_season="2025-26",
                current_max_gw=2,
            )

            self.assertTrue(output_path.exists())
            self.assertTrue((Path(tmpdir) / "source_manifest.json").exists())
            training_frame = pd.read_csv(output_path)
            self.assertIn("label_points_3gw", training_frame.columns)
            self.assertEqual({summary.seasons[0].season}, {"2025-26"})


if __name__ == "__main__":
    unittest.main()

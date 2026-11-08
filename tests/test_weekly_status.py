import tempfile
import unittest
from pathlib import Path

import pandas as pd

from fpl_ai.dataset import STATUS_UNKNOWN, normalize_vaastav_history


class WeeklyStatusBackfillTestCase(unittest.TestCase):
    """A season without a per-week status column takes its status from weekly_status.csv
    (pre-deadline snapshots reconstructed from the data repository's history), week by week,
    and stays unknown where no snapshot exists. The end-of-season players_raw status is never used."""

    def _season_dir(self, root: Path, with_weekly: bool) -> None:
        season = root / "2024-25"
        season.mkdir(parents=True)
        pd.DataFrame([
            {"element": 1, "name": "A", "team": "Arsenal", "position": "MID", "fixture": 1, "opponent_team": 2, "total_points": 5,
             "was_home": True, "kickoff_time": "2024-08-17T14:00:00Z", "team_h_score": 1, "team_a_score": 0, "round": 1,
             "minutes": 90, "value": 80, "selected": 100, "transfers_in": 1, "transfers_out": 1, "GW": 1},
            {"element": 1, "name": "A", "team": "Arsenal", "position": "MID", "fixture": 11, "opponent_team": 3, "total_points": 0,
             "was_home": False, "kickoff_time": "2024-08-24T14:00:00Z", "team_h_score": 0, "team_a_score": 0, "round": 2,
             "minutes": 0, "value": 80, "selected": 100, "transfers_in": 1, "transfers_out": 1, "GW": 2},
        ]).to_csv(season / "merged_gw.csv", index=False)
        pd.DataFrame([{"id": 1, "code": 100, "team": 1, "element_type": 3, "status": "i", "news": "end of season injury",
                       "now_cost": 80, "selected_by_percent": 1.0, "first_name": "A", "second_name": "A", "web_name": "A"}]
                     ).to_csv(season / "players_raw.csv", index=False)
        pd.DataFrame([{"id": 1, "event": 1, "team_h": 1, "team_a": 2, "kickoff_time": "2024-08-17T14:00:00Z", "team_h_difficulty": 2, "team_a_difficulty": 4},
                      {"id": 11, "event": 2, "team_h": 3, "team_a": 1, "kickoff_time": "2024-08-24T14:00:00Z", "team_h_difficulty": 3, "team_a_difficulty": 3}]
                     ).to_csv(season / "fixtures.csv", index=False)
        if with_weekly:
            pd.DataFrame([{"week": 2, "player_id": 1, "status": "d", "news": "Knock - 50% chance", "chance_next": 50,
                           "snapshot_ts": "2024-08-22T10:00:00+00:00", "age_hours": 50.0}]).to_csv(season / "weekly_status.csv", index=False)

    def test_weekly_snapshot_fills_status_per_week_and_leaves_the_rest_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._season_dir(Path(tmp), with_weekly=True)
            raw = normalize_vaastav_history(tmp)
        by_week = raw.set_index("week")
        self.assertEqual(by_week.loc[2, "status"], "d")
        self.assertEqual(by_week.loc[2, "news"], "Knock - 50% chance")
        self.assertEqual(by_week.loc[1, "status"], STATUS_UNKNOWN)   # no snapshot before the GW1 deadline
        self.assertEqual(by_week.loc[1, "news"], "")

    def test_without_a_snapshot_file_the_end_of_season_status_is_not_used(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._season_dir(Path(tmp), with_weekly=False)
            raw = normalize_vaastav_history(tmp)
        self.assertTrue((raw["status"] == STATUS_UNKNOWN).all())
        self.assertTrue((raw["news"] == "").all())


if __name__ == "__main__":
    unittest.main()

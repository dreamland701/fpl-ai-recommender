import os
import unittest
from unittest import mock

import pandas as pd

from fpl_ai.dataset import CanonicalDataset, build_training_frame, chance_of_playing_feature, get_feature_columns
from tests.test_dataset import synthetic_raw_history


class ChanceOfPlayingFeatureTestCase(unittest.TestCase):
    def test_recorded_percentage_wins_over_the_status_prior(self):
        status = pd.Series(["a", "d", "d", "i", "s", "", None, "a"])
        chance = pd.Series([-1, -1, 75, 0, -1, -1, -1, 100])
        out = chance_of_playing_feature(status, chance).tolist()
        self.assertEqual(out, [1.0, 0.5, 0.75, 0.0, 0.0, 1.0, 1.0, 1.0])

    def test_without_a_chance_column_the_status_prior_is_used(self):
        out = chance_of_playing_feature(pd.Series(["a", "i", "u"]), None).tolist()
        self.assertEqual(out, [1.0, 0.1, 0.0])

    def test_training_and_live_frames_carry_the_feature_only_when_flagged(self):
        raw = synthetic_raw_history()
        with mock.patch.dict(os.environ, {"FPL_CHANCE_FEAT": "1"}):
            frame = build_training_frame(raw)
        self.assertIn("chance_pre_deadline", get_feature_columns(frame))
        by_key = frame.set_index(["player_id", "week"])["chance_pre_deadline"]
        self.assertAlmostEqual(by_key.loc[(2, 3)], 0.5)   # the synthetic "d" row, no percentage recorded
        self.assertTrue((by_key.drop((2, 3)) == 1.0).all())
        with mock.patch.dict(os.environ, {"FPL_CHANCE_FEAT": "0"}):
            plain = build_training_frame(raw)
        self.assertNotIn("chance_pre_deadline", plain.columns)
        # live: a doubtful player with a recorded 25% reads 0.25, an injured one without a percentage reads 0.1
        dataset = CanonicalDataset(frame)
        official = pd.DataFrame([
            {"season": "2025-26", "week": 4, "player_id": 1, "player_name": "Mid One", "team_id": 1, "position": "MID",
             "price": 8.1, "selected_by_percent": 20.0, "status": "d", "news": "Knock", "chance_of_playing": 25,
             "fixture_count": 1, "fixture_difficulty_mean": 3, "home_fixture_count": 1, "away_fixture_count": 0},
            {"season": "2025-26", "week": 4, "player_id": 2, "player_name": "Fwd Two", "team_id": 2, "position": "FWD",
             "price": 7.5, "selected_by_percent": 18.0, "status": "i", "news": "Hamstring", "chance_of_playing": -1,
             "fixture_count": 1, "fixture_difficulty_mean": 3, "home_fixture_count": 0, "away_fixture_count": 1},
        ])
        with mock.patch.dict(os.environ, {"FPL_CHANCE_FEAT": "1"}):
            live = dataset.build_live_week_frame(official)
        by_id = live.set_index("player_id")
        self.assertAlmostEqual(by_id.loc[1, "chance_pre_deadline"], 0.25)
        self.assertAlmostEqual(by_id.loc[2, "chance_pre_deadline"], 0.1)
        self.assertEqual(by_id.loc[1, "status_flag_pre_deadline"], 1.0)


if __name__ == "__main__":
    unittest.main()

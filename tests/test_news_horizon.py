import os
import unittest
from datetime import datetime, timezone
from unittest import mock

import pandas as pd

from fpl_ai import news_horizon
from fpl_ai.dataset import build_training_frame, get_feature_columns
from tests.test_dataset import synthetic_raw_history


def utc(y, m, d, h=14):
    return datetime(y, m, d, h, tzinfo=timezone.utc)


class NewsHorizonTestCase(unittest.TestCase):
    def test_return_dates_parse_with_year_rollover(self):
        self.assertEqual(news_horizon.parse_return_date("Hamstring injury - Expected back 11 Jan", utc(2024, 12, 20)), utc(2025, 1, 11, 0))
        self.assertEqual(news_horizon.parse_return_date("Suspended until 04 Dec", utc(2024, 11, 28)), utc(2024, 12, 4, 0))
        self.assertEqual(news_horizon.parse_return_date("Thigh injury - Expected back 25 Oct", utc(2026, 10, 15)), utc(2026, 10, 25, 0))
        self.assertIsNone(news_horizon.parse_return_date("Knee injury - Unknown return date", utc(2024, 11, 28)))
        self.assertIsNone(news_horizon.parse_return_date("Ankle injury - 75% chance of playing", utc(2024, 11, 28)))
        self.assertIsNone(news_horizon.parse_return_date("", utc(2024, 11, 28)))

    def test_weeks_out_count_kickoffs_before_the_return_date(self):
        kickoffs = [utc(2024, 11, 30), utc(2024, 12, 3), utc(2024, 12, 7), utc(2024, 12, 14), utc(2024, 12, 21)]
        ref = utc(2024, 11, 28)
        self.assertEqual(news_horizon.horizon_features("i", "Hamstring injury - Expected back 10 Dec", ref, kickoffs), [3.0, 3.0, 1.0, 0.0])
        self.assertEqual(news_horizon.horizon_features("s", "Suspended until 04 Dec", ref, kickoffs), [2.0, 2.0, 1.0, 0.0])
        self.assertEqual(news_horizon.horizon_features("i", "Knee injury - Unknown return date", ref, kickoffs), [0.0, 0.0, 0.0, 1.0])
        self.assertEqual(news_horizon.horizon_features("d", "Knock - 75% chance of playing", ref, kickoffs), [0.0, 0.0, 0.0, 0.0])
        self.assertEqual(news_horizon.horizon_features("u", "Loaned to Stoke City", ref, kickoffs), [3.0, 5.0, 0.0, 1.0])
        self.assertEqual(news_horizon.horizon_features("a", "", ref, kickoffs), [0.0, 0.0, 0.0, 0.0])
        # a return date beyond every listed kickoff counts the whole horizon; unknown kickoffs are skipped
        self.assertEqual(news_horizon.horizon_features("i", "Expected back 01 Mar", ref, kickoffs[:3] + [None, None]), [3.0, 3.0, 1.0, 0.0])

    def test_training_frame_carries_the_features_only_when_flagged(self):
        raw = synthetic_raw_history()
        raw.loc[(raw["player_id"] == 2) & (raw["week"] == 3), "news"] = "Groin injury - Expected back 06 Sep"
        with mock.patch.dict(os.environ, {"FPL_NEWS_HORIZON": "1"}):
            frame = build_training_frame(raw)
        for column in news_horizon.FEATURES:
            self.assertIn(column, get_feature_columns(frame))
        row = frame[(frame["player_id"] == 2) & (frame["week"] == 3)].iloc[0]
        self.assertEqual(row["return_known"], 1.0)
        self.assertGreaterEqual(row["out_weeks_3"], 1.0)   # the week-3 kickoff (30 Aug) is before 6 Sep
        with mock.patch.dict(os.environ, {"FPL_NEWS_HORIZON": "0"}):
            plain = build_training_frame(raw)
        for column in news_horizon.FEATURES:
            self.assertNotIn(column, plain.columns)


if __name__ == "__main__":
    unittest.main()

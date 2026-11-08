import os
import unittest
from unittest import mock

import numpy as np
import pandas as pd

from fpl_ai.models import PositionRoutedSuite, fit_model_suite_from_frame


def _frame(n_per=600, seed=1):
    rng = np.random.default_rng(seed)
    rows = []
    for position, slope in (("GK", 0.5), ("DEF", 1.0), ("MID", 2.0), ("FWD", 3.0)):
        x = rng.uniform(0, 1, n_per)
        rows.append(pd.DataFrame({"position": position, "feat": x, "fixture_count": 1.0,
                                  "label_points_1gw": slope * x + rng.normal(0, 0.05, n_per),
                                  "label_points_3gw": 3 * slope * x, "label_points_5gw": 5 * slope * x,
                                  "label_minutes_1gw": 90.0, "label_appearance_probability": 1.0}))
    return pd.concat(rows, ignore_index=True)


class PerPositionSuiteTestCase(unittest.TestCase):
    def test_per_position_fits_recover_different_slopes(self):
        frame = _frame()
        with mock.patch.dict(os.environ, {"FPL_PER_POSITION": "1"}):
            routed = fit_model_suite_from_frame(train_frame=frame, feature_names=["feat"])
        self.assertIsInstance(routed, PositionRoutedSuite)
        self.assertEqual(set(routed.suites), {"GK", "DEF", "MID", "FWD"})
        week = pd.DataFrame({"position": ["GK", "DEF", "MID", "FWD", "AM"], "feat": [1.0] * 5, "fixture_count": 1.0,
                             "player_id": range(5), "player_name": "p", "team_id": 1, "season": "2025-26", "week": 9, "price": 5.0})
        preds = {f.player_id: f.predicted_points_1gw for f in routed.predict_frame(week)}
        self.assertAlmostEqual(preds[0], 0.5, delta=0.1)
        self.assertAlmostEqual(preds[1], 1.0, delta=0.1)
        self.assertAlmostEqual(preds[2], 2.0, delta=0.1)
        self.assertAlmostEqual(preds[3], 3.0, delta=0.1)
        self.assertAlmostEqual(preds[4], routed.fallback.predict_frame(week.iloc[[4]])[0].predicted_points_1gw)  # unknown position -> pooled
        self.assertEqual(len(routed.predict_frame(week)), 5)
        with mock.patch.dict(os.environ, {"FPL_PER_POSITION": "0"}):
            pooled = fit_model_suite_from_frame(train_frame=frame, feature_names=["feat"])
        self.assertNotIsInstance(pooled, PositionRoutedSuite)


if __name__ == "__main__":
    unittest.main()

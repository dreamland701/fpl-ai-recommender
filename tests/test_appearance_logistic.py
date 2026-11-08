import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

from fpl_ai.models import LogisticAppearance, fit_model_suite_from_frame


def _frame(n=400, seed=0):
    rng = np.random.default_rng(seed)
    minutes = rng.choice([0.0, 30.0, 90.0], size=n, p=[0.3, 0.2, 0.5])
    frame = pd.DataFrame({
        "minutes_avg_3": minutes + rng.normal(0, 5, n),
        "status_flag_pre_deadline": (minutes == 0).astype(float) * (rng.random(n) < 0.7),
        "price_pre_deadline": rng.uniform(4, 12, n),
        "fixture_count": np.where(rng.random(n) < 0.05, 0.0, 1.0),
    })
    frame["label_minutes_1gw"] = np.where(frame["fixture_count"] > 0, minutes, 0.0)
    frame["label_appearance_probability"] = (frame["label_minutes_1gw"] > 0).astype(float)
    frame["label_points_1gw"] = frame["label_minutes_1gw"] / 30.0
    frame["label_points_3gw"] = frame["label_points_1gw"] * 3
    frame["label_points_5gw"] = frame["label_points_1gw"] * 5
    return frame


class LogisticAppearanceTestCase(unittest.TestCase):
    features = ["minutes_avg_3", "status_flag_pre_deadline", "price_pre_deadline"]

    def test_fit_predict_and_roundtrip(self):
        frame = _frame()
        model = LogisticAppearance(feature_names=self.features).fit(frame)
        p = model.predict(frame)
        self.assertTrue(((p >= 0) & (p <= 1)).all())
        played = frame["label_appearance_probability"].to_numpy() > 0
        self.assertGreater(p[played].mean(), p[~played].mean() + 0.3)   # separates the classes
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "appearance.json"
            model.save(path)
            again = LogisticAppearance.load(path)
        np.testing.assert_allclose(again.predict(frame), p)

    def test_suite_uses_the_classifier_only_when_flagged(self):
        frame = _frame()
        with mock.patch.dict(os.environ, {"FPL_APPEARANCE_LOGISTIC": "1", "FPL_PER_FIXTURE": "1"}):
            suite = fit_model_suite_from_frame(train_frame=frame, feature_names=self.features)
        self.assertIsNotNone(suite.appearance_model)
        week = frame.head(50).copy()
        week["player_id"] = range(50); week["player_name"] = "p"; week["team_id"] = 1; week["position"] = "MID"
        week["season"] = "2025-26"; week["week"] = 9; week["price"] = week["price_pre_deadline"]
        forecasts = suite.predict_frame(week)
        probs = np.array([f.appearance_probability for f in forecasts])
        expected = np.where(week["fixture_count"].to_numpy() > 0, suite.appearance_model.predict(week), 0.0)
        np.testing.assert_allclose(probs, expected, atol=1e-9)
        with mock.patch.dict(os.environ, {"FPL_APPEARANCE_LOGISTIC": "0"}):
            plain = fit_model_suite_from_frame(train_frame=frame, feature_names=self.features)
        self.assertIsNone(plain.appearance_model)


if __name__ == "__main__":
    unittest.main()

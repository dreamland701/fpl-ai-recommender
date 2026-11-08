import tempfile
import unittest
from pathlib import Path

import pandas as pd

from fpl_ai.dataset import CanonicalDataset, build_training_frame
from fpl_ai.models import RidgeRegressor, load_model_suite, train_model_suite

from tests.test_dataset import synthetic_raw_history


class ModelsTestCase(unittest.TestCase):
    def test_train_and_predict_model_suite(self):
        dataset = CanonicalDataset(build_training_frame(synthetic_raw_history()))
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest = train_model_suite(dataset, Path(tmpdir))
            self.assertTrue(Path(manifest.availability_path).exists())

            model_suite = load_model_suite(Path(tmpdir))
            forecasts = model_suite.predict_week(dataset, ("2025-26", 4))

        self.assertEqual(len(forecasts), 2)
        self.assertGreaterEqual(forecasts[0].predicted_points_1gw, 0.0)
        self.assertGreaterEqual(forecasts[0].predicted_minutes, 0.0)


class RidgeRegressorInputClippingTestCase(unittest.TestCase):
    def test_predict_clips_out_of_training_range_input_before_scoring(self):
        # Regression test (found 2026-08-12): a live player priced above
        # any price ever seen in training (Haaland, GW1 2026-27) produced
        # a wildly negative raw 3GW prediction that clipped to a
        # nonsensical 0.0 for an obvious nailed starter. Fix: clamp inputs
        # to the training-observed [min, max] range before scoring, so a
        # linear model can't extrapolate arbitrarily past its domain.
        train = pd.DataFrame(
            {"price": [5.0, 6.0, 7.0, 8.0, 9.0, 10.0], "target": [2.0, 3.0, 4.0, 5.0, 6.0, 7.0]}
        )
        model = RidgeRegressor(feature_names=["price"], alpha=1.0).fit(train, "target")

        far_out_of_range = pd.DataFrame({"price": [50.0]})
        at_max = pd.DataFrame({"price": [10.0]})

        clipped_prediction = model.predict(far_out_of_range)[0]
        max_prediction = model.predict(at_max)[0]

        # Clamped input means an absurdly out-of-range price predicts
        # exactly the same as the training-max price, not something wild.
        self.assertAlmostEqual(clipped_prediction, max_prediction, places=6)

    def test_from_json_dict_without_mins_maxs_still_predicts(self):
        # Backward compatibility: a model saved before this fix has no
        # feature_mins/feature_maxs in its JSON; loading it must not crash,
        # and predict() should just skip clipping (empty mins/maxs).
        payload = {
            "feature_names": ["price"],
            "alpha": 1.0,
            "intercept": 1.0,
            "coefficients": [0.5],
            "feature_means": [7.0],
            "feature_scales": [1.5],
            "rmse": 0.1,
        }
        model = RidgeRegressor.from_json_dict(payload)
        prediction = model.predict(pd.DataFrame({"price": [50.0]}))[0]
        self.assertFalse(pd.isna(prediction))


if __name__ == "__main__":
    unittest.main()


class PerFixtureForecastTestCase(unittest.TestCase):
    """Double gameweeks (2026-10-13, memory fpl-dgw-pricing-defect): with FPL_PER_FIXTURE=1 the
    minutes and 1GW heads work per fixture and scale by the week's fixture count, and P(appear)
    is the chance of playing at least once (not minutes over 90 x fixtures)."""

    def _suite(self, per_fixture: bool):
        from fpl_ai.models import ForecastModelSuite

        # constant heads: 80 minutes and 4 points per (fixture or week), no feature dependence
        def head(value: float) -> RidgeRegressor:
            return RidgeRegressor(feature_names=["price"], alpha=1.0, intercept_=value, coefficients_=[0.0],
                                  feature_means_=[5.0], feature_scales_=[1.0], feature_mins_=[0.0], feature_maxs_=[20.0])

        return ForecastModelSuite(feature_names=["price"], availability_model=head(80.0), points_1gw_model=head(4.0),
                                  points_3gw_model=head(12.0), points_5gw_model=head(20.0), per_fixture=per_fixture)

    def _frame(self) -> pd.DataFrame:
        return pd.DataFrame({"season": ["2025-26"] * 3, "week": [30] * 3, "player_id": [1, 2, 3],
                             "player_name": ["single", "double", "blank"], "team_id": [1, 2, 3], "position": ["MID"] * 3,
                             "price": [7.0, 7.0, 7.0], "fixture_count": [1, 2, 0]})

    def test_per_fixture_scales_minutes_points_and_fixes_appearance(self):
        single, double, blank = self._suite(True).predict_frame(self._frame())
        self.assertAlmostEqual(single.predicted_points_1gw, 4.0)
        self.assertAlmostEqual(double.predicted_points_1gw, 8.0)
        self.assertAlmostEqual(blank.predicted_points_1gw, 0.0)
        self.assertAlmostEqual(single.predicted_minutes, 80.0)
        self.assertAlmostEqual(double.predicted_minutes, 160.0)
        self.assertAlmostEqual(single.appearance_probability, 80 / 90)
        self.assertAlmostEqual(double.appearance_probability, 80 / 90)  # not 80/180
        self.assertAlmostEqual(blank.appearance_probability, 0.0)
        self.assertAlmostEqual(double.predicted_points_3gw, 12.0)  # multi-week heads untouched

    def test_horizon_heads_scale_by_fixtures_ahead(self):
        suite = self._suite(True)
        suite.per_fixture_horizon = True
        frame = self._frame()
        frame["fixtures_next_3"] = [3.0, 4.0, 2.0]
        frame["fixtures_next_5"] = [5.0, 6.0, 4.0]
        single, double, blank = suite.predict_frame(frame)
        self.assertAlmostEqual(single.predicted_points_3gw, 36.0)  # 12 per fixture x 3
        self.assertAlmostEqual(double.predicted_points_3gw, 48.0)
        self.assertAlmostEqual(blank.predicted_points_5gw, 80.0)
        # without the columns the heads assume single fixtures every week
        single, _, _ = suite.predict_frame(self._frame())
        self.assertAlmostEqual(single.predicted_points_5gw, 100.0)

    def test_legacy_formula_halves_a_doubler(self):
        import os
        os.environ.pop("FPL_DGW_PAPP", None)
        single, double, _ = self._suite(False).predict_frame(self._frame())
        self.assertAlmostEqual(double.predicted_points_1gw, 4.0)
        self.assertAlmostEqual(double.appearance_probability, 80 / 180)
        self.assertAlmostEqual(single.appearance_probability, 80 / 90)

    def test_fit_per_fixture_divides_labels(self):
        import os
        from fpl_ai.models import fit_model_suite_from_frame

        frame = pd.DataFrame({"price": [5.0, 5.0, 5.0, 5.0], "fixture_count": [1, 2, 1, 2],
                              "label_minutes_1gw": [90.0, 180.0, 90.0, 180.0], "label_points_1gw": [3.0, 6.0, 3.0, 6.0],
                              "label_points_3gw": [9.0, 12.0, 9.0, 12.0], "label_points_5gw": [15.0] * 4,
                              "fixtures_next_3": [3.0, 4.0, 3.0, 4.0], "fixtures_next_5": [5.0] * 4})
        os.environ["FPL_PER_FIXTURE"] = "1"
        try:
            suite = fit_model_suite_from_frame(frame, ["price"])
        finally:
            os.environ.pop("FPL_PER_FIXTURE", None)
        self.assertTrue(suite.per_fixture)
        self.assertTrue(suite.per_fixture_horizon)
        self.assertAlmostEqual(suite.points_1gw_model.intercept_, 3.0, places=5)
        self.assertAlmostEqual(suite.availability_model.intercept_, 90.0, places=5)
        self.assertAlmostEqual(suite.points_3gw_model.intercept_, 3.0, places=5)  # 9/3 and 12/4

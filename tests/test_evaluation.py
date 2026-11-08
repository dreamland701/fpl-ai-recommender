import unittest

from fpl_ai.dataset import CanonicalDataset, build_training_frame
from fpl_ai.evaluation import evaluate_time_split

from tests.test_dataset import synthetic_raw_history


class EvaluationTestCase(unittest.TestCase):
    def test_evaluate_time_split_uses_past_for_train_and_future_for_test(self):
        dataset = CanonicalDataset(build_training_frame(synthetic_raw_history()))
        report = evaluate_time_split(
            dataset,
            test_season="2025-26",
            test_week_min=4,
            test_week_max=4,
        )
        self.assertEqual(report.test_season, "2025-26")
        self.assertEqual(report.test_weeks, [4])
        self.assertGreater(report.train_rows, 0)
        self.assertGreater(report.test_rows, 0)
        metrics = {summary.metric for summary in report.summaries}
        self.assertEqual(metrics, {"points_1gw_rmse", "minutes_rmse"})


if __name__ == "__main__":
    unittest.main()

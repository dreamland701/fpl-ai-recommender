import json
import tempfile
import unittest
from pathlib import Path

from dataclasses import replace

from fpl_ai.llm_adjust import apply_deltas_to_forecast, apply_llm_deltas, load_llm_delta_lookup, parse_delta_response
from fpl_ai.types import PlayerForecast


def _forecast(player_id: int, week: int = 12) -> PlayerForecast:
    return PlayerForecast(
        season="2025-26",
        week=week,
        player_id=player_id,
        player_name=f"Player {player_id}",
        team_id=1,
        position="MID",
        price=8.0,
        predicted_minutes=80.0,
        predicted_points_1gw=5.0,
        predicted_points_3gw=14.0,
        predicted_points_5gw=22.0,
        appearance_probability=0.9,
        fixture_count=1,
        uncertainty=1.0,
    )


class ParseDeltaResponseTests(unittest.TestCase):
    def test_strict_json_is_parsed_and_clipped(self):
        response = json.dumps(
            {
                "delta_points_1gw": -9.0,
                "delta_points_3gw": 1.2,
                "delta_points_5gw": 2.0,
                "delta_minutes_1gw": 45,
                "delta_appearance_probability": -0.5,
            }
        )
        deltas = parse_delta_response(response)
        self.assertEqual(deltas["delta_points_1gw"], -2.0)
        self.assertEqual(deltas["delta_points_3gw"], 1.2)
        self.assertEqual(deltas["delta_minutes_1gw"], 20.0)
        self.assertEqual(deltas["delta_appearance_probability"], -0.25)

    def test_json_embedded_in_prose_is_extracted(self):
        deltas = parse_delta_response('Sure! {"delta_points_1gw": 0.5} hope that helps')
        self.assertEqual(deltas, {"delta_points_1gw": 0.5})

    def test_garbage_returns_none(self):
        self.assertIsNone(parse_delta_response("no json here"))
        self.assertIsNone(parse_delta_response('{"unrelated": 1}'))

    def test_non_finite_and_boolean_values_are_dropped_not_clipped(self):
        deltas = parse_delta_response(
            '{"delta_points_1gw": NaN, "delta_points_3gw": Infinity, "delta_points_5gw": "nan", '
            '"delta_minutes_1gw": true, "delta_appearance_probability": -0.1}'
        )
        self.assertEqual(deltas, {"delta_appearance_probability": -0.1})
        self.assertIsNone(parse_delta_response('{"delta_points_1gw": NaN}'))


class LookupAndApplyTests(unittest.TestCase):
    def test_lookup_built_by_row_order_and_applied_with_bounds(self):
        with tempfile.TemporaryDirectory() as tmp:
            examples = Path(tmp) / "eval.jsonl"
            predictions = Path(tmp) / "preds.jsonl"
            examples.write_text(
                json.dumps({"season": "2025-26", "week": 12, "metadata": {"player_id": 7}})
                + "\n"
                + json.dumps({"season": "2025-26", "week": 12, "metadata": {"player_id": 8}})
                + "\n"
            )
            predictions.write_text(
                json.dumps({"season": "2025-26", "week": 12, "response": '{"delta_points_1gw": 1.5, "delta_appearance_probability": 0.2}'})
                + "\n"
                + json.dumps({"season": "2025-26", "week": 12, "response": "unparseable"})
                + "\n"
            )
            lookup = load_llm_delta_lookup(examples, predictions)

        self.assertIn(("2025-26", 12, 7), lookup)
        self.assertNotIn(("2025-26", 12, 8), lookup)

        adjusted = apply_llm_deltas([_forecast(7), _forecast(8)], lookup, week=12)
        self.assertAlmostEqual(adjusted[0].predicted_points_1gw, 6.5)
        self.assertAlmostEqual(adjusted[0].appearance_probability, 1.0)  # 0.9 + 0.2 capped
        self.assertAlmostEqual(adjusted[0].predicted_points_3gw, 14.0)  # absent key: unchanged
        self.assertEqual(adjusted[1], _forecast(8))  # no prediction: untouched

    def test_availability_mode_leaves_points_untouched(self):
        lookup = {(12, 7): {"delta_points_1gw": 1.5, "delta_minutes_1gw": -10.0, "delta_appearance_probability": -0.2}}
        adjusted = apply_llm_deltas([_forecast(7)], lookup, week=12, fields="availability")
        self.assertEqual(adjusted[0].predicted_points_1gw, 5.0)
        self.assertEqual(adjusted[0].predicted_points_5gw, 22.0)
        self.assertAlmostEqual(adjusted[0].predicted_minutes, 70.0)
        self.assertAlmostEqual(adjusted[0].appearance_probability, 0.7)

    def test_wrong_week_is_not_applied(self):
        lookup = {(12, 7): {"delta_points_1gw": 1.0}}
        adjusted = apply_llm_deltas([_forecast(7, week=13)], lookup, week=13)
        self.assertEqual(adjusted[0].predicted_points_1gw, 5.0)

    def test_delta_is_not_applied_to_another_season(self):
        lookup = {("2025-26", 12, 7): {"delta_points_1gw": 1.0}}
        next_season = replace(_forecast(7), season="2026-27")
        self.assertEqual(apply_llm_deltas([next_season], lookup, week=12)[0], next_season)
        self.assertAlmostEqual(apply_llm_deltas([_forecast(7)], lookup, week=12)[0].predicted_points_1gw, 6.0)

    def test_shared_apply_clips_and_ignores_non_finite_inputs(self):
        adjusted = apply_deltas_to_forecast(
            _forecast(7), {"delta_points_1gw": 9.0, "delta_points_3gw": float("nan"), "delta_minutes_1gw": -500}
        )
        self.assertAlmostEqual(adjusted.predicted_points_1gw, 7.0)
        self.assertAlmostEqual(adjusted.predicted_points_3gw, 14.0)
        self.assertAlmostEqual(adjusted.predicted_minutes, 60.0)

    def test_identified_predictions_join_on_identity_not_row_order(self):
        rows = [("2025-26", 12, 7, 1.5), ("2025-26", 12, 8, -1.0)]
        with tempfile.TemporaryDirectory() as tmp:
            examples = Path(tmp) / "eval.jsonl"
            predictions = Path(tmp) / "preds.jsonl"
            examples.write_text("".join(
                json.dumps({"season": s, "week": w, "metadata": {"player_id": pid}}) + "\n" for s, w, pid, _ in rows
            ))
            predictions.write_text("".join(
                json.dumps({"season": s, "week": w, "metadata": {"player_id": pid},
                            "response": json.dumps({"delta_points_1gw": d})}) + "\n"
                for s, w, pid, d in reversed(rows)
            ))
            lookup = load_llm_delta_lookup(examples, predictions)
            self.assertEqual(lookup[("2025-26", 12, 7)], {"delta_points_1gw": 1.5})
            self.assertEqual(lookup[("2025-26", 12, 8)], {"delta_points_1gw": -1.0})

            predictions.write_text("".join(
                json.dumps({"season": s, "week": w, "metadata": {"player_id": pid + 100},
                            "response": json.dumps({"delta_points_1gw": d})}) + "\n"
                for s, w, pid, d in rows
            ))
            with self.assertRaises(ValueError):
                load_llm_delta_lookup(examples, predictions)

    def test_row_count_mismatch_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            examples = Path(tmp) / "eval.jsonl"
            predictions = Path(tmp) / "preds.jsonl"
            examples.write_text(json.dumps({"season": "2025-26", "week": 12, "metadata": {"player_id": 7}}) + "\n")
            predictions.write_text("")
            with self.assertRaises(ValueError):
                load_llm_delta_lookup(examples, predictions)


if __name__ == "__main__":
    unittest.main()

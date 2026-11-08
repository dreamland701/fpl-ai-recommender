import json
import tempfile
import unittest
from pathlib import Path

from fpl_ai.llm_eval import evaluate_llm_predictions


class LLMEvalTestCase(unittest.TestCase):
    def test_evaluate_llm_predictions_scores_matching_bundle(self):
        squad_names = [
            "GK One",
            "GK Two",
            "DEF One",
            "DEF Two",
            "DEF Three",
            "DEF Four",
            "DEF Five",
            "MID One",
            "MID Two",
            "MID Three",
            "MID Four",
            "MID Five",
            "FWD One",
            "FWD Two",
            "FWD Three",
        ]
        positions = {
            "GK One": "GK",
            "GK Two": "GK",
            "DEF One": "DEF",
            "DEF Two": "DEF",
            "DEF Three": "DEF",
            "DEF Four": "DEF",
            "DEF Five": "DEF",
            "MID One": "MID",
            "MID Two": "MID",
            "MID Three": "MID",
            "MID Four": "MID",
            "MID Five": "MID",
            "FWD One": "FWD",
            "FWD Two": "FWD",
            "FWD Three": "FWD",
        }
        actual_points = {name: 2.0 for name in squad_names}
        actual_points["MID One"] = 10.0
        actual_points["FWD One"] = 6.0
        actual_minutes = {name: 90.0 for name in squad_names}
        assistant_payload = {
            "transfers": [],
            "captain": "MID One",
            "vice_captain": "FWD One",
            "starters": [
                "GK One",
                "DEF One",
                "DEF Two",
                "DEF Three",
                "MID One",
                "MID Two",
                "MID Three",
                "MID Four",
                "FWD One",
                "FWD Two",
                "FWD Three",
            ],
            "bench_order": ["GK Two", "DEF Four", "MID Five", "DEF Five"],
            "chip": "none",
            "reasoning_summary": ["Hold transfer and captain the best projected midfielder."],
        }
        team_actual_score = sum(actual_points[name] for name in assistant_payload["starters"]) + actual_points["MID One"]

        example = {
            "season": "2025-26",
            "week": 11,
            "deadline_ts": "2025-11-08T12:30:00Z",
            "messages": [
                {"role": "system", "content": "Return strict JSON."},
                {"role": "user", "content": "Example prompt."},
                {"role": "assistant", "content": json.dumps(assistant_payload)},
            ],
            "metadata": {
                "season": "2025-26",
                "week": 11,
                "bank_before": 0.5,
                "bank_after": 0.5,
                "free_transfers_before": 1,
                "free_transfers_after": 2,
                "team_predicted_score": 62.0,
                "team_actual_score": team_actual_score,
                "league_average_score": 48.0,
                "chip_used": "none",
                "chip_reason": "",
                "effective_captain_name": "MID One",
                "evidence_count": 0,
                "evidence_urls": [],
                "player_actual_points": actual_points,
                "player_actual_minutes": actual_minutes,
                "player_positions": positions,
                "current_squad_names": squad_names,
                "post_move_squad_names": squad_names,
                "candidate_transfers": [],
            },
        }
        prediction = {
            "season": "2025-26",
            "week": 11,
            "response": json.dumps(assistant_payload),
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            examples_path = Path(tmpdir) / "eval.jsonl"
            predictions_path = Path(tmpdir) / "predictions.jsonl"
            examples_path.write_text(json.dumps(example) + "\n")
            predictions_path.write_text(json.dumps(prediction) + "\n")
            report = evaluate_llm_predictions(str(examples_path), str(predictions_path))

        self.assertEqual(report.total_examples, 1)
        self.assertEqual(report.matched_predictions, 1)
        self.assertEqual(report.valid_json_predictions, 1)
        self.assertEqual(report.captain_accuracy, 1.0)
        self.assertEqual(report.transfer_exact_match_rate, 1.0)
        self.assertEqual(report.average_predicted_policy_actual_score, round(team_actual_score, 4))
        self.assertEqual(report.average_score_gap_vs_target, 0.0)


if __name__ == "__main__":
    unittest.main()

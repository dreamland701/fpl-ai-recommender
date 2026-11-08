import json
import unittest

from fpl_ai import avail_rl, reghead

PROMPT = ("<|turn>system\nYou are an FPL player forecaster. Blah.<|turn>\n<|turn>user\nForecast this player. Express deltas.\n\n"
          "Delta bounds: x\n\nExample:\n{\"delta_points_1gw\": 0}\n\nPlayer context:\n- Player: A\n\nClassic ML signal:\n{}\n\n"
          "Timestamp-safe text evidence:\n[1] src | 2025-01-01T00:00:00Z\nTitle: t\nText: body\n<|turn>\n<|turn>model\n")


class RegHeadTestCase(unittest.TestCase):
    def test_compact_prompt_keeps_context_and_drops_instructions(self):
        c = reghead.compact_prompt(PROMPT)
        self.assertIn("Player context:", c); self.assertIn("Text: body", c); self.assertTrue(c.endswith("<|turn>model\n"))
        self.assertNotIn("Delta bounds", c); self.assertNotIn("Example:", c); self.assertTrue(c.startswith(reghead.SYSTEM))

    def test_standardiser_roundtrip_and_delta_bounds(self):
        rows = [{"delta_points_1gw": v, "delta_points_3gw": 2 * v, "delta_points_5gw": 3 * v, "delta_minutes_1gw": 10 * v} for v in (-1.0, 0.0, 1.0, 2.0)]
        std = reghead.Standardiser.fit(rows)
        z = std.encode(rows[3]); back = std.decode(z)
        for k, _ in reghead.REG_FIELDS:
            self.assertAlmostEqual(back[k], rows[3][k], places=6)
        d = reghead.deltas_from_output([50.0, 50.0, 50.0, 50.0, 8.0], 0.5, std)
        self.assertEqual(d["delta_points_1gw"], 2.0); self.assertEqual(d["delta_minutes_1gw"], 20.0)
        self.assertEqual(d["delta_appearance_probability"], 0.25)
        d = reghead.deltas_from_output([0.0] * 5, 0.8, std)
        self.assertAlmostEqual(d["delta_appearance_probability"], 0.0, places=3)

    def test_targets_from_metadata(self):
        meta = {"residual_labels_clipped": {"delta_points_1gw": 1.0, "delta_points_3gw": 0.5, "delta_points_5gw": -1.0, "delta_minutes_1gw": 3.0,
                                            "delta_appearance_probability": 0.1},
                "labels": {"appearance_probability": 1.0}, "baseline_forecast": {"baseline_appearance_probability": 0.7}}
        t = reghead.targets_from_metadata(meta)
        self.assertEqual(t["appearance"], 1.0); self.assertEqual(t["baseline_appearance"], 0.7); self.assertEqual(t["delta_points_5gw"], -1.0)


class AvailRLTestCase(unittest.TestCase):
    def test_prompt_and_reward(self):
        p = avail_rl.availability_prompt(PROMPT, 0.834)
        self.assertIn("probability is 0.83", p); self.assertTrue(p.endswith("<|turn>\n<|turn>model\n")); self.assertNotIn("Delta bounds", p)
        self.assertEqual(p.count("<|turn>model"), 1)
        self.assertAlmostEqual(avail_rl.brier_reward('{"reasoning": "fit", "p_play": 0.9}', 1.0, 0.6)["reward"], 0.16 - 0.01, places=6)
        self.assertEqual(avail_rl.brier_reward("no json here", 1.0, 0.6)["reward"], avail_rl.UNPARSEABLE)
        self.assertEqual(avail_rl.parse_p_play('text {"p_play": 1.5}'), None)
        self.assertEqual(avail_rl.parse_p_play('reasoning... "p_play": 0.25 }'), 0.25)

    def test_text_could_matter(self):
        self.assertFalse(avail_rl.text_could_matter({"status_pre_deadline": "a", "news_pre_deadline": "", "evidence_present": False}))
        self.assertTrue(avail_rl.text_could_matter({"status_pre_deadline": "d", "news_pre_deadline": "Knock - 75%", "evidence_present": False}))
        self.assertTrue(avail_rl.text_could_matter({"status_pre_deadline": "", "news_pre_deadline": "", "evidence_present": True}))


if __name__ == "__main__":
    unittest.main()

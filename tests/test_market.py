import math
import os
import unittest
from unittest import mock

import pandas as pd

from fpl_ai import market
from fpl_ai.dataset import build_training_frame, get_feature_columns


def _odds(season="2025-26"):
    return pd.DataFrame([
        # team 1 hosts team 2 on 16 Aug: strong favourite, high total
        {"season": season, "date": "2025-08-16", "home_team_id": 1, "away_team_id": 2,
         "lambda_home": 2.2, "lambda_away": 0.8, "p_home": 0.70, "p_draw": 0.18, "p_away": 0.12},
        # team 2 hosts team 1 on 23 Aug (a double for both in the synthetic week 2)
        {"season": season, "date": "2025-08-23", "home_team_id": 2, "away_team_id": 1,
         "lambda_home": 1.0, "lambda_away": 1.6, "p_home": 0.25, "p_draw": 0.25, "p_away": 0.50},
    ])


def _raw_row(week, player_id, team_id, opponent_id, kickoff, was_home, minutes=90, points=4, xgi=0.5):
    return {"season": "2025-26", "week": week, "player_id": player_id, "player_name": f"P{player_id}", "team_id": team_id,
            "position": "MID", "price": 7.0, "selected_by_percent": 10.0, "transfers_in_event": 10, "transfers_out_event": 5,
            "status": "a", "news": "", "opponent_team_id": opponent_id, "was_home": was_home, "kickoff_time": kickoff,
            "fixture_difficulty": 3, "minutes": minutes, "total_points": points, "team_h_score": 1, "team_a_score": 1,
            "bonus": 0, "bps": 10, "influence": 10.0, "creativity": 10.0, "threat": 10.0, "ict_index": 3.0, "starts": 1,
            "expected_goals": xgi / 2, "expected_assists": xgi / 2, "expected_goal_involvements": xgi,
            "expected_goals_conceded": 1.0, "defensive_contribution": 0.0}


class MarketTestCase(unittest.TestCase):
    def test_devig_normalises_and_rejects_bad_prices(self):
        probs = market.devig([2.0, 4.0, 4.0])
        self.assertAlmostEqual(sum(probs), 1.0)
        self.assertAlmostEqual(probs[0], 0.5)
        self.assertIsNone(market.devig([1.0, 3.0, 3.0]))
        self.assertIsNone(market.devig([float("nan"), 3.0, 3.0]))

    def test_fit_poisson_recovers_known_lambdas(self):
        home, draw, away, over = market.outcome_probs(1.8, 1.1)
        lam_h, lam_a = market.fit_poisson(home, draw, away, over)
        self.assertAlmostEqual(lam_h, 1.8, places=2)
        self.assertAlmostEqual(lam_a, 1.1, places=2)
        # without the over/under line the 1X2 probabilities still pin the pair down
        lam_h2, lam_a2 = market.fit_poisson(home, draw, away, None)
        self.assertAlmostEqual(lam_h2, 1.8, places=1)

    def test_attach_matches_by_london_date_and_falls_back(self):
        raw = pd.DataFrame([
            _raw_row(1, 1, 1, 2, "2025-08-16T19:00:00Z", True),   # 20:00 London, same date
            _raw_row(1, 2, 2, 1, "2025-08-16T19:00:00Z", False),
            _raw_row(2, 1, 1, 3, "2025-08-23T14:00:00Z", True),   # no odds row for team 3
        ])
        out = market.attach_fixture_market(raw, _odds())
        self.assertEqual(out.loc[0, "mkt_available"], 1.0)
        self.assertAlmostEqual(out.loc[0, "mkt_team_xg"], 2.2)
        self.assertAlmostEqual(out.loc[0, "mkt_opp_xg"], 0.8)
        self.assertAlmostEqual(out.loc[0, "mkt_cs_prob"], math.exp(-0.8))
        self.assertAlmostEqual(out.loc[0, "mkt_win_prob"], 0.70)
        self.assertAlmostEqual(out.loc[1, "mkt_team_xg"], 0.8)
        self.assertAlmostEqual(out.loc[1, "mkt_win_prob"], 0.12)
        self.assertEqual(out.loc[2, "mkt_available"], 0.0)
        self.assertAlmostEqual(out.loc[2, "mkt_team_xg"], market.LEAGUE_LAMBDA)

    def test_training_frame_sums_a_double_and_zeroes_a_blank(self):
        raw = pd.DataFrame([
            _raw_row(1, 1, 1, 2, "2025-08-16T14:00:00Z", True),
            _raw_row(1, 2, 2, 1, "2025-08-16T14:00:00Z", False),
            _raw_row(2, 1, 1, 2, "2025-08-23T14:00:00Z", False),
            _raw_row(2, 1, 1, 2, "2025-08-16T14:00:00Z", True),   # second fixture in week 2 (synthetic double)
            _raw_row(2, 2, 2, 1, "2025-08-23T14:00:00Z", True),
            _raw_row(4, 1, 1, 2, "2025-09-13T14:00:00Z", True),   # week 3 is a blank for player 1
            _raw_row(4, 2, 2, 1, "2025-09-13T14:00:00Z", False),
        ])
        with mock.patch.dict(os.environ, {"FPL_MARKET_FEATS": "1"}), \
                mock.patch.object(market, "load_match_odds", return_value=_odds()):
            frame = build_training_frame(raw)
        p1 = frame[frame["player_id"] == 1].set_index("week")
        self.assertAlmostEqual(p1.loc[1, "mkt_team_xg"], 2.2)
        self.assertAlmostEqual(p1.loc[2, "mkt_team_xg"], 2.2 + 1.6)       # both fixtures add
        self.assertAlmostEqual(p1.loc[2, "mkt_cs_prob"], math.exp(-0.8) + math.exp(-1.0))
        self.assertEqual(p1.loc[3, "mkt_team_xg"], 0.0)                   # blank week
        self.assertEqual(p1.loc[3, "mkt_available"], 0.0)
        self.assertAlmostEqual(p1.loc[2, "mkt_xg_x_minutes_3"], (2.2 + 1.6) * p1.loc[2, "minutes_avg_3"] / 90.0)
        self.assertAlmostEqual(p1.loc[2, "mkt_xg_x_xgi_5"], (2.2 + 1.6) * p1.loc[2, "expected_goal_involvements_avg_5"])
        for column in market.FEATURES:
            self.assertIn(column, get_feature_columns(frame))

    def test_flag_off_leaves_the_table_unchanged(self):
        raw = pd.DataFrame([_raw_row(1, 1, 1, 2, "2025-08-16T14:00:00Z", True)])
        with mock.patch.dict(os.environ, {"FPL_MARKET_FEATS": "0"}):
            frame = build_training_frame(raw)
        for column in market.FEATURES:
            self.assertNotIn(column, frame.columns)

    def test_team_week_market_uses_upcoming_then_history_fallback(self):
        fixtures = pd.DataFrame([
            {"team_h": 1, "team_a": 2, "kickoff_time": "2025-08-16T14:00:00Z"},   # priced
            {"team_h": 3, "team_a": 1, "kickoff_time": "2025-08-16T14:00:00Z"},   # not priced: team 1 doubles
        ])
        history = _odds()
        out = market.team_week_market("2025-26", fixtures, upcoming=_odds().iloc[:1], history=history)
        self.assertEqual(out[1]["mkt_available"], 1.0)
        self.assertEqual(out[2]["mkt_available"], 1.0)
        self.assertEqual(out[3]["mkt_available"], 0.0)
        # team 1's week = priced home match (2.2) + fallback for the unpriced one
        self.assertGreater(out[1]["mkt_team_xg"], 2.2)
        self.assertAlmostEqual(out[2]["mkt_team_xg"], 0.8)
        # team 3 has no history: league average on both sides
        self.assertAlmostEqual(out[3]["mkt_opp_xg"], (sum([2.2, 1.6]) / 2 + market.LEAGUE_LAMBDA) / 2, places=6)


if __name__ == "__main__":
    unittest.main()

import tempfile
import unittest
from pathlib import Path

import pandas as pd

from fpl_ai.dataset import CanonicalDataset, build_training_frame, get_week_eligibility, normalize_vaastav_history


def synthetic_raw_history():
    return pd.DataFrame(
        [
            {
                "season": "2025-26",
                "week": 1,
                "player_id": 1,
                "player_name": "Mid One",
                "team_id": 1,
                "position": "MID",
                "price": 8.0,
                "selected_by_percent": 20.0,
                "transfers_in_event": 1000,
                "transfers_out_event": 400,
                "status": "a",
                "news": "",
                "opponent_team_id": 2,
                "was_home": True,
                "kickoff_time": "2025-08-16T11:30:00Z",
                "fixture_difficulty": 3,
                "minutes": 90,
                "total_points": 5,
                "team_h_score": 2,
                "team_a_score": 1,
                "bonus": 1,
                "bps": 20,
                "influence": 30.0,
                "creativity": 22.0,
                "threat": 55.0,
                "ict_index": 10.7,
                "starts": 1,
                "expected_goals": 0.4,
                "expected_assists": 0.2,
                "expected_goal_involvements": 0.6,
                "expected_goals_conceded": 1.1,
                "defensive_contribution": 0.0,
            },
            {
                "season": "2025-26",
                "week": 1,
                "player_id": 2,
                "player_name": "Fwd Two",
                "team_id": 2,
                "position": "FWD",
                "price": 7.5,
                "selected_by_percent": 18.0,
                "transfers_in_event": 900,
                "transfers_out_event": 300,
                "status": "a",
                "news": "",
                "opponent_team_id": 1,
                "was_home": False,
                "kickoff_time": "2025-08-16T11:30:00Z",
                "fixture_difficulty": 3,
                "minutes": 90,
                "total_points": 6,
                "team_h_score": 2,
                "team_a_score": 1,
                "bonus": 2,
                "bps": 24,
                "influence": 40.0,
                "creativity": 14.0,
                "threat": 60.0,
                "ict_index": 11.4,
                "starts": 1,
                "expected_goals": 0.6,
                "expected_assists": 0.1,
                "expected_goal_involvements": 0.7,
                "expected_goals_conceded": 1.5,
                "defensive_contribution": 0.0,
            },
            {
                "season": "2025-26",
                "week": 2,
                "player_id": 1,
                "player_name": "Mid One",
                "team_id": 1,
                "position": "MID",
                "price": 8.1,
                "selected_by_percent": 21.0,
                "transfers_in_event": 800,
                "transfers_out_event": 500,
                "status": "a",
                "news": "",
                "opponent_team_id": 3,
                "was_home": False,
                "kickoff_time": "2025-08-23T14:00:00Z",
                "fixture_difficulty": 2,
                "minutes": 85,
                "total_points": 8,
                "team_h_score": 0,
                "team_a_score": 2,
                "bonus": 3,
                "bps": 30,
                "influence": 48.0,
                "creativity": 28.0,
                "threat": 72.0,
                "ict_index": 14.8,
                "starts": 1,
                "expected_goals": 0.5,
                "expected_assists": 0.3,
                "expected_goal_involvements": 0.8,
                "expected_goals_conceded": 0.9,
                "defensive_contribution": 0.0,
            },
            {
                "season": "2025-26",
                "week": 2,
                "player_id": 2,
                "player_name": "Fwd Two",
                "team_id": 2,
                "position": "FWD",
                "price": 7.6,
                "selected_by_percent": 19.0,
                "transfers_in_event": 700,
                "transfers_out_event": 350,
                "status": "a",
                "news": "",
                "opponent_team_id": 4,
                "was_home": True,
                "kickoff_time": "2025-08-23T14:00:00Z",
                "fixture_difficulty": 4,
                "minutes": 75,
                "total_points": 4,
                "team_h_score": 1,
                "team_a_score": 1,
                "bonus": 0,
                "bps": 15,
                "influence": 25.0,
                "creativity": 10.0,
                "threat": 33.0,
                "ict_index": 6.8,
                "starts": 1,
                "expected_goals": 0.2,
                "expected_assists": 0.05,
                "expected_goal_involvements": 0.25,
                "expected_goals_conceded": 1.0,
                "defensive_contribution": 0.0,
            },
            {
                "season": "2025-26",
                "week": 3,
                "player_id": 2,
                "player_name": "Fwd Two",
                "team_id": 2,
                "position": "FWD",
                "price": 7.7,
                "selected_by_percent": 19.5,
                "transfers_in_event": 600,
                "transfers_out_event": 280,
                "status": "d",
                "news": "Knock",
                "opponent_team_id": 5,
                "was_home": False,
                "kickoff_time": "2025-08-30T14:00:00Z",
                "fixture_difficulty": 3,
                "minutes": 15,
                "total_points": 1,
                "team_h_score": 2,
                "team_a_score": 0,
                "bonus": 0,
                "bps": 4,
                "influence": 6.0,
                "creativity": 2.0,
                "threat": 5.0,
                "ict_index": 1.3,
                "starts": 0,
                "expected_goals": 0.05,
                "expected_assists": 0.0,
                "expected_goal_involvements": 0.05,
                "expected_goals_conceded": 0.5,
                "defensive_contribution": 0.0,
            },
            {
                "season": "2025-26",
                "week": 4,
                "player_id": 1,
                "player_name": "Mid One",
                "team_id": 1,
                "position": "MID",
                "price": 8.2,
                "selected_by_percent": 22.0,
                "transfers_in_event": 500,
                "transfers_out_event": 450,
                "status": "a",
                "news": "",
                "opponent_team_id": 6,
                "was_home": True,
                "kickoff_time": "2025-09-13T14:00:00Z",
                "fixture_difficulty": 2,
                "minutes": 88,
                "total_points": 7,
                "team_h_score": 3,
                "team_a_score": 0,
                "bonus": 2,
                "bps": 26,
                "influence": 41.0,
                "creativity": 26.0,
                "threat": 61.0,
                "ict_index": 12.9,
                "starts": 1,
                "expected_goals": 0.45,
                "expected_assists": 0.2,
                "expected_goal_involvements": 0.65,
                "expected_goals_conceded": 0.4,
                "defensive_contribution": 0.0,
            },
            {
                "season": "2025-26",
                "week": 4,
                "player_id": 2,
                "player_name": "Fwd Two",
                "team_id": 2,
                "position": "FWD",
                "price": 7.8,
                "selected_by_percent": 20.0,
                "transfers_in_event": 620,
                "transfers_out_event": 220,
                "status": "a",
                "news": "",
                "opponent_team_id": 7,
                "was_home": True,
                "kickoff_time": "2025-09-13T14:00:00Z",
                "fixture_difficulty": 2,
                "minutes": 90,
                "total_points": 9,
                "team_h_score": 2,
                "team_a_score": 0,
                "bonus": 3,
                "bps": 32,
                "influence": 55.0,
                "creativity": 18.0,
                "threat": 78.0,
                "ict_index": 15.1,
                "starts": 1,
                "expected_goals": 0.7,
                "expected_assists": 0.1,
                "expected_goal_involvements": 0.8,
                "expected_goals_conceded": 0.3,
                "defensive_contribution": 0.0,
            },
        ]
    )


class DatasetTestCase(unittest.TestCase):
    def test_week_eligibility_includes_gw31_post_season(self):
        # GW31 had two rearranged fixtures (Arsenal-Wolves into GW26,
        # Man City-Crystal Palace into GW36) and was excluded mid-season
        # while the schedule was still unsettled. Confirmed post-season
        # (2026-08-06) the source data already re-tags each fixture to the
        # round it was actually played in, so no exclusion is needed.
        eligibility = get_week_eligibility("2025-26", 31)
        self.assertTrue(eligibility.eligible_for_training)

    def test_week_eligibility_includes_full_season_through_gw38(self):
        eligibility = get_week_eligibility("2025-26", 38)
        self.assertTrue(eligibility.eligible_for_training)

    def test_training_frame_is_leakage_safe_and_adds_blank_weeks(self):
        training_frame = build_training_frame(synthetic_raw_history())
        mid_one_week2 = training_frame[
            (training_frame["player_id"] == 1) & (training_frame["week"] == 2)
        ].iloc[0]
        mid_one_week3 = training_frame[
            (training_frame["player_id"] == 1) & (training_frame["week"] == 3)
        ].iloc[0]

        self.assertAlmostEqual(mid_one_week2["points_avg_1"], 5.0)
        self.assertAlmostEqual(mid_one_week2["price_pre_deadline"], 8.1)
        self.assertAlmostEqual(mid_one_week2["price_change_1"], 0.1)
        self.assertEqual(mid_one_week2["status_flag_pre_deadline"], 0.0)
        self.assertAlmostEqual(mid_one_week2["expected_goals_avg_3"], 0.4)
        self.assertAlmostEqual(mid_one_week2["bonus_avg_3"], 1.0)
        self.assertEqual(mid_one_week3["blank_gw"], 1.0)
        self.assertEqual(mid_one_week3["label_points_1gw"], 0.0)
        self.assertAlmostEqual(mid_one_week2["label_points_3gw"], 15.0)

    def test_canonical_dataset_exposes_rows_and_labels(self):
        dataset = CanonicalDataset(build_training_frame(synthetic_raw_history()))
        rows = dataset.build_player_rows(("2025-26", 4))
        labels = dataset.build_labels(("2025-26", 4))
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(labels), 2)
        self.assertIn("points_avg_3", rows[0].features)
        self.assertIn("price_pre_deadline", rows[0].features)
        self.assertIn("expected_goals_avg_3", rows[0].features)
        self.assertIn("defensive_data_source_available", rows[0].features)
        self.assertNotIn("observed_points", rows[0].features)
        self.assertNotIn("observed_minutes", rows[0].features)
        self.assertNotIn("goals_for", rows[0].features)
        self.assertNotIn("goals_against", rows[0].features)

    def test_week_state_deadline_is_before_first_kickoff(self):
        dataset = CanonicalDataset(build_training_frame(synthetic_raw_history()))
        week_state = dataset.build_week_state(("2025-26", 1))

        self.assertEqual(week_state.deadline_ts, "2025-08-16T10:00:00+00:00")

    def test_live_week_frame_reuses_historical_features_and_current_week_overrides(self):
        dataset = CanonicalDataset(build_training_frame(synthetic_raw_history()))
        official_week_frame = pd.DataFrame(
            [
                {
                    "season": "2025-26",
                    "week": 32,
                    "player_id": 1,
                    "player_name": "Mid One",
                    "team_id": 1,
                    "position": "MID",
                    "price": 8.4,
                    "selected_by_percent": 25.0,
                    "transfers_in_event": 1200,
                    "transfers_out_event": 200,
                    "status": "a",
                    "news": "",
                    "fixture_count": 2,
                    "fixture_difficulty_mean": 2.5,
                    "home_fixture_count": 1,
                    "away_fixture_count": 1,
                }
            ]
        )
        live_frame = dataset.build_live_week_frame(official_week_frame)
        live_row = live_frame.iloc[0]
        self.assertEqual(live_row["week"], 32)
        self.assertEqual(live_row["double_gw"], 1.0)
        self.assertAlmostEqual(live_row["price_pre_deadline"], 8.4)
        self.assertAlmostEqual(live_row["price_change_1"], 0.2)
        self.assertGreaterEqual(live_row["points_avg_3"], 0.0)


def _fixture_row(week, player_id, kickoff_time, total_points, minutes=90, opponent_team_id=2, was_home=True):
    return {
        "season": "2025-26",
        "week": week,
        "player_id": player_id,
        "player_name": f"Player {player_id}",
        "team_id": 1,
        "position": "MID",
        "price": 8.0,
        "selected_by_percent": 20.0,
        "transfers_in_event": 1000,
        "transfers_out_event": 400,
        "status": "a",
        "news": "",
        "opponent_team_id": opponent_team_id,
        "was_home": was_home,
        "kickoff_time": kickoff_time,
        "fixture_difficulty": 3,
        "minutes": minutes,
        "total_points": total_points,
        "team_h_score": 1,
        "team_a_score": 1,
        "bonus": 0,
        "bps": 10,
        "influence": 10.0,
        "creativity": 10.0,
        "threat": 10.0,
        "ict_index": 3.0,
        "starts": 1 if minutes > 0 else 0,
        "expected_goals": 0.2,
        "expected_assists": 0.1,
        "expected_goal_involvements": 0.3,
        "expected_goals_conceded": 1.0,
        "defensive_contribution": 0.0,
    }


class DoubleGameweekLabelTest(unittest.TestCase):
    """Locks in deadline-window label semantics for double gameweeks.

    Points for a gameweek label must be the sum over every fixture attributed
    to that round (the FPL event), and the deadline must sit before the
    earliest kickoff of the round across all fixtures.
    """

    def _dgw_history(self):
        rows = [
            _fixture_row(1, 1, "2025-08-16T11:30:00Z", 5),
            # GW2 is a double gameweek: two fixtures, second one earlier in
            # insertion order to prove kickoff aggregation uses min not first.
            _fixture_row(2, 1, "2025-08-26T18:45:00Z", 2, minutes=70, opponent_team_id=4, was_home=False),
            _fixture_row(2, 1, "2025-08-23T14:00:00Z", 9, opponent_team_id=3),
            _fixture_row(3, 1, "2025-08-30T14:00:00Z", 4),
        ]
        return pd.DataFrame(rows)

    def test_dgw_labels_sum_all_fixtures_in_round(self):
        frame = build_training_frame(self._dgw_history())
        dgw_row = frame.loc[(frame["week"] == 2) & (frame["player_id"] == 1)].iloc[0]

        self.assertEqual(dgw_row["fixture_count"], 2)
        self.assertEqual(dgw_row["double_gw"], 1.0)
        self.assertEqual(dgw_row["label_points_1gw"], 11.0)
        self.assertEqual(dgw_row["label_minutes_1gw"], 160.0)

    def test_multi_week_labels_include_dgw_sums(self):
        frame = build_training_frame(self._dgw_history())
        gw1_row = frame.loc[(frame["week"] == 1) & (frame["player_id"] == 1)].iloc[0]

        # 3GW label from GW1 = GW1 (5) + DGW2 (2 + 9) + GW3 (4).
        self.assertEqual(gw1_row["label_points_3gw"], 20.0)

    def test_forward_fixture_counts_follow_the_schedule(self):
        # fixtures_next_3 from GW1 = GW1 (1) + DGW2 (2) + GW3 (1) = 4; from GW3 only one row is
        # left, so 1 fixture scales to a 3-week rate of 3.0 (same convention as the labels).
        frame = build_training_frame(self._dgw_history())
        gw1_row = frame.loc[(frame["week"] == 1) & (frame["player_id"] == 1)].iloc[0]
        gw3_row = frame.loc[(frame["week"] == 3) & (frame["player_id"] == 1)].iloc[0]
        self.assertEqual(gw1_row["fixtures_next_3"], 4.0)
        self.assertAlmostEqual(gw1_row["fixtures_next_5"], 4.0 * 5 / 3)
        self.assertEqual(gw3_row["fixtures_next_3"], 3.0)

    def test_dgw_deadline_precedes_earliest_kickoff_in_round(self):
        dataset = CanonicalDataset(build_training_frame(self._dgw_history()))
        week_state = dataset.build_week_state(("2025-26", 2))

        # Earliest GW2 kickoff is 2025-08-23T14:00Z; deadline is 90 min prior.
        self.assertEqual(week_state.deadline_ts, "2025-08-23T12:30:00+00:00")


class SeasonEndLabelNormalizationTestCase(unittest.TestCase):
    def test_tail_rows_get_rate_equivalent_multiweek_labels(self):
        # Regression test (found 2026-08-21): forward-sum labels truncate at
        # season end, teaching "elite features -> tiny 5GW target" on ~13%
        # of rows and attenuating the multi-week ridge heads (elite DEFs
        # deflated ~2x). Labels must be scaled to full-horizon
        # rate-equivalents instead.
        frame = build_training_frame(synthetic_raw_history())
        # synthetic season has 4 weeks; player 1 scores 5, 8, 0 (blank), 7
        week2 = frame[(frame["player_id"] == 1) & (frame["week"] == 2)].iloc[0]
        week4 = frame[(frame["player_id"] == 1) & (frame["week"] == 4)].iloc[0]

        # week 2 has a FULL 3-week window (2,3,4): unchanged raw sum.
        self.assertAlmostEqual(week2["label_points_3gw"], 15.0)  # 8+0+7
        # week 4 is the season's last row: window has 1 of 3 weeks ->
        # scaled x3 to the rate-equivalent, not left as a truncated sum.
        self.assertAlmostEqual(week4["label_points_3gw"], 21.0)  # 7 * 3/1
        # 5GW at week 2 sees only 3 of 5 weeks -> scaled by 5/3.
        self.assertAlmostEqual(week2["label_points_5gw"], 15.0 * 5.0 / 3.0)


class NormalizeVaastavHistoryTestCase(unittest.TestCase):
    def test_team_id_uses_numeric_lookup_not_merged_gw_name_string(self):
        # Regression test (found 2026-08-12): vaastav's merged_gw.csv "team"
        # column is a NAME STRING ("Sunderland"), not a numeric id, on every
        # season checked (2022-23 through 2025-26). Before the fix, this
        # coerced to NaN -> the -1 default for every row in the whole
        # project, silently disabling build_initial_squad's "max 3 per
        # club" constraint (candidate.team_id > 0 was never true) and
        # collapsing team_goals_for_avg_3/5 into one global pool instead of
        # per-team. players_raw.csv DOES carry the correct numeric team id;
        # normalize_vaastav_history must prefer it.
        with tempfile.TemporaryDirectory() as tmp:
            season_dir = Path(tmp) / "2025-26"
            season_dir.mkdir(parents=True)
            pd.DataFrame(
                [
                    {
                        "element": 1,
                        "name": "Test Player",
                        "team": "Sunderland",  # name string, matches real vaastav format
                        "round": 1,
                        "opponent_team": 2,
                        "was_home": True,
                        "kickoff_time": "2025-08-16T11:30:00Z",
                        "minutes": 90,
                        "total_points": 5,
                        "value": 50,
                    }
                ]
            ).to_csv(season_dir / "merged_gw.csv", index=False)
            pd.DataFrame([{"id": 1, "web_name": "Test Player", "team": 17, "element_type": 2}]).to_csv(
                season_dir / "players_raw.csv", index=False
            )
            pd.DataFrame([{"id": 2, "team_h": 17, "team_a": 3, "team_h_difficulty": 3, "team_a_difficulty": 2, "event": 1}]).to_csv(
                season_dir / "fixtures.csv", index=False
            )

            frame = normalize_vaastav_history(tmp)

        row = frame.loc[frame["player_id"] == 1].iloc[0]
        self.assertEqual(row["team_id"], 17)  # from players_raw.csv, not -1

    def test_code_survives_the_full_pipeline_into_training_frame(self):
        # code must reach the final per-player-week frame (not just the
        # fixture-level intermediate) for build_live_week_frame's
        # cross-season join to have anything to key on.
        with tempfile.TemporaryDirectory() as tmp:
            season_dir = Path(tmp) / "2025-26"
            season_dir.mkdir(parents=True)
            pd.DataFrame(
                [
                    {
                        "element": 1,
                        "name": "Test Player",
                        "team": "Sunderland",
                        "round": 1,
                        "opponent_team": 2,
                        "was_home": True,
                        "kickoff_time": "2025-08-16T11:30:00Z",
                        "minutes": 90,
                        "total_points": 5,
                        "value": 50,
                    }
                ]
            ).to_csv(season_dir / "merged_gw.csv", index=False)
            pd.DataFrame(
                [{"id": 1, "web_name": "Test Player", "team": 17, "element_type": 2, "code": 999888}]
            ).to_csv(season_dir / "players_raw.csv", index=False)
            pd.DataFrame([{"id": 2, "team_h": 17, "team_a": 3, "team_h_difficulty": 3, "team_a_difficulty": 2, "event": 1}]).to_csv(
                season_dir / "fixtures.csv", index=False
            )

            frame = normalize_vaastav_history(tmp)
            training_frame = build_training_frame(frame)

        row = training_frame.loc[training_frame["player_id"] == 1].iloc[0]
        self.assertEqual(row["code"], 999888)


class BuildLiveWeekFrameCrossSeasonJoinTestCase(unittest.TestCase):
    def test_live_frame_matches_by_code_when_player_id_is_reassigned(self):
        # Regression test (found 2026-08-12, building a real GW1 2026-27
        # squad): FPL's numeric player_id is reassigned across seasons.
        # Live id 411 was "Haaland"; in the 2025-26 training data id 411
        # belonged to a completely different real player. Before this fix,
        # build_live_week_frame joined on player_id alone, silently
        # attaching a stranger's rolling stats to Haaland's live row.
        def _raw_row(player_id, code, name, total_points, week=1):
            return {
                "season": "2025-26",
                "week": week,
                "player_id": player_id,
                "code": code,
                "player_name": name,
                "team_id": 1,
                "position": "MID",
                "price": 8.0,
                "selected_by_percent": 20.0,
                "transfers_in_event": 1000,
                "transfers_out_event": 400,
                "status": "a",
                "news": "",
                "opponent_team_id": 2,
                "was_home": True,
                "kickoff_time": "2025-08-16T11:30:00Z",
                "fixture_difficulty": 3,
                "minutes": 90,
                "total_points": total_points,
                "team_h_score": 2,
                "team_a_score": 1,
                "bonus": 1,
                "bps": 20,
                "influence": 30.0,
                "creativity": 22.0,
                "threat": 55.0,
                "ict_index": 10.7,
                "starts": 1,
                "expected_goals": 0.4,
                "expected_assists": 0.2,
                "expected_goal_involvements": 0.6,
                "expected_goals_conceded": 1.1,
                "defensive_contribution": 0.0,
            }

        # Two weeks each so points_avg_3 (a lagged, shift(1)-then-mean
        # feature) has a real prior-week value to reflect at the "last
        # known row" -- week 1 alone would just shift to nothing 0.0 for
        # both players and defeat the point of the assertion below.
        raw_history = pd.DataFrame(
            [
                _raw_row(999, 223094, "Haaland", total_points=9, week=1),
                _raw_row(999, 223094, "Haaland", total_points=9, week=2),  # real high scorer
                _raw_row(411, 472769, "Some Other Player", total_points=1, week=1),
                _raw_row(411, 472769, "Some Other Player", total_points=1, week=2),  # a stranger who has id 411 THIS season
            ]
        )
        dataset = CanonicalDataset(build_training_frame(raw_history))

        official_week_frame = pd.DataFrame(
            [
                {
                    "season": "2026-27",
                    "week": 1,
                    "player_id": 411,  # THIS season, id 411 is reassigned to Haaland
                    "code": 223094,  # but code correctly still identifies him
                    "player_name": "Haaland",
                    "team_id": 15,
                    "position": "FWD",
                    "price": 15.5,
                    "selected_by_percent": 40.0,
                    "status": "a",
                    "news": "",
                    "fixture_count": 1,
                    "fixture_difficulty_mean": 3.0,
                    "home_fixture_count": 1,
                    "away_fixture_count": 0,
                }
            ]
        )

        live_frame = dataset.build_live_week_frame(official_week_frame)
        row = live_frame.iloc[0]

        self.assertEqual(row["player_id"], 411)  # live identity preserved
        self.assertEqual(row["points_avg_3"], 9.0)  # Haaland's OWN real form, via code
        self.assertNotEqual(row["points_avg_3"], 1.0)  # not the stranger's stats


if __name__ == "__main__":
    unittest.main()

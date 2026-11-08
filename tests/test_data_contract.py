"""Data-contract invariants: units, provenance, as-of features, label maturity.

These pin the defects found in the 2026-10-03 review: ownership counts read as
percentages, end-of-season status/club snapshots used as weekly history,
full-season feature centering, multi-week labels crossing the fit cutoff, and
the live feature builder dropping the prior season.
"""

import os
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

import numpy as np
import pandas as pd

from fpl_ai.dataset import (
    STATUS_UNKNOWN,
    CanonicalDataset,
    build_training_frame,
    normalize_vaastav_history,
    training_rows_asof,
)

TEAMS = {1: "Alpha", 2: "Bravo", 3: "Charlie", 4: "Delta"}
POSITIONS = ["DEF", "MID", "MID", "FWD"]
ENTRIES = 1000


@contextmanager
def env(**values):
    previous = {key: os.environ.get(key) for key in values}
    os.environ.update({key: str(value) for key, value in values.items()})
    try:
        yield
    finally:
        for key, value in previous.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def _pairings(week):
    return [(1, 2), (3, 4)] if week % 3 == 1 else ([(1, 3), (2, 4)] if week % 3 == 2 else [(1, 4), (2, 3)])


def write_season(root, season, weeks, *, code_offset=0, mover=None, weekly_status=None, skip_week_rows=None,
                 score_seed=0, end_status=None, market=None):
    """Write a vaastav-style season: 4 teams x 4 players, two fixtures a week.

    mover: (element, new_team, from_week) moves a player between clubs mid-season.
    weekly_status: {(element, week): status} adds a per-week status column.
    skip_week_rows: {week: [elements]} drops rows (players missing in a blank week).
    end_status: {element: (status, news)} written to players_raw (end-of-season).
    market: {(element, week): (value, selected)} overrides the round's price/ownership.
    """
    season_dir = Path(root) / season
    season_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(score_seed)
    fixtures, rows = [], []
    fixture_id = 0
    for week in weeks:
        for home, away in _pairings(week):
            fixture_id += 1
            home_goals, away_goals = int(rng.integers(0, 4)), int(rng.integers(0, 4))
            kickoff = f"2025-08-{10 + week:02d}T14:00:00Z" if week < 20 else f"2025-09-{week - 19:02d}T14:00:00Z"
            fixtures.append({"id": fixture_id, "event": week, "team_h": home, "team_a": away,
                             "team_h_difficulty": 3, "team_a_difficulty": 3, "kickoff_time": kickoff,
                             "team_h_score": home_goals, "team_a_score": away_goals, "finished": True})
    fixtures_frame = pd.DataFrame(fixtures)
    fixtures_frame.to_csv(season_dir / "fixtures.csv", index=False)

    def club_of(element, week):
        base = (element - 1) // 4 + 1
        if mover and element == mover[0] and week >= mover[2]:
            return mover[1]
        return base

    for week in weeks:
        week_fixtures = fixtures_frame.loc[fixtures_frame["event"] == week]
        for element in range(1, 17):
            if skip_week_rows and element in skip_week_rows.get(week, []):
                continue
            club = club_of(element, week)
            match = week_fixtures.loc[(week_fixtures["team_h"] == club) | (week_fixtures["team_a"] == club)].iloc[0]
            home = bool(match["team_h"] == club)
            minutes = int(rng.choice([0, 25, 90, 90, 90]))
            row = {
                "element": element, "round": week, "fixture": int(match["id"]), "was_home": home,
                "opponent_team": int(match["team_a"] if home else match["team_h"]),
                "name": f"Player {element}", "team": TEAMS[club], "position": POSITIONS[(element - 1) % 4],
                "total_points": int(rng.integers(0, 9)) if minutes else 0, "minutes": minutes,
                "value": 50 + element, "selected": 1000 if element % 2 else 875,
                "transfers_in": 10 * element, "transfers_out": 5 * element,
                "kickoff_time": match["kickoff_time"], "team_h_score": match["team_h_score"],
                "team_a_score": match["team_a_score"], "goals_scored": 0, "assists": 0, "bonus": 0,
                "bps": 10, "influence": 5.0, "creativity": 5.0, "threat": 5.0, "ict_index": 1.5,
                "starts": int(minutes >= 60), "expected_goals": 0.1, "expected_assists": 0.1,
                "expected_goal_involvements": 0.2, "expected_goals_conceded": 1.0,
            }
            if market and (element, week) in market:
                row["value"], row["selected"] = market[(element, week)]
            if weekly_status is not None:
                row["status"] = weekly_status.get((element, week), "a")
                row["news"] = "" if row["status"] == "a" else "Knock"
            rows.append(row)
    pd.DataFrame(rows).to_csv(season_dir / "merged_gw.csv", index=False)

    players = []
    for element in range(1, 17):
        status, news = (end_status or {}).get(element, ("a", ""))
        players.append({"id": element, "web_name": f"Player {element}", "team": club_of(element, max(weeks)),
                        "element_type": {"GK": 1, "DEF": 2, "MID": 3, "FWD": 4}[POSITIONS[(element - 1) % 4]],
                        "status": status, "news": news, "now_cost": 50 + element, "selected_by_percent": "12.5",
                        "code": 10_000 + code_offset + element})
    pd.DataFrame(players).to_csv(season_dir / "players_raw.csv", index=False)
    pd.DataFrame([{"id": k, "name": v, "short_name": v[:3].upper()} for k, v in TEAMS.items()]).to_csv(
        season_dir / "teams.csv", index=False
    )


class OwnershipUnitsTest(unittest.TestCase):
    def test_counts_become_true_percentages(self):
        with tempfile.TemporaryDirectory() as root:
            # Players 2 and 3 are missing in week 3 (a blank-week style gap):
            # the as-of entry total must not dip and inflate everyone else.
            write_season(root, "2024-25", range(1, 6), skip_week_rows={3: [2, 3]})
            raw = normalize_vaastav_history(root)
        self.assertLessEqual(raw["selected_by_percent"].max(), 100.0)
        self.assertGreaterEqual(raw["selected_by_percent"].min(), 0.0)
        odd = raw.loc[raw["player_id"] % 2 == 1, "selected_by_percent"]
        even = raw.loc[raw["player_id"] % 2 == 0, "selected_by_percent"]
        self.assertTrue(np.allclose(odd, 100.0 * 1000 / ENTRIES))
        self.assertTrue(np.allclose(even, 100.0 * 875 / ENTRIES))
        full_week = raw.loc[raw["week"] == 1].drop_duplicates("player_id")
        self.assertAlmostEqual(full_week["selected_by_percent"].sum(), 1500.0, places=6)


class StatusProvenanceTest(unittest.TestCase):
    def test_end_of_season_snapshot_is_not_weekly_history(self):
        with tempfile.TemporaryDirectory() as root:
            write_season(root, "2024-25", range(1, 6), end_status={5: ("i", "Knee injury - Expected back 01 Jun")})
            raw = normalize_vaastav_history(root)
        self.assertTrue((raw["status"] == STATUS_UNKNOWN).all())
        self.assertTrue((raw["news"] == "").all())
        frame = build_training_frame(raw)
        self.assertEqual(frame["status_flag_pre_deadline"].sum(), 0.0)
        self.assertEqual(frame["news_flag_pre_deadline"].sum(), 0.0)

    def test_weekly_status_describes_its_own_round(self):
        with tempfile.TemporaryDirectory() as root:
            write_season(root, "2024-25", range(1, 6), weekly_status={(5, 3): "i"})
            frame = build_training_frame(normalize_vaastav_history(root))
        player = frame.loc[frame["player_id"] == 5].set_index("week")
        self.assertEqual(player.loc[3, "status_flag_pre_deadline"], 1.0)
        self.assertEqual(player.loc[2, "status_flag_pre_deadline"], 0.0)
        self.assertEqual(player.loc[4, "status_flag_pre_deadline"], 0.0)


class ClubAtFixtureTest(unittest.TestCase):
    def test_mid_season_mover_keeps_old_club_before_the_move(self):
        with tempfile.TemporaryDirectory() as root:
            # Player 1 starts at club 1 and joins club 3 from week 4; players_raw
            # (end of season) says club 3 for the whole season.
            write_season(root, "2024-25", range(1, 7), mover=(1, 3, 4))
            raw = normalize_vaastav_history(root)
        player = raw.loc[raw["player_id"] == 1].set_index("week")["team_id"]
        self.assertEqual(int(player.loc[3]), 1)
        self.assertEqual(int(player.loc[4]), 3)


class AsOfFeatureTest(unittest.TestCase):
    def _frame(self, root, seed):
        write_season(root, "2024-25", range(1, 11), score_seed=seed)
        return normalize_vaastav_history(root)

    def test_future_outcomes_cannot_change_past_features(self):
        cutoff = 6
        with env(FPL_OPPONENT_INTERACTION=1, FPL_TEAM_ATTACK_INTERACTION=1):
            with tempfile.TemporaryDirectory() as root:
                raw = self._frame(root, seed=1)
            mutated = raw.copy()
            future = mutated["week"] >= cutoff
            mutated.loc[future, "team_h_score"] = mutated.loc[future, "team_h_score"] + 5
            mutated.loc[future, "total_points"] = mutated.loc[future, "total_points"] + 7
            mutated.loc[future, "minutes"] = 90
            original_frame = build_training_frame(raw)
            mutated_frame = build_training_frame(mutated)
        features = [c for c in CanonicalDataset(original_frame).feature_columns]
        self.assertIn("opp_def_weakness_3", features)
        self.assertIn("team_attack_strength_3", features)
        past = original_frame["week"] <= cutoff
        left = original_frame.loc[past, features].reset_index(drop=True)
        right = mutated_frame.loc[mutated_frame["week"] <= cutoff, features].reset_index(drop=True)
        pd.testing.assert_frame_equal(left, right, check_exact=False, atol=1e-12)


class LabelMaturityTest(unittest.TestCase):
    def test_unsettled_multiweek_labels_are_masked(self):
        with tempfile.TemporaryDirectory() as root:
            write_season(root, "2024-25", range(1, 12), score_seed=3)
            frame = build_training_frame(normalize_vaastav_history(root))
        rows = training_rows_asof(frame, "2024-25", 8)
        self.assertTrue((rows["week"] < 8).all())
        self.assertTrue(rows.loc[rows["week"] >= 4, "label_points_5gw"].isna().all())
        self.assertTrue(rows.loc[rows["week"] < 4, "label_points_5gw"].notna().all())
        self.assertTrue(rows.loc[rows["week"] >= 6, "label_points_3gw"].isna().all())
        self.assertTrue(rows.loc[rows["week"] < 6, "label_points_3gw"].notna().all())
        self.assertTrue(rows["label_points_1gw"].notna().all())

    def test_outcomes_at_or_after_cutoff_cannot_change_training_labels(self):
        with tempfile.TemporaryDirectory() as root:
            write_season(root, "2024-25", range(1, 12), score_seed=4)
            raw = normalize_vaastav_history(root)
        mutated = raw.copy()
        mutated.loc[mutated["week"] >= 8, "total_points"] += 9
        left = training_rows_asof(build_training_frame(raw), "2024-25", 8)
        right = training_rows_asof(build_training_frame(mutated), "2024-25", 8)
        for column in ("label_points_1gw", "label_points_3gw", "label_points_5gw", "label_minutes_1gw"):
            pd.testing.assert_series_equal(
                left[column].reset_index(drop=True), right[column].reset_index(drop=True)
            )


class LiveBatchParityTest(unittest.TestCase):
    def test_live_builder_reproduces_batch_features_including_prior_blend(self):
        next_week = 5
        with env(FPL_PRIOR_BLEND=1, FPL_OPPONENT_INTERACTION=1):
            with tempfile.TemporaryDirectory() as full_root, tempfile.TemporaryDirectory() as live_root:
                # Same player codes in both seasons so the prior blend applies.
                write_season(full_root, "2024-25", range(1, 11), score_seed=11)
                write_season(full_root, "2025-26", range(1, next_week + 1), score_seed=12)
                write_season(live_root, "2024-25", range(1, 11), score_seed=11)
                write_season(live_root, "2025-26", range(1, next_week + 1), score_seed=12)
                live_dir = Path(live_root) / "2025-26"
                merged = pd.read_csv(live_dir / "merged_gw.csv")
                merged.loc[merged["round"] < next_week].to_csv(live_dir / "merged_gw.csv", index=False)

                batch = build_training_frame(normalize_vaastav_history(full_root))
                dataset = CanonicalDataset(batch)
                live = dataset._build_next_week_form_features(live_root, "2025-26", next_week)
        batch_rows = batch.loc[(batch["season"] == "2025-26") & (batch["week"] == next_week)].set_index("code")
        live_rows = live.set_index("code")
        columns = [c for c in dataset.feature_columns if c not in CanonicalDataset._LIVE_OWNED_FEATURES]
        self.assertIn("points_avg_3", columns)
        pd.testing.assert_frame_equal(
            batch_rows.loc[live_rows.index, columns].sort_index(),
            live_rows[columns].sort_index(),
            check_exact=False,
            atol=1e-9,
        )


class MarketTimingTest(unittest.TestCase):
    def test_round_market_state_is_its_own_deadline_state(self):
        move = {(3, week): (54, 600) for week in (3, 4, 5)}
        with tempfile.TemporaryDirectory() as root:
            write_season(root, "2024-25", range(1, 6), market=move)
            frame = build_training_frame(normalize_vaastav_history(root))
        player = frame.loc[frame["player_id"] == 3].set_index("week")
        self.assertAlmostEqual(player.loc[2, "price_pre_deadline"], 5.3)
        self.assertAlmostEqual(player.loc[3, "price_pre_deadline"], 5.4)
        self.assertAlmostEqual(player.loc[3, "price_change_1"], 0.1)
        self.assertEqual(player.loc[1, "price_change_1"], 0.0)
        self.assertAlmostEqual(player.loc[4, "price_change_1"], 0.0)
        self.assertTrue(np.allclose(player["selected_by_percent_pre_deadline"], player["selected_by_percent"]))
        self.assertAlmostEqual(
            player.loc[3, "selected_change_1"],
            player.loc[3, "selected_by_percent"] - player.loc[2, "selected_by_percent"],
        )
        self.assertLess(player.loc[3, "selected_change_1"], 0.0)

    def test_live_market_changes_are_within_season(self):
        with tempfile.TemporaryDirectory() as root:
            write_season(root, "2024-25", range(1, 6))
            frame = build_training_frame(normalize_vaastav_history(root))
        dataset = CanonicalDataset(frame)
        last_pct = float(frame.loc[(frame["week"] == 5) & (frame["player_id"] == 3), "selected_by_percent"].iloc[0])
        base = {"season": "2024-25", "week": 6, "status": "a", "news": "", "fixture_count": 1,
                "home_fixture_count": 1, "away_fixture_count": 0, "fixture_difficulty_mean": 3.0}
        official = pd.DataFrame([
            {**base, "player_id": 3, "code": 10_003, "player_name": "Player 3", "team_id": 1, "position": "MID",
             "price": 5.4, "selected_by_percent": last_pct + 2.0},
            {**base, "player_id": 99, "code": 99_999, "player_name": "New Signing", "team_id": 2, "position": "FWD",
             "price": 6.0, "selected_by_percent": 1.5},
        ])
        live = dataset.build_live_week_frame(official).set_index("player_id")
        self.assertAlmostEqual(live.loc[3, "price_change_1"], 0.1)
        self.assertAlmostEqual(live.loc[3, "selected_change_1"], 2.0)
        self.assertEqual(live.loc[99, "price_change_1"], 0.0)
        self.assertEqual(live.loc[99, "selected_change_1"], 0.0)


class FirstRowPriceTest(unittest.TestCase):
    def test_first_week_price_is_the_launch_price(self):
        with tempfile.TemporaryDirectory() as root:
            write_season(root, "2024-25", range(1, 4))
            frame = build_training_frame(normalize_vaastav_history(root))
        first = frame.loc[frame["week"] == 1]
        self.assertTrue((first["price_pre_deadline"] > 0).all())
        self.assertTrue(np.allclose(first["price_pre_deadline"], first["price"]))


if __name__ == "__main__":
    unittest.main()

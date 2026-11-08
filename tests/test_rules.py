"""Official-rules invariants: legal formations, autosubs and selling prices."""

import itertools
import unittest
from collections import Counter

import pandas as pd

from fpl_ai.backtest import _apply_automatic_substitutions, _apply_transfer, _effective_captain, _refresh_squad_prices
from fpl_ai.config import STARTING_FORMATIONS
from fpl_ai.decision import _optimize_lineup
from fpl_ai.rules import automatic_substitutions, is_legal_xi, selling_price
from fpl_ai.types import PlayerForecast, SquadPlayer

SQUAD_POSITIONS = ["GK"] * 2 + ["DEF"] * 5 + ["MID"] * 5 + ["FWD"] * 3


def make_squad(prices=None):
    return [
        SquadPlayer(player_id, f"P{player_id}", player_id, position, (prices or {}).get(player_id, 5.0))
        for player_id, position in enumerate(SQUAD_POSITIONS, start=1)
    ]


def forecast_for(player, points, appearance=0.95):
    return PlayerForecast(
        season="2025-26", week=10, player_id=player.player_id, player_name=player.player_name,
        team_id=player.team_id, position=player.position, price=player.sell_price,
        predicted_minutes=85.0, predicted_points_1gw=points, predicted_points_3gw=3 * points,
        predicted_points_5gw=5 * points, appearance_probability=appearance, fixture_count=1, uncertainty=0.2,
    )


class FormationTest(unittest.TestCase):
    def test_formations_are_exactly_the_legal_set(self):
        shapes = {(f["DEF"], f["MID"], f["FWD"]) for f in STARTING_FORMATIONS}
        self.assertEqual(
            shapes,
            {(3, 4, 3), (3, 5, 2), (4, 3, 3), (4, 4, 2), (4, 5, 1), (5, 2, 3), (5, 3, 2), (5, 4, 1)},
        )
        self.assertNotIn((3, 3, 4), shapes)
        self.assertTrue(all(f["GK"] == 1 for f in STARTING_FORMATIONS))

    def test_optimizer_matches_exhaustive_search_including_5_2_3(self):
        squad = make_squad()
        # Strong defenders and forwards, weak midfield: the best XI is 5-2-3.
        points = {1: 4.0, 2: 1.0, 3: 6.0, 4: 6.0, 5: 6.0, 6: 6.0, 7: 6.0,
                  8: 5.0, 9: 5.0, 10: 1.0, 11: 1.0, 12: 1.0, 13: 7.0, 14: 7.0, 15: 7.0}
        forecasts = {player.player_id: forecast_for(player, points[player.player_id]) for player in squad}
        starters, bench, _, _, _ = _optimize_lineup(squad, forecasts)
        positions = {player.player_id: player.position for player in squad}
        best = max(
            sum(points[pid] for pid in combo)
            for combo in itertools.combinations(points, 11)
            if is_legal_xi(Counter(positions[pid] for pid in combo))
        )
        self.assertAlmostEqual(sum(points[pid] for pid in starters), best)
        self.assertEqual(Counter(positions[pid] for pid in starters), Counter({"GK": 1, "DEF": 5, "MID": 2, "FWD": 3}))
        self.assertEqual(len(bench), 4)

    def test_squad_that_cannot_field_a_legal_xi_is_rejected(self):
        squad = [player for player in make_squad() if player.position != "GK"]
        forecasts = {player.player_id: forecast_for(player, 3.0) for player in squad}
        with self.assertRaises(ValueError):
            _optimize_lineup(squad, forecasts)


class AutoSubTest(unittest.TestCase):
    # XI: GK 1, DEF 3-5, MID 8-11, FWD 13-15 (3-4-3); bench: GK 2, then 6, 12, 7.
    starters = [1, 3, 4, 5, 8, 9, 10, 11, 13, 14, 15]
    bench = [2, 6, 12, 7]
    positions = {pid: pos for pid, pos in enumerate(SQUAD_POSITIONS, start=1)}

    def run_subs(self, absent):
        minutes = {pid: (0.0 if pid in absent else 90.0) for pid in range(1, 16)}
        return automatic_substitutions(self.positions, self.starters, self.bench, minutes)

    def test_nobody_missing_means_no_substitutions(self):
        counted, subs = self.run_subs(set())
        self.assertEqual(sorted(counted), sorted(self.starters))
        self.assertEqual(subs, [])

    def test_goalkeeper_is_only_replaced_by_the_bench_goalkeeper(self):
        counted, subs = self.run_subs({1})
        self.assertEqual(subs, [(1, 2)])
        counted, subs = self.run_subs({1, 2})
        self.assertEqual(subs, [])
        self.assertEqual(len(counted), 10)

    def test_bench_priority_respects_formation_minimums(self):
        # A missing defender in a back three: the first bench outfielder is a
        # defender (6), so he comes on; the missing midfielder gets the next (12).
        counted, subs = self.run_subs({3, 8})
        self.assertEqual(subs, [(3, 6), (8, 12)])
        self.assertEqual(len(counted), 11)

    def test_missing_defenders_cannot_be_covered_by_midfielders(self):
        # Two of the back three absent and bench defender 6 also absent: only
        # defender 7 can come on, midfielder 12 cannot replace a defender.
        counted, subs = self.run_subs({3, 4, 6})
        self.assertEqual(subs, [(3, 7)])
        self.assertEqual(len(counted), 10)

    def test_partial_substitution_when_bench_cannot_fill_every_gap(self):
        # Four absent outfielders, three playing outfield subs: all three come on.
        counted, subs = self.run_subs({9, 10, 11, 13})
        self.assertEqual(len(subs), 3)
        self.assertEqual(len(counted), 10)

    def test_five_absent_starters_use_every_legal_substitute(self):
        counted, subs = self.run_subs({1, 4, 9, 10, 14})
        self.assertEqual({sub for _, sub in subs}, {2, 6, 12, 7})
        self.assertEqual(len(counted), 10)

    def test_backtest_wrapper_counts_partial_substitutions(self):
        squad = make_squad()
        minutes = {pid: (0.0 if pid in {9, 10, 11, 13} else 90.0) for pid in range(1, 16)}
        points = {pid: 2.0 for pid in range(1, 16)}
        counted, notes = _apply_automatic_substitutions(squad, self.starters, self.bench, points, minutes)
        self.assertEqual(len(counted), 10)
        self.assertEqual(len(notes), 3)

    def test_vice_takes_the_armband_only_when_the_captain_does_not_play(self):
        self.assertEqual(_effective_captain(8, 13, {8: 90.0, 13: 90.0}), 8)
        self.assertEqual(_effective_captain(8, 13, {8: 0.0, 13: 90.0}), 13)


class SellingPriceTest(unittest.TestCase):
    def test_half_of_a_rise_is_kept_rounded_down(self):
        self.assertEqual(selling_price(5.0, 5.1), 5.0)
        self.assertEqual(selling_price(5.0, 5.2), 5.1)
        self.assertEqual(selling_price(5.0, 5.3), 5.1)
        self.assertEqual(selling_price(5.0, 5.4), 5.2)
        self.assertEqual(selling_price(7.5, 8.6), 8.0)

    def test_falls_are_taken_in_full(self):
        self.assertEqual(selling_price(5.0, 4.8), 4.8)
        self.assertEqual(selling_price(5.0, 5.0), 5.0)

    def test_backtest_refresh_keeps_purchase_price_and_bank_is_conserved(self):
        squad = make_squad()
        frame = pd.DataFrame([{"player_id": pid, "price_pre_deadline": 5.4 if pid == 8 else 4.9, "price": 9.9}
                              for pid in range(1, 16)])
        refreshed = _refresh_squad_prices(squad, frame)
        by_id = {player.player_id: player for player in refreshed}
        self.assertEqual(by_id[8].sell_price, 5.2)
        self.assertEqual(by_id[8].purchase_price, 5.0)
        self.assertEqual(by_id[3].sell_price, 4.9)
        # A second refresh at the same prices must not ratchet the purchase price.
        self.assertEqual({p.player_id: p.sell_price for p in _refresh_squad_prices(refreshed, frame)},
                         {p.player_id: p.sell_price for p in refreshed})
        incoming = forecast_for(SquadPlayer(99, "New", 20, "MID", 5.0), 4.0)
        after, bank = _apply_transfer(refreshed, 0.5, [8], [99], {99: incoming})
        self.assertAlmostEqual(bank, 0.5 + 5.2 - 5.0)
        new_player = next(player for player in after if player.player_id == 99)
        self.assertEqual(new_player.purchase_price, 5.0)


if __name__ == "__main__":
    unittest.main()

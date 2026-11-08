import unittest

from fpl_ai.backtest import _apply_automatic_substitutions, _optimize_chip_schedule, build_initial_squad
from fpl_ai.types import PlayerForecast, SquadPlayer


def make_forecast(player_id, name, team_id, position, price, p1, p3, p5, appearance=0.9, minutes=85):
    return PlayerForecast(
        season="2025-26",
        week=11,
        player_id=player_id,
        player_name=name,
        team_id=team_id,
        position=position,
        price=price,
        predicted_minutes=minutes,
        predicted_points_1gw=p1,
        predicted_points_3gw=p3,
        predicted_points_5gw=p5,
        appearance_probability=appearance,
        fixture_count=1,
        uncertainty=0.2,
    )


class BacktestHelpersTestCase(unittest.TestCase):
    def test_optimize_chip_schedule_prefers_highest_total_value(self):
        chip_plan = _optimize_chip_schedule(
            {
                24: {"bench_boost": 12.0, "triple_captain": 5.0},
                25: {"bench_boost": 10.0, "triple_captain": 9.0},
                26: {"bench_boost": 18.0, "triple_captain": 7.0},
            },
            bench_boost_available=True,
            triple_captain_available=True,
        )
        self.assertEqual(chip_plan[25], "triple_captain")
        self.assertEqual(chip_plan[26], "bench_boost")

    def test_optimize_chip_schedule_can_hold_chip_for_later_better_week(self):
        chip_plan = _optimize_chip_schedule(
            {
                11: {"bench_boost": 14.0, "triple_captain": 0.0},
                26: {"bench_boost": 22.0, "triple_captain": 8.0},
            },
            bench_boost_available=True,
            triple_captain_available=True,
        )
        self.assertNotIn(11, chip_plan)
        self.assertEqual(chip_plan[26], "bench_boost")

    def test_build_initial_squad_returns_legal_budgeted_squad(self):
        forecasts = []
        player_id = 1
        for team_id in range(1, 11):
            forecasts.append(make_forecast(player_id, f"GK {team_id}A", team_id, "GK", 4.5, 4.0, 10.0, 16.0))
            player_id += 1
            forecasts.append(make_forecast(player_id, f"GK {team_id}B", team_id, "GK", 4.0, 3.5, 8.0, 12.0))
            player_id += 1
            forecasts.append(make_forecast(player_id, f"DEF {team_id}A", team_id, "DEF", 5.0, 5.0, 12.0, 18.0))
            player_id += 1
            forecasts.append(make_forecast(player_id, f"DEF {team_id}B", team_id, "DEF", 4.3, 3.5, 9.0, 14.0))
            player_id += 1
            forecasts.append(make_forecast(player_id, f"MID {team_id}A", team_id, "MID", 8.0, 6.5, 16.0, 25.0))
            player_id += 1
            forecasts.append(make_forecast(player_id, f"MID {team_id}B", team_id, "MID", 5.5, 4.0, 10.0, 16.0))
            player_id += 1
            forecasts.append(make_forecast(player_id, f"FWD {team_id}A", team_id, "FWD", 7.5, 5.5, 14.0, 22.0))
            player_id += 1

        squad, bank = build_initial_squad(forecasts, budget=100.0)
        self.assertEqual(len(squad), 15)
        self.assertGreaterEqual(bank, 0.0)
        self.assertLessEqual(sum(player.sell_price for player in squad), 100.0 + 1e-9)
        self.assertEqual(sum(player.position == "GK" for player in squad), 2)
        self.assertEqual(sum(player.position == "DEF" for player in squad), 5)
        self.assertEqual(sum(player.position == "MID" for player in squad), 5)
        self.assertEqual(sum(player.position == "FWD" for player in squad), 3)
        self.assertTrue(all(sum(p.team_id == team_id for p in squad) <= 3 for team_id in range(1, 11)))

    def test_automatic_substitutions_use_bench_and_preserve_formation(self):
        squad_players = [
            SquadPlayer(1, "GK Start", 1, "GK", 4.5),
            SquadPlayer(2, "GK Bench", 2, "GK", 4.0),
            SquadPlayer(3, "DEF One", 1, "DEF", 5.0),
            SquadPlayer(4, "DEF Two", 2, "DEF", 4.8),
            SquadPlayer(5, "DEF Three", 3, "DEF", 4.6),
            SquadPlayer(6, "DEF Bench", 4, "DEF", 4.4),
            SquadPlayer(7, "DEF Bench Two", 5, "DEF", 4.0),
            SquadPlayer(8, "MID One", 1, "MID", 8.0),
            SquadPlayer(9, "MID Two", 2, "MID", 7.5),
            SquadPlayer(10, "MID Three", 3, "MID", 7.0),
            SquadPlayer(11, "MID Four", 4, "MID", 6.5),
            SquadPlayer(12, "MID Bench", 5, "MID", 5.0),
            SquadPlayer(13, "FWD One", 6, "FWD", 8.0),
            SquadPlayer(14, "FWD Two", 7, "FWD", 7.0),
            SquadPlayer(15, "FWD Bench", 8, "FWD", 6.0),
        ]
        starters = [1, 3, 4, 5, 8, 9, 10, 11, 13, 14, 6]
        bench_order = [2, 12, 15, 7]
        actual_minutes = {player.player_id: 90.0 for player in squad_players}
        actual_points = {player.player_id: 2.0 for player in squad_players}
        actual_minutes[1] = 0.0
        actual_minutes[13] = 0.0

        realized_starters, notes = _apply_automatic_substitutions(
            squad_players=squad_players,
            starters=starters,
            bench_order=bench_order,
            actual_points=actual_points,
            actual_minutes=actual_minutes,
        )

        self.assertIn(2, realized_starters)
        self.assertIn(12, realized_starters)
        self.assertNotIn(13, realized_starters)
        self.assertEqual(len(realized_starters), 11)
        self.assertTrue(notes)


if __name__ == "__main__":
    unittest.main()

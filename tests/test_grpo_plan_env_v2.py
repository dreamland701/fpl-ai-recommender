"""G5 environment invariants: no future information, strict plans, official scoring, fair baseline."""

import json
import unittest
from dataclasses import replace

from fpl_ai.grpo_env import WeeklyState
from fpl_ai.grpo_plan_env_v2 import (
    PlanEnvV2,
    WeekAction,
    max_free_transfers,
    parse_plan,
    receding_value,
)
from fpl_ai.squad_milp import optimize
from fpl_ai.types import PlayerForecast, SquadPlayer

POSITIONS = ["GK"] * 4 + ["DEF"] * 10 + ["MID"] * 10 + ["FWD"] * 6


def forecasts(season, week, bump=None):
    bump = bump or {}
    out = []
    for i, pos in enumerate(POSITIONS, start=1):
        base = 2.0 + (i % 7) * 0.5 + bump.get(i, 0.0)
        out.append(PlayerForecast(
            season=season, week=week, player_id=i, player_name=f"P{i}", team_id=(i % 10) + 1, position=pos,
            price=4.5 + (i % 5) * 0.5, predicted_minutes=80.0, predicted_points_1gw=base,
            predicted_points_3gw=base * 3, predicted_points_5gw=base * 5, appearance_probability=0.9,
            fixture_count=1, uncertainty=0.2))
    return out


def squad():
    ids = [1, 2, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 25, 26, 27]
    table = {f.player_id: f for f in forecasts("2024-25", 10)}
    return [SquadPlayer(i, f"P{i}", table[i].team_id, table[i].position, table[i].price) for i in ids]


def state(week, season="2024-25", minutes=None, points=None, bump=None, price_bump=None):
    fs = forecasts(season, week, bump)
    if price_bump:
        fs = [replace(f, price=f.price + price_bump.get(f.player_id, 0.0)) for f in fs]
    minutes = minutes or {}
    points = points or {}
    return WeeklyState(season=season, week=week, squad=squad(), bank=0.5, free_transfers=1, forecasts=fs,
                       actual_points={f.player_id: points.get(f.player_id, 2.0) for f in fs},
                       actual_minutes={f.player_id: minutes.get(f.player_id, 90.0) for f in fs})


def env(states, chips=None):
    return PlanEnvV2(states, optimize, chips=chips)


class ObservationTest(unittest.TestCase):
    def test_future_weeks_cannot_change_the_observation(self):
        a = env([state(10), state(11), state(12)])
        b = env([state(10), state(11, bump={30: 9.0}, points={30: 25.0}), state(12, minutes={1: 0.0})])
        self.assertEqual(a.state_prompt(), b.state_prompt())

    def test_prompt_states_the_free_transfer_cap(self):
        self.assertIn("(max 5)", env([state(10), state(11)]).state_prompt())
        self.assertIn("(max 2)", env([state(10, season="2023-24"), state(11, season="2023-24")]).state_prompt())


class ParseTest(unittest.TestCase):
    def test_exact_length_and_schema_required(self):
        good = json.dumps([{"transfer": "hold", "captain": 25, "chip": "none"},
                           {"transfer": "best1", "captain": None, "chip": "triple_captain"}])
        self.assertEqual(len(parse_plan(good, 2)), 2)
        self.assertIsNone(parse_plan(good, 3))
        self.assertIsNone(parse_plan(json.dumps([{"transfer": "sell everyone", "chip": "none"}]), 1))
        self.assertIsNone(parse_plan(json.dumps([{"transfer": "hold", "captain": True, "chip": "none"}]), 1))
        self.assertIsNone(parse_plan('{"transfer": "hold"}', 1))


class RolloutTest(unittest.TestCase):
    def test_each_chip_once_per_half(self):
        e = env([state(10), state(11)])
        _, detail = e.rollout([WeekAction(chip="triple_captain"), WeekAction(chip="triple_captain")])
        self.assertEqual([d["chip"] for d in detail], ["triple_captain", "none"])
        e2 = env([state(19), state(20)])
        _, detail2 = e2.rollout([WeekAction(chip="triple_captain"), WeekAction(chip="triple_captain")])
        self.assertEqual([d["chip"] for d in detail2], ["triple_captain", "triple_captain"])

    def test_unavailable_chip_is_not_played(self):
        e = env([state(10), state(11)], chips={1: frozenset({"bench_boost"})})
        _, detail = e.rollout([WeekAction(chip="wildcard"), WeekAction()])
        self.assertEqual(detail[0]["chip"], "none")

    def test_free_hit_reverts_and_wildcard_persists(self):
        boost = {i: 6.0 for i in (3, 4, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 28, 29, 30)}
        states = [state(10, bump=boost), state(11, bump=boost), state(12, bump=boost)]
        e = env(states)
        start = set(e._start_squad().players)
        squads = []
        original_lineup = PlanEnvV2._lineup

        def spy(squad, table):
            squads.append(set(squad.players))
            return original_lineup(squad, table)

        PlanEnvV2._lineup = staticmethod(spy)
        try:
            e.rollout([WeekAction(chip="free_hit"), WeekAction(), WeekAction(chip="wildcard")])
        finally:
            PlanEnvV2._lineup = staticmethod(original_lineup)
        self.assertNotEqual(squads[0], start)
        self.assertEqual(squads[1], start)
        self.assertNotEqual(squads[2], start)

    def test_absent_starter_is_autosubbed(self):
        played = env([state(10), state(11)])
        missing = env([state(10, minutes={27: 0.0}), state(11)])
        hold = [WeekAction(captain=None), WeekAction()]
        total_played, _ = played.rollout(hold)
        total_missing, _ = missing.rollout(hold)
        # Everyone scores 2: the absent starter is replaced, so the total is unchanged.
        self.assertEqual(total_played, total_missing)

    def test_free_transfer_cap_by_season(self):
        self.assertEqual(max_free_transfers("2023-24"), 2)
        self.assertEqual(max_free_transfers("2024-25"), 5)

    def test_selling_price_keeps_half_the_rise(self):
        e = env([state(10, price_bump={1: 0.4}), state(11)])
        squad = e._start_squad()
        e._refresh_sell(squad, e._forecast_table(e.states[0]))
        self.assertAlmostEqual(squad.players[1]["sell"], squad.players[1]["purchase"] + 0.2)


class BaselineTest(unittest.TestCase):
    def test_baseline_spends_the_same_chips(self):
        e = env([state(10), state(11), state(12)], chips={1: frozenset({"triple_captain", "bench_boost"})})
        chips = {a.chip for a in e.baseline_plan()}
        self.assertTrue({"triple_captain", "bench_boost"} <= chips)
        e2 = env([state(10), state(11)], chips={1: frozenset()})
        self.assertEqual({a.chip for a in e2.baseline_plan()}, {"none"})

    def test_unparseable_plans_are_penalised(self):
        e = env([state(10), state(11)])
        results = e.evaluate_group(["not json", json.dumps([{"transfer": "hold", "chip": "none"}] * 2)])
        self.assertLess(results[0].reward, 0)
        self.assertIsNotNone(results[1].plan)


if __name__ == "__main__":
    unittest.main()


class RecedingValueTest(unittest.TestCase):
    """The G6 reward scores only the first week, then the planner re-planned from the state it leaves."""

    def test_value_is_deterministic(self):
        e = env([state(10), state(11), state(12)])
        first = WeekAction(transfer="best1")
        self.assertEqual(receding_value(e, first), receding_value(e, first))

    def test_equals_first_week_then_replanned_planner(self):
        states = [state(10), state(11, points={5: 9.0}), state(12)]
        e = env(states)
        first = WeekAction(transfer="hold")
        r1, _, carried = PlanEnvV2(states[:1], optimize, chips=e.chips).rollout([first], return_state=True)
        nxt = replace(states[1], squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        cont = PlanEnvV2([nxt, states[2]], optimize, chips=carried["chips"])
        rest, _ = cont.rollout(cont.baseline_plan())
        self.assertAlmostEqual(receding_value(e, first), r1 + rest)

    def test_spending_a_held_chip_forfeits_its_value(self):
        e = env([state(10), state(11), state(12)])
        values = {"free_hit": 100.0, "wildcard": 0.0}
        keep = receding_value(e, WeekAction(transfer="best1"), values) - receding_value(e, WeekAction(transfer="best1"))
        spend = (receding_value(e, WeekAction(transfer="best1", chip="free_hit"), values)
                 - receding_value(e, WeekAction(transfer="best1", chip="free_hit")))
        self.assertAlmostEqual(keep, 100.0)
        self.assertAlmostEqual(spend, 0.0)

    def test_chips_expire_with_the_half(self):
        e = env([state(17), state(18), state(19)])
        values = {"free_hit": 100.0, "wildcard": 100.0}
        self.assertAlmostEqual(receding_value(e, WeekAction(transfer="best1"), values),
                               receding_value(e, WeekAction(transfer="best1")))


class DisciplinedTransferTest(unittest.TestCase):
    """"auto" makes the best single move only when it beats holding by PLANNER_MIN_GAIN (G7b planner)."""

    def test_auto_holds_below_the_bar_and_moves_above_it(self):
        import fpl_ai.grpo_plan_env_v2 as envmod
        e = env([state(10, bump={30: 6.0})])
        saved = envmod.PLANNER_MIN_GAIN
        try:
            envmod.PLANNER_MIN_GAIN = 1e9
            _, held = e.rollout([WeekAction(transfer="auto")])
            envmod.PLANNER_MIN_GAIN = -1e9
            _, moved = env([state(10, bump={30: 6.0})]).rollout([WeekAction(transfer="auto")])
        finally:
            envmod.PLANNER_MIN_GAIN = saved
        self.assertEqual(held[0]["hits"], 0)
        best1 = env([state(10, bump={30: 6.0})]).rollout([WeekAction(transfer="best1")])[0]
        self.assertAlmostEqual(env([state(10, bump={30: 6.0})]).rollout([WeekAction(transfer="hold")])[0],
                               e.rollout([WeekAction(transfer="hold")])[0])
        self.assertAlmostEqual(moved[0]["realized"], best1)


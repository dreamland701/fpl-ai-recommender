"""Tests for the weekly-bandit GRPO environment scaffold."""

import math

from fpl_ai.grpo_env import DecisionAction, WeeklyBanditEnv, WeeklyState, parse_action
from fpl_ai.types import PlayerForecast, SquadPlayer


def _forecast(player_id, name, position, price, pts1, pts3, prob=0.9, team_id=1, minutes=85.0):
    return PlayerForecast(
        season="2025-26",
        week=12,
        player_id=player_id,
        player_name=name,
        team_id=team_id,
        position=position,
        price=price,
        predicted_minutes=minutes,
        predicted_points_1gw=pts1,
        predicted_points_3gw=pts3,
        predicted_points_5gw=pts3 * 1.6,
        appearance_probability=prob,
        fixture_count=1,
        uncertainty=0.2,
    )


def _make_state():
    # 15-player legal squad: 2 GK, 5 DEF, 5 MID, 3 FWD across many teams.
    spec = [
        ("GK", 2), ("DEF", 5), ("MID", 5), ("FWD", 3),
    ]
    squad, forecasts = [], []
    player_id = 1
    for position, count in spec:
        for _ in range(count):
            squad.append(
                SquadPlayer(player_id=player_id, player_name=f"P{player_id}", team_id=player_id, position=position, sell_price=5.0)
            )
            forecasts.append(_forecast(player_id, f"P{player_id}", position, 5.0, 3.0 + 0.1 * player_id, 9.0, team_id=player_id))
            player_id += 1
    # A clearly better transfer candidate (MID) and a weak one.
    forecasts.append(_forecast(100, "Star", "MID", 5.0, 9.0, 27.0, team_id=100))
    forecasts.append(_forecast(101, "Scrub", "MID", 4.5, 0.5, 1.5, team_id=101))

    actual_points = {pid: 2.0 for pid in range(1, 16)}
    actual_points[15] = 12.0        # best captain in the base squad (FWD)
    actual_points[100] = 15.0       # the star transfer pays off
    actual_minutes = {pid: 90.0 for pid in range(1, 16)}
    actual_minutes[100] = 90.0
    return WeeklyState(
        season="2025-26",
        week=12,
        squad=squad,
        bank=2.0,
        free_transfers=1,
        forecasts=forecasts,
        actual_points=actual_points,
        actual_minutes=actual_minutes,
    )


def test_parse_action_clips_and_defaults():
    action = parse_action('{"horizon": "blend5", "soft_knee": 5.0, "transfer_aggressiveness": -3, "captain_pick": "7"}')
    assert action.horizon == "blend5"
    assert action.soft_knee == 0.95          # clipped to bound
    assert action.transfer_aggressiveness == 0.0
    assert action.captain_pick == 7
    assert parse_action("no json here") is None
    assert parse_action('{"horizon": "bogus"}').horizon == "3gw"  # unknown -> default


def test_default_action_reproduces_classic_baseline():
    env = WeeklyBanditEnv(_make_state())
    realized, _ = env._realized_for_action(DecisionAction())
    assert realized == env.baseline_realized()


def test_group_rewards_are_paired_and_advantages_normalized():
    env = WeeklyBanditEnv(_make_state())
    responses = [
        "{}",                                                   # baseline clone
        '{"captain_pick": 15}',                                 # good captain
        '{"transfer_aggressiveness": 2.0}',                     # takes the star transfer
        "garbage output",                                       # unparseable
    ]
    results = env.evaluate_group(responses)

    assert results[0].reward == 0.0, "default action must be reward-neutral vs baseline"
    assert results[3].action is None and results[3].reward == -1.0, "garbage must be penalized"
    mean_advantage = sum(result.advantage for result in results) / len(results)
    assert math.isclose(mean_advantage, 0.0, abs_tol=1e-9)
    stds = [result.advantage for result in results]
    assert any(abs(a) > 0 for a in stds), "advantages should not all collapse to zero"


def test_captain_pick_changes_reward_when_captain_scores():
    env = WeeklyBanditEnv(_make_state())
    baseline = env.baseline_realized()
    realized, detail = env._realized_for_action(DecisionAction(captain_pick=15))
    if detail["captain_id"] == 15:
        assert realized >= baseline


def test_captain_pick_outside_starters_falls_back():
    env = WeeklyBanditEnv(_make_state())
    _, detail = env._realized_for_action(DecisionAction(captain_pick=999))
    assert detail["captain_id"] != 999


def test_state_prompt_contains_squad_and_schema():
    env = WeeklyBanditEnv(_make_state())
    prompt = env.state_prompt()
    assert "GW12" in prompt
    assert "Star" in prompt, "top candidate must be shown"
    assert "captain_pick" in prompt, "output schema must be stated"

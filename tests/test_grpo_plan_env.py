"""Tests for the G2 plan-horizon GRPO environment."""

import json

from fpl_ai.grpo_env import WeeklyState
from fpl_ai.grpo_plan_env import (
    CHIPS,
    PlanAction,
    PlanEpisodeEnv,
    build_episodes,
    parse_plan,
)
from fpl_ai.types import PlayerForecast, SquadPlayer


def _forecast(player_id, name, position, price, pts1, pts3, prob=0.9, team_id=1, minutes=85.0, week=12):
    return PlayerForecast(
        season="2025-26",
        week=week,
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


def _make_week(week, star_pays=True):
    spec = [("GK", 2), ("DEF", 5), ("MID", 5), ("FWD", 3)]
    squad, forecasts = [], []
    player_id = 1
    for position, count in spec:
        for _ in range(count):
            squad.append(
                SquadPlayer(player_id=player_id, player_name=f"P{player_id}", team_id=player_id, position=position, sell_price=5.0)
            )
            forecasts.append(_forecast(player_id, f"P{player_id}", position, 5.0, 3.0 + 0.1 * player_id, 9.0, team_id=player_id, week=week))
            player_id += 1
    forecasts.append(_forecast(100, "Star", "MID", 5.0, 9.0, 27.0, team_id=100, week=week))

    actual_points = {pid: 2.0 for pid in range(1, 16)}
    actual_points[15] = 12.0
    actual_points[100] = 15.0 if star_pays else 0.0
    actual_minutes = {pid: 90.0 for pid in range(1, 16)}
    actual_minutes[100] = 90.0
    return WeeklyState(
        season="2025-26",
        week=week,
        squad=squad,
        bank=2.0,
        free_transfers=1,
        forecasts=forecasts,
        actual_points=actual_points,
        actual_minutes=actual_minutes,
    )


def _make_env(horizon=3):
    return PlanEpisodeEnv([_make_week(12 + i) for i in range(horizon)])


def test_parse_plan_pads_truncates_and_clips():
    plan = parse_plan(json.dumps([{"soft_knee": 5.0}, {"transfer_aggressiveness": -3}]), 3)
    assert len(plan) == 3
    assert plan[0].soft_knee == 0.95            # clipped high
    assert plan[1].transfer_aggressiveness == 0.0  # clipped low
    assert plan[2] == PlanAction()              # padded default
    long = parse_plan(json.dumps([{} for _ in range(9)]), 3)
    assert len(long) == 3


def test_parse_plan_passes_chips_through_and_handles_garbage():
    # parse_plan no longer dedups chip requests itself — it has no week/half
    # context, so legality (once per half-season) is enforced by
    # PlanEpisodeEnv.rollout() instead, which does know each week's half.
    plan = parse_plan(
        json.dumps([
            {"chip_play": "bench_boost"},
            {"chip_play": "bench_boost"},
            {"chip_play": "triple_captain"},
        ]),
        3,
    )
    assert [action.chip_play for action in plan] == ["bench_boost", "bench_boost", "triple_captain"]
    assert parse_plan("no json here at all", 3) is None
    fenced = parse_plan("```json\n[{}, {}]\n```", 3)
    assert fenced is not None and len(fenced) == 3


def test_rollout_masks_duplicate_chip_within_same_half():
    env = _make_env()  # weeks 12,13,14 — all half 1 (<=19)
    plan = parse_plan(
        json.dumps([{"chip_play": "bench_boost"}, {"chip_play": "bench_boost"}, {}]),
        env.horizon,
    )
    _, details = env.rollout(plan)
    assert [d["chip"] for d in details] == ["bench_boost", "none", "none"]
    assert env.chips_used_in_rollout == {1: {"bench_boost"}, 2: set()}


def test_default_plan_matches_baseline_and_zero_reward():
    env = _make_env()
    results = env.evaluate_group([json.dumps([{} for _ in range(env.horizon)])])
    assert results[0].reward == 0.0
    assert results[0].realized_total == env.baseline_total()


def test_bench_boost_adds_bench_points():
    env = _make_env()
    boosted = [{"chip_play": "bench_boost"}] + [{} for _ in range(env.horizon - 1)]
    total, details = env.rollout(parse_plan(json.dumps(boosted), env.horizon))
    # 4 bench players x 2.0 actual each = +8 over baseline (bench ids vary,
    # but every non-starter scored 2.0 in the fixture).
    assert total - env.baseline_total() == 8.0
    assert details[0]["chip"] == "bench_boost"


def test_triple_captain_adds_one_captain_share():
    env = _make_env()
    plan = parse_plan(
        json.dumps([{"chip_play": "triple_captain", "captain_pick": 15}] + [{} for _ in range(env.horizon - 1)]),
        env.horizon,
    )
    total, _ = env.rollout(plan)
    base_plan = parse_plan(json.dumps([{"captain_pick": 15}] + [{} for _ in range(env.horizon - 1)]), env.horizon)
    base_total, _ = env.rollout(base_plan)
    assert total - base_total == 12.0  # captain's actual counted once more


def test_banking_rolls_free_transfer():
    env = _make_env()
    plan = parse_plan(
        json.dumps([{"bank_transfer": True}] + [{} for _ in range(env.horizon - 1)]),
        env.horizon,
    )
    _, details = env.rollout(plan)
    assert details[0]["banked"] is True
    assert details[0]["transfer"] is None


def test_group_normalized_advantages():
    env = _make_env()
    default = json.dumps([{} for _ in range(env.horizon)])
    boosted = json.dumps([{"chip_play": "bench_boost"}] + [{} for _ in range(env.horizon - 1)])
    results = env.evaluate_group([default, boosted, "garbage"])
    rewards = [result.reward for result in results]
    assert rewards[1] > rewards[0] > rewards[2]
    assert abs(sum(result.advantage for result in results)) < 1e-6


def test_chip_replay_illegal_across_season_budget_is_downgraded():
    env = _make_env()  # weeks 12,13,14 — half 1 only
    env.available_chips = {1: frozenset(), 2: frozenset(CHIPS)}  # half-1 budget already spent
    plan = parse_plan(
        json.dumps([{"chip_play": "bench_boost"}] + [{} for _ in range(env.horizon - 1)]),
        env.horizon,
    )
    total, details = env.rollout(plan)
    assert total == env.baseline_total()  # illegal replay masked to "none", no bench bonus
    assert details[0]["chip"] == "none"
    assert env.chips_used_in_rollout == {1: set(), 2: set()}


def test_chip_used_in_one_window_is_illegal_in_the_next_same_half():
    # Simulates composed sequential-window scoring (run_grpo_plan_eval.py):
    # a chip spent in window 1 must not be replayable in window 2, even
    # though they're separate PlanEpisodeEnv instances / separate responses
    # — as long as both windows are in the same half-season.
    window1 = _make_env()  # weeks 12,13,14 — half 1
    plan1 = parse_plan(
        json.dumps([{"chip_play": "bench_boost"}] + [{} for _ in range(window1.horizon - 1)]),
        window1.horizon,
    )
    window1.rollout(plan1)
    assert window1.chips_used_in_rollout == {1: {"bench_boost"}, 2: set()}
    remaining = {
        1: window1.available_chips[1] - window1.chips_used_in_rollout[1],
        2: window1.available_chips[2] - window1.chips_used_in_rollout[2],
    }

    window2 = PlanEpisodeEnv([_make_week(15 + i) for i in range(3)], available_chips=remaining)  # weeks 15-17, still half 1
    plan2 = parse_plan(
        json.dumps([{"chip_play": "bench_boost"}] + [{} for _ in range(window2.horizon - 1)]),
        window2.horizon,
    )
    total, details = window2.rollout(plan2)
    assert total == window2.baseline_total()  # bench_boost illegal this window, masked to none
    assert details[0]["chip"] == "none"
    assert window2.chips_used_in_rollout == {1: set(), 2: set()}


def test_chip_renews_in_second_half_after_first_half_use():
    # The core new behavior: bench_boost used in GW19 (half 1) is legal
    # AGAIN in GW20 (half 2) — two independent copies, one per half.
    env = PlanEpisodeEnv([_make_week(w) for w in (18, 19, 20, 21)])
    plan = parse_plan(
        json.dumps(
            [{}, {"chip_play": "bench_boost"}, {"chip_play": "bench_boost"}, {}]
        ),
        env.horizon,
    )
    _, details = env.rollout(plan)
    assert [d["chip"] for d in details] == ["none", "bench_boost", "bench_boost", "none"]
    assert env.chips_used_in_rollout == {1: {"bench_boost"}, 2: {"bench_boost"}}


def test_state_prompt_describes_both_halves_when_window_straddles():
    env = PlanEpisodeEnv([_make_week(w) for w in (18, 19, 20, 21)])
    prompt = env.state_prompt()
    assert "GW1-19" in prompt
    assert "GW20-38" in prompt


def test_build_episodes_overlap_and_season_split():
    weeks = [_make_week(w) for w in range(12, 24)]
    episodes = build_episodes(weeks, horizon=6, stride=3)
    assert len(episodes) == 3  # starts at 12, 15, 18
    assert all(env.horizon == 6 for env in episodes)
    prompt = episodes[0].state_prompt()
    assert "horizon 6 weeks" in prompt
    assert "chip_play" in prompt
    assert "GW17" in prompt  # outlook covers the window
    assert "transfer_pick" in prompt  # G3 action documented in the schema


def test_transfer_pick_parses_and_clips():
    plan = parse_plan(
        json.dumps([{"transfer_pick": 2}, {"transfer_pick": 7}, {"transfer_pick": "junk"}]),
        3,
    )
    assert plan[0].transfer_pick == 2
    assert plan[1].transfer_pick == 2  # clipped to MAX_TRANSFER_CANDIDATES-1
    assert plan[2].transfer_pick == 0  # unparseable -> default (old behavior)


def test_transfer_pick_default_matches_pre_g3_behavior():
    # transfer_pick=0 must reproduce the old top-1 recommender behavior
    # exactly: the all-defaults plan stays reward-neutral vs baseline.
    env = _make_env()
    results = env.evaluate_group([json.dumps([{} for _ in range(env.horizon)])])
    assert results[0].reward == 0.0

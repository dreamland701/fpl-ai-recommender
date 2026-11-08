"""G4: reward environment for RL on the forecast layer.

The policy is the residual forecast adapter itself (prompt = one player's
E11 prompt, completion = bounded delta JSON). Reward is DECISION VALUE:
swap the sampled delta into the classic forecast pool for that week, run
the deterministic decision function (best free transfer if it projects a
gain, then lineup + captain), and score the realized points of the
resulting XI. Group-relative advantages (TRL GRPO) then reward deltas that
improve the week's decision and ignore players nowhere near a boundary.

Reference pool = pure classic forecasts (no other player's deltas): leak-
free, and the policy never conditions on other players anyway, so the
mismatch vs deployment (where all players carry deltas) only shifts where
boundaries sit, not what the policy sees. Logged rewards: absolute realized
and realized-minus-classic (identical advantages; the latter is readable).
"""
from __future__ import annotations

import json
import re
from typing import Dict, List, Optional, Sequence, Tuple

from .decision import DEFAULT_DECISION_WEIGHTS, DecisionWeights, _optimize_lineup, recommend_actions
from .grpo_env import WeeklyState
from .llm_adjust import apply_llm_deltas
from .types import SquadPlayer, SquadState

DELTA_BOUNDS = {
    "delta_points_1gw": 2.0,
    "delta_points_3gw": 4.0,
    "delta_points_5gw": 6.0,
    "delta_minutes_1gw": 20.0,
    "delta_appearance_probability": 0.25,
}
UNPARSEABLE_REWARD = -1.0


def parse_delta_completion(text: str) -> Optional[Dict[str, float]]:
    text = (text or "").strip()
    parsed = None
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{[^{}]*\}", text)
        if match:
            try:
                parsed = json.loads(match.group(0))
            except json.JSONDecodeError:
                parsed = None
    if not isinstance(parsed, dict):
        return None
    deltas: Dict[str, float] = {}
    for key, bound in DELTA_BOUNDS.items():
        try:
            value = float(parsed.get(key, 0.0) or 0.0)
        except (TypeError, ValueError):
            return None
        deltas[key] = max(-bound, min(bound, value))
    return deltas


def realized_points_for_forecasts(
    state: WeeklyState, forecasts: Sequence, weights: DecisionWeights = DEFAULT_DECISION_WEIGHTS
) -> Tuple[float, Dict[str, object]]:
    """Single-week decision + realized score, mirroring PlanEpisodeEnv._week_realized
    with the default action (take the best 1-transfer if it projects > 0)."""
    forecast_by_id = {f.player_id: f for f in forecasts}
    squad: List[SquadPlayer] = list(state.squad)
    bank = state.bank
    hit = 0
    squad_state = SquadState(
        season=state.season, week=state.week, squad_players=squad,
        bank=bank, free_transfers=state.free_transfers, chips_available={},
    )
    bundle = recommend_actions(
        squad_state=squad_state, forecasts=list(forecasts),
        top_n_transfers=1, max_transfers_considered=1, decision_weights=weights,
    )
    transfer = None
    if bundle.transfers and bundle.transfers[0].projected_gain > 0:
        transfer = bundle.transfers[0]
        hit = transfer.hit_cost
        outgoing = {p.player_id for p in squad if p.player_id in set(transfer.players_out)}
        squad = [p for p in squad if p.player_id not in outgoing]
        for pid in transfer.players_in:
            f = forecast_by_id[pid]
            squad.append(SquadPlayer(player_id=f.player_id, player_name=f.player_name, team_id=f.team_id,
                                     position=f.position, sell_price=f.price))
    starters, bench, captain_id, vice_id, _ = _optimize_lineup(squad, forecast_by_id, weights)
    minutes, actual = state.actual_minutes, state.actual_points
    effective_captain = captain_id if minutes.get(captain_id, 0.0) > 0 else (
        vice_id if minutes.get(vice_id, 0.0) > 0 else captain_id
    )
    realized = sum(actual.get(p, 0.0) for p in starters) + actual.get(effective_captain, 0.0) - hit
    return realized, {
        "transfer": None if transfer is None else (list(transfer.players_out), list(transfer.players_in)),
        "captain": captain_id, "starters": list(starters),
    }


class ForecastRewardEnv:
    """One week-state; rewards a single player's sampled delta by marginal decision value."""

    def __init__(self, state: WeeklyState, weights: DecisionWeights = DEFAULT_DECISION_WEIGHTS,
                 pool_size: int = 30, captain_pool: int = 10):
        self.state = state
        self.weights = weights
        self.classic_realized, self.classic_detail = realized_points_for_forecasts(state, state.forecasts, weights)
        squad_ids = {p.player_id for p in state.squad}
        non_squad = [f for f in state.forecasts if f.player_id not in squad_ids]
        by_horizon = sorted(non_squad, key=weights.horizon_points, reverse=True)[:pool_size]
        by_1gw = sorted(state.forecasts, key=lambda f: f.predicted_points_1gw, reverse=True)[:captain_pool]
        self.relevant_players: List[int] = sorted(squad_ids | {f.player_id for f in by_horizon} | {f.player_id for f in by_1gw})

    @property
    def key(self) -> str:
        return f"{self.state.season}:{self.state.week}"

    def reward(self, player_id: int, completion: str) -> Tuple[float, float, bool]:
        """Returns (reward_relative_to_classic, realized_absolute, parsed_ok)."""
        deltas = parse_delta_completion(completion)
        if deltas is None:
            return UNPARSEABLE_REWARD, float("nan"), False
        lookup = {(int(self.state.week), int(player_id)): deltas}
        forecasts = apply_llm_deltas(self.state.forecasts, lookup, self.state.week, fields="all")
        realized, _ = realized_points_for_forecasts(self.state, forecasts, self.weights)
        return realized - self.classic_realized, realized, True

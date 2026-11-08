"""Weekly-bandit GRPO environment for decision-layer RL (Phase 1 scaffold).

Design (per docs/decision_layer_plan_2026_07_09.md §4 and Wes's 2026-07-10
spec): each gameweek is an independent bandit round. The state is the classic
baseline squad at week W; the policy (Gemma + LoRA) emits G bounded JSON
actions parameterizing the deterministic optimizer (`DecisionWeights` plus a
captain pick and transfer aggressiveness); each action is rolled through the
optimizer and scored on realized points; the reward is paired against the
classic baseline's realized points on the same state, and advantages are
group-normalized. The next state resets to the classic trajectory, so a bad
sampled decision never cascades.

This module is the environment only — deliberately free of TRL/model
dependencies so it unit-tests on CPU in milliseconds. The GRPO training loop
(post-GW1 per the approved sequence) will wrap `WeeklyBanditEnv` with TRL's
GRPOTrainer: `state_prompt` is the query, `evaluate_group` is the reward
function.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from typing import Dict, List, Mapping, Optional, Sequence

from .decision import DecisionWeights, _optimize_lineup, recommend_actions
from .llm_adjust import _extract_first_json_object
from .types import PlayerForecast, SquadPlayer, SquadState

ACTION_BOUNDS = {
    "soft_knee": (0.60, 0.95),
    "transfer_aggressiveness": (0.0, 2.0),
}
# min projected gain required to make the week's transfer, as a function of
# aggressiveness: 0.0 -> needs +2.0, 2.0 -> any positive gain.
BASE_TRANSFER_GAIN_THRESHOLD = 2.0


@dataclass(frozen=True)
class DecisionAction:
    """A bounded, parsed policy action. Every field has a safe default, so a
    default-constructed action reproduces the classic baseline decision."""

    horizon: str = "3gw"
    availability: str = "threshold"
    soft_knee: float = 0.80
    transfer_aggressiveness: float = 2.0
    captain_pick: Optional[int] = None

    def weights(self) -> DecisionWeights:
        return DecisionWeights(
            horizon=self.horizon,
            availability=self.availability,
            soft_availability_knee=self.soft_knee,
        )

    def min_projected_gain(self) -> float:
        return max(0.0, BASE_TRANSFER_GAIN_THRESHOLD - self.transfer_aggressiveness)


def parse_action(text: str) -> Optional[DecisionAction]:
    """Parse a policy response into a clipped action; None if unusable.

    Unknown keys are ignored; out-of-range values are clipped, not rejected —
    the optimizer must stay in charge of legality, the policy only nudges.
    """
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        extracted = _extract_first_json_object(text)
        if extracted is None:
            return None
        try:
            parsed = json.loads(extracted)
        except json.JSONDecodeError:
            return None
    if not isinstance(parsed, dict):
        return None

    horizon = parsed.get("horizon", "3gw")
    if horizon not in {"3gw", "blend5"}:
        horizon = "3gw"
    availability = parsed.get("availability", "threshold")
    if availability not in {"threshold", "soft"}:
        availability = "threshold"

    def _clipped(key: str, default: float) -> float:
        low, high = ACTION_BOUNDS[key]
        try:
            value = float(parsed.get(key, default))
        except (TypeError, ValueError):
            return default
        return max(low, min(high, value))

    captain_pick = parsed.get("captain_pick")
    try:
        captain_pick = int(captain_pick) if captain_pick is not None else None
    except (TypeError, ValueError):
        captain_pick = None

    return DecisionAction(
        horizon=horizon,
        availability=availability,
        soft_knee=_clipped("soft_knee", 0.80),
        transfer_aggressiveness=_clipped("transfer_aggressiveness", 2.0),
        captain_pick=captain_pick,
    )


@dataclass(frozen=True)
class WeeklyState:
    """One bandit round: the classic trajectory's squad state at week W plus
    that week's forecasts and (for reward computation) realized points.

    llm_deltas / evidence_snippets are present only in LLM-adjusted caches
    (build_adjusted_grpo_states.py): per-player {"d1": Δpoints_1gw, "dP":
    ΔP(appear)} and a short scout-text snippet — the distilled text signal
    surfaced to the decision policy."""

    season: str
    week: int
    squad: Sequence[SquadPlayer]
    bank: float
    free_transfers: int
    forecasts: Sequence[PlayerForecast]
    actual_points: Mapping[int, float]
    actual_minutes: Mapping[int, float]
    llm_deltas: Mapping[int, Mapping[str, float]] = field(default_factory=dict)
    evidence_snippets: Mapping[int, str] = field(default_factory=dict)


def load_states(path) -> List[WeeklyState]:
    """Load weekly states from a build_grpo_state_cache.py JSONL file."""
    states: List[WeeklyState] = []
    with open(path) as handle:
        for line in handle:
            row = json.loads(line)
            states.append(
                WeeklyState(
                    season=row["season"],
                    week=int(row["week"]),
                    squad=[SquadPlayer(**player) for player in row["squad"]],
                    bank=float(row["bank"]),
                    free_transfers=int(row["free_transfers"]),
                    forecasts=[
                        PlayerForecast(season=row["season"], week=int(row["week"]), **forecast)
                        for forecast in row["forecasts"]
                    ],
                    actual_points={int(k): v for k, v in row["actual_points"].items()},
                    actual_minutes={int(k): v for k, v in row["actual_minutes"].items()},
                    llm_deltas={int(k): v for k, v in (row.get("llm_deltas") or {}).items()},
                    evidence_snippets={int(k): v for k, v in (row.get("evidence_snippets") or {}).items()},
                )
            )
    return states


@dataclass
class RolloutResult:
    action: Optional[DecisionAction]
    realized_points: float
    reward: float  # realized - classic baseline realized (paired)
    advantage: float = 0.0
    detail: Dict[str, object] = field(default_factory=dict)


class WeeklyBanditEnv:
    """Evaluates groups of policy actions against one weekly state."""

    def __init__(self, state: WeeklyState):
        self.state = state
        self._forecast_by_id = {forecast.player_id: forecast for forecast in state.forecasts}
        self._baseline_realized: Optional[float] = None

    # ---- prompt -----------------------------------------------------------

    def state_prompt(self, top_n_candidates: int = 30) -> str:
        """Compact weekly decision state for the policy. Candidates are the
        top forecasts outside the squad (transfer targets) plus the squad."""
        squad_ids = {player.player_id for player in self.state.squad}
        candidates = sorted(
            (f for f in self.state.forecasts if f.player_id not in squad_ids),
            key=lambda f: f.predicted_points_3gw,
            reverse=True,
        )[:top_n_candidates]

        def _row(forecast: PlayerForecast) -> str:
            return (
                f"{forecast.player_id}|{forecast.player_name}|{forecast.position}|£{forecast.price:.1f}"
                f"|1gw {forecast.predicted_points_1gw:.1f}|3gw {forecast.predicted_points_3gw:.1f}"
                f"|P(app) {forecast.appearance_probability:.2f}"
            )

        squad_lines = "\n".join(
            _row(self._forecast_by_id[p.player_id]) for p in self.state.squad if p.player_id in self._forecast_by_id
        )
        candidate_lines = "\n".join(_row(f) for f in candidates)
        return (
            f"FPL decision state — {self.state.season} GW{self.state.week}\n"
            f"Bank: {self.state.bank:.1f} | Free transfers: {self.state.free_transfers}\n"
            f"Current squad (id|name|pos|price|forecasts):\n{squad_lines}\n"
            f"Top transfer candidates:\n{candidate_lines}\n\n"
            "Output strict JSON: {\"horizon\": \"3gw\"|\"blend5\", \"availability\": \"threshold\"|\"soft\", "
            "\"soft_knee\": 0.6-0.95, \"transfer_aggressiveness\": 0.0-2.0, \"captain_pick\": <player_id|null>}\n"
            "Respond with only the JSON object on a single line — no markdown fences, no explanation."
        )

    # ---- rollout ----------------------------------------------------------

    def _realized_for_action(self, action: DecisionAction) -> tuple[float, Dict[str, object]]:
        weights = action.weights()
        squad_state = SquadState(
            season=self.state.season,
            week=self.state.week,
            squad_players=list(self.state.squad),
            bank=self.state.bank,
            free_transfers=self.state.free_transfers,
            chips_available={},
        )
        bundle = recommend_actions(
            squad_state=squad_state,
            forecasts=self.state.forecasts,
            top_n_transfers=1,
            max_transfers_considered=1,
            decision_weights=weights,
        )
        squad = list(self.state.squad)
        hit_cost = 0
        transfer = None
        if bundle.transfers and bundle.transfers[0].projected_gain >= action.min_projected_gain():
            transfer = bundle.transfers[0]
            hit_cost = transfer.hit_cost
            outgoing = set(transfer.players_out)
            squad = [player for player in squad if player.player_id not in outgoing]
            for player_id in transfer.players_in:
                forecast = self._forecast_by_id[player_id]
                squad.append(
                    SquadPlayer(
                        player_id=forecast.player_id,
                        player_name=forecast.player_name,
                        team_id=forecast.team_id,
                        position=forecast.position,
                        sell_price=forecast.price,
                    )
                )

        forecast_by_id = dict(self._forecast_by_id)
        starters, _bench, captain_id, vice_captain_id, _ = _optimize_lineup(squad, forecast_by_id, weights)
        if action.captain_pick is not None and action.captain_pick in starters:
            captain_id = action.captain_pick

        actual = self.state.actual_points
        minutes = self.state.actual_minutes
        effective_captain = captain_id if minutes.get(captain_id, 0.0) > 0 else (
            vice_captain_id if minutes.get(vice_captain_id, 0.0) > 0 else captain_id
        )
        realized = (
            sum(actual.get(player_id, 0.0) for player_id in starters)
            + actual.get(effective_captain, 0.0)
            - hit_cost
        )
        detail = {
            "transfer": None if transfer is None else (list(transfer.players_out), list(transfer.players_in)),
            "captain_id": captain_id,
            "hit_cost": hit_cost,
        }
        return float(realized), detail

    def baseline_realized(self) -> float:
        """Realized points of the classic decision (default action) on this state."""
        if self._baseline_realized is None:
            self._baseline_realized, _ = self._realized_for_action(DecisionAction())
        return self._baseline_realized

    def evaluate_group(self, responses: Sequence[str]) -> List[RolloutResult]:
        """Roll a group of policy responses; rewards paired vs the classic
        baseline; advantages group-normalized (GRPO-style)."""
        baseline = self.baseline_realized()
        results: List[RolloutResult] = []
        for response in responses:
            action = parse_action(response)
            if action is None:
                # Unparseable output scores as the baseline with a small
                # penalty so "emit garbage" is never advantageous.
                results.append(RolloutResult(action=None, realized_points=baseline, reward=-1.0))
                continue
            realized, detail = self._realized_for_action(action)
            results.append(
                RolloutResult(action=action, realized_points=realized, reward=realized - baseline, detail=detail)
            )

        rewards = [result.reward for result in results]
        mean = sum(rewards) / len(rewards)
        variance = sum((reward - mean) ** 2 for reward in rewards) / len(rewards)
        std = math.sqrt(variance)
        for result in results:
            result.advantage = (result.reward - mean) / std if std > 1e-9 else 0.0
        return results

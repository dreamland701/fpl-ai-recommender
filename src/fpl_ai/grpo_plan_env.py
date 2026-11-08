"""Plan-horizon GRPO environment for decision-layer RL (G2).

Design (extends docs/decision_layer_plan_2026_07_09.md §4; Wes approved the
G2 direction 2026-07-18): TRL 1.0's GRPOTrainer is single-turn, so instead
of interactive weekly rollouts the policy emits a K-week *plan* in one
completion — a JSON array of bounded weekly actions (G1's knobs plus
explicit free-transfer banking and chip timing). The environment rolls the
plan forward through K chained weekly states: the squad, bank, and free
transfers evolve under the policy's own choices (unlike G1's
reset-to-baseline), each chip is playable at most once per episode, and the
episode reward is the cumulative realized points minus the same-window
cumulative of the all-defaults plan (sequential paired baseline). This is
exactly the multi-step credit G1's bandit could not express: banking a
transfer, timing a chip for a double-gameweek, sequencing transfers.

Like grpo_env.py this module is TRL/model-free and unit-tests on CPU.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, replace
from typing import Dict, List, Optional, Sequence

from .decision import _optimize_lineup, recommend_actions
from .grpo_env import (
    ACTION_BOUNDS,
    BASE_TRANSFER_GAIN_THRESHOLD,
    DecisionAction,
    WeeklyState,
    _extract_first_json_object,
)
from .types import PlayerForecast, SquadPlayer, SquadState

CHIPS = ("bench_boost", "triple_captain")
MAX_FREE_TRANSFERS = 2
TRANSFER_HIT_COST = 4
# Since 2023-24 each of bench_boost/triple_captain has two independent
# copies per season: one legal GW1-19, one legal GW20-38 — the second
# renews at GW20 regardless of whether the first-half copy was used.
FIRST_HALF_LAST_WEEK = 19


def chip_half(week: int) -> int:
    return 1 if week <= FIRST_HALF_LAST_WEEK else 2


MAX_TRANSFER_CANDIDATES = 3


@dataclass(frozen=True)
class PlanAction(DecisionAction):
    """One week of a plan: G1's bounded knobs plus banking and chip timing.

    G3 adds transfer_pick: which of the recommender's top-K legal candidate
    transfers to execute (0 = its top pick, matching all prior behavior).
    This is the first rung where the policy chooses squad COMPOSITION
    rather than only gating the greedy recommender — multi-week transfer
    planning (building toward a fixture swing, assembling rotation value)
    was architecturally inexpressible before this field existed."""

    bank_transfer: bool = False
    chip_play: str = "none"
    transfer_pick: int = 0


def _parse_week_entry(parsed: object) -> PlanAction:
    """Clip one plan entry to a PlanAction; anything unusable becomes the
    default (baseline) action for that week — never rejected outright."""
    if not isinstance(parsed, dict):
        return PlanAction()

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

    chip_play = parsed.get("chip_play", "none")
    if chip_play not in CHIPS:
        chip_play = "none"

    try:
        transfer_pick = int(parsed.get("transfer_pick", 0))
    except (TypeError, ValueError):
        transfer_pick = 0
    transfer_pick = max(0, min(MAX_TRANSFER_CANDIDATES - 1, transfer_pick))

    return PlanAction(
        horizon=horizon,
        availability=availability,
        soft_knee=_clipped("soft_knee", 0.80),
        transfer_aggressiveness=_clipped("transfer_aggressiveness", 2.0),
        captain_pick=captain_pick,
        bank_transfer=bool(parsed.get("bank_transfer", False)),
        chip_play=chip_play,
        transfer_pick=transfer_pick,
    )


def parse_plan(text: str, horizon_weeks: int) -> Optional[List[PlanAction]]:
    """Parse a policy response into exactly horizon_weeks clipped actions.

    Accepts either a bare JSON array or {"weeks": [...]}. Short plans are
    padded with defaults, long plans truncated. None only if no JSON
    structure is recoverable at all (same contract as G1's parse_action).

    Chip-play legality (each chip once per half-season, not once per plan —
    a plan CAN legally request e.g. bench_boost in both GW19 and GW20, one
    per half) is NOT enforced here: this function has no week/half context.
    Illegal or duplicate chip requests are downgraded to "none" by
    PlanEpisodeEnv.rollout(), which does have the real per-week half.
    """
    parsed: object = None
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("[")
        end = text.rfind("]")
        if start != -1 and end > start:
            try:
                parsed = json.loads(text[start : end + 1])
            except json.JSONDecodeError:
                parsed = None
        if parsed is None:
            extracted = _extract_first_json_object(text)
            if extracted is not None:
                try:
                    parsed = json.loads(extracted)
                except json.JSONDecodeError:
                    parsed = None
    if parsed is None:
        return None
    if isinstance(parsed, dict):
        parsed = parsed.get("weeks", [parsed])
    if not isinstance(parsed, list):
        return None

    actions = [_parse_week_entry(entry) for entry in parsed[:horizon_weeks]]
    actions += [PlanAction()] * (horizon_weeks - len(actions))
    return actions


@dataclass
class PlanRolloutResult:
    plan: Optional[List[PlanAction]]
    realized_total: float
    reward: float  # cumulative realized - sequential baseline cumulative
    advantage: float = 0.0
    detail: List[Dict[str, object]] = field(default_factory=list)


class PlanEpisodeEnv:
    """Rolls K-week plans through chained weekly states.

    `states` must be consecutive cache entries from one season. Forecasts and
    realized points for week i always come from states[i]; the squad, bank,
    and free transfers are carried forward from the policy's own choices.
    """

    def __init__(
        self,
        states: Sequence[WeeklyState],
        available_chips: Optional[Dict[int, frozenset]] = None,
    ):
        assert len(states) >= 2, "an episode needs at least two weeks"
        assert len({state.season for state in states}) == 1, "episode spans one season"
        self.states = list(states)
        self.horizon = len(self.states)
        self._baseline: Optional[float] = None
        # Chips still legal to play, per half-season (1 = GW<=19, 2 =
        # GW>=20 — each chip has one independent copy per half, the second
        # renewing at GW20 regardless of first-half usage). Defaults to a
        # fresh budget both halves — the training curriculum's per-episode
        # assumption. Callers composing sequential windows across a real
        # season (eval/deployment) must thread the season-remaining budget
        # through explicitly, per half; see build_episodes' docstring and
        # run_grpo_plan_eval.py's season-level bookkeeping.
        available_chips = available_chips or {}
        self.available_chips: Dict[int, frozenset] = {
            1: frozenset(available_chips.get(1, CHIPS)),
            2: frozenset(available_chips.get(2, CHIPS)),
        }
        self.chips_used_in_rollout: Dict[int, set] = {1: set(), 2: set()}

    # ---- rollout ----------------------------------------------------------

    def _week_realized(
        self,
        state: WeeklyState,
        squad: List[SquadPlayer],
        bank: float,
        free_transfers: int,
        action: PlanAction,
    ) -> tuple[float, List[SquadPlayer], float, int, Dict[str, object]]:
        forecast_by_id = {forecast.player_id: forecast for forecast in state.forecasts}
        weights = action.weights()
        transfer = None
        hit_cost = 0

        if not action.bank_transfer:
            squad_state = SquadState(
                season=state.season,
                week=state.week,
                squad_players=list(squad),
                bank=bank,
                free_transfers=free_transfers,
                chips_available={},
            )
            bundle = recommend_actions(
                squad_state=squad_state,
                forecasts=state.forecasts,
                top_n_transfers=MAX_TRANSFER_CANDIDATES,
                max_transfers_considered=1,
                decision_weights=weights,
            )
            # G3: the policy indexes into the top-K legal candidates
            # (clamped to what actually exists this week). pick 0 is the
            # recommender's own top choice — exactly the pre-G3 behavior.
            if bundle.transfers:
                pick = min(action.transfer_pick, len(bundle.transfers) - 1)
                candidate_transfer = bundle.transfers[pick]
            else:
                candidate_transfer = None
            if candidate_transfer is not None and candidate_transfer.projected_gain >= action.min_projected_gain():
                transfer = candidate_transfer
                hit_cost = transfer.hit_cost
                outgoing = {player.player_id: player for player in squad if player.player_id in set(transfer.players_out)}
                squad = [player for player in squad if player.player_id not in outgoing]
                bank += sum(player.sell_price for player in outgoing.values())
                bank -= sum(forecast_by_id[player_id].price for player_id in transfer.players_in)
                for player_id in transfer.players_in:
                    forecast = forecast_by_id[player_id]
                    squad.append(
                        SquadPlayer(
                            player_id=forecast.player_id,
                            player_name=forecast.player_name,
                            team_id=forecast.team_id,
                            position=forecast.position,
                            sell_price=forecast.price,
                        )
                    )

        # FPL free-transfer rule: making a transfer consumes one FT (or takes
        # a hit at zero); holding rolls one over, capped at MAX_FREE_TRANSFERS.
        if transfer is None:
            next_free_transfers = min(MAX_FREE_TRANSFERS, free_transfers + 1)
        else:
            next_free_transfers = max(0, free_transfers - 1) + 1
            next_free_transfers = min(MAX_FREE_TRANSFERS, next_free_transfers)

        starters, bench, captain_id, vice_captain_id, _ = _optimize_lineup(squad, forecast_by_id, weights)
        if action.captain_pick is not None and action.captain_pick in starters:
            captain_id = action.captain_pick

        actual = state.actual_points
        minutes = state.actual_minutes
        effective_captain = captain_id if minutes.get(captain_id, 0.0) > 0 else (
            vice_captain_id if minutes.get(vice_captain_id, 0.0) > 0 else captain_id
        )
        captain_multiplier = 3 if action.chip_play == "triple_captain" else 2
        realized = (
            sum(actual.get(player_id, 0.0) for player_id in starters)
            + (captain_multiplier - 1) * actual.get(effective_captain, 0.0)
            - hit_cost
        )
        if action.chip_play == "bench_boost":
            realized += sum(actual.get(player_id, 0.0) for player_id in bench)

        detail = {
            "week": state.week,
            "transfer": None if transfer is None else (list(transfer.players_out), list(transfer.players_in)),
            "banked": action.bank_transfer,
            "chip": action.chip_play,
            "captain_id": captain_id,
            "hit_cost": hit_cost,
            "realized": realized,
        }
        return float(realized), squad, bank, next_free_transfers, detail

    def rollout(self, plan: Sequence[PlanAction]) -> tuple[float, List[Dict[str, object]]]:
        assert len(plan) == self.horizon
        squad = list(self.states[0].squad)
        bank = self.states[0].bank
        free_transfers = self.states[0].free_transfers
        total = 0.0
        details: List[Dict[str, object]] = []
        remaining = {1: set(self.available_chips[1]), 2: set(self.available_chips[2])}
        for state, action in zip(self.states, plan):
            half = chip_half(state.week)
            if action.chip_play in CHIPS and action.chip_play not in remaining[half]:
                # Illegal replay of a chip already spent this half-season
                # (earlier this window or in a prior one) — downgrade
                # silently, same contract as the old within-plan dedup, but
                # now scoped per half rather than per season.
                action = replace(action, chip_play="none")
            elif action.chip_play in CHIPS:
                remaining[half].discard(action.chip_play)
            realized, squad, bank, free_transfers, detail = self._week_realized(
                state, squad, bank, free_transfers, action
            )
            total += realized
            details.append(detail)
        self.chips_used_in_rollout = {
            1: set(self.available_chips[1]) - remaining[1],
            2: set(self.available_chips[2]) - remaining[2],
        }
        return total, details

    def baseline_total(self) -> float:
        """Cumulative realized points of the all-defaults plan (the classic
        sequential trajectory over this window, no chips)."""
        if self._baseline is None:
            self._baseline, _ = self.rollout([PlanAction()] * self.horizon)
        return self._baseline

    # ---- prompt -----------------------------------------------------------

    def state_prompt(self, top_n_candidates: int = 20, max_snippets: int = 10) -> str:
        start = self.states[0]
        forecast_by_id = {forecast.player_id: forecast for forecast in start.forecasts}
        squad_ids = {player.player_id for player in start.squad}
        candidates = sorted(
            (f for f in start.forecasts if f.player_id not in squad_ids),
            key=lambda f: f.predicted_points_3gw,
            reverse=True,
        )[:top_n_candidates]

        def _row(forecast: PlayerForecast) -> str:
            # Δ1gw = how much the scout-evidence adapter moved this player
            # (present only with LLM-adjusted state caches).
            delta = start.llm_deltas.get(forecast.player_id)
            delta_txt = f"|Δ1gw {delta['d1']:+.1f}" if delta and delta.get("d1") else ""
            return (
                f"{forecast.player_id}|{forecast.player_name}|{forecast.position}|£{forecast.price:.1f}"
                f"|1gw {forecast.predicted_points_1gw:.1f}|3gw {forecast.predicted_points_3gw:.1f}"
                f"|P(app) {forecast.appearance_probability:.2f}{delta_txt}"
            )

        squad_lines = "\n".join(
            _row(forecast_by_id[p.player_id]) for p in start.squad if p.player_id in forecast_by_id
        )
        candidate_lines = "\n".join(_row(f) for f in candidates)

        # Per-week outlook: the current squad's projected 1GW total under
        # each future week's forecasts — the signal for chip timing and
        # transfer sequencing (fixture swings show up here).
        outlook_lines = []
        for state in self.states:
            week_forecasts = {forecast.player_id: forecast for forecast in state.forecasts}
            projected = sum(
                week_forecasts[p.player_id].predicted_points_1gw
                for p in start.squad
                if p.player_id in week_forecasts
            )
            best_out = max(
                (f for f in state.forecasts if f.player_id not in squad_ids),
                key=lambda f: f.predicted_points_1gw,
                default=None,
            )
            best_txt = f" | best outside: {best_out.player_name} {best_out.predicted_points_1gw:.1f}" if best_out else ""
            outlook_lines.append(f"GW{state.week}: squad proj {projected:.0f}{best_txt}")

        # Scout notes: the raw why behind the deltas, for the most
        # decision-relevant players (squad first, then top candidates).
        snippet_lines = []
        if start.evidence_snippets:
            ordered = [p.player_id for p in start.squad] + [f.player_id for f in candidates]
            for player_id in ordered:
                text = start.evidence_snippets.get(player_id)
                if not text:
                    continue
                name = forecast_by_id[player_id].player_name if player_id in forecast_by_id else str(player_id)
                snippet_lines.append(f"- {name}: {text}")
                if len(snippet_lines) >= max_snippets:
                    break
        snippet_block = ("Scout notes:\n" + "\n".join(snippet_lines) + "\n") if snippet_lines else ""

        weeks = ", ".join(f"GW{state.week}" for state in self.states)
        halves_touched = sorted({chip_half(state.week) for state in self.states})
        half_labels = {1: "GW1-19", 2: "GW20-38 (renews at GW20 regardless of first-half usage)"}
        parts = []
        for half in halves_touched:
            avail = self.available_chips[half]
            avail_txt = ", ".join(sorted(avail)) if avail else "none left"
            parts.append(f"{half_labels[half]}: {avail_txt}")
        chips_line = "Chips still available (each usable once per half-season) — " + "; ".join(parts)

        # G3: show the recommender's actual top-K first-week transfer
        # proposals so transfer_pick=0/1/2 is an informed choice for the
        # opening week (later weeks' candidates depend on the policy's own
        # trajectory and are picked by index into whatever the recommender
        # offers then).
        squad_state = SquadState(
            season=start.season,
            week=start.week,
            squad_players=list(start.squad),
            bank=start.bank,
            free_transfers=start.free_transfers,
            chips_available={},
        )
        bundle = recommend_actions(
            squad_state=squad_state,
            forecasts=start.forecasts,
            top_n_transfers=MAX_TRANSFER_CANDIDATES,
            max_transfers_considered=1,
        )
        squad_names = {player.player_id: player.player_name for player in start.squad}

        def _name(player_id: int) -> str:
            if player_id in forecast_by_id:
                return forecast_by_id[player_id].player_name
            return squad_names.get(player_id, str(player_id))

        proposal_lines = []
        for index, suggestion in enumerate(bundle.transfers[:MAX_TRANSFER_CANDIDATES]):
            outs = ", ".join(_name(pid) for pid in suggestion.players_out) or "?"
            ins = ", ".join(_name(pid) for pid in suggestion.players_in) or "?"
            proposal_lines.append(
                f"  pick {index}: {outs} -> {ins} (proj gain {suggestion.projected_gain:+.1f}, hit {suggestion.hit_cost})"
            )
        proposals_block = (
            "First-week transfer proposals (transfer_pick indexes these; later weeks re-rank on your evolving squad):\n"
            + "\n".join(proposal_lines)
            + "\n"
        ) if proposal_lines else ""

        return (
            f"FPL plan state — {start.season}, horizon {self.horizon} weeks ({weeks})\n"
            f"Bank: {start.bank:.1f} | Free transfers: {start.free_transfers} | "
            f"{chips_line}\n"
            f"Current squad (id|name|pos|price|forecasts):\n{squad_lines}\n"
            f"Top transfer candidates this week:\n{candidate_lines}\n"
            f"{proposals_block}"
            f"{snippet_block}"
            f"Week-by-week outlook:\n" + "\n".join(outlook_lines) + "\n\n"
            f"Output a strict JSON array of exactly {self.horizon} weekly actions, one per gameweek in order. "
            "Each action: {\"horizon\": \"3gw\"|\"blend5\", \"availability\": \"threshold\"|\"soft\", "
            "\"soft_knee\": 0.6-0.95, \"transfer_aggressiveness\": 0.0-2.0, \"bank_transfer\": true|false, "
            "\"transfer_pick\": 0|1|2, "
            "\"captain_pick\": <player_id|null>, \"chip_play\": \"none\"|\"bench_boost\"|\"triple_captain\"}\n"
            "Respond with only the JSON array on a single line — no markdown fences, no explanation."
        )

    # ---- group evaluation -------------------------------------------------

    def evaluate_group(self, responses: Sequence[str]) -> List[PlanRolloutResult]:
        baseline = self.baseline_total()
        results: List[PlanRolloutResult] = []
        for response in responses:
            plan = parse_plan(response, self.horizon)
            if plan is None:
                results.append(PlanRolloutResult(plan=None, realized_total=baseline, reward=-1.0))
                continue
            realized, details = self.rollout(plan)
            results.append(
                PlanRolloutResult(plan=plan, realized_total=realized, reward=realized - baseline, detail=details)
            )
        rewards = [result.reward for result in results]
        mean = sum(rewards) / len(rewards)
        variance = sum((reward - mean) ** 2 for reward in rewards) / len(rewards)
        std = math.sqrt(variance)
        for result in results:
            result.advantage = (result.reward - mean) / std if std > 1e-9 else 0.0
        return results


def build_episodes(states: Sequence[WeeklyState], horizon: int = 6, stride: int = 3) -> List[PlanEpisodeEnv]:
    """Slice a season's consecutive cached weeks into overlapping episodes.

    Consecutive means adjacent in cache order (cache weeks are the backtest's
    decision points; gameweek numbers may skip blanks). Overlap (stride <
    horizon) multiplies training states — the squad-diversity lever."""
    by_season: Dict[str, List[WeeklyState]] = {}
    for state in states:
        by_season.setdefault(state.season, []).append(state)
    episodes: List[PlanEpisodeEnv] = []
    for season_states in by_season.values():
        ordered = sorted(season_states, key=lambda state: state.week)
        for start in range(0, len(ordered) - horizon + 1, stride):
            episodes.append(PlanEpisodeEnv(ordered[start : start + horizon]))
    return episodes

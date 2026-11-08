"""Recommendation search over forecasts and current squad state."""

from __future__ import annotations

import os

from dataclasses import dataclass, replace
from itertools import combinations
from typing import Dict, List, Sequence, Tuple

from .config import POSITION_NAME_TO_SQUAD_COUNT, STARTING_FORMATIONS
from .types import (
    CandidateDecisionOption,
    ChipAdvisory,
    EvidenceSnapshot,
    PlayerForecast,
    RecommendationBundle,
    SourceDocument,
    SquadPlayer,
    SquadState,
    TransferRecommendation,
)


@dataclass(frozen=True)
class DecisionWeights:
    """Tunable decision-layer scoring knobs (the GRPO action space later).

    horizon: transfer-evaluation points horizon — "3gw" (starter 3GW sum) or
        "blend5" (5GW + 0.6*3GW + 0.35*1GW, matching the initial-squad
        selection score so weekly transfers optimize the same objective).
    availability: "threshold" keeps the additive penalty below P=0.6;
        "soft" instead multiplies each starter's points by
        min(1, P / soft_availability_knee) — points labels are unconditional,
        so this deliberately over-discounts doubtful starters as risk aversion
        (captaincy/lineup care about downside, not unbiasedness).
    """

    horizon: str = "3gw"
    availability: str = "threshold"
    soft_availability_knee: float = 0.80
    # Multiplier on the captain bonus in _evaluate_squad. 1.0 = historical
    # behavior (captain's 1gw counted once extra). The doubling recurs every
    # week of the horizon, so ~3.0 approximates its value under the default
    # 3gw horizon — under-weighting it is how premium doubling targets lose
    # transfer evaluations to additive arithmetic (Haaland, GW2 2026-27).
    captain_leverage: float = 1.0
    # Programme item 2 (2026-10-17): fixtures of value credited beyond the horizon window (terminal value =
    # terminal_fixtures x the 5GW head's per-fixture rate). With per-fixture horizon heads a single blank
    # otherwise removes a third of a 3GW objective and makes the optimizer sell a premium for one missed week.
    terminal_fixtures: float = 0.0

    def availability_weight(self, forecast: PlayerForecast) -> float:
        if self.availability != "soft":
            return 1.0
        return min(1.0, forecast.appearance_probability / self.soft_availability_knee)

    def horizon_points(self, forecast: PlayerForecast) -> float:
        terminal = self.terminal_fixtures * float(getattr(forecast, "rate_5gw", 0.0))
        if self.horizon == "blend5":
            return (
                forecast.predicted_points_5gw
                + 0.6 * forecast.predicted_points_3gw
                + 0.35 * forecast.predicted_points_1gw
                + terminal
            )
        return forecast.predicted_points_3gw + terminal


DEFAULT_DECISION_WEIGHTS = DecisionWeights()

DECISION_VARIANTS: Dict[str, DecisionWeights] = {
    "baseline": DecisionWeights(),
    "horizon5": DecisionWeights(horizon="blend5"),
    "avail_soft": DecisionWeights(availability="soft"),
    "horizon5_avail": DecisionWeights(horizon="blend5", availability="soft"),
    "captlev2": DecisionWeights(captain_leverage=2.0),
    "captlev3": DecisionWeights(captain_leverage=3.0),
    # item 2 terminal-value horizons
    "3gw_t3": DecisionWeights(terminal_fixtures=3.0),
    "3gw_t6": DecisionWeights(terminal_fixtures=6.0),
    "blend5_t3": DecisionWeights(horizon="blend5", terminal_fixtures=3.0),
    "avail_soft_captlev3": DecisionWeights(availability="soft", captain_leverage=3.0),
}


def _forecast_lookup(forecasts: Sequence[PlayerForecast]) -> Dict[int, PlayerForecast]:
    return {forecast.player_id: forecast for forecast in forecasts}


def _zero_forecast(player: SquadPlayer, season: str, week: int) -> PlayerForecast:
    return PlayerForecast(
        season=season,
        week=week,
        player_id=player.player_id,
        player_name=player.player_name,
        team_id=player.team_id,
        position=player.position,
        price=player.sell_price,
        predicted_minutes=0.0,
        predicted_points_1gw=0.0,
        predicted_points_3gw=0.0,
        predicted_points_5gw=0.0,
        appearance_probability=0.0,
        fixture_count=0,
        uncertainty=1.0,
    )


def _ensure_squad_forecasts(
    players: Sequence[SquadPlayer],
    forecast_by_id: Dict[int, PlayerForecast],
    season: str,
    week: int,
) -> Dict[int, PlayerForecast]:
    safe_lookup = dict(forecast_by_id)
    for player in players:
        if player.player_id not in safe_lookup:
            safe_lookup[player.player_id] = _zero_forecast(player, season=season, week=week)
    return safe_lookup


def _is_legal_squad(players: Sequence[SquadPlayer]) -> bool:
    if len(players) != 15:
        return False
    position_counts = {position: 0 for position in POSITION_NAME_TO_SQUAD_COUNT}
    team_counts: Dict[int, int] = {}
    for player in players:
        position_counts[player.position] = position_counts.get(player.position, 0) + 1
        if player.team_id > 0:
            team_counts[player.team_id] = team_counts.get(player.team_id, 0) + 1
    return position_counts == POSITION_NAME_TO_SQUAD_COUNT and all(count <= 3 for count in team_counts.values())


def _optimize_lineup(
    players: Sequence[SquadPlayer],
    forecast_by_id: Dict[int, PlayerForecast],
    weights: DecisionWeights = DEFAULT_DECISION_WEIGHTS,
) -> Tuple[List[int], List[int], int, int, float]:
    squad_forecasts = [forecast_by_id[player.player_id] for player in players if player.player_id in forecast_by_id]

    def lineup_score(forecast: PlayerForecast) -> float:
        return forecast.predicted_points_1gw * weights.availability_weight(forecast)

    by_position: Dict[str, List[PlayerForecast]] = {"GK": [], "DEF": [], "MID": [], "FWD": []}
    for forecast in squad_forecasts:
        by_position.setdefault(forecast.position, []).append(forecast)
    for forecasts in by_position.values():
        forecasts.sort(key=lineup_score, reverse=True)

    best_lineup: List[int] = []
    best_score = float("-inf")
    for formation in STARTING_FORMATIONS:
        if any(len(by_position[position]) < count for position, count in formation.items()):
            continue
        starters: List[int] = []
        for position, count in formation.items():
            starters.extend([forecast.player_id for forecast in by_position[position][:count]])
        score = sum(lineup_score(forecast_by_id[player_id]) for player_id in starters)
        if score > best_score:
            best_score = score
            best_lineup = starters

    if not best_lineup:
        counts = {position: len(forecasts) for position, forecasts in by_position.items()}
        missing = [player.player_name for player in players if player.player_id not in forecast_by_id]
        raise ValueError(
            f"No legal starting XI: forecasted squad positions {counts}; players without forecasts: {missing}"
        )

    starter_set = set(best_lineup)
    bench_goalkeepers = [
        forecast.player_id for forecast in by_position["GK"] if forecast.player_id not in starter_set
    ]
    outfield_bench = [
        forecast.player_id
        for position in ("DEF", "MID", "FWD")
        for forecast in by_position[position]
        if forecast.player_id not in starter_set
    ]
    outfield_bench = sorted(outfield_bench, key=lambda player_id: lineup_score(forecast_by_id[player_id]), reverse=True)
    bench_order = bench_goalkeepers[:1] + outfield_bench

    starters_sorted = sorted(best_lineup, key=lambda player_id: lineup_score(forecast_by_id[player_id]), reverse=True)
    captain_id = starters_sorted[0]
    vice_captain_id = starters_sorted[1]
    return best_lineup, bench_order, captain_id, vice_captain_id, best_score


def _bench_weights():
    """Programme item 5 (2026-10-17, FPL_BENCH_WEIGHTS="gk,sub1,sub2,sub3"): how much of each bench slot's 1GW
    points counts in the weekly squad evaluation. Measured over 63 bench weeks: the first outfield sub comes on in
    33% of weeks, the second in 6%, the third never (legacy weights 0.05 / 0.12 / 0.06 / 0.04)."""
    raw = os.environ.get("FPL_BENCH_WEIGHTS", "")
    if not raw:
        return None
    try:
        return [float(x) for x in raw.split(",")]
    except ValueError:
        return None


def _evaluate_squad(
    players: Sequence[SquadPlayer],
    forecast_by_id: Dict[int, PlayerForecast],
    weights: DecisionWeights = DEFAULT_DECISION_WEIGHTS,
) -> float:
    starters, bench_order, captain_id, _, _ = _optimize_lineup(players, forecast_by_id, weights)
    starter_score = sum(
        weights.horizon_points(forecast_by_id[player_id]) * weights.availability_weight(forecast_by_id[player_id])
        for player_id in starters
    )
    captain_bonus = (
        weights.captain_leverage
        * forecast_by_id[captain_id].predicted_points_1gw
        * weights.availability_weight(forecast_by_id[captain_id])
    )
    bench_score = 0.0
    bench_weights = _bench_weights()
    for idx, player_id in enumerate(bench_order):
        if bench_weights is not None:
            weight = bench_weights[idx] if idx < len(bench_weights) else 0.0
        else:
            weight = 0.05 if idx == 0 else 0.12 / idx
        bench_score += forecast_by_id[player_id].predicted_points_1gw * weight
    availability_penalty = 0.0
    if weights.availability == "threshold":
        penalty_scale = 4.0 if weights.horizon == "blend5" else 2.0
        availability_penalty = sum(
            max(0.0, 0.6 - forecast_by_id[player_id].appearance_probability) * penalty_scale
            for player_id in starters
        )
    return starter_score + captain_bonus + bench_score - availability_penalty


def _replace_players(
    squad_players: Sequence[SquadPlayer],
    players_out: Sequence[SquadPlayer],
    players_in: Sequence[PlayerForecast],
) -> List[SquadPlayer]:
    outgoing_ids = {player.player_id for player in players_out}
    updated_squad = [player for player in squad_players if player.player_id not in outgoing_ids]
    updated_squad.extend(
        [
            SquadPlayer(
                player_id=forecast.player_id,
                player_name=forecast.player_name,
                team_id=forecast.team_id,
                position=forecast.position,
                sell_price=forecast.price,
            )
            for forecast in players_in
        ]
    )
    return updated_squad


def _is_affordable(bank: float, players_out: Sequence[SquadPlayer], players_in: Sequence[PlayerForecast]) -> bool:
    budget = bank + sum(player.sell_price for player in players_out)
    spend = sum(player.price for player in players_in)
    return budget + 1e-9 >= spend


def _chip_advisories(
    squad_state: SquadState,
    starters: Sequence[int],
    bench_order: Sequence[int],
    captain_id: int,
    forecast_by_id: Dict[int, PlayerForecast],
) -> List[ChipAdvisory]:
    advisories: List[ChipAdvisory] = []
    chips = {key.lower(): value for key, value in squad_state.chips_available.items()}
    starter_forecasts = [forecast_by_id[player_id] for player_id in starters]
    bench_forecasts = [forecast_by_id[player_id] for player_id in bench_order if player_id in forecast_by_id]
    captain_forecast = forecast_by_id[captain_id]
    squad_player_ids = {player.player_id for player in squad_state.squad_players}
    squad_forecasts = [forecast_by_id[player_id] for player_id in squad_player_ids if player_id in forecast_by_id]
    starter_double_count = sum(forecast.fixture_count > 1 for forecast in starter_forecasts)
    bench_double_count = sum(forecast.fixture_count > 1 for forecast in bench_forecasts)
    squad_double_count = sum(forecast.fixture_count > 1 for forecast in squad_forecasts)
    starter_blank_count = sum(forecast.fixture_count == 0 for forecast in starter_forecasts)
    bench_blank_count = sum(forecast.fixture_count == 0 for forecast in bench_forecasts)
    bench_total = sum(forecast.predicted_points_1gw for forecast in bench_forecasts)
    bench_floor = min((forecast.appearance_probability for forecast in bench_forecasts), default=0.0)
    starter_floor = min((forecast.appearance_probability for forecast in starter_forecasts), default=0.0)

    if chips.get("bench_boost", False):
        bench_boost_confidence = 0.0
        if bench_blank_count == 0 and starter_blank_count == 0 and starter_floor >= 0.55:
            bench_boost_confidence = 0.48
            if bench_total >= 12:
                bench_boost_confidence += 0.04
            if bench_total >= 14:
                bench_boost_confidence += 0.05
            if bench_total >= 16:
                bench_boost_confidence += 0.05
            if bench_floor >= 0.65:
                bench_boost_confidence += 0.03
            if bench_floor >= 0.8:
                bench_boost_confidence += 0.02
            if bench_double_count >= 1:
                bench_boost_confidence += 0.05
            if squad_double_count >= 3:
                bench_boost_confidence += 0.03
        if bench_boost_confidence >= 0.56:
            rationale = "Bench depth is strong enough that a Bench Boost is worth considering."
            if bench_double_count >= 1 or squad_double_count >= 3:
                rationale = (
                    "Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot."
                )
            advisories.append(
                ChipAdvisory(
                    chip="bench_boost",
                    confidence=round(min(0.78, bench_boost_confidence), 2),
                    rationale=rationale,
                )
            )

    if chips.get("triple_captain", False):
        non_captain_starters = [
            forecast for forecast in starter_forecasts if forecast.player_id != captain_id
        ]
        best_alternative = max(
            (forecast.predicted_points_1gw for forecast in non_captain_starters),
            default=0.1,
        )
        captain_edge = captain_forecast.predicted_points_1gw / max(best_alternative, 0.1)
        triple_captain_confidence = 0.0
        if captain_forecast.fixture_count > 1:
            triple_captain_confidence = 0.54
            if captain_edge >= 1.1:
                triple_captain_confidence += 0.04
            if captain_edge >= 1.2:
                triple_captain_confidence += 0.03
            if captain_forecast.predicted_points_1gw >= 8:
                triple_captain_confidence += 0.03
            if captain_forecast.predicted_points_1gw >= 10:
                triple_captain_confidence += 0.03
            if captain_forecast.appearance_probability >= 0.85:
                triple_captain_confidence += 0.03
            if starter_double_count >= 3:
                triple_captain_confidence += 0.02
        if triple_captain_confidence >= 0.60:
            rationale = "Captain projection and fixture volume create a plausible Triple Captain spot."
            if captain_edge >= 1.15:
                rationale = (
                    "The captain has a double-gameweek profile and a clear projection edge over the rest of the XI."
                )
            advisories.append(
                ChipAdvisory(
                    chip="triple_captain",
                    confidence=round(min(0.8, triple_captain_confidence), 2),
                    rationale=rationale,
                )
            )

    if chips.get("free_hit", False):
        fragile_starters = [
            forecast
            for forecast in starter_forecasts
            if forecast.fixture_count == 0 or forecast.appearance_probability < 0.4
        ]
        if len(fragile_starters) >= 4:
            advisories.append(
                ChipAdvisory(
                    chip="free_hit",
                    confidence=0.64,
                    rationale="Too many likely blanks or low-minute starters make a Free Hit worth reviewing.",
                )
            )

    if chips.get("wildcard", False):
        weak_players = [
            forecast
            for forecast in forecast_by_id.values()
            if forecast.player_id in {player.player_id for player in squad_state.squad_players}
            and (forecast.predicted_points_3gw < 8 or forecast.appearance_probability < 0.45)
        ]
        if len(weak_players) >= 5:
            advisories.append(
                ChipAdvisory(
                    chip="wildcard",
                    confidence=0.55,
                    rationale="Several squad spots project poorly over the next 3 gameweeks, so a Wildcard is in play.",
                )
            )
    return advisories


def _choose_rankable_chip(advisories: Sequence[ChipAdvisory]) -> ChipAdvisory | None:
    rankable = [advisory for advisory in advisories if advisory.chip in {"bench_boost", "triple_captain"}]
    if not rankable:
        return None
    return max(rankable, key=lambda advisory: advisory.confidence)


def _predicted_option_score(
    squad_players: Sequence[SquadPlayer],
    starters: Sequence[int],
    captain_id: int,
    hit_cost: int,
    chip: str,
    forecast_by_id: Dict[int, PlayerForecast],
) -> float:
    if chip == "bench_boost":
        base_score = sum(
            forecast_by_id[player.player_id].predicted_points_1gw
            for player in squad_players
            if player.player_id in forecast_by_id
        )
    else:
        base_score = sum(
            forecast_by_id[player_id].predicted_points_1gw
            for player_id in starters
            if player_id in forecast_by_id
        )
    captain_points = forecast_by_id[captain_id].predicted_points_1gw
    total = base_score + captain_points - hit_cost
    if chip == "triple_captain":
        total += captain_points
    return round(total, 2)


def _build_candidate_option(
    option_id: int,
    squad_players: Sequence[SquadPlayer],
    forecast_by_id: Dict[int, PlayerForecast],
    projected_gain: float,
    hit_cost: int,
    label: str,
    rationale: str,
    players_out: Sequence[SquadPlayer],
    players_in: Sequence[PlayerForecast],
    chips_available: Dict[str, bool],
    weights: DecisionWeights = DEFAULT_DECISION_WEIGHTS,
) -> CandidateDecisionOption:
    starters, bench_order, captain_id, vice_captain_id, _ = _optimize_lineup(squad_players, forecast_by_id, weights)
    advisory_candidates = _chip_advisories(
        SquadState(
            season=next(iter(forecast_by_id.values())).season,
            week=next(iter(forecast_by_id.values())).week,
            squad_players=squad_players,
            bank=0.0,
            free_transfers=0,
            chips_available=chips_available,
        ),
        starters,
        bench_order,
        captain_id,
        forecast_by_id,
    )
    selected_chip = _choose_rankable_chip(advisory_candidates)
    chip = selected_chip.chip if selected_chip is not None else "none"
    chip_confidence = round(selected_chip.confidence, 2) if selected_chip is not None else 0.0
    predicted_score = _predicted_option_score(
        squad_players=squad_players,
        starters=starters,
        captain_id=captain_id,
        hit_cost=hit_cost,
        chip=chip,
        forecast_by_id=forecast_by_id,
    )
    return CandidateDecisionOption(
        option_id=option_id,
        label=label,
        players_out=[player.player_id for player in players_out],
        players_in=[player.player_id for player in players_in],
        players_out_names=[player.player_name for player in players_out],
        players_in_names=[player.player_name for player in players_in],
        projected_gain=round(projected_gain, 2),
        hit_cost=hit_cost,
        predicted_score=predicted_score,
        captain_id=captain_id,
        captain_name=forecast_by_id[captain_id].player_name,
        vice_captain_id=vice_captain_id,
        vice_captain_name=forecast_by_id[vice_captain_id].player_name,
        starters=[forecast_by_id[player_id].player_name for player_id in starters],
        bench_order=[forecast_by_id[player_id].player_name for player_id in bench_order],
        chip=chip,
        chip_confidence=chip_confidence,
        rationale=rationale,
    )


def _supporting_sources_from_evidence(evidence_snapshot: EvidenceSnapshot | None) -> List[SourceDocument]:
    if evidence_snapshot is None:
        return []
    return [
        SourceDocument(
            title=document.title,
            url=document.url,
            source_name=document.source_name,
            category=document.category,
            published_at=document.published_at,
            snippet=document.snippet,
        )
        for document in evidence_snapshot.documents
    ]


def recommend_actions(
    squad_state: SquadState,
    forecasts: Sequence[PlayerForecast],
    top_n_transfers: int = 5,
    max_transfers_considered: int = 2,
    supporting_sources: Sequence[SourceDocument] = (),
    evidence_snapshot: EvidenceSnapshot | None = None,
    decision_weights: DecisionWeights = DEFAULT_DECISION_WEIGHTS,
) -> RecommendationBundle:
    forecast_by_id = _ensure_squad_forecasts(
        list(squad_state.squad_players),
        _forecast_lookup(forecasts),
        season=squad_state.season,
        week=squad_state.week,
    )
    current_squad = list(squad_state.squad_players)
    current_score = _evaluate_squad(current_squad, forecast_by_id, decision_weights)
    starters, bench_order, captain_id, vice_captain_id, _ = _optimize_lineup(current_squad, forecast_by_id, decision_weights)

    squad_player_ids = {player.player_id for player in current_squad}
    bottom_squad = sorted(
        current_squad,
        key=lambda player: decision_weights.horizon_points(forecast_by_id.get(player.player_id, PlayerForecast(
            season=squad_state.season,
            week=squad_state.week,
            player_id=player.player_id,
            player_name=player.player_name,
            team_id=player.team_id,
            position=player.position,
            price=player.sell_price,
            predicted_minutes=0.0,
            predicted_points_1gw=0.0,
            predicted_points_3gw=0.0,
            predicted_points_5gw=0.0,
            appearance_probability=0.0,
            fixture_count=0,
            uncertainty=1.0,
        ))),
    )[:6]
    incoming_pool = [
        forecast
        for forecast in sorted(forecasts, key=decision_weights.horizon_points, reverse=True)
        if forecast.player_id not in squad_player_ids
    ][:24]

    options: List[TransferRecommendation] = []

    for transfer_count in range(1, max_transfers_considered + 1):
        for players_out in combinations(bottom_squad, transfer_count):
            for players_in in combinations(incoming_pool, transfer_count):
                if not _is_affordable(squad_state.bank, players_out, players_in):
                    continue
                updated_squad = _replace_players(current_squad, players_out, players_in)
                if not _is_legal_squad(updated_squad):
                    continue
                updated_score = _evaluate_squad(updated_squad, forecast_by_id, decision_weights)
                extra_transfers = max(0, transfer_count - squad_state.free_transfers)
                hit_cost = extra_transfers * 4
                projected_gain = updated_score - current_score - hit_cost
                if projected_gain <= 0:
                    continue
                explanation = (
                    f"Projects +{projected_gain:.2f} over the current squad by replacing "
                    f"{', '.join(player.player_name for player in players_out)} with "
                    f"{', '.join(player.player_name for player in players_in)}."
                )
                options.append(
                    TransferRecommendation(
                        players_out=[player.player_id for player in players_out],
                        players_in=[player.player_id for player in players_in],
                        projected_gain=round(projected_gain, 2),
                        hit_cost=hit_cost,
                        explanation=explanation,
                    )
                )

    options.sort(key=lambda option: option.projected_gain, reverse=True)
    advisories = _chip_advisories(squad_state, starters, bench_order, captain_id, forecast_by_id)

    candidate_options: List[CandidateDecisionOption] = [
        _build_candidate_option(
            option_id=0,
            squad_players=current_squad,
            forecast_by_id=forecast_by_id,
            projected_gain=0.0,
            hit_cost=0,
            label="Hold squad",
            rationale="Keep the current squad and optimize captaincy, lineup, and chip usage around the existing players.",
            players_out=[],
            players_in=[],
            chips_available=squad_state.chips_available,
            weights=decision_weights,
        )
    ]
    squad_lookup = {player.player_id: player for player in current_squad}
    for index, option in enumerate(options[:top_n_transfers], start=1):
        players_out = [squad_lookup[player_id] for player_id in option.players_out if player_id in squad_lookup]
        players_in = [forecast_by_id[player_id] for player_id in option.players_in if player_id in forecast_by_id]
        updated_squad = _replace_players(current_squad, players_out, players_in)
        candidate_options.append(
            _build_candidate_option(
                option_id=index,
                squad_players=updated_squad,
                forecast_by_id=forecast_by_id,
                projected_gain=option.projected_gain,
                hit_cost=option.hit_cost,
                label=(
                    f"OUT {', '.join(player.player_name for player in players_out)} | "
                    f"IN {', '.join(player.player_name for player in players_in)}"
                ),
                rationale=option.explanation,
                players_out=players_out,
                players_in=players_in,
                chips_available=squad_state.chips_available,
                weights=decision_weights,
            )
        )

    assumptions = [
        "Forecasts are generated from structured FPL data only in v1.",
        "Text/news inputs are intended for explanation and freshness checks, not direct model features.",
        "Chip recommendations are advisory heuristics, not full chip optimization.",
    ]
    confidence = round(
        max(0.1, min(0.95, 1.0 - sum(forecast_by_id[player_id].uncertainty for player_id in starters) / max(len(starters), 1))),
        2,
    )
    merged_sources = list(supporting_sources)
    for document in _supporting_sources_from_evidence(evidence_snapshot):
        if document.url not in {source.url for source in merged_sources}:
            merged_sources.append(document)
    if evidence_snapshot is not None and evidence_snapshot.document_count:
        assumptions.append(
            f"Candidate ranking context includes {evidence_snapshot.document_count} timestamp-safe evidence documents before the deadline."
        )
    return RecommendationBundle(
        season=squad_state.season,
        week=squad_state.week,
        transfers=options[:top_n_transfers],
        captain_id=captain_id,
        vice_captain_id=vice_captain_id,
        starters=starters,
        bench_order=bench_order,
        chip_advisories=advisories,
        confidence=confidence,
        assumptions=assumptions,
        supporting_sources=merged_sources,
        candidate_options=candidate_options,
        evidence_snapshot=evidence_snapshot,
    )

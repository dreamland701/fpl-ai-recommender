"""Rolling squad-level backtests and reporting."""

from __future__ import annotations

import os
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence, Tuple

import pandas as pd

from .config import POSITION_NAME_TO_SQUAD_COUNT, parse_season_start_year
from .dataset import CanonicalDataset, training_rows_asof
from .decision import (
    DEFAULT_DECISION_WEIGHTS,
    DecisionWeights,
    _ensure_squad_forecasts,
    _evaluate_squad,
    _forecast_lookup,
    _is_legal_squad,
    _optimize_lineup,
    recommend_actions,
)
from .llm_adjust import apply_llm_deltas
from .models import fit_model_suite_from_frame
from .rules import automatic_substitutions, selling_price
from .types import ChipAdvisory, PlayerForecast, SquadPlayer, SquadState


@dataclass(frozen=True)
class BacktestSquadEntry:
    player_id: int
    player_name: str
    position: str
    team_id: int
    price: float
    selected_role: str
    realized_role: str
    predicted_points_1gw: float
    predicted_points_3gw: float
    predicted_points_5gw: float
    actual_points_1gw: float
    predicted_minutes: float
    actual_minutes: float
    appearance_probability: float


@dataclass(frozen=True)
class BacktestTransferMove:
    players_out: Sequence[str]
    players_in: Sequence[str]
    projected_gain: float
    hit_cost: int


@dataclass(frozen=True)
class BacktestTransferCandidate:
    players_out: Sequence[str]
    players_in: Sequence[str]
    projected_gain: float
    hit_cost: int
    explanation: str
    outgoing_players: Sequence["BacktestSquadSnapshotEntry"]
    incoming_players: Sequence["BacktestSquadSnapshotEntry"]


@dataclass(frozen=True)
class BacktestSquadSnapshotEntry:
    player_id: int
    player_name: str
    position: str
    team_id: int
    price: float
    predicted_points_1gw: float
    predicted_points_3gw: float
    predicted_points_5gw: float
    predicted_minutes: float
    appearance_probability: float
    actual_points_1gw: float
    actual_minutes: float


@dataclass(frozen=True)
class BacktestWeekResult:
    season: str
    week: int
    train_rows: int
    bank_before: float
    bank_after: float
    free_transfers_before: int
    free_transfers_after: int
    pre_move_squad: Sequence[BacktestSquadSnapshotEntry]
    candidate_transfers: Sequence[BacktestTransferCandidate]
    transfers_applied: Sequence[BacktestTransferMove]
    chip_used: str
    chip_reason: str
    chip_advisories: Sequence[str]
    predicted_score: float
    actual_score: float
    league_average_score: Optional[float]
    captain_id: int
    captain_name: str
    vice_captain_id: int
    vice_captain_name: str
    effective_captain_id: int
    effective_captain_name: str
    starters: Sequence[int]
    realized_starters: Sequence[int]
    bench_order: Sequence[int]
    squad: Sequence[BacktestSquadEntry]
    notes: Sequence[str]


@dataclass(frozen=True)
class RollingSquadBacktestReport:
    train_seasons: Sequence[str]
    test_season: str
    initial_train_week_max: int
    simulated_weeks: Sequence[int]
    total_predicted_points: float
    total_actual_points: float
    total_transfer_hits: int
    average_predicted_points: float
    average_actual_points: float
    weeks: Sequence[BacktestWeekResult]
    notes: Sequence[str]


def _season_week_key(frame: pd.DataFrame) -> pd.Series:
    return frame["season"].astype(str).map(parse_season_start_year) * 100 + frame["week"].astype(int)


def _training_frame_for_week(dataset: CanonicalDataset, test_season: str, week: int) -> pd.DataFrame:
    return training_rows_asof(dataset.training_frame, test_season, week)


def _selection_score(forecast: PlayerForecast) -> float:
    availability_penalty = max(0.0, 0.65 - forecast.appearance_probability) * 4.0
    return (
        forecast.predicted_points_5gw
        + 0.6 * forecast.predicted_points_3gw
        + 0.35 * forecast.predicted_points_1gw
        - availability_penalty
    )


def _minimum_remaining_cost(
    all_candidates_by_position: Dict[str, Sequence[PlayerForecast]],
    selected_ids: frozenset[int],
    remaining_slots: Dict[str, int],
) -> float:
    total = 0.0
    for position, count in remaining_slots.items():
        if count <= 0:
            continue
        prices = [
            max(0.0, float(candidate.price))
            for candidate in all_candidates_by_position[position]
            if candidate.player_id not in selected_ids
        ]
        if len(prices) < count:
            return float("inf")
        prices.sort()
        total += sum(prices[:count])
    return total


def _candidate_pools_by_position(
    forecasts: Sequence[PlayerForecast],
    pool_sizes: Dict[str, int],
    cheap_counts: Dict[str, int],
) -> Dict[str, List[PlayerForecast]]:
    pools: Dict[str, List[PlayerForecast]] = {}
    for position, squad_count in POSITION_NAME_TO_SQUAD_COUNT.items():
        position_forecasts = [forecast for forecast in forecasts if forecast.position == position and forecast.price > 0]
        position_forecasts.sort(key=_selection_score, reverse=True)
        top_pool = position_forecasts[: pool_sizes.get(position, squad_count * 8)]
        cheap_pool = sorted(position_forecasts, key=lambda forecast: (forecast.price, -_selection_score(forecast)))[
            : cheap_counts.get(position, squad_count * 2)
        ]
        deduped: List[PlayerForecast] = []
        seen: set[int] = set()
        for forecast in top_pool + cheap_pool:
            if forecast.player_id in seen:
                continue
            deduped.append(forecast)
            seen.add(forecast.player_id)
        pools[position] = deduped
    return pools


def _build_initial_squad_milp(forecasts: Sequence[PlayerForecast], budget: float) -> Tuple[List[SquadPlayer], float]:
    """Exact draft (FPL_DRAFT_MILP=1): the wildcard MILP from squad_milp with the beam's selection
    score as the value. The beam fills slots position by position (GK, DEF, MID, FWD) under the
    3-per-club cap, so once three defenders from one club look good it can never add that club's
    midfielder — found 2026-10-13 when correctly priced double gameweeks made it draft three
    Liverpool defenders in GW24 2024-25 and lock Salah (the top forecast by 25 points) out."""
    from .squad_milp import optimize

    table = {
        forecast.player_id: {"pos": forecast.position, "team_id": forecast.team_id, "price": forecast.price, "status": "a"}
        for forecast in forecasts
        if forecast.price > 0 and forecast.position in POSITION_NAME_TO_SQUAD_COUNT
    }
    by_id = {forecast.player_id: forecast for forecast in forecasts}
    value = {pid: max(0.0, _selection_score(by_id[pid])) for pid in table}
    result = optimize(table, value, current_sell={}, bank=budget, free_transfers=15, wildcard=True)
    chosen = [by_id[pid] for pid in result["in"]]
    squad = [
        SquadPlayer(player_id=f.player_id, player_name=f.player_name, team_id=f.team_id, position=f.position, sell_price=f.price)
        for f in chosen
    ]
    if not _is_legal_squad(squad):
        raise ValueError("MILP draft did not produce a legal squad.")
    return squad, max(0.0, round(budget - sum(f.price for f in chosen), 2))


def build_initial_squad(
    forecasts: Sequence[PlayerForecast],
    budget: float = 100.0,
    beam_width: int = 300,
    bench_gk_weight: float = 1.0,
    captain_leverage: float | None = None,
) -> Tuple[List[SquadPlayer], float]:
    """bench_gk_weight scales the SECOND goalkeeper slot's score
    contribution. Only one GK can ever start, so the backup GK's forecast
    points are almost never fielded — at the default 1.0 the beam counts
    them fully and will pay real budget for bench-GK quality it can't use
    (found 2026-08-13 drafting the live GW1 2026-27 squad: it kept a
    £4.5m starting-quality backup over a £4.0m playing one, spending
    £0.5m on unusable points). Live drafting should pass a small weight
    (e.g. 0.15) so that money flows to outfield value via the global
    budget tradeoff instead. Default 1.0 preserves historical backtest
    behavior so old gate numbers stay comparable."""
    if os.environ.get("FPL_DRAFT_MILP", "0") == "1":
        return _build_initial_squad_milp(forecasts, budget)
    candidate_pools = _candidate_pools_by_position(
        forecasts,
        pool_sizes={"GK": 18, "DEF": 60, "MID": 60, "FWD": 36},
        cheap_counts={"GK": 8, "DEF": 20, "MID": 20, "FWD": 12},
    )
    all_candidates_by_position = {
        position: sorted(
            [forecast for forecast in forecasts if forecast.position == position and forecast.price > 0],
            key=lambda forecast: (forecast.price, -_selection_score(forecast)),
        )
        for position in POSITION_NAME_TO_SQUAD_COUNT
    }

    slot_order = ["GK"] * 2 + ["DEF"] * 5 + ["MID"] * 5 + ["FWD"] * 3
    beam = [
        {
            "selected": [],
            "selected_ids": frozenset(),
            "cost": 0.0,
            "score": 0.0,
            "team_counts": {},
        }
    ]

    for slot_index, position in enumerate(slot_order):
        next_beam = []
        remaining_after_pick = slot_order[slot_index + 1 :]
        remaining_template = {name: remaining_after_pick.count(name) for name in POSITION_NAME_TO_SQUAD_COUNT}

        for state in beam:
            for candidate in candidate_pools[position]:
                if candidate.player_id in state["selected_ids"]:
                    continue
                team_counts = dict(state["team_counts"])
                if candidate.team_id > 0:
                    team_counts[candidate.team_id] = team_counts.get(candidate.team_id, 0) + 1
                    if team_counts[candidate.team_id] > 3:
                        continue

                new_selected_ids = state["selected_ids"] | {candidate.player_id}
                new_cost = state["cost"] + candidate.price
                minimum_remaining = _minimum_remaining_cost(
                    all_candidates_by_position,
                    new_selected_ids,
                    remaining_template,
                )
                if new_cost + minimum_remaining > budget + 1e-9:
                    continue
                # Slot 1 completes the GK pair (slot_order starts with two
                # GK slots). The bench keeper is whichever of the two
                # scores LOWER — not whichever was picked second (the
                # dedup collapses pick order, so "second pick" would be
                # order-dependent). Score the pair as
                # max + bench_gk_weight * min, replacing the first GK's
                # full-weight contribution already in state["score"].
                candidate_score = _selection_score(candidate)
                if slot_index == 1:
                    first_gk_score = _selection_score(state["selected"][0])
                    pair_score = max(first_gk_score, candidate_score) + bench_gk_weight * min(
                        first_gk_score, candidate_score
                    )
                    new_score = state["score"] - first_gk_score + pair_score
                else:
                    new_score = state["score"] + candidate_score
                next_beam.append(
                    {
                        "selected": [*state["selected"], candidate],
                        "selected_ids": new_selected_ids,
                        "cost": new_cost,
                        "score": new_score,
                        "team_counts": team_counts,
                    }
                )

        if not next_beam:
            raise ValueError(f"Could not construct a legal squad within budget while filling {position}.")
        next_beam.sort(key=lambda item: (item["score"], -item["cost"]), reverse=True)
        score_priority = next_beam[: max(1, beam_width // 2)]
        next_beam.sort(key=lambda item: (item["cost"], -item["score"]))
        cost_priority = next_beam[: max(1, beam_width // 2)]
        deduped_beam = []
        seen_signatures = set()
        for candidate in [*score_priority, *cost_priority]:
            signature = tuple(sorted(candidate["selected_ids"]))
            if signature in seen_signatures:
                continue
            deduped_beam.append(candidate)
            seen_signatures.add(signature)
        beam = deduped_beam[:beam_width]

    # Captaincy leverage: the captain DOUBLES the best starter every week,
    # but additive beam scores credit nothing for owning a high-ceiling
    # doubling target — which is how a compressed-but-still-top premium
    # (the Haaland case, GW2 2026-27) loses the budget fight to
    # mid-premium + fodder arithmetic. Re-rank the surviving complete
    # squads by score + leverage * best-single-player score. Default (or
    # FPL_DRAFT_CAPTAIN_LEVERAGE unset) is 0.0, preserving every
    # historical gate number; the env gate exists for A/B backtests.
    if captain_leverage is None:
        captain_leverage = float(os.environ.get("FPL_DRAFT_CAPTAIN_LEVERAGE", "0") or 0.0)
    if captain_leverage > 0.0:
        beam.sort(
            key=lambda item: item["score"]
            + captain_leverage * max(_selection_score(f) for f in item["selected"]),
            reverse=True,
        )
    final_state = beam[0]
    squad = [
        SquadPlayer(
            player_id=forecast.player_id,
            player_name=forecast.player_name,
            team_id=forecast.team_id,
            position=forecast.position,
            sell_price=forecast.price,
        )
        for forecast in final_state["selected"]
    ]
    if not _is_legal_squad(squad):
        raise ValueError("Initial squad builder did not produce a legal squad.")
    bank = max(0.0, round(budget - final_state["cost"], 2))
    return squad, bank


def build_cheapest_legal_squad(
    forecasts: Sequence[PlayerForecast],
    budget: float = 100.0,
) -> Tuple[List[SquadPlayer], float]:
    candidates_by_position = {
        position: sorted(
            [forecast for forecast in forecasts if forecast.position == position and forecast.price > 0],
            key=lambda forecast: (forecast.price, -_selection_score(forecast)),
        )
        for position in POSITION_NAME_TO_SQUAD_COUNT
    }
    selected: List[PlayerForecast] = []
    selected_ids: set[int] = set()
    for position, squad_count in POSITION_NAME_TO_SQUAD_COUNT.items():
        for candidate in candidates_by_position[position]:
            if candidate.player_id in selected_ids:
                continue
            selected.append(candidate)
            selected_ids.add(candidate.player_id)
            if sum(player.position == position for player in selected) >= squad_count:
                break

    if len(selected) != 15:
        raise ValueError("Could not seed a full squad from the cheapest players by position.")

    def total_cost(players: Sequence[PlayerForecast]) -> float:
        return sum(player.price for player in players)

    while True:
        team_counts: Dict[int, int] = {}
        for player in selected:
            if player.team_id > 0:
                team_counts[player.team_id] = team_counts.get(player.team_id, 0) + 1
        overfull_teams = [team_id for team_id, count in team_counts.items() if count > 3]
        if not overfull_teams:
            break
        overfull_team = overfull_teams[0]
        replacement = None
        current_total_cost = total_cost(selected)
        for selected_player in sorted(
            [player for player in selected if player.team_id == overfull_team],
            key=lambda player: (player.price, -_selection_score(player)),
            reverse=True,
        ):
            for candidate in candidates_by_position[selected_player.position]:
                if candidate.player_id in selected_ids or candidate.team_id == overfull_team:
                    continue
                if candidate.team_id > 0 and team_counts.get(candidate.team_id, 0) >= 3:
                    continue
                next_total_cost = current_total_cost - selected_player.price + candidate.price
                if next_total_cost > budget + 1e-9:
                    continue
                replacement = (selected_player, candidate)
                break
            if replacement is not None:
                break
        if replacement is None:
            raise ValueError("Could not construct even the cheapest legal squad within budget.")
        outgoing, incoming = replacement
        selected = [incoming if player.player_id == outgoing.player_id else player for player in selected]
        selected_ids.discard(outgoing.player_id)
        selected_ids.add(incoming.player_id)

    if total_cost(selected) > budget + 1e-9:
        raise ValueError("Cheapest legal squad repair exceeded budget.")
    squad = [
        SquadPlayer(
            player_id=forecast.player_id,
            player_name=forecast.player_name,
            team_id=forecast.team_id,
            position=forecast.position,
            sell_price=forecast.price,
        )
        for forecast in selected
    ]
    bank = max(0.0, round(budget - sum(player.sell_price for player in squad), 2))
    return squad, bank


def _lookup_frame_by_player(frame: pd.DataFrame) -> Dict[int, Dict[str, object]]:
    indexed = frame.sort_values(["player_id"]).drop_duplicates(subset=["player_id"], keep="last")
    return {
        int(record["player_id"]): record
        for record in indexed.to_dict(orient="records")
    }


def _apply_transfer(
    squad_players: Sequence[SquadPlayer],
    bank: float,
    players_out: Sequence[int],
    players_in: Sequence[int],
    forecast_by_id: Dict[int, PlayerForecast],
) -> Tuple[List[SquadPlayer], float]:
    outgoing = [player for player in squad_players if player.player_id in set(players_out)]
    incoming = [forecast_by_id[player_id] for player_id in players_in]
    next_bank = bank + sum(player.sell_price for player in outgoing) - sum(player.price for player in incoming)
    kept_players = [player for player in squad_players if player.player_id not in set(players_out)]
    updated_players = kept_players + [
        SquadPlayer(
            player_id=forecast.player_id,
            player_name=forecast.player_name,
            team_id=forecast.team_id,
            position=forecast.position,
            sell_price=forecast.price,
        )
        for forecast in incoming
    ]
    return updated_players, round(next_bank, 2)


def _snapshot_squad_entries(
    squad_players: Sequence[SquadPlayer],
    forecast_by_id: Mapping[int, PlayerForecast],
    actual_points: Mapping[int, float],
    actual_minutes: Mapping[int, float],
) -> List[BacktestSquadSnapshotEntry]:
    entries: List[BacktestSquadSnapshotEntry] = []
    for player in sorted(
        squad_players,
        key=lambda item: (
            item.position != "GK",
            item.position,
            -forecast_by_id[item.player_id].predicted_points_3gw if item.player_id in forecast_by_id else 0.0,
            item.player_name,
        ),
    ):
        forecast = forecast_by_id[player.player_id]
        entries.append(
            BacktestSquadSnapshotEntry(
                player_id=player.player_id,
                player_name=player.player_name,
                position=player.position,
                team_id=player.team_id,
                price=float(player.sell_price),
                predicted_points_1gw=float(forecast.predicted_points_1gw),
                predicted_points_3gw=float(forecast.predicted_points_3gw),
                predicted_points_5gw=float(forecast.predicted_points_5gw),
                predicted_minutes=float(forecast.predicted_minutes),
                appearance_probability=float(forecast.appearance_probability),
                actual_points_1gw=float(actual_points.get(player.player_id, 0.0)),
                actual_minutes=float(actual_minutes.get(player.player_id, 0.0)),
            )
        )
    return entries


def _apply_automatic_substitutions(
    squad_players: Sequence[SquadPlayer],
    starters: Sequence[int],
    bench_order: Sequence[int],
    actual_points: Dict[int, float],
    actual_minutes: Dict[int, float],
) -> Tuple[List[int], List[str]]:
    player_by_id = {player.player_id: player for player in squad_players}
    positions = {player_id: player.position for player_id, player in player_by_id.items()}
    counted, substitutions = automatic_substitutions(positions, starters, bench_order, actual_minutes)
    notes = [
        f"Autosub: {player_by_id[substitute].player_name} replaced {player_by_id[starter].player_name}."
        for starter, substitute in substitutions
    ]
    final_starters = sorted(
        set(counted),
        key=lambda player_id: (
            player_by_id[player_id].position != "GK",
            player_by_id[player_id].position,
            -actual_points.get(player_id, 0.0),
            player_by_id[player_id].player_name,
        ),
    )
    return final_starters, notes


def _refresh_squad_prices(squad_players: Sequence[SquadPlayer], week_frame: pd.DataFrame) -> List[SquadPlayer]:
    frame_by_player = _lookup_frame_by_player(week_frame)
    refreshed: List[SquadPlayer] = []
    for player in squad_players:
        week_row = frame_by_player.get(player.player_id, {})
        market_price = pd.to_numeric(week_row.get("price_pre_deadline", week_row.get("price")), errors="coerce")
        if pd.isna(market_price) or market_price <= 0:
            refreshed.append(player)
            continue
        refreshed.append(
            SquadPlayer(
                player_id=player.player_id,
                player_name=player.player_name,
                team_id=player.team_id,
                position=player.position,
                sell_price=selling_price(player.purchase_price, float(market_price)),
                purchase_price=player.purchase_price,
            )
        )
    return refreshed


def _effective_captain(
    captain_id: int,
    vice_captain_id: int,
    actual_minutes: Dict[int, float],
) -> int:
    if actual_minutes.get(captain_id, 0.0) > 0:
        return captain_id
    if actual_minutes.get(vice_captain_id, 0.0) > 0:
        return vice_captain_id
    return captain_id


def _selected_role(player_id: int, starters: Sequence[int], bench_order: Sequence[int], captain_id: int, vice_captain_id: int) -> str:
    if player_id == captain_id:
        return "Captain"
    if player_id == vice_captain_id:
        return "Vice Captain"
    if player_id in starters:
        return "XI"
    if player_id in bench_order:
        return f"Bench {bench_order.index(player_id) + 1}"
    return "Squad"


def _realized_role(
    player_id: int,
    realized_starters: Sequence[int],
    captain_id: int,
    effective_captain_id: int,
    starters: Sequence[int],
    chip_used: str,
    bench_order: Sequence[int],
) -> str:
    if chip_used == "bench_boost" and player_id in bench_order:
        return "Bench Boost"
    if player_id == effective_captain_id and player_id in realized_starters:
        return "Captain"
    if player_id in realized_starters and player_id in starters:
        return "XI"
    if player_id in realized_starters and player_id not in starters:
        return "Autosub In"
    return "Bench"


def _schedule_points_multiplier(fixture_count: int, fixture_difficulty_mean: float, home_fixture_ratio: float) -> float:
    if fixture_count <= 0:
        return 0.0
    difficulty = fixture_difficulty_mean if fixture_difficulty_mean > 0 else 3.0
    difficulty_factor = max(0.68, 1.18 - 0.09 * (difficulty - 3.0))
    home_factor = 1.0 + max(0.0, home_fixture_ratio - 0.5) * 0.08
    return float(fixture_count) * difficulty_factor * home_factor


def _project_forecast_to_schedule(
    current: PlayerForecast,
    future_row: Mapping[str, object],
    season: str,
    week: int,
) -> PlayerForecast:
    """Scale a current-week forecast onto a future week's known schedule.

    Uses only schedule columns (fixture count/difficulty/venue) from the
    future frame — the same leakage profile as the chip-scheduling DP.
    """
    future_fixture_count = int(float(future_row.get("fixture_count", 0.0) or 0.0))
    future_difficulty = float(future_row.get("fixture_difficulty_mean", 3.0) or 3.0)
    future_home_ratio = float(future_row.get("home_fixture_ratio", 0.5) or 0.5)
    base_points_per_fixture = current.predicted_points_1gw / max(current.fixture_count, 1)
    base_minutes_per_fixture = current.predicted_minutes / max(current.fixture_count, 1)
    schedule_multiplier = _schedule_points_multiplier(
        future_fixture_count,
        future_difficulty,
        future_home_ratio,
    )
    predicted_points_1gw = max(0.0, base_points_per_fixture * schedule_multiplier)
    predicted_minutes = min(
        180.0,
        max(
            0.0,
            base_minutes_per_fixture
            * future_fixture_count
            * max(0.72, 1.05 - 0.05 * max(future_difficulty - 3.0, 0.0)),
        ),
    )
    appearance_probability = 0.0
    if future_fixture_count > 0:
        appearance_probability = min(
            1.0,
            max(
                0.0,
                current.appearance_probability
                * max(0.7, 0.92 + 0.08 * min(future_fixture_count, 2)),
            ),
        )
    return PlayerForecast(
        season=season,
        week=week,
        player_id=current.player_id,
        player_name=current.player_name,
        team_id=current.team_id,
        position=current.position,
        price=current.price,
        predicted_minutes=float(predicted_minutes),
        predicted_points_1gw=float(predicted_points_1gw),
        predicted_points_3gw=float(predicted_points_1gw * 3.0),
        predicted_points_5gw=float(predicted_points_1gw * 5.0),
        appearance_probability=float(appearance_probability),
        fixture_count=future_fixture_count,
        uncertainty=current.uncertainty,
        rate_5gw=current.rate_5gw,
    )


def _project_forecast_by_horizon_diff(
    current: PlayerForecast,
    future_row: Mapping[str, object],
    season: str,
    week: int,
) -> PlayerForecast:
    """Estimate next week from the model's own horizon sums: the 3GW forecast
    minus the 1GW forecast is the model's view of weeks t+2..t+3, which
    already prices in upcoming fixtures — unlike schedule-rescaling t+1."""
    future_fixture_count = int(float(future_row.get("fixture_count", 0.0) or 0.0))
    if future_fixture_count <= 0:
        return replace_forecast_zero(current, season, week)
    next_1gw = max(0.0, (current.predicted_points_3gw - current.predicted_points_1gw) / 2.0)
    next_3gw = max(
        next_1gw,
        current.predicted_points_3gw
        - current.predicted_points_1gw
        + (current.predicted_points_5gw - current.predicted_points_3gw) / 2.0,
    )
    next_5gw = max(next_3gw, current.predicted_points_5gw - current.predicted_points_1gw)
    return PlayerForecast(
        season=season,
        week=week,
        player_id=current.player_id,
        player_name=current.player_name,
        team_id=current.team_id,
        position=current.position,
        price=current.price,
        predicted_minutes=current.predicted_minutes,
        predicted_points_1gw=float(next_1gw),
        predicted_points_3gw=float(next_3gw),
        predicted_points_5gw=float(next_5gw),
        appearance_probability=current.appearance_probability,
        fixture_count=future_fixture_count,
        uncertainty=current.uncertainty,
        rate_5gw=current.rate_5gw,
    )


def replace_forecast_zero(current: PlayerForecast, season: str, week: int) -> PlayerForecast:
    return PlayerForecast(
        season=season,
        week=week,
        player_id=current.player_id,
        player_name=current.player_name,
        team_id=current.team_id,
        position=current.position,
        price=current.price,
        predicted_minutes=0.0,
        predicted_points_1gw=0.0,
        predicted_points_3gw=0.0,
        predicted_points_5gw=0.0,
        appearance_probability=0.0,
        fixture_count=0,
        uncertainty=current.uncertainty,
        rate_5gw=current.rate_5gw,  # a blank week does not erase the player's long-run value (item 2)
    )


def _project_forecast_by_oracle(
    current: PlayerForecast,
    future_row: Mapping[str, object],
    season: str,
    week: int,
) -> PlayerForecast:
    """DIAGNOSTIC ONLY — deliberately leaks realized outcomes. Used by the
    oracle lookahead test to upper-bound the option value of banking
    transfers when next-week knowledge is perfect."""
    if not future_row:
        return replace_forecast_zero(current, season, week)
    minutes = float(future_row.get("label_minutes_1gw", 0.0) or 0.0)
    points_1 = float(future_row.get("label_points_1gw", 0.0) or 0.0)
    points_3 = float(future_row.get("label_points_3gw", 0.0) or (points_1 * 3.0))
    points_5 = float(future_row.get("label_points_5gw", 0.0) or (points_1 * 5.0))
    return PlayerForecast(
        season=season,
        week=week,
        player_id=current.player_id,
        player_name=current.player_name,
        team_id=current.team_id,
        position=current.position,
        price=current.price,
        predicted_minutes=minutes,
        predicted_points_1gw=points_1,
        predicted_points_3gw=points_3,
        predicted_points_5gw=points_5,
        appearance_probability=1.0 if minutes > 0 else 0.0,
        fixture_count=int(float(future_row.get("fixture_count", 0.0) or 0.0)),
        uncertainty=0.0,
        rate_5gw=points_5 / 5.0,
    )


def _project_forecasts_to_week(
    forecasts: Sequence[PlayerForecast],
    future_week_frame: pd.DataFrame,
    season: str,
    week: int,
    projection: str = "schedule",
) -> List[PlayerForecast]:
    future_rows = _lookup_frame_by_player(future_week_frame)
    if projection == "oracle":
        return [
            _project_forecast_by_oracle(current, future_rows.get(current.player_id, {}), season, week)
            for current in forecasts
        ]
    if projection == "horizon_diff":
        return [
            _project_forecast_by_horizon_diff(current, future_rows.get(current.player_id, {}), season, week)
            for current in forecasts
        ]
    return [
        _project_forecast_to_schedule(current, future_rows.get(current.player_id, {}), season, week)
        for current in forecasts
    ]


def _estimated_future_forecasts_for_current_squad(
    squad_players: Sequence[SquadPlayer],
    current_forecast_by_id: Mapping[int, PlayerForecast],
    future_week_frame: pd.DataFrame,
    season: str,
    week: int,
) -> List[PlayerForecast]:
    future_rows = _lookup_frame_by_player(future_week_frame)
    estimated: List[PlayerForecast] = []
    for player in squad_players:
        current = current_forecast_by_id[player.player_id]
        future_row = future_rows.get(player.player_id, {})
        future_fixture_count = int(float(future_row.get("fixture_count", 0.0) or 0.0))
        future_difficulty = float(future_row.get("fixture_difficulty_mean", 3.0) or 3.0)
        future_home_ratio = float(future_row.get("home_fixture_ratio", 0.5) or 0.5)
        base_points_per_fixture = current.predicted_points_1gw / max(current.fixture_count, 1)
        base_minutes_per_fixture = current.predicted_minutes / max(current.fixture_count, 1)
        schedule_multiplier = _schedule_points_multiplier(
            future_fixture_count,
            future_difficulty,
            future_home_ratio,
        )
        predicted_points_1gw = max(0.0, base_points_per_fixture * schedule_multiplier)
        predicted_minutes = min(
            180.0,
            max(
                0.0,
                base_minutes_per_fixture
                * future_fixture_count
                * max(0.72, 1.05 - 0.05 * max(future_difficulty - 3.0, 0.0)),
            ),
        )
        appearance_probability = 0.0
        if future_fixture_count > 0:
            appearance_probability = min(
                1.0,
                max(
                    0.0,
                    current.appearance_probability
                    * max(0.7, 0.92 + 0.08 * min(future_fixture_count, 2)),
                ),
            )
        estimated.append(
            PlayerForecast(
                season=season,
                week=week,
                player_id=player.player_id,
                player_name=player.player_name,
                team_id=player.team_id,
                position=player.position,
                price=player.sell_price,
                predicted_minutes=float(predicted_minutes),
                predicted_points_1gw=float(predicted_points_1gw),
                predicted_points_3gw=float(predicted_points_1gw * 3.0),
                predicted_points_5gw=float(predicted_points_1gw * 5.0),
                appearance_probability=float(appearance_probability),
                fixture_count=future_fixture_count,
                rate_5gw=float(predicted_points_1gw),
                uncertainty=current.uncertainty,
            )
        )
    return estimated


def _chip_week_value_summary(
    squad_players: Sequence[SquadPlayer],
    squad_forecasts: Sequence[PlayerForecast],
    global_schedule_summary: Optional[Mapping[str, float]] = None,
) -> Dict[str, float]:
    sample_forecast = squad_forecasts[0] if squad_forecasts else None
    forecast_by_id = _ensure_squad_forecasts(
        squad_players,
        _forecast_lookup(squad_forecasts),
        season=sample_forecast.season if sample_forecast else "",
        week=sample_forecast.week if sample_forecast else 0,
    )
    starters, bench_order, captain_id, _, _ = _optimize_lineup(squad_players, forecast_by_id)
    bench_value = sum(forecast_by_id[player_id].predicted_points_1gw for player_id in bench_order)
    triple_captain_value = forecast_by_id[captain_id].predicted_points_1gw
    squad_double_count = sum(forecast.fixture_count > 1 for forecast in squad_forecasts)
    schedule_double_count = float((global_schedule_summary or {}).get("double_players", 0.0))
    schedule_blank_count = float((global_schedule_summary or {}).get("blank_players", 0.0))
    bench_value += 0.45 * squad_double_count + min(4.0, 0.035 * schedule_double_count) - min(2.5, 0.02 * schedule_blank_count)
    triple_captain_value += 0.35 * squad_double_count + min(2.5, 0.025 * schedule_double_count) - min(1.5, 0.01 * schedule_blank_count)
    return {
        "bench_boost": max(0.0, float(bench_value)),
        "triple_captain": max(0.0, float(triple_captain_value)),
    }


def _optimize_chip_schedule(
    week_chip_values: Mapping[int, Mapping[str, float]],
    bench_boost_available: bool,
    triple_captain_available: bool,
) -> Dict[int, str]:
    weeks = sorted(week_chip_values)
    memo: Dict[Tuple[int, bool, bool], Tuple[float, Dict[int, str]]] = {}

    def solve(index: int, bb_available: bool, tc_available: bool) -> Tuple[float, Dict[int, str]]:
        key = (index, bb_available, tc_available)
        if key in memo:
            return memo[key]
        if index >= len(weeks):
            memo[key] = (0.0, {})
            return memo[key]

        week = weeks[index]
        best_total, best_plan = solve(index + 1, bb_available, tc_available)
        best_action = "none"

        if bb_available:
            bb_total, bb_plan = solve(index + 1, False, tc_available)
            bb_total += float(week_chip_values[week].get("bench_boost", 0.0))
            if bb_total > best_total + 1e-9:
                best_total = bb_total
                best_plan = dict(bb_plan)
                best_action = "bench_boost"

        if tc_available:
            tc_total, tc_plan = solve(index + 1, bb_available, False)
            tc_total += float(week_chip_values[week].get("triple_captain", 0.0))
            if tc_total > best_total + 1e-9:
                best_total = tc_total
                best_plan = dict(tc_plan)
                best_action = "triple_captain"

        if best_action != "none":
            best_plan = dict(best_plan)
            best_plan[week] = best_action
        memo[key] = (best_total, best_plan)
        return memo[key]

    return solve(0, bench_boost_available, triple_captain_available)[1]


def _chip_choice_reason(
    current_week: int,
    chip_used: str,
    week_chip_values: Mapping[int, Mapping[str, float]],
    chip_schedule: Mapping[int, str],
) -> str:
    if chip_used == "none":
        return ""
    current_value = float(week_chip_values[current_week].get(chip_used, 0.0))
    future_values = [
        float(week_chip_values[week].get(chip_used, 0.0))
        for week in week_chip_values
        if week > current_week
    ]
    best_future = max(future_values, default=0.0)
    if chip_used == "bench_boost":
        return (
            "Optimizer chose Bench Boost here because the current estimated bench gain "
            f"({current_value:.2f}) beats the best remaining Bench Boost opportunity ({best_future:.2f})."
        )
    return (
        "Optimizer chose Triple Captain here because the current estimated captain upside "
        f"({current_value:.2f}) beats the best remaining Triple Captain opportunity ({best_future:.2f})."
    )


def _try_rebuild_squad(
    forecasts: Sequence[PlayerForecast], budget: float
) -> Optional[Tuple[List[SquadPlayer], float]]:
    for beam_width in (300, 800, 1600):
        try:
            return build_initial_squad(forecasts, budget=budget, beam_width=beam_width)
        except ValueError:
            continue
    return None


def _lookahead_transfer_choice(
    candidates: Sequence[object],
    current_squad: Sequence[SquadPlayer],
    bank: float,
    free_transfers: int,
    max_free_transfers: int,
    forecasts: Sequence[PlayerForecast],
    forecast_by_id: Dict[int, PlayerForecast],
    next_week_frame: pd.DataFrame,
    test_season: str,
    next_week: int,
    decision_weights: DecisionWeights,
    discount: float = 0.9,
    max_candidates: int = 3,
    projection: str = "schedule",
):
    """Pick this week's action (hold or one of the top transfer options) by
    immediate squad value plus the discounted best next-week transfer gain.

    Holding banks a free transfer, so the hold branch searches next week with
    the banked allowance — this is where 'wait one week and make a free
    double move' becomes visible to the optimizer. Future forecasts use only
    next week's known schedule (same leakage profile as the chip DP).
    Returns the chosen transfer option, or None to hold.
    """
    safe_forecast_by_id = _ensure_squad_forecasts(
        list(current_squad), dict(forecast_by_id), season=test_season, week=next_week
    )
    squad_ids = {player.player_id for player in current_squad}
    pool = sorted(
        (forecast for forecast in forecasts if forecast.player_id not in squad_ids),
        key=decision_weights.horizon_points,
        reverse=True,
    )[:40]

    best_option = None
    best_value = float("-inf")
    for option in [None, *list(candidates)[:max_candidates]]:
        if option is None:
            squad_after, bank_after, used, hit = list(current_squad), bank, 0, 0
        else:
            squad_after, bank_after = _apply_transfer(
                current_squad, bank, option.players_out, option.players_in, safe_forecast_by_id
            )
            used, hit = len(option.players_in), option.hit_cost
        immediate = _evaluate_squad(squad_after, safe_forecast_by_id, decision_weights) - hit

        ft_next = min(max_free_transfers, max(1, free_transfers - used + 1))
        squad_after_ids = {player.player_id for player in squad_after}
        current_pool_forecasts = [
            safe_forecast_by_id[player.player_id] for player in squad_after
        ] + [forecast for forecast in pool if forecast.player_id not in squad_after_ids]
        projected = _project_forecasts_to_week(
            current_pool_forecasts, next_week_frame, season=test_season, week=next_week, projection=projection
        )
        next_bundle = recommend_actions(
            squad_state=SquadState(
                season=test_season,
                week=next_week,
                squad_players=squad_after,
                bank=bank_after,
                free_transfers=ft_next,
                chips_available={},
            ),
            forecasts=projected,
            top_n_transfers=1,
            max_transfers_considered=ft_next,
            decision_weights=decision_weights,
        )
        next_gain = max(0.0, next_bundle.transfers[0].projected_gain) if next_bundle.transfers else 0.0
        value = immediate + discount * next_gain
        if value > best_value + 1e-9:
            best_value = value
            best_option = option
    return best_option


def run_rolling_squad_backtest(
    dataset: CanonicalDataset,
    test_season: str = "2025-26",
    initial_train_week_max: int = 10,
    start_week: int = 11,
    end_week: int = 30,
    alpha: float = 1.0,
    initial_budget: float = 100.0,
    max_free_transfers: int = 2,
    max_transfers_per_week: int = 1,
    min_projected_gain: float = 0.0,
    league_average_by_week: Optional[Mapping[int, float]] = None,
    llm_delta_lookup: Optional[Mapping[Tuple[int, int], Mapping[str, float]]] = None,
    llm_fields: str = "all",
    decision_weights: DecisionWeights = DEFAULT_DECISION_WEIGHTS,
    transfer_lookahead: int = 1,
    lookahead_discount: float = 0.9,
    lookahead_projection: str = "schedule",
    simulate_wildcard: bool = False,
    simulate_free_hit: bool = False,
    wildcard_min_gain: float = 12.0,
    free_hit_min_gain: float = 10.0,
    oracle_forecasts: bool = False,
) -> RollingSquadBacktestReport:
    if start_week <= initial_train_week_max:
        raise ValueError("start_week must be greater than initial_train_week_max.")

    eligible = dataset.training_frame.loc[
        (dataset.training_frame["season"].astype(str) == test_season)
        & (dataset.training_frame["week"].astype(int) >= start_week)
        & (dataset.training_frame["week"].astype(int) <= end_week)
        & dataset.training_frame["eligible_for_backtest"]
    ]
    simulated_weeks = sorted(eligible["week"].astype(int).unique().tolist())
    if not simulated_weeks:
        raise ValueError("No eligible backtest weeks found in the requested range.")
    schedule_summary_frame = (
        eligible.groupby("week", as_index=False)
        .agg(
            double_players=("double_gw", "sum"),
            blank_players=("blank_gw", "sum"),
        )
        .sort_values("week")
    )
    week_schedule_summary = {
        int(record["week"]): {
            "double_players": float(record["double_players"]),
            "blank_players": float(record["blank_players"]),
        }
        for record in schedule_summary_frame.to_dict(orient="records")
    }

    current_squad: List[SquadPlayer] | None = None
    bank = round(initial_budget, 2)
    free_transfers = 1
    bench_boost_used = False
    triple_captain_used = False
    wildcard_used = False
    free_hit_used = False
    week_results: List[BacktestWeekResult] = []
    total_predicted_points = 0.0
    total_actual_points = 0.0
    total_transfer_hits = 0

    for week in simulated_weeks:
        train_frame = _training_frame_for_week(dataset, test_season=test_season, week=week)
        model_suite = fit_model_suite_from_frame(
            train_frame=train_frame,
            feature_names=dataset.feature_columns,
            alpha=alpha,
        )
        week_frame = dataset.week_frame((test_season, week))
        forecasts = model_suite.predict_frame(week_frame)
        if llm_delta_lookup:
            forecasts = apply_llm_deltas(forecasts, llm_delta_lookup, week, fields=llm_fields)
        week_rows = _lookup_frame_by_player(week_frame)
        if oracle_forecasts:
            # DIAGNOSTIC ONLY — replaces every forecast with realized
            # outcomes so decisions act in "actual space". Absolute totals
            # are meaningless; only paired differences between oracle runs
            # carry information.
            forecasts = [
                _project_forecast_by_oracle(forecast, week_rows.get(forecast.player_id, {}), test_season, week)
                for forecast in forecasts
            ]
        forecast_by_id = _forecast_lookup(forecasts)

        bank_before = bank
        free_transfers_before = free_transfers
        notes: List[str] = []
        transfers_applied: List[BacktestTransferMove] = []
        candidate_transfers: List[BacktestTransferCandidate] = []
        candidate_transfer_options = []
        hit_cost = 0
        transfer_count_used = 0
        pre_move_squad_players: List[SquadPlayer] = []
        week_chip_override = "none"
        free_hit_revert: Optional[Tuple[List[SquadPlayer], float]] = None

        if current_squad is None:
            last_error: Optional[Exception] = None
            for beam_width in (300, 800, 1600, 3000):
                try:
                    current_squad, bank = build_initial_squad(
                        forecasts,
                        budget=initial_budget,
                        beam_width=beam_width,
                    )
                    if beam_width > 300:
                        notes.append(f"Initial squad builder retried with beam width {beam_width} for a legal budgeted squad.")
                    break
                except ValueError as error:
                    last_error = error
            if current_squad is None:
                current_squad, bank = build_cheapest_legal_squad(forecasts, budget=initial_budget)
                notes.append(
                    "Initial squad builder fell back to the cheapest legal squad search after the higher-upside beam search failed."
                )
            pre_move_squad_players = list(current_squad)
            notes.append(
                "Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget."
            )
        else:
            current_squad = _refresh_squad_prices(current_squad, week_frame)
            pre_move_squad_players = list(current_squad)
            safe_forecasts = _ensure_squad_forecasts(
                list(current_squad), dict(forecast_by_id), season=test_season, week=week
            )
            if simulate_wildcard and not wildcard_used:
                rebuild = _try_rebuild_squad(
                    forecasts, budget=bank + sum(player.sell_price for player in current_squad)
                )
                if rebuild is not None:
                    rebuilt_squad, rebuilt_bank = rebuild
                    wildcard_gain = _evaluate_squad(rebuilt_squad, safe_forecasts, decision_weights) - _evaluate_squad(
                        current_squad, safe_forecasts, decision_weights
                    )
                    if wildcard_gain >= wildcard_min_gain:
                        current_squad, bank = rebuilt_squad, rebuilt_bank
                        wildcard_used = True
                        week_chip_override = "wildcard"
                        notes.append(
                            f"Chip used: Wildcard — full rebuild projects +{wildcard_gain:.2f} squad value "
                            f"(threshold {wildcard_min_gain:g})."
                        )
            if week_chip_override == "none" and simulate_free_hit and not free_hit_used:
                rebuild = _try_rebuild_squad(
                    forecasts, budget=bank + sum(player.sell_price for player in current_squad)
                )
                if rebuild is not None:
                    rebuilt_squad, rebuilt_bank = rebuild
                    _, _, _, _, rebuilt_week_score = _optimize_lineup(rebuilt_squad, safe_forecasts, decision_weights)
                    _, _, _, _, current_week_score = _optimize_lineup(current_squad, safe_forecasts, decision_weights)
                    free_hit_gain = rebuilt_week_score - current_week_score
                    if free_hit_gain >= free_hit_min_gain:
                        free_hit_revert = (list(current_squad), bank)
                        current_squad, bank = rebuilt_squad, rebuilt_bank
                        free_hit_used = True
                        week_chip_override = "free_hit"
                        notes.append(
                            f"Chip used: Free Hit — one-week lineup gain +{free_hit_gain:.2f} "
                            f"(threshold {free_hit_min_gain:g}); squad reverts next week."
                        )
            squad_state = SquadState(
                season=test_season,
                week=week,
                squad_players=current_squad,
                bank=bank,
                free_transfers=free_transfers,
                chips_available={},
            )
            if week_chip_override != "none":
                bundle = None
            else:
                bundle = recommend_actions(
                squad_state=squad_state,
                forecasts=forecasts,
                top_n_transfers=max_transfers_per_week,
                max_transfers_considered=max_transfers_per_week,
                decision_weights=decision_weights,
            )
            candidate_transfer_options = list(bundle.transfers[:5]) if bundle is not None else []
            chosen_transfer = None
            if bundle is not None and bundle.transfers and bundle.transfers[0].projected_gain >= min_projected_gain:
                chosen_transfer = bundle.transfers[0]
            if bundle is not None and transfer_lookahead >= 2:
                upcoming_weeks = [candidate for candidate in simulated_weeks if candidate > week]
                if upcoming_weeks:
                    chosen_transfer = _lookahead_transfer_choice(
                        candidates=bundle.transfers,
                        current_squad=current_squad,
                        bank=bank,
                        free_transfers=free_transfers,
                        max_free_transfers=max_free_transfers,
                        forecasts=forecasts,
                        forecast_by_id=forecast_by_id,
                        next_week_frame=dataset.week_frame((test_season, upcoming_weeks[0])),
                        test_season=test_season,
                        next_week=upcoming_weeks[0],
                        decision_weights=decision_weights,
                        discount=lookahead_discount,
                        projection=lookahead_projection,
                    )
                    if chosen_transfer is None:
                        notes.append("Lookahead chose to bank the free transfer this week.")
            if chosen_transfer is not None:
                transfer_count_used = len(chosen_transfer.players_in)
                current_squad, bank = _apply_transfer(
                    current_squad,
                    bank,
                    chosen_transfer.players_out,
                    chosen_transfer.players_in,
                    forecast_by_id,
                )
                hit_cost = chosen_transfer.hit_cost
                total_transfer_hits += hit_cost
                transfers_applied.append(
                    BacktestTransferMove(
                        players_out=[
                            next(player.player_name for player in squad_state.squad_players if player.player_id == player_id)
                            for player_id in chosen_transfer.players_out
                        ],
                        players_in=[forecast_by_id[player_id].player_name for player_id in chosen_transfer.players_in],
                        projected_gain=chosen_transfer.projected_gain,
                        hit_cost=chosen_transfer.hit_cost,
                    )
                )
                if chosen_transfer.hit_cost:
                    notes.append(f"Transfer hit applied: -{chosen_transfer.hit_cost} points.")
            elif week_chip_override == "none":
                notes.append("No transfer was applied this week.")

        active_squad_state = SquadState(
            season=test_season,
            week=week,
            squad_players=current_squad,
            bank=bank,
            free_transfers=free_transfers,
            chips_available={
                "bench_boost": not bench_boost_used,
                "triple_captain": not triple_captain_used,
            },
        )
        active_bundle = recommend_actions(
            squad_state=active_squad_state,
            forecasts=forecasts,
            top_n_transfers=max_transfers_per_week,
            max_transfers_considered=max_transfers_per_week,
            decision_weights=decision_weights,
        )
        starters = list(active_bundle.starters)
        bench_order = list(active_bundle.bench_order)
        captain_id = int(active_bundle.captain_id)
        vice_captain_id = int(active_bundle.vice_captain_id)
        chip_advisories = [
            f"{advisory.chip} ({advisory.confidence:.2f}): {advisory.rationale}"
            for advisory in active_bundle.chip_advisories
        ]
        current_squad_forecasts = [forecast_by_id[player.player_id] for player in current_squad if player.player_id in forecast_by_id]
        remaining_weeks = [remaining_week for remaining_week in simulated_weeks if remaining_week >= week]
        week_chip_values: Dict[int, Dict[str, float]] = {}
        for remaining_week in remaining_weeks:
            if remaining_week == week:
                projected_forecasts = current_squad_forecasts
            else:
                future_frame = dataset.week_frame((test_season, remaining_week))
                projected_forecasts = _estimated_future_forecasts_for_current_squad(
                    squad_players=current_squad,
                    current_forecast_by_id=forecast_by_id,
                    future_week_frame=future_frame,
                    season=test_season,
                    week=remaining_week,
                )
            week_chip_values[remaining_week] = _chip_week_value_summary(
                squad_players=current_squad,
                squad_forecasts=projected_forecasts,
                global_schedule_summary=week_schedule_summary.get(remaining_week),
            )
        chip_schedule = _optimize_chip_schedule(
            week_chip_values=week_chip_values,
            bench_boost_available=not bench_boost_used,
            triple_captain_available=not triple_captain_used,
        )
        if week_chip_override != "none":
            chip_used = week_chip_override
            chip_reason = ""
        else:
            chip_used = chip_schedule.get(week, "none")
            chip_reason = _chip_choice_reason(
                current_week=week,
                chip_used=chip_used,
                week_chip_values=week_chip_values,
                chip_schedule=chip_schedule,
            )
        if chip_used == "bench_boost":
            bench_boost_used = True
            notes.append(f"Chip used: Bench Boost. {chip_reason}")
        elif chip_used == "triple_captain":
            triple_captain_used = True
            notes.append(f"Chip used: Triple Captain on {forecast_by_id[captain_id].player_name}. {chip_reason}")

        predicted_score = (
            sum(forecast_by_id[player_id].predicted_points_1gw for player_id in starters)
            + forecast_by_id[captain_id].predicted_points_1gw
            - hit_cost
        )
        if chip_used == "bench_boost":
            predicted_score = (
                sum(forecast_by_id[player.player_id].predicted_points_1gw for player in current_squad)
                + forecast_by_id[captain_id].predicted_points_1gw
                - hit_cost
            )
        elif chip_used == "triple_captain":
            predicted_score += forecast_by_id[captain_id].predicted_points_1gw

        actual_player_ids = {
            player.player_id for player in current_squad
        } | {
            player.player_id for player in pre_move_squad_players
        } | {
            player_id
            for option in candidate_transfer_options
            for player_id in option.players_in
        }
        actual_points = {
            player_id: float(week_rows.get(player_id, {}).get("label_points_1gw", 0.0))
            for player_id in actual_player_ids
        }
        actual_minutes = {
            player_id: float(week_rows.get(player_id, {}).get("label_minutes_1gw", 0.0))
            for player_id in actual_player_ids
        }
        pre_move_squad_entries = _snapshot_squad_entries(
            squad_players=pre_move_squad_players,
            forecast_by_id=forecast_by_id,
            actual_points=actual_points,
            actual_minutes=actual_minutes,
        )
        pre_move_player_by_id = {player.player_id: player for player in pre_move_squad_players}
        candidate_transfers = []
        for option in candidate_transfer_options:
            outgoing_players = [pre_move_player_by_id[player_id] for player_id in option.players_out if player_id in pre_move_player_by_id]
            incoming_players = [
                SquadPlayer(
                    player_id=forecast_by_id[player_id].player_id,
                    player_name=forecast_by_id[player_id].player_name,
                    team_id=forecast_by_id[player_id].team_id,
                    position=forecast_by_id[player_id].position,
                    sell_price=forecast_by_id[player_id].price,
                )
                for player_id in option.players_in
                if player_id in forecast_by_id
            ]
            candidate_transfers.append(
                BacktestTransferCandidate(
                    players_out=[player.player_name for player in outgoing_players],
                    players_in=[player.player_name for player in incoming_players],
                    projected_gain=option.projected_gain,
                    hit_cost=option.hit_cost,
                    explanation=option.explanation,
                    outgoing_players=_snapshot_squad_entries(
                        squad_players=outgoing_players,
                        forecast_by_id=forecast_by_id,
                        actual_points=actual_points,
                        actual_minutes=actual_minutes,
                    ),
                    incoming_players=_snapshot_squad_entries(
                        squad_players=incoming_players,
                        forecast_by_id=forecast_by_id,
                        actual_points=actual_points,
                        actual_minutes=actual_minutes,
                    ),
                )
            )
        if chip_used == "bench_boost":
            realized_starters = list(starters)
        else:
            realized_starters, autosub_notes = _apply_automatic_substitutions(
                squad_players=current_squad,
                starters=starters,
                bench_order=bench_order,
                actual_points=actual_points,
                actual_minutes=actual_minutes,
            )
            notes.extend(autosub_notes)
        effective_captain_id = _effective_captain(captain_id, vice_captain_id, actual_minutes)
        if chip_used == "bench_boost":
            actual_score = (
                sum(actual_points.get(player.player_id, 0.0) for player in current_squad)
                + actual_points.get(effective_captain_id, 0.0)
                - hit_cost
            )
        else:
            actual_score = (
                sum(actual_points.get(player_id, 0.0) for player_id in realized_starters)
                + actual_points.get(effective_captain_id, 0.0)
                - hit_cost
            )
        if chip_used == "triple_captain":
            actual_score += actual_points.get(effective_captain_id, 0.0)

        player_by_id = {player.player_id: player for player in current_squad}
        squad_entries: List[BacktestSquadEntry] = []
        for player in sorted(
            current_squad,
            key=lambda item: (
                item.position != "GK",
                item.position,
                -forecast_by_id[item.player_id].predicted_points_3gw,
                item.player_name,
            ),
        ):
            forecast = forecast_by_id[player.player_id]
            squad_entries.append(
                BacktestSquadEntry(
                    player_id=player.player_id,
                    player_name=player.player_name,
                    position=player.position,
                    team_id=player.team_id,
                    price=float(player.sell_price),
                    selected_role=_selected_role(player.player_id, starters, bench_order, captain_id, vice_captain_id),
                    realized_role=_realized_role(
                        player.player_id,
                        realized_starters,
                        captain_id,
                        effective_captain_id,
                        starters,
                        chip_used,
                        bench_order,
                    ),
                    predicted_points_1gw=float(forecast.predicted_points_1gw),
                    predicted_points_3gw=float(forecast.predicted_points_3gw),
                    predicted_points_5gw=float(forecast.predicted_points_5gw),
                    actual_points_1gw=float(actual_points.get(player.player_id, 0.0)),
                    predicted_minutes=float(forecast.predicted_minutes),
                    actual_minutes=float(actual_minutes.get(player.player_id, 0.0)),
                    appearance_probability=float(forecast.appearance_probability),
                )
            )

        free_transfers = min(
            max_free_transfers,
            max(1, free_transfers - transfer_count_used + 1),
        )
        if free_hit_revert is not None:
            current_squad, bank = free_hit_revert

        week_results.append(
            BacktestWeekResult(
                season=test_season,
                week=week,
                train_rows=int(len(train_frame)),
                bank_before=round(bank_before, 2),
                bank_after=round(bank, 2),
                free_transfers_before=free_transfers_before,
                free_transfers_after=free_transfers,
                pre_move_squad=pre_move_squad_entries,
                candidate_transfers=candidate_transfers,
                transfers_applied=transfers_applied,
                chip_used=chip_used,
                chip_reason=chip_reason,
                chip_advisories=chip_advisories,
                predicted_score=round(predicted_score, 2),
                actual_score=round(actual_score, 2),
                league_average_score=(
                    None if league_average_by_week is None or week not in league_average_by_week
                    else round(float(league_average_by_week[week]), 2)
                ),
                captain_id=captain_id,
                captain_name=player_by_id[captain_id].player_name,
                vice_captain_id=vice_captain_id,
                vice_captain_name=player_by_id[vice_captain_id].player_name,
                effective_captain_id=effective_captain_id,
                effective_captain_name=player_by_id[effective_captain_id].player_name,
                starters=list(starters),
                realized_starters=list(realized_starters),
                bench_order=list(bench_order),
                squad=squad_entries,
                notes=notes,
            )
        )
        total_predicted_points += predicted_score
        total_actual_points += actual_score

    train_seasons = sorted(
        dataset.training_frame.loc[dataset.training_frame["eligible_for_training"], "season"].astype(str).unique().tolist(),
        key=parse_season_start_year,
    )
    notes = [
        "The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.",
        "Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.",
        "This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.",
        "Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.",
        f"Weekly training expands through the prior deadline, so GW1-GW{initial_train_week_max} are included before the first simulated week.",
    ]
    if league_average_by_week is None:
        notes.append("League-average scores were not available for this run.")
    else:
        notes.append("League-average scores were pulled from official FPL event metadata when available.")
    week_count = max(len(week_results), 1)
    return RollingSquadBacktestReport(
        train_seasons=train_seasons,
        test_season=test_season,
        initial_train_week_max=initial_train_week_max,
        simulated_weeks=simulated_weeks,
        total_predicted_points=round(total_predicted_points, 2),
        total_actual_points=round(total_actual_points, 2),
        total_transfer_hits=total_transfer_hits,
        average_predicted_points=round(total_predicted_points / week_count, 2),
        average_actual_points=round(total_actual_points / week_count, 2),
        weeks=week_results,
        notes=notes,
    )


def report_to_markdown(report: RollingSquadBacktestReport) -> str:
    lines = [
        "# Rolling Squad Backtest Report",
        "",
        f"- Train seasons in scope: {', '.join(report.train_seasons)}",
        f"- In-season warm start: {report.test_season} GW1-GW{report.initial_train_week_max}",
        f"- Simulated weeks: GW{min(report.simulated_weeks)}-GW{max(report.simulated_weeks)}",
        f"- Total predicted points: {report.total_predicted_points:.2f}",
        f"- Total actual points: {report.total_actual_points:.2f}",
        f"- Average predicted points: {report.average_predicted_points:.2f}",
        f"- Average actual points: {report.average_actual_points:.2f}",
        f"- Total transfer hits: {report.total_transfer_hits}",
        "",
        "## Notes",
        "",
    ]
    lines.extend([f"- {note}" for note in report.notes])

    for week in report.weeks:
        lines.extend(
            [
                "",
                f"## GW{week.week}",
                "",
                f"- Train rows: {week.train_rows}",
                f"- Bank: {week.bank_before:.2f} -> {week.bank_after:.2f}",
                f"- Free transfers: {week.free_transfers_before} -> {week.free_transfers_after}",
                f"- Captain: {week.captain_name}",
                f"- Vice captain: {week.vice_captain_name}",
                f"- Effective captain: {week.effective_captain_name}",
                f"- Chip used: {week.chip_used}",
                f"- Predicted score: {week.predicted_score:.2f}",
                f"- Actual score: {week.actual_score:.2f}",
            ]
        )
        if week.chip_reason:
            lines.append(f"- Chip rationale: {week.chip_reason}")
        if week.chip_advisories:
            lines.extend([f"- Chip advisory: {advisory}" for advisory in week.chip_advisories])
        if week.league_average_score is not None:
            lines.append(f"- League average score: {week.league_average_score:.2f}")
        if week.transfers_applied:
            for transfer in week.transfers_applied:
                lines.append(
                    "- Transfer: "
                    + ", ".join(transfer.players_out)
                    + " -> "
                    + ", ".join(transfer.players_in)
                    + f" (projected gain {transfer.projected_gain:.2f}, hit {transfer.hit_cost})"
                )
        else:
            lines.append("- Transfer: none")
        if week.notes:
            lines.extend([f"- {note}" for note in week.notes])
        lines.extend(
            [
                "",
                "| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |",
                "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for player in week.squad:
            lines.append(
                f"| {player.selected_role} | {player.realized_role} | {player.player_name} | {player.position} | {player.team_id} | "
                f"{player.price:.1f} | {player.predicted_points_1gw:.2f} | {player.predicted_points_3gw:.2f} | "
                f"{player.predicted_points_5gw:.2f} | {player.actual_points_1gw:.2f} | {player.predicted_minutes:.1f} | {player.actual_minutes:.1f} |"
            )
    return "\n".join(lines)


def write_backtest_outputs(report: RollingSquadBacktestReport, output_dir: str) -> Dict[str, str]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    json_path = output_path / "rolling_squad_backtest.json"
    markdown_path = output_path / "rolling_squad_backtest.md"
    json_path.write_text(json.dumps(asdict(report), indent=2))
    markdown_path.write_text(report_to_markdown(report))
    return {"json": str(json_path), "markdown": str(markdown_path)}

"""Hybrid ML + evidence prompt builders for constrained Gemma decision ranking."""

from __future__ import annotations

from typing import Dict, List, Sequence

from .decision import _forecast_lookup
from .types import (
    EvidenceSnapshot,
    EvidenceEntitySummary,
    HybridDecisionContext,
    PlayerForecast,
    RecommendationBundle,
    SquadPlayer,
    SquadState,
    WeekState,
)


def _squad_forecast_lines(
    squad_players: Sequence[SquadPlayer],
    forecasts: Sequence[PlayerForecast],
) -> List[str]:
    forecast_by_id: Dict[int, PlayerForecast] = _forecast_lookup(forecasts)
    lines: List[str] = []
    for player in squad_players:
        forecast = forecast_by_id.get(player.player_id)
        if forecast is None:
            continue
        lines.append(
            f"- {player.player_name} ({player.position}, team={player.team_id}, price={forecast.price:.1f}) | "
            f"1gw={forecast.predicted_points_1gw:.2f} | 3gw={forecast.predicted_points_3gw:.2f} | "
            f"minutes={forecast.predicted_minutes:.0f} | appearance={forecast.appearance_probability:.2f}"
        )
    if not lines:
        lines.append("- No squad forecasts available.")
    return lines


def _entity_summary_lines(
    summaries: Sequence[EvidenceEntitySummary],
    header: str,
) -> List[str]:
    if not summaries:
        return [header, "- None"]
    lines = [header]
    for summary in summaries[:5]:
        source_names = ", ".join(summary.source_names[:3]) if summary.source_names else "unknown sources"
        snippets = " | ".join(summary.snippets[:2]) if summary.snippets else "no snippets"
        lines.append(
            f"- {summary.entity_name}: docs={summary.document_count}, latest={summary.latest_published_at}, "
            f"sources={source_names}, notes={snippets}"
        )
    return lines


def evidence_lines_from_snapshot(evidence_snapshot: EvidenceSnapshot | None) -> List[str]:
    if evidence_snapshot is None:
        return ["Evidence snapshot:", "- No deadline-scoped evidence snapshot was attached."]
    lines = [
        "Evidence snapshot:",
        f"- Documents: {evidence_snapshot.document_count}",
        f"- Lookback days: {evidence_snapshot.lookback_days}",
    ]
    for note in evidence_snapshot.notes:
        lines.append(f"- Note: {note}")
    lines.extend(_entity_summary_lines(evidence_snapshot.player_summaries, "Player evidence summaries:"))
    lines.extend(_entity_summary_lines(evidence_snapshot.team_summaries, "Team evidence summaries:"))
    return lines


def candidate_option_lines(bundle: RecommendationBundle) -> List[str]:
    lines: List[str] = []
    for option in bundle.candidate_options:
        lines.append(
            f"- [{option.option_id}] {option.label} | pred_score={option.predicted_score:.2f} | "
            f"gain={option.projected_gain:.2f} | hit={option.hit_cost} | captain={option.captain_name} | "
            f"vice={option.vice_captain_name} | chip={option.chip}"
        )
        lines.append(f"  starters={', '.join(option.starters)}")
        lines.append(f"  bench={', '.join(option.bench_order)}")
        lines.append(f"  rationale={option.rationale}")
    if not lines:
        lines.append("- [0] Hold squad | no legal alternatives were generated.")
    return lines


def build_hybrid_decision_prompt(
    season: str,
    week: int,
    deadline_ts: str,
    bank: float,
    free_transfers: int,
    squad_lines: Sequence[str],
    evidence_lines: Sequence[str],
    candidate_lines: Sequence[str],
) -> str:
    return "\n".join(
        [
            "You are choosing among legal pre-deadline FPL squad actions for one week.",
            f"Season: {season}",
            f"Week: {week}",
            f"Deadline: {deadline_ts}",
            f"Bank before moves: {bank:.2f}",
            f"Free transfers before moves: {free_transfers}",
            "",
            "Current squad and structured ML forecasts:",
            *squad_lines,
            "",
            *evidence_lines,
            "",
            "Legal candidate options from the optimizer:",
            *candidate_lines,
            "",
            "Task:",
            "Choose the single best option using only the pre-deadline information above.",
            "Return strict JSON with keys selected_option and reasoning_summary.",
            "selected_option must be one of the listed integer option ids.",
            "reasoning_summary must be a short list of factual bullet-style strings.",
            "Do not invent new transfers or use post-deadline information.",
        ]
    )


def build_hybrid_decision_context(
    week_state: WeekState,
    squad_state: SquadState,
    forecasts: Sequence[PlayerForecast],
    recommendation_bundle: RecommendationBundle,
) -> HybridDecisionContext:
    prompt = build_hybrid_decision_prompt(
        season=week_state.season,
        week=week_state.week,
        deadline_ts=week_state.deadline_ts,
        bank=squad_state.bank,
        free_transfers=squad_state.free_transfers,
        squad_lines=_squad_forecast_lines(squad_state.squad_players, forecasts),
        evidence_lines=evidence_lines_from_snapshot(recommendation_bundle.evidence_snapshot),
        candidate_lines=candidate_option_lines(recommendation_bundle),
    )
    return HybridDecisionContext(
        season=week_state.season,
        week=week_state.week,
        deadline_ts=week_state.deadline_ts,
        prompt=prompt,
        candidate_options=recommendation_bundle.candidate_options,
        supporting_sources=recommendation_bundle.supporting_sources,
        evidence_snapshot=recommendation_bundle.evidence_snapshot,
    )

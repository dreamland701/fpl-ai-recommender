"""Shared dataclasses used across the application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence


@dataclass(frozen=True)
class WeekEligibility:
    season: str
    week: int
    eligible_for_training: bool
    eligible_for_backtest: bool
    reason: str


@dataclass(frozen=True)
class WeekState:
    season: str
    week: int
    deadline_ts: str
    eligible: WeekEligibility
    fixture_count: int
    player_count: int
    notes: Sequence[str]
    source_timestamps: Dict[str, str]
    evidence_snapshot: Optional["EvidenceSnapshot"] = None


@dataclass(frozen=True)
class PlayerWeekRow:
    season: str
    week: int
    player_id: int
    player_name: str
    team_id: int
    position: str
    features: Dict[str, float]


@dataclass(frozen=True)
class PlayerWeekLabel:
    season: str
    week: int
    player_id: int
    next_gw_points: float
    next_3gw_points: float
    next_5gw_points: float
    next_gw_minutes: float
    next_gw_appearance_probability: float


@dataclass(frozen=True)
class PlayerForecast:
    season: str
    week: int
    player_id: int
    player_name: str
    team_id: int
    position: str
    price: float
    predicted_minutes: float
    predicted_points_1gw: float
    predicted_points_3gw: float
    predicted_points_5gw: float
    appearance_probability: float
    fixture_count: int
    uncertainty: float
    # Programme item 2 (2026-10-17): the 5GW head's per-fixture rate (per-week rate / 1 when the horizon heads are
    # not per fixture), so a decision horizon can add a terminal value for fixtures beyond its window.
    rate_5gw: float = 0.0


@dataclass(frozen=True)
class SquadPlayer:
    player_id: int
    player_name: str
    team_id: int
    position: str
    sell_price: float
    # What the manager paid; a fresh purchase sells at its own price.
    purchase_price: Optional[float] = None

    def __post_init__(self) -> None:
        if self.purchase_price is None:
            object.__setattr__(self, "purchase_price", self.sell_price)


@dataclass(frozen=True)
class SquadState:
    season: str
    week: int
    squad_players: Sequence[SquadPlayer]
    bank: float
    free_transfers: int
    chips_available: Dict[str, bool] = field(default_factory=dict)


@dataclass(frozen=True)
class TransferRecommendation:
    players_out: Sequence[int]
    players_in: Sequence[int]
    projected_gain: float
    hit_cost: int
    explanation: str


@dataclass(frozen=True)
class ChipAdvisory:
    chip: str
    confidence: float
    rationale: str


@dataclass(frozen=True)
class CandidateDecisionOption:
    option_id: int
    label: str
    players_out: Sequence[int]
    players_in: Sequence[int]
    players_out_names: Sequence[str]
    players_in_names: Sequence[str]
    projected_gain: float
    hit_cost: int
    predicted_score: float
    captain_id: int
    captain_name: str
    vice_captain_id: int
    vice_captain_name: str
    starters: Sequence[str]
    bench_order: Sequence[str]
    chip: str
    chip_confidence: float
    rationale: str


@dataclass(frozen=True)
class SourceDocument:
    title: str
    url: str
    source_name: str
    category: str
    published_at: str
    snippet: str


@dataclass(frozen=True)
class EvidenceDocument:
    title: str
    url: str
    source_name: str
    category: str
    published_at: str
    snippet: str
    content: str = ""
    player_name: str = ""
    team_name: str = ""
    trust_tier: str = ""
    hours_before_deadline: float = 0.0


@dataclass(frozen=True)
class EvidenceEntitySummary:
    entity_type: str
    entity_name: str
    document_count: int
    latest_published_at: str
    source_names: Sequence[str]
    categories: Sequence[str]
    snippets: Sequence[str]


@dataclass(frozen=True)
class EvidenceSnapshot:
    season: str
    week: int
    deadline_ts: str
    lookback_days: int
    document_count: int
    source_counts: Dict[str, int]
    category_counts: Dict[str, int]
    documents: Sequence[EvidenceDocument]
    player_summaries: Sequence[EvidenceEntitySummary]
    team_summaries: Sequence[EvidenceEntitySummary]
    notes: Sequence[str]


@dataclass(frozen=True)
class RecommendationBundle:
    season: str
    week: int
    transfers: Sequence[TransferRecommendation]
    captain_id: int
    vice_captain_id: int
    starters: Sequence[int]
    bench_order: Sequence[int]
    chip_advisories: Sequence[ChipAdvisory]
    confidence: float
    assumptions: Sequence[str]
    supporting_sources: Sequence[SourceDocument]
    candidate_options: Sequence[CandidateDecisionOption] = field(default_factory=list)
    evidence_snapshot: Optional[EvidenceSnapshot] = None


@dataclass(frozen=True)
class HybridDecisionContext:
    season: str
    week: int
    deadline_ts: str
    prompt: str
    candidate_options: Sequence[CandidateDecisionOption]
    supporting_sources: Sequence[SourceDocument]
    evidence_snapshot: Optional[EvidenceSnapshot] = None


@dataclass(frozen=True)
class CitedReport:
    title: str
    body: str
    stale_sources: Sequence[str]
    citations: Sequence[str]


@dataclass(frozen=True)
class FittedModelBundle:
    feature_names: Sequence[str]
    availability_path: str
    points_1gw_path: str
    points_3gw_path: str
    points_5gw_path: str
    per_fixture: bool = False  # heads fitted on per-fixture labels (FPL_PER_FIXTURE=1); see models.py
    per_fixture_horizon: bool = False  # 3GW/5GW heads per fixture too (table has fixtures_next_3/5)
    appearance_path: Optional[str] = None  # logistic P(appear) head (FPL_APPEARANCE_LOGISTIC=1)

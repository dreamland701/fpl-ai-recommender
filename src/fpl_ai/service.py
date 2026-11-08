"""Application service façade."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Sequence

from .api import OfficialSnapshotService
from .dataset import CanonicalDataset, WeekId
from .decision import recommend_actions as build_recommendation_bundle
from .evidence import build_evidence_snapshot_from_path
from .hybrid import build_hybrid_decision_context as build_hybrid_context
from .ingest import DEFAULT_COMPLETED_SEASONS, HistoricalDataIngestor, SyncHistorySummary
from .models import ForecastModelSuite, load_model_suite, train_model_suite
from .research import generate_cited_report
from .types import (
    CitedReport,
    EvidenceSnapshot,
    HybridDecisionContext,
    RecommendationBundle,
    SourceDocument,
    SquadState,
    WeekEligibility,
    WeekState,
)


class FPLRecommender:
    def __init__(
        self,
        dataset: Optional[CanonicalDataset] = None,
        model_suite: Optional[ForecastModelSuite] = None,
        snapshot_service: Optional[OfficialSnapshotService] = None,
    ):
        self.dataset = dataset
        self.model_suite = model_suite
        self.snapshot_service = snapshot_service or OfficialSnapshotService()

    @classmethod
    def from_history_root(cls, history_root: str) -> "FPLRecommender":
        return cls(dataset=CanonicalDataset.from_history_root(history_root))

    @classmethod
    def from_training_csv(cls, training_csv: str, model_dir: Optional[str] = None) -> "FPLRecommender":
        dataset = CanonicalDataset.from_csv(training_csv)
        model_suite = load_model_suite(Path(model_dir)) if model_dir else None
        return cls(dataset=dataset, model_suite=model_suite)

    def save_training_rows(self, output_path: str) -> None:
        if self.dataset is None:
            raise ValueError("Dataset is not loaded.")
        self.dataset.to_csv(output_path)

    def sync_history(
        self,
        history_root: str,
        completed_seasons=DEFAULT_COMPLETED_SEASONS,
        current_season: str = "2025-26",
        current_max_gw: int = 30,
    ) -> SyncHistorySummary:
        ingestor = HistoricalDataIngestor(history_root=history_root)
        return ingestor.sync_history(
            completed_seasons=completed_seasons,
            current_season=current_season,
            current_max_gw=current_max_gw,
        )

    def bootstrap_training_data(
        self,
        history_root: str,
        training_output: str,
        completed_seasons=DEFAULT_COMPLETED_SEASONS,
        current_season: str = "2025-26",
        current_max_gw: int = 30,
    ) -> SyncHistorySummary:
        ingestor = HistoricalDataIngestor(history_root=history_root)
        summary = ingestor.bootstrap_training_data(
            training_output=training_output,
            completed_seasons=completed_seasons,
            current_season=current_season,
            current_max_gw=current_max_gw,
        )
        self.dataset = CanonicalDataset.from_csv(training_output)
        return summary

    def build_week_state(self, deadline_ts: Optional[str] = None, week_id: Optional[WeekId] = None) -> WeekState:
        if deadline_ts:
            return self.snapshot_service.build_week_state(deadline_ts)
        if week_id is None or self.dataset is None:
            raise ValueError("Provide either deadline_ts or week_id with a loaded dataset.")
        return self.dataset.build_week_state(week_id)

    def build_evidence_snapshot(
        self,
        deadline_ts: str,
        evidence_path: str,
        curated_only: bool = True,
        max_documents: int = 6,
        lookback_days: int = 14,
    ) -> EvidenceSnapshot:
        week_state = self.snapshot_service.build_week_state(deadline_ts)
        return build_evidence_snapshot_from_path(
            season=week_state.season,
            week=week_state.week,
            deadline_ts=week_state.deadline_ts,
            input_path=evidence_path,
            curated_only=curated_only,
            max_documents=max_documents,
            lookback_days=lookback_days,
        )

    def build_player_rows(self, week_id: WeekId):
        if self.dataset is None:
            raise ValueError("Dataset is not loaded.")
        return self.dataset.build_player_rows(week_id)

    def build_labels(self, week_id: WeekId, horizons=(1, 3, 5)):
        if self.dataset is None:
            raise ValueError("Dataset is not loaded.")
        return self.dataset.build_labels(week_id, horizons=horizons)

    def get_week_eligibility(self, week_id: WeekId) -> WeekEligibility:
        if self.dataset is None:
            raise ValueError("Dataset is not loaded.")
        return self.dataset.get_week_eligibility(week_id)

    def train_models(self, model_dir: str, alpha: float = 1.0):
        if self.dataset is None:
            raise ValueError("Dataset is not loaded.")
        manifest = train_model_suite(self.dataset, Path(model_dir), alpha=alpha)
        self.model_suite = load_model_suite(Path(model_dir))
        return manifest

    def predict_player_outcomes(self, week_id: WeekId):
        if self.dataset is None or self.model_suite is None:
            raise ValueError("Dataset and model suite must be loaded before predicting.")
        return self.model_suite.predict_week(self.dataset, week_id)

    def predict_live_player_outcomes(self, deadline_ts: str):
        if self.dataset is None or self.model_suite is None:
            raise ValueError("Dataset and model suite must be loaded before predicting.")
        official_frame = self.snapshot_service.build_current_week_frame(deadline_ts)
        live_frame = self.dataset.build_live_week_frame(official_frame)
        return self.model_suite.predict_frame(live_frame)

    def recommend_actions(
        self,
        week_id: WeekId,
        squad_state: SquadState,
        supporting_sources: Sequence[SourceDocument] = (),
        evidence_snapshot: EvidenceSnapshot | None = None,
    ) -> RecommendationBundle:
        forecasts = self.predict_player_outcomes(week_id)
        return build_recommendation_bundle(
            squad_state=squad_state,
            forecasts=forecasts,
            supporting_sources=supporting_sources,
            evidence_snapshot=evidence_snapshot,
        )

    def build_hybrid_decision_context(
        self,
        deadline_ts: str,
        squad_state: SquadState,
        evidence_path: str | None = None,
        curated_only: bool = True,
        max_documents: int = 6,
        lookback_days: int = 14,
        top_n_transfers: int = 5,
        max_transfers_considered: int = 2,
    ) -> HybridDecisionContext:
        week_state = self.snapshot_service.build_week_state(deadline_ts)
        evidence_snapshot = None
        if evidence_path:
            evidence_snapshot = build_evidence_snapshot_from_path(
                season=week_state.season,
                week=week_state.week,
                deadline_ts=week_state.deadline_ts,
                input_path=evidence_path,
                curated_only=curated_only,
                max_documents=max_documents,
                lookback_days=lookback_days,
            )
        forecasts = self.predict_live_player_outcomes(deadline_ts)
        recommendation_bundle = build_recommendation_bundle(
            squad_state=squad_state,
            forecasts=forecasts,
            top_n_transfers=top_n_transfers,
            max_transfers_considered=max_transfers_considered,
            evidence_snapshot=evidence_snapshot,
        )
        return build_hybrid_context(
            week_state=week_state,
            squad_state=squad_state,
            forecasts=forecasts,
            recommendation_bundle=recommendation_bundle,
        )

    def generate_cited_report(self, recommendation_bundle: RecommendationBundle) -> CitedReport:
        return generate_cited_report(recommendation_bundle)

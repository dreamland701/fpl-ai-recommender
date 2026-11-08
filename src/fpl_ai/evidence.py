"""Typed evidence snapshot helpers for official/news/Reddit retrieval inputs."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from typing import Dict, Iterable, List, Optional, Sequence

import pandas as pd

from .config import DEFAULT_CURATED_SOURCES
from .llm_data import normalize_evidence_corpus
from .types import EvidenceDocument, EvidenceEntitySummary, EvidenceSnapshot


def _parse_timestamp(value: str) -> Optional[datetime]:
    if not value:
        return None
    normalized = str(value).replace("Z", "+00:00")
    try:
        timestamp = datetime.fromisoformat(normalized)
    except ValueError:
        try:
            timestamp = parsedate_to_datetime(str(value))
        except (TypeError, ValueError, IndexError):
            return None
    if timestamp.tzinfo is None:
        return timestamp.replace(tzinfo=timezone.utc)
    return timestamp.astimezone(timezone.utc)


def _normalize_text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _trust_tier(category: str) -> str:
    if category.startswith("official_"):
        return "high"
    if category == "trusted_news":
        return "medium"
    if category == "reddit":
        return "low"
    return "unknown"


def _source_age_budget(category: str) -> Optional[int]:
    for source in DEFAULT_CURATED_SOURCES:
        if source.category == category:
            return source.max_age_days
    return None


def _eligible_evidence_rows(
    evidence_frame: pd.DataFrame,
    deadline_ts: str,
    max_documents: int,
    lookback_days: int,
) -> pd.DataFrame:
    if evidence_frame.empty:
        return pd.DataFrame()
    deadline = _parse_timestamp(deadline_ts)
    if deadline is None:
        return pd.DataFrame()
    earliest = deadline - timedelta(days=lookback_days)
    frame = evidence_frame.copy()
    if "published_ts" not in frame.columns:
        frame["published_ts"] = frame["published_at"].map(_parse_timestamp)
    eligible = frame.loc[
        frame["published_ts"].map(lambda value: value is not None and earliest <= value <= deadline)
    ].copy()
    if eligible.empty:
        return eligible
    category_priority = {
        "official_club": 0,
        "official_fpl": 1,
        "official_premier_league": 2,
        "official_scout": 3,
        "trusted_news": 4,
        "reddit": 5,
    }
    eligible["category_priority"] = eligible["category"].map(lambda value: category_priority.get(str(value), 9))
    eligible["hours_before_deadline"] = eligible["published_ts"].map(
        lambda value: abs((deadline - value).total_seconds()) / 3600.0
    )
    eligible = eligible.sort_values(
        ["category_priority", "hours_before_deadline", "source_name", "title"],
        ascending=[True, True, True, True],
    ).head(max_documents)
    return eligible.reset_index(drop=True)


def _documents_from_rows(rows: pd.DataFrame) -> List[EvidenceDocument]:
    documents: List[EvidenceDocument] = []
    for record in rows.to_dict(orient="records"):
        documents.append(
            EvidenceDocument(
                title=_normalize_text(record.get("title")),
                url=_normalize_text(record.get("url")),
                source_name=_normalize_text(record.get("source_name")),
                category=_normalize_text(record.get("category")),
                published_at=_normalize_text(record.get("published_at")),
                snippet=_normalize_text(record.get("snippet")),
                content=_normalize_text(record.get("content")),
                player_name=_normalize_text(record.get("player_name")),
                team_name=_normalize_text(record.get("team_name")),
                trust_tier=_trust_tier(_normalize_text(record.get("category"))),
                hours_before_deadline=float(record.get("hours_before_deadline") or 0.0),
            )
        )
    return documents


def _entity_summaries(documents: Sequence[EvidenceDocument], entity_type: str) -> List[EvidenceEntitySummary]:
    grouped: Dict[str, List[EvidenceDocument]] = defaultdict(list)
    for document in documents:
        name = document.player_name if entity_type == "player" else document.team_name
        if name:
            grouped[name].append(document)

    summaries: List[EvidenceEntitySummary] = []
    for entity_name, rows in grouped.items():
        latest_published_at = max((row.published_at for row in rows), default="")
        source_names = sorted({row.source_name for row in rows if row.source_name})
        categories = sorted({row.category for row in rows if row.category})
        snippets = [row.snippet for row in rows if row.snippet][:3]
        summaries.append(
            EvidenceEntitySummary(
                entity_type=entity_type,
                entity_name=entity_name,
                document_count=len(rows),
                latest_published_at=latest_published_at,
                source_names=source_names,
                categories=categories,
                snippets=snippets,
            )
        )
    summaries.sort(key=lambda summary: (-summary.document_count, summary.entity_name))
    return summaries


def build_evidence_snapshot(
    season: str,
    week: int,
    deadline_ts: str,
    evidence_frame: pd.DataFrame,
    max_documents: int = 6,
    lookback_days: int = 14,
) -> EvidenceSnapshot:
    rows = _eligible_evidence_rows(
        evidence_frame=evidence_frame,
        deadline_ts=deadline_ts,
        max_documents=max_documents,
        lookback_days=lookback_days,
    )
    documents = _documents_from_rows(rows)
    source_counts = dict(Counter(document.source_name for document in documents if document.source_name))
    category_counts = dict(Counter(document.category for document in documents if document.category))

    notes: List[str] = []
    if not documents:
        notes.append("No curated evidence documents matched the deadline window.")
    else:
        notes.append(f"Selected {len(documents)} timestamp-safe documents before the deadline.")
        low_trust_count = sum(1 for document in documents if document.trust_tier == "low")
        if low_trust_count:
            notes.append(f"{low_trust_count} selected document(s) came from low-trust Reddit sources.")
        stale_categories = [
            category
            for category in sorted(category_counts)
            if (
                _source_age_budget(category) is not None
                and any(
                    document.category == category and document.hours_before_deadline > (_source_age_budget(category) * 24.0)
                    for document in documents
                )
            )
        ]
        if stale_categories:
            notes.append(
                "Some selected documents exceeded their source freshness budget: " + ", ".join(stale_categories)
            )

    return EvidenceSnapshot(
        season=season,
        week=week,
        deadline_ts=deadline_ts,
        lookback_days=lookback_days,
        document_count=len(documents),
        source_counts=source_counts,
        category_counts=category_counts,
        documents=documents,
        player_summaries=_entity_summaries(documents, "player"),
        team_summaries=_entity_summaries(documents, "team"),
        notes=notes,
    )


def build_evidence_snapshot_from_path(
    season: str,
    week: int,
    deadline_ts: str,
    input_path: str,
    curated_only: bool = True,
    max_documents: int = 6,
    lookback_days: int = 14,
) -> EvidenceSnapshot:
    frame = normalize_evidence_corpus(input_path, curated_only=curated_only)
    return build_evidence_snapshot(
        season=season,
        week=week,
        deadline_ts=deadline_ts,
        evidence_frame=frame,
        max_documents=max_documents,
        lookback_days=lookback_days,
    )


def evidence_snapshot_to_dict(snapshot: EvidenceSnapshot) -> Dict[str, object]:
    return asdict(snapshot)

"""Curated-source policy and cited report generation."""

from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from typing import Iterable, List, Optional, Sequence
from urllib.parse import urlparse

from .config import DEFAULT_CURATED_SOURCES, CuratedSource
from .types import CitedReport, RecommendationBundle, SourceDocument


def curated_sources() -> Sequence[CuratedSource]:
    return DEFAULT_CURATED_SOURCES


def _domain(url: str) -> str:
    return urlparse(url).netloc.lower()


def _matching_source_policy(document: SourceDocument) -> Optional[CuratedSource]:
    document_domain = _domain(document.url)
    for source in DEFAULT_CURATED_SOURCES:
        if _domain(source.url) in document_domain or document_domain in _domain(source.url):
            return source
    return None


def _parse_timestamp(value: str) -> Optional[datetime]:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        timestamp = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if timestamp.tzinfo is None:
        return timestamp.replace(tzinfo=timezone.utc)
    return timestamp.astimezone(timezone.utc)


def stale_sources(documents: Sequence[SourceDocument], now: Optional[datetime] = None) -> List[str]:
    now = now or datetime.now(timezone.utc)
    stale: List[str] = []
    for document in documents:
        policy = _matching_source_policy(document)
        if policy is None:
            stale.append(f"{document.title} ({document.url}) is outside the curated source whitelist.")
            continue
        published_at = _parse_timestamp(document.published_at)
        if published_at is None:
            stale.append(f"{document.title} ({document.url}) is missing a valid publication timestamp.")
            continue
        if now - published_at > timedelta(days=policy.max_age_days):
            stale.append(
                f"{document.title} ({document.url}) is older than the {policy.max_age_days}-day freshness budget for {policy.name}."
            )
    return stale


def generate_cited_report(recommendation_bundle: RecommendationBundle) -> CitedReport:
    citations = [
        f"[{index}] {document.source_name}: {document.title} - {document.url}"
        for index, document in enumerate(recommendation_bundle.supporting_sources, start=1)
    ]
    stale = stale_sources(recommendation_bundle.supporting_sources)

    transfer_lines = [
        f"- Transfer out {transfer.players_out} for {transfer.players_in} (projected gain {transfer.projected_gain}, hit {transfer.hit_cost})"
        for transfer in recommendation_bundle.transfers
    ]
    if not transfer_lines:
        transfer_lines = ["- No positive-EV transfer found from the current search space."]

    advisory_lines = [
        f"- {advisory.chip}: {advisory.rationale} (confidence {advisory.confidence:.2f})"
        for advisory in recommendation_bundle.chip_advisories
    ]
    if not advisory_lines:
        advisory_lines = ["- No chip triggered the current advisory thresholds."]

    body = "\n".join(
        [
            f"Week {recommendation_bundle.week} recommendation confidence: {recommendation_bundle.confidence:.2f}.",
            "",
            "Transfers:",
            *transfer_lines,
            "",
            f"Captain: {recommendation_bundle.captain_id}",
            f"Vice captain: {recommendation_bundle.vice_captain_id}",
            f"Starters: {list(recommendation_bundle.starters)}",
            f"Bench order: {list(recommendation_bundle.bench_order)}",
            "",
            "Chip advisories:",
            *advisory_lines,
            "",
            "Assumptions:",
            *[f"- {assumption}" for assumption in recommendation_bundle.assumptions],
        ]
    )
    return CitedReport(
        title=f"FPL Recommendation Report - {recommendation_bundle.season} GW{recommendation_bundle.week}",
        body=body,
        stale_sources=stale,
        citations=citations,
    )

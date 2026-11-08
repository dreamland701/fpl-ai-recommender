#!/usr/bin/env python3
"""Re-attach per-player evidence to an exported player-forecast corpus.

The corpus exporter selects evidence at week level: the same top-N documents
go to every player in the gameweek. That was tolerable when evidence was
FPL-specific (Scout articles), but with the Guardian 2022-25 backfill
(~150 general football articles/week) week-level selection degrades to
generic match reports shared by all 128 players — which would make the
E1-vs-E2 "does text help" comparison unfair to text.

This script rebuilds `metadata.evidence_documents` per player-week: only
documents published inside the lookback window before the deadline that
mention the player's name (diacritic-stripped, word-boundary, case-sensitive
so short surnames like Son don't match the common noun) survive. Players
nobody wrote about get an empty list, which the dataset builder renders as
"no evidence — prefer near-zero deltas". Baselines and labels are copied
through untouched, so an E2 dataset built from the output differs from E1
only in evidence.

Usage:
  PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py \
    --corpus reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v1.jsonl \
    --evidence reports/evidence_guardian_football_2022_23.jsonl \
    --evidence reports/evidence_guardian_football_2023_24.jsonl \
    --evidence reports/evidence_guardian_football_2024_25.jsonl \
    --evidence reports/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl \
    --output reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v2_player_evidence.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

import pandas as pd

from fpl_ai.llm_data import _parse_timestamp, normalize_evidence_corpus


ANALYSIS_TITLE = re.compile(
    r"scout report|scout selection|team news|predicted line|transfer radar|"
    r"ones to watch|differentials?|best (fpl )?captain|captain for gameweek|"
    r"lessons from|fpl|fantasy premier league|bonus points|"
    r"price (rise|fall|change)|injur(y|ies) (list|round|update)|squad for|"
    r"defensive contribution",
    re.IGNORECASE,
)
ANALYSIS_FIRST = False


def _strip_diacritics(text: str) -> str:
    return "".join(
        char for char in unicodedata.normalize("NFD", text) if unicodedata.category(char) != "Mn"
    )


def _name_pattern(player_name: str) -> re.Pattern | None:
    """Word-boundary pattern for the player's full name or surname.

    Case-sensitive on diacritic-stripped text: 'Son' must not match 'son of'.
    Single-letter or empty tokens are ignored.
    """
    cleaned = _strip_diacritics(player_name).strip()
    tokens = [token for token in cleaned.split() if len(token) > 1]
    if not tokens:
        return None
    alternatives = {re.escape(cleaned)} | {re.escape(tokens[-1])}
    return re.compile(r"\b(?:" + "|".join(sorted(alternatives, key=len, reverse=True)) + r")\b")


def _load_evidence(paths: list[Path], curated_only: bool) -> pd.DataFrame:
    frames = [normalize_evidence_corpus(str(path), curated_only=curated_only) for path in paths]
    merged = pd.concat(frames, ignore_index=True)
    merged = merged.drop_duplicates(subset=["url", "published_at", "title"])
    merged = merged.sort_values("published_ts", ascending=False).reset_index(drop=True)
    merged["search_title"] = merged["title"].map(_strip_diacritics)
    merged["search_content"] = merged["content"].map(_strip_diacritics)
    return merged


def _to_document(record: dict, max_chars: int, center_pos: int | None = None) -> dict:
    content = record["content"]
    if center_pos is not None and len(content) > max_chars:
        # Center on the player's mention rather than keeping the prefix:
        # long documents (podcast transcripts run 30-50k chars) put the
        # player-specific discussion well past a 6000-char prefix cut on
        # average (measured ~70% into the transcript), which silently
        # threw away the very reason this document was matched. Short
        # documents (news articles, front-loaded ledes) are unaffected
        # since the `len(content) > max_chars` guard only fires when
        # truncation was already happening.
        half = max_chars // 2
        start = max(0, min(center_pos - half, len(content) - max_chars))
        content = content[start : start + max_chars]
    else:
        content = content[:max_chars]
    return {
        "title": record["title"],
        "url": record["url"],
        "source_name": record["source_name"],
        "category": record["category"],
        "published_at": record["published_at"],
        "snippet": record["snippet"],
        "content": content,
        "player_name": "",
        "team_name": "",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--corpus", required=True, type=Path)
    parser.add_argument("--evidence", action="append", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--lookback-days", type=int, default=7)
    parser.add_argument("--cutoff-hours", type=float, default=0.0,
                        help="Only attach documents published at least this many hours before the deadline. "
                        "Live runs snapshot ~17 h before the deadline, so training and backtests should use 24 "
                        "(Wes, 2026-10-10): with 0, 18%% of training articles came from the last day, which a live "
                        "decision never sees.")
    parser.add_argument("--max-docs", type=int, default=3)
    parser.add_argument("--analysis-first", action="store_true",
                        help="Rank FPL/Scout-analysis titles above match reports before mention count.")
    parser.add_argument("--max-chars-per-doc", type=int, default=6000)
    parser.add_argument(
        "--include-non-curated",
        action="store_true",
        help="Keep evidence whose URL domain is outside DEFAULT_CURATED_SOURCES (e.g. canonical skysports.com "
        "articles, or hand-built files that are curated by construction but hide behind news.google.com URLs).",
    )
    args = parser.parse_args()
    global ANALYSIS_FIRST
    ANALYSIS_FIRST = bool(args.analysis_first)

    evidence = _load_evidence(args.evidence, curated_only=not args.include_non_curated)
    print(f"normalized evidence: {len(evidence)} documents from {len(args.evidence)} files")

    pattern_cache: dict[str, re.Pattern | None] = {}
    week_key: tuple[str, int] | None = None
    week_records: list[dict] = []
    rows_written = 0
    rows_with_evidence: Counter[str] = Counter()
    docs_attached: Counter[str] = Counter()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    lookback = pd.Timedelta(days=args.lookback_days)
    with args.corpus.open() as corpus_handle, args.output.open("w") as output_handle:
        for line in corpus_handle:
            row = json.loads(line)
            season = str(row["season"])
            key = (season, int(row["week"]))
            if key != week_key:
                week_key = key
                deadline = _parse_timestamp(row["deadline_ts"])
                if deadline is None:
                    week_records = []
                else:
                    cutoff = deadline - pd.Timedelta(hours=args.cutoff_hours)
                    mask = (evidence["published_ts"] <= cutoff) & (
                        evidence["published_ts"] >= deadline - lookback
                    )
                    week_records = evidence.loc[mask].to_dict(orient="records")

            player_name = str(row["metadata"].get("player_name") or "")
            if player_name not in pattern_cache:
                pattern_cache[player_name] = _name_pattern(player_name)
            pattern = pattern_cache[player_name]

            documents: list[dict] = []
            if pattern is not None and week_records:
                scored: list[tuple[int, int, int, dict]] = []
                for index, record in enumerate(week_records):
                    title_hits = len(pattern.findall(record["search_title"]))
                    content_match = pattern.search(record["search_content"])
                    content_hits = len(pattern.findall(record["search_content"])) if content_match else 0
                    if title_hits or content_hits:
                        # Recency tiebreak comes free: week_docs is newest-first.
                        center = content_match.start() if content_match else 0
                        scored.append((3 * title_hits + content_hits, -index, center, record))
                # Quality-aware ranking (2026-09-10, Wes: "the Scout should
                # recommend him and the LM should see it"). Ranking purely by
                # mention count handed every slot to 25k-char match reports —
                # GW4 Calafiori had 10 candidate docs and got 3 match reports,
                # so the FPL-analysis pieces never entered the corpus at all
                # and the split builder's quality preference had nothing to
                # pick from. Sort FPL/Scout-genre titles first, then mentions.
                if ANALYSIS_FIRST:
                    scored.sort(
                        key=lambda item: (
                            1 if ANALYSIS_TITLE.search(str(item[3].get("title") or "")) else 0,
                            item[0],
                            item[1],
                        ),
                        reverse=True,
                    )
                else:
                    scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
                documents = [
                    _to_document(record, args.max_chars_per_doc, center_pos=center)
                    for _, _, center, record in scored[: args.max_docs]
                ]

            row["metadata"]["evidence_documents"] = documents
            output_handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            rows_written += 1
            if documents:
                rows_with_evidence[season] += 1
                docs_attached[season] += len(documents)
            if rows_written % 50000 == 0:
                print(f"{rows_written} rows...")

    print(f"done: {rows_written} rows -> {args.output}")
    print("rows with evidence by season:", dict(sorted(rows_with_evidence.items())))
    print("documents attached by season:", dict(sorted(docs_attached.items())))


if __name__ == "__main__":
    main()

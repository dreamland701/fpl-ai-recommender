"""Build a focused official FPL/PL Scout + Sky podcast full-text evidence corpus."""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Tuple

from fpl_ai.llm_data import normalize_evidence_records, select_evidence_for_deadline


OFFICIAL_PL_SOURCE = "Premier League"
SKY_PODCAST_SOURCES = {
    "Sky Sports Fantasy Podcast",
    "Sky Sports Premier League Podcast",
}
REAL_FULLTEXT_STATUSES = {
    "full_text_extracted",
    "metadata_summary",
    "rss_description_full_text",
    "rss_episode_summary",
}


def _clean_value(value: Any) -> Any:
    if isinstance(value, float) and math.isnan(value):
        return ""
    if isinstance(value, dict):
        return {key: _clean_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_clean_value(item) for item in value]
    return value


def _read_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    materialized = [_clean_value(dict(row)) for row in rows]
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=True, allow_nan=False) for row in materialized)
        + ("\n" if materialized else "")
    )


def _merge_key(row: Mapping[str, Any]) -> Tuple[str, str, str]:
    return (
        str(row.get("title", "")).strip(),
        str(row.get("source_name", "")).strip(),
        str(row.get("published_at", "")).strip(),
    )


def _is_real_fulltext(row: Mapping[str, Any]) -> bool:
    status = str(row.get("extraction_status", "")).strip()
    text = str(row.get("full_text") or row.get("content") or "").strip()
    snippet = str(row.get("snippet") or "").strip()
    if status == "metadata_summary" and len(text) >= 40:
        return True
    if status in REAL_FULLTEXT_STATUSES and len(text) >= 80:
        return True
    return bool(text and snippet and text != snippet and len(text) >= 400)


def _clean_article_text(text: Any) -> str:
    return " ".join(str(text or "").replace("-->", " ").split())


def _merge_preserved_fulltext(
    base_rows: List[Dict[str, Any]],
    preserved_rows: List[Dict[str, Any]],
) -> tuple[List[Dict[str, Any]], int]:
    preserved = {
        _merge_key(row): row
        for row in preserved_rows
        if row.get("source_name") == OFFICIAL_PL_SOURCE
        and row.get("extraction_status") in {"full_text_extracted", "metadata_summary"}
        and row.get("full_text")
    }
    merged = []
    copied = 0
    for row in base_rows:
        updated = dict(row)
        source_name = str(row.get("source_name", ""))
        status = str(row.get("extraction_status", "") or "")
        key = _merge_key(row)
        if key in preserved:
            for field in ("resolved_url", "full_text", "full_text_chars", "extraction_status"):
                updated[field] = preserved[key].get(field, "")
            updated["full_text"] = _clean_article_text(updated.get("full_text", ""))
            updated["full_text_chars"] = len(str(updated.get("full_text", "")))
            updated["content"] = updated.get("full_text", updated.get("content", ""))
            if updated.get("resolved_url"):
                updated["url"] = updated["resolved_url"]
            updated["full_text_kind"] = (
                "official_pl_article_body"
                if updated.get("extraction_status") == "full_text_extracted"
                else "official_pl_metadata_summary"
            )
            copied += 1
        elif source_name in SKY_PODCAST_SOURCES and status in {"rss_description_full_text", "rss_episode_summary"}:
            updated["full_text_kind"] = "sky_podcast_rss_description"
        elif not _is_real_fulltext(updated):
            updated.pop("full_text", None)
            updated.pop("full_text_chars", None)
            updated["extraction_status"] = status or "snippet_only"
            updated["full_text_kind"] = ""
        merged.append(updated)
    return merged, copied


def _focused_rows(rows: Iterable[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    focused = []
    for row in rows:
        source_name = str(row.get("source_name", ""))
        if source_name != OFFICIAL_PL_SOURCE and source_name not in SKY_PODCAST_SOURCES:
            continue
        if not _is_real_fulltext(row):
            continue
        focused.append(dict(row))
    focused.sort(key=lambda row: (int(row.get("week") or 0), str(row.get("published_at", "")), str(row.get("source_name", ""))))
    return focused


def _write_packets(rows: List[Dict[str, Any]], packets_output: Path, max_documents: int, lookback_days: int) -> int:
    frame = normalize_evidence_records(rows, curated_only=False)
    windows = {}
    for row in rows:
        week = int(row["week"])
        windows[week] = {
            "season": row.get("season", ""),
            "week": week,
            "window_start": row.get("window_start", ""),
            "deadline_ts": row.get("deadline_ts", ""),
        }
    packets = []
    for week in sorted(windows):
        window = windows[week]
        documents = select_evidence_for_deadline(
            frame,
            deadline_ts=str(window["deadline_ts"]),
            max_documents=max_documents,
            lookback_days=lookback_days,
        )
        packets.append(
            {
                **window,
                "document_count": len(documents),
                "documents": [asdict(document) for document in documents],
            }
        )
    _write_jsonl(packets_output, packets)
    return len(packets)


def _report(
    merged_rows: List[Dict[str, Any]],
    focused: List[Dict[str, Any]],
    copied_preserved: int,
    packet_rows: int,
    output: Path,
    packets_output: Path,
) -> Dict[str, Any]:
    total_by_source = Counter(str(row.get("source_name", "")) for row in merged_rows)
    real_by_source = Counter(str(row.get("source_name", "")) for row in merged_rows if _is_real_fulltext(row))
    focused_by_source = Counter(str(row.get("source_name", "")) for row in focused)
    focused_by_week: Dict[str, int] = defaultdict(int)
    focused_chars_by_source: Dict[str, int] = defaultdict(int)
    for row in focused:
        focused_by_week[f"GW{row.get('week')}"] += 1
        focused_chars_by_source[str(row.get("source_name", ""))] += int(row.get("full_text_chars") or len(str(row.get("full_text", ""))))
    return {
        "merged_rows": len(merged_rows),
        "focused_fulltext_rows": len(focused),
        "packet_rows": packet_rows,
        "preserved_official_pl_fulltext_rows_copied": copied_preserved,
        "total_rows_by_source": dict(total_by_source.most_common()),
        "real_fulltext_rows_by_source": dict(real_by_source.most_common()),
        "focused_rows_by_source": dict(focused_by_source.most_common()),
        "focused_rows_by_week": dict(sorted(focused_by_week.items(), key=lambda item: int(item[0][2:]))),
        "focused_fulltext_chars_by_source": dict(focused_chars_by_source),
        "documents_output": str(output),
        "packets_output": str(packets_output),
        "notes": [
            "Sky podcast full text is RSS episode description text, not an audio transcript.",
            "Premier League rows are official FPL/PL Scout article bodies when canonical PL URLs were recoverable.",
            "Google News Sky Sports article rows remain snippet-only unless collected through direct source feeds.",
        ],
        "samples": [
            {
                "week": row.get("week"),
                "source_name": row.get("source_name"),
                "title": row.get("title"),
                "published_at": row.get("published_at"),
                "full_text_kind": row.get("full_text_kind"),
                "full_text_chars": row.get("full_text_chars") or len(str(row.get("full_text", ""))),
                "preview": str(row.get("full_text") or row.get("content") or "")[:700],
            }
            for row in focused[:8]
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="reports/evidence_2025_26_gw1_30_google_news_v3_podcasts.jsonl")
    parser.add_argument("--preserved-fulltext", default="reports/evidence_2025_26_gw1_30_google_news_pl_fulltext.jsonl")
    parser.add_argument("--merged-output", default="reports/evidence_2025_26_gw1_30_v3_podcasts_pl_fulltext.jsonl")
    parser.add_argument("--focused-output", default="reports/evidence_2025_26_gw1_30_fpl_sky_fulltext_focus.jsonl")
    parser.add_argument("--packets-output", default="reports/evidence_packets_2025_26_gw1_30_fpl_sky_fulltext_focus.jsonl")
    parser.add_argument("--report-output", default="reports/evidence_2025_26_gw1_30_fpl_sky_fulltext_focus_report.json")
    parser.add_argument("--max-documents-per-week", type=int, default=30)
    parser.add_argument("--lookback-days", type=int, default=14)
    args = parser.parse_args()

    base_rows = _read_jsonl(Path(args.base))
    preserved_rows = _read_jsonl(Path(args.preserved_fulltext))
    merged, copied = _merge_preserved_fulltext(base_rows, preserved_rows)
    focused = _focused_rows(merged)

    _write_jsonl(Path(args.merged_output), merged)
    _write_jsonl(Path(args.focused_output), focused)
    packet_rows = _write_packets(
        focused,
        packets_output=Path(args.packets_output),
        max_documents=args.max_documents_per_week,
        lookback_days=args.lookback_days,
    )
    report = _report(
        merged_rows=merged,
        focused=focused,
        copied_preserved=copied,
        packet_rows=packet_rows,
        output=Path(args.focused_output),
        packets_output=Path(args.packets_output),
    )
    Path(args.report_output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report_output).write_text(json.dumps(report, indent=2, ensure_ascii=True, allow_nan=False))
    print(json.dumps(report, indent=2, ensure_ascii=True, allow_nan=False))


if __name__ == "__main__":
    main()

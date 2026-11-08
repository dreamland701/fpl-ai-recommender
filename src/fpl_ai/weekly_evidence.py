"""Historical weekly evidence backfill for timestamp-safe LLM training."""

from __future__ import annotations

import json
import re
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence
from urllib.parse import parse_qs, unquote, urlparse
from xml.etree import ElementTree

import pandas as pd
import requests

from .dataset import CanonicalDataset
from .evidence_collect import (
    ACTIONABILITY_KEYWORDS,
    FPL_KEYWORDS,
    _has_keyword,
    _mentioned_entities,
    _normalize_text,
    _parse_timestamp,
    _strip_html,
)
from .llm_data import normalize_evidence_records, select_evidence_for_deadline, write_normalized_evidence


GOOGLE_NEWS_RSS_URL = "https://news.google.com/rss/search"
GOOGLE_NEWS_PARAMS = {"hl": "en-US", "gl": "US", "ceid": "US:en"}
SKY_PODCAST_FEEDS: Mapping[str, str] = {
    "Sky Sports Fantasy Podcast": "https://feeds.captivate.fm/sky-sports-fantasy/",
    "Sky Sports Premier League Podcast": "https://feeds.captivate.fm/sky-sports-premierleague/",
}

OFFICIAL_CLUB_SOURCES: Mapping[str, Sequence[str]] = {
    "Arsenal": ("arsenal.com",),
    "Aston Villa": ("avfc.co.uk",),
    "Bournemouth": ("afcb.co.uk",),
    "Brentford": ("brentfordfc.com",),
    "Brighton": ("brightonandhovealbion.com",),
    "Burnley": ("burnleyfootballclub.com",),
    "Chelsea": ("chelseafc.com",),
    "Crystal Palace": ("cpfc.co.uk",),
    "Everton": ("evertonfc.com",),
    "Fulham": ("fulhamfc.com",),
    "Leeds": ("leedsunited.com",),
    "Liverpool": ("liverpoolfc.com",),
    "Man City": ("mancity.com",),
    "Man Utd": ("manutd.com",),
    "Newcastle": ("newcastleunited.com",),
    "Nottingham Forest": ("nottinghamforest.co.uk",),
    "Spurs": ("tottenhamhotspur.com",),
    "Sunderland": ("safc.com",),
    "West Ham": ("whufc.com",),
    "Wolves": ("wolves.co.uk",),
}

TRUSTED_NEWS_SOURCES = {
    "BBC Sport",
    "BBC",
    "The Guardian",
    "Sky Sports",
    "The Athletic",
    "Yahoo Sports",
    "Reuters",
    "ESPN",
    "Forbes",
}

NON_FOOTBALL_FPL_KEYWORDS = (
    "bill",
    "electric",
    "electricity",
    "florida power",
    "rate hike",
    "rate increase",
    "settlement",
    "utility",
)

EQUIVALENT_SOURCE_DOMAINS: Mapping[str, Sequence[str]] = {
    "bbc.com": ("bbc.com", "bbc.co.uk"),
    "bbc.co.uk": ("bbc.com", "bbc.co.uk"),
    "espn.com": ("espn.com", "espn.co.uk"),
    "espn.co.uk": ("espn.com", "espn.co.uk"),
    "si.com": ("si.com", "sportsillustrated.com"),
    "sportsillustrated.com": ("si.com", "sportsillustrated.com"),
}


@dataclass(frozen=True)
class WeekEvidenceWindow:
    season: str
    week: int
    window_start: str
    deadline_ts: str


@dataclass(frozen=True)
class WeeklyEvidenceBackfillReport:
    season: str
    start_week: int
    end_week: int
    document_rows: int
    packet_rows: int
    source_counts: Dict[str, int]
    category_counts: Dict[str, int]
    documents_output: str
    packets_output: str
    notes: Sequence[str]


class SearchResolutionBlocked(RuntimeError):
    """Raised when a search provider blocks automated title resolution."""


def _domain(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def _article_search_title(title: str, source_name: str = "") -> str:
    clean = title
    suffixes = [" - Premier League", " | Premier League"]
    if source_name:
        suffixes.extend([f" - {source_name}", f" | {source_name}"])
    for suffix in suffixes:
        if clean.endswith(suffix):
            clean = clean[: -len(suffix)]
    return " ".join(clean.split())


def _allowed_domains(source_url: str) -> Sequence[str]:
    domain = _domain(source_url)
    return EQUIVALENT_SOURCE_DOMAINS.get(domain, (domain,) if domain else ())


def _domain_matches(source_url: str, target_url: str) -> bool:
    target_domain = _domain(target_url)
    allowed_domains = _allowed_domains(source_url)
    return bool(target_domain and any(target_domain == domain or target_domain.endswith(f".{domain}") for domain in allowed_domains))


def _extract_google_target_url(location: str) -> str:
    if not location:
        return ""
    if "google.com/sorry/" in location:
        raise SearchResolutionBlocked("google_search_blocked")
    if "google.com/url" not in location:
        return location
    parsed = urlparse(location)
    return parse_qs(parsed.query).get("q", [""])[0]


def _extract_search_result_url(html: str, source_url: str) -> str:
    candidates = []
    candidates.extend(match.group(1) for match in re.finditer(r'href="/url\?q=([^"&]+)', html, flags=re.I))
    candidates.extend(match.group(1) for match in re.finditer(r'href="(https?://[^"]+)"', html, flags=re.I))
    for candidate in candidates:
        target = unquote(candidate)
        if target.startswith("http") and _domain_matches(source_url, target):
            return target
    return ""


def _decode_google_news_url(url: str, interval: float = 0.0) -> str:
    if "news.google.com/" not in url:
        return ""
    try:
        from googlenewsdecoder import gnewsdecoder
    except ImportError:
        return ""
    result = gnewsdecoder(url, interval=interval)
    if isinstance(result, dict) and result.get("status") is True:
        decoded = str(result.get("decoded_url", ""))
        return decoded if decoded.startswith("http") else ""
    return ""


def _resolve_premierleague_url(title: str, session: requests.Session, timeout: float = 10.0) -> str:
    query = f'site:premierleague.com/en/news/ "{_article_search_title(title, "Premier League")}"'
    response = session.get(
        "https://www.google.com/search",
        params={"q": query, "btnI": "1", "hl": "en"},
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False,
        timeout=timeout,
    )
    target = _extract_google_target_url(response.headers.get("location", ""))
    if not target:
        target = _extract_search_result_url(response.text, "https://www.premierleague.com")
    if "premierleague.com" not in _domain(target):
        return ""
    return target


def _resolve_premierleague_row_url(row: Mapping[str, object], session: requests.Session, timeout: float = 10.0) -> str:
    decoded_url = _decode_google_news_url(str(row.get("url", "")), interval=0.0)
    if decoded_url and "premierleague.com" in _domain(decoded_url):
        return decoded_url
    return _resolve_premierleague_url(str(row.get("title", "")), session=session, timeout=timeout)


def _resolve_article_url(
    title: str,
    source_name: str,
    source_url: str,
    session: requests.Session,
    timeout: float = 10.0,
) -> str:
    domain = _domain(source_url)
    site_part = f"site:{domain} " if domain else ""
    query = f'{site_part}"{_article_search_title(title, source_name)}" "{source_name}"'
    response = session.get(
        "https://www.google.com/search",
        params={"q": query, "btnI": "1", "hl": "en"},
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False,
        timeout=timeout,
    )
    target = _extract_google_target_url(response.headers.get("location", ""))
    if not target:
        target = _extract_search_result_url(response.text, source_url)
    if not target.startswith("http"):
        return ""
    if domain and not _domain_matches(source_url, target):
        return ""
    return target


def _extract_premierleague_article_text(html: str) -> str:
    paragraphs = []
    for match in re.finditer(r"<p[^>]*>(.*?)</p>", html, flags=re.S | re.I):
        text = _strip_html(match.group(1))
        text = " ".join(text.replace("-->", " ").split())
        if not text:
            continue
        lowered = text.lower()
        if lowered.startswith("external link") or "cookie" in lowered:
            continue
        paragraphs.append(text)
    # De-duplicate while preserving order because PL pages repeat some teaser blocks.
    seen = set()
    unique = []
    for paragraph in paragraphs:
        if paragraph in seen:
            continue
        seen.add(paragraph)
        unique.append(paragraph)
    return "\n\n".join(unique)


def _extract_meta_description(html: str) -> str:
    descriptions = []
    for match in re.finditer(r"<meta[^>]+>", html, flags=re.I):
        tag = match.group(0)
        if not any(name in tag for name in ("description", "og:description", "twitter:description")):
            continue
        content_match = re.search(r'content="([^"]*)"', tag, flags=re.I)
        if not content_match:
            continue
        text = _normalize_text(unescape(content_match.group(1)))
        if text and text not in descriptions:
            descriptions.append(text)
    return descriptions[0] if descriptions else ""


def _extract_page_title(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, flags=re.S | re.I)
    return _strip_html(match.group(1)) if match else ""


def _rss_text_any(item: ElementTree.Element, tags: Sequence[str]) -> str:
    for tag in tags:
        found = item.find(tag)
        if found is not None and found.text:
            return _normalize_text(found.text)
    return ""


def _clean_sky_podcast_episode_text(text: str) -> str:
    cleaned = _strip_html(unescape(text))
    boilerplate_markers = (
        "Make sure to give Sky Sports Fantasy Podcast a follow",
        "Make sure to give Sky Sports Fantasy a follow",
        "To join our Sky Sports mini league",
        "Listen to every episode of the Sky Sports Fantasy Podcast here",
        "Listen to every episode of the Sky Sports Premier League Podcast here",
        "Listen to every episode of One on One from Sky Sports here",
        "You can listen to the Sky Sports Fantasy Podcast on your smart speaker",
        "You can listen to the Sky Sports Premier League Podcast on your smart speaker",
        "You can listen to One on One on your smart speaker",
        "For all the latest Premier League news",
        "For all the latest football news",
        "For advertising opportunities email",
        "To get in touch with the podcast email",
        "To get in touch with us, please email",
        "If you're new to One on One, please give us a follow",
        "Don't forget, as well as listening to the podcast",
    )
    marker_positions = [cleaned.find(marker) for marker in boilerplate_markers if marker in cleaned]
    if marker_positions:
        cleaned = cleaned[: min(marker_positions)].strip()
    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", cleaned) if sentence.strip()]
    deduped = []
    seen = set()
    for sentence in sentences:
        normalized = " ".join(sentence.lower().split())
        if normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(sentence)
    return " ".join(deduped).strip()


def _strings_from_json(value: object, key: str) -> List[str]:
    values: List[str] = []
    if isinstance(value, dict):
        for dict_key, dict_value in value.items():
            if str(dict_key).lower() == key.lower():
                if isinstance(dict_value, str):
                    values.append(dict_value)
                elif isinstance(dict_value, list):
                    values.extend(str(item) for item in dict_value if isinstance(item, (str, int, float)))
            else:
                values.extend(_strings_from_json(dict_value, key))
    elif isinstance(value, list):
        for item in value:
            values.extend(_strings_from_json(item, key))
    return values


def _extract_json_article_text(html: str) -> str:
    for match in re.finditer(
        r"<script[^>]+type=[\"']application/ld\+json[\"'][^>]*>(.*?)</script>",
        html,
        flags=re.S | re.I,
    ):
        script_text = unescape(match.group(1)).strip()
        if not script_text:
            continue
        try:
            data = json.loads(script_text)
        except json.JSONDecodeError:
            continue
        for article_body in _strings_from_json(data, "articleBody"):
            text = _strip_html(article_body)
            if len(text) >= 80:
                return text

    for match in re.finditer(r'"articleBody"\s*:\s*("(?:(?:\\.)|[^"\\])*")', html, flags=re.S | re.I):
        try:
            text = _strip_html(json.loads(match.group(1)))
        except json.JSONDecodeError:
            text = _strip_html(match.group(1).strip('"'))
        if len(text) >= 80:
            return text
    return ""


def _extract_generic_article_text(html: str) -> str:
    json_text = _extract_json_article_text(html)
    if json_text:
        return json_text
    paragraphs = []
    for match in re.finditer(r"<p[^>]*>(.*?)</p>", html, flags=re.S | re.I):
        text = _strip_html(match.group(1))
        if len(text) < 30:
            continue
        lowered = text.lower()
        if any(noise in lowered for noise in ("cookie", "privacy policy", "newsletter", "advertisement")):
            continue
        paragraphs.append(text)
    seen = set()
    unique = []
    for paragraph in paragraphs:
        normalized = " ".join(paragraph.split())
        if normalized in seen:
            continue
        seen.add(normalized)
        unique.append(paragraph)
    return "\n\n".join(unique)


def enrich_premierleague_fulltext(
    input_path: str,
    output_path: str,
    report_output: str,
    max_rows: Optional[int] = None,
    sleep_seconds: float = 0.25,
    session: Optional[requests.Session] = None,
) -> Dict[str, object]:
    session = session or requests.Session()
    rows = [json.loads(line) for line in Path(input_path).read_text().splitlines() if line.strip()]
    enriched = []
    attempted = 0
    resolved = 0
    extracted = 0
    errors: List[str] = []
    for row in rows:
        updated = dict(row)
        if row.get("source_url") == "https://www.premierleague.com" and row.get("category") in {
            "official_scout",
            "official_premier_league",
        }:
            if max_rows is None or attempted < max_rows:
                attempted += 1
                try:
                    resolved_url = _resolve_premierleague_row_url(row, session=session)
                    if resolved_url:
                        resolved += 1
                        page = session.get(resolved_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
                        page.raise_for_status()
                        full_text = _extract_premierleague_article_text(page.text)
                        if not full_text:
                            fallback_text = _extract_meta_description(page.text) or _extract_page_title(page.text)
                            if fallback_text:
                                full_text = fallback_text
                        updated["resolved_url"] = resolved_url
                        updated["full_text"] = full_text
                        updated["full_text_chars"] = len(full_text)
                        updated["extraction_status"] = (
                            "full_text_extracted"
                            if _extract_premierleague_article_text(page.text)
                            else ("metadata_summary" if full_text else "resolved_no_text")
                        )
                        if full_text:
                            updated["content"] = full_text
                            extracted += 1
                    else:
                        updated["extraction_status"] = "resolve_failed"
                except SearchResolutionBlocked as exc:
                    updated["extraction_status"] = "resolve_blocked"
                    errors.append(f"{row.get('title')}: {exc}")
                except Exception as exc:
                    updated["extraction_status"] = "error"
                    errors.append(f"{row.get('title')}: {type(exc).__name__}: {exc}")
                if sleep_seconds > 0:
                    time.sleep(sleep_seconds)
            else:
                updated["extraction_status"] = "skipped_max_rows"
        enriched.append(updated)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(json.dumps(row, ensure_ascii=True) for row in enriched) + ("\n" if enriched else ""))
    report = {
        "input": input_path,
        "output": output_path,
        "rows": len(rows),
        "attempted": attempted,
        "resolved": resolved,
        "full_text_extracted": extracted,
        "errors": errors[:20],
    }
    report_path = Path(report_output)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2))
    return report


def enrich_evidence_fulltext(
    input_path: str,
    output_path: str,
    report_output: str,
    max_rows: Optional[int] = None,
    sleep_seconds: float = 0.25,
    source_name_regex: Optional[str] = None,
    category_regex: Optional[str] = None,
    request_timeout: float = 10.0,
    output_every: int = 25,
    session: Optional[requests.Session] = None,
) -> Dict[str, object]:
    session = session or requests.Session()
    rows = [json.loads(line) for line in Path(input_path).read_text().splitlines() if line.strip()]
    enriched = []
    attempted = 0
    resolved = 0
    extracted = 0
    errors: List[str] = []
    status_counts: Dict[str, int] = {}
    source_pattern = re.compile(source_name_regex, flags=re.I) if source_name_regex else None
    category_pattern = re.compile(category_regex, flags=re.I) if category_regex else None
    for row in rows:
        updated = dict(row)
        if row.get("full_text"):
            updated.setdefault("extraction_status", "full_text_existing")
            enriched.append(updated)
            continue
        if source_pattern and not source_pattern.search(str(row.get("source_name", ""))):
            updated["extraction_status"] = updated.get("extraction_status") or "skipped_source_filter"
            status_counts[str(updated["extraction_status"])] = status_counts.get(str(updated["extraction_status"]), 0) + 1
            enriched.append(updated)
            continue
        if category_pattern and not category_pattern.search(str(row.get("category", ""))):
            updated["extraction_status"] = updated.get("extraction_status") or "skipped_category_filter"
            status_counts[str(updated["extraction_status"])] = status_counts.get(str(updated["extraction_status"]), 0) + 1
            enriched.append(updated)
            continue
        if max_rows is not None and attempted >= max_rows:
            updated["extraction_status"] = updated.get("extraction_status") or "skipped_max_rows"
            status_counts[str(updated["extraction_status"])] = status_counts.get(str(updated["extraction_status"]), 0) + 1
            enriched.append(updated)
            continue
        attempted += 1
        try:
            source_url = str(row.get("source_url") or "")
            if source_url == "https://www.premierleague.com":
                resolved_url = _resolve_premierleague_row_url(row, session=session, timeout=request_timeout)
            else:
                resolved_url = _decode_google_news_url(str(row.get("url", "")), interval=0.0)
                if resolved_url and source_url and not _domain_matches(source_url, resolved_url):
                    resolved_url = ""
                if not resolved_url:
                    resolved_url = _resolve_article_url(
                        title=str(row.get("title", "")),
                        source_name=str(row.get("source_name", "")),
                        source_url=source_url,
                        session=session,
                        timeout=request_timeout,
                    )
            if not resolved_url:
                updated["extraction_status"] = "resolve_failed"
            else:
                resolved += 1
                page = session.get(resolved_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=request_timeout)
                page.raise_for_status()
                if source_url == "https://www.premierleague.com":
                    full_text = _extract_premierleague_article_text(page.text)
                    if not full_text:
                        fallback_text = _extract_meta_description(page.text) or _extract_page_title(page.text)
                        if fallback_text:
                            full_text = fallback_text
                else:
                    full_text = _extract_generic_article_text(page.text)
                updated["resolved_url"] = resolved_url
                updated["full_text"] = full_text
                updated["full_text_chars"] = len(full_text)
                updated["extraction_status"] = (
                    "full_text_extracted"
                    if full_text and not (source_url == "https://www.premierleague.com" and full_text in {_extract_meta_description(page.text), _extract_page_title(page.text)})
                    else ("metadata_summary" if full_text else "resolved_no_text")
                )
                if full_text:
                    updated["content"] = full_text
                    extracted += 1
        except SearchResolutionBlocked as exc:
            updated["extraction_status"] = "resolve_blocked"
            errors.append(f"{row.get('title')}: {exc}")
        except Exception as exc:
            updated["extraction_status"] = "error"
            errors.append(f"{row.get('title')}: {type(exc).__name__}: {exc}")
        status_counts[str(updated.get("extraction_status", ""))] = status_counts.get(str(updated.get("extraction_status", "")), 0) + 1
        enriched.append(updated)
        if sleep_seconds > 0:
            time.sleep(sleep_seconds)
        if output_every > 0 and attempted > 0 and attempted % output_every == 0:
            output = Path(output_path)
            output.parent.mkdir(parents=True, exist_ok=True)
            partial_rows = enriched + rows[len(enriched) :]
            output.write_text(
                "\n".join(json.dumps(item, ensure_ascii=True) for item in partial_rows)
                + ("\n" if partial_rows else "")
            )
            partial_report = {
                "input": input_path,
                "output": output_path,
                "rows": len(rows),
                "attempted": attempted,
                "resolved": resolved,
                "full_text_extracted": extracted,
                "status_counts": status_counts,
                "errors": errors[:50],
                "partial": True,
            }
            Path(report_output).parent.mkdir(parents=True, exist_ok=True)
            Path(report_output).write_text(json.dumps(partial_report, indent=2))

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(json.dumps(row, ensure_ascii=True) for row in enriched) + ("\n" if enriched else ""))
    report = {
        "input": input_path,
        "output": output_path,
        "rows": len(rows),
        "attempted": attempted,
        "resolved": resolved,
        "full_text_extracted": extracted,
        "status_counts": status_counts,
        "errors": errors[:50],
    }
    report_path = Path(report_output)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2))
    return report


def _week_deadline_windows(
    dataset: CanonicalDataset,
    season: str,
    start_week: int,
    end_week: int,
    default_lookback_days: int,
) -> List[WeekEvidenceWindow]:
    windows: List[WeekEvidenceWindow] = []
    previous_deadline: Optional[datetime] = None
    for week in range(start_week, end_week + 1):
        week_frame = dataset.week_frame((season, week))
        kickoff_values = week_frame.get("kickoff_time", pd.Series(dtype=str)).dropna().astype(str)
        kickoff_ts = min((_parse_timestamp(value) for value in kickoff_values), default=None)
        if kickoff_ts is None:
            continue
        deadline = kickoff_ts - timedelta(minutes=90)
        window_start = previous_deadline or (deadline - timedelta(days=default_lookback_days))
        windows.append(
            WeekEvidenceWindow(
                season=season,
                week=week,
                window_start=window_start.isoformat(),
                deadline_ts=deadline.isoformat(),
            )
        )
        previous_deadline = deadline
    return windows


def _google_date(value: datetime) -> str:
    return value.astimezone(timezone.utc).date().isoformat()


def _google_week_queries(week: int, window_start: datetime, deadline: datetime) -> List[Dict[str, str]]:
    after = _google_date(window_start - timedelta(days=1))
    before = _google_date(deadline + timedelta(days=1))
    official_domains = " OR ".join(f"site:{domain}" for domains in OFFICIAL_CLUB_SOURCES.values() for domain in domains)
    return [
        {
            "source_key": "google_news_fpl",
            "category_hint": "trusted_news",
            "query": f'("Fantasy Premier League" OR "FPL Gameweek" OR "FPL tips" OR "Gameweek {week}") after:{after} before:{before}',
        },
        {
            "source_key": "google_news_official_scout",
            "category_hint": "official_scout",
            "query": f'(site:premierleague.com/news) (FPL OR "Fantasy Premier League" OR "Gameweek {week}") after:{after} before:{before}',
        },
        {
            "source_key": "google_news_team_news",
            "category_hint": "trusted_news",
            "query": f'("team news" OR injury OR injured OR fitness OR "press conference") "Premier League" after:{after} before:{before}',
        },
        {
            "source_key": "google_news_sky_sports",
            "category_hint": "trusted_news",
            "query": f'(site:skysports.com) ("team news" OR injury OR injured OR fitness OR "Premier League") after:{after} before:{before}',
        },
        {
            "source_key": "google_news_official_clubs",
            "category_hint": "official_club",
            "query": f'({official_domains}) (injury OR fitness OR training OR "team news" OR "press conference") after:{after} before:{before}',
        },
    ]


def _rss_text(item: ElementTree.Element, tag: str) -> str:
    found = item.find(tag)
    return _normalize_text(found.text if found is not None else "")


def _classify_google_item(source_name: str, source_url: str, title: str, category_hint: str) -> str:
    domain = _domain(source_url)
    if "premierleague.com" in domain and ("fpl" in title.lower() or "fantasy premier league" in title.lower()):
        return "official_scout"
    if "premierleague.com" in domain:
        return "official_premier_league"
    if any(domain.endswith(club_domain) for domains in OFFICIAL_CLUB_SOURCES.values() for club_domain in domains):
        return "official_club"
    if "reddit.com" in domain or "reddit" in source_name.lower():
        return "reddit"
    if source_name in TRUSTED_NEWS_SOURCES:
        return "trusted_news"
    return category_hint


def _fetch_google_news_query(
    session: requests.Session,
    query: Mapping[str, str],
    window: WeekEvidenceWindow,
    max_items: int,
    player_aliases: Mapping[str, str],
    team_aliases: Mapping[str, str],
) -> List[Dict[str, object]]:
    response = session.get(
        GOOGLE_NEWS_RSS_URL,
        params={**GOOGLE_NEWS_PARAMS, "q": query["query"]},
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    response.raise_for_status()
    root = ElementTree.fromstring(response.text)
    deadline = _parse_timestamp(window.deadline_ts)
    window_start = _parse_timestamp(window.window_start)
    if deadline is None or window_start is None:
        return []

    rows: List[Dict[str, object]] = []
    for item in root.findall(".//item"):
        published_ts = _parse_timestamp(_rss_text(item, "pubDate"))
        if published_ts is None or published_ts < window_start or published_ts > deadline:
            continue
        source = item.find("source")
        source_name = _normalize_text(source.text if source is not None else "Google News")
        source_url = _normalize_text(source.attrib.get("url") if source is not None else "")
        title = _rss_text(item, "title")
        link = _rss_text(item, "link")
        snippet = _strip_html(unescape(_rss_text(item, "description")))
        combined_text = " ".join(part for part in (title, snippet, source_name) if part)
        player_mentions = _mentioned_entities(combined_text, player_aliases, minimum_length=4)
        team_mentions = _mentioned_entities(combined_text, team_aliases, minimum_length=3)
        category = _classify_google_item(source_name, source_url, title, query["category_hint"])
        normalized_combined = combined_text.lower()
        has_fpl_signal = _has_keyword(normalized_combined, FPL_KEYWORDS)
        has_actionability = _has_keyword(normalized_combined, ACTIONABILITY_KEYWORDS)
        if _has_keyword(normalized_combined, NON_FOOTBALL_FPL_KEYWORDS):
            continue
        if query["source_key"] == "google_news_fpl" and not has_fpl_signal:
            continue
        if query["source_key"] == "google_news_team_news" and not (
            (player_mentions or team_mentions) and has_actionability
        ):
            continue
        if query["source_key"] == "google_news_official_clubs" and category != "official_club":
            continue
        rows.append(
            {
                "season": window.season,
                "week": window.week,
                "window_start": window.window_start,
                "deadline_ts": window.deadline_ts,
                "title": title,
                "url": link,
                "source_url": source_url,
                "source_name": source_name,
                "category": category,
                "published_at": published_ts.isoformat(),
                "snippet": snippet,
                "content": snippet,
                "player_name": player_mentions[0] if player_mentions else "",
                "team_name": team_mentions[0] if team_mentions else "",
                "player_mentions": player_mentions,
                "team_mentions": team_mentions,
                "relevance_reason": "google_news_backfill",
                "source_key": query["source_key"],
                "timestamp_quality": "published_at",
            }
        )
        if len(rows) >= max_items:
            break
    return rows


def _fetch_sky_podcast_feed_rows(
    session: requests.Session,
    windows: Sequence[WeekEvidenceWindow],
    player_aliases: Mapping[str, str],
    team_aliases: Mapping[str, str],
) -> List[Dict[str, object]]:
    if not windows:
        return []
    first_start = _parse_timestamp(windows[0].window_start)
    last_deadline = _parse_timestamp(windows[-1].deadline_ts)
    if first_start is None or last_deadline is None:
        return []
    rows: List[Dict[str, object]] = []
    for source_name, feed_url in SKY_PODCAST_FEEDS.items():
        response = session.get(feed_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
        response.raise_for_status()
        root = ElementTree.fromstring(response.text)
        for item in root.findall(".//item"):
            published_ts = _parse_timestamp(_rss_text(item, "pubDate"))
            if published_ts is None or published_ts < first_start or published_ts > last_deadline:
                continue
            title = _rss_text(item, "title")
            link = _rss_text(item, "link") or feed_url
            raw_episode_text = _rss_text_any(
                item,
                (
                    "{http://purl.org/rss/1.0/modules/content/}encoded",
                    "description",
                ),
            )
            snippet = _clean_sky_podcast_episode_text(raw_episode_text)
            if not snippet:
                continue
            combined_text = " ".join(part for part in (title, snippet, source_name) if part)
            player_mentions = _mentioned_entities(combined_text, player_aliases, minimum_length=4)
            team_mentions = _mentioned_entities(combined_text, team_aliases, minimum_length=3)
            matched_windows = [
                window
                for window in windows
                if (_parse_timestamp(window.window_start) or first_start)
                <= published_ts
                <= (_parse_timestamp(window.deadline_ts) or last_deadline)
            ]
            if not matched_windows:
                continue
            # Store against the first eligible GW; deadline selection later remains timestamp-based.
            window = matched_windows[0]
            rows.append(
                {
                    "season": window.season,
                    "week": window.week,
                    "window_start": window.window_start,
                    "deadline_ts": window.deadline_ts,
                    "title": title,
                    "url": link,
                    "source_url": feed_url,
                    "source_name": source_name,
                    "category": "trusted_news",
                    "published_at": published_ts.isoformat(),
                    "snippet": snippet,
                    "content": snippet,
                    "full_text": snippet,
                    "full_text_chars": len(snippet),
                    "player_name": player_mentions[0] if player_mentions else "",
                    "team_name": team_mentions[0] if team_mentions else "",
                    "player_mentions": player_mentions,
                    "team_mentions": team_mentions,
                    "relevance_reason": "sky_podcast_feed",
                    "source_key": "sky_sports_podcast_feed",
                    "timestamp_quality": "published_at",
                    "extraction_status": "rss_episode_summary",
                }
            )
    return rows


def _alias_maps_from_dataset(dataset: CanonicalDataset, season: str) -> tuple[Dict[str, str], Dict[str, str]]:
    season_frame = dataset.training_frame.loc[dataset.training_frame["season"].astype(str) == season]
    player_aliases: Dict[str, str] = {}
    for name in sorted(season_frame["player_name"].dropna().astype(str).unique()):
        clean = _normalize_text(name).replace("_", " ")
        parts_with_possible_id = clean.split()
        if parts_with_possible_id and parts_with_possible_id[-1].isdigit():
            clean = " ".join(parts_with_possible_id[:-1])
        if len(clean) >= 4:
            player_aliases[clean.lower()] = clean
        parts = clean.split()
        if parts and len(parts[-1]) >= 4:
            player_aliases[parts[-1].lower()] = clean
    team_aliases: Dict[str, str] = {}
    team_columns = [column for column in ("team_name", "team", "opponent_team_name") if column in season_frame.columns]
    for column in team_columns:
        for name in sorted(season_frame[column].dropna().astype(str).unique()):
            clean = _normalize_text(name)
            if len(clean) >= 3 and not clean.isdigit():
                team_aliases[clean.lower()] = clean
    for team_name in OFFICIAL_CLUB_SOURCES:
        team_aliases[team_name.lower()] = team_name
    return player_aliases, team_aliases


def backfill_weekly_google_news_evidence(
    dataset: CanonicalDataset,
    season: str,
    start_week: int,
    end_week: int,
    documents_output: str,
    packets_output: str,
    report_output: str,
    lookback_days: int = 14,
    max_items_per_query: int = 40,
    max_documents_per_week: int = 80,
    sleep_seconds: float = 0.25,
    session: Optional[requests.Session] = None,
) -> WeeklyEvidenceBackfillReport:
    session = session or requests.Session()
    player_aliases, team_aliases = _alias_maps_from_dataset(dataset, season)
    windows = _week_deadline_windows(dataset, season, start_week, end_week, default_lookback_days=lookback_days)
    rows: List[Dict[str, object]] = []
    notes: List[str] = []
    for window in windows:
        window_start = _parse_timestamp(window.window_start)
        deadline = _parse_timestamp(window.deadline_ts)
        if window_start is None or deadline is None:
            continue
        for query in _google_week_queries(window.week, window_start, deadline):
            try:
                rows.extend(
                    _fetch_google_news_query(
                        session=session,
                        query=query,
                        window=window,
                        max_items=max_items_per_query,
                        player_aliases=player_aliases,
                        team_aliases=team_aliases,
                    )
                )
            except Exception as exc:  # Network backfills should keep partial results.
                notes.append(f"GW{window.week} query {query['source_key']} failed: {type(exc).__name__}: {exc}")
            if sleep_seconds > 0:
                time.sleep(sleep_seconds)

    try:
        rows.extend(
            _fetch_sky_podcast_feed_rows(
                session=session,
                windows=windows,
                player_aliases=player_aliases,
                team_aliases=team_aliases,
            )
        )
    except Exception as exc:
        notes.append(f"Sky podcast feed fetch failed: {type(exc).__name__}: {exc}")

    frame = normalize_evidence_records(rows, curated_only=False)
    write_normalized_evidence(frame, documents_output)

    packets: List[Dict[str, object]] = []
    for window in windows:
        documents = select_evidence_for_deadline(
            frame,
            deadline_ts=window.deadline_ts,
            max_documents=max_documents_per_week,
            lookback_days=lookback_days,
        )
        packets.append(
            {
                "season": window.season,
                "week": window.week,
                "window_start": window.window_start,
                "deadline_ts": window.deadline_ts,
                "document_count": len(documents),
                "documents": [asdict(document) for document in documents],
            }
        )

    packets_path = Path(packets_output)
    packets_path.parent.mkdir(parents=True, exist_ok=True)
    packets_path.write_text("\n".join(json.dumps(packet, ensure_ascii=True) for packet in packets) + ("\n" if packets else ""))

    report = WeeklyEvidenceBackfillReport(
        season=season,
        start_week=start_week,
        end_week=end_week,
        document_rows=int(len(frame)),
        packet_rows=len(packets),
        source_counts={str(key): int(value) for key, value in frame["source_name"].value_counts().to_dict().items()} if not frame.empty else {},
        category_counts={str(key): int(value) for key, value in frame["category"].value_counts().to_dict().items()} if not frame.empty else {},
        documents_output=documents_output,
        packets_output=packets_output,
        notes=notes,
    )
    report_path = Path(report_output)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(asdict(report), indent=2))
    return report

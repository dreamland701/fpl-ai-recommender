"""Evidence collection helpers for curated feeds plus local imports."""

from __future__ import annotations

import json
import os
import re
from html import unescape
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple
from urllib.parse import urljoin
from xml.etree import ElementTree

import pandas as pd
import requests

from .api import OfficialFPLClient
from .llm_data import normalize_evidence_corpus, normalize_evidence_records, write_normalized_evidence


FPL_KEYWORDS = (
    "fpl",
    "fantasy premier league",
    "gameweek",
    "bench boost",
    "triple captain",
    "wildcard",
    "free hit",
)

ACTIONABILITY_KEYWORDS = (
    "injury",
    "injured",
    "fitness",
    "fit",
    "training",
    "trained",
    "returns",
    "return",
    "available",
    "availability",
    "doubt",
    "doubtful",
    "knock",
    "suspended",
    "suspension",
    "lineup",
    "line-up",
    "starts",
    "starting",
    "bench",
    "rested",
    "minutes",
)

LOW_SIGNAL_KEYWORDS = (
    "accounts",
    "appeal",
    "director",
    "europa league",
    "finance",
    "financial",
    "flops of the season",
    "la liga",
    "league one",
    "owner",
    "ownership",
    "players of the season",
    "photos",
    "points deduction",
    "promotion",
    "profit",
    "review:",
    "relegated",
    "relegation",
    "sanction",
    "season by season",
    "takeover",
    "talking points",
    "world cup",
)


@dataclass(frozen=True)
class EvidenceSourceSpec:
    key: str
    name: str
    category: str
    kind: str
    url: str


DEFAULT_FETCHABLE_EVIDENCE_SOURCES: Sequence[EvidenceSourceSpec] = (
    EvidenceSourceSpec(
        key="official_fpl_status",
        name="Fantasy Premier League",
        category="official_fpl",
        kind="fpl_bootstrap_status",
        url="https://fantasy.premierleague.com/api/bootstrap-static/",
    ),
    EvidenceSourceSpec(
        key="premierleague_news",
        name="Premier League",
        category="official_premier_league",
        kind="premierleague_news_index",
        url="https://www.premierleague.com/news",
    ),
    EvidenceSourceSpec(
        key="wolves_official_rss",
        name="Wolves Official Site",
        category="official_club",
        kind="rss",
        url="https://www.wolves.co.uk/news/rss/",
    ),
    EvidenceSourceSpec(
        key="bbc_football_rss",
        name="BBC Sport Football",
        category="trusted_news",
        kind="rss",
        url="https://feeds.bbci.co.uk/sport/football/rss.xml",
    ),
    EvidenceSourceSpec(
        key="guardian_football_rss",
        name="The Guardian Football",
        category="trusted_news",
        kind="rss",
        url="https://www.theguardian.com/football/rss",
    ),
    EvidenceSourceSpec(
        key="sky_sports_football_rss",
        name="Sky Sports Football",
        category="trusted_news",
        kind="rss",
        url="https://www.skysports.com/rss/12040",
    ),
    EvidenceSourceSpec(
        key="reddit_fantasypl",
        name="r/FantasyPL",
        category="reddit",
        kind="reddit_oauth",
        url="https://oauth.reddit.com/r/FantasyPL/new",
    ),
)


def available_fetchable_source_keys() -> List[str]:
    return [source.key for source in DEFAULT_FETCHABLE_EVIDENCE_SOURCES]


def _parse_timestamp(value: object) -> Optional[datetime]:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    normalized = text.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        from email.utils import parsedate_to_datetime

        try:
            parsed = parsedate_to_datetime(text)
        except (TypeError, ValueError, IndexError):
            parsed = None
    if parsed is None:
        for fmt in ("%d %B %Y", "%d %b %Y"):
            try:
                parsed = datetime.strptime(text, fmt).replace(tzinfo=timezone.utc)
                break
            except ValueError:
                continue
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _normalize_text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _response_json(response) -> Dict[str, object]:
    if hasattr(response, "json"):
        return response.json()
    return json.loads(response.text)


def _strip_html(value: str) -> str:
    cleaned = re.sub(r"<[^>]+>", " ", unescape(value or ""))
    return " ".join(cleaned.split())


def _bootstrap_name_maps(client: OfficialFPLClient) -> Tuple[Dict[str, str], Dict[str, str]]:
    payload = client.bootstrap_static()
    player_aliases: Dict[str, str] = {}
    for element in payload.get("elements", []):
        first = _normalize_text(element.get("first_name"))
        second = _normalize_text(element.get("second_name"))
        web_name = _normalize_text(element.get("web_name"))
        full_name = " ".join(part for part in (first, second) if part)
        canonical = full_name or web_name
        aliases = {full_name, second}
        if web_name and web_name.lower() != first.lower():
            aliases.add(web_name)
        for alias in aliases:
            alias = alias.strip()
            if len(alias) >= 4 and len(alias.split()) <= 4:
                player_aliases[alias.lower()] = canonical

    team_aliases: Dict[str, str] = {}
    for team in payload.get("teams", []):
        canonical = _normalize_text(team.get("name"))
        short = _normalize_text(team.get("short_name"))
        for alias in {canonical, short}:
            alias = alias.strip()
            if len(alias) >= 3:
                team_aliases[alias.lower()] = canonical
    return player_aliases, team_aliases


def _mentioned_entities(
    text: str,
    aliases: Mapping[str, str],
    minimum_length: int,
) -> List[str]:
    normalized_text = f" {text.lower()} "
    matches = set()
    for alias, canonical in aliases.items():
        if len(alias) < minimum_length:
            continue
        pattern = rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])"
        if re.search(pattern, normalized_text):
            matches.add(canonical)
    return sorted(matches)


def _is_relevant(text: str, player_mentions: Sequence[str], team_mentions: Sequence[str]) -> bool:
    normalized = text.lower()
    has_fpl_signal = _has_keyword(normalized, FPL_KEYWORDS)
    has_actionability = _has_keyword(normalized, ACTIONABILITY_KEYWORDS)
    has_low_signal = _has_keyword(normalized, LOW_SIGNAL_KEYWORDS)

    if has_low_signal and not has_fpl_signal:
        return False
    if has_fpl_signal:
        return True
    if player_mentions and has_actionability:
        return True
    if team_mentions and has_actionability:
        return True
    return False


def _relevance_reason(text: str, player_mentions: Sequence[str], team_mentions: Sequence[str]) -> str:
    normalized = text.lower()
    if _has_keyword(normalized, FPL_KEYWORDS):
        return "fpl_keyword"
    if player_mentions and _has_keyword(normalized, ACTIONABILITY_KEYWORDS):
        return "player_actionability"
    if team_mentions and _has_keyword(normalized, ACTIONABILITY_KEYWORDS):
        return "team_actionability"
    return "unknown"


def _has_keyword(normalized_text: str, keywords: Sequence[str]) -> bool:
    for keyword in keywords:
        escaped = re.escape(keyword.lower())
        if re.search(r"[^a-z0-9]", keyword.lower()):
            pattern = rf"(?<![a-z0-9]){escaped}(?![a-z0-9])"
        else:
            pattern = rf"\b{escaped}\b"
        if re.search(pattern, normalized_text):
            return True
    return False


def _rss_item_text(item: ElementTree.Element, tags: Sequence[str]) -> str:
    for tag in tags:
        found = item.find(tag)
        if found is not None and found.text:
            return found.text
    return ""


def _rss_items(root: ElementTree.Element) -> List[ElementTree.Element]:
    items = root.findall(".//item")
    if items:
        return items
    namespace = "{http://www.w3.org/2005/Atom}"
    return root.findall(f".//{namespace}entry")


def _fetch_rss_source(
    source: EvidenceSourceSpec,
    session: requests.Session,
    now: datetime,
    lookback_days: int,
    max_items_per_source: int,
    player_aliases: Mapping[str, str],
    team_aliases: Mapping[str, str],
) -> List[Dict[str, object]]:
    response = session.get(source.url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    root = ElementTree.fromstring(response.text)
    rows: List[Dict[str, object]] = []
    earliest = now - timedelta(days=lookback_days)
    for item in _rss_items(root):
        title = _normalize_text(_rss_item_text(item, ("title", "{http://www.w3.org/2005/Atom}title")))
        link = _normalize_text(_rss_item_text(item, ("link", "{http://www.w3.org/2005/Atom}link")))
        if not link:
            atom_link = item.find("{http://www.w3.org/2005/Atom}link")
            if atom_link is not None:
                link = _normalize_text(atom_link.attrib.get("href"))
        published_at = _normalize_text(
            _rss_item_text(
                item,
                (
                    "pubDate",
                    "published",
                    "updated",
                    "{http://www.w3.org/2005/Atom}published",
                    "{http://www.w3.org/2005/Atom}updated",
                ),
            )
        )
        snippet = _strip_html(
            _rss_item_text(
                item,
                (
                    "description",
                    "summary",
                    "{http://www.w3.org/2005/Atom}summary",
                ),
            )
        )
        published_ts = _parse_timestamp(published_at)
        if published_ts is None or published_ts < earliest or published_ts > now:
            continue
        combined_text = " ".join(part for part in (title, snippet) if part)
        player_mentions = _mentioned_entities(combined_text, player_aliases, minimum_length=4)
        team_mentions = _mentioned_entities(combined_text, team_aliases, minimum_length=3)
        if not _is_relevant(combined_text, player_mentions, team_mentions):
            continue
        rows.append(
            {
                "title": title,
                "url": link,
                "source_name": source.name,
                "category": source.category,
                "published_at": published_ts.isoformat(),
                "snippet": snippet,
                "content": snippet,
                "player_name": player_mentions[0] if player_mentions else "",
                "team_name": team_mentions[0] if team_mentions else "",
                "player_mentions": player_mentions,
                "team_mentions": team_mentions,
                "relevance_reason": _relevance_reason(combined_text, player_mentions, team_mentions),
                "source_key": source.key,
                "timestamp_quality": "published_at",
            }
        )
        if len(rows) >= max_items_per_source:
            break
    return rows


def _fetch_fpl_bootstrap_status_source(
    source: EvidenceSourceSpec,
    client: OfficialFPLClient,
    now: datetime,
    max_items_per_source: int,
) -> List[Dict[str, object]]:
    payload = client.bootstrap_static()
    teams_by_id = {int(team["id"]): _normalize_text(team.get("name")) for team in payload.get("teams", []) if team.get("id")}
    rows: List[Dict[str, object]] = []
    for element in payload.get("elements", []):
        news = _normalize_text(element.get("news"))
        status = _normalize_text(element.get("status"))
        chance_next = element.get("chance_of_playing_next_round")
        chance_this = element.get("chance_of_playing_this_round")
        if not news and status in {"", "a"} and chance_next in {None, 100} and chance_this in {None, 100}:
            continue
        first = _normalize_text(element.get("first_name"))
        second = _normalize_text(element.get("second_name"))
        web_name = _normalize_text(element.get("web_name"))
        player_name = " ".join(part for part in (first, second) if part) or web_name
        team_name = teams_by_id.get(int(element.get("team") or 0), "")
        snippet = (
            f"Official FPL status={status or 'unknown'}; "
            f"chance_this_round={chance_this}; chance_next_round={chance_next}; news={news or 'none'}."
        )
        rows.append(
            {
                "title": f"Official FPL status: {player_name}",
                "url": source.url,
                "source_name": source.name,
                "category": source.category,
                "published_at": now.isoformat(),
                "snippet": snippet,
                "content": snippet,
                "player_name": player_name,
                "team_name": team_name,
                "player_mentions": [player_name] if player_name else [],
                "team_mentions": [team_name] if team_name else [],
                "relevance_reason": "official_fpl_status",
                "source_key": source.key,
                "timestamp_quality": "collected_at_snapshot",
            }
        )
        if len(rows) >= max_items_per_source:
            break
    return rows


def _extract_meta_content(html: str, names: Sequence[str]) -> str:
    for name in names:
        pattern = rf'<meta[^>]+(?:property|name)=["\']{re.escape(name)}["\'][^>]+content=["\']([^"\']+)["\']'
        match = re.search(pattern, html, flags=re.IGNORECASE)
        if match:
            return _strip_html(unescape(match.group(1)))
        pattern = rf'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\']{re.escape(name)}["\']'
        match = re.search(pattern, html, flags=re.IGNORECASE)
        if match:
            return _strip_html(unescape(match.group(1)))
    return ""


def _extract_article_published_at(html: str) -> str:
    patterns = (
        r'"datePublished"\s*:\s*"([^"]+)"',
        r'"article:published_time"\s*:\s*"([^"]+)"',
        r'<time[^>]+datetime=["\']([^"\']+)["\']',
    )
    for pattern in patterns:
        match = re.search(pattern, html, flags=re.IGNORECASE)
        if match:
            return _normalize_text(unescape(match.group(1)))
    return _extract_meta_content(html, ("article:published_time", "datePublished"))


def _extract_premierleague_article_links(index_html: str) -> List[str]:
    links = set()
    for match in re.finditer(r'href=["\']([^"\']*/news/\d+/[^"\']+)["\']', index_html, flags=re.IGNORECASE):
        links.add(urljoin("https://www.premierleague.com", unescape(match.group(1))))
    for match in re.finditer(r'https://www\.premierleague\.com/(?:en/)?news/\d+/[A-Za-z0-9/_-]+', index_html):
        links.add(match.group(0))
    return sorted(links)


def _fetch_premierleague_news_source(
    source: EvidenceSourceSpec,
    session: requests.Session,
    now: datetime,
    lookback_days: int,
    max_items_per_source: int,
    player_aliases: Mapping[str, str],
    team_aliases: Mapping[str, str],
) -> List[Dict[str, object]]:
    response = session.get(source.url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    rows: List[Dict[str, object]] = []
    earliest = now - timedelta(days=lookback_days)
    for link in _extract_premierleague_article_links(response.text):
        article = session.get(link, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        article.raise_for_status()
        html = article.text
        title = _extract_meta_content(html, ("og:title", "twitter:title"))
        if not title:
            match = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
            title = _strip_html(match.group(1)) if match else ""
        snippet = _extract_meta_content(html, ("og:description", "description", "twitter:description"))
        published_ts = _parse_timestamp(_extract_article_published_at(html))
        if published_ts is None or published_ts < earliest or published_ts > now:
            continue
        combined_text = " ".join(part for part in (title, snippet) if part)
        player_mentions = _mentioned_entities(combined_text, player_aliases, minimum_length=4)
        team_mentions = _mentioned_entities(combined_text, team_aliases, minimum_length=3)
        if not _is_relevant(combined_text, player_mentions, team_mentions):
            continue
        category = "official_scout" if _has_keyword(combined_text.lower(), FPL_KEYWORDS) else source.category
        rows.append(
            {
                "title": title,
                "url": link,
                "source_name": "The Scout" if category == "official_scout" else source.name,
                "category": category,
                "published_at": published_ts.isoformat(),
                "snippet": snippet,
                "content": snippet,
                "player_name": player_mentions[0] if player_mentions else "",
                "team_name": team_mentions[0] if team_mentions else "",
                "player_mentions": player_mentions,
                "team_mentions": team_mentions,
                "relevance_reason": _relevance_reason(combined_text, player_mentions, team_mentions),
                "source_key": source.key,
                "timestamp_quality": "published_at",
            }
        )
        if len(rows) >= max_items_per_source:
            break
    return rows


def _fetch_reddit_source(
    source: EvidenceSourceSpec,
    session: requests.Session,
    now: datetime,
    lookback_days: int,
    max_items_per_source: int,
    player_aliases: Mapping[str, str],
    team_aliases: Mapping[str, str],
) -> List[Dict[str, object]]:
    client_id = os.environ.get("REDDIT_CLIENT_ID")
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
    user_agent = os.environ.get("REDDIT_USER_AGENT", "fpl-ai-recommender/0.1 by local-user")
    if not client_id or not client_secret:
        return []

    token_response = session.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=(client_id, client_secret),
        data={"grant_type": "client_credentials"},
        headers={"User-Agent": user_agent},
        timeout=20,
    )
    token_response.raise_for_status()
    token = _response_json(token_response).get("access_token")
    if not token:
        return []

    response = session.get(
        source.url,
        params={"limit": min(max_items_per_source * 3, 100), "raw_json": 1},
        headers={"Authorization": f"bearer {token}", "User-Agent": user_agent},
        timeout=20,
    )
    response.raise_for_status()
    payload = _response_json(response)
    earliest = now - timedelta(days=lookback_days)
    rows: List[Dict[str, object]] = []
    for child in payload.get("data", {}).get("children", []):
        data = child.get("data", {})
        created_utc = data.get("created_utc")
        if created_utc is None:
            continue
        published_ts = datetime.fromtimestamp(float(created_utc), tz=timezone.utc)
        if published_ts < earliest or published_ts > now:
            continue
        title = _normalize_text(data.get("title"))
        body = _strip_html(_normalize_text(data.get("selftext")))
        permalink = _normalize_text(data.get("permalink"))
        link = urljoin("https://www.reddit.com", permalink) if permalink else source.url
        combined_text = " ".join(part for part in (title, body[:1000]) if part)
        player_mentions = _mentioned_entities(combined_text, player_aliases, minimum_length=4)
        team_mentions = _mentioned_entities(combined_text, team_aliases, minimum_length=3)
        if not _is_relevant(combined_text, player_mentions, team_mentions):
            continue
        rows.append(
            {
                "title": title,
                "url": link,
                "source_name": source.name,
                "category": source.category,
                "published_at": published_ts.isoformat(),
                "snippet": body[:500],
                "content": body,
                "player_name": player_mentions[0] if player_mentions else "",
                "team_name": team_mentions[0] if team_mentions else "",
                "player_mentions": player_mentions,
                "team_mentions": team_mentions,
                "relevance_reason": _relevance_reason(combined_text, player_mentions, team_mentions),
                "source_key": source.key,
                "timestamp_quality": "published_at",
                "reddit_score": data.get("score"),
                "reddit_num_comments": data.get("num_comments"),
            }
        )
        if len(rows) >= max_items_per_source:
            break
    return rows


def _local_records(paths: Sequence[str]) -> List[Dict[str, object]]:
    records: List[Dict[str, object]] = []
    for path in paths:
        normalized = normalize_evidence_corpus(path, curated_only=False)
        records.extend(normalized.drop(columns=["published_ts"], errors="ignore").to_dict(orient="records"))
    return records


def collect_evidence_records(
    local_inputs: Sequence[str] = (),
    source_keys: Optional[Sequence[str]] = None,
    lookback_days: int = 7,
    max_items_per_source: int = 50,
    session: Optional[requests.Session] = None,
    client: Optional[OfficialFPLClient] = None,
    now: Optional[datetime] = None,
) -> List[Dict[str, object]]:
    client = client or OfficialFPLClient()
    session = session or requests.Session()
    now = now or datetime.now(timezone.utc)
    player_aliases, team_aliases = _bootstrap_name_maps(client)
    selected_sources = [
        source
        for source in DEFAULT_FETCHABLE_EVIDENCE_SOURCES
        if source_keys is None or source.key in set(source_keys)
    ]
    rows: List[Dict[str, object]] = []
    for source in selected_sources:
        if source.kind == "rss":
            rows.extend(
                _fetch_rss_source(
                    source=source,
                    session=session,
                    now=now,
                    lookback_days=lookback_days,
                    max_items_per_source=max_items_per_source,
                    player_aliases=player_aliases,
                    team_aliases=team_aliases,
                )
            )
        elif source.kind == "fpl_bootstrap_status":
            rows.extend(
                _fetch_fpl_bootstrap_status_source(
                    source=source,
                    client=client,
                    now=now,
                    max_items_per_source=max_items_per_source,
                )
            )
        elif source.kind == "premierleague_news_index":
            rows.extend(
                _fetch_premierleague_news_source(
                    source=source,
                    session=session,
                    now=now,
                    lookback_days=lookback_days,
                    max_items_per_source=max_items_per_source,
                    player_aliases=player_aliases,
                    team_aliases=team_aliases,
                )
            )
        elif source.kind == "reddit_oauth":
            rows.extend(
                _fetch_reddit_source(
                    source=source,
                    session=session,
                    now=now,
                    lookback_days=lookback_days,
                    max_items_per_source=max_items_per_source,
                    player_aliases=player_aliases,
                    team_aliases=team_aliases,
                )
            )
    rows.extend(_local_records(local_inputs))
    deduped: Dict[Tuple[str, str, str], Dict[str, object]] = {}
    for row in rows:
        key = (_normalize_text(row.get("url")), _normalize_text(row.get("published_at")), _normalize_text(row.get("title")))
        deduped[key] = row
    return sorted(
        deduped.values(),
        key=lambda row: _parse_timestamp(row.get("published_at")) or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )


def collect_and_write_evidence(
    output_path: str,
    local_inputs: Sequence[str] = (),
    source_keys: Optional[Sequence[str]] = None,
    curated_only: bool = True,
    lookback_days: int = 7,
    max_items_per_source: int = 50,
    session: Optional[requests.Session] = None,
    client: Optional[OfficialFPLClient] = None,
    now: Optional[datetime] = None,
) -> pd.DataFrame:
    records = collect_evidence_records(
        local_inputs=local_inputs,
        source_keys=source_keys,
        lookback_days=lookback_days,
        max_items_per_source=max_items_per_source,
        session=session,
        client=client,
        now=now,
    )
    frame = normalize_evidence_records(records, curated_only=curated_only)
    write_normalized_evidence(frame, output_path)
    return frame

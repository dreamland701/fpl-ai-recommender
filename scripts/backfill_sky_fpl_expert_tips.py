#!/usr/bin/env python3
"""Backfill Sky Sports' weekly "FPL Gameweek N tips and advice from experts".

Wes flagged this series (2026-07-11): before each GW, Sky's FPL experts
publish concrete squad/transfer/captain recommendations — an
expert-*decision* corpus aligned with our training seasons, distinct from
news facts.

Enumeration: the Wayback Machine CDX index lists every archived
skysports.com/football/news URL matching the series pattern (Google News RSS
has no retention for old articles). Articles are then fetched LIVE from
skysports.com (they remain published), with title/datePublished/full text
extracted from the page. Timestamp safety: published_at is stored and the
standard evidence selection enforces published_at <= deadline.

Resumable: existing article IDs in the output are skipped.

Usage:
  python3 scripts/backfill_sky_fpl_expert_tips.py \
    --output reports/evidence_sky_fpl_expert_tips_2022_26.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fpl_ai.weekly_evidence import (  # noqa: E402
    _extract_generic_article_text,
    _extract_json_article_text,
)

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
CDX_URL = "http://web.archive.org/cdx/search/cdx"
CDX_FILTERS = [
    "original:.*gameweek.*tips.*",
    "original:.*fpl.*gameweek.*",
    "original:.*fantasy-premier-league.*advice.*",
]
ARTICLE_ID_PATTERN = re.compile(r"/news/(\d+)/(\d+)/")
WEEK_PATTERN = re.compile(r"gameweek[-\s]+(\d+)", re.IGNORECASE)


# Sky news sections observed hosting the FPL expert-tips series.
CDX_SECTIONS = ("11095", "11096", "12040", "11661")
CDX_WINDOWS = [
    ("20220701", "20221231"), ("20230101", "20230630"), ("20230701", "20231231"),
    ("20240101", "20240630"), ("20240701", "20241231"), ("20250101", "20250630"),
    ("20250701", "20251231"), ("20260101", "20261231"),
]
SLUG_TOPIC = re.compile(r"fantasy|fpl", re.IGNORECASE)
SLUG_SERIES = re.compile(r"gameweek|tips|advice|scout", re.IGNORECASE)


def enumerate_articles(session: requests.Session) -> dict[str, str]:
    """article_id -> canonical live URL.

    Server-side regex filters 504 constantly, so this uses cheap prefix
    queries per (section, half-year window) and filters slugs client-side.
    """
    urls: dict[str, str] = {}
    for section in CDX_SECTIONS:
        for window_from, window_to in CDX_WINDOWS:
            response = None
            for attempt in range(4):
                try:
                    response = session.get(
                        CDX_URL,
                        params={
                            "url": f"skysports.com/football/news/{section}",
                            "matchType": "prefix",
                            "collapse": "urlkey",
                            "fl": "original",
                            "from": window_from,
                            "to": window_to,
                            "limit": "30000",
                        },
                        timeout=180,
                    )
                except requests.RequestException as error:
                    print(f"CDX {section} {window_from}: {error}", flush=True)
                    response = None
                if response is not None and response.status_code == 200:
                    break
                time.sleep(10.0 * (attempt + 1))
            if response is None or response.status_code != 200:
                print(f"CDX {section} {window_from}: GIVING UP", flush=True)
                continue
            lines = response.text.splitlines()
            added = 0
            for line in lines:
                url = line.strip().split("?")[0]
                slug = url.rsplit("/", 1)[-1]
                if not (SLUG_TOPIC.search(slug) and SLUG_SERIES.search(slug)):
                    continue
                match = ARTICLE_ID_PATTERN.search(url)
                if not match:
                    continue
                article_id = match.group(2)
                canonical = "https://www.skysports.com" + url.split("skysports.com", 1)[1]
                if article_id not in urls:
                    added += 1
                    urls[article_id] = canonical
                elif len(canonical) > len(urls[article_id]):
                    urls[article_id] = canonical
            print(
                f"CDX {section} {window_from}: {len(lines)} urls, +{added} series matches ({len(urls)} total)",
                flush=True,
            )
            time.sleep(3.0)
    return urls


def season_for(published: datetime) -> str:
    year = published.year if published.month >= 7 else published.year - 1
    return f"{year}-{str(year + 1)[2:]}"


def fetch_article(session: requests.Session, url: str) -> dict | None:
    response = session.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    if response.status_code != 200:
        return None
    html = response.text
    text = _extract_json_article_text(html) or _extract_generic_article_text(html)
    date_match = re.search(r'"datePublished"\s*:\s*"([^"]+)"', html)
    title_match = re.search(r"<title>(.*?)</title>", html, re.S)
    headline_match = re.search(r'"headline"\s*:\s*"([^"]+)"', html)
    title = (headline_match.group(1) if headline_match else (title_match.group(1) if title_match else "")).strip()
    if not date_match or not text:
        return None
    raw = date_match.group(1).replace("Z", "+00:00")
    try:
        published = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if published.tzinfo is None:
        published = published.replace(tzinfo=timezone.utc)
    week_match = WEEK_PATTERN.search(url) or WEEK_PATTERN.search(title)
    return {
        "season": season_for(published),
        "week": int(week_match.group(1)) if week_match else None,
        "title": title.split(" | ")[0],
        "url": url,
        "source_name": "Sky Sports",
        "category": "expert_tips",
        "published_at": published.isoformat(),
        "content": text,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--sleep", type=float, default=1.5)
    args = parser.parse_args()

    session = requests.Session()
    urls = enumerate_articles(session)
    print(f"CDX enumeration: {len(urls)} unique articles", flush=True)

    done: set[str] = set()
    if args.output.exists():
        with args.output.open() as handle:
            for line in handle:
                match = ARTICLE_ID_PATTERN.search(json.loads(line).get("url", ""))
                if match:
                    done.add(match.group(2))

    found = failed = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a") as out:
        for article_id, url in sorted(urls.items()):
            if article_id in done:
                continue
            try:
                row = fetch_article(session, url)
            except Exception as error:
                row = None
                print(f"{url[:90]}: ERROR {error}", flush=True)
            if row is None:
                failed += 1
            else:
                out.write(json.dumps(row, ensure_ascii=False) + "\n")
                out.flush()
                found += 1
                print(f"{row['season']} GW{row['week']}: {row['title'][:70]} ({len(row['content'])} chars)", flush=True)
            time.sleep(args.sleep)
    print(f"done: {found} fetched, {failed} failed -> {args.output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Backfill the official FPL Scout's articles from the Premier League API.

Wes ranked the official Scout (premierleague.com "Scout Selection", transfer
radar, captaincy picks, ones to watch) as the most useful expert source
(2026-07-11). The PL site is an SPA over the public Pulselive content API,
which supports tag pagination back past 2021 — full coverage of the training
window.

Per article: title, publish date, clean body text (live-page extraction as
fallback for thin bodies), canonical URL. Category `official_scout` matches
the existing evidence pipeline. Timestamp safety comes from the stored
publish date + the standard pre-deadline selection.

Resumable by article id.

Usage:
  python3 scripts/backfill_pl_scout_articles.py \
    --output reports/evidence_pl_scout_2021_26.jsonl \
    --since 2022-06-01
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

API_URL = "https://footballapi.pulselive.com/content/PremierLeague/text/EN"
HEADERS = {
    "Origin": "https://www.premierleague.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36",
}
TAG = "content-creator:The-Scout"
MIN_BODY_CHARS = 400


def clean_html(html: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", html or "", flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return " ".join(text.split())


def live_page_text(session: requests.Session, article_id: int, slug: str) -> str:
    from fpl_ai.weekly_evidence import _extract_generic_article_text, _extract_json_article_text

    url = f"https://www.premierleague.com/en/news/{article_id}/{slug}"
    try:
        response = session.get(url, headers={"User-Agent": HEADERS["User-Agent"]}, timeout=30)
        if response.status_code != 200:
            return ""
        return _extract_json_article_text(response.text) or _extract_generic_article_text(response.text)
    except requests.RequestException:
        return ""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--since", default="2022-06-01", help="Stop paginating once articles are older than this.")
    parser.add_argument("--sleep", type=float, default=1.0)
    args = parser.parse_args()

    done: set[int] = set()
    if args.output.exists():
        with args.output.open() as handle:
            for line in handle:
                done.add(int(json.loads(line)["article_id"]))

    session = requests.Session()
    found = thin = 0
    page = 0
    stale_pages = 0  # tag pages are not strictly chronological; stop only
    # after several consecutive pages contribute nothing in-window.
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a") as out:
        while page < 300 and stale_pages < 5:
            response = session.get(
                API_URL,
                params={"pageSize": 50, "page": page, "tagNames": TAG},
                headers=HEADERS,
                timeout=30,
            )
            response.raise_for_status()
            items = response.json().get("content", [])
            if not items:
                break
            oldest = min((item.get("date") or "9999" for item in items))
            in_window = sum(1 for item in items if str(item.get("date") or "")[:10] >= args.since)
            stale_pages = 0 if in_window else stale_pages + 1
            for item in items:
                article_id = int(item["id"])
                date = str(item.get("date") or "")
                if date[:10] < args.since:
                    continue
                if article_id in done:
                    continue
                title = str(item.get("title") or "").strip()
                slug = str(item.get("titleUrlSegment") or "")
                text = clean_html(item.get("body") or "")
                description = str(item.get("description") or "").strip()
                if len(text) < MIN_BODY_CHARS:
                    fallback = live_page_text(session, article_id, slug)
                    if len(fallback) > len(text):
                        text = fallback
                    else:
                        thin += 1
                    time.sleep(args.sleep)
                url = str(item.get("canonicalUrl") or f"https://www.premierleague.com/en/news/{article_id}/{slug}")
                out.write(
                    json.dumps(
                        {
                            "article_id": article_id,
                            "title": title,
                            "url": url,
                            "source_name": "Premier League",
                            "category": "official_scout",
                            "published_at": date,
                            "content": (text or description)[:20000],
                            "description": description,
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
                out.flush()
                found += 1
            print(f"page {page}: total {found} (oldest on page {oldest[:10]}, in-window {in_window})", flush=True)
            page += 1
            time.sleep(args.sleep)
    print(f"done: {found} articles, {thin} thin-body -> {args.output}")


if __name__ == "__main__":
    main()

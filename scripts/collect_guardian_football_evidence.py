#!/usr/bin/env python3
"""Backfill Guardian football articles as timestamped evidence rows.

Uses the Guardian Open Platform content API (free). Full bodyText and precise
webPublicationDate are available back well past 2021-22 — audited 2026-07-05:
~150 football-tagged articles/week in 2022.

API key: pass --api-key or set GUARDIAN_API_KEY. The shared "test" key works
for prototyping but is heavily throttled; register a free developer key at
https://open-platform.theguardian.com/access/ for real backfills.

Output rows use the existing evidence corpus schema (published_at,
source_name, full_text, extraction_status) so they merge directly with the
PL/Sky corpora.

Usage:
  python3 scripts/collect_guardian_football_evidence.py \
    --from-date 2022-07-01 --to-date 2023-06-30 \
    --output reports/evidence_guardian_football_2022_23.jsonl \
    [--api-key KEY] [--page-size 50] [--sleep 0.6]
"""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

API_URL = "https://content.guardianapis.com/search"

# FPL-relevant Guardian tags. football/football is the umbrella tag; the
# match-report and news tags overlap it, so we query the umbrella only and
# keep tag lists in the row for downstream filtering.
QUERY_TAG = "football/football"


def fetch_page(api_key: str, from_date: str, to_date: str, page: int, page_size: int) -> dict:
    params = {
        "tag": QUERY_TAG,
        "from-date": from_date,
        "to-date": to_date,
        "page": page,
        "page-size": page_size,
        "order-by": "oldest",
        "show-fields": "bodyText,headline,trailText,byline",
        "show-tags": "keyword",
        "api-key": api_key,
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "fpl-ai-research"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read())["response"]


def to_evidence_row(item: dict) -> dict:
    fields = item.get("fields") or {}
    body = fields.get("bodyText") or ""
    tags = [tag.get("id") for tag in item.get("tags") or [] if tag.get("id")]
    return {
        "title": fields.get("headline") or item.get("webTitle") or "",
        "url": item.get("webUrl") or "",
        "source_url": API_URL,
        "source_name": "The Guardian Football",
        "category": "trusted_news",
        "published_at": item.get("webPublicationDate") or "",
        "snippet": (fields.get("trailText") or "")[:500],
        "content": body,
        "full_text": body,
        "full_text_chars": len(body),
        "byline": fields.get("byline") or "",
        "tags": tags,
        "relevance_reason": "guardian_football_tag",
        "source_key": "guardian_open_platform",
        "timestamp_quality": "published_at",
        "extraction_status": "api_body_text",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--from-date", required=True)
    parser.add_argument("--to-date", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--api-key", default=os.environ.get("GUARDIAN_API_KEY", "test"))
    parser.add_argument("--page-size", type=int, default=50)
    parser.add_argument("--sleep", type=float, default=0.6, help="Seconds between requests; raise if throttled.")
    parser.add_argument("--max-pages", type=int, default=0, help="Stop after N pages (0 = all).")
    args = parser.parse_args()

    if args.api_key == "test":
        print("WARNING: using shared 'test' API key (heavily throttled). Set GUARDIAN_API_KEY for real backfills.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    seen_urls: set[str] = set()
    if args.output.exists():
        with args.output.open() as handle:
            for line in handle:
                try:
                    seen_urls.add(json.loads(line).get("url") or "")
                except json.JSONDecodeError:
                    continue
        print(f"resuming: {len(seen_urls)} articles already collected")

    page = 1
    written = 0
    with args.output.open("a") as handle:
        while True:
            for attempt in range(5):
                try:
                    response = fetch_page(args.api_key, args.from_date, args.to_date, page, args.page_size)
                    break
                except Exception as exc:
                    wait = 5 * (attempt + 1)
                    print(f"page {page} failed ({type(exc).__name__}: {exc}); retrying in {wait}s")
                    time.sleep(wait)
            else:
                raise SystemExit(f"page {page} failed after retries; wrote {written} rows, rerun to resume")

            for item in response.get("results") or []:
                row = to_evidence_row(item)
                if not row["url"] or row["url"] in seen_urls or not row["full_text"]:
                    continue
                seen_urls.add(row["url"])
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                written += 1
            handle.flush()

            total_pages = int(response.get("pages") or 1)
            if page % 10 == 0 or page >= total_pages:
                print(f"page {page}/{total_pages} | written {written} | total available {response.get('total')}")
            if page >= total_pages or (args.max_pages and page >= args.max_pages):
                break
            page += 1
            time.sleep(args.sleep)

    print(f"done: {written} new rows in {args.output}")


if __name__ == "__main__":
    main()

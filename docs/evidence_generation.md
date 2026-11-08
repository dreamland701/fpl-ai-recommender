# Evidence Generation

This project builds weekly evidence packets from timestamped source rows so model training and serving can use the same information boundary.

## Source Corpus

- `reports/evidence_2025_26_gw1_30_google_news.jsonl` is the raw 2025-26 GW1-GW30 Google News RSS corpus.
- Each row keeps `published_at`, `window_start`, and `deadline_ts` from the acquisition pass. Enrichment must not change these fields.
- Rows are categorized as `official_scout`, `official_premier_league`, `official_club`, or `trusted_news` using source URL and source-name heuristics in `src/fpl_ai/weekly_evidence.py`.

## Full-Text Enrichment

Use `enrich_evidence_fulltext` for source-filtered enrichment runs and `enrich_premierleague_fulltext` for the PL-only path.

Recommended workflow:

1. Start from the raw Google News JSONL.
2. Run a high-signal source filter first, such as Premier League, BBC, ESPN, Sports Illustrated, official club domains, and Fantasy Football Scout.
3. Inspect the generated report for `resolve_failed`, `resolved_no_text`, and `error` counts.
4. Add source-specific resolver or parser tests before changing extraction logic.
5. Write enriched output to a new JSONL/report pair rather than overwriting the raw corpus.

Full-text enrichment may set `resolved_url`, `full_text`, `full_text_chars`, `extraction_status`, and replace `content` with extracted text. It must not alter `published_at`, `deadline_ts`, or `window_start`.

## Skew Prevention

Training and serving should both consume evidence through the packet selection boundary:

- Select only documents where `published_at <= deadline_ts`.
- Preserve the same `lookback_days` and `max_documents` defaults when comparing offline training to serving behavior.
- Treat post-deadline articles, edited pages, and missing publication metadata as unsafe for that gameweek.
- Prefer raw RSS `published_at` for timestamp quality, even when full text is fetched later from a canonical URL.

This prevents the model from seeing post-deadline injury, lineup, or price-change information during training that would not have been available at serving time.


## V2 Source Notes

The v2 historical backfill adds an explicit Sky Sports query:

```text
(site:skysports.com) ("team news" OR injury OR injured OR fitness OR "Premier League")
```

This substantially increases Sky Sports metadata coverage for the 2025-26 GW1-GW30 corpus. These rows still come from Google News RSS, so they usually contain title/snippet/source metadata rather than full article text. For future serving, direct RSS collection now includes `sky_sports_football_rss`, which provides real Sky article URLs at collection time and avoids later Google News URL recovery.

Known full-text limitations:

- Google News wrapper URLs do not expose publisher article bodies.
- Exact-title Google resolution can return `google.com/sorry` from this host, especially after repeated resolution attempts.
- Yahoo Sports UK rows frequently cannot be reconstructed from title-only slug guesses; direct publisher URL capture at collection time is preferred.
- Official Premier League/FPL Scout full text is available when canonical `premierleague.com/en/news/...` URLs are resolved. Current preserved extraction has 101 full-text PL rows.

Preferred future collection order:

1. Direct official FPL snapshot before deadline.
2. Direct Premier League/FPL Scout URLs when available.
3. Direct source RSS feeds such as Sky Sports Football, BBC, Guardian, and official club RSS feeds.
4. Google News RSS as a historical/backfill fallback.
5. Full-text enrichment only after preserving original `published_at` and source metadata.

## Focused Official FPL + Sky Podcast Full-Text Corpus

For experiments that should avoid snippet-only rows, build a focused corpus:

```bash
PYTHONPATH=src python scripts/build_fpl_sky_fulltext_corpus.py
```

This reads:

- `reports/evidence_2025_26_gw1_30_google_news_v3_podcasts.jsonl`
- `reports/evidence_2025_26_gw1_30_google_news_pl_fulltext.jsonl`

It writes:

- `reports/evidence_2025_26_gw1_30_v3_podcasts_pl_fulltext.jsonl`
- `reports/evidence_2025_26_gw1_30_fpl_sky_fulltext_focus.jsonl`
- `reports/evidence_packets_2025_26_gw1_30_fpl_sky_fulltext_focus.jsonl`
- `reports/evidence_2025_26_gw1_30_fpl_sky_fulltext_focus_report.json`

The focused file keeps only rows with real extracted text:

- Official Premier League/FPL Scout article bodies with `extraction_status=full_text_extracted`.
- Sky Sports Fantasy Podcast and Sky Sports Premier League Podcast RSS episode summaries with `extraction_status=rss_episode_summary`.

Sky podcast rows are not transcripts. They are dated episode summaries from the direct Captivate feeds after repeated Sky promotional boilerplate is stripped. Exact podcast dialogue requires a separate audio-transcription pass over the MP3 enclosure URLs.

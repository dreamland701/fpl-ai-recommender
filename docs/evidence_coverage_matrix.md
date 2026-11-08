# Evidence Source Coverage Matrix

Updated: 2026-07-05. Update this table whenever a backfill lands or a source audit changes.
"Consistent since" = earliest season where the source exists in substantially the same shape
(the criterion for using it in multi-season training).

| Source | Access | Consistent since | Full text? | Timestamps | Status |
|---|---|---|---|---|---|
| PL / FPL Scout articles | canonical URL scrape | 2025-26 verified; 2022-25 backfill TODO | yes (when URL resolves) | page metadata | 2025-26 GW1-30 collected |
| Sky Sports PL Podcast (transcripts) | RSS MP3 → Whisper large-v3 | **2015-11** (1,697 episodes audited) | yes (transcript) | episode pubDate | pipeline verified; season runs pending |
| Sky Sports Fantasy Podcast (transcripts) | RSS MP3 → Whisper large-v3 | **2024-08 only** (feed migration) | yes (transcript) | episode pubDate | pipeline verified |
| Sky podcast RSS summaries | RSS description | 2025-26 collected | no (summary) | episode pubDate | superseded by transcripts |
| The Guardian Football | Open Platform API | **pre-2021 (to 1999)**, ~150 articles/wk | yes (bodyText, avg ~5k chars) | webPublicationDate (exact) | **2022-26 backfilled** (5,727 + 6,792 + 6,296 + 7,037 rows in `reports/evidence_guardian_football_{2022_23,2023_24,2024_25,2025_26}.jsonl`) |
| BBC Sport football | RSS + scrape | RSS current-only; historical needs archive | partial | RSS pubDate | RSS in evidence_collect.py; historical TODO |
| Google News RSS | search RSS | backfill-quality only | snippets mostly | mixed quality | collected 2025-26; fallback only |
| FPL API crowd signals (ownership/transfers/price) | official API via ingest | **2016+ (all our seasons)** | n/a (structured) | event-level | in feature table; momentum derivations TODO |
| Reddit r/FantasyPL | Arctic Shift dumps | 2021-22+ available | yes | post timestamps | stretch; not started |

## Notes

- Guardian is the historical text backbone for 2022-25 training seasons (PL/Scout full text
  is only verified for 2025-26; Sky transcripts cover all seasons but cost GPU time).
- Sky transcript season runs should be scheduled when the GPU is not training (each season
  ≈ 40-80 relevant episodes; measured ~2-4x realtime on the GB10 via transformers Whisper).
- Guardian production backfills need a registered developer key (`GUARDIAN_API_KEY`);
  the shared `test` key is throttled and for prototyping only.
- Evidence rows all use the shared corpus schema; `source_key` + `extraction_status`
  identify provenance downstream.
- Evidence is attached to corpus rows **per player** (name-mention matching) by
  `scripts/attach_player_evidence_to_corpus.py`; the exporter's week-level selection
  is superseded for the residual pipeline.

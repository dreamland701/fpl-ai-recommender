# Evidence/article quality review — 2026-07-26

Independent, CPU-only, read-only review requested by Wes while the GPU ran
the E8 pipeline: how is our text evidence generated, is it actually good,
and does anything need fixing. No model calls — this is me (Claude) reading
raw JSONL rows directly. Reviewed ~25 sample rows across the four evidence
sources that feed the SFT forecast corpus, plus scanned the in-progress
podcast transcript file for systematic issues.

## The four sources and how each is generated

1. **PL/FPL Scout articles** (`reports/evidence_pl_scout_2022_26.jsonl`,
   2,808 rows, 2022-23 → 2025-26). Collected via the official Pulselive
   API (`scripts/backfill_pl_scout_articles.py`), tag
   `content-creator:The-Scout`. Full article bodies, official first-party
   FPL analysis (captaincy picks, differential picks, bonus-point recaps,
   defensive picks, price-rise reports). Present in every season, ~38-39
   articles/season.
2. **The Guardian Football** (`evidence_guardian_football_2025_26.jsonl`
   etc., 25,852 rows across 2022-26). Collected via the Guardian Open
   Platform API (`content.guardianapis.com/search`, tag
   `football/football`), full `bodyText`. ~150 articles/week — this is
   the *general* football tag, not an FPL-specific feed.
3. **Sky Sports written FPL tips** (`evidence_sky_fpl_expert_tips_2022_26.jsonl`,
   45-49 rows). A weekly expert Q&A column, scraped from canonical
   skysports.com URLs enumerated via Wayback CDX + live fetch. Ran
   2022-23 through 2023-24 GW14, then the column was discontinued.
4. **Sky Sports Fantasy Podcast transcripts** (NEW this run,
   `evidence_sky_podcast_transcripts_fantasy_2024_26.jsonl`, in progress,
   32/79 done at review time). RSS feed → MP3 download → Whisper
   large-v3 transcription (`scripts/transcribe_sky_podcasts.py`). Feed
   exists since the Aug-2024 migration, so covers all of 2024-25 +
   2025-26. This is genuinely new signal, not previously used in any
   E-rung.

## Sample readings and per-source assessment

**PL Scout** — consistently on-topic, prose-based, factual, correct
prices/names. Example: *"Who are the best FPL captain for Gameweek 24?"*
(2026-01-30) opens "If you're willing to go against Erling Haaland
(£15.0m)... both Bruno Fernandes (£9.5m) and Gabriel (£6.9m) have the
form and fixture..." — exactly the kind of decision-relevant analysis the
forecast adapter should condition on. One weakness: some articles (e.g.
"FPL GW37 bonus points") are near-pure stat-table dumps ("3pts 2pts 1pt
Aston Villa 2-0 Spurs Konsa Kamara Torres...") rather than prose — still
factually correct and player-specific, just low information density per
character, which matters given the tight per-doc char budgets downstream.

**Guardian** — well-written, professionally edited, but the `football`
tag is general football, not FPL. Of 5 random samples, 2 had zero
fantasy relevance at all (a Socceroos World Cup preview, an Iranian
women's-football humanitarian-visa story) — pure noise for this project.
The other 3 (Son's Spurs farewell, a Bournemouth/Doak transfer, Salah's
dressing-room apology reported by Curtis Jones) are legitimately
fantasy-relevant (squad standing, transfer/injury signal, dressing-room
status). **Opinion: Guardian's raw yield is low** — most of the ~150
articles/week are not about Premier League squads at all — but the
per-player name-matching in `attach_player_evidence_to_corpus.py`
already filters on this (an article only attaches to a player-week if
the player's name appears in it), so the noise mostly doesn't reach
training rows. It does mean Guardian's *effective* FPL coverage is much
thinner than the raw article count suggests.

**Sky written tips** — high quality, structured Q&A directly from named
FPL experts (e.g. FPL Family, FPL Heisenberg), consistently on-topic and
decision-focused ("What are you doing with Haaland if he is injured for
one or two weeks?"). The problem is coverage, not quality: only 45-49
articles total, and the column stopped after 2023-24 GW14 — this source
contributes **nothing** to 2024-25 or 2025-26, which are exactly the two
most recent (and for E7/E8, the most heavily weighted) training seasons.

**Sky Fantasy Podcast transcripts** — by far the richest raw content
(30-50k characters per episode vs. a few thousand for written pieces),
genuinely detailed FPL analysis in natural spoken language (transfer
targets, captaincy debates, chip timing). But two real transcription
quality issues showed up on inspection:

1. **Player mentions are not front-loaded** (the actual finding of this
   review, verified not just eyeballed): I measured where a matched
   player's name first appears in the transcript text. For a Cole
   Palmer-tagged episode, the first mention was at char 36,680 of 52,392
   — **70% into the document**. Podcasts open with banter/recap before
   getting to specific players. **This mattered materially**: both
   `attach_player_evidence_to_corpus.py` (prefix-truncates to
   `--max-chars-per-doc`, default 6000) and
   `build_residual_player_forecast_split_v2.py` (further prefix-truncates
   to `--max-evidence-chars`, 260/800) were doing `content[:budget]` —
   a plain prefix cut. Chained together, a podcast episode matched on
   "Cole Palmer" would have shown the model only the show's cold open,
   **never the Palmer discussion that caused the match in the first
   place**. Short news articles (which front-load the lede) were mostly
   unaffected; this was silently neutering the new podcast source
   specifically. **Fixed** (both files, CPU-only, no GPU involved):
   truncation is now centered on the player's first name-mention instead
   of the document start, with the old prefix-cut behavior preserved as
   the fallback when no mention is found. Verified end-to-end on the
   Palmer example: the final 260-char window that reaches the model now
   reads "...one player who was part of most teams in the last season
   Cole Palmer but the price rise from 5 million to 10.5 million..." —
   the actually-relevant text.
2. **Whisper chunk-boundary duplication** (lower severity, not fixed):
   scanning the 32 transcripts done so far, ~16% (5/32) contain a
   repeated passage where the same sentence appears twice in a row, once
   with a slightly different spelling of a player's name (e.g. "Yancuba
   Minte" / "Yankuba Minte" for what's actually Brighton's Yankuba
   Minteh) — a known artifact of `chunk_length_s=30` long-form chunking
   in the HF ASR pipeline. Also spotted a clean mis-hearing elsewhere:
   "Cole Palmer" transcribed once as "Claude Palmer." Neither is fixed
   tonight — duplication mostly wastes a little token budget rather than
   destroying signal, and outright name mis-hears are a small fraction
   of mentions, but if podcast evidence proves valuable, the fix is
   straightforward: pass a `--hotwords`/`initial_prompt` vocabulary list
   of current Premier League player surnames into the Whisper call to
   bias transcription toward the right spellings.

## Overall opinion

The article/evidence *quality* is good where it's on-topic (PL Scout,
Sky tips, and the podcast once its content is actually reached) — real,
specific, decision-relevant FPL analysis, not vague filler. The bigger
problems were **pipeline problems, not content problems**:
Guardian's raw yield is diluted by general-football noise (already
mitigated downstream), Sky written tips dried up two seasons ago, and the
truncation bug above meant the single richest new source almost never
reached the model in the way it was wired. The truncation fix is applied
now and lands automatically in E8's corpus build later in the pipeline
(transcription is still running as of this review — no GPU work was
touched). The chunk-duplication/name-mishearing issue is real but minor;
worth a `--hotwords` pass later if podcast evidence proves valuable in
E8's gate result.

**If E8 doesn't show a clean win**, the honest first suspect should be
"podcast evidence still isn't dense enough per player-week to move the
needle" (2 docs × 260 chars is a small window even when correctly
centered) rather than "the underlying content wasn't good" — the content
read as genuinely informative in every sample pulled.

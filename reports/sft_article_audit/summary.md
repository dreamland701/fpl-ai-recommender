# SFT article audit (reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38, reports/llm_residual_v2_e22_top96_eval_2627_2_6)

Rows 15168 (train 13536, eval 1632, live 0); docs 24565.

## Coverage, recency, relevance

| split | rows | rows with ≥1 doc | docs/row (mean) | docs naming the player | …with an availability cue | median age of newest doc (h) | docs ≤24 h | docs ≤72 h | liveblog/match-report docs | snippet chars (median) |
|---|---|---|---|---|---|---|---|---|---|---|
| train | 13536 | 0.86 | 1.62 | 0.94 | 0.26 | 64 | 0.10 | 0.39 | 0.46 | 265 |
| eval | 1632 | 0.86 | 1.62 | 0.93 | 0.23 | 68 | 0.09 | 0.34 | 0.50 | 265 |

## By season (train+eval)

| season | rows | rows with docs | docs/row | docs naming player | availability-cue docs | newest doc age median (h) |
|---|---|---|---|---|---|---|
| 2022-23 | 3648 | 0.82 | 1.54 | 0.95 | 0.28 | 61 |
| 2023-24 | 3648 | 0.88 | 1.66 | 0.95 | 0.26 | 68 |
| 2024-25 | 3648 | 0.89 | 1.68 | 0.95 | 0.26 | 63 |
| 2025-26 | 3648 | 0.85 | 1.61 | 0.93 | 0.25 | 68 |
| 2026-27 | 576 | 0.86 | 1.57 | 0.96 | 0.22 | 74 |

## Sources

| source | docs | share | naming player | availability cue | median age (h) | liveblog |
|---|---|---|---|---|---|---|
| BBC | 29 | 0.001 | 1.00 | 0.14 | 51 | 0.00 |
| Premier League | 3823 | 0.156 | 0.93 | 0.23 | 69 | 0.00 |
| Sky Sports | 275 | 0.011 | 0.92 | 0.49 | 40 | 0.00 |
| The Guardian Football | 20337 | 0.828 | 0.95 | 0.26 | 109 | 0.56 |

## Duplication

Distinct docs 7431 for 24565 doc slots: a doc appears in 3.3 prompts on average (max 32); 0.22 of distinct docs sit in ≥5 players' prompts of the same week.

## Actionability: did the text say it before it happened?

| group (status 'a' rows only, i.e. the flag did not warn) | rows | any doc | doc names player | names player + availability cue |
|---|---|---|---|---|
| nailed starter, played ≥60 | 7707 | 0.87 | 0.84 | 0.34 |
| nailed starter, <45 min | 292 | 0.87 | 0.82 | 0.35 |
| nailed starter, did NOT play | 295 | 0.88 | 0.85 | 0.38 |
| unexpected starter (P<0.5, ≥60 min) | 387 | 0.75 | 0.73 | 0.38 |

Same groups, all statuses:

| group | rows | flagged (status≠a) | any doc | names player + cue |
|---|---|---|---|---|
| nailed starter, played ≥60 | 9619 | 0.20 | 0.87 | 0.34 |
| nailed starter, <45 min | 368 | 0.21 | 0.86 | 0.35 |
| nailed starter, did NOT play | 445 | 0.34 | 0.87 | 0.41 |
| unexpected starter (P<0.5, ≥60 min) | 479 | 0.19 | 0.78 | 0.41 |

Docs attached to the 'nailed starter, did NOT play' rows, by source:

| source | docs | naming player | with cue |
|---|---|---|---|
| BBC | 1 | 1.00 | 0.00 |
| FourFourTwo | 1 | 1.00 | 1.00 |
| Liverpool FC | 1 | 1.00 | 1.00 |
| London Evening Standard | 1 | 1.00 | 1.00 |
| Premier League | 37 | 0.92 | 0.24 |
| Sky Sports | 4 | 1.00 | 0.25 |
| The Guardian Football | 427 | 0.94 | 0.26 |
| The New York Times | 1 | 1.00 | 1.00 |
| beIN SPORTS | 1 | 1.00 | 1.00 |

## Verdict (2026-10-18)

The text going into the SFT carries almost no pre-deadline information:

- **Stale.** The newest document attached to a prompt is 64 hours old at the median; only 10% of documents are from
  the last 24 hours before the deadline and 39% from the last 72 (the corpus deliberately excludes the final 12 h to
  match the live refresh, but the 24–72 h band is nearly empty too).
- **Match reports, not news.** 83% of documents are Guardian pieces and 56% of those are live blogs of the previous
  match; the snippet is 265 characters around the player's name ("Dias comes across and takes out Antonio with a
  mistimed slide tackle"). The classic signal already prices the previous match through points, minutes, xG and
  ICT features, so this text is redundant by construction.
- **Thin.** 1.6 documents per row, never more than 2, 14% of rows have none.
- **Not actionable.** On the rows where text could have mattered, nailed starters whose official flag said
  available and who then did not play (295 rows), a document naming the player with any availability wording was
  present 38% of the time, against 34% for nailed starters who played the full match. The same 4-point lift holds
  for unexpected starters. The text does not warn; the official status line (flag ≠ a) covers 34% of those absences
  and nothing else does. Sky Sports pieces are the only source whose snippets carry availability wording half the
  time, and they are 1% of the documents.

This is why four SFT recipes and the regression head found no player-specific points signal, why the availability
edge is small and mostly recalibration, and why a larger reader (R5, the 31B expert reader) could not do better:
there is little to read. Model scale cannot create information that is not in the input.

**Information ceiling.** Unflagged absences among nailed starters are 3.7% of their rows, about 0.4 squad players
a week; catching every one with perfect team news is worth roughly 2–4 points each, so the ceiling of a perfect
pre-deadline availability feed is about 1 point a week (≈ +40 over the 21-window bench if half were caught), below
the bench's detection bar even on expected points. Points-side text is priced by the market already
(`fpl-article-source-value`).

**What "better articles" would actually mean.** Pre-deadline team news: Thursday/Friday press-conference injury
updates, official club injury bulletins and predicted line-ups, published 6–40 hours before the deadline. The live
refresh could capture them today by running later (Friday evening PDT for a Saturday deadline); the training corpus
cannot, because no historical archive of that material is on disk, and building one is a multi-day scrape with the
ceiling above.

## Live sources checked (2026-10-18)

- The Guardian API key works (HTTP 200); the live refresh collects Guardian + Premier League Scout articles.
- The Sky Sports RSS and Premier League news fetchers in `evidence_collect` return 0 records; the Guardian and BBC
  RSS feeds return ~12 recent items, too thin to carry team news at refresh time.
- The Premier League content API's "team news" stream is match-day line-up posts ("Forest team news: Gibbs-White
  misses out against Arsenal"), published after the deadline, so it is not a pre-deadline source and not a
  historical one either. The 3,369 Premier League documents in the corpus are Scout picks and "FPL lessons";
  only 24 are team-news pieces.
- The live corpus (2026-27 GW2-6) has the same profile as training: 903 docs, none within 12 h (by design), 95
  within 24 h, 601 of 903 three to seven days old, 403 live blogs.

Cheapest live improvement: run the final refresh later (the GW8 deadline is Friday 17:30 UTC, so Friday 07:00 PDT
catches Thursday pressers), and the weekly sheet keeps the official status line as the availability authority.

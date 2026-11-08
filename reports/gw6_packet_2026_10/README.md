# GW6 deadline packet (2026-27) — corrected pipeline vs the pre-fix pipeline

- **Deadline:** 2026-10-10 10:00 UTC (first kickoff Arsenal v Leeds, 11:30 UTC).
- **Snapshot:** official FPL API frozen at **2026-10-04 06:51 UTC** (`snapshot/`). Both pipelines read the same files.
- **Data:** 2026-27 history through GW5. GW5 was confirmed settled by `scripts/gw_status.py --event 5` (finished, data checked).
- **Decisions:** classic ridge + F6 on the fixed pipeline. The E11-full adapter is decoded in shadow (GPU approved 2026-10-04); it is logged, not used for the decision.

## Your entered team (confirmed 2026-10-04)

Your FPL entry (ID 6535607) was pulled from the public API and matches the Transfers screen you pasted:

- **Squad (15):** Donnarumma, Sels; Konsa, Mitchell, Bijol, Justin, N.Williams; Saka, Groß, Cherki, B.Fernandes, Cunha; Evanilson, João Pedro, Isak.
- **Bank and transfers:** £0.3m in the bank, 1 free transfer.
- **Chips:** none used, so Wildcard, Free Hit, Bench Boost and Triple Captain are all available. The first set runs to GW19.
- **Selling prices:** recomputed from purchase prices (your transfer history plus launch prices), and all 15 match the app (`entry_state.json`). Groß now sells at 5.7, up 0.1 since 28 September.

Re-run with `fetch_entry.py` → `snapshot.py` → `entry_state.py` → `forecast.py new` → `decide.py` → `route_lineups.py`. Every script honours `PACKET_DIR`.

**A refreshed packet is scheduled for Friday 9 October, 17:00 UTC (10:00 your time).** It will have:

- fresh prices, injury flags and news after the press conferences
- your entry re-read, including any transfers you have already made
- the E11-full shadow decode, plus E20's if it has trained by then

It will be written to `final/README.md`.

## Why the forecasts moved

| | GW6 (old → fixed) | GW6–10 (old → fixed) |
|---|---|---|
| Haaland | 6.21 → **8.15** | 28.7 → **39.6** |
| B.Fernandes | 5.57 → 6.17 | 25.9 → 31.0 |
| João Pedro | 2.14 → 3.02 | 12.5 → 16.1 |
| Groß | 5.47 → 6.15 | 23.5 → 25.9 |

Three things drive this.

**The pre-fix live pipeline had an ownership-unit bug that only existed live.** Training stored ownership as raw manager counts (Haaland around 8 million). The live builder fed in percentages (73.9). The model therefore read Haaland as almost unowned. His "ownership change" feature came out at −7,989,275: today's 73.9% minus last week's count.

With the coefficients the old model actually learned, this alone moved high-ownership players' 5-week forecasts:

- Haaland −5.6
- João Pedro −5.4
- Bruno −2.7
- Cherki −1.2

(`ownership_units_decomposition.json`). Backtests never saw it, because their units were consistently wrong. This is a concrete mechanism behind the GW2 "Haaland ranked 43rd" problem.

**The fixed model leans on correctly scaled ownership.** Ownership at 73.9% now adds +9.5 points to Haaland's 5-week forecast (`contrib_*.json`).

**The old 5-week head had large offsetting weights on overlapping features.** For Haaland: ICT index −24, threat +15, influence +10, and two opponent-strength terms −9 and +6. On the rebuilt data these shrink to −7, +3.5, +3.3, −0.9 and −0.1.

**Is the fixed model now too high on premiums?** In 84 historical backtest weeks, its bias on players priced £10m+ is −0.01 points per week for next-week forecasts. Over five weeks it is +1.25 (about +0.25 per gameweek, not significant). Shading Haaland's 39.6 to about 38 would account for that. His actual 2026-27 scores are 2, 13, 9, 9, 6, an average of 7.8. His last four seasons averaged 7.2, 5.7, 4.8 and 6.3 per game. So 7.9 per gameweek is in line with current form but above his longer history.

## Your squad and the main targets (fixed pipeline, with old values)

| Player | Pos | GW6 opp | Price | Own % | Status | GW6 old → fixed | GW6–10 old → fixed |
|---|---|---|---|---|---|---|---|
| Sels | GK | CRY (A) | 5.0 | 1.6 | a | 2.45 → 2.60 | 11.5 → 12.5 |
| Donnarumma | GK | LIV (A) | 5.5 | 7.6 | a | 2.56 → 2.61 | 13.2 → 14.0 |
| Bijol | DEF | ARS (A) | 5.0 | 0.7 | a | 0.41 → 0.47 | 5.0 → 5.2 |
| Mitchell | DEF | NFO (H) | 4.5 | 6.1 | a | 3.13 → 3.04 | 14.2 → 14.4 |
| Justin | DEF | ARS (A) | 4.5 | 1.4 | a | 3.03 → 2.82 | 15.7 → 14.9 |
| N.Williams | DEF | CRY (A) | 5.0 | 8.7 | a | 3.40 → 3.19 | 15.0 → 15.1 |
| Konsa | DEF | LEE (H) | 4.6 | 19.4 | a | 3.38 → 3.30 | 13.0 → 13.6 |
| B.Fernandes | MID | TOT (H) | 11.9 | 38.5 | a | 5.57 → 6.17 | 25.9 → 31.0 |
| Cunha | MID | TOT (H) | 7.9 | 5.8 | a | 4.06 → 4.09 | 18.0 → 19.0 |
| Saka | MID | LEE (H) | 9.5 | 13.8 | a | 4.90 → 4.82 | 23.2 → 24.6 |
| Groß | MID | SUN (A) | 5.9 | 29.2 | a | 5.47 → 6.15 | 23.5 → 25.9 |
| Cherki | MID | LIV (A) | 7.8 | 28.4 | a | 4.45 → 4.32 | 21.1 → 22.2 |
| João Pedro | FWD | BOU (H) | 7.7 | 65.0 | **d** knee, 75% | 2.14 → 3.02 | 12.5 → 16.1 |
| Isak | FWD | MCI (H) | 9.1 | 22.3 | **d** thigh, 75% | 4.02 → 3.76 | 18.4 → 18.8 |
| Evanilson | FWD | CHE (A) | 6.0 | 3.2 | a | 3.26 → 3.42 | 15.6 → 16.1 |
| *Haaland* | FWD | LIV (A) | 15.6 | 73.9 | a | 6.21 → 8.15 | 28.7 → 39.6 |
| *De Cuyper* | DEF | SUN (A) | 5.0 | 27.9 | a | 4.55 → 4.74 | 20.1 → 21.0 |
| *E.Le Fée* | MID | BHA (H) | 5.7 | 3.4 | a | 3.63 → 3.92 | 16.0 → 17.5 |
| *Xhaka* | MID | BHA (H) | 5.5 | 3.6 | a | 3.69 → 3.72 | 16.8 → 17.3 |

## Options (fixed pipeline)

Gain is over GW6–10 versus holding, net of hits. It uses the route scorer from `haaland_routes.py`: best legal XI on 5-week points, captain doubled, plus 0.1 × the outfield bench.

| Option | GW6–10 gain | Pre-fix pipeline said | Bank after | GW6 XI forecast (incl. C) |
|---|---|---|---|---|
| Hold | 0 | 0 | 0.3 | 51.1 |
| Bijol → De Cuyper (1 FT) | **+7.5** | +6.8 | 0.3 | 52.7 |
| Bruno + Isak → Haaland + Le Fée (−4) | **+11.9** | +0.9 (Belloumi variant) | 0.0 | 55.2 before hit |
| Bruno + Isak → Haaland + Xhaka (−4) | +11.6 | — | 0.2 | 55.0 before hit |
| Bijol + Bruno + Isak → De Cuyper + Le Fée + Haaland (−8) | +15.4 | +3.7 | 0.0 | 56.9 before hit |
| Roll the FT, do Bruno + Isak → Haaland + Le Fée in GW7 (2 FTs) | +11.8 | +4.0 | 0.0 | 51.1 in GW6 |
| Wildcard (full rebuild, GW6–10) | +34.6 | +30.2 | 0.1 | — |
| Free Hit (GW6 only) | +9.0 (one week) | +8.0 | 0.0 | — |

Lineups (`route_lineups.json`; bench order is the order to enter, GK first):

- **Hold:**
  - XI: Donnarumma; Konsa, N.Williams, Mitchell; Bruno, Groß, Saka, Cherki, Cunha; Isak, Evanilson.
  - Bench: Sels > João Pedro > Justin > Bijol.
  - Captain Bruno, vice Groß.
- **Bijol → De Cuyper:**
  - XI: same, with De Cuyper for Mitchell.
  - Bench: Sels > Mitchell > João Pedro > Justin.
  - Captain Bruno, vice Groß.
- **Bruno + Isak → Haaland + Le Fée:**
  - XI: Donnarumma; Konsa, N.Williams, Mitchell; Groß, Saka, Cherki, Cunha, Le Fée; Haaland, Evanilson.
  - Bench: Sels > João Pedro > Justin > Bijol.
  - Captain Haaland, vice Groß.

## Shadow read: E11-full adapter (logged, not used for the decision)

Decoded on 2026-10-04 on the fixed pipeline's classic baselines, the non-F6 table E11-full was trained on (`shadow_e11full.json`); all 667 responses parsed. It behaves as in earlier weeks:

- **Points:** a near-uniform cut that grows with the forecast. For GW6: Haaland 8.27 → 6.77, Bruno 6.15 → 5.05, Groß 5.91 → 4.91.
- **P(appear):** a uniform +0.05 to +0.11 for likely starters, with João Pedro 0.40 → 0.61.
- **Decisions:** on its own forecasts the decision layer keeps Bruno as captain and prefers N.Williams → Hall (+2.4) over Bijol → De Cuyper.

That matches the 29 September finding that the adapter's gain is mostly a decision-neutral shrink. Classic + F6 makes the call.

## Shadow reads, 2026-10-08 (logged, not used for the decision)

**E20 SFT side by side** (`sft_side_by_side_E20_gw6.md`; planned Bijol → De Cuyper applied; evidence collected through 7 October):

- **Same XI and same captain as classic:** Groß, vice Bruno. The only practical difference is the bench: SFT puts João Pedro last (Sels; then Justin, Konsa, João Pedro), which fits the news that he is likely out.
- **The generic shrink this week is −0.34 for a 2-point player and −1.03 for an 8-point player.** It moves everyone the same way.
- **The four "player-specific" moves don't follow the text the adapter read:**
  - Groß −0.36, while the article says he was player of the month.
  - Rogers −0.41, while the articles praise his England performances.
  - De Cuyper −0.34, from transfer counts and a Nations League report.
  - João Pedro's chance of playing *rises* from 0.40 to 0.61, despite the knee news.
- This is the concrete picture behind "the player-specific part is mostly noise".

**Old RL planner (G2-v3), shadow:**

- It returned one week instead of three; the old parser filled the rest with defaults.
- Its GW6 call is to bank the free transfer, captain Mbeumo (not in your squad, so ignored) and play no chip.
- This illustrates why it is not trusted until the rebuilt G5 beats the same-chips planner.

## How to read this

- **Read the Wildcard figure as an upper-bound hint, not a forecast.** The squad builder that drafted it ignores captaincy (its squad has no Haaland), and picking 11 new players from noisy forecasts overstates the gain more than a one- or two-player move does. The first Wildcard must be used by GW19.
- **The model's view:** with the bug fixed, getting Haaland is worth about 4 more points over five weeks than the free Bijol → De Cuyper move. For GW6 alone the Haaland double is about level with holding once the −4 hit is paid. The case rests on GW7–10.
- **That 4-point margin is small.** Five-week forecast error for top players is about 8 points (mean absolute error). The fixed pipeline's backtest edge over the deployed one is positive but not yet proven: +191 points over 21 windows, t = 1.54.
- **Rolling to GW7 gives the same expected value without the hit.** You also learn about Isak's and João Pedro's fitness and the Liverpool–City result first. The cost is price risk on a route with £0.0m to spare: a Haaland rise or a Bruno/Isak drop breaks it. The Xhaka variant leaves £0.2m.
- **The backtest decision layer never proposes this move.** Its transfer search only sells the six weakest squad players (review item P2, "candidate pruning"). So a "sell two good players to fund a premium" move is outside what the backtests validated.

## Files

- `snapshot/`: frozen API responses and manifest (retrieval time, deadline).
- `forecasts_old_pipeline.jsonl`, `forecasts_new_pipeline.jsonl`: every player, both pipelines.
- `decision_sheet.json`, `route_lineups.json`: decision-layer output, routes and lineups.
- `ownership_units_decomposition.json`, `contrib_old.json`, `contrib_new.json`: why the forecasts moved.
- `entry/`, `entry_state.json`: your entry from the FPL API, with purchase and selling prices.
- `shadow_e11full.json`: the adapter's shadow read.
- Re-run (each honours `PACKET_DIR`):
  - `fetch_entry.py`
  - `snapshot.py`
  - `entry_state.py`
  - `PYTHONPATH=<code>/src forecast.py <old|new> <table> <out>`
  - `decide.py`
  - `route_lineups.py`
  - `shadow_sheet.py <examples> <predictions> <label>`
  - `final_summary.py`

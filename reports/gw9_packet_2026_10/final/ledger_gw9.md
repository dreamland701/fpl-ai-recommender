# GW9 ledger (settled Mon 2026-11-02; scored Tue 2026-11-03 21:45 PST from the public API: `entry/picks_gw9.json`, `entry/history_settled.json`, `entry/live_gw9.json`, `entry/transfers_settled.json`; hindsight XIs in `final/hindsight_gw9.json` via `scripts/settle_gw.py`)

| | |
|---|---|
| Entered move | João Pedro → Isak (free; sold 7.7, bought 9.1, bank 0.3), Wes's Wednesday call, as replayed in the final sheet. Captain Haaland, vice Rogers, no chip. |
| Entered XI | The final call exactly: Donnarumma; Konsa, N.Williams, De Cuyper; McGinn, Groß, Rogers, Cherki; Haaland, Evanilson, Isak. Bench as entered: Sels > Cunha > Justin > Mitchell (the Thursday order; the final sheet had Justin first — no auto-sub happened, so no effect). |
| GW9 points | **49** (league average 47); bench 8 (Sels 1, Cunha 2, Justin 2, Mitchell 3); no auto-subs |
| Overall rank | 3,147,238 → 3,195,261; season total 535 |
| Expected (own forecasts) | entered / final call 57.7; classic + SFT H5 57.5 (its own forecasts); role-override sheet 57.9 |

Realised: Konsa 10, De Cuyper 9, Rogers 9, Evanilson 9; Haaland 2 (×2 = 4), Isak 2 (90 min), Groß 2, Donnarumma 2,
N.Williams 1, Cherki 1 (35 min), McGinn 0 (86 min, missed penalty). Konsa's 10 = clean sheet + 2 bonus + the DefCon
bonus (15 contributions); De Cuyper assist + clean sheet; Rogers and Evanilson goals; Haaland 90 minutes without a return. The four big forecasts under-delivered (Haaland 8.4 → 2, Groß 4.7 → 2,
Isak 4.3 → 2, McGinn 3.4 → 0) and three defenders over-delivered; 57.7 expected → 49.

## Judgment calls

| Call | Verdict | Numbers |
|---|---|---|
| João Pedro → Isak (Wes's call; the Wed sheet had Thiago +7.2 / N.Jackson +7.1 / Isak +6.0 as a 5-GW coin flip) | −7 on the day vs either alternative | Isak 2 (90 min) vs Thiago 9, N.Jackson 9: the Thiago or Jackson XI scores 56. Holding the injured João Pedro (Justin + Cunha start) scores 50, so the move itself was −1. Minutes read right (P 0.79 / 71 min → 90), points blanked |
| Captain Haaland (8.38; most-captained league-wide) | −7 vs the vice | Haaland 2; Rogers (VC) 9, Konsa 10, De Cuyper 9, Evanilson 9 |
| N.Williams over Justin (coin flip, +0.06) | −1 | N.Williams 1 vs Justin 2; the SFT H5 XI (Justin) scores 50 vs 49 |
| Cherki in the XI (P 0.51, 3.54) with Justin first sub | −1 to −2 | Cherki played 35 min for 1; Justin 2, Cunha 2, Mitchell 3 sat on the bench. The auto-sub cover was not needed |
| No hit | RIGHT | Cunha → Tavernier (−4): Tavernier 3 for McGinn 0 = 52 gross, 48 net; Donnarumma + Cunha → Raya + Tavernier (−8): 55 gross, 47 net |
| Konsa → Calafiori not possible (0 FT) and not wanted | RIGHT | Konsa 10 in the XI; that route scores 41 |
| No Bench Boost (planner said no; +11.8 projected) | −8 in hindsight | 57 with the chip; bench 8 vs the +11.8 projection |
| No Wildcard / Free Hit (WC +38.5 projected GW9-13, FH +10.7) | −30 in hindsight, one week | Both MILP squads share the forecast XI Raya 5, Gabriel 6, Van Hecke 15, De Cuyper 9, Tavernier 3, Rogers 9, Groß 2, Palmer 8, Haaland 2, N.Jackson 9, Evanilson 9 = **79**. GW8's chip squads scored 39/32 vs the hold's 54, so two weeks net ≈ 0; the 14-window calibration (+16.8 projected → −0.7 realised) still stands |

Scorecard: transfer −7 vs the alternatives (−1 vs hold), captaincy −7, N.Williams −1, Cherki −1, no hit +1, Bench Boost −8
(hindsight), chip squads −30 (hindsight). 49 against an average of 47: +2, par.

## Classic vs classic+SFT XI in hindsight (realised points, auto-subs applied, plain captain)

| XI | Expected | Realised |
|---|---|---|
| Wes entered = final call (classic+F6 hold) | 57.7 | **49** |
| Classic + SFT H5 (Justin for N.Williams) | 57.5 own / 57.6 classic | 50 |
| Role override --auto (Konsa nailed): same XI | 57.9 | 49 |
| F16 Guardian-lineups shadow (API squad: Cunha for Justin) vs its base | 56.5 / 56.6 | 49 / 49 |
| Hold João Pedro (Wed hold XI: Justin + Cunha) | 55.5 | 50 |
| João Pedro → Thiago (Wed sheet pick) | 56.9 | 56 |
| João Pedro → N.Jackson | 57.3 | 56 |
| Cunha → Tavernier (−4) | 60.1 | 52 (48 net) |
| Donnarumma + Cunha → Raya + Tavernier (−8) | 61.5 | 55 (47 net) |
| Konsa → Calafiori | 57.4 | 41 |
| Final call + Bench Boost | 69.5 | 57 |
| MILP wildcard squad, forecast XI (+38.5 projected GW9-13) | 68.3 | 79 |
| Free Hit squad, forecast XI (+10.7 projected) | 68.3 | 79 |

The SFT's one XI difference (Justin for N.Williams) was +1; its availability reads were all "fit, starts" and all 15 played. The F16
shadow's Cunha-for-Justin swap was level (2 v 2).

## H5 shadow accuracy (`final/h5_gw9_accuracy.md`; final read of Sat 09:15Z, 669 players)

Points: RMSE classic 1.817 vs SFT 1.831, MAE 1.028 vs 1.119, bias +0.04 vs −0.13; on the 21 decision-relevant rows
(classic ≥ 4) 3.682 vs 3.701, SFT closer on 43%. Availability: Brier 0.0916 vs classic 0.1300 (uncertain rows 0.1387 vs
0.2155), AUC 0.952 vs 0.949 (uncertain rows 0.802 vs 0.765). Same profile as every live week: no points information, a
better-calibrated P(appear) (the classic P is minutes/90, not a probability). Twelve forecast starters did not play (White,
Guéhi, Henderson, Tielemans, Gravenberch, Lacroix …); the SFT raised most of them too.

## Carried forward to GW10 (deadline Fri 2026-11-06 18:30Z = 10:30 PST)

- 1 FT, bank 0.3. Isak stays the judgment: one blank in 90 minutes is not evidence either way.
- Chips BB / FH / WC all expire after GW19; chip planning starts with the GW10 packet. Two data points on the chip squads so
  far (−15/−22 in GW8, +30 in GW9) = noise around the calibration study's zero.
- Captaincy: Haaland's blank is the third week in a row the armband lost to a defender in the squad; the planner rule still
  takes the top forecast (8.4 vs 5.7). Not a reason to change: captain-timing studies say luck.
- Ingest done (`run_weekly_ingest.sh 9`, GW9 flagged 0.30); tables rebuilt with cutoff 9 (`scripts/run_post_ingest_rebuild.sh`);
  GW10 parity audit in `reports/gw10_packet_2026_11/parity_audit.md`.

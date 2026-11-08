# GW8 recommendation (interim, 2026-10-21 18:30 PDT; deadline Fri 2026-10-23 10:30 PDT)

**Context.** Saka went off after 10 minutes at Bayern (2026-10-21) with a thigh-muscle injury; Arteta: "a number of
weeks", scans pending. The FPL feed showed "Thigh injury - 50% chance of playing" (added 20:30 UTC). The classic
model on the feed as-is still prices him at P(appear) 0.76 (GW8 4.57, GW8-12 22.6) and would only move
Cunha → Rogers (+9.2). The decision therefore comes from the Saka-out scenario (his forecasts zeroed over GW8-12),
`interim_1021_saka_out/`.

**Do:** Saka → Rogers (free transfer; selling 9.5, buying 8.0, bank after 1.7). Captain Haaland, vice Rogers. No chip.

| route (GW8-12 value vs hold, net of hits) | gain | bank after |
|---|---|---|
| Saka → Rogers (free) | +12.6 | 1.7 |
| Konsa + Saka → Calafiori + Rogers (−4) | +17.1 | 0.2 |
| Donnarumma + Saka + N.Williams → Raya + Rogers + Calafiori (−8) | +19.3 | 0.1 |
| Wildcard (GW8-12) | +15.1 | 0.2 |
| Free Hit (GW8 only) | +5.4 | 0.2 |
| Saka → Palmer (free) alternative | GW8 XI 56.6 vs 57.1 with Rogers; GW8-12 25.1 vs 26.0 | 0.0 |

The −4 route's extra +4.5 over five weeks is inside one standard error of a two-player comparison; Konsa → Calafiori
is better taken as GW9's free transfer. The wildcard projects below the single free move and wildcard projections
have not realised in the past (chip calibration note).

**Lineup (Saka → Rogers), GW8 XI forecast 57.1 including the captain:**

| | players (GW8 forecast) |
|---|---|
| GK | Donnarumma 2.8 |
| DEF | De Cuyper 4.1, Justin 3.6, Mitchell 3.5, N.Williams 3.4 |
| MID | Rogers 5.9, Groß 4.4, Cherki 3.4 |
| FWD | Haaland 8.3 (C), João Pedro 5.6 (VC), Evanilson 3.8 |
| bench | Sels 2.6 > Cunha 3.3 (P(appear) 0.57) > Konsa 3.2 (0.81) > McGinn 2.8 (0.73) |

Marginal calls to re-check on Friday: Cherki (P(appear) 0.40 after 0 minutes in GW7) starts over Cunha (0.57, 6
minutes in GW7) by 0.04 of a point; whichever gets the better press-conference news starts, the other is first
outfield sub. Haaland is the captain by 2.4 points over the next best; Rogers (Chelsea v Spurs, Saturday 16:30) is
the vice.

**Fixtures.** Fri IPS v NFO (Sels, N.Williams); Sat AVL v MCI (McGinn; Donnarumma, Cherki, Haaland), ARS v EVE
(Konsa), CHE v TOT (Rogers, João Pedro); Sun LIV v BHA (De Cuyper, Groß), MUN v BOU (Cunha; Evanilson),
CRY v NEW (Mitchell), SUN v LEE (Justin).

**Next.** The H1 (E4B) side-by-side runs now (`side_by_side_h1_saka_rogers.md` / `_hold.md`). The final refresh
is armed for Friday 07:00 PDT (`scripts/run_gw8_final_refresh.sh`): it re-reads the feed (Saka's scan result,
Thursday pressers) and rebuilds the sheet into `final/`.

## Override after Wes's challenge (18:50 PDT): start Konsa and Cunha, bench N.Williams and Cherki

The model's XI differences here are 0.1 points, inside noise, and the numbers behind them are stale on two counts:

| player | model GW8 | expected minutes | per 90 | this season | GW8 context |
|---|---|---|---|---|---|
| Konsa | 3.25 | 73 | 4.0 | 0 and 11 min in GW1-2, then five straight 90s, 2 CS, 9 pts last week | ARS (4 CS, 0.71 conceded/g) home to EVE (1.14 scored/g) |
| N.Williams | 3.37 | 77 | 3.9 | 7/7 starts, 1 CS, 3.3 pts/g | NFO (3 CS, 1.29/g) away at IPS (1.57 scored/g) |
| Mitchell | 3.46 | 85 | 3.7 | 7/7, 1 CS, one 15-pt haul | CRY (1 CS, 2.43 conceded/g) home to NEW |
| Justin | 3.57 | 80 | 4.0 | 7/7, 2 CS, 4.9 pts/g | LEE (4 CS, 0.86/g) away at SUN (0.86 scored/g) |
| Cunha | 3.31 | 51 | 5.8 | six straight starts, 6.0 pts/g, then a 6-minute cameo at Liverpool in GW7, no news | MUN home to BOU (1.86 conceded/g) |
| Cherki | 3.35 | 36 | 8.4 | 4/7 60+ min, 7.3 pts/g when he plays, 0 min in GW7, no news | MCI (2.71 scored/g) away at AVL |

Konsa: the forecast is dragged by the minutes share from GW1-2; he is nailed now and in the best defence of the four
with the best clean-sheet fixture. The model's known weakness (elite-defence clean-sheet compression) runs the same
way. Start him over N.Williams. Cunha vs Cherki: the forecasts are equal and both are bets on who starts; Cunha's
cameo looks like a rest, Cherki is Pep rotation. The H1 side-by-side also starts Cunha (P(appear) read 0.56 → 0.81
vs Cherki 0.40 → 0.65). Start Cunha; Cherki first outfield sub so that if any starter blanks on minutes his points
come in when he plays.

**Final XI (model value 57.0 vs 57.1, no cost):** Donnarumma; De Cuyper, Justin, Mitchell, Konsa; Rogers, Groß,
Cunha; Haaland (C), João Pedro (VC), Evanilson. Bench: Sels, Cherki, N.Williams, McGinn. Transfer Saka → Rogers.
Re-check Friday: Cunha's and Cherki's starts in the pressers, Saka's scan.

## Chips (chip line `reports/chip_line_gw8_interim.md`, 18:55 PDT)

Priced this week: Triple Captain on Haaland +8.4 (best of the next four weeks +8.2, i.e. flat); Bench Boost +11.9;
Free Hit +9.2; Wildcard +35 over five weeks on the chip line's valuation (+15.1 on the decision sheet's; neither
has realised historically). The planner rule says "triple captain now" only because no double is published for the
half and this week's forecast is the best in its window by 0.2 points. The chip research found TC timing on
forecasts is a coin flip against random, so there is no edge either way. City's remaining fixtures to GW19 hold no
double; the leakiest opponents are Newcastle away in GW17 (2.0 conceded a game), Chelsea at home in GW15 (1.86)
and Villa away now (1.57). Call: hold the Triple Captain this week, target GW15 at home to Chelsea unless a double
appears; using it now is not wrong, it is a coin flip with 0.2 points on the table.

# GW9 recommendation (interim, Tue 2026-10-27 09:00 PDT; deadline Sat 2026-10-31 04:00 PDT = 11:00 UTC)

**Context.** João Pedro's feed status moved from "75% chance" (Saturday) to **injured, thigh, unknown return** (Monday); he
did not play GW8 and is 69.8% owned. Calafiori is **doubtful, hip, 75%** (added Sat 18:30 UTC, after he came off the
bench for 22 minutes at Everton); the Guardian's Friday article had predicted him to start, so the GW8 benching was
not readable before the deadline. Two packet fixes landed today: the decision sheet and the exact optimizer now zero
every player flagged i/s/u/n with no stated chance of at least 25% (the ridge is additive, so João Pedro still
carried GW9 3.57 / GW9-13 18.8 and sat in the hold XI of the optimizer), and the chip line no longer dies on the
examples-file tag. Bank £1.7m, 1 free transfer, chips left: Bench Boost, Free Hit, Wildcard (Triple Captain used GW8).

**Do (interim):** **João Pedro → Thiago** (Brentford, £7.8m; BRE v NFO Sat 15:00), the free transfer.
Captain **Haaland** (MCI v BHA, GW9 8.21), vice **Rogers** (CHE v MUN, 5.54). No chip.

| route (GW9-13 value vs holding, net of hits) | gain | GW9 only | bank after |
|---|---|---|---|
| João Pedro → Thiago (free) | **+7.2** | +1.7 | 1.6 |
| João Pedro → N.Jackson (AVL, £6.7m; GW9-13 19.3 vs Thiago 21.4) | ≈ +5 | — | 2.7 |
| Sels + João Pedro → Raya + Thiago (−4) | +10.1 | — | 0.4 |
| Cunha + João Pedro + N.Williams → Gabriel + Tavernier + Thiago (−8) | +13.2 | — | 0.2 |
| Konsa → Calafiori (free) | 0.0 (XI unchanged, 55.2 either way) | 0.0 | 0.3 |
| Wildcard (GW9-13, exact optimizer) | +33.9 projected | — | 0.0 |
| Free Hit (GW9 only, exact optimizer) | +8.0 projected | — | — |

The −4 route's extra +2.9 over five weeks is inside one standard error of a two-player comparison; Raya (£6.2m, GW9-13
20.9, 1.00 to play) is the natural GW10 free transfer (ARS v HUL at home) if Donnarumma or Sels is to go. Wildcard
projections have not realised in the past (+16.8 projected → −0.7 realised over 14 windows, chip-calibration note), and
this one is built on the same forecasts that just lost João Pedro; keep the chips.

**Konsa → Calafiori is off the table this week.** With the hip flag the model gives Calafiori P(appear) 0.59 and
GW9 3.31 against Konsa's 3.34 (both Arsenal, away at Liverpool on Sunday), so the swap moves nothing and spends the
free transfer the João Pedro slot needs. Revisit once he is unflagged.

**Lineup (João Pedro → Thiago), GW9 XI forecast 56.5 including the captain:**
Donnarumma; De Cuyper, Konsa, Justin; Rogers, Groß, Cherki, Cunha; Haaland, Thiago, Evanilson.
Bench: Sels > McGinn > Mitchell > N.Williams (arm, 75%). C Haaland, VC Rogers.
Cherki (P(appear) 0.55, 49 min) and Cunha (0.68, 61 min) hold the last two midfield places over McGinn (0.80, 3.32)
by 0.5 and 0.0 points; Friday's team news decides those two, and Saturday's final refresh re-picks the XI.

**Hold instead (no transfer), GW9 XI forecast 55.2:** Donnarumma; De Cuyper, Konsa, Justin; Rogers, Groß, Cherki,
Cunha, McGinn; Haaland, Evanilson; bench Sels > Mitchell > N.Williams > João Pedro.

**Classic vs classic + SFT.** The H5 shadow read (the sheet with the text behind each move) needs a ~10-minute GPU
read on Saturday's final snapshot; the final refresh (`scripts/run_gw9_final_refresh.sh`, armed, fires Sat 02:15 PDT)
runs it only if `logs/gw9_gpu_ok` exists. Without it the sheet shows classic only.

**Why Calafiori looked so strong until GW8 (Wes's question).** The minutes and appearance heads are current-season-only
by design (the 2026-09-01 constraint: blend quality, not availability, so injured players re-rank instantly on
return), so seven straight starts read as 90 minutes / P(appear) 1.00 and his GW8 forecast was the top defender (5.5),
whatever the 22-of-38 and 11-of-38 start records of the two previous seasons said. The population test
(`minutes_prior_study.md`, 16,546 nailed-looking player-weeks) says this is NOT a systematic error: players who look
nailed now but had a low prior-season start share deliver exactly what the forecast says (excess +0.03 ± 0.09 points,
the Calafiori profile +0.01 ± 0.09; defenders alone −0.17 ± 0.15, borderline). The one real gap is players with no
Premier League season behind them (new signings, promoted squads): −0.23 ± 0.09 per week, defenders −0.35 ± 0.14,
weeks 1-10 −0.38 ± 0.20. That is the "fresh season" effect in the form the data supports, and it is being tested as a
ridge feature (F17, `reports/prior_f17/`). Hot starts beyond the 6-week prior ramp do not regress measurably
(−0.10 ± 0.22). What GW8 actually was: a late knock, invisible to everyone before the deadline.

**Files:** `README.md` (packet summary), `decide.log`, `milp.log`, `route_lineups.log`, `role_override_sheet.md`
(no squad player in the Konsa cell this week), `minutes_prior_study.md`.

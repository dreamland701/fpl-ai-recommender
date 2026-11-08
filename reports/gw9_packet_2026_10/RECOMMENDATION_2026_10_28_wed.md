# GW9 recommendation (Wednesday, 2026-10-28 15:50 PDT; deadline Sat 2026-10-31 04:00 PDT = 11:00 UTC)

Built from the 15:35 PDT rebuild of `wed/` (snapshot 2026-10-28T22:35Z, entry 6535607: bank £1.7m, 1 free transfer,
no GW9 transfers made, chips left Bench Boost / Free Hit / Wildcard). Classic + F6 on the fixed pipeline decides;
out/suspended players with no stated chance of at least 25% are zeroed in the sheet and the optimizer.

**Do:** **João Pedro → Thiago** (Brentford, £7.8m; BRE v NFO Sat 15:00 UTC), the free transfer, bank £1.6m after.
Captain **Haaland** (MCI v BHA Sat 15:00, GW9 8.28), vice **Rogers** (CHE v MUN Sat 12:30, 5.55). No chip.
**N.Jackson** (Aston Villa, £6.8m; AVL v FUL Sat 20:00) is the equal pick: level over five weeks, ahead for GW9 alone,
£1.0m cheaper. Either is right by the model; Thiago is the five-week optimum by 0.1 and the Tuesday pick, so it stays.

## Routes (GW9-13 value vs holding 273.9, net of hits; exact optimizer)

| route | GW9-13 | GW9 XI (hold 55.5) | hit | bank after |
|---|---|---|---|---|
| João Pedro → Thiago (free) | **+7.2** | 56.9 | 0 | 1.6 |
| João Pedro → N.Jackson (free) | +7.1 | 57.3 | 0 | 2.6 |
| João Pedro → Isak (free; Isak as forecast, P 0.72) | +6.0 | 56.1 | 0 | 0.3 |
| João Pedro + Cunha → Isak + Tavernier | +7.2 | — | −4 | 1.7 |
| João Pedro + Cunha + Donnarumma → Isak + Tavernier + Raya | +10.1 | — | −8 | 1.0 |
| João Pedro + Donnarumma → N.Jackson + Raya | +10.0 | — | −4 | 1.9 |
| Cunha + N.Williams → Gabriel + Tavernier (João Pedro stays, injured, 4th sub) | +11.2 | 59.0 | −4 | 0.2 |
| Cunha + João Pedro + N.Williams → Gabriel + Tavernier + Thiago | +14.4 | — | −8 | 0.1 |
| Konsa → Calafiori (free; hip, 75%) | ≈ 0 (XI 55.3 vs 55.5) | 55.3 | 0 | 0.3 |
| Wildcard (GW9-13, projected) | +35.8 | — | — | 0.0 |
| Free Hit (GW9 only, projected) | +8.9 | — | — | 0.0 |

Reading the hit routes: every −4 route gains 1-4 points over the free move over five weeks, inside the noise of a
two-player comparison; past two-transfer options have realised at ~85% of projection and wildcards at ~0 (chip
calibration note), so none earns its hit. Keep the chips.

## The Isak question (is a second move needed for funds or value?)

- **Funds: no.** João Pedro sells at £7.7m, bank £1.7m, Isak costs £9.1m (up £0.1m since Tuesday): the swap is
  affordable alone with £0.3m left.
- **Value: no.** The best Isak-with-a-second-move routes are +7.2 (−4) and +10.1 (−8) against +6.0 for the plain swap;
  the extra 1-4 points over five weeks do not cover a hit with any confidence. The second moves (Cunha → Tavernier,
  Donnarumma → Raya) are worth doing as later free transfers whichever striker comes in.
- **Isak vs Thiago/Jackson.** As forecast Isak is GW9 3.89 / GW9-13 20.3 / 65 min / P(appear) 0.72 (the GW6 blank still
  sits in his rolling minutes). If that blank is treated as a normal 78-minute game (`returner_counterfactual.py Isak 6 78`
  on this snapshot) he reads 4.17 / 21.5 / 73 min / P 0.81, level with Thiago (4.69 / 21.5) and Jackson (5.03 / 21.4)
  over five weeks and ~0.5-0.9 behind for GW9. So: Isak if you believe he is fully fit is a coin flip with the other
  two on five-week value and costs £1.3-2.3m more; by the model's own read Thiago is ahead by ~1.2 over five weeks.

## Lineup (João Pedro → Thiago), GW9 XI forecast 56.9 including the captain

Donnarumma; De Cuyper, Konsa, Justin; Rogers, Groß, Cherki, McGinn; Haaland, Thiago, Evanilson.
Bench: Sels > Cunha > Mitchell > N.Williams (arm, 75%). C Haaland, VC Rogers.
McGinn (3.34, P 0.80, 72 min) holds the last midfield place over Cunha (3.27, P 0.67, 60 min) by 0.07; Cherki (3.73,
P 0.54, 49 min) stays in on points. Friday's Guardian team news and Saturday's 02:15 PDT refresh re-pick these three.
With N.Jackson instead of Thiago the XI is the same with Jackson in Thiago's slot (57.3).

**Hold instead (no transfer), GW9 XI forecast 55.5:** Donnarumma; De Cuyper, Konsa, Justin; Rogers, Groß, Cherki,
McGinn, Cunha; Haaland, Evanilson; bench Sels > Mitchell > N.Williams > João Pedro.

## What moved since Tuesday's interim

| | Tuesday | Wednesday 15:35 | why |
|---|---|---|---|
| João Pedro | i, thigh, 0% (raw 3.57 / 18.7) | unchanged flag; raw 2.46 / 15.1, price 7.9 → 7.8 | 1.07M transfers out; zeroed either way |
| N.Jackson | 4.37 / 19.3, £6.7m | 5.03 / 21.4, £6.8m | transfers in 526k → 916k, ownership 9.3 → 13.0%: the crowd term, not new football |
| Isak | 3.61 / 19.4, £9.0m | 3.89 / 20.3, £9.1m | same mechanism (357k in) |
| Evanilson | 4.32 / 19.8 | 4.56 / 20.6 | same (332k in) |
| Tavernier | 4.58 / 21.2 | 4.80 / 22.0 | same (653k in) |
| Thiago | 4.66 / 21.4 | 4.69 / 21.5 | flat |
| Calafiori | d, hip, 75%: 3.31 / 17.6 | d, hip, 75%: 3.15 / 17.1 | 326k out; Konsa → Calafiori stays dead |
| Haaland | 8.21 / 41.1, £15.7m | 8.28 / 41.2, £15.8m | price rise |
| Squad flags | João Pedro i/0%, N.Williams d/75% | same; no new flags | |
| XI vs interim | Cunha in, McGinn bench | McGinn in, Cunha bench (0.07 apart) | |

No status changed in the squad or among the targets since Tuesday; every forecast move above is price/ownership/
transfer momentum, which the model carries as features (live-parity fixed 2026-10-04). The free-transfer route and its
gain are unchanged (+7.2); Jackson closed from ≈+5 to +7.1 on that momentum.

## Classic vs classic + SFT

The H5 shadow read needs a ~10-minute GPU read on Saturday's final snapshot; the armed final refresh
(`scripts/run_gw9_final_refresh.sh`, pid in `logs/pids/gw9_final_refresh.pid`, fires Sat 02:15 PDT) runs it only if
`logs/gw9_gpu_ok` exists. The F16 shadow sheet (classic+F6 vs classic+F6+Guardian lineups) is built by the same refresh
once Friday's predicted-lineups article is in the store. Without the GPU flag the side-by-side shows classic only.

**Files:** `wed/README.md`, `wed/decide.log`, `wed/milp.log`, `wed/forced_routes.log` (Isak-forced routes),
`wed/route_lineups.log`, `wed/role_override_sheet_isak.md` (Konsa override +0.3 GW only; XI unchanged),
`wed/role_override_sheet.md` (Konsa → Calafiori, no override), Jackson-forced routes in the session scratchpad
(`gw9_wed_jackson/forced_routes.json`).

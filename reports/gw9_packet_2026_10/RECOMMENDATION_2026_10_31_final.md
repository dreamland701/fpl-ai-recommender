# GW9 recommendation (FINAL, Saturday 2026-10-31 03:05 PDT; deadline 04:00 PDT = 11:00 UTC)

Built from the 02:15 PDT refresh of `final/` (snapshot 2026-10-31T09:15Z). The public API still shows the pre-transfer
squad (João Pedro, bank £1.7m, 1 FT) because current-GW transfers are hidden until the deadline; Wes's confirmed
João Pedro → Isak (£9.1m) was applied by hand at 02:55 PDT exactly as on Thursday (bank £0.3m, 0 FT; `final/build.log`),
and the squad-dependent steps were replayed on CPU (API-state outputs kept as `final/*_api.*`). Classic + F6 on the
fixed pipeline decides; the H5 shadow read (GPU, 669 rows, 9.8 min) and the F16 Guardian-lineup shadow are logged alongside.

**Do:** **no transfer, no chip.** 0 free transfers: every move costs 4 and none earns it.
XI **Donnarumma; De Cuyper, Konsa, N.Williams; Rogers, Groß, Cherki, McGinn; Haaland, Evanilson, Isak.**
Bench **Sels > Justin > Cunha > Mitchell.** Captain **Haaland** (MCI v BHA Sat 15:00Z, GW9 8.38), vice **Rogers**
(CHE v MUN Sat 12:30Z, 5.71). GW9 XI forecast 57.7 including the captain (Thursday 56.3); hold EV GW9-13 285.3 (281.2).

Same XI as Thursday. The one change is the bench order: Justin (3.24) is now ahead of Cunha (3.22; Thursday 3.27), so
Justin is the first auto-sub. That matters because Cherki stays in the XI at P(appear) 0.51 / 46 min (3.54 v Justin 3.24):
if he does not appear, Justin comes in for a legal 4-3-3; if he plays, the XI keeps the higher-upside pick. The Guardian
lists Cherki in City's XI and the H5 adapter reads him at 0.76.

## Routes (GW9-13 value vs holding 285.3, net of hits; exact optimizer + decision sheet)

| route | GW9-13 now | if rolled a week | GW9 XI (hold 57.7) | hit | bank after |
|---|---|---|---|---|---|
| Hold | 0 | — | 57.7 | 0 | 0.3 |
| Cunha → Tavernier | +4.6 | +6.0 | 60.1 | −4 | 1.6 |
| Donnarumma + Cunha → Raya + Tavernier | +7.6 | +7.5 | 61.5 | −8 | 0.9 |
| Mitchell + Cunha + Isak → Gabriel + Tavernier + N.Jackson | +11.9 | +8.8 | — | −12 | 0.3 |
| Wildcard (GW9-13) | +38.5 projected (exact), +5.6 on the decision sheet | — | — | — | 0.1 |
| Free Hit (GW9 only) | +10.7 projected (XI 70.8), +5.8 on the decision sheet | — | — | — | 0.0 |

Reading: Cunha → Tavernier is worth more as next week's free transfer (+6.0) than as a hit now (+4.6), so roll. The two-
and three-move routes add 3-7 points over five weeks over their free versions, inside the noise of a two-player
comparison; two-transfer options have realised at ~85% of projection and wildcards at ~0 (chip calibration). The GW8
"Konsa → Calafiori" route is dead twice over (0 FT; Calafiori still d/75%, hip).

## Guardian predicted lineups (published Fri 2026-10-30 16:19Z, 18.7 h before the deadline)

All 14 fit squad players are listed in their clubs' XIs (João Pedro: injured). Nobody in the squad is sub, doubtful or
out. Among the top-150 forecasts the article benches Gvardiol, Gray, Barnes, Hume, Tielemans and Buendía; none is ours.
The F16 shadow forecast (classic+F6+Guardian categories, not deciding) would swap Cunha (3.34) in for Justin (3.29): the
"XI" tag lifts Cunha's P(appear) 0.66 → 0.70, still a coin flip, and the production model keeps Justin ahead because
Cunha's 60-minute rotation history is real (United's 12:30Z kickoff is also the first of the round, so a late surprise
there costs nothing: he is the third sub).

## Status check vs Thursday

No squad flag moved: all 15 are 'a' (N.Williams, Isak, Konsa, Haaland a/100%). League-wide, 29 status/news lines
changed overnight, none in the squad or among live targets: Madueke 75 → 50%, Szoboszlai out → d/50%, Branthwaite
d/75% (concussion), Mainoo d/25%, Osula d/50%, Mukiele d/75%; Tosin, Lacroix, Hato, Anselmino, Carvalho out; Grealish,
Smith Rowe, Maddison, Mykolenko, Affengruber, Matheus N. cleared; Udogie back. Calafiori d/75% and Timber d/75% unchanged.
Fixtures as published: CHE v MUN Sat 12:30Z; BOU v LEE, BRE v NFO, COV v SUN, HUL v IPS, MCI v BHA 15:00Z; TOT v CRY
17:30Z; AVL v FUL 20:00Z; LIV v ARS Sun 16:30Z; NEW v EVE Mon 20:00Z. No postponements.

## What moved since Thursday (all price / ownership / transfer momentum, no new football)

| Player | Thursday (GW9 / GW9-13, P, min) | Final | why |
|---|---|---|---|
| Evanilson | 4.66 / 20.9, 0.97, 87 | 5.44 / 23.4, 1.00, 90, price 6.3 | ownership 9.7 → 14.1% |
| Isak | 3.95 / 20.5, 0.73, 66 | 4.34 / 21.8, 0.79, 71 | ownership 17.4 → 19.8%, GW7-8 minutes rolling in |
| Rogers | 5.55 / 25.4 | 5.71 / 25.9, price 8.1 | price rise, 50.2 → 50.8% |
| Konsa | 3.39 / 16.3 | 3.50 / 16.7 | 20.4 → 21.1% |
| Haaland | 8.28 / 41.3 | 8.38 / 41.6 | 78.3 → 78.9% |
| Cherki | 3.71 / 19.0, 0.54, 48 | 3.54 / 18.4, 0.51, 46 | 38.1 → 37.0% (sells) |
| Groß | 4.79 / 24.3 | 4.69 / 24.0 | 46.1 → 45.5% |
| Cunha | 3.27 / 16.8, 0.67, 60 | 3.22 / 16.6, 0.66, 60 | 6.0 → 5.7% |
| N.Williams | 3.30 / 16.0 | 3.28 / 15.9 | flat |
| Justin | 3.24 / 15.1 | 3.24 / 15.1 | unchanged |

N.Williams v Justin stays a coin flip (+0.04 classic; the SFT has it −0.04 the other way); classic decides, so N.Williams
starts as on Thursday. Role override `--auto`: Konsa only (six straight starts since GW3), 3.50 → 3.80 GW / 16.7 → 18.6
GW9-13 if nailed; XI unchanged (57.7 → 57.9).

## Classic vs classic + SFT (H5 shadow, `final/side_by_side_h5.md`)

| | Classic | Classic + H5 |
|---|---|---|
| XI | Donnarumma; De Cuyper, Konsa, N.Williams; Rogers, Groß, Cherki, McGinn; Haaland, Evanilson, Isak | same, with Justin for N.Williams |
| Bench | Sels, Justin, Cunha, Mitchell | Sels, Cunha, N.Williams, Mitchell |
| C / VC | Haaland / Rogers | Haaland / Rogers |
| GW9 XI | 57.7 | 57.5 |

The adapter's generic rule this week is delta = +0.099 × classic − 0.308 (−0.11 for a 2-point player, +0.48 for an
8-point one); every player-specific remainder in the squad is within ±0.25 (De Cuyper −0.23, Rogers −0.21, Haaland
−0.55 against a +0.52 generic lift, net −0.03). Its availability read is high everywhere — Cherki 0.51 → 0.76,
Cunha 0.66 → 0.91, Isak 0.79 → 0.96, McGinn 0.81 → 0.96 — consistent with the Guardian XIs in its team-sheet block.
The text it singled out is match-report filler: Cherki replaced at half-time in Villa 2-1 City and the Scout's "transfer
curse" note; McGinn "outstanding" in the same game; Isak's form pieces; for Cunha two name matches to other players
(Como's Da Cunha). Nothing in it changes a pick. The one SFT difference (Justin for N.Williams) is a −0.04 coin flip.

## Chips

Planner rule: **none**. Bench Boost would be +11.8 now (Sels 2.5, Justin 3.2, Cunha 3.2, Mitchell 2.9), the best of the
next five weeks on today's forecasts (+10.9 best in GW10-13), but a 12-point bench is below the planner's bar; the
chip-timing study found BB without a double or a wildcard-built bench ≈ coin flip. Wildcard +38.5 projected realises at
~0 historically. **Planning item from GW10:** Bench Boost, Free Hit and Wildcard all expire after GW19 and no double or
blank is published this half, so three chips have ten gameweeks; the natural shape is a Wildcard around the GW11
international break, Bench Boost on the rebuilt bench, Free Hit for one of the congested rounds (GW13-14, GW18-19).

## Training

H6b (last knob on the SFT points recipe: 2 epochs, LoRA LR 1e-4, head LR 2e-3) started on its own at 02:32:43 PDT,
30 s after the refresh exited; step 1 at 02:35:13, 63.2 s/step, 1,680 steps, peak 17.3 GB. Training ends ~07:45 PDT
Sunday, scoring + backtests ~1.5 h, verdict ~10:00 PDT Sunday (`logs/train_h6b.log`, chain `logs/h6b_after_gw9.log`,
sentinel "H6B CHAIN DONE" / "H6B FAILED"). GW9 is settled with `scripts/gw_status.py --event 9` first, then the ledger row.

**Files:** `final/README.md`, `final/build.log` (hand-edit), `final/decide.log`, `final/milp.log`, `final/route_lineups.log`,
`final/role_override_sheet.md`, `final/f16_shadow.md` (Guardian lineups), `final/side_by_side_h5.md`, `reports/chip_line_gw9.md`;
pre-hand-edit versions `final/*_api.*`; forecasts `final/forecasts_new_pipeline.jsonl`, `final/forecasts_f16_shadow.jsonl`,
H5 read `reports/h_series/h5_gw9final_pred.jsonl`.

# GW8 final recommendation (2026-10-23 07:50 PDT; deadline 10:30 PDT / 17:30 UTC)

**Snapshot.** Final refresh ran 07:00-07:05 PDT into `final/` (sentinel in `logs/gw8_final_refresh.log`; the G8 chip
shadow line failed on a filename, nothing else). Live feed re-read 07:44 PDT: no status change since the snapshot.
Saka: status i, 0% chance, "Thigh injury - Unknown return date" (Arteta on Wednesday: quad, "doesn't look good at
all"; no scan result in the Guardian or Scout stores by 14:00 UTC). Everyone else in the squad: available, no news.
Haaland fit after resting on the bench at AEK (PA, Friday). Evanilson "hurt himself making the challenge" at Milan on
Thursday but finished the game and carries no flag. Cherki started and scored at AEK on Tuesday (0 min in GW7).
Cunha started at Como on Wednesday and was taken off at half-time in the 4-1 (tactical reshuffle; 6-min cameo in GW7).

**Decision source.** The classic model still prices Saka at P(appear) 0.67 (GW8 4.00, GW8-12 20.7) on the 0% flag,
so the feed-as-is sheet would only move Cunha → Rogers (+9.8). The decision again comes from the Saka-out scenario
(`final_saka_out/`: Saka's p1/p3/p5/P(appear)/minutes zeroed, decide/milp/route_lineups re-run).

**Do:** Saka → Rogers (free; selling 9.6, buying 8.0, bank after 1.7). Captain Haaland, vice Rogers. No chip.

| route (GW8-12 value vs hold, net of hits) | gain | bank after |
|---|---|---|
| Saka → Rogers (free) | +13.2 (GW8 alone +3.1) | 1.7 |
| Konsa + Saka → Calafiori + Rogers (−4) | +18.0 | 0.2 |
| Donnarumma + Saka + N.Williams → Raya + Rogers + Calafiori (−8) | +20.5 | 0.1 |
| Wildcard (GW8-12), exact MILP | +48.0 | 0.1 |
| Free Hit (GW8 only) | +11.9 | 0.0 |

The −4 double adds +4.8 over five weeks for Konsa → Calafiori, inside the noise of a two-player comparison; it is
GW9's free move instead. The wildcard projection is large on paper but wildcard projections have not realised in the
past (+16.8 projected → −0.7 realised over 14 windows, chip-calibration note), and the squad it drafts leans on
one-week form; no chip.

## Lineup after Saka → Rogers (same fitted classic model, three readings)

| | Classic (standard) | Classic, Konsa re-forecast as nailed (`final/role_override_sheet.md`) | Classic + SFT H1 (Wednesday's read, `interim_1021/side_by_side_h1_saka_rogers.md`) |
|---|---|---|---|
| GK | Donnarumma | Donnarumma | Donnarumma |
| DEF | De Cuyper, Justin, Mitchell, N.Williams | De Cuyper, Justin, **Konsa**, Mitchell | De Cuyper, Justin, Mitchell, N.Williams |
| MID | Rogers, Groß, Cherki | Rogers, Groß, Cherki | Rogers, Groß, **Cunha** |
| FWD | Haaland (C), João Pedro, Evanilson | Haaland (C), João Pedro, Evanilson | Haaland (C), João Pedro, Evanilson |
| bench | Sels > Konsa > Cunha > McGinn | Sels > N.Williams > Cunha > McGinn | Sels > Cherki > Konsa > McGinn |
| expected GW8 pts | 57.9 | 58.1 | 54.1 (its own forecasts) |

Marginal calls (all inside 0.2 of a point):

- Konsa 3.31 (P(appear) 0.82, 74 min) vs N.Williams 3.35 (0.85, 77 min) standard; Konsa 3.55 (0.90, 81 min) if nailed.
  Konsa has started five straight league games plus the full game at Bayern; Arsenal home to Everton (Sat 15:00
  UK) vs Forest away at Ipswich (Fri 20:00 UK). Wes chose Konsa on Wednesday; nothing since argues against it.
- Cherki 3.49 (P(appear) 0.41, per-90 8.4) vs Cunha 3.28 (0.56, per-90 5.8). Cherki started and scored on Tuesday;
  Cunha was hooked at half-time on Wednesday. Wednesday's H1 read preferred Cunha (P(appear) 0.81 vs 0.65) on text
  that is now a week stale. Coin flip; the model order is Cherki.
- Vice: Rogers 6.08 (Chelsea v Spurs, Sat 17:30 UK) over João Pedro 5.73.

**Fixtures.** Fri IPS v NFO (Sels, N.Williams); Sat AVL v MCI (McGinn; Donnarumma, Cherki, Haaland), ARS v EVE
(Konsa), CHE v TOT (Rogers, João Pedro); Sun LIV v BHA (De Cuyper, Groß), MUN v BOU (Cunha; Evanilson),
CRY v NEW (Mitchell), SUN v LEE (Justin).

**GPU note.** The 31B extraction backfill is running (288/2,291 docs at 07:38 PDT, ~45 s/doc, `logs/extract_backfill.log`);
the E4B H1 read on the final snapshot did not run (no `logs/gw8_gpu_ok`). Touching that flag pauses the backfill
for the H1 side-by-side; otherwise the Wednesday read stands.

# GW10 recommendation (interim, Wed 2026-11-04 22:30 PST; deadline Fri 2026-11-06 10:30 PST = 18:30 UTC)

Built on CPU from the 06:26Z snapshot (`reports/gw10_packet_2026_11/`, `README.md`), classic + F6 on the fixed pipeline, fitted on
every settled week through GW9 (cutoff 9, 196,914 training rows). The GPU is running the Gemma-4-12B capacity test (H12), so the
SFT (H5) shadow read and the classic-vs-SFT sheet are queued behind it (`scripts/run_gw10_interim_sft.sh`, Thursday afternoon);
Friday's final refresh (08:35 PST, `scripts/run_gw10_final_refresh.sh`) re-picks with the Guardian predicted lineups and a fresh H5 read.

**State (FPL API, matches the app bar the 0.1 rounding on five selling prices):** bank £0.3m, **1 free transfer**, chips left
Bench Boost, Free Hit, Wildcard (Triple Captain used GW8; all three expire after GW19). GW9 settled 49 vs average 47.
Fixtures: EVE v COV Fri 20:00Z; LEE v TOT Sat 12:30Z; ARS v HUL, FUL v NEW 15:00Z; NFO v MCI 17:30Z; BHA v BRE, CRY v LIV,
IPS v BOU, SUN v CHE Sun 14:00Z; MUN v AVL 16:30Z. Then the international break: GW11 deadline Sat 2026-11-21 11:00Z.

**Do (interim):** **Cunha → Rice** (Arsenal, £7.4m; ARS v HUL Sat 15:00Z), the free transfer. Bank after £0.7m.
Captain **Haaland** (MCI at NFO Sat 17:30Z, GW10 8.79), vice **Rogers** (CHE at SUN Sun 14:00Z, 6.34). No chip.

| route (GW10-14 value vs holding 285.7, net of hits) | gain now | if rolled a week | GW10 XI (hold 60.9) | hit | bank after |
|---|---|---|---|---|---|
| **Cunha → Rice (free)** | **+4.8** | +3.5 | 62.2 | 0 | 0.7 |
| Cherki → Rice (free) | ≈ +4 (GW10-only optimizer's pick, +1.3) | — | 62.2 | 0 | 0.7 |
| Donnarumma + Cunha → Raya + Rice | +8.5 | +9.4 (both free next week) | 64.0 | −4 | 0.0 |
| Donnarumma + N.Williams + Cunha → Raya + Calafiori + Rayan | +7.7 | +7.4 | — | −8 | 0.1 |
| Wildcard (GW10-14) | +28.8 projected (exact optimizer), −2.9 on the decision sheet | — | — | — | 0.0 |
| Free Hit (GW10 only) | +7.3 projected (exact), +1.1 on the sheet | — | — | — | 0.0 |

**Why Rice, why now.** Rice is the best midfielder the Cunha money reaches: GW10-14 22.0 (Cunha 17.1), P(appear) 0.97 and 87
minutes (Cunha 0.68 / 61: 6, 84, 45, 90, 65 minutes since GW7), GW10 4.84 vs 3.55 at home to Hull, then NEW away, MCI home, BRE and
TOT away; 1, 7, 9, 3, 8 points in GW5-9. Mbeumo (£7.9m, 21.2, P 0.94) is the next option. The move is worth +1.3 more now than next
week because of the Hull game. Rolling instead keeps two free transfers for after the break (two weeks of injury news) and makes the
pair Raya + Rice free in GW11 (+9.4); the model does not price that optionality, and the two-step version of the same plan — Rice
now, then **Donnarumma → Raya (£6.2m) free next week**, which the £0.7m left over makes affordable (£5.5m + £0.7m) — comes to
about +10.7 over the horizon, the best of the three. Raya's run (HUL, NEW, MCI, BRE, TOT) and 21.7 vs Donnarumma's 14.0 make it the
natural GW11 transfer; Verbruggen (£4.6m, 17.0) is the cheap alternative if the money is wanted elsewhere.

**Which midfielder goes.** The five-week optimizer sells Cunha, the single-week one sells Cherki (3.50 vs 3.55 this week): a coin
flip on paper (Cherki 17.8 vs Cunha 17.1 over GW10-14). Cherki's minutes are 0, 45, 35 since GW7 and the model has him at P(appear)
0.47 / 42 minutes for the trip to Forest; Cunha is 61 minutes a game in a United side at home to Villa. Keep Cherki for now on the
optimizer's number; Friday's Guardian lineups and the H5 read (its one proven strength is the P(appear) read) settle it, and if
City's press conference benches Cherki the final refresh swaps the sale.

**Lineup with Cunha → Rice, GW10 XI forecast 62.2 including the captain:**
Donnarumma; De Cuyper, Konsa, N.Williams; Rogers, Groß, Rice, Cherki; Haaland, Isak, Evanilson.
Bench: Sels > McGinn > Justin > Mitchell. C Haaland, VC Rogers.

**Hold instead (no transfer), GW10 XI 60.9:** Donnarumma; De Cuyper, Konsa, N.Williams; Rogers, Groß, Cunha, Cherki; Haaland, Isak,
Evanilson; bench Sels > McGinn > Justin > Mitchell. Hold EV GW10-14 285.7.

## Squad as the model sees it (no flags on any of the 15)

| Player | Club, GW10 | GW10 | GW10-14 | P(appear) / min | since GW9 final |
|---|---|---|---|---|---|
| Donnarumma | MCI @ NFO | 3.03 | 14.0 | 0.88 / 79 | 2.79 → 3.03 |
| Konsa | ARS v HUL | 4.24 | 18.1 | 0.93 / 83 | 3.50 → 4.24 (Hull at home; 9, 14, 10 pts in GW7-9) |
| N.Williams | NFO v MCI | 3.30 | 15.9 | 0.89 / 80 | flat |
| De Cuyper | BHA v BRE | 5.01 | 22.7 | 0.97 / 88 | 4.21 → 5.01 |
| Justin | LEE v TOT | 3.18 | 15.0 | 0.90 / 80 | flat |
| Mitchell | CRY v LIV | 3.00 | 13.8 | 0.91 / 82 | flat |
| Rogers | CHE @ SUN | 6.34 | 27.2 | 1.00 / 90 | 5.71 → 6.34 |
| Groß | BHA v BRE | 5.32 | 24.8 | 1.00 / 90 | 4.69 → 5.32 |
| Cherki | MCI @ NFO | 3.50 | 17.8 | 0.47 / 42 | P 0.51 → 0.47 (35 min in GW9) |
| Cunha | MUN v AVL | 3.55 | 17.1 | 0.68 / 61 | 3.22 → 3.55 |
| McGinn | AVL @ MUN | 3.36 | 16.0 | 0.82 / 74 | flat |
| Haaland | MCI @ NFO | 8.79 | 41.1 | 1.00 / 90 | 8.38 → 8.79 |
| Isak | LIV @ CRY | 4.70 | 21.7 | 0.74 / 67 | 4.34 → 4.70; P 0.79 → 0.74 |
| Evanilson | BOU @ IPS | 4.33 | 19.7 | 0.74 / 67 | 5.44 → 4.33; **P 1.00 → 0.74** |
| Sels | NFO v MCI | 2.42 | 11.9 | 0.84 / 76 | flat |

**Evanilson's drop is the model, not the data.** His rows are right (75 minutes and 9 points in GW9, status 'a', no flag). The
minutes head reacts to three straight substitutions (78, 86, 75 minutes), to the away game and to the transfer surge (227k → 961k
transfers in last week) and cuts him 90 → 67 minutes; a nailed starter subbed late realises ~80. He stays in the XI either way, and
no route turns on him; the H5 read gives its own P(appear) for him, Isak (GW6 blank still in the window) and Cherki on Thursday.
Role override `--auto` fires only for Isak (three straight starts since GW7) and makes him slightly worse (4.70 → 4.18); XI unchanged.

## Chips

None this week. Bench Boost would be +12.0 (Sels 2.4, McGinn 3.4, Justin 3.2, Mitchell 3.0), below the planner's bar; Free Hit
+7.3 projected; the exact wildcard squad projects +28.8 (Raya, Gabriel, Calafiori, De Cuyper, Van Hecke; Groß, Rogers, Palmer, Slater,
Hughes; Haaland, Evanilson, Thiago) and wildcards have realised at ~0 on average, though last week's MILP squad would have scored 79.
Planning item: GW10 is followed by the international break, so **GW11 (deadline Sat 21 Nov) is the wildcard week if one is to be
played this half** — two weeks to build it, and GW12 Fri 27 Nov, GW13 Tue 1 Dec, GW14 Sat 5 Dec are three rounds in nine days
(Free Hit cover). BB/FH/WC all expire after GW19; no double or blank published.

## Timeline

- Thu 07:07 PST: CPU re-pick (`thu/`) after the midweek European games; a note only if the call or a flag changes.
- Thu ~11:15 PST: H12 training ends (step 540/840 at 22:17 PST, 155.7 s/step); predictions + scoring → verdict ~13:30-14:00 PST;
  the H5 read for GW10 and the classic-vs-SFT sheet start automatically when the chain releases the GPU (~25 min).
- Fri 08:35 PST: final refresh — Guardian predicted lineups (published ~15:40-16:20Z the last two weeks), F16 shadow, fresh H5 read,
  hand-edit replay of any confirmed move (`logs/gw10_hand_edit`, OUT:IN per line); final recommendation ~09:40 PST; deadline 10:30 PST.

**Files:** `README.md`, `decide.log`, `milp.log`, `route_lineups.log`, `role_override_sheet.md`, `forecasts_new_pipeline.jsonl`,
`entry_state.json`, `snapshot/`; scripts `scripts/run_gw10_interim.sh`, `scripts/run_gw10_interim_sft.sh`, `scripts/run_gw10_final_refresh.sh`,
`scripts/apply_hand_edit.py`.

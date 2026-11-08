# GW10 final packet (fixed pipeline)

- **Snapshot:** 2026-11-06T16:35:02+00:00 UTC; deadline 2026-11-06T18:30:00Z.
- **Entry 6535607:** bank £0.7m, free transfers 0, chips used: 3xc. Transfers already made for GW10: none.
- **Selling prices vs the app values pasted 2026-10-04:** ['Konsa: computed 4.6 vs app 4.5', 'N.Williams: computed 4.9 vs app 5.0', 'Groß: computed 5.8 vs app 5.7', 'Cherki: computed 7.8 vs app 7.7', 'Evanilson: computed 6.2 vs app 6.0', 'Cunha: computed 7.8 vs app 7.9'].

## Squad and targets as the model sees them

| Player | Status | Chance | News | GW10 | GW10–14 | P(appear) | min |
|---|---|---|---|---|---|---|---|
| Donnarumma | a | -1.0 | — | 3.03 | 14.0 | 0.88 | 79 |
| Konsa | a | 100.0 | — | 4.21 | 18.0 | 0.92 | 83 |
| N.Williams | a | 100.0 | — | 3.27 | 15.8 | 0.89 | 80 |
| De Cuyper | a | -1.0 | — | 5.19 | 23.3 | 1.00 | 90 |
| McGinn | a | -1.0 | — | 3.36 | 16.0 | 0.82 | 74 |
| Groß | a | -1.0 | — | 5.35 | 24.9 | 1.00 | 90 |
| Rogers | a | -1.0 | — | 6.47 | 27.7 | 1.00 | 90 |
| Cherki | a | -1.0 | — | 3.27 | 17.1 | 0.43 | 39 |
| Haaland | a | 100.0 | — | 8.82 | 41.2 | 1.00 | 90 |
| Evanilson | a | -1.0 | — | 4.77 | 21.1 | 0.81 | 73 |
| Isak | a | 100.0 | — | 4.98 | 22.6 | 0.79 | 71 |
| Sels | a | -1.0 | — | 2.42 | 11.9 | 0.84 | 76 |
| Rice | a | 100.0 | — | 4.96 | 22.4 | 0.99 | 89 |
| Justin | a | -1.0 | — | 3.18 | 15.0 | 0.90 | 80 |
| Mitchell | a | -1.0 | — | 2.99 | 13.8 | 0.90 | 81 |
| Raya | a | -1.0 | — | 4.92 | 21.9 | 1.00 | 90 |
| Gabriel | a | -1.0 | — | 5.58 | 25.1 | 1.00 | 90 |
| Calafiori | a | 100.0 | — | 5.34 | 23.2 | 1.00 | 90 |
| Verbruggen | a | -1.0 | — | 3.63 | 17.2 | 1.00 | 90 |
| Mbeumo | a | -1.0 | — | 4.39 | 21.0 | 0.93 | 84 |
| Thiago | a | -1.0 | — | 4.04 | 21.4 | 0.99 | 90 |
| Tavernier | a | -1.0 | — | 4.45 | 20.1 | 0.75 | 68 |
| N.Jackson | a | -1.0 | — | 3.37 | 16.5 | 0.56 | 51 |
| Rayan | a | -1.0 | — | 4.28 | 18.2 | 0.87 | 78 |
| Van Hecke | a | 100.0 | — | 4.16 | 19.7 | 0.93 | 84 |
| Saka | i | 0.0 | Thigh injury - Unknown return date | 2.32 | 13.4 | 0.28 | 25 |

## What moved since the interim packet

| Player | Status now | News now | GW10 (interim → now) | GW10–14 (interim → now) |
|---|---|---|---|---|
| De Cuyper | a | — | 5.01 → 5.19 | 22.7 → 23.3 |
| Cherki | a | — | 3.50 → 3.27 | 17.8 → 17.1 |
| Evanilson | a | — | 4.33 → 4.77 | 19.7 → 21.1 |
| Isak | a | — | 4.70 → 4.98 | 21.7 → 22.6 |
| Tavernier | a | — | 4.13 → 4.45 | 19.1 → 20.1 |
| N.Jackson | a | — | 3.14 → 3.37 | 15.8 → 16.5 |
| Van Hecke | a | — | 3.96 → 4.16 | 19.0 → 19.7 |

## Exact optimizer (GW10–14 value vs holding, net of hits)

| Route | Gain | Hit | Bank after | Captain |
|---|---|---|---|---|
| GW10-14, max 1: Donnarumma → Raya | +3.9 | 4 | 0.0 | Haaland |
| GW10-14, max 2: Donnarumma → Raya | +3.9 | 4 | 0.0 | Haaland |
| GW10-14, max 3: Donnarumma → Raya | +3.9 | 4 | 0.0 | Haaland |
| GW10-14 wildcard | +25.2 | — | 0.0 | Haaland |
| GW10 only, max 1: hold → — | +0.0 | 0 | 0.7 | Haaland |
| GW10 only, max 2: hold → — | +0.0 | 0 | 0.7 | Haaland |
| GW10 only, max 3: hold → — | +0.0 | 0 | 0.7 | Haaland |
| GW10 only free hit | +6.2 | — | -0.0 | Haaland |

## Enumerated routes (decision sheet, GW10–14 gain vs holding, net of hits)

| Option | Gain now | If rolled | Bank after |
|---|---|---|---|
| Donnarumma → Raya | +3.9 | +6.0 | 0.0 |
| Donnarumma + Cherki → Raya + Tavernier | +3.0 | +4.1 | 1.2 |
| Donnarumma + Cherki + Mitchell → Raya + Tavernier + Van Hecke | +3.0 | +3.1 | 0.7 |
| Wildcard (GW10-14) | -5.1 | — | 0.4 |
| Free Hit (GW10 only) | +0.8 | — | 0.6 |

Hold: XI Donnarumma, De Cuyper, Konsa, N.Williams, Rogers, Groß, Rice, McGinn, Haaland, Isak, Evanilson; bench Sels > Cherki > Justin > Mitchell; captain Haaland, vice Rogers.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 0.7): XI Donnarumma, De Cuyper, Konsa, N.Williams, Rogers, Groß, Rice, McGinn, Haaland, Isak, Evanilson; bench Sels > Cherki > Justin > Mitchell; C Haaland, VC Rogers; GW10 XI forecast 63.2 before hits.
- **Donnarumma -> Raya (GW10-14, max 1 moves, hit 4)** (bank after 0.0): XI Raya, De Cuyper, Konsa, N.Williams, Rogers, Groß, Rice, McGinn, Haaland, Isak, Evanilson; bench Sels > Cherki > Justin > Mitchell; C Haaland, VC Rogers; GW10 XI forecast 65.1 before hits.
- **Donnarumma -> Raya (GW10-14, max 2 moves, hit 4)** (bank after 0.0): XI Raya, De Cuyper, Konsa, N.Williams, Rogers, Groß, Rice, McGinn, Haaland, Isak, Evanilson; bench Sels > Cherki > Justin > Mitchell; C Haaland, VC Rogers; GW10 XI forecast 65.1 before hits.

## Role-override sheet (new signings / role changes the ridge cannot see)

See [role_override_sheet.md](role_override_sheet.md).

## Classic vs classic + SFT (H5), with the text behind each move

See [side_by_side_h5.md](side_by_side_h5.md).

## F16 Guardian-lineup shadow (classic+F6+F16, not deciding)

See [f16_shadow.md](f16_shadow.md).

Classic + F6 on the fixed pipeline makes the decision; the SFT arm is logged in shadow. See ../README.md for how to read the route gains and their uncertainty.

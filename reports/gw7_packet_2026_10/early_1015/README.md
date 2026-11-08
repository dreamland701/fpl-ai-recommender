# GW7 final packet (fixed pipeline)

- **Snapshot:** 2026-10-15T02:28:59+00:00 UTC; deadline 2026-10-17T10:00:00Z.
- **Entry 6535607:** bank £0.3m, free transfers 1, chips used: none. Transfers already made for GW7: none.
- **Selling prices vs the 10-04 app values:** ['Cherki: computed 7.8 vs app 7.7', 'João Pedro: computed 7.7 vs app 7.6', 'Isak: computed 9.0 vs app 9.1'].

## What moved since 2026-10-04

| Player | Status now | News now | GW7 (10-04 → now) | GW7–11 (10-04 → now) |
|---|---|---|---|---|
| Groß | a | — | 4.93 → 4.99 | 21.7 → 22.3 |
| Isak | i | Thigh injury - Unknown return date | 1.61 → 1.65 | 10.5 → 12.4 |

## Options (GW7–11 gain vs holding, net of hits; route scorer from the 10-04 packet)

| Option | Gain now | If rolled to GW7 | Bank after |
|---|---|---|---|
| B.Fernandes + Isak → McGinn + Haaland | +15.6 | +13.1 | 0.2 |
| B.Fernandes + Cunha + Isak → Rogers + McGinn + Haaland | +17.5 | +13.5 | 0.2 |
| Cunha → Rogers | +5.9 | +4.4 | 0.3 |
| Saka + Konsa → Rogers + Calafiori | +7.3 | +8.4 | 0.5 |
| Donnarumma + N.Williams + Saka → Raya + Calafiori + Rogers | +7.4 | +7.7 | 0.4 |
| Wildcard (GW7-11) | +19.5 | — | 0.1 |
| Free Hit (GW7 only) | +5.9 | — | 0.0 |

Hold: XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, B.Fernandes, Groß, Saka, Cunha, João Pedro, Evanilson; bench Sels > N.Williams > Mitchell > Isak; captain Cherki, vice B.Fernandes.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 0.3): XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, B.Fernandes, Groß, Saka, Cunha, João Pedro, Evanilson; bench Sels > N.Williams > Mitchell > Isak; C Cherki, VC B.Fernandes; GW7 XI forecast 53.8 before hits.
- **Cunha -> Rogers (1 FT)** (bank after 0.3): XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, Rogers, B.Fernandes, Groß, Saka, João Pedro, Evanilson; bench Sels > N.Williams > Mitchell > Isak; C Cherki, VC Rogers; GW7 XI forecast 55.4 before hits.
- **Bruno + Isak -> McGinn + Haaland (-4)** (bank after 0.2): XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, Groß, Saka, Cunha, Haaland, João Pedro, Evanilson; bench Sels > McGinn > N.Williams > Mitchell; C Haaland, VC Cherki; GW7 XI forecast 60.0 before hits.
- **Bruno + Cunha + Isak -> Rogers + McGinn + Haaland (-8)** (bank after 0.2): XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, Rogers, Groß, Saka, Haaland, João Pedro, Evanilson; bench Sels > McGinn > N.Williams > Mitchell; C Haaland, VC Cherki; GW7 XI forecast 61.5 before hits.
- **Isak -> Thiago (1 FT)** (bank after 1.5): XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, B.Fernandes, Groß, Saka, Cunha, João Pedro, Evanilson; bench Sels > Thiago > N.Williams > Mitchell; C Cherki, VC B.Fernandes; GW7 XI forecast 53.8 before hits.

## E20 holdout (2025-26 GW27–38, fixed pipeline)

- base decode FAILED (scoring skipped)
- scoring FAILED
- MAE:
- availability AUC among likely starters (promotion-rule metric): classic 0.549 vs E20 0.727 (n=2439)
- GW27-30: E20 225  classic+F6 266  -41
- GW31-34: E20 216  classic+F6 229  -13
- GW35-38: E20 263  classic+F6 258  +5
- TOTAL: E20 704  classic+F6 753  -49  windows won 1/3 (adapter noise sd ~24/window)

Classic + F6 on the fixed pipeline makes the decision; adapters are logged in shadow. See ../README.md for how to read the route gains and their uncertainty.

## Early refresh 2026-10-15 02:29 UTC (after the Tue/Wed Champions League round)

Exact optimizer (`squad_milp.optimize`, GW7–11 value, captain doubled, 0.1 x bench, hits −4), see `milp_transfers.json`:

| Transfers allowed | Move | Net gain GW7–11 | Net gain GW7 only | Bank after |
|---|---|---|---|---|
| 1 (free) | Cunha → Rogers | +5.9 | +1.5 | 0.3 |
| 2 (−4) | B.Fernandes + Isak → McGinn + Haaland | +15.6 | +2.4 (GW7-only optimum is Haaland + Tonali) | 0.2 |
| 3 (−8) | N.Williams + B.Fernandes + Isak → Calafiori + Slater + Haaland | +19.1 | +2.4 | 0.2 |
| 1, selling Isak | Isak → Thiago | +0.7 | +0.2 | 1.5 |

Press check (41 Guardian + 4 Scout articles, 10-13..10-15): Haaland 2 goals vs PSG (City lost 2–4, no injury
noted); Saka started on the bench vs Lille and scored after coming on at 65'; Cunha and Fernandes both played in the
0–2 at Atlético; Isak absent at Lask ("Thigh injury - Unknown return date" in the API). No status or news change on
any owned player or target since the 10-13 snapshot.

Price exposure (event transfer flow 10-13 → 10-15): Fernandes 306k out, Isak 293k out (already −0.1 this event),
Haaland 93k in, Rogers 275k in (already +0.1 this event), McGinn 38k in. The Haaland route has £0.2m to spare, so one
more Isak fall or a Haaland rise would break it at its current price.

# GW7 final packet (fixed pipeline)

- **Snapshot:** 2026-10-16T17:00:01+00:00 UTC; deadline 2026-10-17T10:00:00Z.
- **Entry 6535607:** bank £0.3m, free transfers 1, chips used: none. Transfers already made for GW7: none.
- **Selling prices vs the 10-04 app values:** ['Cherki: computed 7.8 vs app 7.7', 'João Pedro: computed 7.7 vs app 7.6', 'Isak: computed 9.0 vs app 9.1'].

## What moved since 2026-10-04

| Player | Status now | News now | GW7 (10-04 → now) | GW7–11 (10-04 → now) |
|---|---|---|---|---|
| De Cuyper | a | — | 4.57 → 4.79 | 19.6 → 20.7 |
| Groß | a | — | 4.93 → 5.27 | 21.7 → 23.2 |
| B.Fernandes | a | — | 5.32 → 5.26 | 29.2 → 28.6 |
| Cherki | a | — | 5.59 → 5.96 | 24.3 → 25.8 |
| João Pedro | a | — | 5.39 → 5.51 | 26.1 → 26.8 |
| Isak | d | Thigh injury - 25% chance of playing | 1.61 → 1.47 | 10.5 → 11.9 |
| De Cuyper | a | — | 4.57 → 4.79 | 19.6 → 20.7 |
| Rogers | a | — | 5.60 → 5.71 | 25.9 → 26.5 |

## Options (GW7–11 gain vs holding, net of hits; route scorer from the 10-04 packet)

| Option | Gain now | If rolled to GW7 | Bank after |
|---|---|---|---|
| B.Fernandes + Isak → McGinn + Haaland | +17.8 | +14.6 | 0.2 |
| B.Fernandes + Cunha + Isak → Rogers + McGinn + Haaland | +20.1 | +15.3 | 0.2 |
| Cunha → Rogers | +6.3 | +4.7 | 0.3 |
| Saka + Konsa → Rogers + Calafiori | +8.0 | +8.9 | 0.5 |
| Donnarumma + N.Williams + Saka → Raya + Calafiori + Rogers | +8.2 | +8.2 | 0.4 |
| Wildcard (GW7-11) | +19.7 | — | 0.1 |
| Free Hit (GW7 only) | +6.4 | — | 0.0 |

Hold: XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, Groß, B.Fernandes, Saka, Cunha, João Pedro, Evanilson; bench Sels > N.Williams > Mitchell > Isak; captain Cherki, vice João Pedro.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 0.3): XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, Groß, B.Fernandes, Saka, Cunha, João Pedro, Evanilson; bench Sels > N.Williams > Mitchell > Isak; C Cherki, VC João Pedro; GW7 XI forecast 55.1 before hits.
- **Bruno + Isak -> Haaland + Le Fée (-4)** (bank after -0.1): XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, Groß, Saka, Cunha, Haaland, João Pedro, Evanilson; bench Sels > E.Le Fée > N.Williams > Mitchell; C Haaland, VC Cherki; GW7 XI forecast 61.3 before hits.
- **Bruno + Isak -> Haaland + Xhaka (-4)** (bank after 0.2): XI Donnarumma, De Cuyper, Konsa, Justin, Cherki, Groß, Saka, Cunha, Haaland, João Pedro, Evanilson; bench Sels > Xhaka > N.Williams > Mitchell; C Haaland, VC Cherki; GW7 XI forecast 61.3 before hits.

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

## Exact optimizer on the final forecasts (2026-10-16 12:20 PDT; `milp_routes.py`, see `milp_transfers.json`)

| Transfers allowed | Move | Net gain GW7–11 | Net gain GW7 only | Bank after |
|---|---|---|---|---|
| 1 (free) | Cunha → Rogers | +6.3 | +1.6 | 0.3 |
| 2 (−4) | B.Fernandes + Isak → McGinn + Haaland, C Haaland | +17.8 | +2.5 (GW7-only optimum is Haaland + Tonali) | 0.2 |
| 3 (−8) | N.Williams + B.Fernandes + Isak → Calafiori + Slater + Haaland | +21.7 | +2.5 | 0.2 |
| wildcard (exact, GW7–11) | Raya, Calafiori, De Cuyper, Groß, Rogers, Palmer, João Pedro, Thomas, van Ewijk, Thomas-Asante, Dewsbury-Hall, Button, Cherki, Haaland, Van Hecke | +48.2 | — | 0.0 |

Unchanged from the early packet: the accepted route stays B.Fernandes + Isak → McGinn + Haaland (−4), which now
projects +17.8 (Isak is flagged "d", 25% chance). The third move adds +3.9 for another −4, inside the noise of a
five-week projection (two-transfer options realise ~85%; see `reports/transfer_calibration/summary.md`). Projected
wildcard gains have not realised historically (+16.8 → −0.7 over 14 windows), so no chip.

Lineup after the moves (classic): Donnarumma; De Cuyper, Konsa, Justin; Cherki, Groß, Saka, Cunha; Haaland, João
Pedro, Evanilson; bench Sels > McGinn > N.Williams > Mitchell; C Haaland, VC Cherki (Justin now edges N.Williams,
3.13 vs 2.96). H1 head shadow sheet on this corpus: `side_by_side_h1.md` (one near-tie swap, McGinn 3.70 for
Evanilson 3.69; P(appear) raised for every squad player, no out call).

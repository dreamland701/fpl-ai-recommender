# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW26
- Total predicted points: 1470.22
- Total actual points: 1418.00
- Average predicted points: 58.81
- Average actual points: 56.72
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Tijjani Reijnders
- Vice captain: Antoine Semenyo
- Effective captain: Tijjani Reijnders
- Chip used: none
- Predicted score: 73.40
- Actual score: 41.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 4.06 | 10.49 | 16.97 | 0.00 | 93.3 | 0.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.17 | 10.48 | 17.06 | 1.00 | 85.9 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.26 | 17.21 | 27.28 | 1.00 | 100.2 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.83 | 12.38 | 19.76 | 6.00 | 112.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.88 | 12.13 | 19.26 | 5.00 | 97.3 | 68.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.72 | 12.12 | 19.41 | 6.00 | 115.3 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.20 | 11.72 | 19.24 | 3.00 | 102.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.15 | 14.57 | 23.70 | 2.00 | 103.7 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.29 | 10.56 | 17.21 | 2.00 | 69.0 | 62.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 7.39 | 12.02 | 2.00 | 71.0 | 85.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 7.50 | 22.59 | 37.98 | 5.00 | 116.6 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 7.92 | 20.67 | 32.32 | 2.00 | 153.8 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.33 | 17.32 | 28.70 | 0.00 | 95.4 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.70 | 16.65 | 25.84 | 6.00 | 130.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.03 | 14.94 | 24.53 | 3.00 | 105.6 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.62
- Actual score: 49.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.78 | 7.90 | 13.00 | 8.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.32 | 4.04 | 7.00 | 0.00 | 36.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.77 | 13.34 | 20.85 | 6.00 | 84.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.05 | 10.63 | 17.61 | 8.00 | 76.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.62 | 10.21 | 16.71 | 1.00 | 73.9 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.06 | 9.99 | 16.34 | 2.00 | 72.3 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.23 | 6.84 | 11.85 | 0.00 | 17.4 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.92 | 16.82 | 25.71 | 2.00 | 92.9 | 72.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.54 | 7.74 | 12.88 | 2.00 | 48.6 | 64.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.33 | 7.26 | 11.86 | 6.00 | 64.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.97 | 22.35 | 37.38 | 3.00 | 106.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.18 | 15.85 | 24.47 | 2.00 | 94.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.89 | 15.62 | 25.49 | 10.00 | 85.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.59 | 15.54 | 24.38 | 2.00 | 95.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 12.27 | 18.96 | 2.00 | 69.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.50
- Actual score: 76.00
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 9.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.81 | 9.56 | 14.59 | 10.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 2.10 | 6.86 | 9.85 | 0.00 | 66.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.25 | 13.48 | 20.19 | 8.00 | 91.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.86 | 12.48 | 18.72 | 1.00 | 69.9 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.05 | 12.22 | 18.38 | 9.00 | 85.2 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.0 | 2.12 | 7.36 | 11.81 | 0.00 | 31.9 | 0.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.25 | 4.97 | 7.89 | 0.00 | 17.2 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.94 | 17.76 | 26.46 | 7.00 | 85.8 | 78.0 |
| XI | XI | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 8.99 | 13.35 | 2.00 | 72.6 | 85.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.26 | 7.98 | 12.20 | 0.00 | 51.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.04 | 23.79 | 37.44 | 9.00 | 104.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 6.13 | 17.71 | 25.52 | 13.00 | 90.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.77 | 14.63 | 23.32 | 2.00 | 70.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.02 | 12.90 | 19.41 | 3.00 | 66.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.66 | 11.88 | 18.07 | 3.00 | 73.5 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.55
- Actual score: 53.00
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 4.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.09 | 9.60 | 15.40 | 2.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.82 | 3.12 | 4.96 | 0.00 | 29.1 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.41 | 12.41 | 18.72 | 2.00 | 73.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.48 | 12.17 | 18.76 | 4.00 | 82.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.09 | 11.78 | 18.28 | 2.00 | 81.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.09 | 10.00 | 16.50 | 0.00 | 55.6 | 63.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.0 | 1.60 | 5.60 | 9.61 | 2.00 | 23.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.55 | 16.46 | 26.20 | 2.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Lyle Foster | FWD | 3 | 5.0 | 3.05 | 8.44 | 13.50 | 6.00 | 73.1 | 85.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.46 | 4.89 | 8.01 | 1.00 | 26.4 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.26 | 22.10 | 36.06 | 5.00 | 99.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.25 | 17.90 | 27.28 | 5.00 | 88.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.00 | 14.28 | 22.82 | 10.00 | 75.7 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.87 | 11.86 | 19.44 | 7.00 | 72.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.19 | 10.54 | 17.52 | 9.00 | 74.9 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.40 -> 1.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 62.52
- Actual score: 47.00
- Transfer: William Saliba -> Marcos Senesi Barón (projected gain 6.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.97 | 9.04 | 16.01 | 10.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.74 | 2.61 | 5.54 | 0.00 | 24.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.65 | 14.77 | 21.11 | 7.00 | 99.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.88 | 12.41 | 20.02 | 2.00 | 72.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.91 | 12.33 | 20.27 | 13.00 | 94.5 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 3.25 | 11.15 | 18.70 | 2.00 | 78.6 | 90.0 |
| Bench 2 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.23 | 9.32 | 16.84 | 0.00 | 59.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.02 | 16.70 | 28.05 | 2.00 | 94.4 | 90.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.80 | 8.26 | 14.66 | 2.00 | 77.9 | 79.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.27 | 4.97 | 9.77 | 0.00 | 24.8 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.70 | 19.27 | 33.76 | 2.00 | 82.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.4 | 6.33 | 18.33 | 28.73 | 7.00 | 98.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.41 | 17.17 | 28.02 | -1.00 | 90.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 5.56 | 14.98 | 24.05 | 2.00 | 105.1 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.46 | 14.36 | 24.10 | 2.00 | 86.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 1.60 -> 2.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 57.43
- Actual score: 75.00
- Transfer: Daniel Muñoz Mejía -> Marc Guéhi (projected gain 3.84, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.16 | 9.56 | 16.29 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.4 | 0.73 | 1.87 | 3.69 | 0.00 | 12.6 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.57 | 15.25 | 22.19 | 9.00 | 97.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.24 | 15.21 | 20.45 | 2.00 | 87.7 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.83 | 14.78 | 21.60 | 3.00 | 102.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.93 | 12.45 | 18.53 | 1.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.0 | 2.57 | 8.54 | 14.40 | 7.00 | 60.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.70 | 13.11 | 21.70 | 2.00 | 66.4 | 73.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.46 | 7.57 | 11.97 | 1.00 | 65.7 | 68.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 0.67 | 3.34 | 6.57 | 1.00 | 16.1 | 32.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.4 | 6.44 | 18.77 | 28.15 | 18.00 | 98.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.55 | 17.67 | 30.29 | 2.00 | 74.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.81 | 13.50 | 21.21 | 3.00 | 64.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.18 | 12.15 | 19.16 | 12.00 | 72.6 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.57 | 11.07 | 16.62 | 3.00 | 64.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 2.40 -> 0.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohammed Kudus
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.97
- Actual score: 56.00
- Transfer: Eliezer Mayenda Dossou -> Nick Woltemade (projected gain 3.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.23 | 9.00 | 14.99 | 7.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.4 | 0.34 | 1.25 | 2.74 | 0.00 | 10.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.35 | 15.84 | 22.61 | 12.00 | 91.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.37 | 14.27 | 20.21 | 2.00 | 78.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.75 | 11.62 | 21.63 | 4.00 | 94.7 | 90.0 |
| Bench 3 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.70 | 10.25 | 17.24 | 8.00 | 78.2 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 3.78 | 9.69 | 17.86 | 3.00 | 85.2 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.3 | 4.97 | 13.41 | 21.53 | 8.00 | 88.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.51 | 12.52 | 22.54 | 2.00 | 75.9 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.51 | 5.95 | 12.04 | 0.00 | 56.9 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.5 | 7.41 | 20.46 | 32.91 | 4.00 | 119.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.48 | 17.13 | 29.34 | 2.00 | 73.2 | 84.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.70 | 15.97 | 23.92 | 2.00 | 101.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 3.89 | 14.20 | 20.99 | 8.00 | 66.4 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.89 | 10.49 | 18.19 | 1.00 | 71.3 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 59.95
- Actual score: 46.00
- Transfer: Tijjani Reijnders -> Moisés Caicedo Corozo (projected gain 0.06, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.87 | 8.73 | 14.80 | 4.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.4 | 0.23 | 1.04 | 2.40 | 0.00 | 8.9 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.70 | 16.31 | 24.78 | 9.00 | 96.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.05 | 14.78 | 21.38 | 5.00 | 93.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.27 | 13.51 | 21.88 | 4.00 | 93.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.51 | 12.36 | 19.74 | 1.00 | 90.4 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 4.03 | 11.88 | 18.90 | 3.00 | 88.0 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.3 | 5.62 | 15.45 | 23.03 | 2.00 | 86.8 | 85.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.45 | 13.06 | 21.76 | 2.00 | 76.7 | 84.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 1.16 | 3.31 | 7.60 | 7.00 | 25.4 | 13.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.6 | 6.83 | 19.28 | 30.00 | 3.00 | 97.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 4.82 | 15.21 | 27.40 | 6.00 | 62.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.68 | 13.48 | 21.43 | 4.00 | 80.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.32 | 13.03 | 20.04 | 3.00 | 74.1 | 77.0 |
| Bench 3 | Bench | Moisés Caicedo Corozo | MID | 7 | 5.9 | 3.90 | 11.55 | 16.77 | 2.00 | 67.4 | 90.0 |

## GW10

- Train rows: 167841
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Antoine Semenyo
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: none
- Predicted score: 56.18
- Actual score: 78.00
- Transfer: Mohammed Kudus -> Iliman Ndiaye (projected gain 3.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 3.28 | 9.45 | 15.45 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.3 | 0.00 | 0.31 | 0.90 | 0.00 | 4.3 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.58 | 15.56 | 24.45 | 12.00 | 92.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.9 | 5.11 | 14.92 | 24.09 | 10.00 | 95.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.64 | 12.96 | 21.33 | 3.00 | 85.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.90 | 11.98 | 19.69 | 5.00 | 82.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.93 | 11.10 | 17.84 | 7.00 | 83.3 | 90.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.4 | 5.01 | 14.15 | 21.44 | 1.00 | 75.8 | 45.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 1.96 | 8.00 | 15.12 | 9.00 | 40.9 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 1.15 | 4.51 | 8.48 | 0.00 | 29.9 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.47 | 17.65 | 29.08 | 2.00 | 100.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.33 | 16.37 | 28.18 | 10.00 | 72.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.58 | 14.30 | 22.64 | 9.00 | 87.0 | 61.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.78 | 14.02 | 22.57 | 5.00 | 76.5 | 90.0 |
| Bench 2 | Bench | Moisés Caicedo Corozo | MID | 7 | 5.9 | 3.34 | 10.92 | 17.74 | 10.00 | 72.0 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: none
- Predicted score: 61.09
- Actual score: 39.00
- Transfer: Nick Woltemade -> Jarrod Bowen (projected gain 0.69, hit 0)
- Autosub: Marcos Senesi Barón replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 2.59 | 8.49 | 14.17 | 2.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.3 | 0.09 | 0.34 | 0.81 | 0.00 | 4.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.42 | 17.21 | 27.25 | 1.00 | 95.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 4.9 | 5.36 | 15.18 | 23.84 | 0.00 | 93.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.82 | 11.99 | 19.06 | 6.00 | 86.5 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.16 | 11.98 | 19.43 | 2.00 | 93.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.71 | 11.28 | 18.40 | 1.00 | 87.6 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.96 | 15.51 | 24.86 | 7.00 | 91.5 | 82.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.80 | 12.56 | 20.17 | 2.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 0.91 | 3.33 | 6.41 | 0.00 | 19.1 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.53 | 17.70 | 30.05 | 2.00 | 86.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.84 | 17.44 | 28.14 | 0.00 | 105.4 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.9 | 5.51 | 13.87 | 21.48 | 2.00 | 95.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.75 | 13.81 | 22.96 | 5.00 | 82.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.57 | 12.52 | 20.12 | 3.00 | 78.0 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.86
- Actual score: 35.00
- Transfer: Jarrod Bowen -> Igor Thiago Nascimento Rodrigues (projected gain 2.43, hit 0)
- Autosub: Marc Guéhi replaced Antoine Semenyo.
- Autosub: Lyle Foster replaced Moisés Caicedo Corozo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 2.92 | 8.63 | 14.25 | 3.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.3 | 0.00 | 0.00 | 0.27 | 0.00 | 0.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.06 | 13.30 | 21.22 | 3.00 | 102.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.66 | 12.64 | 20.63 | 6.00 | 83.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.89 | 12.51 | 19.79 | 3.00 | 95.2 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 8 | 4.9 | 3.49 | 9.15 | 15.15 | 5.00 | 47.1 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 1.77 | 8.42 | 15.80 | 0.00 | 35.7 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.69 | 15.54 | 24.21 | 1.00 | 83.2 | 75.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.4 | 4.89 | 13.93 | 21.78 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Autosub In | Lyle Foster | FWD | 3 | 5.0 | 0.81 | 2.78 | 5.26 | 1.00 | 16.3 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.2 | 6.41 | 18.53 | 30.91 | 2.00 | 93.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.33 | 15.17 | 23.99 | 2.00 | 91.8 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 4 | 7.5 | 5.17 | 14.90 | 24.30 | 0.00 | 80.6 | 0.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.51 | 12.63 | 18.97 | 0.00 | 79.0 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.91 | 12.15 | 20.49 | 3.00 | 73.5 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 1.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Mohamed Salah
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 56.52
- Actual score: 54.00
- Transfer: Moisés Caicedo Corozo -> Morgan Rogers (projected gain 8.01, hit 0)
- Autosub: Antoine Semenyo replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 2.80 | 8.17 | 13.36 | 1.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.3 | 0.29 | 0.29 | 0.48 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.01 | 11.90 | 20.01 | 1.00 | 80.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.72 | 11.34 | 18.11 | 2.00 | 82.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.9 | 3.96 | 11.08 | 18.48 | 0.00 | 74.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.35 | 10.03 | 17.48 | 6.00 | 67.8 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 0.33 | 4.55 | 9.96 | 0.00 | 11.4 | 0.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.5 | 6.86 | 17.58 | 26.08 | 13.00 | 99.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.80 | 11.96 | 19.84 | 1.00 | 59.5 | 54.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 0.99 | 3.55 | 6.19 | 2.00 | 21.4 | 74.0 |
| Vice Captain | Bench | Mohamed Salah | MID | 12 | 14.2 | 6.31 | 18.59 | 30.60 | 0.00 | 91.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 6.9 | 6.15 | 15.54 | 23.91 | 3.00 | 105.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.79 | 14.18 | 24.05 | 11.00 | 82.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.92 | 10.74 | 18.71 | 2.00 | 66.5 | 79.0 |
| Bench 2 | Autosub In | Antoine Semenyo | MID | 4 | 7.5 | 2.23 | 8.12 | 14.89 | 1.00 | 29.4 | 90.0 |

## GW14

- Train rows: 170850
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Declan Rice
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.38
- Actual score: 44.00
- Transfer: Morgan Rogers -> Declan Rice (projected gain 5.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 2.46 | 7.74 | 12.91 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.3 | 0.00 | 0.00 | 0.06 | 1.00 | 0.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.49 | 12.60 | 20.15 | 1.00 | 87.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.42 | 11.99 | 19.44 | 4.00 | 90.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.9 | 4.14 | 11.07 | 18.09 | 14.00 | 77.6 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.44 | 10.39 | 17.02 | 0.00 | 76.2 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 1.52 | 5.28 | 11.15 | 0.00 | 17.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.5 | 3.53 | 12.87 | 20.69 | 1.00 | 62.5 | 30.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.46 | 12.79 | 21.25 | 2.00 | 64.5 | 90.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 1.73 | 5.30 | 8.15 | 2.00 | 40.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.15 | 17.21 | 27.48 | 4.00 | 99.5 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 5.52 | 15.66 | 25.48 | 3.00 | 89.3 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.4 | 5.20 | 14.11 | 23.40 | 4.00 | 84.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.1 | 4.18 | 13.36 | 23.17 | 1.00 | 43.7 | 45.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.68 | 10.69 | 17.46 | 3.00 | 73.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Daniel Muñoz Mejía
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 52.32
- Actual score: 81.00
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 3.88, hit 0)
- Autosub: Iliman Ndiaye replaced Daniel Muñoz Mejía.
- Autosub: Marcos Senesi Barón replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 2.34 | 7.48 | 12.37 | 1.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.3 | 1.01 | 2.78 | 4.14 | 0.00 | 35.6 | 0.0 |
| Vice Captain | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.1 | 4.92 | 14.44 | 22.97 | 0.00 | 94.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.9 | 4.60 | 13.24 | 20.61 | 8.00 | 93.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.90 | 11.72 | 19.22 | 6.00 | 83.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.96 | 11.38 | 18.88 | 2.00 | 86.4 | 90.0 |
| Bench 3 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 2.37 | 7.11 | 12.51 | 8.00 | 40.9 | 61.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.6 | 4.87 | 13.86 | 22.28 | 2.00 | 73.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.79 | 11.70 | 19.93 | 1.00 | 62.5 | 32.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.26 | 6.13 | 9.17 | 1.00 | 53.7 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.70 | 15.96 | 26.28 | 18.00 | 89.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.1 | 4.72 | 14.40 | 25.04 | 0.00 | 59.0 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 3.91 | 12.59 | 22.02 | 6.00 | 69.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.4 | 3.91 | 12.28 | 20.98 | 3.00 | 64.1 | 90.0 |
| Bench 2 | Autosub In | Iliman Ndiaye | MID | 9 | 6.5 | 3.60 | 10.76 | 17.30 | 8.00 | 75.1 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.30 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.58
- Actual score: 67.00
- Transfer: Daniel Muñoz Mejía -> Matty Cash (projected gain 4.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 2.55 | 7.43 | 12.24 | 9.00 | 81.4 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 0.16 | 0.60 | 1.06 | 1.00 | 10.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.91 | 13.83 | 21.92 | 1.00 | 100.4 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 5.22 | 13.71 | 21.43 | 0.00 | 107.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.24 | 12.61 | 20.43 | 6.00 | 91.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.96 | 11.60 | 18.80 | 6.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 2.34 | 7.67 | 13.68 | 1.00 | 52.8 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 7.22 | 18.04 | 28.17 | 2.00 | 109.5 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 2.75 | 9.35 | 16.67 | 2.00 | 44.7 | 80.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 1.95 | 5.52 | 8.26 | 2.00 | 42.6 | 61.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.1 | 7.86 | 20.57 | 33.61 | 13.00 | 119.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.31 | 14.14 | 23.46 | 2.00 | 83.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 3.62 | 11.41 | 19.48 | 6.00 | 65.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.43 | 11.25 | 19.97 | 7.00 | 29.1 | 64.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.4 | 3.41 | 10.54 | 17.59 | 2.00 | 70.9 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.40 -> 2.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 57.02
- Actual score: 57.00
- Transfer: Iliman Ndiaye -> Harry Wilson (projected gain 5.58, hit 0)
- Autosub: Igor Thiago Nascimento Rodrigues replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 2.60 | 7.86 | 12.73 | 7.00 | 81.7 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 1.34 | 3.51 | 5.13 | 0.00 | 44.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.87 | 13.29 | 20.91 | 1.00 | 93.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.13 | 11.90 | 19.48 | 2.00 | 86.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.90 | 11.72 | 19.10 | 1.00 | 85.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.03 | 10.38 | 17.11 | 4.00 | 74.7 | 90.0 |
| Bench 3 | Bench | Matty Cash | DEF | 2 | 4.9 | 2.85 | 9.19 | 14.44 | 2.00 | 61.0 | 90.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.8 | 3.19 | 10.73 | 17.13 | 2.00 | 41.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.25 | 10.06 | 17.14 | 6.00 | 59.9 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 1.83 | 5.39 | 8.70 | 0.00 | 44.6 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.28 | 19.16 | 31.14 | 1.00 | 90.8 | 45.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.7 | 5.91 | 16.00 | 24.19 | 2.00 | 106.7 | 83.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.3 | 6.28 | 15.68 | 24.66 | 10.00 | 98.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.95 | 14.77 | 25.03 | 0.00 | 58.7 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.54 | 13.73 | 22.31 | 11.00 | 74.5 | 90.0 |

## GW18

- Train rows: 173897
- Bank: 2.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Declan Rice
- Effective captain: Morgan Rogers
- Chip used: none
- Predicted score: 54.29
- Actual score: 41.00
- Transfer: Harry Wilson -> Morgan Rogers (projected gain 6.34, hit 0)
- Autosub: Igor Thiago Nascimento Rodrigues replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 3.02 | 8.37 | 13.40 | 3.00 | 81.1 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 0.31 | 0.90 | 1.54 | 0.00 | 13.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.10 | 13.76 | 21.59 | 2.00 | 96.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.11 | 11.93 | 19.02 | 2.00 | 80.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.87 | 11.30 | 17.89 | 2.00 | 80.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.86 | 11.01 | 18.45 | 2.00 | 84.4 | 68.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 2.95 | 8.88 | 14.74 | 1.00 | 75.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.96 | 11.37 | 18.68 | 8.00 | 74.1 | 68.0 |
| Bench 2 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 2.28 | 8.48 | 14.79 | 5.00 | 48.1 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 0.96 | 2.89 | 5.12 | 0.00 | 19.9 | 0.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.3 | 6.02 | 16.29 | 25.50 | 1.00 | 106.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.1 | 5.83 | 16.24 | 25.52 | 5.00 | 99.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.4 | 5.35 | 15.51 | 24.48 | 9.00 | 84.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.20 | 12.66 | 21.38 | 0.00 | 35.6 | 0.0 |
| Bench 3 | Bench | Bruno Borges Fernandes | MID | 14 | 9.1 | 2.14 | 10.85 | 20.14 | 0.00 | 23.2 | 0.0 |

## GW19

- Train rows: 174672
- Bank: 0.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Matheus Santos Carneiro da Cunha
- Vice captain: Antoine Semenyo
- Effective captain: Matheus Santos Carneiro da Cunha
- Chip used: none
- Predicted score: 52.77
- Actual score: 31.00
- Transfer: Bruno Borges Fernandes -> Matheus Santos Carneiro da Cunha (projected gain 7.44, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 2.31 | 7.41 | 12.40 | 7.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 0.06 | 0.76 | 1.39 | 0.00 | 14.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.61 | 12.66 | 20.21 | 2.00 | 92.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.11 | 11.95 | 19.66 | 6.00 | 83.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.73 | 11.10 | 17.38 | 3.00 | 84.6 | 90.0 |
| Bench 2 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.45 | 10.11 | 16.78 | 0.00 | 72.5 | 0.0 |
| Bench 3 | Bench | Matty Cash | DEF | 2 | 4.9 | 2.10 | 7.55 | 13.08 | 0.00 | 68.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 4.45 | 12.67 | 20.54 | 1.00 | 74.8 | 27.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.81 | 11.19 | 18.64 | 2.00 | 74.5 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 0.87 | 2.70 | 4.61 | 0.00 | 18.2 | 0.0 |
| Captain | Captain | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 6.39 | 16.04 | 24.31 | 2.00 | 89.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.4 | 4.95 | 15.04 | 24.20 | 5.00 | 82.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.87 | 12.95 | 21.03 | 1.00 | 73.9 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.1 | 4.16 | 12.91 | 21.00 | 0.00 | 69.2 | 0.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 3.99 | 11.91 | 20.11 | 0.00 | 36.6 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 1.30 -> 1.50
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Antoine Semenyo
- Effective captain: Morgan Rogers
- Chip used: none
- Predicted score: 51.19
- Actual score: 55.00
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.05, hit 0)
- Autosub: Matty Cash replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 3.24 | 9.43 | 15.18 | 3.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 0.22 | 0.71 | 1.22 | 0.00 | 8.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.40 | 12.47 | 19.94 | 2.00 | 95.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.00 | 11.74 | 19.44 | 1.00 | 86.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.90 | 11.23 | 18.59 | 1.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.0 | 1.51 | 6.26 | 11.28 | 0.00 | 41.5 | 0.0 |
| Bench 2 | Autosub In | Matty Cash | DEF | 2 | 4.8 | 1.87 | 5.61 | 9.79 | 5.00 | 43.4 | 89.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.6 | 3.87 | 11.32 | 18.82 | 17.00 | 80.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.03 | 10.01 | 16.87 | 2.00 | 59.9 | 61.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 0.43 | 2.03 | 4.07 | 0.00 | 14.2 | 0.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.4 | 6.13 | 16.77 | 26.43 | 5.00 | 102.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.4 | 5.22 | 15.33 | 24.54 | 1.00 | 92.6 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.89 | 14.95 | 24.00 | 4.00 | 73.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.26 | 10.72 | 17.64 | 9.00 | 51.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 3.12 | 10.26 | 18.08 | 0.00 | 25.0 | 0.0 |

## GW21

- Train rows: 176242
- Bank: 1.50 -> 1.80
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Rayan Cherki
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 54.80
- Actual score: 61.00
- Transfer: Marc Cucurella Saseta -> James Tarkowski (projected gain 5.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.7 | 3.10 | 9.36 | 15.09 | 2.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 0.11 | 0.62 | 1.27 | 2.00 | 7.8 | 45.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 5.06 | 13.14 | 20.19 | 4.00 | 93.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.42 | 12.21 | 19.59 | 6.00 | 91.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.27 | 10.48 | 17.55 | 6.00 | 83.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.41 | 9.29 | 16.40 | 6.00 | 74.0 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 4.8 | 2.76 | 7.86 | 13.04 | 6.00 | 67.4 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 6.08 | 16.05 | 25.55 | 12.00 | 110.9 | 81.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.66 | 11.07 | 18.08 | 1.00 | 63.8 | 15.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 0.56 | 1.78 | 3.81 | 0.00 | 13.0 | 14.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.8 | 5.13 | 14.82 | 23.66 | 1.00 | 84.0 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.11 | 14.53 | 23.72 | 6.00 | 91.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.83 | 13.81 | 22.23 | 3.00 | 75.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.64 | 13.21 | 21.71 | 2.00 | 76.9 | 73.0 |
| Bench 3 | Bench | Mohamed Salah | MID | 12 | 14.0 | 2.65 | 9.53 | 16.94 | 0.00 | 21.0 | 0.0 |

## GW22

- Train rows: 177037
- Bank: 1.80 -> 8.60
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 55.43
- Actual score: 33.00
- Transfer: Mohamed Salah -> Bruno Guimarães Rodriguez Moura (projected gain 6.83, hit 0)
- Autosub: Matheus Santos Carneiro da Cunha replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.7 | 3.26 | 9.45 | 15.40 | 2.00 | 90.5 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 1.13 | 3.25 | 5.28 | 0.00 | 34.1 | 0.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 4.54 | 12.85 | 20.66 | 0.00 | 95.4 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.19 | 12.56 | 19.85 | 8.00 | 85.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.51 | 12.02 | 19.38 | 2.00 | 90.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.71 | 10.94 | 17.89 | 3.00 | 82.9 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.8 | 3.37 | 9.33 | 14.95 | 2.00 | 76.1 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 5.87 | 15.34 | 24.21 | 2.00 | 89.7 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.1 | 2.61 | 9.31 | 15.97 | 8.00 | 41.4 | 73.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 0.77 | 2.87 | 4.96 | 1.00 | 21.8 | 16.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.85 | 15.79 | 25.15 | 3.00 | 100.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.41 | 15.77 | 25.40 | 2.00 | 98.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 5.12 | 14.61 | 24.21 | 2.00 | 86.2 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 3.75 | 11.78 | 19.58 | 1.00 | 51.9 | 45.0 |
| Bench 2 | Autosub In | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 2.87 | 9.95 | 17.79 | 4.00 | 55.7 | 19.0 |

## GW23

- Train rows: 177836
- Bank: 8.60 -> 9.20
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Antoine Semenyo
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 56.19
- Actual score: 59.00
- Transfer: Matheus Santos Carneiro da Cunha -> Declan Rice (projected gain 6.01, hit 0)
- Autosub: Matty Cash replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.7 | 3.01 | 8.92 | 14.59 | 1.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 0.44 | 1.43 | 2.64 | 0.00 | 18.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.94 | 13.36 | 21.62 | 4.00 | 90.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.22 | 11.68 | 18.07 | 3.00 | 88.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.65 | 10.87 | 17.80 | 9.00 | 85.4 | 90.0 |
| Bench 2 | Autosub In | Matty Cash | DEF | 2 | 4.8 | 3.37 | 9.66 | 15.18 | 6.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.0 | 2.82 | 7.79 | 13.48 | 6.00 | 49.5 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.8 | 5.99 | 15.84 | 25.15 | 2.00 | 93.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.1 | 3.78 | 11.46 | 18.80 | 12.00 | 67.4 | 84.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 1.11 | 3.40 | 5.54 | 5.00 | 24.5 | 21.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.4 | 5.75 | 15.71 | 25.01 | 8.00 | 94.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.44 | 15.59 | 24.26 | 1.00 | 93.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.71 | 13.47 | 21.99 | 8.00 | 78.7 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.52 | 13.37 | 21.97 | 0.00 | 75.6 | 0.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.7 | 4.20 | 11.93 | 20.36 | 3.00 | 56.5 | 72.0 |

## GW24

- Train rows: 178639
- Bank: 9.20 -> 6.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.27
- Actual score: 67.00
- Transfer: Bruno Guimarães Rodriguez Moura -> Bruno Borges Fernandes (projected gain 8.95, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.7 | 3.28 | 9.00 | 14.69 | 6.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.2 | 0.50 | 1.45 | 2.58 | 0.00 | 17.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.31 | 12.37 | 19.88 | 4.00 | 92.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.47 | 12.10 | 18.75 | 8.00 | 94.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.04 | 12.04 | 19.74 | 2.00 | 83.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.83 | 10.90 | 17.83 | 3.00 | 76.8 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | 2 | 4.8 | 3.65 | 10.21 | 15.91 | 2.00 | 87.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 6.22 | 15.71 | 24.57 | 10.00 | 101.1 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.8 | 4.27 | 13.45 | 21.85 | 2.00 | 77.6 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 1.49 | 4.66 | 7.42 | 2.00 | 30.0 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.5 | 6.93 | 18.33 | 27.46 | 10.00 | 102.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.4 | 5.94 | 16.76 | 26.85 | 7.00 | 101.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.52 | 16.15 | 25.46 | 3.00 | 94.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 5.53 | 15.41 | 24.60 | 2.00 | 93.5 | 90.0 |
| Bench 3 | Bench | Rayan Cherki | MID | 13 | 6.6 | 3.41 | 10.70 | 18.47 | 8.00 | 50.7 | 68.0 |

## GW25

- Train rows: 179450
- Bank: 6.90 -> 4.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Declan Rice
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.05
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.96) beats the best remaining Bench Boost opportunity (14.24).
- Transfer: Matty Cash -> Gabriel dos Santos Magalhães (projected gain 4.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.96) beats the best remaining Bench Boost opportunity (14.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.7 | 2.57 | 8.33 | 13.66 | 1.00 | 79.8 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.2 | 0.00 | 0.27 | 0.66 | 0.00 | 5.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.57 | 15.20 | 24.03 | 6.00 | 90.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 12.20 | 19.30 | 0.00 | 90.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 11.79 | 19.37 | 2.00 | 82.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.14 | 11.38 | 18.29 | 2.00 | 87.7 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 3.55 | 10.47 | 17.25 | 3.00 | 72.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.95 | 13.83 | 21.55 | 8.00 | 69.5 | 74.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.56 | 12.14 | 20.15 | 5.00 | 65.5 | 90.0 |
| Bench 4 | Bench Boost | Lyle Foster | FWD | 3 | 4.9 | 2.00 | 5.27 | 8.21 | 1.00 | 38.3 | 23.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.6 | 6.10 | 16.75 | 25.15 | 10.00 | 82.7 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.83 | 16.32 | 26.14 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.4 | 5.40 | 15.89 | 25.92 | 2.00 | 95.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.66 | 13.74 | 22.18 | 10.00 | 80.4 | 90.0 |
| Bench 3 | Bench Boost | Rayan Cherki | MID | 13 | 6.6 | 3.41 | 10.68 | 17.83 | 1.00 | 57.5 | 29.0 |

## GW26

- Train rows: 180267
- Bank: 4.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: triple_captain
- Predicted score: 70.33
- Actual score: 107.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.89) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Marco Bizot -> David Raya Martín (projected gain 5.17, hit 0)
- Chip used: Triple Captain on Declan Rice. Optimizer chose Triple Captain here because the current estimated captain upside (9.89) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.38 | 13.16 | 20.67 | 3.00 | 117.8 | 180.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.7 | 2.81 | 8.12 | 13.28 | 2.00 | 78.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.64 | 16.83 | 26.29 | 7.00 | 124.0 | 180.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.58 | 12.54 | 19.47 | 7.00 | 91.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.10 | 11.88 | 18.98 | 17.00 | 89.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.88 | 10.84 | 18.16 | 2.00 | 80.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.65 | 10.48 | 17.81 | 1.00 | 77.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.15 | 13.97 | 21.86 | 10.00 | 68.5 | 90.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.58 | 12.12 | 20.34 | 2.00 | 73.1 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 1.58 | 4.60 | 7.53 | 1.00 | 31.1 | 17.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.4 | 6.87 | 17.28 | 27.20 | 14.00 | 119.0 | 180.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.6 | 5.88 | 16.67 | 27.18 | 2.00 | 80.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.5 | 5.34 | 15.11 | 24.89 | 14.00 | 91.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.14 | 14.90 | 23.81 | 2.00 | 92.0 | 90.0 |
| Bench 3 | Bench | Rayan Cherki | MID | 13 | 6.5 | 3.26 | 9.48 | 15.98 | 1.00 | 49.1 | 19.0 |
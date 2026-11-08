# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 263.52
- Total actual points: 145.00
- Average predicted points: 65.88
- Average actual points: 36.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW9 are included before the first simulated week.
- League-average scores were not available for this run.

## GW10

- Train rows: 167841
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Antoine Semenyo
- Vice captain: Micky van de Ven
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 62.57
- Actual score: 72.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.27 | 12.18 | 19.76 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.59 | 10.75 | 17.73 | 2.00 | 100.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 5.34 | 15.85 | 25.94 | 12.00 | 90.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.9 | 5.22 | 15.43 | 25.17 | 10.00 | 94.9 | 90.0 |
| Vice Captain | XI | Micky van de Ven | DEF | 18 | 4.7 | 5.39 | 15.16 | 24.50 | 2.00 | 104.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.44 | 14.38 | 23.74 | 3.00 | 94.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.0 | 4.82 | 13.69 | 22.08 | 6.00 | 82.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.05 | 15.22 | 25.60 | 9.00 | 85.3 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 4.87 | 13.83 | 21.53 | 2.00 | 98.6 | 61.0 |
| Bench 2 | Bench | Nick Woltemade | FWD | 15 | 7.4 | 4.77 | 13.69 | 21.22 | 1.00 | 73.2 | 45.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.14 | 19.02 | 31.60 | 2.00 | 102.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 5.12 | 15.40 | 26.37 | 10.00 | 69.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 5.25 | 15.40 | 24.89 | 2.00 | 91.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.99 | 14.93 | 23.91 | 9.00 | 90.8 | 61.0 |
| Bench 4 | Bench | Mohammed Kudus | MID | 18 | 6.8 | 4.41 | 12.99 | 21.30 | 1.00 | 76.9 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 62.31
- Actual score: 27.00
- Chip advisory: bench_boost (0.65): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Mohammed Kudus -> Moisés Caicedo Corozo (projected gain 1.00, hit 0)
- Autosub outfielders: Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.33 | 12.57 | 20.22 | 1.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.55 | 10.24 | 16.91 | 2.00 | 98.4 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.87 | 17.75 | 28.98 | 1.00 | 94.6 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.0 | 5.58 | 15.63 | 25.27 | 0.00 | 94.8 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.89 | 13.99 | 22.90 | 1.00 | 96.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.66 | 13.72 | 22.77 | 2.00 | 99.1 | 90.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.1 | 4.41 | 12.95 | 20.66 | 1.00 | 80.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.21 | 14.55 | 24.52 | 7.00 | 79.3 | 82.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 4.45 | 12.76 | 19.97 | 1.00 | 84.2 | 27.0 |
| Bench 4 | Bench | Nick Woltemade | FWD | 15 | 7.5 | 3.91 | 12.25 | 20.16 | 5.00 | 60.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 5.92 | 18.25 | 30.13 | 0.00 | 100.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 5.51 | 16.57 | 25.53 | 7.00 | 80.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 4.87 | 15.36 | 26.23 | 2.00 | 74.6 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.9 | 4.95 | 13.74 | 22.25 | 2.00 | 88.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.61 | 13.69 | 22.21 | 3.00 | 80.1 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 1.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: triple_captain
- Predicted score: 69.82
- Actual score: 27.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (7.78).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Nick Woltemade -> Jean-Philippe Mateta (projected gain 2.31, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (7.78).
- Autosub outfielders: Jurriën Timber, Marc Guéhi, Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.24 | 12.21 | 19.75 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.59 | 10.38 | 16.99 | 2.00 | 96.8 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.6 | 5.82 | 17.18 | 28.10 | 0.00 | 95.0 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.8 | 4.46 | 13.59 | 22.41 | 0.00 | 100.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.78 | 12.95 | 21.72 | 3.00 | 93.1 | 90.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 4.16 | 12.02 | 19.42 | 5.00 | 79.8 | 90.0 |
| Bench 3 | Autosub In | Marc Guéhi | DEF | 13 | 5.1 | 3.99 | 11.14 | 18.80 | 5.00 | 55.6 | 90.0 |
| Vice Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.99 | 16.67 | 26.14 | 1.00 | 88.4 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.0 | 4.54 | 14.30 | 22.52 | 1.00 | 65.1 | 59.0 |
| Bench 4 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.25 | 10.16 | 17.24 | 2.00 | 50.8 | 85.0 |
| Captain | Bench | Antoine Semenyo | MID | 13 | 8.1 | 6.60 | 18.65 | 30.08 | 0.00 | 100.1 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 5.92 | 17.09 | 27.32 | 1.00 | 94.2 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.34 | 15.91 | 26.55 | 2.00 | 79.5 | 90.0 |
| XI | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.74 | 13.54 | 21.29 | 0.00 | 84.8 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.21 | 12.90 | 21.66 | 3.00 | 77.7 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Bryan Mbeumo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 68.81
- Actual score: 19.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.22) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Iliman Ndiaye -> Pedro Lomba Neto (projected gain 2.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.22) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.87 | 11.50 | 18.91 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.43 | 10.14 | 16.62 | 1.00 | 94.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.70 | 13.69 | 22.51 | 2.00 | 96.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.8 | 4.23 | 12.70 | 20.56 | 0.00 | 88.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.38 | 12.64 | 21.02 | 0.00 | 78.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.14 | 12.06 | 19.12 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 2.40 | 9.00 | 17.68 | 0.00 | 39.4 | 0.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.78 | 16.09 | 25.79 | 1.00 | 87.0 | 54.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.25 | 13.62 | 22.17 | 6.00 | 62.7 | 90.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 3.38 | 11.38 | 19.26 | 1.00 | 62.4 | 10.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.51 | 16.32 | 25.64 | 1.00 | 81.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 5.14 | 15.52 | 25.64 | 0.00 | 75.2 | 0.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.1 | 4.74 | 13.69 | 22.17 | 2.00 | 80.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.08 | 12.42 | 21.69 | 1.00 | 54.7 | 90.0 |
| Bench 3 | Bench Boost | Moisés Caicedo Corozo | MID | 7 | 6.1 | 3.01 | 9.30 | 15.84 | -2.00 | 51.1 | 37.0 |
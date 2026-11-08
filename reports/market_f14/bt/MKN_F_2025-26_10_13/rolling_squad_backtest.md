# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 276.15
- Total actual points: 184.00
- Average predicted points: 69.04
- Average actual points: 46.00
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 69.68
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.98 | 12.71 | 20.19 | 6.00 | 95.8 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.01 | 0.17 | 0.42 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 6.24 | 16.34 | 25.33 | 12.00 | 96.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.07 | 14.89 | 24.01 | 10.00 | 95.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.68 | 14.33 | 22.31 | 6.00 | 89.7 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.24 | 12.59 | 20.94 | 3.00 | 83.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.24 | 11.83 | 18.98 | 2.00 | 91.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.90 | 23.39 | 38.05 | 13.00 | 102.9 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 6.15 | 16.24 | 25.35 | 9.00 | 95.2 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 5.11 | 14.31 | 21.65 | 1.00 | 75.6 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 6.90 | 19.48 | 30.23 | 2.00 | 116.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 4.64 | 16.78 | 28.11 | 2.00 | 92.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.86 | 14.72 | 23.24 | 9.00 | 87.2 | 61.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.0 | 3.79 | 10.69 | 16.66 | 2.00 | 80.2 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.56 | 9.57 | 15.73 | 1.00 | 62.7 | 59.0 |

## GW11

- Train rows: 168588
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.53
- Actual score: 33.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 4.45, hit 0)
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.53 | 12.28 | 19.46 | 1.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.08 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 6.23 | 18.13 | 28.19 | 1.00 | 100.8 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.03 | 14.87 | 23.50 | 0.00 | 89.8 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.71 | 12.91 | 20.22 | 1.00 | 81.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.23 | 12.16 | 19.76 | 2.00 | 93.8 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 3.92 | 11.20 | 18.31 | 1.00 | 85.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.51 | 23.37 | 38.86 | 4.00 | 94.3 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.33 | 16.04 | 24.86 | 2.00 | 78.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 6.21 | 15.56 | 24.69 | 7.00 | 94.6 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.46 | 17.05 | 27.72 | 0.00 | 99.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.31 | 14.45 | 22.47 | 7.00 | 65.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.47 | 12.59 | 20.44 | 3.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.55 | 9.60 | 15.66 | 1.00 | 58.1 | 73.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.58 | 8.99 | 14.18 | 3.00 | 80.3 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 72.97
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.69) beats the best remaining Bench Boost opportunity (10.05).
- Transfer: Gabriel dos Santos Magalhães -> Virgil van Dijk (projected gain 3.18, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.69) beats the best remaining Bench Boost opportunity (10.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.13 | 11.34 | 18.20 | 2.00 | 83.7 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.53 | 14.00 | 22.17 | 3.00 | 108.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.10 | 13.72 | 21.43 | 5.00 | 93.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 5.31 | 13.09 | 20.56 | 3.00 | 101.9 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.14 | 10.84 | 17.71 | 0.00 | 86.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.28 | 9.00 | 15.03 | 5.00 | 44.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.45 | 23.53 | 38.89 | 2.00 | 97.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.57 | 15.31 | 23.84 | 1.00 | 80.6 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.91 | 14.63 | 23.63 | 1.00 | 65.9 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.66 | 18.54 | 29.08 | 1.00 | 106.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.49 | 15.22 | 24.63 | 0.00 | 85.3 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.42 | 11.97 | 20.63 | 3.00 | 68.6 | 80.0 |
| Bench 3 | Bench Boost | James Garner | MID | 9 | 5.0 | 2.82 | 9.07 | 15.36 | 6.00 | 72.1 | 90.0 |
| Bench 4 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.73 | 8.71 | 14.18 | 2.00 | 68.4 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 1.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.97
- Actual score: 30.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.21) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 5.21, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.21) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.07 | 9.73 | 16.12 | 3.00 | 75.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.14 | 11.88 | 18.80 | 2.00 | 85.7 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.75 | 11.73 | 18.84 | 2.00 | 75.4 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.14 | 11.69 | 19.34 | 0.00 | 89.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.99 | 11.02 | 18.90 | 6.00 | 75.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.72 | 10.84 | 18.22 | 0.00 | 72.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 9.21 | 24.86 | 39.53 | 2.00 | 108.4 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.53 | 12.21 | 20.57 | 6.00 | 51.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.52 | 11.70 | 19.63 | 1.00 | 56.6 | 54.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 6.25 | 15.54 | 23.82 | 3.00 | 107.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.23 | 14.38 | 23.27 | 1.00 | 69.5 | 90.0 |
| Bench 2 | Bench | Iliman Ndiaye | MID | 9 | 6.5 | 3.52 | 10.41 | 18.51 | 2.00 | 62.9 | 79.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.34 | 9.37 | 15.87 | 2.00 | 76.3 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.20 | 8.58 | 14.12 | 0.00 | 70.5 | 0.0 |
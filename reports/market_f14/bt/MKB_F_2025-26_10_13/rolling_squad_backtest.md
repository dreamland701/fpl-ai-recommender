# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 277.69
- Total actual points: 179.00
- Average predicted points: 69.42
- Average actual points: 44.75
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
- Predicted score: 68.63
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.45 | 12.29 | 19.71 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.06 | 0.24 | 0.47 | 0.00 | 1.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.61 | 15.88 | 24.86 | 12.00 | 89.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.04 | 14.92 | 24.05 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.06 | 13.97 | 22.02 | 6.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.69 | 12.89 | 21.19 | 3.00 | 87.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.51 | 12.04 | 19.14 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.91 | 23.62 | 38.64 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.87 | 16.46 | 25.51 | 9.00 | 90.0 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 4.87 | 14.31 | 21.64 | 1.00 | 72.9 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.28 | 20.32 | 31.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.47 | 17.49 | 28.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.65 | 14.49 | 22.87 | 9.00 | 86.1 | 61.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.41 | 10.39 | 16.40 | 2.00 | 77.8 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.11 | 10.14 | 16.39 | 1.00 | 70.7 | 59.0 |

## GW11

- Train rows: 168588
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.33
- Actual score: 33.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 3.05, hit 0)
- Autosub: Jurriën Timber replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.11 | 12.03 | 19.25 | 1.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.02 | 0.02 | 0.13 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.45 | 17.50 | 27.57 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.27 | 15.11 | 23.73 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 4.07 | 12.42 | 19.83 | 1.00 | 77.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.19 | 12.04 | 19.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.27 | 11.49 | 18.56 | 1.00 | 89.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.50 | 24.35 | 40.05 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.49 | 16.36 | 24.98 | 2.00 | 79.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.69 | 15.37 | 24.64 | 7.00 | 88.5 | 82.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.87 | 17.40 | 28.11 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.45 | 14.64 | 22.64 | 7.00 | 67.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.53 | 12.56 | 20.17 | 3.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.03 | 10.03 | 16.12 | 1.00 | 66.4 | 73.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.36 | 8.75 | 13.89 | 3.00 | 78.3 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.25
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.49) beats the best remaining Bench Boost opportunity (11.00).
- Transfer: Gabriel dos Santos Magalhães -> Virgil van Dijk (projected gain 4.61, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.49) beats the best remaining Bench Boost opportunity (11.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.85 | 11.06 | 17.90 | 2.00 | 82.1 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.6 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.75 | 13.58 | 21.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.96 | 13.54 | 21.54 | 3.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.81 | 12.57 | 19.85 | 3.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.54 | 11.22 | 18.07 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 3.52 | 9.15 | 15.12 | 5.00 | 47.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.43 | 24.50 | 40.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.66 | 15.51 | 24.14 | 1.00 | 82.2 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.19 | 14.92 | 23.79 | 1.00 | 69.7 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.73 | 18.90 | 29.48 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.46 | 14.88 | 24.25 | 0.00 | 85.0 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.94 | 12.25 | 20.65 | 3.00 | 73.4 | 80.0 |
| Bench 3 | Bench Boost | James Garner | MID | 9 | 5.0 | 3.12 | 9.37 | 15.64 | 6.00 | 75.3 | 90.0 |
| Bench 4 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.84 | 8.83 | 14.31 | 2.00 | 70.6 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Eberechi Eze
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.48
- Actual score: 25.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.01) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 5.06, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.01) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.30 | 9.95 | 16.43 | 3.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.9 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.88 | 11.99 | 19.14 | 2.00 | 78.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.91 | 11.54 | 18.39 | 2.00 | 83.4 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.97 | 11.43 | 18.99 | 0.00 | 87.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.98 | 11.03 | 18.41 | 0.00 | 75.4 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.0 | 3.59 | 10.45 | 18.09 | 6.00 | 68.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 9.01 | 25.24 | 40.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.68 | 12.17 | 20.46 | 6.00 | 54.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.00 | 11.84 | 19.66 | 1.00 | 62.8 | 54.0 |
| Vice Captain | XI | Eberechi Eze | MID | 1 | 7.7 | 5.18 | 15.44 | 24.64 | 2.00 | 90.0 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.66 | 14.60 | 23.35 | 1.00 | 73.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.88 | 10.64 | 18.60 | 2.00 | 66.7 | 79.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.40 | 9.44 | 15.93 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.75 | 9.09 | 14.63 | 0.00 | 77.1 | 0.0 |
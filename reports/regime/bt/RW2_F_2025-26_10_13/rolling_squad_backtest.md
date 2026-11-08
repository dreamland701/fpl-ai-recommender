# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 276.58
- Total actual points: 177.00
- Average predicted points: 69.15
- Average actual points: 44.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 68.03
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.21 | 11.93 | 19.16 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.12 | 0.40 | 0.71 | 0.00 | 5.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.46 | 15.66 | 24.70 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.00 | 14.88 | 23.94 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.93 | 14.00 | 22.34 | 6.00 | 85.9 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.76 | 13.14 | 21.72 | 3.00 | 88.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.41 | 12.08 | 18.98 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.89 | 23.63 | 38.49 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.92 | 16.09 | 25.08 | 9.00 | 89.9 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 4.96 | 14.24 | 21.91 | 1.00 | 74.1 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.28 | 20.18 | 30.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.41 | 17.38 | 28.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.65 | 14.58 | 23.24 | 9.00 | 87.6 | 61.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.35 | 10.43 | 16.74 | 2.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Josh Cullen | MID | 3 | 5.0 | 3.15 | 10.39 | 17.35 | 1.00 | 78.7 | 81.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.23
- Actual score: 33.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 2.95, hit 0)
- Autosub: Jurriën Timber replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.94 | 11.68 | 18.89 | 1.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.17 | 0.34 | 0.70 | 0.00 | 5.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.34 | 17.23 | 27.47 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.25 | 15.05 | 23.66 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 3.92 | 12.18 | 19.82 | 1.00 | 79.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.18 | 11.92 | 19.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.24 | 11.34 | 18.24 | 1.00 | 89.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.49 | 24.50 | 40.03 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.58 | 16.23 | 25.07 | 2.00 | 80.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.78 | 15.04 | 24.01 | 7.00 | 90.0 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.72 | 16.99 | 27.43 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.61 | 14.65 | 22.95 | 7.00 | 70.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.60 | 12.81 | 20.41 | 3.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Josh Cullen | MID | 3 | 5.0 | 2.65 | 9.13 | 14.73 | 10.00 | 69.6 | 90.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.33 | 8.78 | 13.95 | 3.00 | 79.4 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.51
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.79) beats the best remaining Bench Boost opportunity (10.52).
- Transfer: Marc Guéhi -> Nico O'Reilly (projected gain 3.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.79) beats the best remaining Bench Boost opportunity (10.52).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.80 | 11.03 | 17.82 | 2.00 | 83.0 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.03 | 0.29 | 0.00 | 4.9 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.70 | 13.55 | 21.41 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.73 | 12.14 | 19.13 | 3.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.0 | 4.18 | 12.08 | 19.01 | 1.00 | 86.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.44 | 10.98 | 17.75 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 2.70 | 9.37 | 17.01 | 0.00 | 55.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.43 | 24.78 | 40.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.38 | 15.01 | 23.83 | 1.00 | 72.9 | 59.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.49 | 14.93 | 23.19 | 1.00 | 81.6 | 75.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.74 | 18.68 | 29.08 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.36 | 14.79 | 23.90 | 0.00 | 85.0 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.06 | 12.46 | 20.86 | 3.00 | 75.5 | 80.0 |
| Bench 2 | Bench Boost | James Garner | MID | 9 | 5.0 | 3.14 | 9.43 | 15.72 | 6.00 | 76.7 | 90.0 |
| Bench 3 | Bench Boost | Josh Cullen | MID | 3 | 5.0 | 2.95 | 8.95 | 15.07 | 2.00 | 77.0 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.82
- Actual score: 30.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.81) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 5.95, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.81) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.38 | 10.21 | 16.65 | 3.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.08 | 0.22 | 0.38 | 0.00 | 4.6 | 0.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.0 | 4.78 | 13.00 | 19.69 | 4.00 | 88.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.01 | 12.20 | 19.62 | 2.00 | 80.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.83 | 11.25 | 17.93 | 2.00 | 84.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.89 | 11.22 | 18.50 | 0.00 | 87.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 1.21 | 5.77 | 11.55 | 0.00 | 31.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.81 | 25.09 | 40.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.83 | 12.56 | 20.60 | 6.00 | 57.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.92 | 11.48 | 19.11 | 1.00 | 64.1 | 54.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.88 | 15.53 | 23.95 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.79 | 14.61 | 23.49 | 1.00 | 75.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.07 | 10.95 | 18.94 | 2.00 | 67.9 | 79.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.0 | 3.48 | 9.66 | 16.26 | 2.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Josh Cullen | MID | 3 | 5.0 | 2.86 | 8.51 | 13.87 | 2.00 | 77.8 | 80.0 |
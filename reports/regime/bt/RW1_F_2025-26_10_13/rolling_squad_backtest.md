# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 276.80
- Total actual points: 177.00
- Average predicted points: 69.20
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
- Predicted score: 68.09
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.17 | 11.90 | 19.09 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.29 | 0.88 | 1.54 | 0.00 | 5.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.46 | 15.73 | 24.87 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.00 | 14.98 | 23.92 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.90 | 14.04 | 22.51 | 6.00 | 86.8 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.76 | 13.32 | 21.94 | 3.00 | 89.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.28 | 12.08 | 18.84 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.91 | 23.69 | 38.46 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 6.05 | 15.98 | 25.06 | 9.00 | 90.0 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 5.07 | 14.35 | 22.53 | 1.00 | 74.0 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.25 | 20.04 | 30.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.46 | 17.43 | 28.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.63 | 14.68 | 23.54 | 9.00 | 86.9 | 61.0 |
| Bench 4 | Bench | Josh Cullen | MID | 3 | 5.0 | 3.16 | 10.49 | 17.51 | 1.00 | 78.6 | 81.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.31 | 10.44 | 16.90 | 2.00 | 79.3 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.37
- Actual score: 33.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 2.44, hit 0)
- Autosub: Jurriën Timber replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.97 | 11.72 | 19.00 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.27 | 0.79 | 1.44 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.41 | 17.40 | 27.90 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.29 | 15.14 | 23.71 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 3.92 | 12.15 | 19.98 | 1.00 | 80.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.28 | 12.05 | 19.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.25 | 11.27 | 18.15 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.38 | 24.45 | 39.55 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.67 | 16.29 | 25.56 | 2.00 | 80.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.68 | 14.51 | 23.27 | 7.00 | 90.0 | 82.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.71 | 16.93 | 27.19 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.70 | 14.64 | 23.36 | 7.00 | 70.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.64 | 13.03 | 20.61 | 3.00 | 77.4 | 90.0 |
| Bench 4 | Bench | Josh Cullen | MID | 3 | 5.0 | 2.61 | 9.12 | 14.70 | 10.00 | 69.1 | 90.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.31 | 8.76 | 13.92 | 3.00 | 78.8 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.73
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.80) beats the best remaining Bench Boost opportunity (10.53).
- Transfer: Marc Guéhi -> Nico O'Reilly (projected gain 3.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.80) beats the best remaining Bench Boost opportunity (10.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.85 | 11.17 | 17.94 | 2.00 | 84.5 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.52 | 1.24 | 0.00 | 6.1 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.70 | 13.55 | 21.47 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.86 | 12.15 | 19.08 | 3.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.0 | 4.13 | 12.11 | 19.17 | 1.00 | 86.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.47 | 11.02 | 17.84 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 2.71 | 9.70 | 17.21 | 0.00 | 58.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.32 | 24.74 | 40.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.64 | 15.37 | 24.28 | 1.00 | 75.7 | 59.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.42 | 14.64 | 22.73 | 1.00 | 82.1 | 75.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.74 | 18.52 | 28.89 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.31 | 14.73 | 23.58 | 0.00 | 86.2 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.17 | 12.72 | 21.09 | 3.00 | 76.1 | 80.0 |
| Bench 2 | Bench Boost | James Garner | MID | 9 | 5.0 | 3.18 | 9.48 | 15.76 | 6.00 | 77.1 | 90.0 |
| Bench 3 | Bench Boost | Josh Cullen | MID | 3 | 5.0 | 2.91 | 9.10 | 15.16 | 2.00 | 77.1 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.61
- Actual score: 30.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.64) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 5.93, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.64) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.43 | 10.40 | 16.87 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.35 | 0.90 | 1.44 | 0.00 | 6.0 | 0.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.0 | 4.80 | 12.91 | 19.85 | 4.00 | 88.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.05 | 12.25 | 19.93 | 2.00 | 82.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.90 | 11.33 | 18.57 | 0.00 | 88.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.87 | 11.23 | 17.91 | 2.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 1.18 | 5.66 | 11.30 | 0.00 | 34.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.64 | 24.85 | 40.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.96 | 12.86 | 20.60 | 6.00 | 59.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.81 | 11.04 | 18.42 | 1.00 | 64.3 | 54.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.81 | 15.50 | 23.93 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.85 | 14.54 | 23.60 | 1.00 | 76.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.23 | 11.11 | 19.15 | 2.00 | 68.5 | 79.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.0 | 3.51 | 9.65 | 16.26 | 2.00 | 78.5 | 90.0 |
| Bench 3 | Bench | Josh Cullen | MID | 3 | 5.0 | 2.87 | 8.57 | 13.91 | 2.00 | 77.6 | 80.0 |
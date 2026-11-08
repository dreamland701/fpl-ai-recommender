# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 277.71
- Total actual points: 184.00
- Average predicted points: 69.43
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
- Predicted score: 68.72
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.71 | 12.71 | 20.19 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.17 | 0.42 | 0.00 | 1.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.83 | 16.34 | 25.33 | 12.00 | 88.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.05 | 14.89 | 24.01 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.29 | 14.33 | 22.31 | 6.00 | 83.2 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.52 | 12.59 | 20.94 | 3.00 | 88.4 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.41 | 11.83 | 18.98 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.79 | 23.39 | 38.05 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.86 | 16.24 | 25.35 | 9.00 | 90.0 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 4.87 | 14.31 | 21.65 | 1.00 | 73.0 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.04 | 19.48 | 30.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.19 | 16.78 | 28.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.89 | 14.72 | 23.24 | 9.00 | 86.5 | 61.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.0 | 3.66 | 10.69 | 16.66 | 2.00 | 77.2 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.94 | 9.57 | 15.73 | 1.00 | 72.4 | 59.0 |

## GW11

- Train rows: 168588
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.28
- Actual score: 33.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 4.47, hit 0)
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.38 | 12.28 | 19.46 | 1.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.08 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.79 | 18.13 | 28.19 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.20 | 14.87 | 23.50 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.40 | 12.91 | 20.22 | 1.00 | 76.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.24 | 12.16 | 19.76 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 4.14 | 11.20 | 18.31 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.15 | 23.37 | 38.86 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.43 | 16.04 | 24.86 | 2.00 | 81.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.77 | 15.56 | 24.69 | 7.00 | 87.3 | 82.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.79 | 17.05 | 27.72 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.38 | 14.45 | 22.47 | 7.00 | 68.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.62 | 12.59 | 20.44 | 3.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.00 | 9.60 | 15.66 | 1.00 | 68.2 | 73.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.51 | 8.99 | 14.18 | 3.00 | 78.1 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 74.87
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.31) beats the best remaining Bench Boost opportunity (10.78).
- Transfer: Gabriel dos Santos Magalhães -> Virgil van Dijk (projected gain 3.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.31) beats the best remaining Bench Boost opportunity (10.78).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.06 | 11.34 | 18.20 | 2.00 | 82.2 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.07 | 14.00 | 22.17 | 3.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.90 | 13.72 | 21.43 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.94 | 13.09 | 20.56 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.45 | 10.84 | 17.71 | 0.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.49 | 9.00 | 15.03 | 5.00 | 48.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.14 | 23.53 | 38.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.63 | 15.31 | 23.84 | 1.00 | 82.6 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.16 | 14.63 | 23.63 | 1.00 | 71.8 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.65 | 18.54 | 29.08 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.55 | 15.22 | 24.63 | 0.00 | 84.2 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.85 | 11.97 | 20.63 | 3.00 | 75.5 | 80.0 |
| Bench 3 | Bench Boost | James Garner | MID | 9 | 5.0 | 3.00 | 9.07 | 15.36 | 6.00 | 76.3 | 90.0 |
| Bench 4 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.85 | 8.71 | 14.18 | 2.00 | 71.0 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.84
- Actual score: 30.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.92) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Iliman Ndiaye -> Morgan Rogers (projected gain 5.13, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.92) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.30 | 9.73 | 16.12 | 3.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.07 | 11.88 | 18.80 | 2.00 | 82.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.87 | 11.73 | 18.84 | 2.00 | 79.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.04 | 11.69 | 19.34 | 0.00 | 86.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.67 | 11.02 | 18.90 | 6.00 | 67.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.89 | 10.84 | 18.22 | 0.00 | 76.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.92 | 24.86 | 39.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.68 | 12.21 | 20.57 | 6.00 | 54.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.04 | 11.70 | 19.63 | 1.00 | 64.0 | 54.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.96 | 15.54 | 23.82 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.56 | 14.38 | 23.27 | 1.00 | 74.7 | 90.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.0 | 3.37 | 9.37 | 15.87 | 2.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.56 | 8.58 | 14.12 | 0.00 | 78.5 | 0.0 |
| Bench 3 | Bench | Antoine Semenyo | MID | 4 | 7.9 | 2.68 | 8.35 | 15.15 | 1.00 | 33.5 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 277.54
- Total actual points: 184.00
- Average predicted points: 69.38
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
- Predicted score: 68.79
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.67 | 12.71 | 20.20 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.01 | 0.17 | 0.41 | 0.00 | 1.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.81 | 16.35 | 25.34 | 12.00 | 88.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.07 | 14.89 | 24.01 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.25 | 14.33 | 22.32 | 6.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.57 | 12.58 | 20.92 | 3.00 | 88.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.38 | 11.83 | 18.99 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.77 | 23.39 | 38.06 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.90 | 16.24 | 25.34 | 9.00 | 90.0 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 4.94 | 14.31 | 21.63 | 1.00 | 73.1 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.09 | 19.48 | 30.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.23 | 16.78 | 28.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.91 | 14.72 | 23.23 | 9.00 | 86.5 | 61.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.0 | 3.70 | 10.69 | 16.65 | 2.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.00 | 9.56 | 15.71 | 1.00 | 72.5 | 59.0 |

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
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.40 | 12.28 | 19.45 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.03 | 0.00 | 0.07 | 0.00 | 1.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.83 | 18.13 | 28.18 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.18 | 14.87 | 23.50 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.43 | 12.91 | 20.21 | 1.00 | 76.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.32 | 12.16 | 19.73 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.7 | 4.11 | 11.20 | 18.32 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.08 | 23.37 | 38.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.43 | 16.04 | 24.87 | 2.00 | 81.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.63 | 15.57 | 24.73 | 7.00 | 87.1 | 82.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.86 | 17.05 | 27.70 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.37 | 14.46 | 22.48 | 7.00 | 68.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.66 | 12.60 | 20.42 | 3.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.04 | 9.60 | 15.65 | 1.00 | 68.3 | 73.0 |
| Bench 3 | Bench | James Garner | MID | 9 | 5.0 | 3.57 | 8.99 | 14.16 | 3.00 | 78.2 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 74.94
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.35) beats the best remaining Bench Boost opportunity (10.84).
- Transfer: Gabriel dos Santos Magalhães -> Virgil van Dijk (projected gain 5.18, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.35) beats the best remaining Bench Boost opportunity (10.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.07 | 11.34 | 18.20 | 2.00 | 82.2 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.18 | 14.00 | 22.13 | 3.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.92 | 13.72 | 21.42 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.91 | 13.09 | 20.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.56 | 10.83 | 17.68 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 3.47 | 9.00 | 15.03 | 5.00 | 48.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.08 | 23.53 | 38.90 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.54 | 15.32 | 23.87 | 1.00 | 82.4 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.16 | 14.63 | 23.64 | 1.00 | 71.8 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.68 | 18.54 | 29.07 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.49 | 15.22 | 24.64 | 0.00 | 84.1 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.89 | 11.97 | 20.62 | 3.00 | 75.6 | 80.0 |
| Bench 3 | Bench Boost | James Garner | MID | 9 | 5.0 | 3.05 | 9.07 | 15.35 | 6.00 | 76.4 | 90.0 |
| Bench 4 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.84 | 8.71 | 14.18 | 2.00 | 71.0 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.53
- Actual score: 30.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.87) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Iliman Ndiaye -> Morgan Rogers (projected gain 5.14, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.87) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.23 | 9.73 | 16.14 | 3.00 | 80.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.11 | 11.88 | 18.79 | 2.00 | 82.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.81 | 11.73 | 18.86 | 2.00 | 79.4 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.07 | 11.69 | 19.33 | 0.00 | 86.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.75 | 11.03 | 18.88 | 6.00 | 67.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.88 | 10.84 | 18.23 | 0.00 | 76.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.87 | 24.86 | 39.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.66 | 12.21 | 20.57 | 6.00 | 54.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.04 | 11.70 | 19.63 | 1.00 | 64.0 | 54.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.86 | 15.54 | 23.85 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.50 | 14.38 | 23.29 | 1.00 | 74.6 | 90.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.0 | 3.39 | 9.37 | 15.86 | 2.00 | 77.2 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.61 | 8.57 | 14.10 | 0.00 | 78.6 | 0.0 |
| Bench 3 | Bench | Antoine Semenyo | MID | 4 | 7.9 | 2.68 | 8.35 | 15.15 | 1.00 | 33.5 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 286.69
- Total actual points: 193.00
- Average predicted points: 71.67
- Average actual points: 48.25
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
- Predicted score: 68.94
- Actual score: 92.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.32 | 12.02 | 19.18 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.16 | 0.64 | 1.26 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.47 | 15.57 | 24.43 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.97 | 14.73 | 23.83 | 10.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.76 | 13.03 | 21.68 | 3.00 | 88.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.58 | 12.24 | 19.18 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.45 | 10.56 | 17.15 | 6.00 | 81.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.26 | 24.22 | 39.82 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.93 | 16.42 | 25.76 | 9.00 | 90.0 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 5.04 | 14.54 | 22.43 | 1.00 | 80.7 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.22 | 20.04 | 31.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.51 | 17.54 | 29.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.61 | 14.37 | 22.91 | 9.00 | 87.3 | 61.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.77 | 13.85 | 22.78 | 13.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.24 | 10.42 | 16.94 | 1.00 | 74.0 | 59.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 69.30
- Actual score: 34.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 6.42, hit 0)
- Autosub: Marcos Senesi Barón replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.01 | 11.79 | 18.92 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.15 | 0.57 | 1.18 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.31 | 17.17 | 27.29 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.25 | 15.01 | 23.64 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.16 | 11.97 | 19.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.28 | 11.50 | 18.39 | 1.00 | 88.6 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.68 | 11.09 | 17.32 | 8.00 | 82.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.98 | 25.24 | 41.51 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 6.81 | 18.30 | 29.02 | 7.00 | 90.0 | 82.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.67 | 16.64 | 25.65 | 2.00 | 85.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.80 | 17.20 | 27.71 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.51 | 16.89 | 26.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.45 | 14.72 | 22.89 | 7.00 | 66.2 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.25 | 11.95 | 19.95 | 3.00 | 74.1 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.23 | 10.46 | 16.86 | 1.00 | 70.9 | 73.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 78.01
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.17) beats the best remaining Bench Boost opportunity (11.81).
- Transfer: Gabriel dos Santos Magalhães -> Jurriën Timber (projected gain 4.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.17) beats the best remaining Bench Boost opportunity (11.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.10 | 11.47 | 18.70 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.27 | 0.89 | 0.00 | 1.9 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.67 | 13.41 | 21.11 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.72 | 12.36 | 19.55 | 3.00 | 90.0 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.5 | 4.40 | 11.34 | 18.75 | 6.00 | 84.9 | 82.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.47 | 11.04 | 17.77 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 3.73 | 9.57 | 15.71 | 5.00 | 52.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.84 | 25.26 | 41.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.91 | 15.97 | 24.91 | 1.00 | 89.7 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.52 | 15.59 | 24.91 | 1.00 | 79.4 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.84 | 19.10 | 30.06 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.99 | 14.90 | 22.73 | 6.00 | 82.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 4.95 | 14.04 | 24.06 | 0.00 | 75.4 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.07 | 12.53 | 21.02 | 3.00 | 76.7 | 80.0 |
| Bench 4 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.97 | 9.11 | 14.69 | 2.00 | 73.3 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.43
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.94) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Iliman Ndiaye -> Morgan Rogers (projected gain 4.57, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.94) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.65 | 10.65 | 17.58 | 3.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.21 | 0.60 | 1.07 | 0.00 | 1.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.98 | 12.22 | 19.37 | 2.00 | 79.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.88 | 11.47 | 18.27 | 2.00 | 84.8 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.93 | 11.30 | 18.67 | 0.00 | 86.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.09 | 11.28 | 18.64 | 0.00 | 77.0 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.58 | 10.04 | 16.55 | 1.00 | 80.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.94 | 24.83 | 40.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.98 | 12.86 | 21.35 | 6.00 | 59.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.27 | 12.43 | 20.43 | 1.00 | 67.0 | 54.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 6.02 | 15.69 | 24.39 | 3.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.04 | 15.65 | 24.01 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.77 | 14.89 | 23.85 | 1.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.38 | 8.38 | 13.92 | 0.00 | 69.3 | 0.0 |
| Bench 4 | Bench | Antoine Semenyo | MID | 4 | 7.9 | 2.07 | 7.09 | 14.75 | 1.00 | 27.5 | 90.0 |
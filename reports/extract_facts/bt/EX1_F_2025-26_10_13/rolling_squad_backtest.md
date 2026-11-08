# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 286.42
- Total actual points: 193.00
- Average predicted points: 71.60
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
- Predicted score: 69.03
- Actual score: 92.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.29 | 11.99 | 19.20 | 6.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.32 | 0.90 | 1.59 | 0.00 | 5.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.44 | 15.53 | 24.42 | 12.00 | 89.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.96 | 14.72 | 23.78 | 10.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.73 | 12.98 | 21.51 | 3.00 | 87.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.56 | 12.21 | 19.22 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.43 | 10.52 | 17.09 | 6.00 | 81.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.29 | 24.27 | 39.93 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.96 | 16.49 | 25.89 | 9.00 | 90.0 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 5.05 | 14.56 | 22.43 | 1.00 | 81.0 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.35 | 20.28 | 31.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.47 | 17.48 | 28.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.61 | 14.36 | 22.82 | 9.00 | 87.3 | 61.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.76 | 13.84 | 22.74 | 13.00 | 82.3 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.19 | 10.34 | 16.83 | 1.00 | 72.6 | 59.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 69.20
- Actual score: 34.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 6.44, hit 0)
- Autosub: Marcos Senesi Barón replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.98 | 11.75 | 18.92 | 1.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.31 | 0.82 | 1.50 | 0.00 | 6.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.27 | 17.13 | 27.20 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.23 | 14.99 | 23.61 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.15 | 11.95 | 19.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.27 | 11.49 | 18.43 | 1.00 | 88.2 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.64 | 11.04 | 17.20 | 8.00 | 81.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.99 | 25.28 | 41.58 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 6.76 | 18.30 | 29.10 | 7.00 | 90.0 | 82.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.70 | 16.70 | 25.73 | 2.00 | 86.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.77 | 17.15 | 27.68 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.53 | 16.92 | 26.40 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.52 | 14.85 | 22.94 | 7.00 | 68.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.16 | 11.93 | 20.10 | 3.00 | 71.8 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.18 | 10.39 | 16.77 | 1.00 | 69.4 | 73.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 77.92
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.03) beats the best remaining Bench Boost opportunity (11.65).
- Transfer: Gabriel dos Santos Magalhães -> Jurriën Timber (projected gain 4.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.03) beats the best remaining Bench Boost opportunity (11.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.08 | 11.45 | 18.71 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.52 | 1.20 | 0.00 | 6.4 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.65 | 13.38 | 21.10 | 5.00 | 89.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.69 | 12.31 | 19.50 | 3.00 | 90.0 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.5 | 4.35 | 11.27 | 18.69 | 6.00 | 83.7 | 82.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.45 | 11.01 | 17.75 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 3.64 | 9.45 | 15.60 | 5.00 | 49.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.87 | 25.33 | 41.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.91 | 15.99 | 24.94 | 1.00 | 89.5 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.51 | 15.58 | 24.91 | 1.00 | 79.0 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.95 | 19.28 | 30.16 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.99 | 14.91 | 22.72 | 6.00 | 82.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.00 | 13.74 | 23.30 | 0.00 | 76.9 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.03 | 12.48 | 20.99 | 3.00 | 75.7 | 80.0 |
| Bench 4 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.94 | 9.07 | 14.65 | 2.00 | 72.4 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.28
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.96) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Iliman Ndiaye -> Morgan Rogers (projected gain 4.68, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.96) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.63 | 10.62 | 17.59 | 3.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.36 | 0.85 | 1.37 | 0.00 | 6.3 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.95 | 12.18 | 19.37 | 2.00 | 78.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.86 | 11.43 | 18.24 | 2.00 | 84.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.89 | 11.23 | 18.61 | 0.00 | 85.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.03 | 11.18 | 18.57 | 0.00 | 75.5 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.55 | 10.00 | 16.53 | 1.00 | 80.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.96 | 24.87 | 40.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.92 | 12.78 | 21.30 | 6.00 | 58.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.22 | 12.38 | 20.40 | 1.00 | 65.6 | 54.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 6.04 | 15.72 | 24.42 | 3.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.05 | 15.68 | 24.04 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.81 | 14.98 | 23.85 | 1.00 | 74.6 | 90.0 |
| Bench 3 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.77 | 9.20 | 14.84 | 0.00 | 77.9 | 0.0 |
| Bench 4 | Bench | Antoine Semenyo | MID | 4 | 7.9 | 1.99 | 6.56 | 13.78 | 1.00 | 25.9 | 90.0 |
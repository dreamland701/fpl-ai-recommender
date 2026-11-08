# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 266.25
- Total actual points: 188.00
- Average predicted points: 66.56
- Average actual points: 47.00
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
- Predicted score: 66.64
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 5.13 | 14.17 | 22.52 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 5.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 6.07 | 16.38 | 27.27 | 12.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.68 | 14.95 | 24.27 | 6.00 | 85.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.93 | 13.56 | 21.65 | 10.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.53 | 12.20 | 18.55 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.35 | 9.56 | 16.60 | 1.00 | 78.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.32 | 21.22 | 35.97 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 4.49 | 13.19 | 22.71 | 9.00 | 88.9 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.82 | 11.47 | 14.40 | 2.00 | 81.9 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 6.78 | 19.51 | 30.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 4.93 | 16.79 | 26.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.26 | 14.33 | 23.49 | 9.00 | 87.7 | 61.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.22 | 14.02 | 22.60 | 5.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.60 | 9.94 | 15.48 | 1.00 | 72.8 | 59.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.46
- Actual score: 29.00
- Transfer: Iliman Ndiaye -> Moisés Caicedo Corozo (projected gain 0.20, hit 0)
- Autosub: Sean Longstaff replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.46 | 13.53 | 21.67 | 1.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 6.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.64 | 17.57 | 27.31 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.10 | 13.64 | 20.60 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.20 | 13.40 | 21.89 | 1.00 | 78.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.11 | 11.75 | 18.97 | 1.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.61 | 8.71 | 14.35 | 4.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.51 | 21.17 | 34.17 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.32 | 13.78 | 22.62 | 2.00 | 79.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.18 | 8.23 | 15.28 | 1.00 | 67.9 | 27.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.52 | 16.13 | 26.07 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.87 | 14.99 | 23.57 | 7.00 | 68.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.01 | 13.86 | 22.78 | 5.00 | 84.6 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.20 | 12.83 | 19.19 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Sean Longstaff | MID | 11 | 4.9 | 2.71 | 10.08 | 16.73 | 1.00 | 69.3 | 73.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 71.70
- Actual score: 31.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.01) beats the best remaining Bench Boost opportunity (9.13).
- Transfer: Gabriel dos Santos Magalhães -> Virgil van Dijk (projected gain 7.78, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.01) beats the best remaining Bench Boost opportunity (9.13).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.87 | 12.15 | 19.91 | 2.00 | 82.1 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 5.1 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.30 | 15.15 | 23.78 | 5.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.54 | 14.34 | 22.69 | 3.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.21 | 11.01 | 17.43 | 0.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.1 | 3.85 | 9.73 | 15.89 | 4.00 | 77.6 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 2.94 | 6.75 | 11.69 | 5.00 | 49.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.55 | 20.83 | 33.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.48 | 14.86 | 23.49 | 1.00 | 70.8 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.50 | 8.04 | 11.67 | 2.00 | 40.7 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.54 | 18.33 | 28.28 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.72 | 15.27 | 23.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.49 | 14.67 | 23.88 | 0.00 | 85.1 | 0.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.58 | 11.89 | 17.60 | 0.00 | 78.9 | 0.0 |
| Bench 3 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.58 | 8.27 | 13.40 | 2.00 | 72.6 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 1.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 64.45
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.52) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Moisés Caicedo Corozo -> Declan Rice (projected gain 6.89, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.52) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.00 | 12.24 | 19.83 | 3.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 4.8 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.32 | 13.89 | 21.70 | 2.00 | 78.8 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.36 | 11.09 | 17.98 | 0.00 | 85.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.45 | 10.27 | 17.16 | 6.00 | 69.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.81 | 9.91 | 16.61 | 0.00 | 75.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.1 | 3.59 | 9.75 | 15.39 | 0.00 | 80.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.52 | 20.24 | 33.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.58 | 12.70 | 20.87 | 6.00 | 56.9 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.62 | 8.65 | 15.09 | 1.00 | 52.7 | 10.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 5.22 | 15.17 | 22.60 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.99 | 14.71 | 23.68 | 1.00 | 74.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.56 | 14.29 | 24.89 | 11.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Antoine Semenyo | MID | 4 | 7.9 | 2.87 | 8.62 | 15.66 | 1.00 | 40.7 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.47 | 8.31 | 13.57 | 0.00 | 78.2 | 0.0 |
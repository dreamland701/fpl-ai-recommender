# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 278.27
- Total actual points: 212.00
- Average predicted points: 69.57
- Average actual points: 53.00
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
- Predicted score: 67.01
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.31 | 11.96 | 19.05 | 6.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.24 | 0.84 | 1.14 | 0.00 | 5.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.50 | 15.60 | 24.44 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.95 | 14.69 | 23.83 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.72 | 12.99 | 21.56 | 3.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.39 | 9.57 | 14.94 | 1.00 | 78.8 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.81 | 9.00 | 14.89 | 1.00 | 80.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.96 | 23.69 | 38.71 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.74 | 16.18 | 25.12 | 9.00 | 88.8 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.36 | 10.81 | 17.08 | 2.00 | 81.6 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.18 | 19.99 | 30.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.48 | 17.51 | 29.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.73 | 14.78 | 23.31 | 9.00 | 87.5 | 61.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.95 | 14.20 | 22.95 | 5.00 | 80.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.50 | 13.38 | 21.53 | 13.00 | 73.3 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.58
- Actual score: 34.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.02 | 11.83 | 18.82 | 1.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.20 | 0.47 | 0.94 | 0.00 | 6.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.36 | 17.29 | 27.26 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.22 | 14.95 | 23.61 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.13 | 11.92 | 19.41 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.71 | 8.93 | 14.61 | 4.00 | 77.0 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 2.99 | 8.42 | 13.42 | 3.00 | 84.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.67 | 24.60 | 40.44 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.45 | 16.29 | 24.95 | 2.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.18 | 10.15 | 15.99 | 1.00 | 67.6 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.78 | 17.15 | 27.81 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.34 | 16.67 | 25.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.54 | 14.98 | 23.12 | 7.00 | 68.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.88 | 14.25 | 23.58 | 5.00 | 85.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.54 | 12.72 | 20.45 | 3.00 | 78.1 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 74.15
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.84) beats the best remaining Bench Boost opportunity (10.59).
- Transfer: Gabriel dos Santos Magalhães -> Jurriën Timber (projected gain 3.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.84) beats the best remaining Bench Boost opportunity (10.59).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.74 | 10.86 | 17.58 | 2.00 | 82.0 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.15 | 0.49 | 0.00 | 5.3 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.64 | 13.41 | 21.07 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.68 | 12.32 | 19.66 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.30 | 9.55 | 16.71 | 4.00 | 78.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.55 | 9.18 | 15.37 | 5.00 | 49.5 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 2.94 | 8.30 | 13.47 | 3.00 | 83.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.54 | 24.60 | 40.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.14 | 14.86 | 23.83 | 1.00 | 71.0 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.60 | 8.08 | 13.77 | 2.00 | 40.3 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.71 | 18.95 | 29.59 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.37 | 15.40 | 24.40 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.95 | 14.89 | 22.68 | 6.00 | 82.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.45 | 14.88 | 24.39 | 0.00 | 85.0 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.00 | 12.48 | 21.05 | 3.00 | 75.8 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.30 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.53
- Actual score: 40.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.03) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 5.62, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.03) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.30 | 9.95 | 16.30 | 3.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.12 | 0.26 | 0.54 | 0.00 | 4.8 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.91 | 12.06 | 19.18 | 2.00 | 78.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.93 | 11.69 | 18.42 | 2.00 | 83.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.97 | 11.08 | 18.45 | 0.00 | 75.7 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.49 | 9.72 | 15.62 | 0.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.05 | 8.74 | 13.78 | 3.00 | 84.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 9.03 | 25.26 | 40.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.77 | 12.49 | 20.93 | 6.00 | 57.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.49 | 9.56 | 15.82 | 1.00 | 51.9 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.01 | 15.54 | 23.88 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.82 | 15.28 | 23.73 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.78 | 14.99 | 23.92 | 1.00 | 74.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.93 | 14.60 | 24.69 | 11.00 | 85.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.00 | 10.96 | 19.12 | 2.00 | 68.3 | 79.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 279.61
- Total actual points: 219.00
- Average predicted points: 69.90
- Average actual points: 54.75
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
- Predicted score: 66.89
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.30 | 11.99 | 19.24 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.32 | 0.92 | 1.64 | 0.00 | 5.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.46 | 15.50 | 24.38 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.96 | 14.66 | 23.70 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.70 | 12.88 | 21.39 | 3.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.55 | 10.08 | 15.80 | 1.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.89 | 9.24 | 15.41 | 1.00 | 80.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.91 | 23.43 | 38.15 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.82 | 16.49 | 25.66 | 9.00 | 89.4 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.36 | 10.73 | 16.97 | 2.00 | 82.0 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.18 | 19.92 | 30.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.50 | 17.61 | 29.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.01 | 14.67 | 23.60 | 5.00 | 81.1 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.54 | 14.18 | 22.49 | 9.00 | 87.2 | 61.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.59 | 13.76 | 22.38 | 13.00 | 74.2 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.45
- Actual score: 34.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.98 | 11.73 | 18.93 | 1.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.31 | 0.84 | 1.54 | 0.00 | 6.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.29 | 17.05 | 27.08 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.23 | 14.90 | 23.46 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.13 | 11.84 | 19.18 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.82 | 9.30 | 15.36 | 4.00 | 76.5 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.12 | 8.81 | 13.97 | 3.00 | 84.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.61 | 24.38 | 39.92 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.52 | 16.56 | 25.47 | 2.00 | 79.6 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.19 | 10.14 | 15.87 | 1.00 | 67.9 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.82 | 17.31 | 28.07 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.40 | 16.93 | 26.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.48 | 14.49 | 22.30 | 7.00 | 67.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.90 | 14.46 | 24.00 | 5.00 | 85.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.47 | 12.45 | 19.89 | 3.00 | 77.6 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.29
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.10) beats the best remaining Bench Boost opportunity (10.90).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 3.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.10) beats the best remaining Bench Boost opportunity (10.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.78 | 10.91 | 17.76 | 2.00 | 82.1 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.54 | 1.24 | 0.00 | 6.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.14 | 13.51 | 22.70 | 14.00 | 88.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.69 | 12.25 | 19.40 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.46 | 10.05 | 17.54 | 4.00 | 77.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.59 | 9.24 | 15.29 | 5.00 | 48.9 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.01 | 8.51 | 13.89 | 3.00 | 82.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.52 | 24.50 | 39.90 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.27 | 15.26 | 24.49 | 1.00 | 71.2 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.62 | 8.07 | 13.62 | 2.00 | 40.6 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.70 | 18.70 | 29.04 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.42 | 15.74 | 24.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.11 | 15.33 | 23.55 | 6.00 | 83.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.50 | 15.05 | 24.64 | 0.00 | 85.2 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.95 | 12.24 | 20.60 | 3.00 | 75.2 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Eberechi Eze
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.98
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.92) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 5.96, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.92) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.34 | 10.05 | 16.52 | 3.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.36 | 0.86 | 1.40 | 0.00 | 6.3 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.10 | 13.86 | 22.63 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.81 | 11.25 | 17.93 | 2.00 | 83.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.99 | 11.01 | 18.30 | 0.00 | 74.9 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.64 | 10.17 | 16.34 | 0.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.14 | 9.03 | 14.21 | 3.00 | 84.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.92 | 24.86 | 39.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.88 | 12.79 | 21.55 | 6.00 | 57.3 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.40 | 9.20 | 15.43 | 1.00 | 52.6 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.15 | 16.06 | 24.79 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 1 | 7.7 | 5.28 | 16.05 | 25.71 | 2.00 | 90.0 | 71.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.97 | 14.90 | 25.23 | 11.00 | 85.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.74 | 14.62 | 23.25 | 1.00 | 73.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.95 | 10.83 | 18.79 | 2.00 | 67.8 | 79.0 |
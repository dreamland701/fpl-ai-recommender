# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 275.03
- Total actual points: 201.00
- Average predicted points: 68.76
- Average actual points: 50.25
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
- Predicted score: 67.51
- Actual score: 90.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.33 | 11.92 | 19.43 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.11 | 0.32 | 0.76 | 0.00 | 1.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.45 | 15.50 | 24.51 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.04 | 14.85 | 23.93 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.95 | 13.43 | 21.51 | 6.00 | 84.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.71 | 13.17 | 21.55 | 3.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.88 | 9.34 | 15.29 | 1.00 | 80.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.95 | 23.93 | 39.36 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.84 | 15.52 | 24.25 | 9.00 | 90.0 | 89.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.58 | 10.96 | 17.13 | 2.00 | 86.6 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.34 | 19.87 | 30.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.53 | 18.05 | 29.77 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.57 | 14.23 | 22.41 | 9.00 | 86.7 | 61.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.85 | 14.10 | 22.70 | 5.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 2.18 | 5.86 | 8.94 | 3.00 | 48.6 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.70
- Actual score: 31.00
- Transfer: Jurriën Timber -> Reece James (projected gain 0.53, hit 0)
- Autosub: Junior Kroupi replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.00 | 11.64 | 18.89 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.10 | 0.30 | 0.64 | 0.00 | 2.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.31 | 17.15 | 27.15 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.30 | 15.05 | 23.80 | 0.00 | 90.0 | 0.0 |
| XI | XI | Reece James | DEF | 7 | 5.5 | 4.47 | 12.44 | 19.47 | 1.00 | 81.5 | 13.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.17 | 12.18 | 19.66 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 4.0 | 3.16 | 8.95 | 14.11 | 3.00 | 85.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.67 | 25.08 | 41.34 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.48 | 15.29 | 23.51 | 2.00 | 79.4 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.36 | 10.22 | 15.76 | 1.00 | 71.3 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.90 | 17.79 | 28.83 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.46 | 13.92 | 21.33 | 7.00 | 67.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.75 | 13.79 | 22.93 | 5.00 | 82.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.50 | 12.47 | 20.07 | 3.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 2.29 | 6.49 | 10.15 | 2.00 | 59.9 | 74.0 |

## GW12

- Train rows: 169340
- Bank: 0.60 -> 1.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 72.13
- Actual score: 42.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.05) beats the best remaining Bench Boost opportunity (9.36).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 4.56, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.05) beats the best remaining Bench Boost opportunity (9.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.80 | 11.02 | 17.92 | 2.00 | 82.4 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.02 | 0.34 | 0.00 | 2.2 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.13 | 13.45 | 22.78 | 14.00 | 87.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.79 | 12.54 | 19.95 | 3.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.51 | 9.40 | 15.71 | 5.00 | 47.2 | 90.0 |
| Bench 2 | Bench Boost | Reece James | DEF | 7 | 5.5 | 3.00 | 9.02 | 15.58 | 1.00 | 50.7 | 45.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.11 | 8.81 | 14.21 | 3.00 | 84.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.56 | 25.05 | 41.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.17 | 14.50 | 23.20 | 1.00 | 69.9 | 59.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.66 | 7.73 | 12.90 | 2.00 | 41.3 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.77 | 18.73 | 29.30 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.47 | 15.47 | 25.21 | 0.00 | 85.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.30 | 15.18 | 24.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.91 | 12.07 | 20.47 | 3.00 | 73.6 | 80.0 |
| Bench 4 | Bench Boost | Carlos Baleba | MID | 6 | 4.7 | 2.40 | 6.73 | 10.36 | 1.00 | 57.2 | 45.0 |

## GW13

- Train rows: 170095
- Bank: 1.30 -> 2.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.68
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 6.64, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.06) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.34 | 10.17 | 16.81 | 3.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.14 | 0.28 | 0.53 | 0.00 | 2.0 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.10 | 13.73 | 22.66 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.83 | 11.50 | 18.30 | 2.00 | 83.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.01 | 11.12 | 18.66 | 0.00 | 75.2 | 90.0 |
| XI | XI | Maxime Estève | DEF | 3 | 3.9 | 3.21 | 9.15 | 14.37 | 3.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Reece James | DEF | 7 | 5.5 | 2.58 | 8.78 | 14.72 | 8.00 | 58.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 9.06 | 25.45 | 41.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.68 | 12.16 | 20.35 | 6.00 | 53.9 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.42 | 8.86 | 14.63 | 1.00 | 53.0 | 10.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.91 | 15.42 | 23.84 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.71 | 14.67 | 23.30 | 1.00 | 73.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.79 | 14.31 | 24.25 | 11.00 | 81.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.93 | 10.78 | 18.91 | 2.00 | 66.5 | 79.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 1.92 | 5.95 | 9.64 | 1.00 | 50.4 | 6.0 |
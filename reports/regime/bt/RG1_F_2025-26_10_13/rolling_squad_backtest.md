# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 275.55
- Total actual points: 205.00
- Average predicted points: 68.89
- Average actual points: 51.25
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
- Predicted score: 67.19
- Actual score: 90.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.25 | 11.73 | 18.56 | 6.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.14 | 0.43 | 0.51 | 0.00 | 3.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.54 | 15.86 | 25.01 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.97 | 14.81 | 24.11 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.14 | 14.39 | 22.82 | 6.00 | 86.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.71 | 12.95 | 21.66 | 3.00 | 88.3 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.93 | 9.42 | 15.87 | 1.00 | 80.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.97 | 23.65 | 38.48 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.78 | 16.22 | 24.94 | 9.00 | 88.4 | 89.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.27 | 10.42 | 16.42 | 2.00 | 80.9 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.18 | 20.04 | 30.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.25 | 16.75 | 27.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.96 | 14.26 | 22.80 | 5.00 | 79.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.49 | 13.96 | 22.22 | 9.00 | 86.8 | 61.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 2.11 | 5.74 | 8.64 | 3.00 | 48.5 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.96
- Actual score: 33.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.96 | 11.56 | 18.37 | 1.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.23 | 0.44 | 0.62 | 0.00 | 4.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.33 | 17.34 | 27.62 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.24 | 15.03 | 23.78 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.11 | 12.78 | 20.53 | 1.00 | 79.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.11 | 11.87 | 19.26 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.17 | 9.01 | 14.33 | 3.00 | 84.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.65 | 24.64 | 40.38 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.47 | 16.38 | 24.97 | 2.00 | 78.9 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.09 | 9.85 | 15.31 | 1.00 | 67.1 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.61 | 16.52 | 26.60 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.52 | 14.79 | 22.94 | 7.00 | 68.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.85 | 14.02 | 23.20 | 5.00 | 84.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.46 | 12.31 | 19.72 | 3.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 2.24 | 6.43 | 9.94 | 2.00 | 60.0 | 74.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.55
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.92) beats the best remaining Bench Boost opportunity (9.34).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 5.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.92) beats the best remaining Bench Boost opportunity (9.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.77 | 10.78 | 17.30 | 2.00 | 80.6 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.17 | 0.28 | 0.00 | 4.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.80 | 13.88 | 21.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.20 | 13.80 | 23.27 | 14.00 | 89.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.69 | 12.31 | 19.53 | 3.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.63 | 9.45 | 15.73 | 5.00 | 49.9 | 90.0 |
| Bench 2 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.05 | 8.64 | 14.12 | 3.00 | 83.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.53 | 24.69 | 40.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.18 | 14.97 | 23.82 | 1.00 | 70.7 | 59.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.50 | 7.74 | 12.94 | 2.00 | 39.9 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.69 | 18.76 | 29.21 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.37 | 15.27 | 24.08 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.32 | 14.36 | 23.35 | 0.00 | 85.7 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.93 | 12.13 | 20.43 | 3.00 | 75.3 | 80.0 |
| Bench 4 | Bench Boost | Carlos Baleba | MID | 6 | 4.7 | 2.37 | 6.63 | 10.22 | 1.00 | 57.7 | 45.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Daniel Muñoz Mejía
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.85
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.97) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 6.33, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.97) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.34 | 9.96 | 16.17 | 3.00 | 78.4 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.17 | 0.41 | 0.53 | 0.00 | 3.9 | 0.0 |
| Vice Captain | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.19 | 14.23 | 23.33 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.06 | 12.55 | 20.10 | 2.00 | 79.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.82 | 11.33 | 18.14 | 2.00 | 84.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.02 | 11.17 | 18.65 | 0.00 | 76.0 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.16 | 9.08 | 14.33 | 3.00 | 84.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.97 | 25.18 | 40.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.75 | 12.34 | 20.69 | 6.00 | 57.2 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.31 | 8.96 | 15.04 | 1.00 | 52.2 | 10.0 |
| XI | XI | Eberechi Eze | MID | 1 | 7.7 | 5.16 | 15.36 | 24.44 | 2.00 | 90.0 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.75 | 14.79 | 23.56 | 1.00 | 74.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.93 | 14.49 | 24.48 | 11.00 | 84.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.92 | 10.69 | 18.57 | 2.00 | 67.6 | 79.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 1.91 | 5.89 | 9.57 | 1.00 | 51.1 | 6.0 |
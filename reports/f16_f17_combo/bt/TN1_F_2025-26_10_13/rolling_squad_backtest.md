# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 280.74
- Total actual points: 219.00
- Average predicted points: 70.18
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
- Predicted score: 67.09
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.33 | 12.03 | 19.23 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.21 | 0.45 | 0.00 | 1.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.50 | 15.64 | 24.62 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.98 | 14.77 | 23.96 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.75 | 13.01 | 21.75 | 3.00 | 88.2 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.58 | 10.14 | 15.81 | 1.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.92 | 9.32 | 15.63 | 1.00 | 81.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.00 | 23.77 | 38.77 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.75 | 16.20 | 25.05 | 9.00 | 88.6 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.36 | 10.76 | 17.10 | 2.00 | 82.3 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.16 | 20.06 | 30.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.51 | 17.55 | 29.12 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.61 | 14.38 | 22.98 | 9.00 | 87.6 | 61.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.98 | 14.32 | 22.92 | 5.00 | 80.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.52 | 13.45 | 21.81 | 13.00 | 74.6 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.73
- Actual score: 34.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.01 | 11.78 | 18.94 | 1.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.05 | 0.16 | 0.49 | 0.00 | 1.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.33 | 17.22 | 27.47 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.26 | 15.02 | 23.74 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.16 | 11.95 | 19.38 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.86 | 9.36 | 15.43 | 4.00 | 77.4 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.15 | 8.85 | 14.06 | 3.00 | 85.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.71 | 24.74 | 40.57 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.46 | 16.29 | 24.92 | 2.00 | 79.0 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.18 | 10.12 | 15.92 | 1.00 | 67.9 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.82 | 17.23 | 27.82 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.29 | 16.55 | 25.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.53 | 14.82 | 22.94 | 7.00 | 68.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.88 | 14.14 | 23.39 | 5.00 | 85.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.56 | 12.66 | 20.28 | 3.00 | 78.7 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.46
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.05) beats the best remaining Bench Boost opportunity (10.84).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 3.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.05) beats the best remaining Bench Boost opportunity (10.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.83 | 10.99 | 17.82 | 2.00 | 83.3 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.08 | 0.00 | 0.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.20 | 13.65 | 22.92 | 14.00 | 89.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.74 | 12.39 | 19.63 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.51 | 10.15 | 17.68 | 4.00 | 78.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.71 | 9.51 | 15.65 | 5.00 | 51.9 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.06 | 8.59 | 13.99 | 3.00 | 83.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.59 | 24.77 | 40.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.27 | 15.08 | 24.03 | 1.00 | 72.0 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.48 | 7.86 | 13.41 | 2.00 | 36.3 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.73 | 18.91 | 29.49 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.39 | 15.38 | 24.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.33 | 15.10 | 25.07 | 0.00 | 81.4 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.99 | 14.90 | 22.78 | 6.00 | 83.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.05 | 12.47 | 21.01 | 3.00 | 76.8 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Eberechi Eze
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.45
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.99) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 5.39, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.99) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.39 | 10.15 | 16.59 | 3.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.04 | 0.20 | 0.00 | 0.3 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.14 | 13.99 | 22.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.86 | 11.40 | 18.19 | 2.00 | 84.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.08 | 11.23 | 18.61 | 0.00 | 77.1 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.66 | 10.23 | 16.41 | 0.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.17 | 9.08 | 14.27 | 3.00 | 85.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.99 | 25.15 | 40.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.91 | 12.66 | 21.12 | 6.00 | 59.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.26 | 9.03 | 15.31 | 1.00 | 48.4 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.03 | 15.63 | 24.02 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 1 | 7.7 | 5.22 | 15.54 | 24.77 | 2.00 | 90.0 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.82 | 14.95 | 23.83 | 1.00 | 75.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.96 | 14.57 | 24.64 | 11.00 | 85.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.07 | 11.07 | 19.17 | 2.00 | 69.8 | 79.0 |
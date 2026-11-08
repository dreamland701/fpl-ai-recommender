# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 279.22
- Total actual points: 213.00
- Average predicted points: 69.81
- Average actual points: 53.25
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
- Predicted score: 67.11
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.32 | 12.01 | 19.19 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.17 | 0.65 | 1.28 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.47 | 15.58 | 24.54 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.97 | 14.77 | 23.93 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.76 | 13.07 | 21.80 | 3.00 | 88.4 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.57 | 10.11 | 15.80 | 1.00 | 78.5 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.94 | 9.35 | 15.67 | 1.00 | 81.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.80 | 22.98 | 38.55 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.92 | 16.63 | 25.88 | 9.00 | 90.0 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.35 | 10.75 | 17.02 | 2.00 | 82.0 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 6.95 | 19.60 | 30.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.52 | 17.57 | 29.12 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.09 | 14.88 | 24.10 | 13.00 | 82.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.60 | 14.37 | 22.92 | 9.00 | 87.5 | 61.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.92 | 14.22 | 22.90 | 5.00 | 77.9 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.51
- Actual score: 33.00
- Transfer: Iliman Ndiaye -> Moisés Caicedo Corozo (projected gain 2.79, hit 0)
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.00 | 11.78 | 18.91 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.16 | 0.58 | 1.20 | 0.00 | 1.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.31 | 17.18 | 27.37 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.26 | 15.03 | 23.73 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.17 | 11.99 | 19.42 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.86 | 9.39 | 15.46 | 4.00 | 77.5 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.15 | 8.86 | 14.06 | 3.00 | 85.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.73 | 24.81 | 40.60 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.42 | 16.22 | 24.76 | 2.00 | 78.0 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.97 | 9.81 | 15.27 | 1.00 | 62.8 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.81 | 17.21 | 27.75 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.24 | 16.43 | 25.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.45 | 14.72 | 22.89 | 7.00 | 66.5 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.59 | 14.41 | 22.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.80 | 14.03 | 23.36 | 5.00 | 82.9 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.58
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.27) beats the best remaining Bench Boost opportunity (9.89).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 4.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.27) beats the best remaining Bench Boost opportunity (9.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.84 | 11.02 | 17.82 | 2.00 | 83.2 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.28 | 0.91 | 0.00 | 1.9 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.17 | 13.62 | 22.87 | 14.00 | 89.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.72 | 12.38 | 19.59 | 3.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.1 | 3.50 | 10.15 | 17.69 | 4.00 | 78.9 | 90.0 |
| Bench 2 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.27 | 9.15 | 14.96 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 2.68 | 7.04 | 12.15 | 5.00 | 37.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.60 | 24.83 | 40.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.29 | 15.16 | 24.08 | 1.00 | 72.0 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.32 | 7.70 | 12.79 | 2.00 | 31.8 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.58 | 18.63 | 29.21 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.30 | 15.24 | 24.23 | 2.00 | 89.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.98 | 14.88 | 22.72 | 6.00 | 82.7 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.53 | 12.78 | 19.17 | 0.00 | 79.1 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 4.19 | 11.79 | 20.74 | 0.00 | 66.7 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 1.20 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Eberechi Eze
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.02
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.24) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 6.49, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.24) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.41 | 10.20 | 16.64 | 3.00 | 81.1 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.21 | 0.61 | 1.09 | 0.00 | 1.8 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.12 | 13.94 | 22.73 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.88 | 11.46 | 18.27 | 2.00 | 84.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.10 | 11.29 | 18.69 | 0.00 | 77.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.1 | 3.66 | 10.24 | 16.42 | 0.00 | 81.2 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.16 | 9.07 | 14.25 | 3.00 | 85.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 9.24 | 25.77 | 41.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.99 | 12.87 | 21.35 | 6.00 | 60.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.28 | 9.07 | 15.36 | 1.00 | 48.5 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.03 | 15.64 | 23.99 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 1 | 7.7 | 5.18 | 15.43 | 24.58 | 2.00 | 90.0 | 71.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.89 | 14.46 | 24.62 | 11.00 | 83.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.05 | 13.16 | 21.32 | 1.00 | 62.8 | 90.0 |
| Bench 3 | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.36 | 7.85 | 12.61 | -2.00 | 43.4 | 37.0 |
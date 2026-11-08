# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 279.02
- Total actual points: 213.00
- Average predicted points: 69.75
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
- Predicted score: 67.03
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.29 | 11.97 | 19.19 | 6.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.05 | 0.30 | 0.60 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.44 | 15.54 | 24.53 | 12.00 | 89.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.97 | 14.75 | 23.89 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.73 | 13.01 | 21.62 | 3.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.55 | 10.08 | 15.87 | 1.00 | 77.8 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.90 | 9.29 | 15.51 | 1.00 | 80.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.75 | 23.01 | 38.78 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.97 | 16.81 | 26.23 | 9.00 | 90.0 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.34 | 10.73 | 16.93 | 2.00 | 81.6 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.07 | 19.80 | 30.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.48 | 17.52 | 29.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.98 | 14.73 | 23.94 | 13.00 | 81.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.99 | 14.36 | 23.02 | 5.00 | 79.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.60 | 14.36 | 22.82 | 9.00 | 87.5 | 61.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.53
- Actual score: 33.00
- Transfer: Iliman Ndiaye -> Moisés Caicedo Corozo (projected gain 2.98, hit 0)
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.98 | 11.74 | 18.90 | 1.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.12 | 0.29 | 0.56 | 0.00 | 4.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.28 | 17.15 | 27.28 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.24 | 15.03 | 23.69 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.15 | 11.97 | 19.40 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.83 | 9.36 | 15.43 | 4.00 | 76.7 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.12 | 8.82 | 14.01 | 3.00 | 84.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.72 | 24.81 | 40.63 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.43 | 16.25 | 24.81 | 2.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.04 | 9.91 | 15.25 | 1.00 | 62.3 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.78 | 17.16 | 27.70 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.24 | 16.43 | 25.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.52 | 14.84 | 22.92 | 7.00 | 68.3 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 5.59 | 14.47 | 22.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.88 | 14.16 | 23.45 | 5.00 | 84.8 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.54
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.26) beats the best remaining Bench Boost opportunity (9.86).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 4.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.26) beats the best remaining Bench Boost opportunity (9.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.80 | 10.95 | 17.79 | 2.00 | 82.2 | 90.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.00 | 0.10 | 0.39 | 0.00 | 3.9 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.12 | 13.55 | 22.82 | 14.00 | 88.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.69 | 12.33 | 19.55 | 3.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.1 | 3.46 | 10.07 | 17.61 | 4.00 | 77.6 | 90.0 |
| Bench 2 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.27 | 9.19 | 15.08 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 2.44 | 6.60 | 11.69 | 5.00 | 31.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.61 | 24.85 | 40.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.26 | 15.13 | 24.05 | 1.00 | 71.1 | 59.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.54 | 8.06 | 13.17 | 2.00 | 36.2 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.67 | 18.79 | 29.28 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.38 | 15.37 | 24.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.98 | 14.90 | 22.71 | 6.00 | 82.6 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 6.0 | 4.51 | 12.76 | 19.15 | 0.00 | 78.6 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 4.20 | 11.30 | 19.92 | 0.00 | 66.5 | 0.0 |

## GW13

- Train rows: 170095
- Bank: 1.20 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Eberechi Eze
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.91
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 6.51, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.37 | 10.14 | 16.61 | 3.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.40 | 0.47 | 0.59 | 0.00 | 3.5 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.09 | 13.90 | 22.73 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.85 | 11.42 | 18.23 | 2.00 | 84.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.04 | 11.19 | 18.61 | 0.00 | 75.7 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.1 | 3.64 | 10.20 | 16.39 | 0.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.14 | 9.02 | 14.21 | 3.00 | 84.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 9.29 | 25.94 | 41.90 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.93 | 12.79 | 21.29 | 6.00 | 58.3 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.42 | 9.32 | 15.64 | 1.00 | 52.9 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.04 | 15.67 | 24.00 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 1 | 7.7 | 5.16 | 15.41 | 24.57 | 2.00 | 90.0 | 71.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.95 | 14.57 | 24.65 | 11.00 | 84.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 3.97 | 12.96 | 20.93 | 1.00 | 61.1 | 90.0 |
| Bench 4 | Bench | Moisés Caicedo Corozo | MID | 7 | 6.0 | 2.26 | 7.70 | 12.46 | -2.00 | 40.7 | 37.0 |
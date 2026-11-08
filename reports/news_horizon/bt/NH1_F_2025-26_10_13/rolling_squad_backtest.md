# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 279.57
- Total actual points: 219.00
- Average predicted points: 69.89
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
- Predicted score: 66.81
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.29 | 11.95 | 19.15 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.03 | 0.34 | 0.72 | 0.00 | 4.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.45 | 15.58 | 24.54 | 12.00 | 89.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.96 | 14.75 | 23.81 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.71 | 12.94 | 21.35 | 3.00 | 87.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.54 | 10.10 | 15.92 | 1.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.88 | 9.22 | 15.19 | 1.00 | 80.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.99 | 23.71 | 38.69 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.74 | 16.27 | 25.28 | 9.00 | 88.3 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.33 | 10.74 | 17.08 | 2.00 | 81.4 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.18 | 20.19 | 31.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.46 | 17.45 | 28.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.61 | 14.39 | 22.89 | 9.00 | 87.7 | 61.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.97 | 14.28 | 23.02 | 5.00 | 79.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.47 | 13.38 | 21.54 | 13.00 | 73.4 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.43
- Actual score: 34.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.97 | 11.69 | 18.83 | 1.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.11 | 0.32 | 0.68 | 0.00 | 3.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.28 | 17.15 | 27.26 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.22 | 14.98 | 23.64 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.14 | 11.94 | 19.40 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.81 | 9.29 | 15.33 | 4.00 | 76.3 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.12 | 8.81 | 13.97 | 3.00 | 84.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.69 | 24.66 | 40.43 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.44 | 16.29 | 24.95 | 2.00 | 78.5 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.16 | 10.12 | 15.91 | 1.00 | 67.4 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.78 | 17.18 | 27.79 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.28 | 16.58 | 25.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.51 | 14.75 | 22.80 | 7.00 | 68.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.87 | 14.11 | 23.41 | 5.00 | 84.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.54 | 12.63 | 20.29 | 3.00 | 78.1 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.28
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.09) beats the best remaining Bench Boost opportunity (10.89).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 3.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.09) beats the best remaining Bench Boost opportunity (10.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.79 | 10.87 | 17.64 | 2.00 | 82.4 | 90.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.00 | 0.14 | 0.52 | 0.00 | 3.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.14 | 13.54 | 22.83 | 14.00 | 88.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.70 | 12.33 | 19.60 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.46 | 10.04 | 17.56 | 4.00 | 77.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.62 | 9.29 | 15.33 | 5.00 | 49.5 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.02 | 8.50 | 13.87 | 3.00 | 82.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.58 | 24.74 | 40.40 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.21 | 14.95 | 23.85 | 1.00 | 70.7 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.61 | 8.04 | 13.61 | 2.00 | 40.3 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.72 | 18.96 | 29.62 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.38 | 15.36 | 24.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.99 | 14.92 | 22.79 | 6.00 | 82.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.48 | 14.86 | 24.19 | 0.00 | 85.2 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.00 | 12.38 | 20.93 | 3.00 | 75.3 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Eberechi Eze
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.04
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.99) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 5.41, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.99) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.35 | 10.02 | 16.39 | 3.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.38 | 0.49 | 0.69 | 0.00 | 3.0 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.09 | 13.91 | 22.79 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.83 | 11.32 | 18.10 | 2.00 | 83.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.02 | 11.10 | 18.46 | 0.00 | 75.4 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.64 | 10.19 | 16.39 | 0.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.14 | 9.02 | 14.22 | 3.00 | 84.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.99 | 25.14 | 40.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.83 | 12.42 | 20.72 | 6.00 | 57.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.40 | 9.25 | 15.59 | 1.00 | 52.6 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.03 | 15.66 | 24.06 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 1 | 7.7 | 5.20 | 15.53 | 24.79 | 2.00 | 90.0 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.78 | 14.85 | 23.67 | 1.00 | 74.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.93 | 14.49 | 24.54 | 11.00 | 84.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.00 | 10.93 | 19.04 | 2.00 | 68.1 | 79.0 |
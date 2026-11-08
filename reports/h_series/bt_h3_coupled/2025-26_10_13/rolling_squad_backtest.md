# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 281.01
- Total actual points: 219.00
- Average predicted points: 70.25
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
- Predicted score: 67.18
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.30 | 11.99 | 19.23 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.04 | 0.23 | 0.53 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.47 | 15.61 | 24.61 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.97 | 14.77 | 23.90 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.72 | 12.96 | 21.54 | 3.00 | 87.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.56 | 10.11 | 15.89 | 1.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.90 | 9.26 | 15.42 | 1.00 | 80.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.99 | 23.77 | 38.84 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.77 | 16.25 | 25.18 | 9.00 | 88.9 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.40 | 10.81 | 17.07 | 2.00 | 81.9 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.21 | 20.14 | 30.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.47 | 17.49 | 28.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.04 | 14.38 | 23.06 | 5.00 | 79.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.61 | 14.38 | 22.88 | 9.00 | 87.7 | 61.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.63 | 13.55 | 21.85 | 13.00 | 73.7 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.92
- Actual score: 34.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.98 | 11.74 | 18.93 | 1.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.37 | 0.44 | 0.73 | 0.00 | 3.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.30 | 17.19 | 27.37 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.24 | 15.01 | 23.69 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.14 | 11.93 | 19.36 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.85 | 9.35 | 15.43 | 4.00 | 76.5 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.12 | 8.81 | 13.99 | 3.00 | 84.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.69 | 24.72 | 40.60 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.59 | 16.45 | 25.09 | 2.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.35 | 10.34 | 16.10 | 1.00 | 67.9 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.79 | 17.18 | 27.79 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.29 | 16.57 | 25.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.75 | 15.07 | 23.17 | 7.00 | 68.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.90 | 14.15 | 23.46 | 5.00 | 84.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.54 | 12.63 | 20.27 | 3.00 | 78.1 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.54
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.11) beats the best remaining Bench Boost opportunity (10.91).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 3.65, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.11) beats the best remaining Bench Boost opportunity (10.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.75 | 10.88 | 17.74 | 2.00 | 82.1 | 90.0 |
| Bench 1 | Bench Boost | Gabriel Słonina | GK | 7 | 3.9 | 0.15 | 0.23 | 0.52 | 0.00 | 3.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.15 | 13.57 | 22.86 | 14.00 | 88.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.71 | 12.34 | 19.59 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.47 | 10.07 | 17.60 | 4.00 | 77.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.53 | 9.28 | 15.44 | 5.00 | 49.2 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.02 | 8.52 | 13.91 | 3.00 | 82.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.59 | 24.79 | 40.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.45 | 15.25 | 24.21 | 1.00 | 70.8 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.48 | 7.96 | 13.58 | 2.00 | 40.7 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.74 | 18.95 | 29.53 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.38 | 15.37 | 24.30 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.03 | 14.96 | 22.81 | 6.00 | 83.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.46 | 14.90 | 24.32 | 0.00 | 85.1 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.05 | 12.46 | 21.02 | 3.00 | 75.6 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Eberechi Eze
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.37
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.99) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 5.45, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.99) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.31 | 10.03 | 16.50 | 3.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.01 | 0.14 | 0.24 | 0.00 | 3.5 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.11 | 13.95 | 22.80 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.83 | 11.35 | 18.15 | 2.00 | 83.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.01 | 11.12 | 18.51 | 0.00 | 75.3 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.62 | 10.17 | 16.36 | 0.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.14 | 9.04 | 14.23 | 3.00 | 84.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.99 | 25.18 | 40.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.89 | 12.61 | 21.10 | 6.00 | 56.9 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.39 | 9.25 | 15.57 | 1.00 | 52.7 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.04 | 15.65 | 24.04 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 1 | 7.7 | 5.21 | 15.53 | 24.75 | 2.00 | 90.0 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.92 | 15.04 | 23.92 | 1.00 | 74.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.96 | 14.55 | 24.62 | 11.00 | 84.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.12 | 11.08 | 19.21 | 2.00 | 68.1 | 79.0 |
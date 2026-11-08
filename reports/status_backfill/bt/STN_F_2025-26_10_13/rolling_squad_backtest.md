# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 281.80
- Total actual points: 219.00
- Average predicted points: 70.45
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
- Predicted score: 68.06
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.39 | 11.99 | 19.23 | 6.00 | 92.1 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.32 | 0.90 | 1.61 | 0.00 | 5.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.59 | 15.61 | 24.61 | 12.00 | 92.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.05 | 14.77 | 23.90 | 10.00 | 94.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.64 | 12.96 | 21.54 | 3.00 | 85.9 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.59 | 10.11 | 15.88 | 1.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.86 | 9.25 | 15.41 | 1.00 | 79.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.93 | 23.77 | 38.84 | 13.00 | 104.9 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 6.33 | 16.25 | 25.18 | 9.00 | 97.8 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.50 | 10.76 | 17.02 | 2.00 | 83.9 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.68 | 20.14 | 30.85 | 2.00 | 125.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.40 | 17.49 | 28.99 | 2.00 | 99.6 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.62 | 14.38 | 22.88 | 9.00 | 87.8 | 61.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.89 | 14.31 | 22.99 | 5.00 | 78.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.60 | 13.41 | 21.71 | 13.00 | 75.3 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Jean-Philippe Mateta
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.20
- Actual score: 34.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.06 | 11.74 | 18.93 | 1.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.31 | 0.83 | 1.51 | 0.00 | 5.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.41 | 17.19 | 27.37 | 1.00 | 95.4 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.30 | 15.01 | 23.69 | 0.00 | 92.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.14 | 11.93 | 19.36 | 2.00 | 92.4 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.87 | 9.32 | 15.39 | 4.00 | 77.1 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.12 | 8.82 | 14.00 | 3.00 | 84.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.59 | 24.72 | 40.60 | 4.00 | 106.0 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.81 | 16.33 | 24.98 | 2.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.35 | 10.16 | 15.93 | 1.00 | 69.9 | 27.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.73 | 17.18 | 27.79 | 0.00 | 103.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.51 | 16.57 | 25.61 | 2.00 | 98.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.59 | 14.81 | 22.93 | 7.00 | 68.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.86 | 14.12 | 23.42 | 5.00 | 85.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.60 | 12.63 | 20.27 | 3.00 | 78.7 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 75.58
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.16) beats the best remaining Bench Boost opportunity (10.98).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 3.61, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.16) beats the best remaining Bench Boost opportunity (10.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.76 | 10.91 | 17.77 | 2.00 | 81.9 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 3.9 | 0.00 | 0.53 | 1.22 | 0.00 | 6.0 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.27 | 13.57 | 22.86 | 14.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.81 | 12.34 | 19.59 | 3.00 | 93.6 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.48 | 10.07 | 17.60 | 4.00 | 77.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.57 | 9.36 | 15.52 | 5.00 | 48.8 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.00 | 8.52 | 13.92 | 3.00 | 82.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.50 | 24.79 | 40.50 | 2.00 | 110.7 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.35 | 15.02 | 24.00 | 1.00 | 72.2 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.69 | 8.12 | 13.74 | 2.00 | 40.3 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 7.01 | 18.95 | 29.53 | 1.00 | 111.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.40 | 15.37 | 24.30 | 2.00 | 93.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.08 | 14.92 | 22.78 | 6.00 | 84.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.16 | 14.91 | 24.33 | 0.00 | 80.5 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.01 | 12.42 | 20.98 | 3.00 | 75.4 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Eberechi Eze
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 70.95
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.95) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 5.42, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.95) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.28 | 10.06 | 16.53 | 3.00 | 79.1 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.34 | 0.86 | 1.39 | 0.00 | 5.7 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.24 | 13.95 | 22.80 | 1.00 | 93.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.72 | 11.36 | 18.16 | 2.00 | 82.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.97 | 11.12 | 18.52 | 0.00 | 74.5 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.60 | 10.19 | 16.38 | 0.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.15 | 9.04 | 14.24 | 3.00 | 84.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.95 | 25.18 | 40.58 | 2.00 | 110.3 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.70 | 12.54 | 21.03 | 6.00 | 54.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.34 | 9.27 | 15.59 | 1.00 | 49.5 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.11 | 15.65 | 24.04 | 4.00 | 92.5 | 90.0 |
| Vice Captain | XI | Eberechi Eze | MID | 1 | 7.7 | 5.47 | 15.53 | 24.75 | 2.00 | 101.5 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.71 | 14.89 | 23.78 | 1.00 | 73.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.91 | 14.52 | 24.59 | 11.00 | 85.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.00 | 10.97 | 19.10 | 2.00 | 68.1 | 79.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 279.97
- Total actual points: 220.00
- Average predicted points: 69.99
- Average actual points: 55.00
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
- Predicted score: 66.80
- Actual score: 97.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.33 | 12.06 | 19.31 | 6.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.14 | 0.26 | 0.43 | 0.00 | 4.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.40 | 15.40 | 24.27 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.96 | 14.70 | 23.79 | 10.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.64 | 12.77 | 21.32 | 3.00 | 88.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.56 | 10.07 | 15.76 | 1.00 | 77.6 | 90.0 |
| Bench 4 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.86 | 9.14 | 15.24 | 1.00 | 79.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.83 | 23.35 | 38.19 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.83 | 16.43 | 25.46 | 9.00 | 88.7 | 89.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.31 | 10.64 | 16.86 | 2.00 | 82.2 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.33 | 20.46 | 31.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.49 | 17.52 | 29.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.02 | 14.46 | 23.21 | 5.00 | 79.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.60 | 14.36 | 22.88 | 9.00 | 87.7 | 61.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.52 | 13.50 | 21.89 | 13.00 | 73.5 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.41
- Actual score: 34.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.02 | 11.83 | 19.06 | 1.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.00 | 0.05 | 0.00 | 4.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.24 | 16.99 | 27.06 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.24 | 14.97 | 23.60 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.07 | 11.74 | 19.09 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.83 | 9.30 | 15.34 | 4.00 | 76.2 | 90.0 |
| Bench 3 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.10 | 8.72 | 13.81 | 3.00 | 84.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.51 | 24.24 | 39.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.55 | 16.57 | 25.37 | 2.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.14 | 10.04 | 15.75 | 1.00 | 68.0 | 27.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.81 | 17.19 | 27.78 | 0.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 5.34 | 16.68 | 25.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.67 | 15.23 | 23.59 | 7.00 | 67.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.92 | 14.29 | 23.69 | 5.00 | 84.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.53 | 12.59 | 20.20 | 3.00 | 78.1 | 90.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.14) beats the best remaining Bench Boost opportunity (10.95).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 3.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.14) beats the best remaining Bench Boost opportunity (10.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.82 | 10.99 | 17.86 | 2.00 | 81.6 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.09 | 0.10 | 0.33 | 0.00 | 4.5 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.18 | 13.63 | 22.91 | 14.00 | 87.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.63 | 12.15 | 19.31 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.46 | 10.02 | 17.49 | 4.00 | 77.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.59 | 9.27 | 15.37 | 5.00 | 49.3 | 90.0 |
| Bench 3 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 2.99 | 8.41 | 13.71 | 3.00 | 82.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.41 | 24.32 | 39.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.28 | 15.20 | 24.29 | 1.00 | 70.6 | 59.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.60 | 8.02 | 13.58 | 2.00 | 40.8 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.84 | 19.24 | 29.99 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.44 | 15.55 | 24.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.04 | 15.05 | 22.98 | 6.00 | 82.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.48 | 14.89 | 24.28 | 0.00 | 84.8 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.00 | 12.39 | 20.94 | 3.00 | 75.7 | 80.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 1.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.48
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.81) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Morgan Rogers (projected gain 5.52, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.81) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.37 | 10.13 | 16.61 | 3.00 | 79.2 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.00 | 0.04 | 0.10 | 0.00 | 4.9 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.15 | 14.04 | 22.90 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.76 | 11.17 | 17.89 | 2.00 | 84.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.99 | 11.05 | 18.39 | 0.00 | 75.2 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.64 | 10.16 | 16.29 | 0.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.13 | 8.96 | 14.06 | 3.00 | 84.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.81 | 24.69 | 39.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.87 | 12.67 | 21.23 | 6.00 | 56.8 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.36 | 9.15 | 15.40 | 1.00 | 52.8 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.08 | 15.77 | 24.22 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.93 | 15.60 | 24.02 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.89 | 15.20 | 24.26 | 1.00 | 73.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.99 | 14.70 | 24.86 | 11.00 | 84.2 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.00 | 10.95 | 19.05 | 2.00 | 68.1 | 79.0 |
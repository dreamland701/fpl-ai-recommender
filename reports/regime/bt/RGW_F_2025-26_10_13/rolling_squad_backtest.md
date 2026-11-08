# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 274.13
- Total actual points: 207.00
- Average predicted points: 68.53
- Average actual points: 51.75
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
- Predicted score: 67.00
- Actual score: 90.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.17 | 11.69 | 18.52 | 6.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.06 | 0.26 | 0.32 | 0.00 | 2.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.51 | 15.82 | 24.94 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.99 | 14.88 | 24.07 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.11 | 14.58 | 23.30 | 6.00 | 87.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.72 | 13.04 | 21.68 | 3.00 | 89.2 | 90.0 |
| Bench 3 | Bench | Maxime Estève | DEF | 3 | 4.0 | 2.90 | 9.37 | 15.75 | 1.00 | 80.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.86 | 23.50 | 38.11 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.92 | 16.05 | 24.83 | 9.00 | 89.1 | 89.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.26 | 10.24 | 16.39 | 2.00 | 84.6 | 61.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.25 | 20.06 | 30.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.16 | 16.53 | 27.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.94 | 14.23 | 22.75 | 5.00 | 78.7 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.52 | 14.14 | 22.54 | 9.00 | 86.8 | 61.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 2.02 | 5.56 | 8.36 | 3.00 | 48.3 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Jean-Philippe Mateta
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.69
- Actual score: 33.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxime Estève replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.93 | 11.53 | 18.38 | 1.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.14 | 0.29 | 0.32 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.35 | 17.29 | 27.55 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.23 | 15.02 | 23.67 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.08 | 12.78 | 20.75 | 1.00 | 80.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.12 | 11.76 | 18.92 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Maxime Estève | DEF | 3 | 4.0 | 3.09 | 8.78 | 13.92 | 3.00 | 85.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.45 | 24.44 | 39.83 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.57 | 16.26 | 25.04 | 2.00 | 80.0 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.04 | 9.51 | 15.23 | 1.00 | 69.7 | 27.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.51 | 16.25 | 26.10 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.63 | 14.65 | 22.98 | 7.00 | 70.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.84 | 14.03 | 23.17 | 5.00 | 83.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.51 | 12.46 | 19.79 | 3.00 | 77.4 | 90.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 2.23 | 6.37 | 9.84 | 2.00 | 61.0 | 74.0 |

## GW12

- Train rows: 169340
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.26
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.99) beats the best remaining Bench Boost opportunity (9.43).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 5.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.99) beats the best remaining Bench Boost opportunity (9.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.80 | 10.91 | 17.39 | 2.00 | 81.5 | 90.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.00 | 0.15 | 0.27 | 0.00 | 2.6 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.83 | 14.00 | 22.20 | 5.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.18 | 13.57 | 22.88 | 14.00 | 88.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.68 | 12.01 | 18.91 | 3.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.57 | 9.23 | 15.31 | 5.00 | 49.7 | 90.0 |
| Bench 2 | Bench Boost | Maxime Estève | DEF | 3 | 3.9 | 3.03 | 8.55 | 13.85 | 3.00 | 83.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.37 | 24.69 | 40.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.33 | 14.95 | 23.63 | 1.00 | 72.4 | 59.0 |
| Bench 3 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.57 | 7.74 | 12.95 | 2.00 | 42.3 | 85.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.69 | 18.47 | 28.72 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.31 | 15.08 | 23.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.18 | 14.16 | 22.79 | 0.00 | 85.7 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.97 | 12.13 | 20.23 | 3.00 | 75.2 | 80.0 |
| Bench 4 | Bench Boost | Carlos Baleba | MID | 6 | 4.7 | 2.39 | 6.63 | 10.15 | 1.00 | 58.3 | 45.0 |

## GW13

- Train rows: 170095
- Bank: 0.70 -> 1.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Daniel Muñoz Mejía
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.19
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.79) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Declan Rice (projected gain 6.57, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.79) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.38 | 10.11 | 16.30 | 3.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.45 | 0.60 | 0.61 | 0.00 | 2.4 | 0.0 |
| Vice Captain | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.19 | 14.09 | 23.18 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 4.12 | 12.59 | 20.35 | 2.00 | 81.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.80 | 11.15 | 17.79 | 2.00 | 84.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.95 | 11.00 | 18.21 | 0.00 | 77.2 | 90.0 |
| Bench 2 | Bench | Maxime Estève | DEF | 3 | 3.9 | 3.13 | 8.86 | 13.92 | 3.00 | 84.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.79 | 25.11 | 40.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.75 | 12.33 | 20.22 | 6.00 | 57.6 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.46 | 9.23 | 15.57 | 1.00 | 56.0 | 10.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.99 | 15.38 | 23.52 | 4.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.76 | 14.49 | 23.24 | 1.00 | 75.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.90 | 14.45 | 24.41 | 11.00 | 82.8 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.98 | 10.65 | 18.36 | 2.00 | 67.5 | 79.0 |
| Bench 4 | Bench | Carlos Baleba | MID | 6 | 4.7 | 1.87 | 5.87 | 9.38 | 1.00 | 51.1 | 6.0 |
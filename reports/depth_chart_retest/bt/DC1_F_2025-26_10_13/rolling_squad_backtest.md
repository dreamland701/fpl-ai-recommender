# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 279.45
- Total actual points: 192.00
- Average predicted points: 69.86
- Average actual points: 48.00
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
- Predicted score: 68.29
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.67 | 13.04 | 20.93 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.07 | 0.31 | 0.53 | 0.00 | 3.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.31 | 15.08 | 23.75 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.90 | 14.57 | 23.57 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.01 | 13.87 | 21.95 | 6.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.63 | 12.75 | 21.21 | 3.00 | 86.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.35 | 11.60 | 18.29 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.01 | 23.83 | 38.97 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.89 | 16.60 | 25.76 | 9.00 | 90.0 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 5.15 | 15.13 | 23.02 | 1.00 | 76.4 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.10 | 19.86 | 30.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.27 | 16.91 | 28.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.63 | 14.46 | 23.00 | 9.00 | 87.3 | 61.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.39 | 10.93 | 17.87 | 1.00 | 74.0 | 59.0 |
| Bench 2 | Bench | Granit Xhaka | MID | 17 | 5.1 | 3.85 | 10.93 | 17.31 | 10.00 | 81.0 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.14
- Actual score: 33.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 3.83, hit 0)
- Autosub: Jurriën Timber replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.37 | 12.84 | 20.70 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.14 | 0.28 | 0.58 | 0.00 | 4.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.17 | 16.71 | 26.56 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.18 | 14.84 | 23.39 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 4.01 | 12.30 | 19.76 | 1.00 | 79.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.07 | 11.79 | 19.12 | 2.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.10 | 11.01 | 17.73 | 1.00 | 87.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.66 | 24.64 | 40.47 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.58 | 16.64 | 25.47 | 2.00 | 80.5 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.88 | 16.06 | 25.78 | 7.00 | 90.0 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.55 | 16.54 | 26.79 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.44 | 14.63 | 22.65 | 7.00 | 67.5 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.49 | 12.52 | 20.07 | 3.00 | 77.2 | 90.0 |
| Bench 3 | Bench | Granit Xhaka | MID | 17 | 5.1 | 3.56 | 12.00 | 19.50 | 3.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.36 | 10.94 | 17.73 | 1.00 | 70.4 | 73.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 76.03
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.70) beats the best remaining Bench Boost opportunity (11.23).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 4.33, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.70) beats the best remaining Bench Boost opportunity (11.23).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.16 | 11.99 | 19.49 | 2.00 | 86.0 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.15 | 0.00 | 3.1 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.59 | 13.26 | 20.96 | 5.00 | 88.4 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.02 | 13.23 | 22.33 | 14.00 | 85.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.64 | 12.23 | 19.42 | 3.00 | 89.9 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.22 | 10.41 | 16.84 | 0.00 | 87.5 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 3.52 | 9.11 | 15.11 | 5.00 | 47.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.57 | 24.77 | 40.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.69 | 15.68 | 24.40 | 1.00 | 81.2 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.40 | 15.56 | 24.85 | 1.00 | 72.4 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.57 | 18.60 | 29.01 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.12 | 14.02 | 22.97 | 0.00 | 81.6 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.90 | 12.20 | 20.67 | 3.00 | 73.2 | 80.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.1 | 4.10 | 11.72 | 19.84 | 2.00 | 83.4 | 90.0 |
| Bench 4 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.96 | 9.23 | 14.97 | 2.00 | 71.3 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.80 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.99
- Actual score: 31.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.99) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Iliman Ndiaye -> Declan Rice (projected gain 4.87, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.99) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.71 | 11.12 | 18.23 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.06 | 0.15 | 0.28 | 0.00 | 2.9 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.93 | 13.46 | 22.05 | 1.00 | 89.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.82 | 11.88 | 18.97 | 2.00 | 76.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.82 | 11.38 | 18.21 | 2.00 | 83.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.88 | 10.79 | 18.00 | 0.00 | 73.2 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.66 | 10.65 | 17.78 | 0.00 | 83.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.99 | 25.20 | 40.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 4.01 | 13.08 | 21.90 | 6.00 | 58.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.26 | 12.53 | 20.76 | 1.00 | 65.0 | 54.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 5.02 | 15.66 | 24.11 | 4.00 | 89.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.62 | 14.55 | 23.29 | 1.00 | 72.2 | 90.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.1 | 3.95 | 11.10 | 18.17 | 5.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.78 | 9.28 | 15.05 | 0.00 | 76.9 | 0.0 |
| Bench 4 | Bench | Antoine Semenyo | MID | 4 | 7.9 | 2.58 | 8.13 | 14.94 | 1.00 | 38.1 | 90.0 |
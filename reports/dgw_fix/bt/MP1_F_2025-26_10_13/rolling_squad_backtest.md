# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 281.13
- Total actual points: 185.00
- Average predicted points: 70.28
- Average actual points: 46.25
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
- Predicted score: 68.33
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.33 | 12.06 | 19.43 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.15 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.45 | 15.56 | 24.45 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 5.04 | 14.92 | 24.09 | 10.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.95 | 13.75 | 21.75 | 6.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.71 | 12.96 | 21.33 | 3.00 | 87.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.58 | 12.21 | 19.36 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.95 | 23.66 | 38.71 | 13.00 | 90.0 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.84 | 16.39 | 25.42 | 9.00 | 90.0 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 4.81 | 14.15 | 21.44 | 1.00 | 73.1 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 7.34 | 20.46 | 31.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.53 | 17.65 | 29.08 | 2.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.57 | 14.30 | 22.64 | 9.00 | 86.7 | 61.0 |
| Bench 2 | Bench | Granit Xhaka | MID | 17 | 5.1 | 3.71 | 10.52 | 16.67 | 10.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.10 | 10.11 | 16.36 | 1.00 | 70.9 | 59.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.53
- Actual score: 33.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 3.42, hit 0)
- Autosub: Jurriën Timber replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 4.00 | 11.84 | 19.05 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.03 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 5.31 | 17.21 | 27.25 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 5.30 | 15.18 | 23.84 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Jurriën Timber | DEF | 1 | 6.1 | 3.94 | 12.18 | 19.55 | 1.00 | 77.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.17 | 11.98 | 19.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.32 | 11.59 | 18.66 | 1.00 | 89.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.67 | 24.73 | 40.58 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.48 | 16.35 | 24.97 | 2.00 | 79.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.73 | 15.51 | 24.86 | 7.00 | 88.1 | 82.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.90 | 17.44 | 28.14 | 0.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.46 | 14.65 | 22.65 | 7.00 | 67.3 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.50 | 12.52 | 20.12 | 3.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Granit Xhaka | MID | 17 | 5.1 | 3.37 | 11.48 | 18.51 | 3.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Sean Longstaff | MID | 11 | 4.9 | 3.03 | 10.04 | 16.16 | 1.00 | 66.6 | 73.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 76.39
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.89) beats the best remaining Bench Boost opportunity (11.49).
- Transfer: Gabriel dos Santos Magalhães -> Daniel Muñoz Mejía (projected gain 2.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.89) beats the best remaining Bench Boost opportunity (11.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.80 | 10.99 | 17.84 | 2.00 | 82.4 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.70 | 13.50 | 21.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.13 | 13.49 | 22.66 | 14.00 | 87.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.79 | 12.51 | 19.79 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.53 | 11.20 | 18.05 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 3.51 | 9.15 | 15.15 | 5.00 | 47.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.56 | 24.78 | 40.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.67 | 15.54 | 24.21 | 1.00 | 82.2 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.17 | 14.89 | 23.78 | 1.00 | 69.9 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.77 | 19.02 | 29.68 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.47 | 14.90 | 24.30 | 0.00 | 85.0 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 3.91 | 12.15 | 20.49 | 3.00 | 73.6 | 80.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.1 | 3.98 | 11.29 | 19.14 | 2.00 | 81.7 | 90.0 |
| Bench 4 | Bench Boost | Sean Longstaff | MID | 11 | 4.9 | 2.85 | 8.83 | 14.31 | 2.00 | 70.8 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.80 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.88
- Actual score: 24.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Iliman Ndiaye -> Morgan Rogers (projected gain 4.80, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.06) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.8 | 3.34 | 10.05 | 16.58 | 3.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 5.10 | 13.89 | 22.72 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.92 | 12.08 | 19.27 | 2.00 | 78.3 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.95 | 11.36 | 18.89 | 0.00 | 87.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.83 | 11.34 | 18.11 | 2.00 | 83.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.01 | 11.08 | 18.48 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 9.06 | 25.35 | 40.87 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.68 | 12.16 | 20.46 | 6.00 | 53.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.05 | 11.96 | 19.84 | 1.00 | 62.8 | 54.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 6.9 | 5.91 | 15.54 | 23.91 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.71 | 14.72 | 23.51 | 1.00 | 73.2 | 90.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.1 | 3.88 | 10.85 | 17.70 | 5.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Sean Longstaff | MID | 11 | 4.9 | 2.72 | 9.06 | 14.62 | 0.00 | 77.0 | 0.0 |
| Bench 4 | Bench | Antoine Semenyo | MID | 4 | 7.9 | 2.57 | 8.12 | 14.89 | 1.00 | 34.2 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 265.11
- Total actual points: 207.00
- Average predicted points: 66.28
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
- Predicted score: 62.41
- Actual score: 93.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 15 | 5.2 | 3.21 | 9.46 | 15.37 | 3.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.06 | 0.33 | 0.63 | 0.00 | 4.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.88 | 13.90 | 22.29 | 12.00 | 82.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 5.04 | 13.85 | 21.77 | 6.00 | 84.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.38 | 13.06 | 21.58 | 10.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.49 | 10.56 | 17.05 | 6.00 | 80.6 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.60 | 10.11 | 15.80 | 1.00 | 79.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 7.40 | 22.06 | 36.52 | 13.00 | 82.9 | 81.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.8 | 5.18 | 14.55 | 22.85 | 9.00 | 81.8 | 89.0 |
| XI | XI | Nick Woltemade | FWD | 15 | 7.5 | 4.85 | 14.15 | 21.37 | 1.00 | 74.8 | 45.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.3 | 6.63 | 18.44 | 28.52 | 2.00 | 82.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 4.89 | 15.79 | 26.66 | 2.00 | 82.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.53 | 13.41 | 21.63 | 13.00 | 75.4 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.02 | 12.67 | 20.56 | 9.00 | 80.5 | 61.0 |
| Bench 4 | Bench | Josh Cullen | MID | 3 | 5.0 | 3.18 | 10.25 | 17.05 | 1.00 | 80.4 | 81.0 |

## GW11

- Train rows: 168588
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Jean-Philippe Mateta
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.34
- Actual score: 42.00
- Transfer: Nick Woltemade -> João Pedro Junqueira de Jesus (projected gain 3.19, hit 0)
- Autosub: Chris Richards replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 15 | 5.2 | 2.90 | 8.68 | 14.46 | 3.00 | 82.7 | 76.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.13 | 0.29 | 0.67 | 0.00 | 5.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.72 | 15.48 | 25.09 | 1.00 | 82.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.0 | 4.66 | 13.30 | 21.41 | 0.00 | 82.9 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.01 | 12.25 | 19.61 | 1.00 | 80.0 | 90.0 |
| Bench 2 | Autosub In | Chris Richards | DEF | 8 | 4.5 | 3.70 | 11.04 | 17.08 | 8.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 2.87 | 9.33 | 15.34 | 4.00 | 78.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.10 | 23.01 | 38.32 | 4.00 | 82.9 | 90.0 |
| Vice Captain | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.52 | 16.35 | 24.93 | 2.00 | 80.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.25 | 14.16 | 23.20 | 7.00 | 82.9 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 5.21 | 15.47 | 25.51 | 0.00 | 82.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.59 | 15.01 | 23.30 | 7.00 | 71.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.7 | 4.71 | 14.85 | 23.33 | 2.00 | 82.9 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.59 | 12.65 | 20.21 | 3.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Josh Cullen | MID | 3 | 5.0 | 2.76 | 9.34 | 15.13 | 10.00 | 73.5 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.94
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.32) beats the best remaining Bench Boost opportunity (12.52).
- Transfer: Gabriel dos Santos Magalhães -> Marc Cucurella Saseta (projected gain 3.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.32) beats the best remaining Bench Boost opportunity (12.52).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 15 | 5.2 | 2.57 | 7.98 | 13.61 | 3.00 | 80.5 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.00 | 0.00 | 0.25 | 0.00 | 4.1 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.67 | 12.67 | 20.56 | 6.00 | 81.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.10 | 11.75 | 19.01 | 5.00 | 82.9 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.5 | 4.43 | 11.29 | 18.62 | 6.00 | 83.1 | 82.0 |
| Bench 3 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.1 | 3.51 | 10.08 | 17.55 | 4.00 | 79.4 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.0 | 3.75 | 9.76 | 16.12 | 5.00 | 52.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.00 | 23.08 | 38.26 | 2.00 | 82.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 5.70 | 15.49 | 23.94 | 1.00 | 80.6 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 5.30 | 15.22 | 24.38 | 1.00 | 74.3 | 59.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 6.16 | 17.24 | 27.28 | 1.00 | 82.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 5.07 | 14.95 | 22.66 | 6.00 | 82.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.0 | 5.55 | 14.94 | 24.21 | 0.00 | 84.2 | 0.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.06 | 12.44 | 20.93 | 3.00 | 77.4 | 80.0 |
| Bench 4 | Bench Boost | Josh Cullen | MID | 3 | 5.0 | 3.06 | 8.90 | 15.01 | 2.00 | 78.9 | 90.0 |

## GW13

- Train rows: 170095
- Bank: 0.50 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.42
- Actual score: 25.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.42) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 3.64, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.42) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Nick Pope | GK | 15 | 5.2 | 2.77 | 8.16 | 13.49 | 0.00 | 81.6 | 0.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.05 | 0.17 | 0.37 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.99 | 12.18 | 19.35 | 2.00 | 80.6 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.14 | 12.05 | 20.05 | 1.00 | 80.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 4.06 | 11.13 | 18.48 | 0.00 | 77.0 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.1 | 3.72 | 10.24 | 16.29 | 0.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.58 | 9.97 | 16.45 | 1.00 | 81.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.8 | 8.42 | 23.47 | 38.31 | 2.00 | 82.9 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 7.9 | 3.97 | 12.94 | 21.62 | 6.00 | 60.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.21 | 12.38 | 20.54 | 1.00 | 68.0 | 54.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.4 | 4.83 | 14.91 | 23.74 | 1.00 | 76.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.47 | 13.94 | 21.77 | 4.00 | 82.9 | 90.0 |
| XI | XI | Eberechi Eze | MID | 1 | 7.7 | 4.63 | 13.82 | 22.49 | 2.00 | 82.9 | 71.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.08 | 11.18 | 19.48 | 2.00 | 71.5 | 79.0 |
| Bench 4 | Bench | Josh Cullen | MID | 3 | 5.0 | 2.90 | 8.46 | 13.76 | 2.00 | 79.7 | 80.0 |
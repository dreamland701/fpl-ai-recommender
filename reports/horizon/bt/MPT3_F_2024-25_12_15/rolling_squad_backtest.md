# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 227.50
- Total actual points: 214.00
- Average predicted points: 56.88
- Average actual points: 53.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 140908
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.10
- Actual score: 23.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.46 | 10.04 | 16.49 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.79 | 1.25 | 0.00 | 8.4 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.22 | 20.02 | 0.00 | 86.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.80 | 10.23 | 16.76 | 0.00 | 87.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.57 | 9.77 | 15.59 | 1.00 | 88.4 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.20 | 6.85 | 11.62 | 0.00 | 82.9 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.43 | 6.65 | 10.87 | 2.00 | 81.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 7.95 | 21.87 | 36.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.40 | 14.31 | 22.63 | 2.00 | 85.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.81 | 11.51 | 18.43 | 2.00 | 79.0 | 85.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.40 | 17.91 | 29.74 | 2.00 | 89.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.02 | 15.84 | 25.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 3.86 | 13.46 | 22.32 | 3.00 | 77.8 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.64 | 12.24 | 19.97 | 1.00 | 84.6 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.17 | 8.98 | 14.47 | 1.00 | 78.5 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 56.95
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.91) beats the best remaining Bench Boost opportunity (6.12).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.91) beats the best remaining Bench Boost opportunity (6.12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 10.71 | 17.47 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.57 | 1.03 | 1.50 | 0.00 | 7.9 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 3.60 | 11.63 | 19.23 | 0.00 | 86.8 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.06 | 9.15 | 14.94 | 2.00 | 80.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.69 | 8.09 | 13.32 | 2.00 | 72.9 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.18 | 6.70 | 11.05 | 1.00 | 79.5 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.81 | 3.01 | 5.93 | 0.00 | 35.6 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.1 | 5.79 | 18.51 | 31.87 | 2.00 | 79.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.01 | 12.40 | 19.93 | 1.00 | 61.5 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.77 | 10.27 | 16.64 | 2.00 | 72.2 | 78.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.57 | 18.23 | 29.85 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.42 | 14.98 | 25.01 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.79 | 12.58 | 20.29 | 9.00 | 71.9 | 65.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 2.93 | 9.12 | 15.14 | 2.00 | 59.2 | 85.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 1.35 | 4.53 | 8.25 | 0.00 | 32.7 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 52.47
- Actual score: 45.00
- Transfer: Alexander Isak -> Nicolas Jackson (projected gain 17.02, hit 0)
- Autosub: Dara O'Shea replaced Nicolas Jackson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.57 | 10.11 | 16.51 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.76 | 1.24 | 0.00 | 8.4 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.30 | 9.37 | 15.27 | 6.00 | 82.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.60 | 8.60 | 14.88 | 6.00 | 51.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.50 | 8.03 | 13.32 | 1.00 | 77.5 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 4.0 | 2.40 | 6.76 | 11.04 | 1.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.44 | 2.05 | 4.05 | 0.00 | 24.6 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.07 | 18.62 | 31.78 | 5.00 | 81.4 | 90.0 |
| XI | Bench | Nicolas Jackson | FWD | 6 | 8.1 | 5.68 | 15.60 | 24.54 | 0.00 | 87.3 | 0.0 |
| XI | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.11 | 9.44 | 15.63 | 0.00 | 68.7 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 7.45 | 20.69 | 33.67 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.64 | 12.92 | 22.43 | 2.00 | 73.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.89 | 12.00 | 21.02 | 2.00 | 77.2 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 3.20 | 9.53 | 16.00 | 2.00 | 67.4 | 70.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 0.94 | 2.84 | 5.44 | 0.00 | 18.7 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 56.98
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 7.65, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.72 | 10.99 | 17.91 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.44 | 0.84 | 1.26 | 0.00 | 7.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.01 | 11.30 | 18.93 | 1.00 | 80.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.86 | 9.20 | 15.04 | 1.00 | 82.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.65 | 7.66 | 12.29 | 1.00 | 77.5 | 82.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.27 | 6.57 | 10.65 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 1.01 | 2.47 | 0.00 | 13.3 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.40 | 19.14 | 32.50 | 7.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.15 | 10.58 | 16.61 | 2.00 | 59.8 | 70.0 |
| XI | XI | Nicolas Jackson | FWD | 6 | 8.1 | 2.73 | 8.93 | 14.66 | 2.00 | 32.2 | 75.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.63 | 19.28 | 31.40 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.51 | 14.25 | 23.84 | 9.00 | 87.0 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.60 | 10.79 | 19.09 | 13.00 | 76.2 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.6 | 2.47 | 8.24 | 13.85 | 1.00 | 58.3 | 59.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 0.25 | 1.40 | 2.93 | 0.00 | 6.0 | 0.0 |
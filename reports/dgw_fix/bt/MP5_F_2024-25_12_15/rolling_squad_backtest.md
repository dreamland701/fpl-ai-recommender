# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 228.13
- Total actual points: 245.00
- Average predicted points: 57.03
- Average actual points: 61.25
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
- Predicted score: 61.96
- Actual score: 23.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.50 | 10.15 | 16.67 | 6.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.05 | 0.32 | 0.50 | 0.00 | 4.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.27 | 12.29 | 20.14 | 0.00 | 87.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.83 | 10.32 | 16.91 | 0.00 | 88.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 3.57 | 9.79 | 15.62 | 1.00 | 88.6 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.23 | 6.91 | 11.71 | 0.00 | 83.5 | 0.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.47 | 6.75 | 11.04 | 2.00 | 82.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 7.79 | 21.44 | 35.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 5.40 | 14.31 | 22.63 | 2.00 | 85.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.80 | 11.49 | 18.39 | 2.00 | 78.9 | 85.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.95 | 19.33 | 31.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.04 | 15.89 | 25.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.34 | 14.69 | 24.25 | 3.00 | 88.4 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.67 | 12.31 | 20.08 | 1.00 | 85.2 | 58.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.16 | 8.97 | 14.46 | 1.00 | 78.4 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 57.53
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.53) beats the best remaining Bench Boost opportunity (6.94).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 3.31, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.53) beats the best remaining Bench Boost opportunity (6.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 10.77 | 17.57 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.35 | 0.44 | 0.59 | 0.00 | 2.9 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 3.57 | 11.54 | 19.10 | 0.00 | 86.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.05 | 9.14 | 14.92 | 2.00 | 79.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.68 | 8.06 | 13.26 | 2.00 | 72.7 | 90.0 |
| Bench 2 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.20 | 6.76 | 11.15 | 1.00 | 80.0 | 90.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 1.17 | 3.98 | 7.43 | 0.00 | 43.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.1 | 5.51 | 17.78 | 30.73 | 2.00 | 73.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 3.93 | 12.18 | 19.56 | 1.00 | 59.5 | 21.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.74 | 10.19 | 16.52 | 2.00 | 71.5 | 78.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.56 | 18.21 | 29.84 | 14.00 | 90.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.35 | 14.80 | 24.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.67 | 12.25 | 19.77 | 9.00 | 69.1 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.53 | 10.51 | 17.01 | 5.00 | 83.4 | 85.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 1.81 | 5.71 | 10.07 | 0.00 | 42.9 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 50.59
- Actual score: 64.00
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 7.60, hit 0)
- Autosub: Alexander Isak replaced Danny Welbeck.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.59 | 10.17 | 16.61 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.17 | 0.33 | 0.00 | 3.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.03 | 11.68 | 18.75 | 1.00 | 87.4 | 28.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.29 | 9.34 | 15.22 | 6.00 | 82.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.48 | 7.98 | 13.24 | 1.00 | 77.0 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.42 | 6.82 | 11.13 | 1.00 | 79.2 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.77 | 2.89 | 5.36 | 0.00 | 31.8 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 5.77 | 17.81 | 30.51 | 5.00 | 74.7 | 90.0 |
| XI | Bench | Danny Welbeck | FWD | 5 | 5.9 | 3.09 | 9.39 | 15.56 | 0.00 | 68.3 | 0.0 |
| Bench 2 | Autosub In | Alexander Isak | FWD | 15 | 8.5 | 2.09 | 8.25 | 14.53 | 11.00 | 31.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 7.46 | 20.72 | 33.72 | 7.00 | 90.0 | 78.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.51 | 12.57 | 21.89 | 2.00 | 70.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.8 | 3.74 | 11.63 | 20.45 | 2.00 | 74.0 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.75 | 10.74 | 17.39 | 15.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.26 | 3.67 | 6.71 | 0.00 | 25.8 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.80 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 58.05
- Actual score: 102.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.07) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Harry Winks -> Morgan Rogers (projected gain 10.89, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.07) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.73 | 11.04 | 17.98 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.20 | 0.22 | 0.30 | 0.00 | 1.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.00 | 9.53 | 16.22 | 3.00 | 69.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.85 | 9.16 | 14.98 | 1.00 | 82.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.4 | 2.63 | 7.62 | 12.24 | 1.00 | 77.2 | 82.0 |
| Bench 2 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.28 | 6.60 | 10.68 | 1.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.20 | 1.70 | 3.56 | 0.00 | 19.3 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.16 | 18.50 | 31.52 | 7.00 | 86.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.5 | 4.32 | 12.63 | 20.92 | 8.00 | 72.8 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 5 | 5.9 | 1.97 | 5.75 | 10.57 | 1.00 | 32.8 | 20.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 10.9 | 6.70 | 19.47 | 31.70 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.38 | 13.90 | 23.33 | 9.00 | 84.1 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.22 | 11.12 | 18.06 | 2.00 | 76.5 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.28 | 10.72 | 17.80 | 2.00 | 82.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.37 | 10.18 | 18.13 | 13.00 | 71.2 | 90.0 |
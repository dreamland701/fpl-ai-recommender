# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 236.29
- Total actual points: 240.00
- Average predicted points: 59.07
- Average actual points: 60.00
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
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.88
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.52 | 10.08 | 16.28 | 6.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.35 | 1.02 | 1.43 | 0.00 | 12.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.63 | 12.66 | 20.18 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.30 | 12.15 | 19.82 | 0.00 | 88.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.83 | 10.38 | 16.79 | 0.00 | 88.6 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 4.2 | 2.70 | 7.92 | 12.79 | 0.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.48 | 6.78 | 10.98 | 2.00 | 82.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 8.07 | 22.29 | 36.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.21 | 12.53 | 20.85 | 16.00 | 84.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.84 | 11.92 | 18.79 | 2.00 | 79.8 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 7.92 | 22.23 | 36.15 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.97 | 16.36 | 26.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.66 | 12.49 | 20.18 | 1.00 | 85.3 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.86 | 11.07 | 17.70 | 2.00 | 78.3 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.20 | 9.17 | 14.55 | 1.00 | 79.3 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.33
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.90).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.48, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.90).
- Autosub: Wout Faes replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 10.73 | 17.18 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.69 | 1.20 | 1.65 | 0.00 | 11.6 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.66 | 11.53 | 19.22 | 0.00 | 87.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.81 | 11.35 | 18.12 | 6.00 | 86.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.10 | 9.28 | 15.10 | 2.00 | 81.3 | 90.0 |
| Bench 2 | Autosub In | Wout Faes | DEF | 11 | 4.1 | 2.51 | 7.30 | 11.97 | 0.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.23 | 6.91 | 11.15 | 1.00 | 81.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 5.96 | 18.46 | 31.74 | 2.00 | 82.3 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 5.96 | 17.39 | 26.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.85 | 10.52 | 17.01 | 2.00 | 73.8 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.16 | 24.31 | 38.47 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.84 | 13.18 | 21.27 | 9.00 | 73.1 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.61 | 10.90 | 17.64 | 5.00 | 85.4 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.17 | 9.66 | 15.93 | 2.00 | 70.3 | 65.0 |
| Bench 4 | Bench | Harry Winks | MID | 11 | 4.5 | 1.30 | 5.24 | 9.42 | 0.00 | 30.6 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.40
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.07) beats the best remaining Bench Boost opportunity (0.25).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.07) beats the best remaining Bench Boost opportunity (0.25).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.51 | 9.84 | 16.12 | 6.00 | 84.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.75 | 1.31 | 0.00 | 9.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.61 | 13.80 | 22.63 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.93 | 11.58 | 18.71 | 1.00 | 85.1 | 28.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.23 | 9.31 | 15.27 | 6.00 | 80.9 | 90.0 |
| Bench 2 | Bench Boost | Wout Faes | DEF | 11 | 4.1 | 2.53 | 6.82 | 11.19 | 1.00 | 78.9 | 30.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.34 | 6.78 | 11.14 | 1.00 | 77.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.11 | 19.00 | 32.44 | 5.00 | 81.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.14 | 13.67 | 21.32 | 2.00 | 73.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.08 | 9.52 | 15.89 | 0.00 | 68.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.78 | 24.11 | 38.80 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.60 | 13.04 | 22.59 | 2.00 | 72.6 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.71 | 10.89 | 17.90 | 15.00 | 80.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.86 | 8.37 | 14.07 | 8.00 | 60.8 | 86.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.98 | 3.15 | 5.77 | 0.00 | 19.7 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 47.68
- Actual score: 38.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 6.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.76 | 10.93 | 17.56 | 2.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.55 | 1.00 | 1.42 | 0.00 | 10.9 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.86 | 16.56 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.11 | 9.48 | 16.07 | 3.00 | 71.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.91 | 9.24 | 15.08 | 1.00 | 84.0 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.32 | 6.64 | 10.79 | 1.00 | 78.5 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 1.69 | 5.18 | 9.00 | 1.00 | 55.1 | 9.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.48 | 19.20 | 32.55 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.74 | 13.47 | 21.60 | 1.00 | 84.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.14 | 11.07 | 17.32 | 2.00 | 59.9 | 70.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.34 | 38.70 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.44 | 14.19 | 24.00 | 9.00 | 85.2 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.23 | 11.35 | 18.18 | 2.00 | 77.1 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.39 | 11.19 | 18.27 | 2.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 0.24 | 1.86 | 3.92 | 0.00 | 5.1 | 0.0 |
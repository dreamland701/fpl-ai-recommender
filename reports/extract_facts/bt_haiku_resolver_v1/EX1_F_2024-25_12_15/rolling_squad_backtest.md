# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 232.47
- Total actual points: 238.00
- Average predicted points: 58.12
- Average actual points: 59.50
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
- Predicted score: 62.44
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.46 | 10.00 | 16.23 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.82 | 1.24 | 0.00 | 8.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.60 | 12.62 | 20.16 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.25 | 12.08 | 19.78 | 0.00 | 86.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.79 | 10.33 | 16.77 | 0.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 4.2 | 2.65 | 7.85 | 12.74 | 0.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 2.21 | 7.10 | 11.71 | 0.00 | 83.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 8.04 | 22.29 | 36.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.17 | 12.49 | 20.83 | 16.00 | 83.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.81 | 11.88 | 18.77 | 2.00 | 78.8 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 7.92 | 22.23 | 36.19 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.95 | 16.34 | 26.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.62 | 12.45 | 20.17 | 1.00 | 84.2 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.81 | 11.00 | 17.66 | 2.00 | 77.0 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.17 | 9.13 | 14.53 | 1.00 | 78.5 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.93
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.89).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.53, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.89).
- Autosub: Wout Faes replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 10.66 | 17.15 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.57 | 1.02 | 1.49 | 0.00 | 7.9 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.63 | 11.48 | 19.19 | 0.00 | 87.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.28 | 18.08 | 6.00 | 85.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.06 | 9.23 | 15.07 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Autosub In | Wout Faes | DEF | 11 | 4.1 | 2.46 | 7.22 | 11.92 | 0.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.83 | 3.31 | 6.00 | 0.00 | 36.3 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 5.93 | 18.43 | 31.75 | 2.00 | 81.5 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 5.95 | 17.38 | 26.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.80 | 10.45 | 16.96 | 2.00 | 72.5 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.16 | 24.32 | 38.52 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.81 | 13.15 | 21.28 | 9.00 | 72.2 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.57 | 10.85 | 17.63 | 5.00 | 84.5 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.11 | 9.59 | 15.89 | 2.00 | 68.7 | 65.0 |
| Bench 3 | Bench | Harry Winks | MID | 11 | 4.5 | 1.39 | 4.95 | 8.61 | 0.00 | 33.4 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.61
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.27) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.27) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.57 | 9.93 | 16.14 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.72 | 1.20 | 0.00 | 8.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.77 | 14.04 | 22.86 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.01 | 11.70 | 18.73 | 1.00 | 86.8 | 28.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.31 | 9.41 | 15.29 | 6.00 | 82.5 | 90.0 |
| Bench 2 | Bench Boost | Wout Faes | DEF | 11 | 4.1 | 2.60 | 6.92 | 11.20 | 1.00 | 80.4 | 30.0 |
| Bench 4 | Bench Boost | Jan Bednarek | DEF | 17 | 4.0 | 0.46 | 2.03 | 3.94 | 0.00 | 25.0 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.18 | 19.11 | 32.47 | 5.00 | 83.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.21 | 13.79 | 21.35 | 2.00 | 75.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.13 | 9.59 | 15.86 | 0.00 | 69.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.90 | 24.29 | 38.90 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.66 | 13.13 | 22.59 | 2.00 | 73.7 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.79 | 11.00 | 17.93 | 15.00 | 81.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.91 | 8.42 | 14.03 | 8.00 | 61.5 | 86.0 |
| Bench 3 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.98 | 3.15 | 5.72 | 0.00 | 19.5 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 45.49
- Actual score: 37.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 6.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.70 | 10.86 | 17.51 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.43 | 0.81 | 1.26 | 0.00 | 7.2 | 0.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.82 | 16.63 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.01 | 9.35 | 15.96 | 3.00 | 69.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.86 | 9.18 | 15.04 | 1.00 | 82.8 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 1.86 | 5.43 | 9.28 | 1.00 | 60.9 | 9.0 |
| Bench 3 | Bench | Jan Bednarek | DEF | 17 | 4.0 | 0.00 | 0.87 | 2.21 | 0.00 | 13.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.46 | 19.17 | 32.55 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.69 | 13.41 | 21.58 | 1.00 | 83.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.12 | 11.06 | 17.33 | 2.00 | 59.3 | 70.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.36 | 38.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.52 | 14.29 | 24.01 | 9.00 | 87.1 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.18 | 11.28 | 18.13 | 2.00 | 75.7 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.34 | 11.14 | 18.25 | 2.00 | 84.3 | 90.0 |
| XI | Bench | Harry Winks | MID | 11 | 4.5 | 0.29 | 1.44 | 3.02 | 0.00 | 6.5 | 0.0 |
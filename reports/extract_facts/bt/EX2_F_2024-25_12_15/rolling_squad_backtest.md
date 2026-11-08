# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 236.01
- Total actual points: 240.00
- Average predicted points: 59.00
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
- Predicted score: 62.86
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.52 | 10.10 | 16.33 | 6.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.35 | 1.02 | 1.43 | 0.00 | 12.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.64 | 12.68 | 20.21 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.30 | 12.17 | 19.86 | 0.00 | 88.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.84 | 10.41 | 16.85 | 0.00 | 88.7 | 90.0 |
| Bench 3 | Bench | Wout Faes | DEF | 11 | 4.2 | 2.71 | 7.94 | 12.83 | 0.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.48 | 6.79 | 11.00 | 2.00 | 82.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.2 | 8.04 | 22.25 | 36.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.8 | 4.22 | 12.56 | 20.89 | 16.00 | 84.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.84 | 11.92 | 18.80 | 2.00 | 79.9 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 7.92 | 22.23 | 36.16 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.97 | 16.38 | 26.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.67 | 12.53 | 20.23 | 1.00 | 85.5 | 58.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.86 | 11.08 | 17.72 | 2.00 | 78.4 | 81.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 3.21 | 9.20 | 14.60 | 1.00 | 79.5 | 10.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.37
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.90).
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 1.49, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.16) beats the best remaining Triple Captain opportunity (8.90).
- Autosub: Wout Faes replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.89 | 10.76 | 17.23 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.69 | 1.19 | 1.64 | 0.00 | 11.6 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.66 | 11.54 | 19.25 | 0.00 | 88.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.81 | 11.36 | 18.15 | 6.00 | 86.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.12 | 9.32 | 15.16 | 2.00 | 81.4 | 90.0 |
| Bench 2 | Autosub In | Wout Faes | DEF | 11 | 4.1 | 2.52 | 7.31 | 12.01 | 0.00 | 81.3 | 90.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 4.0 | 2.24 | 6.93 | 11.18 | 1.00 | 81.1 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 15.1 | 5.94 | 18.40 | 31.68 | 2.00 | 82.3 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 5.97 | 17.43 | 26.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.84 | 10.51 | 17.01 | 2.00 | 73.9 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.16 | 24.33 | 38.45 | 13.00 | 90.0 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.85 | 13.18 | 21.29 | 9.00 | 73.2 | 65.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.62 | 10.93 | 17.70 | 5.00 | 85.5 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.17 | 9.66 | 15.94 | 2.00 | 70.3 | 65.0 |
| Bench 4 | Bench | Harry Winks | MID | 11 | 4.5 | 1.31 | 5.24 | 9.43 | 0.00 | 30.9 | 0.0 |

## GW14

- Train rows: 142282
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.04
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.10) beats the best remaining Bench Boost opportunity (0.26).
- Transfer: Joško Gvardiol -> Pedro Porro (projected gain 3.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.10) beats the best remaining Bench Boost opportunity (0.26).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.52 | 9.86 | 16.17 | 6.00 | 84.2 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.23 | 0.75 | 1.31 | 0.00 | 9.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.15 | 12.57 | 20.48 | 1.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.93 | 11.60 | 18.74 | 1.00 | 85.2 | 28.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.24 | 9.33 | 15.31 | 6.00 | 81.1 | 90.0 |
| Bench 2 | Bench Boost | Wout Faes | DEF | 11 | 4.1 | 2.54 | 6.84 | 11.23 | 1.00 | 79.0 | 30.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 4.0 | 2.35 | 6.80 | 11.18 | 1.00 | 77.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 15.0 | 6.09 | 18.95 | 32.38 | 5.00 | 81.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.15 | 13.68 | 21.33 | 2.00 | 73.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.9 | 3.08 | 9.53 | 15.91 | 0.00 | 68.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.1 | 7.79 | 24.13 | 38.83 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.62 | 13.06 | 22.65 | 2.00 | 72.9 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.73 | 10.91 | 17.94 | 15.00 | 80.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 2.87 | 8.37 | 14.09 | 8.00 | 60.9 | 86.0 |
| Bench 4 | Bench Boost | Harry Winks | MID | 11 | 4.5 | 0.99 | 3.16 | 5.81 | 0.00 | 19.9 | 0.0 |

## GW15

- Train rows: 142975
- Bank: 0.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 47.74
- Actual score: 38.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 6.18, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.77 | 10.96 | 17.60 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.55 | 0.99 | 1.42 | 0.00 | 10.9 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 0.00 | 9.87 | 16.58 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.11 | 9.49 | 16.08 | 3.00 | 72.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 2.92 | 9.27 | 15.13 | 1.00 | 84.1 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 4.0 | 2.32 | 6.65 | 10.81 | 1.00 | 78.6 | 90.0 |
| XI | XI | Wout Faes | DEF | 11 | 4.1 | 1.69 | 5.18 | 9.01 | 1.00 | 55.1 | 9.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.47 | 19.17 | 32.53 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 6.9 | 4.74 | 13.46 | 21.59 | 1.00 | 84.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.9 | 4.15 | 11.09 | 17.34 | 2.00 | 60.0 | 70.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.1 | 0.00 | 23.35 | 38.69 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 4.45 | 14.19 | 24.01 | 9.00 | 85.4 | 75.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.3 | 4.24 | 11.37 | 18.21 | 2.00 | 77.3 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.40 | 11.21 | 18.31 | 2.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Harry Winks | MID | 11 | 4.5 | 0.24 | 1.85 | 3.91 | 0.00 | 5.3 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 409.64
- Total actual points: 408.00
- Average predicted points: 58.52
- Average actual points: 58.29
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW2

- Train rows: 134294
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.52
- Actual score: 74.00
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.52 | 10.91 | 18.28 | 10.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.0 | 3.29 | 9.95 | 16.81 | 3.00 | 86.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 5.89 | 17.43 | 28.89 | 6.00 | 101.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 5.18 | 15.49 | 25.81 | 6.00 | 82.5 | 71.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.26 | 12.00 | 19.94 | 2.00 | 90.4 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.0 | 3.59 | 10.68 | 17.40 | 6.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Dan Burn | DEF | 15 | 4.5 | 3.43 | 10.22 | 17.00 | 1.00 | 87.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.5 | 4.50 | 13.07 | 21.86 | 9.00 | 91.8 | 78.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.0 | 3.78 | 12.03 | 19.92 | 2.00 | 78.4 | 72.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.37 | 9.82 | 15.90 | 2.00 | 70.3 | 70.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 6.71 | 20.00 | 33.49 | 10.00 | 92.9 | 82.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 6.53 | 19.85 | 32.93 | 6.00 | 89.2 | 87.0 |
| XI | XI | Mitoma Kaoru | MID | 5 | 6.5 | 5.43 | 15.21 | 24.50 | 6.00 | 84.4 | 89.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 12 | 7.5 | 4.76 | 14.00 | 23.12 | 6.00 | 76.6 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.0 | 4.24 | 13.67 | 23.04 | 1.00 | 88.7 | 90.0 |

## GW3

- Train rows: 134921
- Bank: 0.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.80
- Actual score: 66.00
- League average score: 0.00
- Transfer: Bryan Mbeumo -> Antoine Semenyo (projected gain 2.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 11.40 | 18.71 | 2.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.0 | 3.23 | 9.46 | 15.53 | 4.00 | 84.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 5.34 | 16.16 | 26.46 | 6.00 | 78.8 | 75.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 5.00 | 15.53 | 25.69 | 1.00 | 95.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.90 | 11.57 | 18.61 | 2.00 | 83.1 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.96 | 11.54 | 18.38 | 2.00 | 82.4 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | 15 | 4.5 | 3.49 | 9.88 | 16.12 | 0.00 | 84.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.5 | 3.32 | 11.15 | 18.29 | 2.00 | 74.5 | 84.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | 4 | 6.0 | 3.20 | 9.05 | 14.87 | 8.00 | 63.7 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.43 | 7.29 | 11.62 | 1.00 | 55.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.5 | 6.31 | 19.40 | 31.56 | 17.00 | 84.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.90 | 17.76 | 29.00 | 6.00 | 83.0 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 12 | 7.6 | 4.54 | 13.65 | 21.90 | 3.00 | 67.5 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 4.55 | 13.28 | 21.66 | 6.00 | 84.3 | 90.0 |
| XI | XI | Mitoma Kaoru | MID | 5 | 6.5 | 3.88 | 12.40 | 20.26 | 2.00 | 79.5 | 84.0 |

## GW4

- Train rows: 135569
- Bank: 1.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.35
- Actual score: 41.00
- League average score: 0.00
- Transfer: Jamie Vardy -> João Pedro Junqueira de Jesus (projected gain 0.43, hit 0)
- Autosub outfielders: Yoane Wissa.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.48 | 10.99 | 17.96 | 9.00 | 82.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.0 | 2.96 | 9.01 | 15.06 | 3.00 | 82.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.76 | 14.44 | 24.03 | 1.00 | 74.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.20 | 13.45 | 22.29 | 2.00 | 85.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.90 | 11.65 | 19.25 | 1.00 | 80.3 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.66 | 10.97 | 17.72 | 5.00 | 80.1 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | 15 | 4.5 | 2.88 | 8.60 | 14.22 | 1.00 | 79.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 4.04 | 11.61 | 18.41 | 0.00 | 77.0 | 0.0 |
| Bench 2 | Autosub In | Yoane Wissa | FWD | 4 | 6.1 | 3.63 | 11.25 | 18.11 | 7.00 | 73.9 | 45.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 5 | 5.6 | 3.56 | 10.61 | 16.81 | 2.00 | 65.5 | 84.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.6 | 6.95 | 21.06 | 34.72 | 2.00 | 94.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.90 | 17.61 | 28.85 | 7.00 | 81.5 | 85.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.5 | 4.56 | 13.15 | 21.35 | 1.00 | 83.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 12 | 7.6 | 3.95 | 12.23 | 20.19 | 1.00 | 61.4 | 59.0 |
| XI | XI | Mitoma Kaoru | MID | 5 | 6.6 | 4.00 | 11.36 | 18.45 | 3.00 | 72.1 | 90.0 |

## GW5

- Train rows: 136228
- Bank: 1.50 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.05
- Actual score: 64.00
- League average score: 0.00
- Transfer: Diogo Teixeira da Silva -> Luis Díaz (projected gain 2.74, hit 0)
- Autosub outfielders: Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.43 | 10.98 | 18.51 | 4.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.0 | 2.87 | 8.86 | 14.68 | 3.00 | 83.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.0 | 4.54 | 13.56 | 22.48 | 11.00 | 73.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.37 | 13.29 | 22.11 | 2.00 | 85.4 | 87.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.36 | 10.36 | 17.11 | 1.00 | 78.2 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 6.0 | 2.83 | 9.53 | 16.25 | 1.00 | 62.0 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | 15 | 4.5 | 2.68 | 8.18 | 13.61 | 1.00 | 78.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.7 | 3.68 | 11.37 | 17.75 | 6.00 | 68.1 | 90.0 |
| XI | Bench | Yoane Wissa | FWD | 4 | 6.1 | 3.25 | 10.22 | 16.87 | 0.00 | 60.3 | 0.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 2.72 | 9.34 | 14.71 | 1.00 | 38.9 | 19.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 6.41 | 19.88 | 32.17 | 6.00 | 81.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.11 | 16.12 | 26.90 | 4.00 | 76.3 | 45.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.7 | 4.11 | 13.04 | 20.79 | 16.00 | 51.6 | 71.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.6 | 3.61 | 11.74 | 19.10 | 2.00 | 76.3 | 69.0 |
| XI | XI | Mitoma Kaoru | MID | 5 | 6.7 | 3.76 | 11.65 | 18.77 | 5.00 | 70.8 | 90.0 |

## GW6

- Train rows: 136889
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.86
- Actual score: 48.00
- League average score: 0.00
- Transfer: Antoine Semenyo -> Emile Smith Rowe (projected gain 2.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.19 | 11.77 | 19.39 | 1.00 | 93.2 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.0 | 2.77 | 8.73 | 14.65 | 3.00 | 86.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.94 | 14.13 | 23.53 | 1.00 | 84.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.31 | 12.91 | 21.30 | 5.00 | 87.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.42 | 10.73 | 17.81 | 9.00 | 75.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.85 | 10.42 | 16.95 | 0.00 | 81.6 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | 15 | 4.5 | 2.62 | 8.11 | 13.53 | 2.00 | 79.5 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 3.66 | 11.41 | 18.50 | 2.00 | 76.4 | 80.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 2.28 | 8.00 | 14.31 | 0.00 | 41.7 | 0.0 |
| Bench 4 | Bench | Yoane Wissa | FWD | 4 | 6.1 | 2.20 | 6.81 | 11.83 | 0.00 | 31.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 7.02 | 20.75 | 34.32 | 10.00 | 91.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.0 | 5.45 | 15.96 | 26.44 | 3.00 | 71.5 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.8 | 5.10 | 15.33 | 25.10 | 2.00 | 72.2 | 72.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.7 | 4.15 | 12.52 | 20.14 | 3.00 | 77.0 | 87.0 |
| XI | XI | Mitoma Kaoru | MID | 5 | 6.7 | 3.76 | 11.31 | 18.77 | 2.00 | 76.1 | 90.0 |

## GW7

- Train rows: 137553
- Bank: 1.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.99
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (7.84).
- League average score: 0.00
- Transfer: Mitoma Kaoru -> Bryan Mbeumo (projected gain 3.07, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (7.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.93 | 11.27 | 18.38 | 2.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.0 | 2.64 | 8.25 | 14.04 | 6.00 | 83.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.26 | 13.01 | 21.85 | 8.00 | 78.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.11 | 12.26 | 20.54 | 1.00 | 83.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.89 | 11.37 | 18.86 | 1.00 | 79.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.63 | 9.98 | 16.06 | 2.00 | 75.4 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | 15 | 4.5 | 2.59 | 7.68 | 12.91 | 8.00 | 75.8 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 3.96 | 11.40 | 18.80 | 8.00 | 71.7 | 90.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | 4 | 6.0 | 1.51 | 5.30 | 9.59 | 0.00 | 22.7 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 1.32 | 5.17 | 9.82 | 0.00 | 13.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.8 | 6.39 | 18.80 | 31.51 | 3.00 | 81.8 | 72.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.97 | 17.24 | 27.70 | 16.00 | 75.5 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 8.0 | 4.36 | 14.18 | 22.67 | 1.00 | 56.0 | 17.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.3 | 4.64 | 13.93 | 21.86 | 8.00 | 79.0 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 4.06 | 12.48 | 20.20 | 1.00 | 73.6 | 25.0 |

## GW8

- Train rows: 138219
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.07
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.88) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: William Saliba -> Gabriel dos Santos Magalhães (projected gain 2.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.88) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 11.33 | 18.70 | 1.00 | 88.0 | 90.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.0 | 3.08 | 9.17 | 15.32 | 3.00 | 86.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.70 | 13.81 | 23.09 | 2.00 | 85.3 | 80.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.15 | 11.98 | 19.74 | 2.00 | 84.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 3.92 | 11.53 | 18.21 | 1.00 | 76.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.97 | 11.48 | 18.66 | 10.00 | 83.5 | 90.0 |
| Bench 2 | Bench Boost | Dan Burn | DEF | 15 | 4.4 | 3.00 | 8.69 | 14.26 | 1.00 | 82.1 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 5.8 | 4.23 | 12.18 | 19.85 | 9.00 | 82.9 | 80.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 0.87 | 4.24 | 8.19 | 0.00 | 15.4 | 0.0 |
| Bench 3 | Bench Boost | Yoane Wissa | FWD | 4 | 5.9 | 0.93 | 3.96 | 7.37 | 1.00 | 14.3 | 24.0 |
| Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 6.56 | 19.51 | 32.14 | 0.00 | 90.5 | 0.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 6.05 | 17.98 | 30.13 | 12.00 | 74.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.4 | 4.98 | 15.20 | 24.54 | 2.00 | 87.4 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 8.1 | 4.08 | 12.62 | 21.60 | 1.00 | 49.8 | 24.0 |
| XI | XI | Emile Smith Rowe | MID | 9 | 5.8 | 3.28 | 9.80 | 16.96 | 1.00 | 53.6 | 79.0 |
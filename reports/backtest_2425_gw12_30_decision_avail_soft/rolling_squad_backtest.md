# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1191.09
- Total actual points: 1270.00
- Average predicted points: 62.69
- Average actual points: 66.84
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.18
- Actual score: 58.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.36 | 9.76 | 15.77 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 4.9 | 3.13 | 9.09 | 14.54 | 6.00 | 85.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.3 | 4.46 | 12.58 | 20.02 | 0.00 | 87.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.2 | 4.18 | 11.29 | 17.77 | 1.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.5 | 3.72 | 11.01 | 17.74 | 14.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.7 | 3.60 | 10.70 | 17.01 | 2.00 | 86.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 3.91 | 10.62 | 16.72 | 0.00 | 87.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 6.7 | 4.11 | 11.83 | 18.81 | 16.00 | 85.0 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.73 | 11.72 | 18.46 | 1.00 | 76.6 | 27.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | -1 | 5.9 | 3.68 | 10.93 | 17.18 | 2.00 | 77.2 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.8 | 6.52 | 18.57 | 29.56 | 13.00 | 88.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.0 | 5.88 | 16.66 | 27.16 | 2.00 | 87.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.14 | 15.50 | 24.79 | 3.00 | 94.1 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | -1 | 5.7 | 4.49 | 12.02 | 18.94 | 1.00 | 82.1 | 58.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.89 | 10.93 | 17.62 | 2.00 | 74.5 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.25
- Actual score: 65.00
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 0.56, hit 0)
- Autosub outfielders: Antonee Robinson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.76 | 10.49 | 16.61 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 4.9 | 3.14 | 9.22 | 14.88 | 0.00 | 84.2 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | -1 | 6.3 | 4.16 | 12.97 | 20.91 | 0.00 | 91.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.30 | 12.14 | 19.55 | 2.00 | 93.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.3 | 3.63 | 10.97 | 17.61 | 6.00 | 83.0 | 90.0 |
| Bench 2 | Autosub In | Antonee Robinson | DEF | -1 | 4.7 | 3.54 | 10.17 | 16.21 | 2.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 3.42 | 9.81 | 15.64 | 0.00 | 84.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 6.8 | 4.85 | 13.75 | 21.59 | 2.00 | 93.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 6.0 | 4.06 | 10.98 | 17.26 | 2.00 | 76.4 | 78.0 |
| Bench 4 | Bench | Chris Wood | FWD | -1 | 6.6 | 3.51 | 10.44 | 17.10 | 9.00 | 55.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.0 | 6.97 | 20.41 | 31.89 | 13.00 | 95.1 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 10.9 | 5.86 | 16.71 | 26.65 | 14.00 | 86.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.08 | 14.49 | 23.64 | 2.00 | 86.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.64 | 10.83 | 17.55 | 2.00 | 73.6 | 65.0 |
| XI | XI | Alex Iwobi | MID | -1 | 5.6 | 3.97 | 10.74 | 16.66 | 5.00 | 86.7 | 85.0 |

## GW14

- Train rows: 142282
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.64
- Actual score: 81.00
- Transfer: Morgan Rogers -> Justin Kluivert (projected gain 1.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.69 | 10.06 | 15.90 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 4.9 | 3.04 | 8.68 | 14.14 | 6.00 | 81.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.01 | 11.82 | 18.92 | 1.00 | 86.8 | 28.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.3 | 3.93 | 11.70 | 18.66 | 1.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 3.35 | 9.78 | 15.64 | 0.00 | 84.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 3.46 | 9.74 | 15.51 | 6.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Joško Gvardiol | DEF | -1 | 6.3 | 2.91 | 9.34 | 16.06 | 6.00 | 51.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.0 | 4.49 | 13.85 | 21.77 | 2.00 | 81.8 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.56 | 11.19 | 17.91 | 2.00 | 75.1 | 61.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | -1 | 6.0 | 3.41 | 10.23 | 16.61 | 0.00 | 70.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.1 | 7.41 | 21.59 | 33.60 | 18.00 | 99.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 10.9 | 6.60 | 17.96 | 28.23 | 7.00 | 93.3 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 4.46 | 13.58 | 22.19 | 2.00 | 86.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.3 | 4.56 | 11.38 | 17.07 | 3.00 | 76.9 | 63.0 |
| XI | XI | Alex Iwobi | MID | -1 | 5.6 | 4.06 | 11.15 | 17.30 | 15.00 | 83.9 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 54.56
- Actual score: 73.00
- Transfer: Justin Kluivert -> Morgan Rogers (projected gain 2.26, hit 0)
- Autosub outfielders: Chris Wood.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.54 | 10.22 | 16.19 | 2.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 4.9 | 2.04 | 8.29 | 13.72 | 0.00 | 53.8 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 3.97 | 11.61 | 18.88 | 1.00 | 75.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 3.42 | 10.15 | 16.63 | 3.00 | 70.5 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 2.46 | 9.90 | 16.41 | 0.00 | 54.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 3.14 | 9.65 | 15.42 | 1.00 | 85.9 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 4.9 | 3.20 | 8.66 | 13.83 | 4.00 | 82.0 | 85.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.65 | 13.09 | 20.69 | 1.00 | 85.1 | 90.0 |
| Bench 2 | Autosub In | Chris Wood | FWD | -1 | 6.6 | 3.37 | 10.24 | 16.68 | 8.00 | 60.7 | 78.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | -1 | 5.9 | 2.57 | 7.53 | 12.91 | 1.00 | 39.5 | 20.0 |
| Captain | Bench | Mohamed Salah | MID | -1 | 13.2 | 6.99 | 22.36 | 35.42 | 0.00 | 77.8 | 0.0 |
| Vice Captain | Captain | Cole Palmer | MID | -1 | 11.0 | 6.63 | 18.43 | 28.57 | 18.00 | 89.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 3.91 | 11.91 | 20.40 | 13.00 | 76.2 | 90.0 |
| XI | XI | Alex Iwobi | MID | -1 | 5.6 | 4.09 | 11.88 | 18.83 | 2.00 | 89.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.3 | 4.04 | 11.00 | 17.37 | 2.00 | 73.7 | 90.0 |

## GW16

- Train rows: 143668
- Bank: 0.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 56.55
- Actual score: 60.00
- Transfer: Virgil van Dijk -> William Saliba (projected gain 1.65, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.46 | 9.97 | 15.83 | 6.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 4.9 | 1.33 | 5.18 | 9.11 | 8.00 | 45.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 4.08 | 11.61 | 18.68 | 6.00 | 84.1 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 4.03 | 11.28 | 18.08 | 7.00 | 74.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.1 | 3.71 | 10.13 | 15.22 | 6.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | -1 | 4.7 | 2.71 | 8.66 | 14.17 | 6.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.9 | 3.13 | 8.54 | 13.78 | -2.00 | 79.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.25 | 12.14 | 19.38 | 9.00 | 78.4 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.5 | 3.95 | 11.06 | 17.53 | 2.00 | 72.8 | 90.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | -1 | 5.9 | 2.27 | 7.02 | 12.19 | 0.00 | 39.9 | 0.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 11.0 | 7.75 | 21.25 | 33.07 | 3.00 | 105.4 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.2 | 6.11 | 18.37 | 30.20 | 5.00 | 64.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.7 | 4.31 | 13.16 | 21.99 | 9.00 | 85.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.3 | 3.77 | 11.19 | 17.72 | 2.00 | 76.6 | 90.0 |
| XI | XI | Alex Iwobi | MID | -1 | 5.6 | 3.38 | 10.61 | 17.14 | 2.00 | 82.5 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.80 -> 1.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 58.06
- Actual score: 68.00
- Transfer: Alex Iwobi -> Enzo Fernández (projected gain 1.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.75 | 10.80 | 17.06 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 4.9 | 2.87 | 8.16 | 13.31 | 7.00 | 73.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.1 | 3.81 | 11.73 | 19.08 | 0.00 | 85.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.2 | 3.98 | 11.34 | 17.27 | 2.00 | 76.0 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.6 | 3.36 | 10.54 | 17.17 | -1.00 | 75.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.7 | 3.96 | 10.53 | 16.87 | 6.00 | 91.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.9 | 3.18 | 8.68 | 13.81 | 0.00 | 79.6 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.75 | 13.30 | 21.25 | 9.00 | 84.2 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.67 | 10.53 | 16.56 | 2.00 | 71.3 | 90.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | -1 | 5.8 | 1.69 | 5.48 | 9.97 | 0.00 | 25.3 | 0.0 |
| Captain | Captain | Cole Palmer | MID | -1 | 11.1 | 7.50 | 21.22 | 33.09 | 3.00 | 100.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 13.4 | 6.78 | 20.25 | 33.08 | 21.00 | 83.2 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.66 | 13.75 | 22.48 | 2.00 | 90.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.0 | 3.89 | 11.63 | 18.17 | 3.00 | 78.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.81 | 10.80 | 17.22 | 14.00 | 80.0 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 1.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.90
- Actual score: 64.00
- Transfer: Chris Wood -> Dominic Solanke-Mitchell (projected gain 0.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.95 | 11.02 | 17.54 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 4.9 | 2.65 | 8.26 | 13.67 | 9.00 | 73.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.8 | 3.68 | 11.47 | 18.31 | 1.00 | 85.5 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 4.21 | 11.37 | 17.60 | 7.00 | 80.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 3.49 | 10.41 | 17.05 | 1.00 | 83.9 | 9.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | -1 | 6.1 | 3.47 | 10.01 | 16.10 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 1.32 | 4.64 | 9.26 | 6.00 | 34.4 | 86.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.82 | 13.19 | 21.46 | 12.00 | 86.7 | 90.0 |
| XI | XI | Dominic Solanke-Mitchell | FWD | -1 | 7.5 | 4.14 | 11.37 | 17.84 | 2.00 | 86.9 | 90.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | -1 | 5.7 | 1.23 | 4.45 | 8.54 | 0.00 | 20.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.4 | 8.27 | 22.92 | 36.45 | 9.00 | 95.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.2 | 7.18 | 20.60 | 32.60 | 10.00 | 99.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.71 | 13.74 | 22.13 | 3.00 | 89.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.3 | 4.08 | 12.12 | 19.63 | 2.00 | 83.7 | 68.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.1 | 4.09 | 11.26 | 17.89 | 2.00 | 82.1 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.41
- Actual score: 78.00
- Transfer: Dominic Solanke-Mitchell -> Kai Havertz (projected gain 0.71, hit 0)
- Autosub outfielders: Rayan Aït-Nouri.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.99 | 11.60 | 18.57 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 4.9 | 3.27 | 9.80 | 15.96 | 1.00 | 86.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 4.00 | 11.82 | 18.97 | 2.00 | 80.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 4.17 | 11.58 | 18.50 | 4.00 | 91.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.67 | 10.32 | 16.56 | 6.00 | 76.4 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | -1 | 5.5 | 2.97 | 9.10 | 15.48 | 4.00 | 55.1 | 90.0 |
| Bench 2 | Autosub In | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.60 | 7.63 | 12.42 | 10.00 | 68.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.77 | 14.01 | 23.05 | 1.00 | 91.9 | 45.0 |
| XI | Bench | Kai Havertz | FWD | -1 | 7.9 | 4.05 | 11.20 | 17.53 | 0.00 | 74.6 | 0.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | -1 | 5.6 | 0.58 | 3.30 | 6.82 | 0.00 | 14.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.5 | 8.70 | 24.26 | 38.09 | 16.00 | 104.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.3 | 7.02 | 20.73 | 33.72 | 2.00 | 94.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.32 | 13.41 | 21.82 | 7.00 | 85.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.1 | 4.23 | 11.34 | 18.08 | 1.00 | 83.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.4 | 3.81 | 11.14 | 18.07 | 11.00 | 74.6 | 90.0 |

## GW20

- Train rows: 146484
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.03
- Actual score: 66.00
- Transfer: Danny Welbeck -> João Pedro Junqueira de Jesus (projected gain 0.83, hit 0)
- Autosub outfielders: Pedro Porro, Rayan Aït-Nouri.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.83 | 11.12 | 17.97 | 3.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.0 | 2.98 | 9.09 | 14.77 | 4.00 | 83.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 4.41 | 12.01 | 19.09 | 1.00 | 89.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.82 | 11.20 | 18.17 | 2.00 | 79.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.86 | 10.46 | 16.34 | 2.00 | 79.3 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | -1 | 5.5 | 3.52 | 10.44 | 17.11 | 4.00 | 77.6 | 90.0 |
| Bench 3 | Autosub In | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.79 | 8.25 | 13.43 | 1.00 | 72.8 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 3.95 | 12.60 | 20.61 | 0.00 | 73.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 3.69 | 11.08 | 17.99 | 9.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Kai Havertz | FWD | -1 | 7.9 | 2.66 | 7.99 | 13.28 | 0.00 | 40.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 9.74 | 25.70 | 40.06 | 7.00 | 111.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 6.80 | 20.23 | 32.61 | 10.00 | 97.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 5.11 | 14.29 | 22.75 | 19.00 | 88.6 | 90.0 |
| XI | Bench | Morgan Rogers | MID | -1 | 5.5 | 4.95 | 13.16 | 20.77 | 0.00 | 87.2 | 0.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.1 | 4.13 | 11.64 | 18.48 | 1.00 | 86.7 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.64
- Actual score: 41.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Chris Wood (projected gain 4.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 4.05 | 11.20 | 17.89 | 2.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.0 | 3.02 | 8.98 | 14.48 | 1.00 | 87.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 4.23 | 12.19 | 19.61 | 7.00 | 87.0 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.99 | 10.72 | 17.04 | 2.00 | 80.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.28 | 10.18 | 16.45 | 1.00 | 79.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.51 | 10.14 | 16.10 | 1.00 | 78.5 | 90.0 |
| Bench 2 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.65 | 8.00 | 13.02 | 1.00 | 76.5 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.8 | 4.01 | 12.50 | 20.12 | 9.00 | 74.2 | 89.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 4.14 | 11.41 | 18.02 | 1.00 | 82.7 | 77.0 |
| Bench 4 | Bench | Kai Havertz | FWD | -1 | 7.9 | 2.26 | 6.98 | 12.15 | 1.00 | 29.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 8.80 | 25.04 | 39.63 | 2.00 | 101.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 7.26 | 20.65 | 33.23 | 10.00 | 104.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.7 | 5.84 | 16.75 | 26.32 | 2.00 | 100.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.1 | 3.74 | 10.73 | 17.28 | 2.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Morgan Rogers | MID | -1 | 5.5 | 2.42 | 8.09 | 14.19 | 6.00 | 42.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.82
- Actual score: 43.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Kai Havertz -> Cody Gakpo (projected gain 1.69, hit 0)
- Autosub outfielders: Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.63 | 10.46 | 16.85 | 1.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.0 | 3.21 | 8.93 | 14.17 | 2.00 | 82.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 4.62 | 12.69 | 20.20 | 8.00 | 91.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.63 | 10.29 | 16.29 | 1.00 | 82.2 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | -1 | 6.3 | 3.59 | 10.13 | 16.14 | 0.00 | 79.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.62 | 10.09 | 16.26 | 6.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.46 | 7.53 | 12.45 | 1.00 | 75.4 | 73.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.8 | 4.69 | 12.78 | 20.54 | 12.00 | 82.1 | 82.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.4 | 4.20 | 11.75 | 18.21 | 2.00 | 74.3 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 3.62 | 10.40 | 16.64 | 2.00 | 72.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.57 | 24.30 | 38.26 | 3.00 | 97.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 7.42 | 20.82 | 33.10 | 2.00 | 104.3 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.57 | 16.10 | 25.79 | 2.00 | 94.6 | 90.0 |
| Bench 3 | Autosub In | Morgan Rogers | MID | -1 | 5.5 | 3.42 | 10.95 | 17.76 | 1.00 | 73.8 | 90.0 |
| XI | Bench | Enzo Fernández | MID | -1 | 5.0 | 3.67 | 10.32 | 16.55 | 0.00 | 78.9 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.70 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.94
- Actual score: 72.00
- Transfer: Enzo Fernández -> Amad Diallo (projected gain 3.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.43 | 9.96 | 16.10 | 9.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.0 | 2.85 | 8.49 | 13.60 | 5.00 | 83.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 4.59 | 12.48 | 19.65 | 2.00 | 90.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 3.83 | 10.42 | 16.60 | 6.00 | 81.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.65 | 10.25 | 16.29 | 8.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.8 | 2.04 | 6.73 | 10.81 | 2.00 | 68.6 | 86.0 |
| Bench 4 | Bench | William Saliba | DEF | -1 | 6.3 | 2.09 | 6.60 | 11.24 | 9.00 | 43.4 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 4.80 | 14.28 | 22.72 | 2.00 | 82.0 | 90.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.4 | 4.33 | 11.66 | 18.13 | 16.00 | 71.1 | 67.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 3.45 | 9.96 | 15.91 | 1.00 | 73.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.33 | 23.38 | 36.76 | 8.00 | 92.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.4 | 6.59 | 19.43 | 31.35 | 2.00 | 95.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.65 | 15.77 | 25.22 | 7.00 | 94.1 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.5 | 4.74 | 13.54 | 21.64 | 3.00 | 89.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.5 | 3.66 | 10.15 | 16.23 | 1.00 | 70.3 | 71.0 |

## GW24

- Train rows: 149404
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 77.77
- Actual score: 127.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.40) beats the best remaining Bench Boost opportunity (15.73).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.64): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Morgan Rogers -> Justin Kluivert (projected gain 2.70, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.40) beats the best remaining Bench Boost opportunity (15.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Jordan Pickford | GK | -1 | 5.0 | 4.01 | 10.45 | 16.10 | 10.00 | 112.8 | 180.0 |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.53 | 10.41 | 16.85 | 3.00 | 86.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.96 | 11.86 | 19.21 | 4.00 | 87.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.51 | 10.73 | 17.31 | 0.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 3.54 | 10.54 | 17.00 | 6.00 | 83.4 | 90.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | -1 | 6.2 | 2.48 | 7.81 | 13.38 | 2.00 | 61.0 | 90.0 |
| Bench 3 | Bench Boost | Rayan Aït-Nouri | DEF | -1 | 4.7 | 2.54 | 7.45 | 11.77 | 7.00 | 71.8 | 72.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.5 | 6.11 | 15.03 | 22.74 | 7.00 | 99.1 | 137.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 4.61 | 13.69 | 22.01 | 17.00 | 84.5 | 81.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 3.09 | 9.65 | 15.42 | 1.00 | 71.6 | 45.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 9.43 | 24.92 | 38.83 | 29.00 | 122.8 | 177.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.3 | 6.64 | 18.89 | 30.48 | 6.00 | 94.5 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.80 | 16.30 | 25.86 | 2.00 | 89.7 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.6 | 4.81 | 13.13 | 20.68 | 2.00 | 90.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.6 | 4.29 | 12.71 | 20.30 | 2.00 | 83.6 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 86.47
- Actual score: 99.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.62) beats the best remaining Triple Captain opportunity (8.95).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: William Saliba -> Virgil van Dijk (projected gain 4.87, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (14.62) beats the best remaining Triple Captain opportunity (8.95).
- Autosub outfielders: Joško Gvardiol, João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | -1 | 5.1 | 4.66 | 13.17 | 20.12 | 3.00 | 118.0 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.5 | 3.52 | 10.04 | 16.46 | 7.00 | 81.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 6.16 | 15.11 | 22.26 | 2.00 | 146.9 | 180.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.90 | 11.62 | 18.71 | 2.00 | 86.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 3.75 | 10.43 | 16.60 | 6.00 | 85.6 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | -1 | 5.9 | 3.58 | 10.33 | 16.37 | 6.00 | 83.1 | 86.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.7 | 2.30 | 7.02 | 11.22 | 1.00 | 68.0 | 90.0 |
| XI | Bench | Cody Gakpo | FWD | -1 | 7.6 | 6.64 | 17.23 | 25.83 | 0.00 | 114.5 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 5.46 | 15.45 | 24.63 | 9.00 | 91.2 | 90.0 |
| Bench 3 | Autosub In | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 2.75 | 8.33 | 13.83 | 1.00 | 58.1 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 11.60 | 29.88 | 45.80 | 20.00 | 175.0 | 180.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.3 | 6.33 | 18.44 | 29.52 | 2.00 | 92.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.66 | 16.30 | 25.77 | 3.00 | 86.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.8 | 4.80 | 13.53 | 21.28 | 5.00 | 75.6 | 76.0 |
| XI | Bench | Amad Diallo | MID | -1 | 5.6 | 4.33 | 12.82 | 20.29 | 0.00 | 81.9 | 0.0 |

## GW26

- Train rows: 150945
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.03
- Actual score: 63.00
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 6.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.5 | 3.91 | 10.79 | 17.22 | 2.00 | 86.2 | 90.0 |
| XI | XI | Jordan Pickford | GK | -1 | 5.1 | 3.93 | 10.65 | 16.90 | 1.00 | 96.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 4.70 | 13.64 | 21.24 | 6.00 | 129.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.87 | 11.53 | 18.41 | 1.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 4.06 | 11.10 | 17.63 | 1.00 | 88.1 | 25.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.65 | 10.77 | 17.13 | 1.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.7 | 2.86 | 8.09 | 13.08 | 6.00 | 75.2 | 79.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 5.47 | 15.95 | 25.09 | 5.00 | 95.2 | 90.0 |
| Bench 3 | Bench | Cody Gakpo | FWD | -1 | 7.6 | 3.37 | 10.70 | 18.31 | 1.00 | 49.9 | 11.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 3.00 | 8.26 | 13.74 | 12.00 | 46.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 10.40 | 29.01 | 45.45 | 14.00 | 161.5 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 11.2 | 5.84 | 17.63 | 28.54 | 2.00 | 92.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.85 | 15.96 | 25.02 | 14.00 | 87.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.6 | 5.30 | 14.65 | 22.26 | 2.00 | 102.9 | 77.0 |
| XI | XI | Justin Kluivert | MID | -1 | 5.9 | 4.56 | 14.03 | 21.93 | 2.00 | 68.4 | 72.0 |

## GW27

- Train rows: 151728
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.18
- Actual score: 63.00
- Transfer: Cody Gakpo -> Jean-Philippe Mateta (projected gain 3.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.5 | 3.31 | 10.00 | 15.99 | 6.00 | 84.4 | 90.0 |
| XI | XI | Jordan Pickford | GK | -1 | 5.1 | 3.41 | 9.99 | 15.94 | 2.00 | 93.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 4.07 | 11.91 | 18.94 | 7.00 | 108.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.67 | 10.73 | 17.13 | 0.00 | 84.6 | 18.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.60 | 10.63 | 17.06 | 7.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | -1 | 5.4 | 3.00 | 9.13 | 15.03 | 2.00 | 66.0 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.7 | 3.01 | 8.26 | 13.14 | 1.00 | 73.4 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 5.73 | 16.84 | 26.79 | 2.00 | 101.3 | 84.0 |
| XI | XI | Jean-Philippe Mateta | FWD | -1 | 7.3 | 4.70 | 13.45 | 21.17 | 8.00 | 85.4 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.4 | 3.73 | 10.36 | 16.61 | 8.00 | 70.1 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 9.48 | 26.84 | 42.52 | 6.00 | 137.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 6.14 | 17.62 | 27.64 | 5.00 | 92.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.1 | 6.25 | 17.27 | 27.67 | 3.00 | 89.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 6.0 | 4.48 | 13.31 | 20.92 | 10.00 | 70.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.7 | 4.17 | 11.27 | 18.00 | 7.00 | 82.0 | 90.0 |

## GW28

- Train rows: 152512
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.20
- Actual score: 65.00
- Transfer: Pedro Porro -> Daniel Muñoz (projected gain 0.19, hit 0)
- Autosub outfielders: João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.76 | 10.76 | 17.10 | 3.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.18 | 9.47 | 15.29 | 2.00 | 86.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 4.33 | 11.74 | 18.65 | 2.00 | 100.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.70 | 11.02 | 17.66 | 2.00 | 82.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | -1 | 4.9 | 3.94 | 10.86 | 17.40 | 6.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | -1 | 5.1 | 2.84 | 8.81 | 14.80 | 0.00 | 60.7 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | -1 | 4.7 | 2.86 | 8.04 | 12.75 | 2.00 | 75.3 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 5.00 | 15.31 | 24.80 | 2.00 | 89.9 | 86.0 |
| XI | Bench | Jean-Philippe Mateta | FWD | -1 | 7.4 | 4.84 | 13.39 | 21.25 | 0.00 | 84.2 | 0.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | -1 | 5.4 | 3.51 | 9.83 | 15.94 | 9.00 | 65.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 9.00 | 25.33 | 40.00 | 15.00 | 119.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | -1 | 11.1 | 6.56 | 17.75 | 27.97 | 1.00 | 90.9 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.0 | 5.87 | 17.01 | 27.12 | 2.00 | 89.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 6.0 | 5.20 | 14.66 | 23.53 | 5.00 | 86.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.6 | 4.00 | 11.25 | 18.39 | 3.00 | 86.5 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.80 -> 1.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.71
- Actual score: 35.00
- Transfer: Jean-Philippe Mateta -> Yoane Wissa (projected gain 3.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.76 | 10.74 | 17.19 | 6.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.40 | 9.62 | 15.48 | 3.00 | 85.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.73 | 10.65 | 17.11 | 1.00 | 83.5 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | -1 | 5.0 | 2.86 | 10.48 | 17.51 | 0.00 | 52.5 | 0.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.53 | 9.99 | 16.36 | 7.00 | 77.8 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 2.35 | 9.27 | 16.02 | 0.00 | 61.2 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 4.7 | 3.29 | 8.86 | 14.02 | 2.00 | 77.0 | 79.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 5.16 | 15.67 | 25.11 | 2.00 | 85.8 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 3.82 | 11.27 | 17.74 | 1.00 | 80.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | -1 | 6.5 | 3.86 | 11.16 | 17.92 | 8.00 | 77.1 | 90.0 |
| Captain | Bench | Mohamed Salah | MID | -1 | 13.8 | 7.65 | 24.42 | 39.61 | 0.00 | 85.7 | 0.0 |
| Vice Captain | Bench | Cole Palmer | MID | -1 | 11.0 | 5.51 | 16.31 | 26.30 | 0.00 | 81.7 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 5.29 | 15.40 | 24.73 | 6.00 | 90.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 6.1 | 5.42 | 15.37 | 24.61 | 2.00 | 89.7 | 78.0 |
| Bench 3 | Bench | Morgan Rogers | MID | -1 | 5.6 | 2.64 | 9.80 | 16.54 | 0.00 | 56.8 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 1.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.75
- Actual score: 49.00
- Transfer: Morgan Rogers -> Morgan Gibbs-White (projected gain 4.75, hit 0)
- Autosub outfielders: Cole Palmer, Daniel Muñoz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.99 | 11.26 | 17.96 | 2.00 | 91.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.04 | 9.72 | 15.98 | 3.00 | 90.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 4.20 | 11.86 | 18.54 | 6.00 | 85.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.14 | 9.66 | 16.00 | 1.00 | 82.9 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 4.8 | 3.37 | 9.45 | 14.61 | 8.00 | 75.4 | 81.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | -1 | 5.0 | 3.23 | 8.91 | 14.82 | 2.00 | 52.1 | 75.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 2.64 | 8.32 | 14.52 | 8.00 | 57.3 | 90.0 |
| XI | Bench | Chris Wood | FWD | -1 | 7.3 | 5.52 | 15.43 | 24.21 | 0.00 | 81.4 | 0.0 |
| XI | XI | Yoane Wissa | FWD | -1 | 6.5 | 3.88 | 11.38 | 18.12 | 5.00 | 83.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 3.69 | 10.93 | 17.25 | 2.00 | 76.3 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 7.29 | 21.50 | 35.46 | 3.00 | 75.0 | 90.0 |
| Vice Captain | Bench | Justin Kluivert | MID | -1 | 6.2 | 5.70 | 16.24 | 25.86 | 0.00 | 87.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 5.35 | 15.82 | 25.05 | 8.00 | 92.7 | 90.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | -1 | 10.9 | 4.28 | 12.18 | 21.03 | 6.00 | 44.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | -1 | 6.6 | 4.32 | 12.03 | 18.83 | 3.00 | 77.4 | 90.0 |
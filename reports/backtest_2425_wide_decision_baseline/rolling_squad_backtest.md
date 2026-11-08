# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2024-25 GW1-GW1
- Simulated weeks: GW2-GW38
- Total predicted points: 2226.17
- Total actual points: 2288.00
- Average predicted points: 60.17
- Average actual points: 61.84
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 134294
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.82
- Actual score: 78.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.88 | 11.50 | 18.47 | 10.00 | 92.2 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 3.34 | 9.62 | 15.62 | 3.00 | 88.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 5.99 | 16.93 | 26.99 | 6.00 | 104.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.0 | 5.55 | 15.43 | 24.27 | 6.00 | 84.7 | 71.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 4.51 | 12.09 | 19.01 | 2.00 | 93.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 3.96 | 11.26 | 17.56 | 6.00 | 87.3 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | -1 | 4.5 | 3.44 | 9.83 | 15.73 | 1.00 | 89.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.5 | 4.51 | 12.40 | 19.76 | 9.00 | 92.9 | 78.0 |
| Bench 2 | Bench | Yoane Wissa | FWD | -1 | 6.0 | 3.88 | 11.37 | 17.49 | 2.00 | 81.3 | 72.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | -1 | 5.5 | 3.73 | 10.09 | 15.26 | 2.00 | 75.4 | 70.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.0 | 6.88 | 19.63 | 30.88 | 6.00 | 93.3 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.5 | 6.90 | 19.37 | 30.62 | 10.00 | 94.8 | 82.0 |
| XI | XI | Mitoma Kaoru | MID | -1 | 6.5 | 5.44 | 14.21 | 21.49 | 6.00 | 85.2 | 89.0 |
| XI | XI | Diogo Teixeira da Silva | MID | -1 | 7.5 | 4.95 | 13.63 | 21.07 | 6.00 | 78.6 | 71.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.0 | 4.35 | 13.13 | 21.05 | 1.00 | 92.0 | 90.0 |

## GW3

- Train rows: 134921
- Bank: 0.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.92
- Actual score: 66.00
- Transfer: Bryan Mbeumo -> Antoine Semenyo (projected gain 2.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.98 | 11.64 | 18.57 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 3.21 | 9.10 | 14.52 | 4.00 | 83.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.0 | 5.31 | 15.23 | 24.02 | 6.00 | 77.8 | 75.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.96 | 14.89 | 23.90 | 1.00 | 94.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 4.17 | 11.75 | 18.23 | 2.00 | 85.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.98 | 11.55 | 18.11 | 2.00 | 83.8 | 87.0 |
| Bench 2 | Bench | Dan Burn | DEF | -1 | 4.5 | 3.43 | 9.36 | 14.72 | 0.00 | 83.8 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.5 | 3.52 | 11.17 | 17.48 | 2.00 | 77.3 | 84.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | -1 | 6.0 | 3.40 | 9.05 | 14.04 | 8.00 | 66.5 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | -1 | 5.6 | 2.81 | 8.13 | 12.62 | 1.00 | 60.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.5 | 6.23 | 18.42 | 28.94 | 17.00 | 83.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.0 | 6.09 | 17.53 | 27.66 | 6.00 | 86.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | -1 | 5.5 | 4.85 | 13.37 | 20.87 | 6.00 | 90.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | -1 | 7.6 | 4.51 | 13.03 | 20.15 | 3.00 | 67.1 | 75.0 |
| XI | XI | Mitoma Kaoru | MID | -1 | 6.5 | 4.10 | 12.43 | 19.43 | 2.00 | 82.5 | 84.0 |

## GW4

- Train rows: 135569
- Bank: 1.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.24
- Actual score: 41.00
- Transfer: Jamie Vardy -> João Pedro Junqueira de Jesus (projected gain 0.87, hit 0)
- Autosub outfielders: Yoane Wissa.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.55 | 11.13 | 18.00 | 9.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.94 | 8.75 | 14.24 | 3.00 | 84.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.0 | 4.77 | 13.84 | 22.21 | 1.00 | 74.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.30 | 13.46 | 21.78 | 2.00 | 87.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.92 | 11.36 | 18.24 | 1.00 | 81.1 | 45.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 3.75 | 10.99 | 17.36 | 5.00 | 82.1 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | -1 | 4.5 | 2.81 | 8.26 | 13.36 | 1.00 | 80.6 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 4.15 | 11.73 | 18.29 | 0.00 | 79.3 | 0.0 |
| Bench 2 | Autosub In | Yoane Wissa | FWD | -1 | 6.1 | 3.71 | 10.92 | 16.86 | 7.00 | 75.1 | 45.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | -1 | 5.6 | 3.68 | 10.87 | 17.11 | 2.00 | 68.2 | 84.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.6 | 6.97 | 20.22 | 32.08 | 2.00 | 94.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.1 | 6.03 | 17.26 | 27.30 | 7.00 | 83.8 | 85.0 |
| XI | XI | Antoine Semenyo | MID | -1 | 5.5 | 4.76 | 13.04 | 20.33 | 1.00 | 87.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | -1 | 7.6 | 3.91 | 11.73 | 18.75 | 1.00 | 61.6 | 59.0 |
| XI | XI | Mitoma Kaoru | MID | -1 | 6.6 | 4.15 | 11.34 | 17.82 | 3.00 | 75.0 | 90.0 |

## GW5

- Train rows: 136228
- Bank: 1.50 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.54
- Actual score: 64.00
- Transfer: Diogo Teixeira da Silva -> Luis Díaz (projected gain 3.05, hit 0)
- Autosub outfielders: Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.52 | 11.04 | 18.16 | 4.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.85 | 8.56 | 13.78 | 3.00 | 83.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.0 | 4.60 | 13.25 | 21.48 | 11.00 | 73.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.36 | 12.99 | 21.13 | 2.00 | 85.2 | 87.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 3.48 | 10.42 | 16.74 | 1.00 | 79.9 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | -1 | 6.0 | 2.91 | 9.46 | 15.72 | 1.00 | 63.6 | 90.0 |
| Bench 3 | Bench | Dan Burn | DEF | -1 | 4.5 | 2.63 | 7.83 | 12.67 | 1.00 | 78.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.7 | 3.60 | 11.11 | 17.19 | 6.00 | 67.0 | 90.0 |
| XI | Bench | Yoane Wissa | FWD | -1 | 6.1 | 3.28 | 9.71 | 15.33 | 0.00 | 60.4 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 2.58 | 9.36 | 15.33 | 1.00 | 36.9 | 19.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.7 | 6.46 | 19.55 | 30.90 | 6.00 | 81.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.1 | 5.25 | 16.00 | 25.88 | 4.00 | 78.5 | 45.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.7 | 4.17 | 13.21 | 21.15 | 16.00 | 52.0 | 71.0 |
| XI | XI | Antoine Semenyo | MID | -1 | 5.6 | 3.67 | 11.45 | 18.12 | 2.00 | 77.7 | 69.0 |
| XI | XI | Mitoma Kaoru | MID | -1 | 6.7 | 3.70 | 11.24 | 17.81 | 5.00 | 70.1 | 90.0 |

## GW6

- Train rows: 136889
- Bank: 1.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.14
- Actual score: 47.00
- Transfer: Antoine Semenyo -> Eberechi Eze (projected gain 2.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 4.18 | 11.46 | 18.39 | 1.00 | 92.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.76 | 8.36 | 13.60 | 3.00 | 86.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.1 | 4.98 | 13.76 | 22.19 | 1.00 | 85.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 4.29 | 12.45 | 19.95 | 5.00 | 86.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.39 | 10.24 | 16.47 | 9.00 | 75.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 3.87 | 10.18 | 16.08 | 0.00 | 81.5 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | -1 | 4.5 | 2.59 | 7.72 | 12.46 | 2.00 | 79.7 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.8 | 3.70 | 11.22 | 17.64 | 2.00 | 77.1 | 80.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.7 | 2.31 | 7.88 | 13.74 | 0.00 | 42.3 | 0.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | -1 | 6.1 | 2.35 | 6.79 | 11.30 | 0.00 | 33.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.7 | 7.03 | 19.83 | 31.25 | 10.00 | 91.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.0 | 5.49 | 15.49 | 24.69 | 3.00 | 71.4 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.8 | 5.14 | 14.96 | 23.72 | 2.00 | 72.9 | 72.0 |
| XI | XI | Eberechi Eze | MID | -1 | 6.9 | 4.23 | 12.20 | 19.40 | 2.00 | 81.6 | 90.0 |
| XI | XI | Mitoma Kaoru | MID | -1 | 6.7 | 3.82 | 10.97 | 17.47 | 2.00 | 77.0 | 90.0 |

## GW7

- Train rows: 137553
- Bank: 0.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.66
- Actual score: 49.00
- Transfer: Mitoma Kaoru -> Dwight McNeil (projected gain 2.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.90 | 11.23 | 18.31 | 2.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.70 | 8.28 | 13.77 | 6.00 | 85.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.1 | 4.36 | 12.91 | 21.11 | 8.00 | 79.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 4.07 | 11.76 | 19.20 | 1.00 | 83.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.87 | 10.99 | 17.86 | 1.00 | 78.5 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 3.61 | 9.82 | 15.61 | 2.00 | 75.9 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | -1 | 4.5 | 2.63 | 7.69 | 12.58 | 8.00 | 77.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.8 | 3.98 | 10.98 | 17.49 | 8.00 | 71.8 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.6 | 1.36 | 5.32 | 10.27 | 0.00 | 13.3 | 0.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | -1 | 6.0 | 1.51 | 5.08 | 9.07 | 0.00 | 23.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.8 | 6.56 | 18.42 | 29.58 | 3.00 | 83.6 | 72.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.1 | 5.98 | 16.78 | 26.42 | 16.00 | 75.8 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 8.0 | 4.48 | 14.68 | 23.56 | 1.00 | 56.9 | 17.0 |
| XI | XI | Dwight McNeil | MID | -1 | 5.5 | 4.59 | 13.26 | 21.05 | 2.00 | 91.1 | 90.0 |
| XI | XI | Eberechi Eze | MID | -1 | 6.9 | 3.71 | 11.40 | 18.26 | 2.00 | 75.8 | 90.0 |

## GW8

- Train rows: 138219
- Bank: 1.30 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.16
- Actual score: 55.00
- Transfer: Eberechi Eze -> Bryan Mbeumo (projected gain 4.50, hit 0)
- Autosub outfielders: Dan Burn.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.62 | 10.88 | 17.55 | 1.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 3.00 | 8.65 | 14.05 | 3.00 | 85.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.1 | 4.69 | 13.37 | 21.48 | 2.00 | 84.8 | 80.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.24 | 11.88 | 18.87 | 2.00 | 85.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.88 | 10.90 | 17.25 | 10.00 | 82.7 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 3.07 | 8.93 | 14.31 | -3.00 | 76.8 | 29.0 |
| Bench 2 | Autosub In | Dan Burn | DEF | -1 | 4.4 | 2.89 | 8.10 | 12.88 | 1.00 | 80.3 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.8 | 4.19 | 11.63 | 18.24 | 9.00 | 82.9 | 80.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 5.5 | 0.83 | 4.18 | 8.29 | 0.00 | 15.3 | 0.0 |
| Bench 3 | Bench | Yoane Wissa | FWD | -1 | 5.9 | 0.97 | 3.89 | 7.17 | 1.00 | 14.8 | 24.0 |
| Captain | Bench | Bukayo Saka | MID | -1 | 10.1 | 6.56 | 18.45 | 29.06 | 0.00 | 90.3 | 0.0 |
| Vice Captain | Captain | Mohamed Salah | MID | -1 | 12.7 | 6.06 | 17.18 | 27.53 | 12.00 | 74.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.4 | 5.07 | 14.94 | 23.38 | 2.00 | 88.4 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 8.1 | 4.10 | 12.29 | 20.40 | 1.00 | 49.5 | 24.0 |
| XI | XI | Dwight McNeil | MID | -1 | 5.6 | 4.13 | 11.98 | 19.13 | 6.00 | 78.4 | 90.0 |

## GW9

- Train rows: 138886
- Bank: 0.70 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.22
- Actual score: 72.00
- Transfer: João Pedro Junqueira de Jesus -> Raúl Jiménez (projected gain 3.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.7 | 3.31 | 10.31 | 16.58 | 0.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.75 | 8.50 | 13.78 | 2.00 | 83.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.1 | 3.82 | 12.08 | 19.53 | 1.00 | 79.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 4.61 | 11.98 | 18.80 | 9.00 | 89.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.00 | 11.63 | 18.49 | 2.00 | 86.6 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | -1 | 4.4 | 2.44 | 7.48 | 11.91 | 1.00 | 77.9 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | -1 | 6.0 | 2.08 | 6.82 | 11.27 | 0.00 | 52.7 | 0.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.8 | 4.34 | 11.77 | 18.25 | 7.00 | 81.1 | 72.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.6 | 3.89 | 10.79 | 15.88 | 2.00 | 70.7 | 90.0 |
| Bench 4 | Bench | Yoane Wissa | FWD | -1 | 5.9 | 1.72 | 4.99 | 8.53 | 10.00 | 29.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.6 | 5.78 | 17.50 | 27.94 | 10.00 | 85.7 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 7.5 | 5.07 | 14.28 | 22.53 | 15.00 | 85.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 10.1 | 4.40 | 13.67 | 22.85 | 9.00 | 50.6 | 84.0 |
| XI | XI | Dwight McNeil | MID | -1 | 5.7 | 4.16 | 11.94 | 19.05 | 2.00 | 82.0 | 85.0 |
| XI | XI | Luis Díaz | MID | -1 | 8.0 | 3.06 | 10.57 | 18.20 | 5.00 | 43.3 | 62.0 |

## GW10

- Train rows: 139556
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.08
- Actual score: 48.00
- Transfer: Yoane Wissa -> Chris Wood (projected gain 0.43, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.7 | 3.21 | 9.94 | 16.37 | 3.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.48 | 8.01 | 13.09 | 5.00 | 83.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.1 | 4.11 | 12.33 | 19.59 | 7.00 | 83.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.1 | 4.11 | 11.85 | 19.03 | 2.00 | 80.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.80 | 10.89 | 17.38 | 1.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Dan Burn | DEF | -1 | 4.4 | 2.29 | 7.29 | 11.69 | 6.00 | 78.6 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | -1 | 6.0 | 0.94 | 4.23 | 8.56 | 2.00 | 25.2 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.3 | 4.22 | 11.32 | 17.62 | 7.00 | 79.1 | 78.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.7 | 4.02 | 11.08 | 16.65 | 2.00 | 70.0 | 72.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | -1 | 5.9 | 3.64 | 10.97 | 17.30 | 5.00 | 76.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.6 | 5.88 | 17.27 | 27.55 | 9.00 | 83.4 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 7.6 | 5.59 | 16.20 | 25.23 | 3.00 | 94.6 | 86.0 |
| XI | XI | Bukayo Saka | MID | -1 | 10.0 | 4.20 | 13.74 | 23.94 | 2.00 | 63.4 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.9 | 3.87 | 11.84 | 19.78 | 1.00 | 53.1 | 24.0 |
| XI | XI | Dwight McNeil | MID | -1 | 5.8 | 4.22 | 11.54 | 18.21 | 2.00 | 78.2 | 90.0 |

## GW11

- Train rows: 140230
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.78
- Actual score: 55.00
- Transfer: Luis Díaz -> Jarrod Bowen (projected gain 1.86, hit 0)
- Autosub outfielders: Raúl Jiménez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.18 | 9.80 | 15.99 | 2.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.68 | 8.17 | 13.20 | 2.00 | 82.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 4.25 | 12.56 | 20.33 | 1.00 | 87.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.0 | 4.06 | 11.68 | 18.88 | 1.00 | 82.6 | 24.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.86 | 10.65 | 17.06 | 4.00 | 81.8 | 90.0 |
| Bench 3 | Bench | Dan Burn | DEF | -1 | 4.4 | 2.62 | 7.83 | 12.34 | 1.00 | 80.4 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | -1 | 6.0 | 2.18 | 6.86 | 11.04 | 2.00 | 58.6 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.4 | 4.20 | 11.87 | 18.43 | 2.00 | 78.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 5.9 | 3.79 | 11.18 | 17.77 | 2.00 | 78.4 | 90.0 |
| Bench 2 | Autosub In | Raúl Jiménez | FWD | -1 | 5.8 | 3.56 | 9.89 | 15.60 | 5.00 | 63.7 | 74.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.7 | 5.94 | 17.17 | 27.42 | 14.00 | 87.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.15 | 15.24 | 24.40 | 5.00 | 86.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 10.1 | 4.20 | 13.48 | 21.94 | 2.00 | 66.9 | 80.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.4 | 4.22 | 11.73 | 18.55 | 3.00 | 82.8 | 90.0 |
| XI | Bench | Dwight McNeil | MID | -1 | 5.8 | 3.97 | 11.18 | 17.95 | 0.00 | 79.8 | 0.0 |

## GW12

- Train rows: 140908
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.68
- Actual score: 80.00
- Transfer: Dwight McNeil -> Emile Smith Rowe (projected gain 1.20, hit 0)
- Autosub outfielders: William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.36 | 9.76 | 15.77 | 6.00 | 85.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 3.02 | 8.26 | 13.14 | 2.00 | 80.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.3 | 4.46 | 12.58 | 20.02 | 0.00 | 87.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.72 | 11.01 | 17.74 | 14.00 | 86.9 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.0 | 3.62 | 10.18 | 16.72 | 0.00 | 61.7 | 0.0 |
| Bench 3 | Bench | Dan Burn | DEF | -1 | 4.4 | 3.07 | 8.05 | 12.47 | 0.00 | 78.8 | 0.0 |
| Bench 4 | Autosub In | William Saliba | DEF | -1 | 6.0 | 2.67 | 7.69 | 12.11 | 7.00 | 66.7 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.73 | 11.72 | 18.46 | 1.00 | 76.6 | 27.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | -1 | 5.9 | 3.68 | 10.93 | 17.18 | 2.00 | 77.2 | 85.0 |
| XI | XI | Raúl Jiménez | FWD | -1 | 5.8 | 3.91 | 10.70 | 17.09 | 2.00 | 68.1 | 70.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.8 | 6.52 | 18.57 | 29.56 | 13.00 | 88.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.14 | 15.50 | 24.79 | 3.00 | 94.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 10.1 | 4.20 | 12.78 | 20.69 | 13.00 | 70.3 | 82.0 |
| XI | XI | Emile Smith Rowe | MID | -1 | 5.7 | 4.49 | 12.02 | 18.94 | 1.00 | 82.1 | 58.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.5 | 4.02 | 11.50 | 18.18 | 7.00 | 84.1 | 90.0 |

## GW13

- Train rows: 141592
- Bank: 0.70 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.27
- Actual score: 72.00
- Transfer: Trent Alexander-Arnold -> Virgil van Dijk (projected gain 2.02, hit 0)
- Autosub outfielders: William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.76 | 10.49 | 16.61 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.69 | 7.96 | 12.82 | 2.00 | 80.0 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | -1 | 6.3 | 4.16 | 12.97 | 20.91 | 0.00 | 91.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.30 | 12.14 | 19.55 | 2.00 | 93.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.3 | 3.63 | 10.97 | 17.61 | 6.00 | 83.0 | 90.0 |
| Bench 2 | Autosub In | William Saliba | DEF | -1 | 6.0 | 3.38 | 9.06 | 13.80 | 1.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | -1 | 4.4 | 1.53 | 4.95 | 8.82 | 4.00 | 43.0 | 90.0 |
| XI | XI | Danny Welbeck | FWD | -1 | 6.0 | 4.06 | 10.98 | 17.26 | 2.00 | 76.4 | 78.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.51 | 10.44 | 17.10 | 9.00 | 55.9 | 90.0 |
| Bench 3 | Bench | Raúl Jiménez | FWD | -1 | 5.8 | 3.29 | 9.57 | 15.26 | 2.00 | 63.0 | 77.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.0 | 6.97 | 20.41 | 31.89 | 13.00 | 95.1 | 83.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.08 | 14.49 | 23.64 | 2.00 | 86.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 10.1 | 4.73 | 13.34 | 21.38 | 18.00 | 73.1 | 73.0 |
| XI | XI | Emile Smith Rowe | MID | -1 | 5.8 | 3.71 | 10.82 | 17.52 | 2.00 | 68.1 | 85.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.5 | 3.40 | 10.30 | 16.89 | 2.00 | 80.2 | 90.0 |

## GW14

- Train rows: 142282
- Bank: 1.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.36
- Actual score: 72.00
- Transfer: Raúl Jiménez -> Matheus Santos Carneiro Da Cunha (projected gain 3.63, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.69 | 10.06 | 15.90 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.35 | 7.36 | 11.95 | 0.00 | 79.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.01 | 11.82 | 18.92 | 1.00 | 86.8 | 28.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.3 | 3.93 | 11.70 | 18.66 | 1.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | -1 | 6.3 | 2.91 | 9.34 | 16.06 | 6.00 | 51.5 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 3.12 | 8.18 | 12.56 | 15.00 | 71.9 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | -1 | 4.4 | 2.15 | 6.62 | 10.82 | 1.00 | 68.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.0 | 4.49 | 13.85 | 21.77 | 2.00 | 81.8 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.56 | 11.19 | 17.91 | 2.00 | 75.1 | 61.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | -1 | 6.0 | 3.41 | 10.23 | 16.61 | 0.00 | 70.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.1 | 7.41 | 21.59 | 33.60 | 18.00 | 99.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.2 | 5.94 | 16.79 | 26.29 | 3.00 | 77.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 4.46 | 13.58 | 22.19 | 2.00 | 86.6 | 90.0 |
| XI | XI | Emile Smith Rowe | MID | -1 | 5.8 | 3.60 | 10.64 | 17.40 | 2.00 | 72.8 | 70.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.4 | 3.73 | 10.40 | 16.85 | 2.00 | 78.0 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.40
- Actual score: 56.00
- Transfer: Emile Smith Rowe -> Alex Iwobi (projected gain 2.35, hit 0)
- Autosub outfielders: Danny Welbeck.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.54 | 10.22 | 16.19 | 2.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.36 | 6.98 | 11.44 | 1.00 | 76.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 3.97 | 11.61 | 18.88 | 1.00 | 75.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 3.42 | 10.15 | 16.63 | 3.00 | 70.5 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 2.46 | 9.90 | 16.41 | 0.00 | 54.0 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 6.0 | 3.32 | 9.08 | 13.86 | 9.00 | 76.4 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | -1 | 4.4 | 2.12 | 6.40 | 10.59 | 0.00 | 68.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.65 | 13.09 | 20.69 | 1.00 | 85.1 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.37 | 10.24 | 16.68 | 8.00 | 60.7 | 78.0 |
| Bench 2 | Autosub In | Danny Welbeck | FWD | -1 | 5.9 | 2.57 | 7.53 | 12.91 | 1.00 | 39.5 | 20.0 |
| Captain | Bench | Mohamed Salah | MID | -1 | 13.2 | 6.99 | 22.36 | 35.42 | 0.00 | 77.8 | 0.0 |
| Vice Captain | Captain | Bukayo Saka | MID | -1 | 10.4 | 5.98 | 17.10 | 27.14 | 2.00 | 79.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 3.91 | 11.91 | 20.40 | 13.00 | 76.2 | 90.0 |
| XI | XI | Alex Iwobi | MID | -1 | 5.6 | 4.09 | 11.88 | 18.83 | 2.00 | 89.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.4 | 4.18 | 11.43 | 17.94 | 12.00 | 83.2 | 90.0 |

## GW16

- Train rows: 143668
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.94
- Actual score: 61.00
- Transfer: Danny Welbeck -> Jamie Vardy (projected gain 0.32, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.46 | 9.97 | 15.83 | 6.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 2.70 | 7.14 | 11.53 | 0.00 | 77.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 4.08 | 11.61 | 18.68 | 6.00 | 84.1 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 4.03 | 11.28 | 18.08 | 7.00 | 74.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.1 | 3.71 | 10.13 | 15.22 | 6.00 | 74.1 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 2.60 | 7.67 | 12.84 | 1.00 | 50.9 | 90.0 |
| Bench 3 | Bench | Dan Burn | DEF | -1 | 4.4 | 2.62 | 6.82 | 10.87 | 6.00 | 74.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.25 | 12.14 | 19.38 | 9.00 | 78.4 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.5 | 3.95 | 11.06 | 17.53 | 2.00 | 72.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | -1 | 5.5 | 3.79 | 10.82 | 16.82 | 1.00 | 84.0 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.2 | 6.11 | 18.37 | 30.20 | 5.00 | 64.1 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.5 | 5.92 | 16.93 | 26.37 | 3.00 | 81.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.7 | 4.31 | 13.16 | 21.99 | 9.00 | 85.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.4 | 4.23 | 12.12 | 19.08 | 2.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Alex Iwobi | MID | -1 | 5.6 | 3.38 | 10.61 | 17.14 | 2.00 | 82.5 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.65
- Actual score: 69.00
- Transfer: Alex Iwobi -> Enzo Fernández (projected gain 1.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.75 | 10.80 | 17.06 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.0 | 1.27 | 4.24 | 7.78 | 0.00 | 42.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.1 | 3.81 | 11.73 | 19.08 | 0.00 | 85.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.2 | 3.98 | 11.34 | 17.27 | 2.00 | 76.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 3.36 | 10.54 | 17.17 | -1.00 | 75.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 3.18 | 9.50 | 15.50 | 1.00 | 70.6 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | -1 | 4.4 | 2.75 | 7.47 | 11.60 | 6.00 | 77.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.75 | 13.30 | 21.25 | 9.00 | 84.2 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.67 | 10.53 | 16.56 | 2.00 | 71.3 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | -1 | 5.6 | 3.45 | 9.28 | 14.69 | 2.00 | 70.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.4 | 6.78 | 20.25 | 33.08 | 21.00 | 83.2 | 86.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 10.6 | 6.05 | 17.67 | 28.07 | 1.00 | 82.4 | 23.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.66 | 13.75 | 22.48 | 2.00 | 90.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.4 | 4.18 | 11.77 | 18.59 | 6.00 | 82.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.0 | 3.89 | 11.63 | 18.17 | 3.00 | 78.8 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 1.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.05
- Actual score: 62.00
- Transfer: Dan Burn -> Antonee Robinson (projected gain 1.49, hit 0)
- Autosub outfielders: Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.95 | 11.02 | 17.54 | 6.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 4.9 | 0.93 | 3.57 | 6.87 | 0.00 | 31.9 | 0.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.8 | 3.68 | 11.47 | 18.31 | 1.00 | 85.5 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 4.21 | 11.37 | 17.60 | 7.00 | 80.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 3.49 | 10.41 | 17.05 | 1.00 | 83.9 | 9.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | -1 | 6.1 | 3.47 | 10.01 | 16.10 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.5 | 3.47 | 9.38 | 15.19 | 2.00 | 70.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.82 | 13.19 | 21.46 | 12.00 | 86.7 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.6 | 3.78 | 10.60 | 16.77 | 2.00 | 70.6 | 86.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | -1 | 5.6 | 3.12 | 9.58 | 15.30 | 0.00 | 72.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.4 | 8.27 | 22.92 | 36.45 | 9.00 | 95.1 | 90.0 |
| Vice Captain | Bench | Bukayo Saka | MID | -1 | 10.6 | 5.33 | 15.34 | 25.03 | 0.00 | 61.1 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.71 | 13.74 | 22.13 | 3.00 | 89.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.4 | 4.44 | 11.71 | 18.70 | 8.00 | 78.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.1 | 4.09 | 11.26 | 17.89 | 2.00 | 82.1 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 0.80 -> 4.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.01
- Actual score: 68.00
- Transfer: Bukayo Saka -> Anthony Gordon (projected gain 2.75, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.99 | 11.60 | 18.57 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 4.9 | 0.73 | 2.97 | 5.99 | 0.00 | 23.6 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 4.00 | 11.82 | 18.97 | 2.00 | 80.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 4.17 | 11.58 | 18.50 | 4.00 | 91.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.67 | 10.32 | 16.56 | 6.00 | 76.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.5 | 3.51 | 9.94 | 15.99 | 6.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | -1 | 5.5 | 2.97 | 9.10 | 15.48 | 4.00 | 55.1 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 4.77 | 14.01 | 23.05 | 1.00 | 91.9 | 45.0 |
| Bench 2 | Bench | Chris Wood | FWD | -1 | 6.6 | 3.36 | 10.16 | 16.48 | 12.00 | 69.7 | 75.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | -1 | 5.6 | 1.82 | 6.01 | 10.25 | 2.00 | 33.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.5 | 8.70 | 24.26 | 38.09 | 16.00 | 104.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 4.32 | 13.41 | 21.82 | 7.00 | 85.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.5 | 4.51 | 12.87 | 20.21 | 1.00 | 83.1 | 59.0 |
| XI | XI | Anthony Gordon | MID | -1 | 7.2 | 4.44 | 12.79 | 20.12 | 6.00 | 76.4 | 84.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.1 | 4.23 | 11.34 | 18.08 | 1.00 | 83.9 | 90.0 |

## GW20

- Train rows: 146484
- Bank: 4.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.77
- Actual score: 65.00
- Transfer: Jamie Vardy -> Alexander Isak (projected gain 8.24, hit 0)
- Autosub outfielders: Chris Wood.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.83 | 11.12 | 17.97 | 3.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 4.9 | 0.74 | 2.88 | 5.72 | 0.00 | 20.6 | 0.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 4.41 | 12.01 | 19.09 | 1.00 | 89.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.82 | 11.20 | 18.17 | 2.00 | 79.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.86 | 10.46 | 16.34 | 2.00 | 79.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.5 | 3.83 | 10.44 | 16.52 | 1.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | -1 | 5.5 | 3.52 | 10.44 | 17.11 | 4.00 | 77.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.1 | 6.74 | 19.24 | 30.25 | 7.00 | 89.5 | 85.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | -1 | 7.1 | 3.95 | 12.60 | 20.61 | 0.00 | 73.5 | 0.0 |
| Bench 2 | Autosub In | Chris Wood | FWD | -1 | 6.6 | 3.81 | 11.04 | 17.65 | 8.00 | 72.6 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 9.74 | 25.70 | 40.06 | 7.00 | 111.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.6 | 5.11 | 14.29 | 22.75 | 19.00 | 88.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 7.3 | 4.60 | 13.35 | 21.04 | 7.00 | 77.3 | 77.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.1 | 4.13 | 11.64 | 18.48 | 1.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | MID | -1 | 7.5 | 3.78 | 11.18 | 17.88 | 0.00 | 71.4 | 0.0 |

## GW21

- Train rows: 147195
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.45
- Actual score: 56.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Cody Gakpo (projected gain 2.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 4.05 | 11.20 | 17.89 | 2.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 4.9 | 0.82 | 2.83 | 5.44 | 0.00 | 17.5 | 0.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 4.23 | 12.19 | 19.61 | 7.00 | 87.0 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.3 | 3.99 | 10.72 | 17.04 | 2.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | -1 | 5.5 | 3.28 | 10.18 | 16.45 | 1.00 | 79.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.51 | 10.14 | 16.10 | 1.00 | 78.5 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | -1 | 6.5 | 3.35 | 9.78 | 15.59 | 2.00 | 79.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.2 | 6.57 | 19.34 | 30.73 | 16.00 | 84.1 | 77.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.8 | 4.01 | 12.50 | 20.12 | 9.00 | 74.2 | 89.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.3 | 4.11 | 12.15 | 18.93 | 2.00 | 76.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 8.80 | 25.04 | 39.63 | 2.00 | 101.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.7 | 5.84 | 16.75 | 26.32 | 2.00 | 100.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 7.4 | 4.81 | 13.80 | 22.13 | 9.00 | 74.1 | 77.0 |
| XI | XI | Enzo Fernández | MID | -1 | 5.1 | 3.74 | 10.73 | 17.28 | 2.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Jarrod Bowen | MID | -1 | 7.4 | 2.45 | 7.68 | 13.29 | 0.00 | 37.8 | 0.0 |

## GW22

- Train rows: 147919
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.39
- Actual score: 44.00
- Transfer: Jarrod Bowen -> Amad Diallo (projected gain 3.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.63 | 10.46 | 16.85 | 1.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 4.9 | 0.60 | 2.18 | 4.14 | 0.00 | 13.1 | 0.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 4.62 | 12.69 | 20.20 | 8.00 | 91.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 3.63 | 10.29 | 16.29 | 1.00 | 82.2 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | -1 | 6.3 | 3.59 | 10.13 | 16.14 | 0.00 | 79.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 3.62 | 10.09 | 16.26 | 6.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 3.35 | 9.67 | 15.36 | 6.00 | 77.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.3 | 7.05 | 20.49 | 32.40 | 2.00 | 95.4 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 6.8 | 4.69 | 12.78 | 20.54 | 12.00 | 82.1 | 82.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.4 | 4.20 | 11.75 | 18.21 | 2.00 | 74.3 | 86.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.57 | 24.30 | 38.26 | 3.00 | 97.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.57 | 16.10 | 25.79 | 2.00 | 94.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 7.6 | 5.12 | 14.65 | 23.11 | 2.00 | 74.8 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.4 | 5.11 | 14.16 | 22.26 | 2.00 | 95.1 | 90.0 |
| Bench 2 | Bench | Enzo Fernández | MID | -1 | 5.0 | 3.67 | 10.32 | 16.55 | 0.00 | 78.9 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 2.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.04
- Actual score: 80.00
- Transfer: William Saliba -> Trent Alexander-Arnold (projected gain 3.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.43 | 9.96 | 16.10 | 9.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 4.9 | 0.81 | 2.12 | 3.73 | 0.00 | 9.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.2 | 4.91 | 13.84 | 21.77 | 5.00 | 85.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 4.59 | 12.48 | 19.65 | 2.00 | 90.3 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.4 | 3.83 | 10.42 | 16.60 | 6.00 | 81.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 3.86 | 10.33 | 16.12 | 2.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | -1 | 6.0 | 3.65 | 10.25 | 16.29 | 8.00 | 83.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.4 | 6.88 | 19.45 | 30.76 | 13.00 | 93.8 | 78.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 4.80 | 14.28 | 22.72 | 2.00 | 82.0 | 90.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.4 | 4.33 | 11.66 | 18.13 | 16.00 | 71.1 | 67.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.33 | 23.38 | 36.76 | 8.00 | 92.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.65 | 15.77 | 25.22 | 7.00 | 94.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 7.7 | 5.17 | 14.07 | 22.17 | 5.00 | 78.5 | 87.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.5 | 4.74 | 13.54 | 21.64 | 3.00 | 89.3 | 90.0 |
| Bench 4 | Bench | Enzo Fernández | MID | -1 | 5.0 | 1.85 | 6.10 | 10.75 | 2.00 | 42.3 | 90.0 |

## GW24

- Train rows: 149404
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 71.45
- Actual score: 116.00
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Nick Pope -> Jordan Pickford (projected gain 0.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | -1 | 5.0 | 4.01 | 10.45 | 16.10 | 10.00 | 112.8 | 180.0 |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.6 | 3.53 | 10.41 | 16.85 | 3.00 | 86.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 6.31 | 16.28 | 24.75 | 7.00 | 114.8 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 5.01 | 12.15 | 18.28 | 6.00 | 108.1 | 180.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.96 | 11.86 | 19.21 | 4.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | -1 | 5.9 | 3.51 | 10.73 | 17.31 | 0.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | -1 | 5.4 | 3.54 | 10.54 | 17.00 | 6.00 | 83.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.5 | 7.04 | 20.18 | 31.98 | 2.00 | 99.2 | 90.0 |
| XI | XI | Cody Gakpo | FWD | -1 | 7.5 | 6.11 | 15.03 | 22.74 | 7.00 | 99.1 | 137.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 4.61 | 13.69 | 22.01 | 17.00 | 84.5 | 81.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 9.43 | 24.92 | 38.83 | 29.00 | 122.8 | 177.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.8 | 5.80 | 16.30 | 25.86 | 2.00 | 89.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | -1 | 7.7 | 4.94 | 14.26 | 22.95 | 1.00 | 81.3 | 90.0 |
| XI | XI | Amad Diallo | MID | -1 | 5.6 | 4.81 | 13.13 | 20.68 | 2.00 | 90.3 | 90.0 |
| Bench 4 | Bench | Enzo Fernández | MID | -1 | 4.9 | 3.03 | 8.08 | 13.19 | 4.00 | 67.2 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 79.05
- Actual score: 86.00
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Amad Diallo -> Dominik Szoboszlai (projected gain 1.56, hit 0)
- Autosub outfielders: Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | -1 | 5.1 | 4.66 | 13.17 | 20.12 | 3.00 | 118.0 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.5 | 3.52 | 10.04 | 16.46 | 7.00 | 81.2 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 6.93 | 17.54 | 26.72 | 13.00 | 125.1 | 128.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 6.16 | 15.11 | 22.26 | 2.00 | 146.9 | 180.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.90 | 11.62 | 18.71 | 2.00 | 86.6 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro | DEF | -1 | 5.4 | 3.75 | 10.43 | 16.60 | 6.00 | 85.6 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | -1 | 5.9 | 3.58 | 10.33 | 16.37 | 6.00 | 83.1 | 86.0 |
| XI | XI | Alexander Isak | FWD | -1 | 9.5 | 6.15 | 18.54 | 29.74 | 2.00 | 94.3 | 89.0 |
| XI | Bench | Cody Gakpo | FWD | -1 | 7.6 | 6.64 | 17.23 | 25.83 | 0.00 | 114.5 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 5.46 | 15.45 | 24.63 | 9.00 | 91.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 11.60 | 29.88 | 45.80 | 20.00 | 175.0 | 180.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.66 | 16.30 | 25.77 | 3.00 | 86.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | -1 | 6.3 | 6.12 | 14.38 | 20.60 | 4.00 | 126.1 | 180.0 |
| XI | XI | Anthony Gordon | MID | -1 | 7.7 | 4.18 | 12.89 | 21.16 | 2.00 | 75.9 | 72.0 |
| Bench 4 | Bench | Enzo Fernández | MID | -1 | 4.8 | 2.47 | 7.49 | 12.06 | 1.00 | 67.8 | 90.0 |

## GW26

- Train rows: 150945
- Bank: 0.50 -> 2.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 70.89
- Actual score: 90.00
- Transfer: Anthony Gordon -> Morgan Rogers (projected gain 3.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.5 | 3.91 | 10.79 | 17.22 | 2.00 | 86.2 | 90.0 |
| XI | XI | Jordan Pickford | GK | -1 | 5.1 | 3.93 | 10.65 | 16.90 | 1.00 | 96.2 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 6.21 | 17.73 | 28.04 | 6.00 | 112.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 4.70 | 13.64 | 21.24 | 6.00 | 129.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.87 | 11.53 | 18.41 | 1.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 4.06 | 11.10 | 17.63 | 1.00 | 88.1 | 25.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | -1 | 5.9 | 3.65 | 10.77 | 17.13 | 1.00 | 83.7 | 90.0 |
| XI | XI | Alexander Isak | FWD | -1 | 9.5 | 5.73 | 16.97 | 27.55 | 13.00 | 91.2 | 86.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 5.47 | 15.95 | 25.09 | 5.00 | 95.2 | 90.0 |
| Bench 3 | Bench | Cody Gakpo | FWD | -1 | 7.6 | 3.37 | 10.70 | 18.31 | 1.00 | 49.9 | 11.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 10.40 | 29.01 | 45.45 | 14.00 | 161.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.85 | 15.96 | 25.02 | 14.00 | 87.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.6 | 5.30 | 14.65 | 22.26 | 2.00 | 102.9 | 77.0 |
| XI | XI | Dominik Szoboszlai | MID | -1 | 6.3 | 4.98 | 13.61 | 20.17 | 13.00 | 110.5 | 90.0 |
| Bench 4 | Bench | Enzo Fernández | MID | -1 | 4.8 | 2.46 | 7.59 | 12.15 | 7.00 | 75.7 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 2.50 -> 2.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.78
- Actual score: 63.00
- Transfer: Cody Gakpo -> Jean-Philippe Mateta (projected gain 4.29, hit 0)
- Autosub outfielders: Enzo Fernández.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.5 | 3.31 | 10.00 | 15.99 | 6.00 | 84.4 | 90.0 |
| XI | XI | Jordan Pickford | GK | -1 | 5.1 | 3.41 | 9.99 | 15.94 | 2.00 | 93.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 5.64 | 16.12 | 25.72 | 6.00 | 99.2 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 4.07 | 11.91 | 18.94 | 7.00 | 108.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.1 | 3.67 | 10.73 | 17.13 | 0.00 | 84.6 | 18.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | -1 | 5.9 | 3.60 | 10.63 | 17.06 | 7.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | -1 | 5.4 | 3.00 | 9.13 | 15.03 | 2.00 | 66.0 | 90.0 |
| XI | Bench | Alexander Isak | FWD | -1 | 9.5 | 5.69 | 17.24 | 27.62 | 0.00 | 96.2 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 5.73 | 16.84 | 26.79 | 2.00 | 101.3 | 84.0 |
| XI | XI | Jean-Philippe Mateta | FWD | -1 | 7.3 | 4.70 | 13.45 | 21.17 | 8.00 | 85.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 9.48 | 26.84 | 42.52 | 6.00 | 137.7 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 7.9 | 6.14 | 17.62 | 27.64 | 5.00 | 92.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | -1 | 6.3 | 4.60 | 12.86 | 19.50 | 11.00 | 95.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.7 | 4.17 | 11.27 | 18.00 | 7.00 | 82.0 | 90.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | -1 | 4.7 | 3.65 | 9.24 | 14.14 | 3.00 | 78.2 | 89.0 |

## GW28

- Train rows: 152512
- Bank: 2.80 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.92
- Actual score: 53.00
- Transfer: Enzo Fernández -> Justin Kluivert (projected gain 3.44, hit 0)
- Autosub outfielders: Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.76 | 10.76 | 17.10 | 3.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.18 | 9.47 | 15.29 | 2.00 | 86.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.4 | 5.62 | 15.21 | 24.09 | 2.00 | 90.2 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 4.33 | 11.74 | 18.65 | 2.00 | 100.7 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | -1 | 5.9 | 3.70 | 11.02 | 17.66 | 2.00 | 82.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 3.75 | 10.67 | 17.14 | 1.00 | 82.2 | 86.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | -1 | 5.1 | 2.84 | 8.81 | 14.80 | 0.00 | 60.7 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 5.00 | 15.31 | 24.80 | 2.00 | 89.9 | 86.0 |
| XI | XI | Alexander Isak | FWD | -1 | 9.5 | 4.67 | 13.99 | 23.26 | 2.00 | 58.5 | 78.0 |
| XI | Bench | Jean-Philippe Mateta | FWD | -1 | 7.4 | 4.84 | 13.39 | 21.25 | 0.00 | 84.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 9.00 | 25.33 | 40.00 | 15.00 | 119.6 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 8.0 | 5.87 | 17.01 | 27.12 | 2.00 | 89.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | -1 | 6.0 | 5.20 | 14.66 | 23.53 | 5.00 | 86.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | -1 | 6.3 | 4.87 | 12.88 | 20.06 | 1.00 | 92.0 | 45.0 |
| Bench 2 | Autosub In | Morgan Rogers | MID | -1 | 5.6 | 4.00 | 11.25 | 18.39 | 3.00 | 86.5 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 1.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 56.98
- Actual score: 26.00
- Transfer: Dominik Szoboszlai -> Luis Díaz (projected gain 1.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.76 | 10.74 | 17.19 | 6.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.40 | 9.62 | 15.48 | 3.00 | 85.9 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.5 | 3.81 | 13.29 | 22.25 | 0.00 | 57.8 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 5.9 | 3.73 | 10.65 | 17.11 | 1.00 | 83.5 | 90.0 |
| XI | Bench | Pedro Porro | DEF | -1 | 5.3 | 3.52 | 10.51 | 17.07 | 0.00 | 80.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.53 | 9.99 | 16.36 | 7.00 | 77.8 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 2.35 | 9.27 | 16.02 | 0.00 | 61.2 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 5.16 | 15.67 | 25.11 | 2.00 | 85.8 | 79.0 |
| XI | Bench | Alexander Isak | FWD | -1 | 9.4 | 4.02 | 13.87 | 23.70 | 0.00 | 45.7 | 0.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | -1 | 7.5 | 1.18 | 7.06 | 13.95 | 0.00 | 6.7 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | -1 | 13.8 | 7.65 | 24.42 | 39.61 | 0.00 | 85.7 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 5.29 | 15.40 | 24.73 | 6.00 | 90.7 | 90.0 |
| Vice Captain | Captain | Justin Kluivert | MID | -1 | 6.1 | 5.42 | 15.37 | 24.61 | 2.00 | 89.7 | 78.0 |
| XI | Bench | Luis Díaz | MID | -1 | 7.5 | 3.41 | 11.77 | 19.50 | 0.00 | 49.9 | 0.0 |
| Bench 2 | Bench | Morgan Rogers | MID | -1 | 5.6 | 2.64 | 9.80 | 16.54 | 0.00 | 56.8 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.73
- Actual score: 60.00
- Transfer: Pedro Porro -> Ola Aina (projected gain 4.10, hit 0)
- Autosub outfielders: Jean-Philippe Mateta, Virgil van Dijk, Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.99 | 11.26 | 17.96 | 2.00 | 91.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.04 | 9.72 | 15.98 | 3.00 | 90.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 4.20 | 11.86 | 18.54 | 6.00 | 85.3 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.5 | 3.88 | 11.65 | 19.71 | 0.00 | 55.3 | 0.0 |
| XI | XI | Ola Aina | DEF | -1 | 5.4 | 4.14 | 11.63 | 18.19 | 1.00 | 84.8 | 39.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 5.0 | 3.14 | 9.66 | 16.00 | 1.00 | 82.9 | 90.0 |
| Bench 3 | Autosub In | Virgil van Dijk | DEF | -1 | 6.4 | 2.64 | 8.32 | 14.52 | 8.00 | 57.3 | 90.0 |
| XI | Bench | Chris Wood | FWD | -1 | 7.3 | 5.52 | 15.43 | 24.21 | 0.00 | 81.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | -1 | 9.4 | 3.72 | 11.54 | 19.35 | 8.00 | 43.9 | 65.0 |
| Bench 2 | Autosub In | Jean-Philippe Mateta | FWD | -1 | 7.5 | 2.70 | 7.94 | 13.94 | 1.00 | 36.3 | 58.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 7.29 | 21.50 | 35.46 | 3.00 | 75.0 | 90.0 |
| Vice Captain | Bench | Justin Kluivert | MID | -1 | 6.2 | 5.70 | 16.24 | 25.86 | 0.00 | 87.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 5.35 | 15.82 | 25.05 | 8.00 | 92.7 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 3.49 | 10.21 | 17.09 | 9.00 | 51.1 | 85.0 |
| Bench 4 | Autosub In | Morgan Rogers | MID | -1 | 5.6 | 2.59 | 8.11 | 13.63 | 10.00 | 54.0 | 87.0 |

## GW31

- Train rows: 154881
- Bank: 0.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.46
- Actual score: 38.00
- Transfer: Jean-Philippe Mateta -> Omar Marmoush (projected gain 3.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.84 | 11.57 | 18.75 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 2.94 | 9.23 | 15.74 | 3.00 | 88.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.0 | 4.06 | 11.93 | 19.44 | 9.00 | 87.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 3.54 | 10.80 | 18.10 | 1.00 | 82.4 | 90.0 |
| XI | Bench | Ola Aina | DEF | -1 | 5.4 | 3.06 | 9.50 | 16.00 | 0.00 | 68.4 | 0.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | -1 | 4.9 | 2.86 | 9.21 | 15.27 | 1.00 | 82.7 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.3 | 2.30 | 7.73 | 15.41 | 0.00 | 32.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | -1 | 9.4 | 5.22 | 15.18 | 24.88 | 2.00 | 62.4 | 71.0 |
| XI | XI | Omar Marmoush | FWD | -1 | 7.4 | 4.22 | 12.94 | 20.58 | 2.00 | 66.2 | 90.0 |
| Bench 3 | Bench | Chris Wood | FWD | -1 | 7.2 | 2.85 | 9.64 | 18.41 | 0.00 | 38.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 8.06 | 23.43 | 38.63 | 2.00 | 97.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 8.1 | 5.58 | 15.75 | 25.70 | 3.00 | 91.8 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 4.48 | 12.99 | 21.44 | 6.00 | 77.3 | 35.0 |
| XI | Bench | Justin Kluivert | MID | -1 | 6.3 | 3.83 | 11.46 | 19.44 | 0.00 | 51.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.5 | 3.52 | 10.48 | 17.49 | 9.00 | 76.1 | 90.0 |

## GW32

- Train rows: 155673
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 67.48
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.26) beats the best remaining Triple Captain opportunity (14.96).
- Transfer: Ola Aina -> Daniel Muñoz (projected gain 4.90, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (10.26) beats the best remaining Triple Captain opportunity (14.96).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.86 | 11.32 | 18.15 | 2.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.04 | 9.29 | 15.41 | 9.00 | 89.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | -1 | 5.2 | 5.12 | 12.95 | 19.82 | -1.00 | 102.4 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.1 | 4.02 | 11.68 | 18.56 | 1.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.5 | 3.61 | 10.57 | 17.51 | 9.00 | 79.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | -1 | 4.9 | 3.19 | 9.34 | 15.11 | 1.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.3 | 2.19 | 6.99 | 12.80 | 0.00 | 25.9 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.5 | 6.27 | 15.83 | 24.50 | 11.00 | 92.3 | 148.0 |
| XI | XI | Omar Marmoush | FWD | -1 | 7.5 | 4.54 | 12.77 | 20.12 | 7.00 | 78.0 | 81.0 |
| Bench 2 | Bench | Chris Wood | FWD | -1 | 7.1 | 2.60 | 8.55 | 15.54 | 2.00 | 31.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 7.78 | 22.75 | 37.22 | 6.00 | 92.3 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 4.94 | 14.90 | 24.10 | 2.00 | 90.2 | 90.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 4.26 | 12.19 | 20.28 | 9.00 | 62.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.5 | 4.32 | 12.18 | 19.45 | 6.00 | 79.4 | 84.0 |
| Bench 4 | Bench | Justin Kluivert | MID | -1 | 6.2 | 1.96 | 7.47 | 14.43 | 0.00 | 24.6 | 0.0 |

## GW33

- Train rows: 156471
- Bank: 0.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 81.05
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.26) beats the best remaining Bench Boost opportunity (12.05).
- Transfer: Justin Kluivert -> Jacob Murphy (projected gain 7.65, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.26) beats the best remaining Bench Boost opportunity (12.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 5.05 | 12.33 | 18.73 | 7.00 | 113.3 | 180.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | -1 | 5.1 | 3.06 | 9.14 | 14.78 | 1.00 | 87.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | -1 | 5.2 | 5.69 | 14.86 | 22.41 | 6.00 | 138.4 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.2 | 5.17 | 12.60 | 19.06 | 7.00 | 114.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.5 | 4.27 | 11.87 | 19.11 | 7.00 | 89.2 | 90.0 |
| Bench 2 | Bench Boost | Antonee Robinson | DEF | -1 | 4.9 | 3.07 | 8.58 | 13.64 | 1.00 | 82.0 | 90.0 |
| Bench 4 | Bench Boost | Trent Alexander-Arnold | DEF | -1 | 7.2 | 2.08 | 6.44 | 11.47 | 6.00 | 22.2 | 19.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.5 | 6.76 | 19.03 | 29.40 | 2.00 | 105.6 | 75.0 |
| XI | XI | Omar Marmoush | FWD | -1 | 7.6 | 6.34 | 14.99 | 22.09 | 4.00 | 109.4 | 180.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | -1 | 7.0 | 2.80 | 8.95 | 15.42 | 8.00 | 53.9 | 75.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 7.63 | 21.90 | 35.29 | 3.00 | 93.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | -1 | 5.2 | 5.53 | 16.12 | 24.66 | 2.00 | 100.9 | 64.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.0 | 5.02 | 14.42 | 23.20 | 18.00 | 86.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.6 | 5.62 | 14.14 | 21.40 | 7.00 | 110.3 | 166.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 5.33 | 14.04 | 22.35 | 3.00 | 81.6 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 1.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.61
- Actual score: 37.00
- Transfer: Jacob Murphy -> Leandro Trossard (projected gain 1.75, hit 0)
- Autosub: Jordan Pickford replaced David Raya Martin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | -1 | 5.6 | 3.74 | 13.14 | 20.45 | 0.00 | 91.9 | 0.0 |
| Bench 1 | Autosub In | Jordan Pickford | GK | -1 | 5.1 | 2.55 | 8.10 | 13.40 | 4.00 | 83.5 | 90.0 |
| XI | Bench | Daniel Muñoz | DEF | -1 | 5.3 | 4.43 | 14.52 | 22.91 | 0.00 | 101.9 | 0.0 |
| XI | Bench | Joško Gvardiol | DEF | -1 | 6.2 | 3.76 | 13.56 | 21.41 | 0.00 | 93.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.6 | 4.28 | 11.56 | 18.25 | 2.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | -1 | 4.9 | 3.12 | 8.27 | 13.06 | 0.00 | 78.0 | 0.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | -1 | 7.2 | 2.49 | 7.03 | 11.74 | 5.00 | 32.7 | 75.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.5 | 5.84 | 15.90 | 25.16 | 6.00 | 80.5 | 76.0 |
| XI | Bench | Omar Marmoush | FWD | -1 | 7.7 | 4.60 | 15.51 | 23.63 | 0.00 | 82.2 | 0.0 |
| Bench 2 | Bench | Chris Wood | FWD | -1 | 6.9 | 3.16 | 9.31 | 15.25 | 2.00 | 62.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 7.41 | 20.07 | 31.86 | 8.00 | 88.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.9 | 5.72 | 16.57 | 26.56 | 2.00 | 96.1 | 90.0 |
| XI | Bench | Morgan Rogers | MID | -1 | 5.7 | 4.40 | 14.91 | 23.28 | 0.00 | 81.0 | 0.0 |
| XI | Bench | Leandro Trossard | MID | -1 | 6.7 | 4.27 | 13.98 | 21.45 | 0.00 | 86.6 | 0.0 |
| XI | XI | Luis Díaz | MID | -1 | 7.5 | 4.75 | 12.99 | 20.39 | 7.00 | 78.0 | 75.0 |

## GW35

- Train rows: 158070
- Bank: 0.00 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.55
- Actual score: 44.00
- Transfer: Trent Alexander-Arnold -> Rayan Aït-Nouri (projected gain 3.76, hit 0)
- Autosub outfielders: Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | -1 | 5.1 | 3.25 | 9.08 | 14.55 | 2.00 | 85.1 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.6 | 3.04 | 8.86 | 14.53 | 1.00 | 63.6 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 5.0 | 4.10 | 13.01 | 20.26 | 2.00 | 76.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.6 | 3.69 | 11.09 | 17.60 | 6.00 | 81.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | -1 | 5.3 | 3.24 | 9.60 | 15.63 | 1.00 | 69.5 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | -1 | 6.2 | 3.21 | 9.29 | 15.27 | 8.00 | 66.2 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | -1 | 4.8 | 1.53 | 5.75 | 9.75 | 2.00 | 42.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.6 | 6.17 | 17.17 | 26.08 | 9.00 | 86.7 | 90.0 |
| XI | XI | Omar Marmoush | FWD | -1 | 7.7 | 4.05 | 11.31 | 18.06 | 2.00 | 58.2 | 82.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 3.59 | 10.71 | 16.76 | 2.00 | 71.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 7.25 | 20.63 | 32.59 | 2.00 | 91.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.0 | 5.77 | 16.33 | 25.56 | 5.00 | 88.1 | 90.0 |
| XI | Bench | Luis Díaz | MID | -1 | 7.6 | 4.61 | 13.86 | 21.37 | 0.00 | 75.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.7 | 3.58 | 10.49 | 17.07 | 3.00 | 56.9 | 90.0 |
| Bench 3 | Bench | Leandro Trossard | MID | -1 | 6.7 | 2.97 | 8.56 | 13.85 | 2.00 | 52.3 | 90.0 |

## GW36

- Train rows: 158871
- Bank: 2.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.55
- Actual score: 55.00
- Transfer: Luis Díaz -> Jarrod Bowen (projected gain 1.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.6 | 3.33 | 10.13 | 16.54 | 2.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.01 | 9.14 | 14.74 | 3.00 | 85.3 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 5.0 | 4.29 | 11.81 | 19.59 | 1.00 | 80.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.3 | 4.36 | 11.75 | 18.62 | 6.00 | 90.6 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | -1 | 6.7 | 3.93 | 11.57 | 18.60 | 1.00 | 88.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | -1 | 5.3 | 4.04 | 11.25 | 18.00 | 11.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | -1 | 4.8 | 2.84 | 8.17 | 13.51 | 0.00 | 73.9 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | -1 | 9.6 | 6.17 | 17.23 | 27.27 | 2.00 | 89.2 | 90.0 |
| XI | XI | Omar Marmoush | FWD | -1 | 7.6 | 4.77 | 13.06 | 21.25 | 1.00 | 73.9 | 6.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.0 | 4.15 | 10.87 | 17.22 | 8.00 | 76.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.8 | 6.77 | 19.71 | 31.61 | 2.00 | 90.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 8.1 | 5.98 | 16.49 | 26.38 | 6.00 | 94.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.6 | 4.52 | 13.45 | 21.52 | 8.00 | 81.1 | 72.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.7 | 4.40 | 12.77 | 20.41 | 6.00 | 82.2 | 88.0 |
| Bench 3 | Bench | Leandro Trossard | MID | -1 | 6.7 | 3.49 | 10.64 | 16.98 | 7.00 | 76.3 | 77.0 |

## GW37

- Train rows: 159672
- Bank: 2.20 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.96
- Actual score: 48.00
- Transfer: Leandro Trossard -> Eberechi Eze (projected gain 1.16, hit 0)
- Autosub outfielders: Omar Marmoush.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | -1 | 5.1 | 3.57 | 9.67 | 15.34 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | -1 | 5.6 | 3.10 | 9.39 | 15.49 | 7.00 | 79.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.4 | 4.17 | 12.31 | 19.57 | 2.00 | 80.0 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | -1 | 6.7 | 3.86 | 11.50 | 18.42 | 0.00 | 86.8 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | -1 | 5.1 | 3.97 | 11.25 | 18.02 | 0.00 | 81.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | -1 | 5.2 | 4.03 | 11.16 | 17.72 | 1.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | -1 | 4.8 | 1.72 | 5.68 | 9.94 | 1.00 | 40.9 | 88.0 |
| XI | Bench | Alexander Isak | FWD | -1 | 9.6 | 5.53 | 16.38 | 26.15 | 0.00 | 84.8 | 0.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.1 | 4.29 | 11.75 | 18.09 | 2.00 | 77.6 | 90.0 |
| Bench 3 | Autosub In | Omar Marmoush | FWD | -1 | 7.6 | 3.07 | 10.17 | 17.62 | 8.00 | 39.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.7 | 6.51 | 19.22 | 30.96 | 2.00 | 89.4 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 8.2 | 5.75 | 16.85 | 26.65 | 5.00 | 94.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.7 | 4.60 | 13.49 | 21.53 | 8.00 | 79.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.7 | 4.60 | 12.96 | 20.44 | 6.00 | 79.3 | 90.0 |
| XI | XI | Eberechi Eze | MID | -1 | 6.9 | 4.42 | 12.60 | 20.01 | 6.00 | 75.8 | 9.0 |

## GW38

- Train rows: 160473
- Bank: 2.10 -> 1.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.14
- Actual score: 62.00
- Transfer: Rayan Aït-Nouri -> Fabian Schär (projected gain 0.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | -1 | 5.5 | 3.96 | 10.84 | 17.12 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | -1 | 5.1 | 3.25 | 9.76 | 15.58 | 11.00 | 87.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | -1 | 6.5 | 4.39 | 12.54 | 19.77 | 8.00 | 88.6 | 90.0 |
| XI | XI | Fabian Schär | DEF | -1 | 5.5 | 3.99 | 11.37 | 18.20 | 1.00 | 83.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | -1 | 5.2 | 3.57 | 10.78 | 17.49 | 2.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.7 | 2.81 | 8.73 | 14.83 | 1.00 | 55.4 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | -1 | 4.7 | 2.42 | 7.33 | 11.91 | 1.00 | 72.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | -1 | 9.5 | 4.30 | 13.05 | 22.00 | 2.00 | 50.1 | 90.0 |
| XI | XI | Chris Wood | FWD | -1 | 7.2 | 4.15 | 11.26 | 17.43 | 2.00 | 77.7 | 90.0 |
| Bench 2 | Bench | Omar Marmoush | FWD | -1 | 7.5 | 3.59 | 11.08 | 18.76 | 2.00 | 65.2 | 81.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.6 | 6.59 | 19.22 | 30.79 | 10.00 | 91.4 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | -1 | 8.3 | 5.93 | 17.00 | 26.71 | 8.00 | 99.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | -1 | 5.7 | 5.02 | 14.39 | 22.43 | 1.00 | 90.6 | 83.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.8 | 4.97 | 13.68 | 21.71 | 13.00 | 83.8 | 90.0 |
| XI | XI | Eberechi Eze | MID | -1 | 7.0 | 3.68 | 11.42 | 18.92 | 3.00 | 61.3 | 61.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 218.11
- Total actual points: 262.00
- Average predicted points: 54.53
- Average actual points: 65.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 143668
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 51.77
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.25 | 9.26 | 14.67 | 6.00 | 91.6 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.10 | 7.03 | 12.49 | 2.00 | 86.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.91 | 11.66 | 18.58 | 6.00 | 96.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.08 | 8.25 | 13.81 | 6.00 | 67.4 | 62.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 2.62 | 8.11 | 13.70 | 1.00 | 83.0 | 90.0 |
| Bench 2 | Bench | Kyle Walker-Peters | DEF | 17 | 4.4 | 2.50 | 7.33 | 11.73 | 0.00 | 89.0 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 9 | 4.7 | 1.95 | 7.13 | 13.11 | 6.00 | 84.7 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.15 | 9.40 | 15.46 | 1.00 | 84.3 | 58.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 2.74 | 8.78 | 14.57 | 2.00 | 60.1 | 79.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.36 | 5.94 | 9.97 | 1.00 | 73.0 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.44 | 21.49 | 33.96 | 3.00 | 115.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.16 | 19.25 | 32.36 | 5.00 | 100.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 5.28 | 16.29 | 27.79 | 3.00 | 93.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.68 | 11.51 | 18.16 | 5.00 | 91.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.01 | 11.23 | 19.97 | 9.00 | 83.1 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 49.43
- Actual score: 55.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 1.64, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.10 | 8.98 | 14.42 | 3.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.14 | 6.52 | 11.02 | 0.00 | 86.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 4.34 | 11.02 | 17.96 | 6.00 | 111.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.23 | 10.02 | 15.47 | 2.00 | 85.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.50 | 9.76 | 14.73 | 7.00 | 93.9 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.6 | 2.41 | 8.20 | 14.07 | -1.00 | 75.6 | 90.0 |
| Bench 3 | Bench | Kyle Walker-Peters | DEF | 17 | 4.4 | 1.96 | 5.59 | 9.11 | 6.00 | 88.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.08 | 8.17 | 13.36 | 2.00 | 77.4 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.1 | 2.52 | 8.15 | 13.37 | 2.00 | 62.6 | 70.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.39 | 4.70 | 8.22 | 1.00 | 30.4 | 45.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 6.34 | 22.30 | 34.85 | 3.00 | 105.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 5.87 | 18.53 | 31.45 | 21.00 | 92.7 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 5.06 | 15.99 | 26.13 | 1.00 | 89.0 | 23.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.45 | 11.39 | 18.82 | 2.00 | 92.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.59 | 9.97 | 15.30 | 3.00 | 76.3 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.66
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.10) beats the best remaining Bench Boost opportunity (9.95).
- Transfer: Bukayo Saka -> Son Heung-min (projected gain 5.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.10) beats the best remaining Bench Boost opportunity (9.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.39 | 9.79 | 15.69 | 6.00 | 90.5 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 2.11 | 6.42 | 10.27 | 7.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.77 | 10.96 | 17.26 | 7.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 2.77 | 8.34 | 13.91 | 1.00 | 80.3 | 9.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 2.33 | 7.67 | 11.98 | 1.00 | 78.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 2.61 | 7.60 | 12.44 | 6.00 | 76.7 | 90.0 |
| Bench 3 | Bench Boost | Kyle Walker-Peters | DEF | 17 | 4.3 | 2.08 | 5.27 | 9.02 | 2.00 | 77.3 | 85.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 6.0 | 2.59 | 7.98 | 12.56 | 1.00 | 64.2 | 28.0 |
| Bench 2 | Bench Boost | Jamie Vardy | FWD | 11 | 5.6 | 2.20 | 7.22 | 11.82 | 0.00 | 68.3 | 0.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 1.71 | 4.87 | 8.61 | 0.00 | 34.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 8.47 | 21.60 | 36.19 | 9.00 | 107.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.68 | 19.48 | 31.95 | 10.00 | 113.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.57 | 13.28 | 23.26 | 3.00 | 89.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 3.82 | 12.48 | 21.49 | 2.00 | 90.7 | 80.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.08 | 9.44 | 15.49 | 2.00 | 78.0 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 57.25
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Francisco Evanilson de Lima Barbosa -> Chris Wood (projected gain 2.17, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.10 | 9.45 | 15.59 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.90 | 7.82 | 12.88 | 2.00 | 88.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.47 | 10.84 | 18.39 | 2.00 | 88.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.21 | 10.04 | 16.42 | 4.00 | 93.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 3.10 | 8.28 | 13.97 | 12.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.5 | 2.13 | 6.72 | 12.08 | 4.00 | 62.4 | 90.0 |
| XI | XI | Kyle Walker-Peters | DEF | 17 | 4.3 | 2.52 | 6.70 | 10.27 | 1.00 | 85.1 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 2.80 | 8.90 | 14.53 | 12.00 | 76.5 | 75.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 1.00 | 3.95 | 7.12 | 2.00 | 14.5 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.03 | 3.60 | 6.30 | 1.00 | 26.3 | 25.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 7.44 | 21.37 | 35.18 | 16.00 | 112.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 6.49 | 19.04 | 31.97 | 2.00 | 103.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.21 | 12.20 | 19.57 | 7.00 | 87.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 3.79 | 12.01 | 20.81 | 0.00 | 83.4 | 63.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.24 | 9.66 | 15.26 | 1.00 | 81.5 | 90.0 |
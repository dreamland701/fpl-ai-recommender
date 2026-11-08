# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 253.24
- Total actual points: 253.00
- Average predicted points: 63.31
- Average actual points: 63.25
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
- Predicted score: 58.49
- Actual score: 52.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.49 | 10.32 | 16.83 | 6.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.77 | 8.57 | 14.47 | 2.00 | 81.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.14 | 12.24 | 20.47 | 6.00 | 87.1 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.99 | 11.53 | 19.13 | 7.00 | 77.9 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 3.15 | 9.73 | 15.94 | 1.00 | 80.9 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.28 | 9.19 | 14.88 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 9 | 4.7 | 2.79 | 9.17 | 15.47 | 6.00 | 84.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.87 | 11.56 | 18.71 | 1.00 | 86.8 | 58.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.5 | 3.95 | 11.31 | 18.69 | 2.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.83 | 7.60 | 12.32 | 1.00 | 65.8 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 7.73 | 22.15 | 36.16 | 3.00 | 103.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.2 | 6.29 | 19.98 | 34.36 | 5.00 | 70.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.5 | 6.00 | 17.68 | 28.39 | 3.00 | 81.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.19 | 13.23 | 22.92 | 9.00 | 85.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 3.82 | 11.52 | 18.77 | 5.00 | 81.4 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 58.58
- Actual score: 45.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.64 | 10.76 | 17.56 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.60 | 8.38 | 14.05 | 0.00 | 83.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.62 | 11.38 | 19.15 | 0.00 | 84.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.39 | 11.12 | 18.70 | -1.00 | 76.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 4.02 | 11.08 | 18.32 | 6.00 | 93.0 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.78 | 9.18 | 15.06 | 0.00 | 77.9 | 0.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 3.07 | 9.10 | 15.14 | 6.00 | 80.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.5 | 3.81 | 11.14 | 17.99 | 2.00 | 72.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.51 | 9.95 | 16.45 | 2.00 | 73.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.61 | 5.41 | 9.37 | 1.00 | 41.5 | 45.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 7.54 | 22.10 | 35.81 | 3.00 | 97.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.3 | 6.82 | 21.38 | 35.95 | 21.00 | 87.4 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.5 | 6.04 | 18.03 | 29.52 | 1.00 | 82.1 | 23.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.74 | 14.48 | 24.42 | 2.00 | 93.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 3.91 | 12.03 | 19.29 | 3.00 | 76.3 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.38
- Actual score: 70.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.33) beats the best remaining Triple Captain opportunity (10.58).
- Transfer: Joško Gvardiol -> Ola Aina (projected gain 0.46, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.33) beats the best remaining Triple Captain opportunity (10.58).
- Autosub: Daniel Muñoz replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.91 | 11.07 | 18.16 | 6.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.42 | 7.32 | 12.19 | 7.00 | 79.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.65 | 11.26 | 18.05 | 1.00 | 85.3 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 4.9 | 3.87 | 10.77 | 17.64 | 6.00 | 85.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.42 | 10.74 | 18.27 | 1.00 | 84.2 | 9.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.31 | 9.34 | 15.30 | 6.00 | 84.6 | 90.0 |
| Bench 4 | Autosub In | Daniel Muñoz | DEF | 7 | 4.7 | 1.62 | 5.73 | 10.28 | 6.00 | 43.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.5 | 3.79 | 10.93 | 17.80 | 2.00 | 69.2 | 86.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.09 | 10.00 | 16.57 | 0.00 | 72.5 | 0.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.00 | 5.87 | 9.86 | 0.00 | 46.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.3 | 8.33 | 24.10 | 39.86 | 9.00 | 98.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 7.17 | 21.46 | 35.38 | 10.00 | 96.9 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.5 | 5.34 | 15.70 | 26.30 | 0.00 | 60.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.83 | 14.53 | 24.15 | 3.00 | 90.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.12 | 11.87 | 19.46 | 2.00 | 82.4 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 1.20 -> 4.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.79
- Actual score: 86.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.95) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bukayo Saka -> Anthony Gordon (projected gain 4.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.95) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.99 | 11.75 | 19.30 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 3.32 | 8.91 | 14.40 | 2.00 | 85.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 4.23 | 12.15 | 20.08 | 4.00 | 92.2 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 4.9 | 3.57 | 10.56 | 17.11 | 8.00 | 82.2 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.35 | 9.81 | 15.97 | 1.00 | 84.2 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.5 | 2.86 | 9.24 | 16.22 | 4.00 | 55.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.35 | 8.98 | 14.64 | 2.00 | 72.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.5 | 3.36 | 10.14 | 16.56 | 12.00 | 67.8 | 75.0 |
| Bench 3 | Bench Boost | Jamie Vardy | FWD | 11 | 5.5 | 1.75 | 6.11 | 10.47 | 2.00 | 32.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 1.02 | 3.60 | 6.55 | 1.00 | 25.6 | 25.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.3 | 8.61 | 24.91 | 40.78 | 16.00 | 104.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.88 | 20.91 | 34.84 | 2.00 | 88.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.38 | 13.89 | 23.04 | 7.00 | 86.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.2 | 4.38 | 13.11 | 21.39 | 6.00 | 74.5 | 84.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.14 | 11.74 | 19.10 | 1.00 | 81.7 | 90.0 |
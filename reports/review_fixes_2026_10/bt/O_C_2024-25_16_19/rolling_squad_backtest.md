# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 253.18
- Total actual points: 253.00
- Average predicted points: 63.30
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
- Predicted score: 58.42
- Actual score: 52.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.48 | 10.30 | 16.85 | 6.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.74 | 8.50 | 14.26 | 2.00 | 81.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.16 | 12.26 | 20.42 | 6.00 | 87.0 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.01 | 11.55 | 19.05 | 7.00 | 77.9 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 3.13 | 9.67 | 15.86 | 1.00 | 80.9 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.31 | 9.22 | 14.95 | 2.00 | 76.9 | 90.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 9 | 4.7 | 2.79 | 9.18 | 15.46 | 6.00 | 84.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.89 | 11.57 | 18.77 | 1.00 | 86.7 | 58.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.5 | 3.92 | 11.25 | 18.63 | 2.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.86 | 7.62 | 12.33 | 1.00 | 65.8 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 7.70 | 22.14 | 36.34 | 3.00 | 103.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.2 | 6.29 | 20.04 | 34.56 | 5.00 | 70.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.5 | 5.99 | 17.71 | 28.65 | 3.00 | 81.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.18 | 13.24 | 22.87 | 9.00 | 85.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 3.79 | 11.53 | 18.85 | 5.00 | 81.4 | 90.0 |

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
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.62 | 10.80 | 17.66 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.57 | 8.34 | 13.94 | 0.00 | 83.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.59 | 11.39 | 19.14 | 0.00 | 84.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 4.05 | 11.15 | 18.36 | 6.00 | 93.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.40 | 11.08 | 18.64 | -1.00 | 76.6 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 3.09 | 9.14 | 15.17 | 6.00 | 80.0 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 2.75 | 9.13 | 15.00 | 0.00 | 77.9 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.78 | 11.11 | 18.02 | 2.00 | 72.4 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.54 | 10.00 | 16.49 | 2.00 | 72.9 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.60 | 5.36 | 9.36 | 1.00 | 41.5 | 45.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.53 | 22.04 | 35.94 | 3.00 | 97.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.85 | 21.38 | 36.19 | 21.00 | 87.4 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.02 | 18.18 | 29.91 | 1.00 | 82.1 | 23.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.77 | 14.51 | 24.44 | 2.00 | 93.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.90 | 12.01 | 19.31 | 3.00 | 76.4 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.37
- Actual score: 70.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.33) beats the best remaining Triple Captain opportunity (10.57).
- Transfer: Joško Gvardiol -> Ola Aina (projected gain 0.59, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.33) beats the best remaining Triple Captain opportunity (10.57).
- Autosub outfielders: Daniel Muñoz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.90 | 11.16 | 18.28 | 6.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.39 | 7.36 | 12.22 | 7.00 | 79.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.63 | 11.35 | 18.10 | 1.00 | 85.4 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 4.9 | 3.90 | 10.89 | 17.87 | 6.00 | 85.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.44 | 10.72 | 18.15 | 1.00 | 84.1 | 9.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.7 | 3.29 | 9.35 | 15.28 | 6.00 | 84.6 | 90.0 |
| Bench 4 | Autosub In | Daniel Muñoz | DEF | 7 | 4.7 | 1.59 | 5.78 | 10.37 | 6.00 | 43.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.82 | 11.05 | 18.06 | 2.00 | 69.1 | 86.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 3.10 | 10.00 | 16.61 | 0.00 | 72.5 | 0.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.03 | 5.92 | 9.98 | 0.00 | 46.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 8.33 | 24.15 | 40.07 | 9.00 | 98.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.16 | 21.44 | 35.49 | 10.00 | 96.9 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.6 | 5.33 | 15.80 | 26.62 | 0.00 | 60.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.81 | 14.52 | 24.15 | 3.00 | 90.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 4.11 | 11.85 | 19.45 | 2.00 | 82.5 | 90.0 |

## GW19

- Train rows: 145775
- Bank: 1.20 -> 4.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.81
- Actual score: 86.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bukayo Saka -> Anthony Gordon (projected gain 4.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.96 | 11.78 | 19.39 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.4 | 3.34 | 8.94 | 14.45 | 2.00 | 85.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.20 | 12.16 | 20.06 | 4.00 | 92.3 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.0 | 3.56 | 10.57 | 17.16 | 8.00 | 82.3 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.7 | 3.34 | 9.79 | 16.01 | 1.00 | 84.2 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.5 | 2.90 | 9.20 | 16.00 | 4.00 | 55.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.7 | 3.37 | 9.01 | 14.69 | 2.00 | 72.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.35 | 10.23 | 16.76 | 12.00 | 67.8 | 75.0 |
| Bench 3 | Bench Boost | Jamie Vardy | FWD | 11 | 5.6 | 1.76 | 6.09 | 10.58 | 2.00 | 32.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 5.0 | 1.00 | 3.62 | 6.55 | 1.00 | 25.7 | 25.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.64 | 24.96 | 40.85 | 16.00 | 104.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.87 | 20.99 | 35.15 | 2.00 | 88.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.34 | 13.83 | 22.99 | 7.00 | 86.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.2 | 4.39 | 13.24 | 21.61 | 6.00 | 74.5 | 84.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 4.14 | 11.62 | 19.03 | 1.00 | 81.7 | 90.0 |
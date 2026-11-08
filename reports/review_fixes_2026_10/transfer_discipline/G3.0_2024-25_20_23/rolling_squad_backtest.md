# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 280.44
- Total actual points: 229.00
- Average predicted points: 70.11
- Average actual points: 57.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 146484
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.56
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.67 | 10.73 | 17.43 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 3.48 | 9.96 | 15.83 | 9.00 | 94.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.52 | 14.69 | 23.32 | 0.00 | 90.5 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.81 | 12.94 | 20.61 | 2.00 | 90.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.77 | 12.74 | 20.26 | 1.00 | 98.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.97 | 12.07 | 20.02 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 3.16 | 9.56 | 15.27 | 6.00 | 83.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.05 | 9.74 | 16.02 | 9.00 | 72.7 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.69 | 8.58 | 13.72 | 5.00 | 58.2 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.64 | 7.36 | 12.05 | 1.00 | 65.2 | 35.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.27 | 27.83 | 45.19 | 7.00 | 114.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.39 | 22.12 | 36.44 | 10.00 | 106.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.72 | 15.58 | 25.09 | 19.00 | 100.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.25 | 14.65 | 22.97 | 7.00 | 82.5 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.89 | 11.16 | 18.19 | 5.00 | 65.5 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.32
- Actual score: 48.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 10.65 | 17.32 | 2.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.79 | 9.02 | 14.75 | 3.00 | 83.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.50 | 12.76 | 19.77 | 6.00 | 86.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.46 | 11.53 | 19.05 | 2.00 | 70.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.09 | 11.45 | 18.89 | 2.00 | 86.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.92 | 11.36 | 18.29 | 7.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.84 | 8.93 | 14.59 | 2.00 | 79.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.96 | 10.88 | 17.70 | 1.00 | 80.7 | 77.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.09 | 8.52 | 13.80 | 2.00 | 66.2 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.13 | 6.38 | 10.94 | 1.00 | 56.9 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.26 | 26.06 | 42.65 | 2.00 | 110.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.31 | 21.74 | 35.79 | 10.00 | 112.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.40 | 16.06 | 25.94 | 2.00 | 98.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.75 | 16.01 | 25.13 | 9.00 | 91.1 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.58 | 10.97 | 17.59 | 3.00 | 69.0 | 77.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 75.15
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.49) beats the best remaining Bench Boost opportunity (14.19).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.49) beats the best remaining Bench Boost opportunity (14.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 4.36 | 11.45 | 18.18 | 1.00 | 96.1 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.55 | 10.21 | 16.85 | 1.00 | 85.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.11 | 12.39 | 20.78 | 11.00 | 78.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.51 | 12.05 | 19.50 | 8.00 | 91.6 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.96 | 11.31 | 17.87 | 4.00 | 80.9 | 65.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.81 | 11.07 | 18.34 | 0.00 | 86.1 | 0.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 4.7 | 3.81 | 9.98 | 15.96 | 1.00 | 83.8 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.28 | 9.49 | 15.75 | 2.00 | 65.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.39 | 9.44 | 14.87 | 2.00 | 69.8 | 90.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.47 | 5.27 | 9.21 | 1.00 | 48.0 | 57.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.03 | 26.47 | 43.21 | 3.00 | 106.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.68 | 22.54 | 36.84 | 2.00 | 110.7 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.99 | 15.07 | 25.20 | 2.00 | 89.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.98 | 14.86 | 23.25 | 2.00 | 76.7 | 90.0 |
| Bench 3 | Bench Boost | Jacob Murphy | MID | 15 | 5.1 | 3.19 | 9.84 | 16.40 | 2.00 | 64.0 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.42
- Actual score: 64.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Ola Aina (projected gain 3.05, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.40 | 9.85 | 16.28 | 9.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.86 | 9.03 | 14.78 | 1.00 | 82.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 6.07 | 16.38 | 25.79 | 5.00 | 100.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.72 | 11.94 | 18.89 | 2.00 | 78.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.16 | 11.47 | 18.71 | 2.00 | 84.1 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.92 | 11.42 | 18.26 | 1.00 | 91.9 | 78.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.73 | 8.35 | 13.79 | 0.00 | 78.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.44 | 9.84 | 16.16 | 1.00 | 73.2 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.15 | 8.50 | 14.11 | 9.00 | 70.7 | 76.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.85 | 6.08 | 10.38 | 1.00 | 57.5 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.29 | 25.89 | 41.96 | 8.00 | 104.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.29 | 19.98 | 33.53 | 2.00 | 97.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.42 | 16.00 | 26.55 | 7.00 | 100.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.50 | 14.76 | 23.67 | 5.00 | 77.9 | 87.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.61 | 9.27 | 15.77 | 6.00 | 60.8 | 90.0 |
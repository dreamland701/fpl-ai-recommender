# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 281.93
- Total actual points: 230.00
- Average predicted points: 70.48
- Average actual points: 57.50
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
- Predicted score: 68.57
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.67 | 10.77 | 17.49 | 3.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 3.47 | 9.94 | 15.81 | 9.00 | 95.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.51 | 14.73 | 23.44 | 0.00 | 90.3 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.81 | 12.93 | 20.59 | 2.00 | 91.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.77 | 12.79 | 20.34 | 1.00 | 97.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.95 | 12.04 | 20.00 | 2.00 | 85.8 | 90.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 3.17 | 9.51 | 15.15 | 6.00 | 83.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.05 | 9.72 | 15.96 | 9.00 | 72.8 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.69 | 8.58 | 13.74 | 5.00 | 58.5 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.63 | 7.41 | 12.17 | 1.00 | 65.0 | 35.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.27 | 27.90 | 45.32 | 7.00 | 114.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.42 | 22.16 | 36.44 | 10.00 | 106.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.71 | 15.55 | 25.07 | 19.00 | 100.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.24 | 14.69 | 23.07 | 7.00 | 82.3 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.89 | 11.19 | 18.22 | 5.00 | 65.0 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.01
- Actual score: 48.00
- Transfer: João Pedro Junqueira de Jesus -> Raúl Jiménez (projected gain 1.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 10.68 | 17.37 | 2.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.79 | 9.00 | 14.71 | 3.00 | 83.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.50 | 12.75 | 19.74 | 6.00 | 86.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.45 | 11.56 | 19.16 | 2.00 | 70.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.08 | 11.42 | 18.86 | 2.00 | 86.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.93 | 11.40 | 18.36 | 7.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.85 | 8.88 | 14.46 | 2.00 | 79.6 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.63 | 12.28 | 18.47 | 1.00 | 75.2 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.08 | 8.52 | 13.81 | 2.00 | 66.5 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.12 | 6.44 | 11.07 | 1.00 | 56.7 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.27 | 26.13 | 42.77 | 2.00 | 110.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.34 | 21.78 | 35.77 | 10.00 | 112.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.74 | 16.04 | 25.22 | 9.00 | 90.8 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.39 | 16.03 | 25.91 | 2.00 | 98.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.59 | 11.00 | 17.61 | 3.00 | 68.5 | 77.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 75.97
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.60) beats the best remaining Bench Boost opportunity (14.19).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.60) beats the best remaining Bench Boost opportunity (14.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 4.36 | 11.43 | 18.15 | 1.00 | 96.3 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.55 | 10.25 | 16.91 | 1.00 | 85.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.09 | 12.43 | 20.88 | 11.00 | 78.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.52 | 12.09 | 19.56 | 8.00 | 91.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.96 | 11.29 | 17.84 | 4.00 | 81.2 | 65.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.80 | 11.04 | 18.31 | 0.00 | 86.4 | 0.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 4.7 | 3.82 | 9.93 | 15.84 | 1.00 | 83.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.08 | 10.25 | 16.42 | 2.00 | 57.4 | 70.0 |
| Bench 2 | Bench Boost | Jamie Vardy | FWD | 11 | 5.5 | 3.38 | 9.44 | 14.88 | 2.00 | 70.1 | 90.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.47 | 5.33 | 9.35 | 1.00 | 47.8 | 57.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.04 | 26.55 | 43.36 | 3.00 | 106.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.72 | 22.59 | 36.83 | 2.00 | 110.5 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.98 | 15.03 | 25.16 | 2.00 | 90.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.98 | 14.90 | 23.34 | 2.00 | 76.4 | 90.0 |
| Bench 3 | Bench Boost | Jacob Murphy | MID | 15 | 5.1 | 3.20 | 9.87 | 16.42 | 2.00 | 63.5 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.38
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.30) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Ola Aina (projected gain 3.04, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.30) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.40 | 9.89 | 16.33 | 9.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.86 | 9.01 | 14.75 | 1.00 | 83.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 6.07 | 16.42 | 25.89 | 5.00 | 100.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.72 | 11.92 | 18.86 | 2.00 | 78.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.16 | 11.51 | 18.78 | 2.00 | 83.6 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.92 | 11.40 | 18.23 | 1.00 | 92.1 | 78.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.74 | 8.31 | 13.67 | 0.00 | 78.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.36 | 9.17 | 15.17 | 2.00 | 49.0 | 63.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.14 | 8.49 | 14.11 | 9.00 | 70.9 | 76.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.84 | 6.14 | 10.52 | 1.00 | 57.3 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.30 | 25.97 | 42.11 | 8.00 | 104.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.32 | 20.03 | 33.52 | 2.00 | 97.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.41 | 15.97 | 26.52 | 7.00 | 100.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.50 | 14.80 | 23.77 | 5.00 | 77.6 | 87.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.62 | 9.30 | 15.79 | 6.00 | 60.4 | 90.0 |
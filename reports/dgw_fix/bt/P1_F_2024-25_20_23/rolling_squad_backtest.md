# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 280.78
- Total actual points: 230.00
- Average predicted points: 70.19
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
- Predicted score: 68.24
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 10.73 | 17.43 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 3.34 | 9.96 | 15.83 | 9.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.42 | 14.69 | 23.32 | 0.00 | 87.9 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.69 | 12.94 | 20.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.62 | 12.74 | 20.26 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.04 | 12.07 | 20.02 | 2.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 3.09 | 9.56 | 15.27 | 6.00 | 83.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.13 | 9.74 | 16.02 | 9.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.68 | 8.58 | 13.72 | 5.00 | 58.5 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.64 | 7.36 | 12.05 | 1.00 | 64.9 | 35.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.28 | 27.83 | 45.19 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.48 | 22.12 | 36.44 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.62 | 15.58 | 25.09 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.10 | 14.65 | 22.97 | 7.00 | 80.4 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.85 | 11.16 | 18.19 | 5.00 | 67.2 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.26
- Actual score: 48.00
- Transfer: João Pedro Junqueira de Jesus -> Raúl Jiménez (projected gain 1.34, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 10.65 | 17.32 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.78 | 9.02 | 14.75 | 3.00 | 84.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.27 | 12.76 | 19.77 | 6.00 | 84.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.43 | 11.53 | 19.05 | 2.00 | 69.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.17 | 11.45 | 18.89 | 2.00 | 86.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.92 | 11.36 | 18.29 | 7.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.83 | 8.93 | 14.59 | 2.00 | 80.3 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.43 | 12.22 | 18.38 | 1.00 | 73.3 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.08 | 8.52 | 13.80 | 2.00 | 65.6 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.17 | 6.38 | 10.94 | 1.00 | 57.8 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.21 | 26.06 | 42.65 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.42 | 21.74 | 35.79 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.35 | 16.06 | 25.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.44 | 16.01 | 25.13 | 9.00 | 86.1 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.53 | 10.97 | 17.59 | 3.00 | 69.9 | 77.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 75.79
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.65) beats the best remaining Bench Boost opportunity (14.25).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.65) beats the best remaining Bench Boost opportunity (14.25).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 4.29 | 11.45 | 18.18 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.61 | 10.21 | 16.85 | 1.00 | 86.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.11 | 12.39 | 20.78 | 11.00 | 78.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.53 | 12.05 | 19.50 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.31 | 17.87 | 4.00 | 79.6 | 65.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.89 | 11.07 | 18.34 | 0.00 | 86.5 | 0.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 4.7 | 3.79 | 9.98 | 15.96 | 1.00 | 84.6 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.94 | 10.19 | 16.33 | 2.00 | 56.9 | 70.0 |
| Bench 2 | Bench Boost | Jamie Vardy | FWD | 11 | 5.5 | 3.32 | 9.44 | 14.87 | 2.00 | 69.2 | 90.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.55 | 5.27 | 9.21 | 1.00 | 49.4 | 57.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.06 | 26.47 | 43.21 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.86 | 22.54 | 36.84 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.97 | 15.07 | 25.20 | 2.00 | 89.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.81 | 14.86 | 23.25 | 2.00 | 74.5 | 90.0 |
| Bench 3 | Bench Boost | Jacob Murphy | MID | 15 | 5.1 | 3.18 | 9.84 | 16.40 | 2.00 | 65.0 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 74.49
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.37) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Ola Aina (projected gain 3.03, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.37) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.48 | 9.85 | 16.28 | 9.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.85 | 9.03 | 14.78 | 1.00 | 83.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.93 | 16.38 | 25.79 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.63 | 11.94 | 18.89 | 2.00 | 78.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.22 | 11.47 | 18.71 | 2.00 | 84.7 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.87 | 11.42 | 18.26 | 1.00 | 90.0 | 78.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.74 | 8.35 | 13.79 | 0.00 | 79.6 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.37 | 9.12 | 15.08 | 2.00 | 50.7 | 63.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.11 | 8.50 | 14.11 | 9.00 | 70.5 | 76.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.94 | 6.08 | 10.38 | 1.00 | 59.3 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.37 | 25.89 | 41.96 | 8.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.45 | 19.98 | 33.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.32 | 16.00 | 26.55 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.50 | 14.76 | 23.67 | 5.00 | 79.0 | 87.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.62 | 9.27 | 15.77 | 6.00 | 61.7 | 90.0 |
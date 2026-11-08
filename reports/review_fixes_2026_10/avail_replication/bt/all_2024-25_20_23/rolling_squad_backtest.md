# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 233.63
- Total actual points: 236.00
- Average predicted points: 58.41
- Average actual points: 59.00
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
- Predicted score: 58.66
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.07 | 9.63 | 15.33 | 3.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.68 | 8.46 | 13.43 | 9.00 | 95.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.12 | 11.69 | 18.32 | 0.00 | 91.5 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.27 | 11.64 | 18.16 | 1.00 | 98.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.21 | 11.54 | 18.51 | 2.00 | 93.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.37 | 10.97 | 17.52 | 2.00 | 89.5 | 90.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.66 | 8.46 | 13.17 | 6.00 | 86.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 2.45 | 8.34 | 13.92 | 9.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.39 | 7.58 | 12.32 | 5.00 | 68.2 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.14 | 6.26 | 10.35 | 1.00 | 48.2 | 35.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.27 | 23.83 | 39.19 | 7.00 | 113.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.39 | 18.12 | 30.44 | 10.00 | 104.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.35 | 13.45 | 21.17 | 7.00 | 86.5 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.62 | 13.38 | 23.39 | 19.00 | 100.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.29 | 10.06 | 16.79 | 5.00 | 73.5 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.62
- Actual score: 48.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.12 | 9.55 | 15.62 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.39 | 7.72 | 12.05 | 3.00 | 85.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 3.90 | 11.06 | 17.37 | 6.00 | 92.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.12 | 10.26 | 16.29 | 7.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.39 | 10.15 | 16.39 | 2.00 | 89.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 2.76 | 10.03 | 16.65 | 2.00 | 75.7 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.04 | 7.23 | 12.19 | 2.00 | 82.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.56 | 9.68 | 15.60 | 1.00 | 83.7 | 77.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.29 | 7.32 | 12.10 | 2.00 | 65.2 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.83 | 5.28 | 9.04 | 1.00 | 46.9 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.26 | 22.06 | 36.65 | 2.00 | 109.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.21 | 17.74 | 29.79 | 10.00 | 111.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.40 | 12.66 | 20.94 | 2.00 | 97.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.75 | 12.61 | 19.53 | 9.00 | 90.1 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 2.88 | 9.37 | 15.09 | 3.00 | 75.0 | 77.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.65
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.69) beats the best remaining Bench Boost opportunity (11.87).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.69) beats the best remaining Bench Boost opportunity (11.87).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 3.86 | 10.15 | 15.88 | 1.00 | 98.1 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 2.95 | 8.61 | 14.45 | 1.00 | 87.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.41 | 11.29 | 18.38 | 11.00 | 82.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 2.91 | 9.97 | 17.24 | 0.00 | 90.1 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.36 | 9.71 | 15.57 | 4.00 | 85.9 | 65.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.21 | 9.35 | 14.90 | 8.00 | 90.6 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 4.7 | 3.21 | 8.48 | 13.96 | 1.00 | 86.8 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 2.68 | 8.29 | 14.45 | 2.00 | 71.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 2.79 | 7.74 | 12.27 | 2.00 | 75.8 | 90.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.47 | 5.27 | 9.21 | 1.00 | 48.0 | 57.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.73 | 22.47 | 37.21 | 3.00 | 103.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.48 | 19.14 | 31.54 | 2.00 | 109.7 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 3.88 | 12.56 | 18.65 | 2.00 | 75.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.39 | 11.07 | 19.20 | 2.00 | 69.9 | 90.0 |
| Bench 3 | Bench Boost | Jacob Murphy | MID | 15 | 5.1 | 2.59 | 8.24 | 13.90 | 2.00 | 71.0 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.71
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.79) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Ola Aina (projected gain 2.95, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.79) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 2.90 | 8.45 | 13.78 | 9.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.56 | 7.93 | 12.38 | 1.00 | 85.9 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.07 | 13.28 | 20.29 | 5.00 | 99.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.32 | 10.64 | 16.59 | 2.00 | 85.5 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.22 | 10.32 | 16.26 | 1.00 | 92.9 | 78.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | 9 | 5.0 | 2.56 | 7.47 | 12.71 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.43 | 7.35 | 12.29 | 0.00 | 82.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 2.94 | 8.44 | 13.76 | 1.00 | 72.2 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 2.65 | 7.10 | 11.61 | 9.00 | 76.7 | 76.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.65 | 5.48 | 9.48 | 1.00 | 56.5 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.79 | 21.89 | 35.96 | 8.00 | 103.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 4.69 | 15.98 | 27.53 | 2.00 | 77.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.12 | 12.60 | 20.85 | 7.00 | 98.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.40 | 11.96 | 19.07 | 5.00 | 76.9 | 87.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.01 | 7.97 | 13.37 | 6.00 | 69.8 | 90.0 |
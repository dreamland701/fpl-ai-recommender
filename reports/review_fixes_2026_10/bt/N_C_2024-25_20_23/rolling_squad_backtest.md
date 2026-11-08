# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 277.29
- Total actual points: 225.00
- Average predicted points: 69.32
- Average actual points: 56.25
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
- Predicted score: 65.85
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 10.80 | 17.62 | 3.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 3.62 | 10.18 | 16.23 | 9.00 | 95.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.22 | 14.00 | 22.36 | 0.00 | 87.0 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.80 | 12.76 | 20.36 | 1.00 | 99.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.01 | 12.14 | 20.21 | 2.00 | 86.3 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.18 | 11.92 | 19.08 | 2.00 | 86.6 | 90.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 3.29 | 9.72 | 15.57 | 6.00 | 83.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.20 | 9.80 | 16.25 | 9.00 | 73.2 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.69 | 8.36 | 13.53 | 5.00 | 57.6 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.64 | 7.39 | 12.12 | 1.00 | 65.9 | 35.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.69 | 26.73 | 43.61 | 7.00 | 113.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.26 | 22.00 | 36.26 | 10.00 | 106.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.70 | 15.76 | 25.36 | 19.00 | 101.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.74 | 13.68 | 21.53 | 7.00 | 78.5 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.66 | 10.75 | 17.66 | 1.00 | 79.8 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.67
- Actual score: 47.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 10.47 | 17.08 | 2.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.76 | 8.95 | 14.66 | 3.00 | 81.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.42 | 12.45 | 19.38 | 6.00 | 84.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.64 | 11.60 | 19.23 | 2.00 | 68.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.98 | 11.27 | 18.62 | 2.00 | 84.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.82 | 11.17 | 18.08 | 7.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.78 | 8.84 | 14.45 | 2.00 | 77.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.93 | 10.96 | 17.76 | 1.00 | 80.1 | 77.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.96 | 8.45 | 13.55 | 2.00 | 63.7 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.05 | 6.25 | 10.77 | 1.00 | 56.0 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.01 | 26.49 | 43.62 | 2.00 | 110.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.67 | 22.16 | 36.59 | 10.00 | 115.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.53 | 16.38 | 26.38 | 2.00 | 98.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.72 | 15.75 | 24.87 | 9.00 | 90.2 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.23 | 9.69 | 16.00 | 2.00 | 75.9 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 74.69
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.52) beats the best remaining Bench Boost opportunity (13.38).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.52) beats the best remaining Bench Boost opportunity (13.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 4.15 | 11.13 | 17.76 | 1.00 | 97.6 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.56 | 10.28 | 16.88 | 1.00 | 85.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.99 | 12.14 | 20.33 | 11.00 | 76.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.38 | 12.03 | 19.36 | 8.00 | 91.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.07 | 11.33 | 17.90 | 4.00 | 80.0 | 65.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.81 | 11.12 | 18.34 | 0.00 | 85.9 | 0.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 4.7 | 3.65 | 9.78 | 15.67 | 1.00 | 85.0 | 90.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.16 | 9.53 | 15.68 | 2.00 | 65.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.37 | 9.25 | 14.65 | 2.00 | 69.4 | 90.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.59 | 5.46 | 9.51 | 1.00 | 49.3 | 57.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.98 | 26.29 | 42.92 | 3.00 | 105.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.66 | 22.24 | 36.58 | 2.00 | 113.3 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.92 | 15.20 | 25.16 | 2.00 | 87.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.22 | 14.90 | 23.42 | 2.00 | 77.1 | 90.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 6 | 5.0 | 3.21 | 9.40 | 15.54 | 0.00 | 72.5 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.07
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.10) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Ola Aina (projected gain 3.27, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.10) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.38 | 9.90 | 16.30 | 9.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.97 | 9.22 | 15.02 | 1.00 | 83.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.93 | 16.19 | 25.49 | 5.00 | 101.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.40 | 11.68 | 18.41 | 2.00 | 78.4 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.05 | 11.62 | 18.52 | 1.00 | 92.5 | 78.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.04 | 11.39 | 18.50 | 2.00 | 83.4 | 90.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.82 | 8.51 | 13.98 | 0.00 | 79.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.51 | 10.09 | 16.43 | 1.00 | 74.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.06 | 8.50 | 13.98 | 9.00 | 70.3 | 76.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.82 | 6.01 | 10.24 | 1.00 | 56.4 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.10 | 25.86 | 41.86 | 8.00 | 107.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 6.52 | 20.15 | 33.80 | 2.00 | 97.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.81 | 16.67 | 27.43 | 7.00 | 101.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.07 | 14.25 | 22.89 | 5.00 | 78.4 | 87.0 |
| Bench 4 | Bench | Enzo Fernández | MID | 6 | 4.9 | 1.29 | 4.87 | 9.05 | 2.00 | 32.9 | 90.0 |
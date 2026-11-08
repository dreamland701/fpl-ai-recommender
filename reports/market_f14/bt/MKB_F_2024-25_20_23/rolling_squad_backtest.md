# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 284.33
- Total actual points: 259.00
- Average predicted points: 71.08
- Average actual points: 64.75
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
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 72.99
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 10.73 | 17.41 | 3.00 | 86.8 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.01 | 0.22 | 0.38 | 0.00 | 5.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.34 | 14.45 | 22.96 | 0.00 | 88.1 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.64 | 12.87 | 20.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.66 | 12.81 | 20.32 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.96 | 6.14 | 9.59 | 1.00 | 74.2 | 81.0 |
| Bench 3 | Bench | James Bree | DEF | 17 | 3.9 | 1.89 | 5.07 | 7.97 | 1.00 | 53.6 | 45.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.76 | 21.53 | 34.38 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.88 | 13.99 | 21.60 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.17 | 0.56 | 1.03 | 0.00 | 5.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.12 | 27.36 | 44.50 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.41 | 22.01 | 36.29 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.56 | 15.42 | 24.87 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.02 | 14.51 | 22.78 | 7.00 | 80.8 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.76 | 11.04 | 18.04 | 1.00 | 80.5 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.24
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 10.65 | 17.32 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.07 | 0.32 | 0.48 | 0.00 | 5.1 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.27 | 12.76 | 19.76 | 6.00 | 84.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.49 | 11.69 | 19.28 | 2.00 | 68.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.87 | 11.23 | 18.10 | 7.00 | 83.2 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.19 | 6.29 | 10.13 | 0.00 | 74.9 | 0.0 |
| Bench 3 | Bench | James Bree | DEF | 17 | 3.9 | 1.56 | 4.60 | 7.32 | 1.00 | 47.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.55 | 20.10 | 32.08 | 16.00 | 80.1 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.40 | 10.84 | 17.18 | 9.00 | 65.8 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.05 | 0.43 | 0.74 | 0.00 | 5.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.23 | 26.11 | 42.71 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.39 | 21.75 | 35.81 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.43 | 15.96 | 25.04 | 9.00 | 86.2 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.26 | 15.86 | 25.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.25 | 9.89 | 16.16 | 2.00 | 74.9 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.84
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.14) beats the best remaining Bench Boost opportunity (3.62).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.14) beats the best remaining Bench Boost opportunity (3.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.27 | 11.36 | 18.01 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.17 | 0.25 | 0.52 | 0.00 | 5.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.10 | 12.42 | 20.84 | 11.00 | 78.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.49 | 11.93 | 19.29 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.75 | 11.15 | 17.65 | 4.00 | 80.0 | 65.0 |
| Bench 2 | Bench Boost | James Bree | DEF | 17 | 3.9 | 1.86 | 5.65 | 8.86 | 1.00 | 63.7 | 85.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.07 | 3.42 | 5.99 | 0.00 | 40.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.83 | 21.49 | 34.30 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.48 | 17.05 | 26.54 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.04 | 0.53 | 0.97 | 0.00 | 4.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.98 | 26.33 | 43.01 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.86 | 22.61 | 36.95 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.92 | 14.93 | 25.00 | 2.00 | 89.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.75 | 14.73 | 23.06 | 2.00 | 74.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.27 | 9.69 | 15.91 | 0.00 | 72.2 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 76.26
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.31) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.31) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.77 | 8.84 | 14.53 | 1.00 | 83.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.00 | 0.05 | 0.29 | 0.00 | 3.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.98 | 16.59 | 26.19 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.56 | 11.78 | 18.65 | 2.00 | 78.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.13 | 11.22 | 18.34 | 2.00 | 84.8 | 90.0 |
| XI | XI | James Bree | DEF | 17 | 3.9 | 1.67 | 5.11 | 8.00 | 4.00 | 61.6 | 87.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.64 | 2.14 | 4.21 | 1.00 | 29.6 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.78 | 20.84 | 33.65 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.33 | 13.51 | 21.54 | 2.00 | 78.4 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.28 | 0.59 | 0.00 | 3.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.31 | 25.84 | 41.99 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.42 | 19.98 | 33.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.24 | 15.85 | 26.35 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.44 | 14.61 | 23.43 | 5.00 | 79.5 | 87.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.9 | 1.35 | 5.21 | 9.55 | 2.00 | 33.8 | 90.0 |
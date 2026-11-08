# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.53
- Total actual points: 256.00
- Average predicted points: 70.88
- Average actual points: 64.00
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
- Predicted score: 73.48
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.77 | 17.49 | 3.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.09 | 0.64 | 1.07 | 0.00 | 9.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.42 | 14.70 | 23.33 | 0.00 | 87.9 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.70 | 12.96 | 20.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.55 | 12.58 | 20.02 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.91 | 6.04 | 9.45 | 1.00 | 74.5 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.87 | 5.19 | 7.92 | 1.00 | 58.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.74 | 21.48 | 34.26 | 7.00 | 89.9 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.83 | 13.87 | 21.43 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.06 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.28 | 27.77 | 45.10 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.42 | 21.96 | 36.21 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.65 | 15.65 | 25.21 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.12 | 14.70 | 23.04 | 7.00 | 80.8 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.75 | 10.98 | 17.96 | 1.00 | 81.1 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 3
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.31
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.91 | 10.72 | 17.43 | 2.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.39 | 0.91 | 1.48 | 0.00 | 10.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.25 | 12.72 | 19.70 | 6.00 | 83.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.47 | 11.62 | 19.19 | 2.00 | 70.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.86 | 11.25 | 18.11 | 7.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.16 | 6.20 | 9.99 | 0.00 | 75.5 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 5.73 | 8.86 | 1.00 | 68.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.48 | 19.95 | 31.89 | 16.00 | 78.3 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.48 | 11.07 | 17.49 | 9.00 | 65.7 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.23 | 26.08 | 42.69 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.37 | 21.61 | 35.58 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.39 | 16.17 | 26.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.44 | 16.01 | 25.14 | 9.00 | 86.1 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.19 | 9.69 | 15.87 | 2.00 | 75.4 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 3 -> 3
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.32
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.38) beats the best remaining Bench Boost opportunity (3.66).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.38) beats the best remaining Bench Boost opportunity (3.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.30 | 11.47 | 18.21 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.78 | 1.38 | 0.00 | 9.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.15 | 12.51 | 20.95 | 11.00 | 79.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.52 | 12.03 | 19.46 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.32 | 17.89 | 4.00 | 79.5 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.75 | 9.12 | 0.00 | 72.5 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.24 | 3.78 | 6.52 | 0.00 | 44.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.82 | 21.46 | 34.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.41 | 16.93 | 26.40 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.03 | 26.38 | 43.08 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.29 | 21.18 | 34.75 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.01 | 15.16 | 25.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.82 | 14.91 | 23.33 | 2.00 | 74.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.73 | 8.37 | 13.89 | 0.00 | 61.9 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 3 -> 4
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.42
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.86 | 9.06 | 14.82 | 1.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.33 | 0.75 | 1.32 | 0.00 | 7.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.91 | 16.34 | 25.72 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.62 | 11.91 | 18.85 | 2.00 | 77.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.19 | 11.40 | 18.61 | 2.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.55 | 2.70 | 4.70 | 6.00 | 40.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.84 | 2.57 | 4.85 | 1.00 | 33.6 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.83 | 20.94 | 33.81 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.39 | 13.64 | 21.69 | 2.00 | 77.4 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.33 | 25.77 | 41.78 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.89 | 18.64 | 31.47 | 2.00 | 84.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.28 | 15.92 | 26.41 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.51 | 14.77 | 23.69 | 5.00 | 79.2 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 0.96 | 4.22 | 8.02 | 2.00 | 26.5 | 90.0 |
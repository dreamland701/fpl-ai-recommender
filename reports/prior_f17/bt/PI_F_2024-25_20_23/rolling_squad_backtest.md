# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 282.82
- Total actual points: 256.00
- Average predicted points: 70.70
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
- Predicted score: 73.23
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.75 | 10.76 | 17.44 | 3.00 | 87.3 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.27 | 0.81 | 1.23 | 0.00 | 9.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.38 | 14.58 | 23.15 | 0.00 | 87.8 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.71 | 12.97 | 20.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.54 | 12.54 | 19.92 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.94 | 6.16 | 9.70 | 1.00 | 75.2 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.87 | 5.21 | 7.97 | 1.00 | 59.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.69 | 21.35 | 34.07 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.83 | 13.86 | 21.41 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.02 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.21 | 27.59 | 44.81 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.46 | 22.08 | 36.42 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.58 | 15.46 | 24.90 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.15 | 14.78 | 23.17 | 7.00 | 80.9 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.73 | 10.94 | 17.89 | 1.00 | 81.2 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.10
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.92 | 10.71 | 17.38 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.30 | 0.84 | 1.23 | 0.00 | 10.3 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.26 | 12.76 | 19.77 | 6.00 | 83.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.42 | 11.51 | 19.03 | 2.00 | 70.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.86 | 11.21 | 18.02 | 7.00 | 81.8 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.19 | 6.32 | 10.23 | 0.00 | 76.2 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 5.75 | 8.90 | 1.00 | 68.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.42 | 19.80 | 31.68 | 16.00 | 78.7 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.49 | 11.09 | 17.52 | 9.00 | 65.5 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.17 | 25.90 | 42.42 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.41 | 21.72 | 35.78 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.47 | 16.09 | 25.26 | 9.00 | 86.2 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.33 | 16.02 | 25.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.18 | 9.65 | 15.81 | 2.00 | 75.4 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.34
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.60) beats the best remaining Bench Boost opportunity (3.91).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.24, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.60) beats the best remaining Bench Boost opportunity (3.91).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.32 | 11.48 | 18.19 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.41 | 0.80 | 1.33 | 0.00 | 10.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.11 | 12.39 | 20.77 | 11.00 | 79.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.51 | 11.97 | 19.35 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.83 | 11.35 | 17.93 | 4.00 | 79.3 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.76 | 9.15 | 0.00 | 72.6 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.27 | 3.91 | 6.79 | 0.00 | 45.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.76 | 21.31 | 34.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.40 | 16.90 | 26.34 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.96 | 26.19 | 42.78 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.36 | 21.38 | 35.09 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.96 | 15.04 | 25.14 | 2.00 | 89.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.85 | 14.99 | 23.46 | 2.00 | 74.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.72 | 8.35 | 13.87 | 0.00 | 62.0 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.15
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.26) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.26) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.88 | 9.06 | 14.80 | 1.00 | 83.2 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.23 | 0.57 | 1.05 | 0.00 | 8.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.87 | 16.23 | 25.56 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.62 | 11.91 | 18.84 | 2.00 | 77.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.18 | 11.34 | 18.49 | 2.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.55 | 2.72 | 4.76 | 6.00 | 40.2 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.87 | 2.71 | 5.15 | 1.00 | 34.5 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.78 | 20.79 | 33.58 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.38 | 13.63 | 21.67 | 2.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.26 | 25.60 | 41.52 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.95 | 18.82 | 31.77 | 2.00 | 84.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.24 | 15.81 | 26.23 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.52 | 14.80 | 23.73 | 5.00 | 79.2 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 0.95 | 4.21 | 8.00 | 2.00 | 26.7 | 90.0 |
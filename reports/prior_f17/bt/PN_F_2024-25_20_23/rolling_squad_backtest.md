# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.64
- Total actual points: 256.00
- Average predicted points: 70.91
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
- Predicted score: 73.54
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.78 | 17.50 | 3.00 | 87.8 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.34 | 1.08 | 1.69 | 0.00 | 11.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.42 | 14.72 | 23.38 | 0.00 | 88.1 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.71 | 12.99 | 20.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.57 | 12.68 | 20.18 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.85 | 5.84 | 9.14 | 1.00 | 73.4 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.81 | 5.00 | 7.61 | 1.00 | 58.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.76 | 21.61 | 34.50 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.86 | 13.97 | 21.60 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.24 | 27.69 | 44.98 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.41 | 22.00 | 36.30 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.68 | 15.74 | 25.36 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.12 | 14.69 | 23.02 | 7.00 | 81.1 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.77 | 11.04 | 18.04 | 1.00 | 81.6 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.36
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.91 | 10.73 | 17.46 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.38 | 1.11 | 1.72 | 0.00 | 11.9 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.26 | 12.74 | 19.73 | 6.00 | 84.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.46 | 11.62 | 19.20 | 2.00 | 70.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.89 | 11.33 | 18.25 | 7.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.10 | 6.00 | 9.66 | 0.00 | 74.3 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.02 | 5.53 | 8.53 | 1.00 | 67.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.50 | 20.07 | 32.12 | 16.00 | 78.9 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.51 | 11.13 | 17.56 | 9.00 | 66.3 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.21 | 26.03 | 42.64 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.36 | 21.61 | 35.62 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.40 | 16.21 | 26.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.43 | 15.98 | 25.08 | 9.00 | 86.2 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.20 | 9.74 | 15.94 | 2.00 | 75.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.39
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.53) beats the best remaining Bench Boost opportunity (3.83).
- Transfer: David Raya Martin -> Matz Sels (projected gain 0.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.53) beats the best remaining Bench Boost opportunity (3.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.22 | 11.16 | 17.68 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.49 | 1.09 | 1.83 | 0.00 | 11.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.14 | 12.50 | 20.96 | 11.00 | 79.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.55 | 12.12 | 19.61 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.84 | 11.34 | 17.91 | 4.00 | 80.1 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.85 | 5.55 | 8.80 | 0.00 | 71.4 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.18 | 3.59 | 6.21 | 0.00 | 43.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.83 | 21.53 | 34.40 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.43 | 17.03 | 26.59 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.01 | 26.36 | 43.09 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.27 | 21.16 | 34.76 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.01 | 15.18 | 25.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.82 | 14.88 | 23.27 | 2.00 | 75.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.74 | 8.41 | 13.96 | 0.00 | 62.2 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.35
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.30) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.30) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.78 | 8.76 | 14.30 | 1.00 | 81.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.32 | 0.86 | 1.55 | 0.00 | 10.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.90 | 16.33 | 25.73 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.63 | 11.93 | 18.86 | 2.00 | 78.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.21 | 11.49 | 18.77 | 2.00 | 84.7 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.49 | 2.53 | 4.43 | 6.00 | 39.1 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.78 | 2.39 | 4.57 | 1.00 | 32.7 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.84 | 21.00 | 33.93 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.42 | 13.75 | 21.87 | 2.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.30 | 25.75 | 41.81 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.87 | 18.64 | 31.50 | 2.00 | 84.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.29 | 15.98 | 26.51 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.51 | 14.78 | 23.71 | 5.00 | 79.4 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 0.98 | 4.28 | 8.12 | 2.00 | 26.9 | 90.0 |
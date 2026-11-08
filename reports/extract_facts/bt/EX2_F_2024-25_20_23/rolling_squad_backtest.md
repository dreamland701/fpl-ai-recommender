# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 287.86
- Total actual points: 256.00
- Average predicted points: 71.96
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
- Predicted score: 73.67
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 10.88 | 17.57 | 3.00 | 88.9 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.14 | 0.66 | 1.09 | 0.00 | 5.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.42 | 14.69 | 23.25 | 0.00 | 88.0 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.72 | 12.97 | 20.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.57 | 12.60 | 19.95 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.96 | 6.12 | 9.52 | 1.00 | 75.9 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.91 | 5.25 | 7.96 | 1.00 | 60.2 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.74 | 21.44 | 34.00 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.80 | 13.78 | 21.21 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.27 | 27.74 | 44.88 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.46 | 22.03 | 36.16 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.68 | 15.68 | 25.15 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.13 | 14.69 | 22.93 | 7.00 | 81.1 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.81 | 11.08 | 18.01 | 1.00 | 82.5 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.12
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.89 | 10.71 | 17.50 | 2.00 | 85.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.33 | 0.92 | 1.45 | 0.00 | 11.5 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.75 | 13.83 | 22.10 | 6.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.45 | 11.59 | 19.23 | 2.00 | 69.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.83 | 11.19 | 18.10 | 7.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.12 | 6.15 | 10.01 | 0.00 | 74.5 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.00 | 5.60 | 8.82 | 1.00 | 66.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.03 | 19.32 | 31.90 | 16.00 | 72.1 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.45 | 11.01 | 17.44 | 9.00 | 64.7 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.12 | 0.00 | 0.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.71 | 27.17 | 45.00 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.89 | 22.79 | 38.04 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.92 | 17.08 | 27.42 | 9.00 | 90.0 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.33 | 16.06 | 26.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.17 | 9.67 | 15.93 | 2.00 | 74.5 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 73.58
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.33) beats the best remaining Bench Boost opportunity (3.58).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.33) beats the best remaining Bench Boost opportunity (3.58).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.32 | 11.49 | 18.17 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.28 | 0.65 | 1.18 | 0.00 | 5.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.23 | 12.64 | 21.03 | 11.00 | 81.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.55 | 12.08 | 19.45 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.85 | 11.36 | 17.85 | 4.00 | 80.5 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.95 | 5.80 | 9.15 | 0.00 | 73.5 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.10 | 3.56 | 6.25 | 0.00 | 39.0 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.35 | 22.77 | 36.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.89 | 18.13 | 28.73 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.55 | 27.67 | 45.48 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 6.87 | 21.07 | 35.93 | 2.00 | 89.9 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.37 | 16.24 | 25.80 | 2.00 | 84.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.07 | 15.23 | 25.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.63 | 8.69 | 14.73 | 0.00 | 58.5 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.49
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.32) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.32) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 2.91 | 9.14 | 14.86 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.10 | 0.42 | 0.90 | 0.00 | 4.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.90 | 16.30 | 25.57 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.64 | 11.94 | 18.79 | 2.00 | 78.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.25 | 11.50 | 18.66 | 2.00 | 85.6 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.39 | 2.47 | 4.44 | 6.00 | 34.5 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.72 | 2.39 | 4.62 | 1.00 | 29.1 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.84 | 20.96 | 33.66 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.42 | 13.68 | 21.61 | 2.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.32 | 25.77 | 41.63 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.78 | 18.96 | 32.26 | 2.00 | 80.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.29 | 15.93 | 26.32 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.56 | 14.85 | 23.65 | 5.00 | 80.3 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 0.93 | 4.66 | 8.96 | 2.00 | 25.1 | 90.0 |
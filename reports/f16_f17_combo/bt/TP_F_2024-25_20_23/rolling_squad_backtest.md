# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 283.40
- Total actual points: 256.00
- Average predicted points: 70.85
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
- Predicted score: 74.05
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.86 | 10.92 | 17.57 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.13 | 0.52 | 0.82 | 0.00 | 4.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.46 | 14.64 | 23.12 | 0.00 | 88.8 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.75 | 13.07 | 20.72 | 1.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.60 | 12.40 | 19.55 | 2.00 | 87.1 | 90.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.82 | 5.69 | 8.82 | 1.00 | 72.5 | 81.0 |
| Bench 2 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.83 | 5.00 | 7.54 | 1.00 | 58.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.87 | 21.83 | 34.77 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.89 | 13.91 | 21.39 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.20 | 27.30 | 44.15 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.46 | 21.93 | 36.04 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.69 | 15.55 | 24.89 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.23 | 14.85 | 23.15 | 7.00 | 84.1 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.85 | 11.11 | 18.02 | 1.00 | 84.0 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.60
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.93 | 10.71 | 17.47 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.32 | 0.78 | 1.17 | 0.00 | 10.5 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.06 | 12.04 | 18.63 | 6.00 | 77.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.96 | 11.59 | 18.77 | 7.00 | 85.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.41 | 11.41 | 18.92 | 2.00 | 68.8 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.96 | 5.64 | 9.17 | 0.00 | 70.3 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.89 | 5.27 | 8.28 | 1.00 | 63.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.51 | 20.19 | 32.45 | 16.00 | 79.7 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.45 | 10.91 | 17.25 | 9.00 | 64.9 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.08 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.07 | 25.60 | 42.04 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.26 | 21.27 | 35.11 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.41 | 15.96 | 25.15 | 9.00 | 85.9 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.29 | 15.80 | 25.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.19 | 9.66 | 15.88 | 2.00 | 75.4 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.08
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.07) beats the best remaining Bench Boost opportunity (3.30).
- Transfer: David Raya Martin -> Matz Sels (projected gain 1.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.07) beats the best remaining Bench Boost opportunity (3.30).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 4.41 | 11.68 | 18.50 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.28 | 0.53 | 0.93 | 0.00 | 4.8 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.70 | 12.48 | 20.15 | 8.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.18 | 12.40 | 20.63 | 11.00 | 80.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.76 | 10.85 | 16.91 | 4.00 | 77.4 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.83 | 5.44 | 8.54 | 0.00 | 70.8 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 0.96 | 3.13 | 5.53 | 0.00 | 35.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.89 | 21.59 | 34.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.44 | 16.91 | 26.28 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.99 | 26.16 | 42.66 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.07 | 21.06 | 34.93 | 2.00 | 90.0 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.93 | 15.06 | 23.46 | 2.00 | 78.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.01 | 14.92 | 24.79 | 2.00 | 89.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 2.63 | 8.65 | 14.73 | 0.00 | 59.1 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 75.67
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.0 | 3.00 | 9.34 | 15.22 | 1.00 | 87.3 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.11 | 0.32 | 0.67 | 0.00 | 3.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.90 | 16.15 | 25.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.40 | 11.90 | 19.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.55 | 11.41 | 17.81 | 2.00 | 75.1 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.28 | 2.19 | 3.97 | 6.00 | 32.2 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.61 | 2.06 | 4.07 | 1.00 | 26.5 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.88 | 20.96 | 33.76 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.48 | 13.72 | 21.68 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.29 | 25.58 | 41.44 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.70 | 18.65 | 31.84 | 2.00 | 79.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.30 | 15.78 | 26.05 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.64 | 14.96 | 23.88 | 5.00 | 82.8 | 87.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.9 | 0.96 | 4.72 | 9.13 | 2.00 | 26.4 | 90.0 |
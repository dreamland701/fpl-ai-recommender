# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 287.94
- Total actual points: 271.00
- Average predicted points: 71.98
- Average actual points: 67.75
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
- Predicted score: 73.04
- Actual score: 86.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 3.78 | 11.21 | 17.84 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.02 | 0.43 | 0.73 | 0.00 | 8.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.45 | 14.70 | 23.28 | 0.00 | 89.0 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.75 | 12.96 | 20.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.48 | 12.43 | 19.78 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.80 | 5.73 | 8.95 | 1.00 | 73.2 | 81.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.80 | 5.03 | 7.68 | 1.00 | 58.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 8.09 | 22.50 | 35.93 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 5.15 | 14.81 | 22.96 | 8.00 | 90.0 | 87.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.80 | 11.64 | 19.07 | 9.00 | 81.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.85 | 26.64 | 43.29 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.28 | 21.63 | 35.71 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.48 | 15.22 | 24.55 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.08 | 14.65 | 22.99 | 7.00 | 79.0 | 77.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.63 | 7.34 | 11.62 | 2.00 | 67.3 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.45
- Actual score: 69.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 3.22 | 10.26 | 16.73 | 3.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.32 | 0.71 | 1.15 | 0.00 | 8.4 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.26 | 12.77 | 19.81 | 6.00 | 83.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.45 | 11.55 | 19.06 | 2.00 | 70.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.81 | 11.12 | 17.92 | 7.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.02 | 5.85 | 9.42 | 0.00 | 73.5 | 0.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.96 | 5.42 | 8.39 | 1.00 | 66.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.80 | 20.90 | 33.43 | 16.00 | 81.3 | 77.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 4.51 | 12.53 | 20.35 | 1.00 | 86.1 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.80 | 11.98 | 18.96 | 9.00 | 69.0 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.88 | 25.16 | 41.25 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.24 | 21.29 | 35.11 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.38 | 15.93 | 25.03 | 9.00 | 84.0 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.22 | 15.75 | 25.47 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.40 | 6.96 | 11.35 | 5.00 | 69.2 | 62.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 73.33
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.35) beats the best remaining Bench Boost opportunity (4.76).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.35) beats the best remaining Bench Boost opportunity (4.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 4.67 | 12.52 | 19.91 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.15 | 0.59 | 1.07 | 0.00 | 7.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.09 | 12.36 | 20.72 | 11.00 | 78.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.49 | 11.99 | 19.42 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.29 | 17.84 | 4.00 | 79.7 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.77 | 5.37 | 8.54 | 0.00 | 70.9 | 0.0 |
| Bench 4 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.17 | 3.56 | 6.18 | 0.00 | 43.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 7.05 | 22.15 | 35.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.66 | 17.68 | 27.61 | 12.00 | 90.0 | 82.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.80 | 10.88 | 17.98 | 2.00 | 70.9 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.79 | 25.59 | 41.75 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.21 | 20.85 | 34.17 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.91 | 14.93 | 25.01 | 2.00 | 88.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.72 | 14.65 | 22.93 | 2.00 | 73.4 | 90.0 |
| Bench 3 | Bench Boost | Tyler Dibling | MID | 17 | 4.5 | 1.26 | 4.81 | 8.08 | 0.00 | 48.3 | 0.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 78.10
- Actual score: 64.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.21) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.21) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 3.21 | 10.07 | 16.45 | 1.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.26 | 0.56 | 1.01 | 0.00 | 6.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.88 | 16.27 | 25.64 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.59 | 11.84 | 18.74 | 2.00 | 77.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.15 | 11.30 | 18.47 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.77 | 2.37 | 4.55 | 1.00 | 32.6 | 3.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.41 | 2.31 | 4.10 | 6.00 | 38.8 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 8.05 | 21.61 | 34.90 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.64 | 14.39 | 22.90 | 2.00 | 80.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.72 | 10.68 | 17.49 | 1.00 | 76.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.21 | 25.37 | 41.11 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.79 | 18.29 | 30.85 | 2.00 | 85.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.13 | 15.57 | 25.87 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.33 | 14.30 | 22.96 | 5.00 | 77.0 | 87.0 |
| Bench 3 | Bench | Tyler Dibling | MID | 17 | 4.5 | 0.55 | 2.82 | 5.40 | 0.00 | 24.6 | 0.0 |
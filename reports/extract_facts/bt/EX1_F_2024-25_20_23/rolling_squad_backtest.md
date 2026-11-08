# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 292.63
- Total actual points: 263.00
- Average predicted points: 73.16
- Average actual points: 65.75
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
- Predicted score: 73.37
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.76 | 10.82 | 17.53 | 3.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.09 | 0.63 | 1.06 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.41 | 14.68 | 23.26 | 0.00 | 87.6 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.69 | 12.93 | 20.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.54 | 12.56 | 19.94 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.92 | 6.05 | 9.48 | 1.00 | 74.6 | 81.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.86 | 5.18 | 7.90 | 1.00 | 58.8 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.71 | 21.44 | 34.05 | 7.00 | 89.2 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.77 | 13.74 | 21.20 | 8.00 | 89.2 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.09 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.26 | 27.77 | 44.96 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.43 | 22.00 | 36.16 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.65 | 15.64 | 25.15 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 5.10 | 14.68 | 22.95 | 7.00 | 80.5 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.77 | 11.03 | 18.00 | 1.00 | 81.5 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.93
- Actual score: 68.00
- Transfer: David Raya Martin -> Jordan Pickford (projected gain 0.04, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.84 | 10.83 | 17.85 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.39 | 0.91 | 1.47 | 0.00 | 10.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.84 | 13.99 | 22.16 | 6.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.50 | 11.68 | 19.24 | 2.00 | 70.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.88 | 11.29 | 18.12 | 7.00 | 82.3 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.17 | 6.22 | 10.01 | 0.00 | 75.7 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.07 | 5.72 | 8.85 | 1.00 | 68.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.04 | 19.47 | 32.16 | 16.00 | 72.3 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.50 | 11.10 | 17.47 | 9.00 | 65.8 | 89.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.01 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.84 | 27.38 | 45.13 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 8.00 | 22.97 | 38.13 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 6.02 | 17.25 | 27.51 | 9.00 | 90.0 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.40 | 16.18 | 26.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.22 | 9.76 | 15.94 | 2.00 | 76.0 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 74.60
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.39) beats the best remaining Bench Boost opportunity (3.67).
- Transfer: Enzo Fernández -> Amad Diallo (projected gain 5.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.39) beats the best remaining Bench Boost opportunity (3.67).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.27 | 8.96 | 14.67 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.77 | 1.36 | 0.00 | 8.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.19 | 12.59 | 21.01 | 11.00 | 80.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.52 | 12.04 | 19.44 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 11.31 | 17.84 | 4.00 | 79.4 | 65.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.76 | 9.13 | 0.00 | 72.5 | 0.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.26 | 3.81 | 6.55 | 0.00 | 44.6 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.35 | 22.80 | 36.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.89 | 18.16 | 28.78 | 12.00 | 90.0 | 82.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.58 | 27.73 | 45.56 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 6.98 | 20.93 | 35.45 | 2.00 | 90.0 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.36 | 16.25 | 25.85 | 2.00 | 84.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.03 | 15.19 | 25.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.63 | 13.83 | 21.87 | 2.00 | 90.0 | 90.0 |

## GW23

- Train rows: 148648
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 78.73
- Actual score: 70.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 2.98 | 8.90 | 14.72 | 5.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.32 | 0.74 | 1.30 | 0.00 | 7.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.89 | 16.29 | 25.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.60 | 11.88 | 18.77 | 2.00 | 77.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.21 | 11.44 | 18.64 | 2.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.55 | 2.72 | 4.73 | 6.00 | 40.2 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.85 | 2.58 | 4.87 | 1.00 | 33.8 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.82 | 20.95 | 33.70 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.37 | 13.62 | 21.60 | 2.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.33 | 25.79 | 41.68 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.93 | 18.74 | 31.54 | 2.00 | 85.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.27 | 15.89 | 26.32 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.51 | 14.80 | 23.65 | 5.00 | 79.2 | 87.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.18 | 12.38 | 20.21 | 3.00 | 82.4 | 90.0 |
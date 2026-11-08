# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 288.96
- Total actual points: 291.00
- Average predicted points: 72.24
- Average actual points: 72.75
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
- Predicted score: 73.40
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.79 | 10.86 | 17.53 | 3.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.21 | 0.82 | 1.23 | 0.00 | 13.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.40 | 14.63 | 23.17 | 0.00 | 87.7 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.71 | 12.93 | 20.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.56 | 12.57 | 19.91 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.50 | 7.03 | 11.34 | -1.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.95 | 6.09 | 9.47 | 1.00 | 75.7 | 81.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.75 | 21.46 | 34.10 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.80 | 13.76 | 21.21 | 8.00 | 89.8 | 87.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 4.23 | 11.81 | 19.21 | 9.00 | 79.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.27 | 27.73 | 44.89 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.45 | 22.02 | 36.14 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.67 | 15.67 | 25.14 | 19.00 | 90.0 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 6.5 | 4.49 | 13.32 | 21.99 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.64 | 7.43 | 11.74 | 2.00 | 67.1 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.10
- Actual score: 79.00
- Transfer: Dejan Kulusevski -> Amad Diallo (projected gain 1.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 10.69 | 17.45 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.41 | 0.94 | 1.59 | 0.00 | 11.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.14 | 12.53 | 19.55 | 6.00 | 81.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.42 | 11.56 | 19.17 | 2.00 | 69.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.81 | 11.17 | 18.07 | 7.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.11 | 6.20 | 10.14 | 1.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.11 | 6.12 | 9.96 | 0.00 | 74.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.06 | 18.99 | 31.88 | 16.00 | 72.9 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.45 | 11.02 | 17.46 | 9.00 | 64.6 | 89.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.92 | 10.90 | 17.82 | 1.00 | 79.5 | 77.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.11 | 25.89 | 42.45 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.28 | 21.47 | 35.43 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.32 | 16.05 | 25.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 4.59 | 11.98 | 19.50 | 20.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.40 | 6.97 | 11.45 | 5.00 | 68.9 | 62.0 |

## GW22

- Train rows: 147919
- Bank: 1.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 75.48
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.87) beats the best remaining Bench Boost opportunity (8.18).
- Transfer: Tyler Dibling -> Anthony Elanga (projected gain 2.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.87) beats the best remaining Bench Boost opportunity (8.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.37 | 16.99 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.34 | 0.95 | 1.53 | 0.00 | 12.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.21 | 12.62 | 20.99 | 11.00 | 81.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.54 | 12.05 | 19.41 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.85 | 11.35 | 17.86 | 4.00 | 80.4 | 65.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.03 | 6.28 | 10.22 | 1.00 | 82.1 | 90.0 |
| Bench 4 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.09 | 3.55 | 6.23 | 0.00 | 38.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.82 | 21.46 | 34.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.36 | 16.80 | 26.15 | 12.00 | 90.0 | 82.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.41 | 9.66 | 15.89 | 2.00 | 68.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.03 | 26.36 | 42.91 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.86 | 20.56 | 35.62 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.06 | 15.23 | 25.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 4.65 | 13.87 | 21.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.3 | 4.49 | 11.54 | 18.16 | 2.00 | 78.6 | 73.0 |

## GW23

- Train rows: 148648
- Bank: 0.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 77.99
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Elanga -> Justin Kluivert (projected gain 2.35, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.57 | 10.02 | 16.44 | 9.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.44 | 0.92 | 1.46 | 0.00 | 11.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.88 | 16.25 | 25.52 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.64 | 11.94 | 18.80 | 2.00 | 78.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.24 | 11.48 | 18.62 | 2.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.23 | 6.49 | 10.71 | 1.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.72 | 2.39 | 4.62 | 1.00 | 29.1 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.86 | 20.96 | 33.71 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.42 | 13.68 | 21.64 | 2.00 | 78.4 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.53 | 10.03 | 16.33 | 1.00 | 75.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.33 | 25.76 | 41.63 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.76 | 18.95 | 32.21 | 2.00 | 80.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.29 | 15.91 | 26.31 | 7.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.22 | 12.41 | 20.21 | 3.00 | 83.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.6 | 4.13 | 12.28 | 19.36 | 13.00 | 90.0 | 87.0 |
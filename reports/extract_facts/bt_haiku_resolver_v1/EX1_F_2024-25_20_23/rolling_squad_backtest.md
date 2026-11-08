# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 288.82
- Total actual points: 291.00
- Average predicted points: 72.21
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
- Predicted score: 72.93
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.75 | 10.79 | 17.48 | 3.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.09 | 0.63 | 1.06 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.39 | 14.62 | 23.18 | 0.00 | 87.3 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.67 | 12.89 | 20.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.52 | 12.53 | 19.91 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.45 | 6.97 | 11.31 | -1.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.90 | 6.03 | 9.43 | 1.00 | 74.4 | 81.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.73 | 21.47 | 34.15 | 7.00 | 89.4 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.77 | 13.72 | 21.19 | 8.00 | 89.0 | 87.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 4.15 | 11.73 | 19.05 | 9.00 | 78.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.27 | 27.76 | 44.97 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.43 | 22.00 | 36.15 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.64 | 15.63 | 25.13 | 19.00 | 90.0 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 6.5 | 4.35 | 13.03 | 21.77 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.56 | 7.32 | 11.66 | 2.00 | 64.7 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.84
- Actual score: 79.00
- Transfer: Dejan Kulusevski -> Amad Diallo (projected gain 1.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.93 | 10.76 | 17.46 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.39 | 0.91 | 1.48 | 0.00 | 10.0 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.21 | 12.64 | 19.57 | 6.00 | 83.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.47 | 11.65 | 19.18 | 2.00 | 70.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.87 | 11.26 | 18.09 | 7.00 | 82.2 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.17 | 6.29 | 10.15 | 1.00 | 78.8 | 90.0 |
| Bench 4 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.16 | 6.21 | 9.98 | 0.00 | 75.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.06 | 18.88 | 31.76 | 16.00 | 72.8 | 77.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.49 | 11.10 | 17.48 | 9.00 | 65.8 | 89.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.97 | 10.99 | 17.84 | 1.00 | 80.7 | 77.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.21 | 26.07 | 42.54 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.37 | 21.61 | 35.49 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.39 | 16.18 | 26.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 4.66 | 12.08 | 19.52 | 20.00 | 85.5 | 90.0 |
| Bench 2 | Bench | Tyler Dibling | MID | 17 | 4.5 | 2.43 | 7.01 | 11.41 | 5.00 | 69.4 | 62.0 |

## GW22

- Train rows: 147919
- Bank: 1.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 75.21
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.81) beats the best remaining Bench Boost opportunity (8.11).
- Transfer: Tyler Dibling -> Anthony Elanga (projected gain 2.10, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.81) beats the best remaining Bench Boost opportunity (8.11).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.65 | 10.30 | 16.94 | 1.00 | 86.8 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.22 | 0.77 | 1.37 | 0.00 | 9.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.17 | 12.56 | 20.95 | 11.00 | 79.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.51 | 12.01 | 19.40 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.81 | 11.29 | 17.83 | 4.00 | 79.3 | 65.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.00 | 6.21 | 10.18 | 1.00 | 81.0 | 90.0 |
| Bench 4 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.25 | 3.79 | 6.52 | 0.00 | 44.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.80 | 21.46 | 34.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 6.34 | 16.78 | 26.16 | 12.00 | 90.0 | 82.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.34 | 9.57 | 15.85 | 2.00 | 66.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.03 | 26.38 | 42.95 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.96 | 20.11 | 34.70 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.03 | 15.19 | 25.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 4.62 | 13.83 | 21.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.3 | 4.45 | 11.47 | 18.13 | 2.00 | 77.4 | 73.0 |

## GW23

- Train rows: 148648
- Bank: 0.30 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 77.84
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Elanga -> Justin Kluivert (projected gain 2.36, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.52 | 9.95 | 16.39 | 9.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.33 | 0.75 | 1.31 | 0.00 | 7.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.87 | 16.24 | 25.53 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.60 | 11.87 | 18.76 | 2.00 | 77.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.19 | 11.42 | 18.59 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.19 | 6.43 | 10.68 | 1.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.84 | 2.58 | 4.87 | 1.00 | 33.8 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.84 | 20.97 | 33.74 | 13.00 | 90.0 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.38 | 13.62 | 21.61 | 2.00 | 77.1 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.48 | 9.96 | 16.30 | 1.00 | 73.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.33 | 25.78 | 41.68 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.92 | 18.72 | 31.47 | 2.00 | 85.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.26 | 15.88 | 26.31 | 7.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.18 | 12.37 | 20.22 | 3.00 | 82.4 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.6 | 4.09 | 12.22 | 19.33 | 13.00 | 90.0 | 87.0 |
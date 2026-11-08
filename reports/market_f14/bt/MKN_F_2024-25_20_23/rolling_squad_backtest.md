# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 284.56
- Total actual points: 250.00
- Average predicted points: 71.14
- Average actual points: 62.50
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
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 69.06
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.76 | 10.80 | 17.44 | 3.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.09 | 0.31 | 0.36 | 0.00 | 8.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.50 | 14.52 | 23.03 | 0.00 | 92.0 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 5.06 | 13.04 | 20.54 | 1.00 | 99.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.04 | 12.21 | 19.90 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.71 | 5.86 | 9.32 | 1.00 | 72.5 | 81.0 |
| Bench 2 | Bench | James Bree | DEF | 17 | 3.9 | 1.84 | 5.06 | 7.95 | 1.00 | 52.7 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.52 | 19.77 | 32.13 | 7.00 | 74.4 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.97 | 13.72 | 21.31 | 8.00 | 94.5 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.23 | 0.64 | 1.13 | 0.00 | 6.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.49 | 26.19 | 42.61 | 7.00 | 101.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.64 | 21.28 | 35.42 | 10.00 | 97.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.28 | 15.11 | 24.54 | 19.00 | 95.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.55 | 13.91 | 22.16 | 7.00 | 76.7 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.76 | 11.01 | 18.01 | 1.00 | 80.9 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 66.60
- Actual score: 61.00
- Transfer: Chris Wood -> Raúl Jiménez (projected gain 1.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.13 | 11.12 | 18.00 | 2.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.13 | 0.23 | 0.44 | 0.00 | 6.2 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.65 | 12.87 | 19.86 | 6.00 | 89.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.98 | 12.09 | 19.72 | 2.00 | 76.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.67 | 11.09 | 17.96 | 7.00 | 78.9 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.24 | 6.31 | 10.17 | 0.00 | 76.0 | 0.0 |
| Bench 3 | Bench | James Bree | DEF | 17 | 3.9 | 1.28 | 4.27 | 6.91 | 1.00 | 43.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.87 | 19.45 | 30.61 | 16.00 | 77.9 | 77.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.02 | 11.70 | 17.84 | 1.00 | 67.4 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.29 | 0.73 | 1.10 | 0.00 | 10.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.93 | 26.02 | 41.98 | 2.00 | 113.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.43 | 21.66 | 35.52 | 10.00 | 114.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.75 | 15.73 | 24.56 | 9.00 | 89.8 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.39 | 15.24 | 25.20 | 2.00 | 88.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.85 | 10.41 | 16.68 | 2.00 | 83.5 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 1.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.71
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (2.99) beats the best remaining Bench Boost opportunity (3.44).
- Transfer: Enzo Fernández -> Amad Diallo (projected gain 4.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (2.99) beats the best remaining Bench Boost opportunity (3.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.89 | 10.61 | 17.33 | 1.00 | 90.2 | 90.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.15 | 0.19 | 0.36 | 0.00 | 6.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.37 | 12.71 | 21.24 | 11.00 | 85.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.43 | 11.92 | 19.27 | 8.00 | 90.2 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.88 | 11.22 | 17.79 | 4.00 | 83.1 | 65.0 |
| Bench 2 | Bench Boost | James Bree | DEF | 17 | 3.9 | 1.60 | 5.23 | 8.29 | 1.00 | 58.7 | 85.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.05 | 3.41 | 6.02 | 0.00 | 41.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.96 | 21.02 | 33.33 | 2.00 | 94.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.94 | 10.11 | 16.23 | 2.00 | 55.8 | 70.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.18 | 0.71 | 1.19 | 0.00 | 7.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.92 | 25.31 | 41.08 | 3.00 | 101.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.63 | 22.23 | 36.28 | 2.00 | 108.8 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.99 | 14.64 | 22.80 | 2.00 | 77.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 3.86 | 14.16 | 24.37 | 2.00 | 78.2 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.94 | 14.16 | 22.42 | 2.00 | 96.0 | 90.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 79.18
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.91) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Raúl Jiménez -> Yoane Wissa (projected gain 3.06, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.91) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 10.30 | 16.75 | 9.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.13 | 0.17 | 0.35 | 0.00 | 6.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 6.85 | 17.08 | 26.63 | 5.00 | 113.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.35 | 11.53 | 18.41 | 2.00 | 76.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.80 | 11.01 | 18.11 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Bench | James Bree | DEF | 17 | 3.9 | 1.52 | 4.90 | 7.75 | 4.00 | 60.0 | 87.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.74 | 2.30 | 4.45 | 1.00 | 31.6 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.00 | 19.87 | 32.31 | 13.00 | 88.6 | 78.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 4.03 | 11.83 | 19.24 | 2.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.11 | 0.42 | 0.74 | 0.00 | 5.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.91 | 24.81 | 39.39 | 8.00 | 106.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.78 | 19.54 | 33.13 | 2.00 | 91.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.97 | 15.58 | 26.12 | 7.00 | 96.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.11 | 14.19 | 22.85 | 5.00 | 73.6 | 87.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 3.78 | 12.07 | 20.03 | 3.00 | 74.6 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 280.41
- Total actual points: 250.00
- Average predicted points: 70.10
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
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 70.86
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 10.80 | 17.44 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.00 | 0.31 | 0.36 | 0.00 | 4.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.35 | 14.52 | 23.03 | 0.00 | 87.9 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.81 | 13.04 | 20.54 | 1.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.21 | 12.21 | 19.90 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.80 | 5.86 | 9.32 | 1.00 | 74.9 | 81.0 |
| Bench 2 | Bench | James Bree | DEF | 17 | 3.9 | 1.88 | 5.06 | 7.95 | 1.00 | 53.7 | 45.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.15 | 19.77 | 32.13 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.82 | 13.72 | 21.31 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.21 | 0.64 | 1.13 | 0.00 | 5.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.86 | 26.19 | 42.61 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.14 | 21.28 | 35.42 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.47 | 15.11 | 24.54 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.69 | 13.91 | 22.16 | 7.00 | 82.4 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.67 | 11.01 | 18.01 | 1.00 | 80.5 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.95
- Actual score: 61.00
- Transfer: Chris Wood -> Raúl Jiménez (projected gain 1.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.95 | 11.12 | 18.00 | 2.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.08 | 0.23 | 0.44 | 0.00 | 4.3 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.22 | 12.87 | 19.86 | 6.00 | 83.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.60 | 12.09 | 19.72 | 2.00 | 67.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.91 | 11.09 | 17.96 | 7.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.21 | 6.31 | 10.17 | 0.00 | 74.9 | 0.0 |
| Bench 3 | Bench | James Bree | DEF | 17 | 3.9 | 1.47 | 4.27 | 6.91 | 1.00 | 48.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.41 | 19.45 | 30.61 | 16.00 | 78.5 | 77.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.36 | 11.70 | 17.84 | 1.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.15 | 0.73 | 1.10 | 0.00 | 5.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.29 | 26.02 | 41.98 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.28 | 21.66 | 35.52 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.36 | 15.73 | 24.56 | 9.00 | 85.8 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.01 | 15.24 | 25.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.29 | 10.41 | 16.68 | 2.00 | 72.6 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 1.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.73
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.01) beats the best remaining Bench Boost opportunity (3.46).
- Transfer: Enzo Fernández -> Amad Diallo (projected gain 4.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.01) beats the best remaining Bench Boost opportunity (3.46).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.76 | 10.61 | 17.33 | 1.00 | 85.3 | 90.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.08 | 0.19 | 0.36 | 0.00 | 4.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.01 | 12.71 | 21.24 | 11.00 | 77.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.56 | 11.92 | 19.27 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.67 | 11.22 | 17.79 | 4.00 | 80.0 | 65.0 |
| Bench 2 | Bench Boost | James Bree | DEF | 17 | 3.9 | 1.76 | 5.23 | 8.29 | 1.00 | 64.6 | 85.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.07 | 3.41 | 6.02 | 0.00 | 40.8 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.71 | 21.02 | 33.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.99 | 10.11 | 16.23 | 2.00 | 57.8 | 70.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.10 | 0.71 | 1.19 | 0.00 | 4.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.62 | 25.31 | 41.08 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.68 | 22.23 | 36.28 | 2.00 | 90.0 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.71 | 14.64 | 22.80 | 2.00 | 74.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.61 | 14.16 | 24.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.81 | 14.16 | 22.42 | 2.00 | 90.0 | 90.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 76.86
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.86) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Raúl Jiménez -> Yoane Wissa (projected gain 2.95, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.86) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.73 | 10.30 | 16.75 | 9.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.06 | 0.17 | 0.35 | 0.00 | 4.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.88 | 17.08 | 26.63 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.40 | 11.53 | 18.41 | 2.00 | 79.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.10 | 11.01 | 18.11 | 2.00 | 86.0 | 90.0 |
| Bench 2 | Bench | James Bree | DEF | 17 | 3.9 | 1.57 | 4.90 | 7.75 | 4.00 | 62.0 | 87.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.68 | 2.30 | 4.45 | 1.00 | 29.3 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.47 | 19.87 | 32.31 | 13.00 | 90.0 | 78.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.90 | 11.83 | 19.24 | 2.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.07 | 0.42 | 0.74 | 0.00 | 3.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.86 | 24.81 | 39.39 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.21 | 19.54 | 33.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.16 | 15.58 | 26.12 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.27 | 14.19 | 22.85 | 5.00 | 80.4 | 87.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.16 | 12.07 | 20.03 | 3.00 | 83.8 | 90.0 |
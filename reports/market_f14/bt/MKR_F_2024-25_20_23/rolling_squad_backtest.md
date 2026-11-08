# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 279.76
- Total actual points: 250.00
- Average predicted points: 69.94
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
- Predicted score: 70.55
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.85 | 10.79 | 17.42 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.01 | 0.29 | 0.32 | 0.00 | 4.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.31 | 14.53 | 23.06 | 0.00 | 87.8 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.81 | 13.04 | 20.54 | 1.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.20 | 12.22 | 19.91 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 1.87 | 5.85 | 9.27 | 1.00 | 75.0 | 81.0 |
| Bench 2 | Bench | James Bree | DEF | 17 | 3.9 | 1.92 | 5.05 | 7.92 | 1.00 | 53.7 | 45.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 7.13 | 19.78 | 32.15 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.83 | 13.72 | 21.30 | 8.00 | 90.0 | 87.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.24 | 0.63 | 1.11 | 0.00 | 5.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.77 | 26.21 | 42.67 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.14 | 21.28 | 35.42 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.36 | 15.14 | 24.61 | 19.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.67 | 13.91 | 22.17 | 7.00 | 82.4 | 77.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.1 | 3.70 | 11.00 | 17.99 | 1.00 | 80.5 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.10
- Actual score: 61.00
- Transfer: Chris Wood -> Raúl Jiménez (projected gain 1.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 11.13 | 18.04 | 2.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.12 | 0.22 | 0.42 | 0.00 | 4.4 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.25 | 12.86 | 19.84 | 6.00 | 83.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.67 | 12.08 | 19.67 | 2.00 | 67.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.88 | 11.09 | 17.98 | 7.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Conor Coady | DEF | 11 | 4.0 | 2.26 | 6.30 | 10.13 | 0.00 | 75.0 | 0.0 |
| Bench 3 | Bench | James Bree | DEF | 17 | 3.9 | 1.46 | 4.27 | 6.92 | 1.00 | 48.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.43 | 19.45 | 30.60 | 16.00 | 78.5 | 77.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.33 | 11.71 | 17.87 | 1.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.13 | 0.73 | 1.11 | 0.00 | 5.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.33 | 26.01 | 41.94 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.28 | 21.66 | 35.51 | 10.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.38 | 15.72 | 24.55 | 9.00 | 85.8 | 77.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.01 | 15.24 | 25.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.32 | 10.40 | 16.66 | 2.00 | 72.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 1.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.74
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (3.14) beats the best remaining Bench Boost opportunity (3.61).
- Transfer: Enzo Fernández -> Amad Diallo (projected gain 4.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (3.14) beats the best remaining Bench Boost opportunity (3.61).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.78 | 10.61 | 17.31 | 1.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Daniel Iversen | GK | 11 | 3.9 | 0.10 | 0.19 | 0.35 | 0.00 | 4.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.01 | 12.71 | 21.24 | 11.00 | 77.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.46 | 11.93 | 19.33 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.65 | 11.22 | 17.80 | 4.00 | 80.0 | 65.0 |
| Bench 2 | Bench Boost | James Bree | DEF | 17 | 3.9 | 1.81 | 5.22 | 8.25 | 1.00 | 64.7 | 85.0 |
| Bench 3 | Bench Boost | Conor Coady | DEF | 11 | 4.0 | 1.09 | 3.41 | 6.00 | 0.00 | 40.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.68 | 21.02 | 33.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.91 | 10.13 | 16.29 | 2.00 | 57.6 | 70.0 |
| Bench 4 | Bench Boost | Ross Stewart | FWD | 17 | 4.4 | 0.13 | 0.70 | 1.16 | 0.00 | 4.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.61 | 25.31 | 41.09 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.71 | 22.22 | 36.26 | 2.00 | 90.0 | 83.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 4.69 | 14.64 | 22.81 | 2.00 | 74.3 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.86 | 14.15 | 22.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.63 | 14.15 | 24.35 | 2.00 | 90.0 | 90.0 |

## GW23

- Train rows: 148648
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 76.38
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.85) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Raúl Jiménez -> Yoane Wissa (projected gain 2.95, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.85) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.79 | 10.29 | 16.71 | 9.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Daniel Iversen | GK | 11 | 3.9 | 0.03 | 0.18 | 0.36 | 0.00 | 4.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.88 | 17.08 | 26.63 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.29 | 11.55 | 18.48 | 2.00 | 79.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.04 | 11.02 | 18.14 | 2.00 | 85.9 | 90.0 |
| Bench 2 | Bench | James Bree | DEF | 17 | 3.9 | 1.62 | 4.89 | 7.72 | 4.00 | 62.0 | 87.0 |
| Bench 3 | Bench | Conor Coady | DEF | 11 | 4.0 | 0.66 | 2.30 | 4.46 | 1.00 | 29.3 | 3.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.35 | 19.89 | 32.38 | 13.00 | 90.0 | 78.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.3 | 3.86 | 11.83 | 19.26 | 2.00 | 81.1 | 90.0 |
| Bench 4 | Bench | Ross Stewart | FWD | 17 | 4.4 | 0.11 | 0.41 | 0.72 | 0.00 | 3.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.85 | 24.82 | 39.41 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.20 | 19.54 | 33.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.10 | 15.59 | 26.15 | 7.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.16 | 14.21 | 22.92 | 5.00 | 80.2 | 87.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.18 | 12.07 | 20.01 | 3.00 | 83.9 | 90.0 |
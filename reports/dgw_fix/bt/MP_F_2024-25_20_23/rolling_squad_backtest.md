# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 288.64
- Total actual points: 257.00
- Average predicted points: 72.16
- Average actual points: 64.25
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
- Predicted score: 73.05
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.72 | 10.88 | 17.80 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.00 | 0.15 | 0.32 | 0.00 | 4.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.42 | 14.54 | 27.77 | 0.00 | 87.9 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.69 | 12.77 | 20.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.62 | 12.56 | 20.22 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.45 | 6.86 | 11.18 | -1.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.83 | 4.87 | 7.50 | 1.00 | 58.0 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.86 | 21.22 | 34.23 | 7.00 | 90.0 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.89 | 13.46 | 21.00 | 8.00 | 90.0 | 87.0 |
| XI | XI | Cody Gakpo | FWD | 12 | 7.3 | 4.33 | 11.90 | 22.64 | 6.00 | 61.0 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.28 | 28.03 | 55.33 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.48 | 22.39 | 37.14 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.62 | 15.36 | 24.88 | 19.00 | 90.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.85 | 10.87 | 17.60 | 5.00 | 67.2 | 85.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.11 | 6.16 | 9.86 | 1.00 | 72.8 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.89
- Actual score: 55.00
- Transfer: Chris Wood -> Raúl Jiménez (projected gain 0.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.88 | 10.87 | 17.73 | 2.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.10 | 0.24 | 0.47 | 0.00 | 4.4 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.27 | 12.28 | 19.08 | 6.00 | 84.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.43 | 11.40 | 26.29 | 2.00 | 69.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.92 | 11.22 | 18.17 | 7.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.20 | 6.21 | 9.88 | 1.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 5.49 | 8.46 | 1.00 | 68.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.56 | 19.83 | 31.90 | 16.00 | 80.1 | 77.0 |
| XI | XI | Cody Gakpo | FWD | 12 | 7.3 | 3.68 | 11.77 | 26.02 | 2.00 | 70.7 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.43 | 11.51 | 17.66 | 1.00 | 73.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.21 | 26.29 | 60.47 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.42 | 22.05 | 36.51 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.35 | 15.75 | 25.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.53 | 10.59 | 16.87 | 3.00 | 69.9 | 77.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.25 | 6.23 | 10.03 | 2.00 | 73.7 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 1.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 73.95
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.14) beats the best remaining Bench Boost opportunity (8.56).
- Transfer: Boubakary Soumaré -> Amad Diallo (projected gain 3.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.14) beats the best remaining Bench Boost opportunity (8.56).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.61 | 10.42 | 17.12 | 1.00 | 86.2 | 90.0 |
| Bench 1 | Bench Boost | Cieran Slicker | GK | 10 | 3.9 | 0.00 | 0.04 | 0.22 | 0.00 | 4.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.11 | 16.56 | 29.13 | 11.00 | 78.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.53 | 12.14 | 19.56 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 10.95 | 17.22 | 4.00 | 79.6 | 65.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.05 | 6.27 | 9.99 | 1.00 | 82.2 | 90.0 |
| Bench 4 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.53 | 8.68 | 0.00 | 72.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.90 | 21.46 | 34.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cody Gakpo | FWD | 12 | 7.3 | 4.21 | 15.99 | 26.74 | 2.00 | 70.7 | 86.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.94 | 9.66 | 15.28 | 2.00 | 56.9 | 70.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.06 | 35.70 | 61.39 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.86 | 23.03 | 37.78 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.97 | 14.89 | 24.80 | 2.00 | 89.2 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.72 | 13.42 | 21.37 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Jacob Murphy | MID | 15 | 5.1 | 3.18 | 9.58 | 15.91 | 2.00 | 65.0 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 78.75
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.37) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: David Raya Martin -> Emiliano Martínez Romero (projected gain 1.70, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.37) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.25 | 11.85 | 17.46 | 2.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Cieran Slicker | GK | 10 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 3.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.93 | 27.13 | 35.84 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.63 | 11.72 | 18.56 | 2.00 | 78.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.22 | 11.59 | 18.93 | 2.00 | 84.7 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.24 | 6.56 | 10.74 | 1.00 | 83.8 | 90.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.37 | 2.14 | 3.61 | 6.00 | 36.1 | 90.0 |
| XI | XI | Cody Gakpo | FWD | 12 | 7.4 | 5.18 | 22.89 | 29.91 | 16.00 | 79.3 | 67.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.89 | 21.07 | 34.28 | 13.00 | 90.0 | 78.0 |
| Bench 2 | Bench | Raúl Jiménez | FWD | 9 | 5.7 | 3.37 | 8.86 | 14.45 | 2.00 | 50.7 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.37 | 43.70 | 59.67 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 6.45 | 20.47 | 34.42 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.32 | 15.82 | 26.05 | 7.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.16 | 11.96 | 19.39 | 3.00 | 82.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.62 | 9.00 | 15.27 | 6.00 | 61.7 | 90.0 |
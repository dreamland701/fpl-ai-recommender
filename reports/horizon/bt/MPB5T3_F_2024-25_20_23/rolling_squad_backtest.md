# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 287.81
- Total actual points: 264.00
- Average predicted points: 71.95
- Average actual points: 66.00
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
- Predicted score: 72.95
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.74 | 10.93 | 17.88 | 3.00 | 87.6 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.28 | 0.85 | 1.63 | 0.00 | 9.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.42 | 14.54 | 27.77 | 0.00 | 87.9 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.70 | 12.80 | 20.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.55 | 12.39 | 19.94 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.45 | 6.85 | 11.18 | -1.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.87 | 4.98 | 7.66 | 1.00 | 58.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.2 | 7.74 | 20.91 | 33.76 | 7.00 | 89.9 | 85.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.83 | 13.31 | 20.79 | 8.00 | 90.0 | 87.0 |
| XI | XI | Cody Gakpo | FWD | 12 | 7.3 | 4.43 | 12.17 | 23.12 | 6.00 | 63.4 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 10.28 | 28.00 | 55.22 | 7.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 7.42 | 22.24 | 36.90 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.65 | 15.44 | 25.01 | 19.00 | 90.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.91 | 11.03 | 17.86 | 5.00 | 68.5 | 85.0 |
| Bench 3 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.15 | 6.25 | 9.99 | 1.00 | 73.6 | 90.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.88
- Actual score: 55.00
- Transfer: Chris Wood -> Raúl Jiménez (projected gain 1.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.91 | 10.96 | 17.86 | 2.00 | 86.5 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.31 | 0.87 | 1.66 | 0.00 | 10.5 | 0.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.25 | 12.24 | 19.02 | 6.00 | 83.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.47 | 11.48 | 26.48 | 2.00 | 70.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.86 | 11.08 | 17.97 | 7.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.17 | 6.16 | 9.81 | 1.00 | 78.8 | 90.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 5.48 | 8.44 | 1.00 | 68.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.2 | 6.48 | 19.62 | 31.59 | 16.00 | 78.3 | 77.0 |
| XI | XI | Cody Gakpo | FWD | 12 | 7.3 | 3.77 | 12.00 | 26.56 | 2.00 | 72.8 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.36 | 11.33 | 17.38 | 1.00 | 71.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.23 | 26.33 | 60.56 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.37 | 21.92 | 36.29 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.39 | 15.87 | 25.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.55 | 10.64 | 16.98 | 3.00 | 70.4 | 77.0 |
| Bench 2 | Bench | Boubakary Soumaré | MID | 11 | 4.4 | 2.29 | 6.32 | 10.16 | 2.00 | 74.5 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 1.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 73.70
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.55) beats the best remaining Bench Boost opportunity (9.05).
- Transfer: Boubakary Soumaré -> Amad Diallo (projected gain 10.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.55) beats the best remaining Bench Boost opportunity (9.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.63 | 10.47 | 17.19 | 1.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.42 | 1.25 | 1.77 | 0.00 | 10.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.15 | 16.71 | 29.39 | 11.00 | 79.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.52 | 12.12 | 19.52 | 8.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.82 | 10.95 | 17.24 | 4.00 | 79.5 | 65.0 |
| Bench 3 | Bench Boost | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.00 | 6.16 | 9.82 | 1.00 | 81.1 | 90.0 |
| Bench 4 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.54 | 8.70 | 0.00 | 72.5 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.3 | 6.82 | 21.25 | 34.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cody Gakpo | FWD | 12 | 7.3 | 4.28 | 16.24 | 27.17 | 2.00 | 72.3 | 86.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 3.90 | 9.56 | 15.14 | 2.00 | 56.0 | 70.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.03 | 35.59 | 61.21 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.29 | 21.55 | 35.48 | 2.00 | 90.0 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.01 | 14.99 | 24.95 | 2.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.66 | 13.26 | 21.13 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Jacob Murphy | MID | 15 | 5.1 | 3.21 | 9.68 | 16.07 | 2.00 | 65.8 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 78.28
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.33) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.51 | 10.22 | 16.74 | 9.00 | 86.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.25 | 0.95 | 1.47 | 0.00 | 9.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 5.91 | 27.03 | 35.73 | 5.00 | 90.0 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 4.62 | 11.70 | 18.53 | 2.00 | 77.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.19 | 11.52 | 18.81 | 2.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Taylor Harwood-Bellis | DEF | 17 | 4.1 | 2.19 | 6.46 | 10.58 | 1.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 0.55 | 2.59 | 4.34 | 6.00 | 40.0 | 90.0 |
| XI | XI | Cody Gakpo | FWD | 12 | 7.4 | 5.23 | 23.09 | 30.19 | 16.00 | 80.3 | 67.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.3 | 7.83 | 20.91 | 34.02 | 13.00 | 90.0 | 78.0 |
| Bench 2 | Bench | Raúl Jiménez | FWD | 9 | 5.7 | 3.41 | 8.99 | 14.65 | 2.00 | 51.8 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.33 | 43.50 | 59.41 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 5.89 | 19.01 | 32.14 | 2.00 | 84.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.28 | 15.73 | 25.91 | 7.00 | 90.0 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.5 | 4.18 | 12.02 | 19.49 | 3.00 | 82.5 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.66 | 9.12 | 15.46 | 6.00 | 62.7 | 90.0 |
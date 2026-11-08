# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 245.51
- Total actual points: 224.00
- Average predicted points: 61.38
- Average actual points: 56.00
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
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.04
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.46 | 10.73 | 17.43 | 3.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 3.17 | 9.96 | 15.83 | 9.00 | 88.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.75 | 14.69 | 23.32 | 0.00 | 74.5 | 85.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 3.08 | 12.94 | 20.61 | 2.00 | 85.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.49 | 12.74 | 20.26 | 1.00 | 87.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.72 | 12.07 | 20.02 | 2.00 | 79.2 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 4.7 | 3.51 | 9.56 | 15.27 | 6.00 | 86.3 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 2.29 | 9.74 | 16.02 | 9.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.89 | 8.58 | 13.72 | 5.00 | 69.6 | 90.0 |
| XI | XI | Adam Armstrong | FWD | 17 | 5.1 | 3.13 | 7.36 | 12.05 | 1.00 | 70.0 | 35.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.20 | 27.83 | 45.19 | 7.00 | 82.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 4.80 | 22.12 | 36.44 | 10.00 | 87.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.17 | 15.58 | 25.09 | 19.00 | 85.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.4 | 4.55 | 14.65 | 22.97 | 7.00 | 82.8 | 77.0 |
| Bench 2 | Bench | Jacob Murphy | MID | 15 | 5.1 | 2.92 | 11.16 | 18.19 | 5.00 | 76.5 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.93
- Actual score: 48.00
- Transfer: João Pedro Junqueira de Jesus -> Raúl Jiménez (projected gain 1.34, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.50 | 10.65 | 17.32 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.9 | 2.46 | 9.02 | 14.75 | 3.00 | 88.4 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 3.64 | 12.76 | 19.77 | 6.00 | 84.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.54 | 11.53 | 19.05 | 2.00 | 71.1 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.3 | 3.52 | 11.45 | 18.89 | 2.00 | 80.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.90 | 11.36 | 18.29 | 7.00 | 85.6 | 90.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 2.39 | 8.93 | 14.59 | 2.00 | 87.1 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.64 | 12.22 | 18.38 | 1.00 | 79.9 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.97 | 8.52 | 13.80 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.05 | 6.38 | 10.94 | 1.00 | 58.9 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 6.66 | 26.06 | 42.65 | 2.00 | 85.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.56 | 21.74 | 35.79 | 10.00 | 86.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 6.00 | 16.06 | 25.94 | 2.00 | 86.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.30 | 16.01 | 25.13 | 9.00 | 75.4 | 77.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.58 | 10.97 | 17.59 | 3.00 | 77.0 | 77.0 |

## GW22

- Train rows: 147919
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 62.95
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (7.45).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (7.45).
- Autosub: Lewis Hall replaced William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 3.61 | 11.45 | 18.18 | 1.00 | 86.7 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.27 | 10.21 | 16.85 | 1.00 | 86.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.59 | 12.39 | 20.78 | 11.00 | 74.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.20 | 12.05 | 19.50 | 8.00 | 86.5 | 90.0 |
| Bench 2 | Autosub In | Lewis Hall | DEF | 15 | 4.9 | 3.52 | 11.31 | 17.87 | 4.00 | 84.9 | 65.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.3 | 3.60 | 11.07 | 18.34 | 0.00 | 85.8 | 0.0 |
| Bench 3 | Bench | Nikola Milenković | DEF | 16 | 4.7 | 3.46 | 9.98 | 15.96 | 1.00 | 86.5 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.17 | 10.19 | 16.33 | 2.00 | 74.1 | 70.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.86 | 9.44 | 14.87 | 2.00 | 76.1 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.40 | 5.27 | 9.21 | 1.00 | 50.4 | 57.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.6 | 5.61 | 26.47 | 43.21 | 3.00 | 85.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.4 | 6.71 | 22.54 | 36.84 | 2.00 | 83.3 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 4.72 | 15.07 | 25.20 | 2.00 | 84.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.48 | 14.86 | 23.25 | 2.00 | 78.7 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.97 | 9.84 | 16.40 | 2.00 | 71.6 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.58
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.87) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: William Saliba -> Ola Aina (projected gain 3.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.14 | 9.85 | 16.28 | 9.00 | 85.4 | 90.0 |
| XI | XI | Matz Sels | GK | 16 | 4.9 | 3.58 | 9.03 | 14.78 | 1.00 | 87.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.66 | 16.38 | 25.79 | 5.00 | 83.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.9 | 3.67 | 11.94 | 18.89 | 2.00 | 74.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 3.82 | 11.47 | 18.71 | 2.00 | 85.6 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 2.96 | 11.42 | 18.26 | 1.00 | 86.7 | 78.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 4.7 | 2.92 | 8.35 | 13.79 | 0.00 | 84.8 | 90.0 |
| Bench 3 | Bench Boost | Raúl Jiménez | FWD | 9 | 5.7 | 2.18 | 9.12 | 15.08 | 2.00 | 41.9 | 63.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.38 | 8.50 | 14.11 | 9.00 | 72.5 | 76.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.63 | 6.08 | 10.38 | 1.00 | 47.6 | 59.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.46 | 25.89 | 41.96 | 8.00 | 85.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 4.97 | 19.98 | 33.53 | 2.00 | 78.7 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.7 | 6.55 | 16.00 | 26.55 | 7.00 | 84.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.5 | 5.40 | 14.76 | 23.67 | 5.00 | 81.4 | 87.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.81 | 9.27 | 15.77 | 6.00 | 55.7 | 90.0 |
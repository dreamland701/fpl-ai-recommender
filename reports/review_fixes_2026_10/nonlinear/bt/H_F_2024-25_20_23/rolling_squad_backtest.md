# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 233.92
- Total actual points: 188.00
- Average predicted points: 58.48
- Average actual points: 47.00
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
- Vice captain: Alex Iwobi
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.45
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Adam Armstrong replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.46 | 10.55 | 17.83 | 4.00 | 88.7 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.46 | 10.49 | 17.11 | 3.00 | 85.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 4.75 | 15.60 | 22.71 | 0.00 | 74.5 | 85.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 4.22 | 13.26 | 20.51 | 2.00 | 81.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 3.75 | 11.54 | 19.66 | 1.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Dan Burn | DEF | 15 | 4.4 | 2.77 | 10.71 | 16.37 | 1.00 | 84.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.72 | 9.78 | 18.31 | 2.00 | 79.2 | 90.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 3.59 | 11.93 | 19.23 | 8.00 | 82.0 | 87.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 2.89 | 10.03 | 14.35 | 5.00 | 69.6 | 90.0 |
| Bench 2 | Autosub In | Adam Armstrong | FWD | 17 | 5.1 | 3.13 | 8.26 | 13.89 | 1.00 | 70.0 | 35.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.20 | 21.40 | 29.86 | 7.00 | 82.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.4 | 4.80 | 20.32 | 35.01 | 10.00 | 87.9 | 90.0 |
| XI | XI | Joelinton Cássio Apolinário de Lira | MID | 15 | 6.0 | 3.70 | 14.68 | 22.10 | 1.00 | 73.5 | 90.0 |
| Vice Captain | XI | Alex Iwobi | MID | 9 | 5.9 | 4.83 | 12.89 | 21.44 | 2.00 | 83.7 | 62.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.5 | 4.23 | 10.62 | 20.72 | 0.00 | 67.2 | 0.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.64
- Actual score: 35.00
- Transfer: Alex Iwobi -> Jacob Murphy (projected gain 3.23, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.50 | 10.48 | 17.13 | 2.00 | 85.4 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.58 | 10.32 | 19.14 | 1.00 | 90.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.54 | 11.48 | 23.20 | 2.00 | 71.1 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 3.32 | 11.41 | 17.10 | 2.00 | 82.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 3.96 | 11.32 | 19.75 | 1.00 | 79.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.52 | 10.64 | 18.04 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | 15 | 4.4 | 3.39 | 9.39 | 15.83 | 6.00 | 84.8 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.97 | 10.13 | 17.87 | 2.00 | 77.9 | 90.0 |
| XI | XI | Liam Delap | FWD | 10 | 5.6 | 4.17 | 9.80 | 18.40 | 1.00 | 75.6 | 83.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.05 | 6.73 | 10.58 | 1.00 | 58.9 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 6.66 | 20.26 | 32.33 | 2.00 | 85.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.56 | 20.07 | 30.79 | 10.00 | 86.5 | 90.0 |
| XI | XI | Joelinton Cássio Apolinário de Lira | MID | 15 | 6.0 | 4.03 | 13.27 | 19.74 | 3.00 | 78.1 | 82.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.1 | 3.58 | 12.61 | 18.17 | 3.00 | 77.0 | 77.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 3.42 | 10.41 | 16.93 | 6.00 | 76.0 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.80 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 60.27
- Actual score: 34.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (7.41).
- Transfer: Jacob Murphy -> Alex Iwobi (projected gain 6.30, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.71) beats the best remaining Triple Captain opportunity (7.41).
- Autosub: Morgan Rogers replaced William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 4.25 | 11.91 | 19.03 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.27 | 9.02 | 15.94 | 1.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 3.66 | 10.48 | 18.54 | 1.00 | 80.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.59 | 10.42 | 18.42 | 11.00 | 74.5 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.4 | 3.59 | 10.19 | 15.56 | 0.00 | 86.3 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 6.3 | 3.60 | 10.04 | 18.33 | 0.00 | 85.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.60 | 9.79 | 16.80 | 6.00 | 82.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.86 | 11.19 | 17.19 | 2.00 | 76.1 | 90.0 |
| Bench 3 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.80 | 8.47 | 13.16 | 2.00 | 67.4 | 72.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 1.40 | 6.28 | 9.47 | 1.00 | 50.4 | 57.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.4 | 6.71 | 19.89 | 37.77 | 2.00 | 83.3 | 83.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.6 | 5.61 | 17.29 | 28.17 | 3.00 | 85.0 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.9 | 4.83 | 16.01 | 19.51 | 1.00 | 81.2 | 45.0 |
| Bench 2 | Autosub In | Morgan Rogers | MID | 2 | 5.5 | 2.90 | 12.83 | 18.72 | 1.00 | 79.1 | 90.0 |
| XI | XI | Joelinton Cássio Apolinário de Lira | MID | 15 | 6.0 | 3.56 | 12.32 | 21.55 | 1.00 | 71.0 | 90.0 |

## GW23

- Train rows: 148648
- Bank: -0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.56
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.50) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alex Iwobi -> Amad Diallo (projected gain 5.82, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.50) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.0 | 3.97 | 10.44 | 19.41 | 5.00 | 89.3 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martin | GK | 1 | 5.6 | 3.14 | 9.92 | 16.35 | 9.00 | 85.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.2 | 3.66 | 14.56 | 21.95 | 5.00 | 83.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 3.29 | 10.71 | 17.70 | 7.00 | 85.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.59 | 10.16 | 16.07 | 2.00 | 80.9 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 4.4 | 2.97 | 8.42 | 15.47 | 2.00 | 83.1 | 90.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | 1 | 6.2 | 1.38 | 3.81 | 8.53 | 9.00 | 16.5 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.5 | 3.38 | 9.90 | 17.64 | 9.00 | 72.5 | 76.0 |
| Bench 2 | Bench Boost | Liam Delap | FWD | 10 | 5.6 | 2.35 | 8.64 | 11.98 | 1.00 | 60.8 | 78.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 1.63 | 5.48 | 10.49 | 1.00 | 47.6 | 59.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 4.97 | 20.12 | 36.37 | 2.00 | 78.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 7.46 | 19.19 | 26.92 | 8.00 | 85.1 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.6 | 4.29 | 13.96 | 23.98 | 3.00 | 83.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.5 | 4.00 | 10.87 | 17.51 | 1.00 | 81.1 | 71.0 |
| XI | XI | Joelinton Cássio Apolinário de Lira | MID | 15 | 6.0 | 3.03 | 10.37 | 16.45 | 2.00 | 74.4 | 90.0 |
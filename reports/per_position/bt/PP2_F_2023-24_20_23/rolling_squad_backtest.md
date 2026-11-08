# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 243.74
- Total actual points: 285.00
- Average predicted points: 60.93
- Average actual points: 71.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 117854
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.81
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.85 | 12.03 | 21.04 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 14.4 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 6.22 | 16.92 | 26.26 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.73 | 11.00 | 17.77 | 0.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.01 | 10.09 | 15.59 | 1.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.53 | 5.61 | 8.82 | 1.00 | 77.1 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.96 | 5.16 | 8.01 | 2.00 | 67.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.66 | 15.14 | 24.80 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.02 | 13.91 | 23.79 | 7.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 1.73 | 4.53 | 7.06 | 0.00 | 48.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 8.20 | 22.10 | 35.76 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.99 | 17.58 | 28.91 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.50 | 17.13 | 26.68 | 7.00 | 85.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.21 | 15.04 | 24.18 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 4.23 | 11.45 | 18.14 | 4.00 | 76.1 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 59.84
- Actual score: 48.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.57, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Chris Richards replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 4.10 | 11.76 | 18.99 | 9.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.19 | 0.62 | 1.14 | 0.00 | 11.8 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 4.24 | 13.85 | 21.75 | 0.00 | 71.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.09 | 10.94 | 17.49 | 6.00 | 88.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.21 | 9.10 | 14.64 | 17.00 | 86.9 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.25 | 5.82 | 9.19 | 1.00 | 74.8 | 79.0 |
| Bench 3 | Autosub In | Chris Richards | DEF | 8 | 3.9 | 1.34 | 4.90 | 7.85 | 0.00 | 71.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.69 | 16.22 | 27.83 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.11 | 13.40 | 22.26 | 2.00 | 66.6 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 0.88 | 2.99 | 4.52 | 1.00 | 20.9 | 8.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.95 | 20.80 | 31.90 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.37 | 18.11 | 26.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.23 | 14.68 | 23.73 | 2.00 | 88.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 3.40 | 12.81 | 25.04 | 0.00 | 31.8 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.50 | 9.72 | 15.35 | 2.00 | 70.8 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 4.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 60.44
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.09) beats the best remaining Triple Captain opportunity (8.04).
- Transfer: Trent Alexander-Arnold -> Pedro Porro (projected gain 4.39, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (7.09) beats the best remaining Triple Captain opportunity (8.04).
- Autosub: Chris Richards replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.83 | 10.77 | 17.20 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.28 | 0.73 | 1.16 | 0.00 | 11.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.11 | 12.46 | 19.60 | 1.00 | 82.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.04 | 11.23 | 17.81 | 2.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.18 | 8.28 | 12.83 | 2.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.06 | 5.88 | 9.10 | 0.00 | 68.4 | 90.0 |
| Bench 2 | Autosub In | Chris Richards | DEF | 8 | 3.9 | 2.14 | 5.26 | 8.52 | 1.00 | 75.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.96 | 14.27 | 24.91 | 7.00 | 79.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 3.98 | 12.29 | 21.14 | 13.00 | 63.2 | 86.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 1.53 | 4.29 | 7.23 | 1.00 | 24.0 | 45.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.09 | 18.39 | 29.26 | 10.00 | 79.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.47 | 14.73 | 26.95 | 0.00 | 21.2 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.47 | 12.85 | 20.95 | 6.00 | 44.9 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.05 | 12.60 | 21.86 | 1.00 | 65.2 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.09 | 8.79 | 14.81 | 1.00 | 70.6 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 4.40 -> 2.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 58.65
- Actual score: 90.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.29) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rodrigo Muniz Carvalho -> Timo Werner (projected gain 6.81, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.29) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.40 | 9.93 | 16.78 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.13 | 0.19 | 0.00 | 6.6 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.71 | 10.34 | 16.83 | 1.00 | 80.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.28 | 10.30 | 16.34 | 1.00 | 81.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.92 | 9.33 | 14.24 | -1.00 | 81.2 | 90.0 |
| Bench 3 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 1.89 | 5.35 | 8.42 | 0.00 | 72.3 | 90.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 1.73 | 5.27 | 8.30 | 0.00 | 73.4 | 90.0 |
| XI | XI | Timo Werner | FWD | 18 | 6.5 | 5.08 | 15.20 | 24.88 | 2.00 | 67.2 | 85.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.71 | 15.19 | 26.48 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.65 | 14.04 | 22.50 | 2.00 | 67.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.64 | 17.00 | 27.23 | 9.00 | 85.0 | 78.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.80 | 14.43 | 24.38 | 0.00 | 32.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.44 | 13.84 | 22.67 | 20.00 | 64.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.02 | 12.42 | 21.55 | 2.00 | 72.2 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.68 | 8.48 | 13.89 | 16.00 | 68.7 | 90.0 |
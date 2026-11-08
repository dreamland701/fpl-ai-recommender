# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 246.85
- Total actual points: 293.00
- Average predicted points: 61.71
- Average actual points: 73.25
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
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.47
- Actual score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.34 | 9.56 | 15.45 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.23 | 0.74 | 1.39 | 0.00 | 8.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.71 | 16.40 | 26.20 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.47 | 13.06 | 20.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.12 | 11.54 | 18.65 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.17 | 6.91 | 10.96 | 1.00 | 76.3 | 16.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.86 | 5.91 | 9.29 | 1.00 | 75.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.04 | 16.48 | 26.22 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.10 | 14.03 | 21.78 | 7.00 | 85.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.25 | 13.16 | 21.13 | 2.00 | 81.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.74 | 21.28 | 34.70 | 16.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.63 | 16.68 | 27.19 | 7.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.33 | 15.63 | 25.18 | 3.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.98 | 12.11 | 19.95 | 3.00 | 88.9 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 3.69 | 9.48 | 15.17 | 4.00 | 74.5 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 5.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 61.00
- Actual score: 40.00
- Transfer: Mohamed Salah -> Phil Foden (projected gain 7.10, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.19 | 8.88 | 14.67 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.39 | 0.85 | 1.58 | 0.00 | 11.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.63 | 13.68 | 22.09 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.83 | 12.57 | 21.13 | 0.00 | 72.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.17 | 11.33 | 18.41 | 6.00 | 89.8 | 90.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.21 | 5.97 | 9.71 | 1.00 | 70.2 | 79.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 0.97 | 3.90 | 7.09 | 0.00 | 31.5 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.18 | 17.33 | 27.37 | 1.00 | 90.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.07 | 13.13 | 21.27 | 2.00 | 80.4 | 82.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.31 | 12.99 | 20.37 | 2.00 | 69.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.44 | 19.91 | 31.53 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.21 | 17.62 | 26.80 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.05 | 14.65 | 23.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.48 | 13.11 | 21.46 | 3.00 | 89.5 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.81 | 8.36 | 13.05 | 2.00 | 69.1 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 5.30 -> 2.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.98
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.10) beats the best remaining Triple Captain opportunity (6.92).
- Transfer: Jordan Beyer -> Kieran Trippier (projected gain 3.12, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.10) beats the best remaining Triple Captain opportunity (6.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.12 | 8.87 | 15.09 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.39 | 0.84 | 1.65 | 0.00 | 11.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.42 | 12.80 | 21.12 | 1.00 | 84.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.64 | 11.15 | 19.01 | 7.00 | 78.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.01 | 11.01 | 17.88 | 2.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.26 | 8.67 | 15.64 | 1.00 | 29.2 | 22.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.98 | 5.80 | 9.42 | 0.00 | 64.4 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.17 | 15.04 | 24.50 | 7.00 | 82.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.40 | 12.93 | 20.55 | 13.00 | 62.6 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.69 | 11.82 | 18.98 | 8.00 | 71.2 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.10 | 17.26 | 27.69 | 10.00 | 82.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.02 | 12.29 | 21.00 | 1.00 | 68.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.61 | 11.95 | 19.03 | 6.00 | 44.7 | 76.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.58 | 11.44 | 18.82 | 2.00 | 75.2 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.57 | 7.76 | 12.80 | 1.00 | 65.8 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 2.60 -> 1.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 64.40
- Actual score: 100.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.05) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alejandro Garnacho -> Anthony Gordon (projected gain 0.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.05) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.17 | 9.01 | 15.05 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.11 | 0.40 | 0.00 | 0.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.66 | 13.37 | 21.58 | 9.00 | 88.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.21 | 12.22 | 19.94 | 1.00 | 84.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.63 | 10.65 | 17.16 | 1.00 | 86.2 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.91 | 10.27 | 17.45 | 1.00 | 49.3 | 57.0 |
| Bench 4 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.22 | 5.95 | 9.48 | 0.00 | 70.8 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.93 | 16.50 | 26.52 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.69 | 13.00 | 21.62 | 2.00 | 61.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.62 | 12.98 | 21.06 | 2.00 | 81.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.75 | 17.12 | 27.43 | 9.00 | 90.0 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.34 | 12.76 | 20.93 | 20.00 | 65.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.08 | 12.24 | 21.01 | 2.00 | 77.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.2 | 4.33 | 12.10 | 19.48 | 4.00 | 90.0 | 45.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 5 | 6.4 | 3.92 | 11.66 | 19.02 | 11.00 | 83.9 | 90.0 |
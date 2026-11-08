# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 246.51
- Total actual points: 297.00
- Average predicted points: 61.63
- Average actual points: 74.25
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
- Predicted score: 62.78
- Actual score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.26 | 9.41 | 15.33 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.36 | 0.91 | 1.60 | 0.00 | 12.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.66 | 16.34 | 26.19 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.42 | 12.99 | 20.83 | 2.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.07 | 11.46 | 18.59 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.12 | 6.85 | 10.94 | 1.00 | 75.2 | 16.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.80 | 5.84 | 9.22 | 1.00 | 73.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.98 | 16.38 | 26.15 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.03 | 13.94 | 21.70 | 7.00 | 83.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.17 | 13.04 | 21.04 | 2.00 | 79.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.70 | 21.21 | 34.67 | 16.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.58 | 16.59 | 27.12 | 7.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.29 | 15.56 | 25.13 | 3.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.92 | 12.02 | 19.88 | 3.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 3.65 | 9.44 | 15.16 | 4.00 | 73.4 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 5.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 61.32
- Actual score: 40.00
- Transfer: Mohamed Salah -> Phil Foden (projected gain 6.96, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.11 | 8.76 | 14.57 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.37 | 0.81 | 1.45 | 0.00 | 10.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.58 | 13.60 | 22.04 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.91 | 12.69 | 21.21 | 0.00 | 74.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.24 | 11.42 | 18.44 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.29 | 6.08 | 9.75 | 1.00 | 71.6 | 79.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.07 | 3.62 | 6.31 | 0.00 | 34.3 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.14 | 17.26 | 27.31 | 1.00 | 90.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.15 | 13.25 | 21.36 | 2.00 | 81.9 | 82.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.23 | 12.90 | 20.33 | 2.00 | 66.9 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.54 | 20.07 | 31.65 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.17 | 17.55 | 26.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.15 | 14.79 | 23.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.57 | 13.24 | 21.52 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.75 | 8.29 | 13.00 | 2.00 | 67.7 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 5.30 -> 2.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 58.77
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.17) beats the best remaining Triple Captain opportunity (7.00).
- Transfer: Jordan Beyer -> Kieran Trippier (projected gain 3.19, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.17) beats the best remaining Triple Captain opportunity (7.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.16 | 8.91 | 15.09 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.38 | 0.80 | 1.55 | 0.00 | 10.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.49 | 12.90 | 21.18 | 1.00 | 85.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.66 | 11.15 | 18.96 | 7.00 | 78.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.06 | 11.07 | 17.90 | 2.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.25 | 8.62 | 15.54 | 1.00 | 28.8 | 22.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.06 | 5.91 | 9.49 | 0.00 | 65.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.24 | 15.12 | 24.54 | 7.00 | 83.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.48 | 13.07 | 20.69 | 13.00 | 64.2 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.75 | 11.92 | 19.05 | 8.00 | 72.6 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.38 | 27.80 | 10.00 | 83.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.07 | 12.33 | 20.99 | 1.00 | 69.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.69 | 12.07 | 19.15 | 6.00 | 46.4 | 76.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.64 | 11.52 | 18.87 | 2.00 | 76.5 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.64 | 7.86 | 12.86 | 1.00 | 67.1 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 2.60 -> 1.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 63.64
- Actual score: 104.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.07) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alejandro Garnacho -> Cole Palmer (projected gain 0.64, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.07) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.08 | 8.87 | 14.92 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.30 | 0.63 | 0.00 | 5.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.56 | 13.19 | 21.42 | 9.00 | 85.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.14 | 12.12 | 19.87 | 1.00 | 83.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.56 | 10.53 | 17.06 | 1.00 | 84.4 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.03 | 10.44 | 17.67 | 1.00 | 54.1 | 57.0 |
| Bench 4 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.18 | 5.89 | 9.43 | 0.00 | 69.7 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.86 | 16.38 | 26.42 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.89 | 13.35 | 22.07 | 2.00 | 67.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.56 | 12.88 | 20.99 | 2.00 | 79.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.68 | 17.01 | 27.34 | 9.00 | 88.9 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.28 | 12.66 | 20.84 | 20.00 | 63.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.98 | 12.10 | 20.88 | 2.00 | 75.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.13 | 12.08 | 19.21 | 8.00 | 77.8 | 90.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 5 | 6.4 | 3.85 | 11.55 | 18.93 | 11.00 | 82.3 | 90.0 |
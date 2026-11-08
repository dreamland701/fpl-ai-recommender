# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 239.81
- Total actual points: 286.00
- Average predicted points: 59.95
- Average actual points: 71.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.34
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.58 | 9.30 | 15.06 | 11.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.60 | 1.15 | 1.64 | 0.00 | 11.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.61 | 16.22 | 25.92 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.36 | 12.83 | 20.47 | 2.00 | 89.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.02 | 11.26 | 18.15 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.30 | 7.36 | 11.74 | 1.00 | 79.8 | 16.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.45 | 6.99 | 11.17 | 8.00 | 80.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.88 | 16.08 | 25.50 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.05 | 14.01 | 21.74 | 7.00 | 84.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.10 | 12.75 | 20.41 | 2.00 | 77.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.62 | 22.15 | 36.09 | 16.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.48 | 16.22 | 26.33 | 7.00 | 86.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.20 | 15.29 | 24.59 | 3.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.82 | 11.58 | 19.02 | 3.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 3.75 | 9.81 | 15.78 | 4.00 | 77.1 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 5.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.13
- Actual score: 39.00
- Transfer: Mohamed Salah -> Phil Foden (projected gain 8.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.88 | 10.59 | 17.50 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.13 | 0.73 | 1.28 | 2.00 | 11.3 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.51 | 13.46 | 21.69 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.06 | 11.02 | 17.84 | 6.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.44 | 9.14 | 16.93 | 0.00 | 49.3 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.57 | 7.09 | 11.69 | 6.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.14 | 4.43 | 7.97 | 0.00 | 36.1 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.03 | 17.01 | 26.75 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.27 | 12.93 | 20.22 | 2.00 | 68.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.92 | 12.69 | 20.47 | 2.00 | 75.8 | 82.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.26 | 19.40 | 30.57 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.11 | 17.46 | 26.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.94 | 12.65 | 20.06 | 2.00 | 60.6 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.30 | 12.53 | 20.40 | 3.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.90 | 8.85 | 13.96 | 2.00 | 72.2 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 5.40 -> 1.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.73
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.97) beats the best remaining Triple Captain opportunity (6.77).
- Transfer: Alejandro Garnacho -> Martin Ødegaard (projected gain 2.26, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.97) beats the best remaining Triple Captain opportunity (6.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.39 | 9.43 | 15.79 | 3.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.37 | 3.18 | 5.14 | 0.00 | 36.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.31 | 12.65 | 20.84 | 1.00 | 81.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.19 | 11.28 | 18.94 | 1.00 | 42.5 | 22.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.92 | 10.78 | 17.49 | 2.00 | 81.8 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.58 | 7.55 | 12.32 | 0.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 0.12 | 1.96 | 3.87 | 0.00 | 23.1 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.07 | 14.76 | 23.97 | 7.00 | 78.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.39 | 12.89 | 20.45 | 13.00 | 62.6 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.53 | 11.44 | 18.34 | 8.00 | 66.9 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.97 | 16.84 | 26.94 | 10.00 | 78.6 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.48 | 13.14 | 21.47 | 2.00 | 73.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.93 | 12.13 | 20.75 | 1.00 | 65.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.61 | 11.99 | 19.14 | 6.00 | 44.3 | 76.0 |
| Bench 2 | Bench | Pascal Groß | MID | 5 | 6.4 | 3.43 | 10.96 | 17.97 | 2.00 | 70.5 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 1.70 -> 3.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 61.61
- Actual score: 98.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.47) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> Kieran Trippier (projected gain 2.70, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.47) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.21 | 9.64 | 15.65 | 1.00 | 83.9 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.63 | 1.52 | 2.54 | 0.00 | 19.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.43 | 12.62 | 20.29 | 9.00 | 81.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.13 | 12.12 | 19.81 | 1.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.54 | 10.43 | 16.79 | 1.00 | 83.7 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.77 | 7.75 | 12.56 | 2.00 | 77.3 | 90.0 |
| Bench 4 | Bench Boost | Jordan Beyer | DEF | 6 | 4.0 | 0.28 | 1.74 | 3.51 | 0.00 | 8.5 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.81 | 16.29 | 26.15 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.70 | 13.00 | 21.58 | 2.00 | 61.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.45 | 12.51 | 20.25 | 2.00 | 76.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.64 | 16.78 | 26.80 | 9.00 | 86.9 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.39 | 13.06 | 21.46 | 20.00 | 66.6 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.06 | 12.60 | 20.28 | 2.00 | 74.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.97 | 11.97 | 20.56 | 2.00 | 74.7 | 90.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 5 | 6.4 | 3.79 | 11.27 | 18.34 | 11.00 | 79.7 | 90.0 |
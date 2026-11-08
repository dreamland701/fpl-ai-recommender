# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 239.98
- Total actual points: 286.00
- Average predicted points: 60.00
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
- Predicted score: 61.81
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.52 | 9.22 | 14.99 | 11.00 | 77.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.47 | 0.95 | 1.45 | 0.00 | 8.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.59 | 16.21 | 25.94 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.32 | 12.79 | 20.46 | 2.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.99 | 11.22 | 18.13 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.25 | 7.30 | 11.72 | 1.00 | 78.6 | 16.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.41 | 6.93 | 11.14 | 8.00 | 78.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.85 | 16.03 | 25.49 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.00 | 13.93 | 21.68 | 7.00 | 83.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.04 | 12.68 | 20.38 | 2.00 | 75.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.55 | 22.03 | 35.95 | 16.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 16.18 | 26.30 | 7.00 | 86.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.17 | 15.25 | 24.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.78 | 11.54 | 19.00 | 3.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 3.71 | 9.77 | 15.78 | 4.00 | 76.1 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 5.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.44
- Actual score: 39.00
- Transfer: Mohamed Salah -> Phil Foden (projected gain 8.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.97 | 10.71 | 17.54 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.53 | 1.09 | 2.00 | 7.7 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.47 | 13.42 | 21.67 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.14 | 11.13 | 17.88 | 6.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.31 | 8.93 | 16.58 | 0.00 | 46.2 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.63 | 7.19 | 11.72 | 6.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.23 | 4.08 | 7.10 | 0.00 | 38.2 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.01 | 16.97 | 26.74 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.21 | 12.86 | 20.21 | 2.00 | 66.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.00 | 12.85 | 20.57 | 2.00 | 77.5 | 82.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.37 | 19.57 | 30.68 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.07 | 17.38 | 26.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.39 | 12.67 | 20.47 | 3.00 | 85.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.81 | 12.38 | 19.70 | 2.00 | 56.9 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.85 | 8.78 | 13.93 | 2.00 | 70.9 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 5.40 -> 1.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 58.61
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.86).
- Transfer: Alejandro Garnacho -> Martin Ødegaard (projected gain 2.27, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.46 | 9.53 | 15.83 | 3.00 | 80.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.37 | 3.17 | 5.06 | 0.00 | 36.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.39 | 12.76 | 20.90 | 1.00 | 83.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.16 | 11.25 | 18.97 | 1.00 | 41.6 | 22.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.98 | 10.87 | 17.54 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.64 | 7.64 | 12.37 | 0.00 | 77.2 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 0.14 | 1.98 | 3.85 | 0.00 | 23.1 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.15 | 14.88 | 24.03 | 7.00 | 80.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.47 | 13.04 | 20.58 | 13.00 | 64.1 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.61 | 11.57 | 18.43 | 8.00 | 68.5 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.05 | 16.99 | 27.07 | 10.00 | 80.3 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.57 | 13.26 | 21.55 | 2.00 | 75.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.99 | 12.21 | 20.77 | 1.00 | 66.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.68 | 12.12 | 19.25 | 6.00 | 46.0 | 76.0 |
| Bench 2 | Bench | Pascal Groß | MID | 5 | 6.4 | 3.50 | 11.08 | 18.03 | 2.00 | 72.0 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 1.70 -> 3.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 61.12
- Actual score: 98.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.29) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> Kieran Trippier (projected gain 2.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.29) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.15 | 9.56 | 15.58 | 1.00 | 82.4 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.51 | 1.33 | 2.35 | 0.00 | 15.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.35 | 12.51 | 20.20 | 9.00 | 79.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.08 | 12.06 | 19.78 | 1.00 | 81.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.50 | 10.36 | 16.75 | 1.00 | 82.4 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.72 | 7.68 | 12.52 | 2.00 | 75.9 | 90.0 |
| Bench 4 | Bench Boost | Jordan Beyer | DEF | 6 | 4.0 | 0.31 | 1.33 | 2.50 | 0.00 | 9.2 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.77 | 16.22 | 26.12 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.92 | 13.37 | 22.05 | 2.00 | 69.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.42 | 12.47 | 20.24 | 2.00 | 75.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.60 | 16.73 | 26.78 | 9.00 | 85.9 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.34 | 12.99 | 21.41 | 20.00 | 65.4 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.02 | 12.56 | 20.26 | 2.00 | 73.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.91 | 11.89 | 20.51 | 2.00 | 73.1 | 90.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 5 | 6.4 | 3.75 | 11.21 | 18.31 | 11.00 | 78.6 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 245.39
- Total actual points: 299.00
- Average predicted points: 61.35
- Average actual points: 74.75
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
- Predicted score: 62.28
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.51 | 9.15 | 14.87 | 11.00 | 76.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.48 | 0.97 | 1.48 | 0.00 | 8.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.67 | 16.49 | 26.45 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.39 | 13.04 | 20.95 | 2.00 | 88.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.96 | 11.10 | 17.95 | 0.00 | 89.7 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.25 | 7.29 | 11.70 | 1.00 | 78.5 | 16.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.40 | 6.88 | 11.05 | 8.00 | 78.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.88 | 16.27 | 26.03 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.01 | 13.98 | 21.82 | 7.00 | 83.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.01 | 12.62 | 20.28 | 2.00 | 74.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.61 | 21.04 | 34.38 | 16.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.46 | 16.28 | 26.48 | 7.00 | 85.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.18 | 15.27 | 24.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.99 | 12.61 | 21.09 | 3.00 | 85.1 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 3.68 | 9.51 | 15.28 | 4.00 | 75.7 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 5.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 61.26
- Actual score: 39.00
- Transfer: Mohamed Salah -> Phil Foden (projected gain 6.59, hit 0)
- Autosub: Jan Paul van Hecke replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.96 | 10.65 | 17.42 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.01 | 0.55 | 1.12 | 2.00 | 7.7 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.59 | 13.84 | 22.47 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.95 | 13.00 | 21.76 | 0.00 | 73.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.11 | 11.01 | 17.66 | 6.00 | 88.0 | 90.0 |
| Bench 3 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.61 | 7.12 | 11.61 | 6.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.21 | 4.05 | 7.08 | 0.00 | 37.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.05 | 17.22 | 27.30 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.18 | 12.77 | 20.13 | 2.00 | 66.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.97 | 12.74 | 20.37 | 2.00 | 76.5 | 82.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.39 | 19.61 | 30.66 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.06 | 17.06 | 25.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.00 | 14.37 | 23.19 | 2.00 | 88.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.62 | 13.75 | 22.55 | 3.00 | 88.4 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.80 | 8.52 | 13.46 | 2.00 | 70.5 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 5.40 -> 2.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.58
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.98) beats the best remaining Triple Captain opportunity (6.78).
- Transfer: Jordan Beyer -> Kieran Trippier (projected gain 3.73, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.98) beats the best remaining Triple Captain opportunity (6.78).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.43 | 9.44 | 15.67 | 3.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.39 | 3.21 | 5.12 | 0.00 | 36.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.46 | 13.03 | 21.46 | 1.00 | 83.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.62 | 11.22 | 19.11 | 7.00 | 74.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.94 | 10.73 | 17.29 | 2.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.29 | 8.99 | 16.24 | 1.00 | 28.2 | 22.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.63 | 7.61 | 12.32 | 0.00 | 77.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.13 | 15.01 | 24.41 | 7.00 | 79.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.40 | 12.84 | 20.32 | 13.00 | 62.8 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.55 | 11.43 | 18.15 | 8.00 | 67.2 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.98 | 16.81 | 26.65 | 10.00 | 78.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.70 | 12.13 | 20.09 | 2.00 | 74.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.91 | 11.94 | 20.36 | 1.00 | 64.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.50 | 11.38 | 17.89 | 6.00 | 43.5 | 76.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.70 | 8.11 | 13.35 | 1.00 | 70.3 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 2.70 -> 1.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 64.28
- Actual score: 105.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.20) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alejandro Garnacho -> Cole Palmer (projected gain 1.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.20) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.13 | 9.50 | 15.50 | 1.00 | 82.0 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.52 | 1.36 | 2.40 | 0.00 | 15.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.51 | 13.12 | 21.33 | 9.00 | 81.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.15 | 12.37 | 20.41 | 1.00 | 81.7 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.12 | 10.95 | 18.66 | 1.00 | 53.4 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.45 | 10.22 | 16.52 | 1.00 | 81.6 | 90.0 |
| Bench 4 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.71 | 7.64 | 12.47 | 2.00 | 75.6 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.76 | 16.31 | 26.41 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.85 | 13.21 | 21.88 | 2.00 | 67.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.38 | 12.35 | 20.02 | 2.00 | 74.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.52 | 16.53 | 26.38 | 9.00 | 84.5 | 78.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.39 | 13.25 | 21.35 | 8.00 | 83.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.97 | 12.38 | 20.57 | 11.00 | 80.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.19 | 12.34 | 20.26 | 20.00 | 63.4 | 90.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | 19 | 7.9 | 3.86 | 11.74 | 20.33 | 2.00 | 72.1 | 90.0 |
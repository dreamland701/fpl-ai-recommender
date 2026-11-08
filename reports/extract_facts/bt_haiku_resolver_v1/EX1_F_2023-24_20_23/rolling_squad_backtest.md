# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 238.57
- Total actual points: 299.00
- Average predicted points: 59.64
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.46
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.52 | 9.19 | 14.95 | 11.00 | 76.9 | 90.0 |
| Bench 1 | Bench | Lawrence Vigouroux | GK | 6 | 3.9 | 0.08 | 0.67 | 1.00 | 0.00 | 9.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.56 | 16.16 | 25.85 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.29 | 12.74 | 20.39 | 2.00 | 87.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.97 | 11.17 | 18.06 | 0.00 | 89.8 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.24 | 7.29 | 11.69 | 1.00 | 78.5 | 16.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.40 | 6.93 | 11.13 | 8.00 | 78.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.83 | 15.98 | 25.40 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.98 | 13.89 | 21.64 | 7.00 | 83.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.01 | 12.64 | 20.32 | 2.00 | 75.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 6.49 | 17.07 | 31.27 | 16.00 | 81.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.40 | 16.08 | 26.18 | 7.00 | 85.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.15 | 15.21 | 24.52 | 3.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.76 | 11.50 | 18.95 | 3.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 3.71 | 9.77 | 15.76 | 4.00 | 76.0 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 5.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.72
- Actual score: 39.00
- Transfer: Mohamed Salah -> Phil Foden (projected gain 8.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.96 | 10.69 | 17.49 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Lawrence Vigouroux | GK | 6 | 3.9 | 0.35 | 0.58 | 1.11 | 0.00 | 7.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.46 | 13.40 | 21.63 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.13 | 11.10 | 17.82 | 6.00 | 88.2 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 1.88 | 9.88 | 17.30 | 0.00 | 39.5 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.62 | 7.17 | 11.69 | 6.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.21 | 4.06 | 7.05 | 0.00 | 38.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.98 | 16.89 | 26.62 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.18 | 12.84 | 20.14 | 2.00 | 66.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.98 | 12.81 | 20.50 | 2.00 | 77.1 | 82.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.36 | 19.53 | 30.59 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.06 | 17.36 | 26.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 5.01 | 14.31 | 22.73 | 3.00 | 86.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.62 | 10.49 | 20.32 | 2.00 | 62.9 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.83 | 8.75 | 13.88 | 2.00 | 70.6 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 5.30 -> 2.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.56
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.83).
- Transfer: Jordan Beyer -> Kieran Trippier (projected gain 3.05, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.45 | 9.50 | 15.78 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Lawrence Vigouroux | GK | 6 | 3.9 | 0.00 | 0.26 | 0.71 | 0.00 | 8.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.37 | 12.72 | 20.82 | 1.00 | 82.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.97 | 10.84 | 17.47 | 2.00 | 82.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.46 | 10.57 | 17.89 | 7.00 | 72.6 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.11 | 10.14 | 16.04 | 1.00 | 29.2 | 22.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.63 | 7.63 | 12.35 | 0.00 | 77.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.12 | 14.81 | 23.90 | 7.00 | 80.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.45 | 13.01 | 20.50 | 13.00 | 63.7 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.58 | 11.53 | 18.37 | 8.00 | 68.1 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.03 | 16.96 | 26.95 | 10.00 | 80.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.97 | 12.18 | 20.72 | 1.00 | 65.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.64 | 12.07 | 19.11 | 6.00 | 45.4 | 76.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.47 | 11.03 | 17.95 | 2.00 | 71.7 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.75 | 8.39 | 13.87 | 1.00 | 70.8 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 2.60 -> 1.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 62.83
- Actual score: 105.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.79) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alejandro Garnacho -> Cole Palmer (projected gain 1.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.14 | 9.52 | 15.52 | 1.00 | 82.2 | 45.0 |
| Bench 1 | Bench Boost | Lawrence Vigouroux | GK | 6 | 3.9 | 0.41 | 0.65 | 1.00 | 0.00 | 6.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.33 | 12.47 | 20.15 | 9.00 | 79.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.06 | 12.02 | 19.69 | 1.00 | 80.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.48 | 10.32 | 16.67 | 1.00 | 82.1 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.94 | 10.29 | 17.42 | 1.00 | 51.2 | 57.0 |
| Bench 4 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.72 | 7.67 | 12.51 | 2.00 | 75.7 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.76 | 16.18 | 26.02 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.08 | 13.72 | 23.68 | 2.00 | 75.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.41 | 12.45 | 20.20 | 2.00 | 75.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.55 | 16.63 | 26.64 | 9.00 | 85.4 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.33 | 12.95 | 21.32 | 20.00 | 65.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.25 | 12.68 | 20.30 | 8.00 | 82.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.90 | 11.87 | 20.46 | 2.00 | 72.9 | 90.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 5 | 6.4 | 3.73 | 11.17 | 18.25 | 11.00 | 78.5 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 230.76
- Total actual points: 252.00
- Average predicted points: 57.69
- Average actual points: 63.00
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
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.99
- Actual score: 76.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.54 | 9.17 | 14.82 | 11.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.42 | 0.86 | 1.37 | 0.00 | 7.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.15 | 14.92 | 24.15 | 0.00 | 82.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 3.88 | 11.51 | 18.67 | 2.00 | 80.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 4.11 | 11.36 | 18.30 | 1.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.94 | 6.24 | 9.83 | 1.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.07 | 5.77 | 9.53 | 1.00 | 65.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.13 | 14.14 | 21.94 | 7.00 | 82.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.05 | 12.63 | 20.23 | 2.00 | 76.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.00 | 10.70 | 16.48 | 2.00 | 78.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.19 | 19.78 | 32.60 | 16.00 | 82.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.55 | 16.31 | 26.47 | 7.00 | 84.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.47 | 16.21 | 26.95 | 9.00 | 82.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.74 | 13.98 | 22.84 | 3.00 | 82.7 | 90.0 |
| Bench 4 | Bench | James McAtee | MID | 17 | 4.4 | 1.83 | 6.20 | 10.31 | 0.00 | 62.3 | 0.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 55.05
- Actual score: 34.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 9.90, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.54 | 9.48 | 15.78 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.44 | 1.01 | 2.00 | 6.7 | 82.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.93 | 12.83 | 21.50 | 0.00 | 75.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.06 | 12.22 | 19.98 | 6.00 | 82.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.52 | 10.14 | 16.23 | 6.00 | 81.1 | 90.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.40 | 6.46 | 10.79 | 2.00 | 73.8 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.42 | 6.44 | 10.28 | 1.00 | 76.6 | 79.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.31 | 13.12 | 20.75 | 2.00 | 70.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.01 | 12.78 | 20.39 | 2.00 | 79.0 | 82.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.56 | 12.48 | 18.94 | 2.00 | 80.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.97 | 18.39 | 29.05 | 3.00 | 82.7 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 5.72 | 16.31 | 24.97 | 2.00 | 82.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.57 | 13.15 | 21.44 | 2.00 | 81.3 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.90 | 11.08 | 21.33 | 0.00 | 30.9 | 0.0 |
| Bench 4 | Bench | James McAtee | MID | 17 | 4.4 | 1.49 | 4.32 | 7.59 | 2.00 | 37.3 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 4.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Julián Álvarez
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.26
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (6.85).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 4.72, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (6.85).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.46 | 9.47 | 15.60 | 3.00 | 81.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.33 | 3.09 | 4.98 | 0.00 | 35.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.49 | 12.93 | 21.08 | 1.00 | 81.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.06 | 10.99 | 17.61 | 2.00 | 81.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.45 | 10.10 | 16.14 | 2.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.25 | 6.47 | 10.50 | 0.00 | 72.3 | 90.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.40 | 6.29 | 10.22 | 6.00 | 73.8 | 90.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.53 | 13.24 | 21.04 | 13.00 | 67.1 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.68 | 11.79 | 18.88 | 8.00 | 71.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.67 | 11.07 | 17.46 | 2.00 | 72.5 | 70.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.04 | 16.93 | 26.86 | 10.00 | 81.3 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.20 | 12.51 | 23.28 | 0.00 | 20.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.03 | 12.37 | 21.16 | 1.00 | 69.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.58 | 11.96 | 19.09 | 6.00 | 43.9 | 76.0 |
| Bench 3 | Bench | James McAtee | MID | 17 | 4.4 | 2.38 | 6.78 | 11.12 | 7.00 | 64.0 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 4.70 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 59.46
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.61) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 7.89, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.61) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.25 | 9.70 | 15.67 | 1.00 | 80.6 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.46 | 1.24 | 2.26 | 0.00 | 14.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.18 | 12.22 | 19.89 | 1.00 | 79.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.59 | 10.48 | 16.81 | 1.00 | 80.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.15 | 10.03 | 16.25 | 1.00 | 78.8 | 90.0 |
| Bench 4 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.27 | 7.00 | 11.30 | 0.00 | 75.0 | 90.0 |
| Bench 3 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.30 | 6.14 | 9.72 | 0.00 | 74.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.32 | 14.94 | 24.43 | 18.00 | 82.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.97 | 13.56 | 22.50 | 2.00 | 71.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.42 | 12.39 | 20.03 | 2.00 | 76.8 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.67 | 16.84 | 26.87 | 9.00 | 83.4 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.40 | 13.16 | 21.83 | 20.00 | 68.5 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.33 | 12.48 | 21.57 | 0.00 | 31.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.89 | 11.77 | 20.21 | 2.00 | 74.0 | 90.0 |
| Bench 2 | Bench Boost | James McAtee | MID | 17 | 4.4 | 2.58 | 7.08 | 11.58 | 2.00 | 68.7 | 71.0 |
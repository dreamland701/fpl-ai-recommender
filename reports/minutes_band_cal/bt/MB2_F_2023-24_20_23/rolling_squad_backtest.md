# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 229.49
- Total actual points: 253.00
- Average predicted points: 57.37
- Average actual points: 63.25
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
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.92
- Actual score: 76.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.58 | 9.25 | 15.03 | 11.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.47 | 0.95 | 1.48 | 0.00 | 8.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.20 | 15.05 | 24.26 | 0.00 | 82.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 3.94 | 11.65 | 18.78 | 2.00 | 80.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.94 | 11.11 | 17.95 | 1.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.98 | 6.32 | 10.04 | 1.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.05 | 5.75 | 9.48 | 1.00 | 65.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.96 | 13.89 | 21.58 | 7.00 | 81.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.08 | 12.71 | 20.44 | 2.00 | 76.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.04 | 10.78 | 16.69 | 2.00 | 78.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.24 | 19.92 | 32.71 | 16.00 | 82.8 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.53 | 16.35 | 27.06 | 9.00 | 82.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.37 | 16.06 | 26.11 | 7.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.80 | 14.12 | 22.94 | 3.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.20 | 6.13 | 9.84 | 1.00 | 65.3 | 45.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 55.35
- Actual score: 34.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 9.99, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.60 | 9.64 | 15.92 | 3.00 | 82.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.53 | 1.11 | 2.00 | 7.7 | 82.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.91 | 12.82 | 21.48 | 0.00 | 75.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.12 | 12.38 | 20.11 | 6.00 | 82.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.59 | 10.30 | 16.37 | 6.00 | 81.1 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.45 | 6.50 | 10.45 | 1.00 | 75.7 | 79.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.39 | 6.44 | 10.77 | 2.00 | 74.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.29 | 13.10 | 20.73 | 2.00 | 70.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.04 | 12.84 | 20.56 | 2.00 | 78.1 | 82.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.37 | 12.23 | 18.56 | 2.00 | 79.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.03 | 18.55 | 29.18 | 3.00 | 82.8 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 5.78 | 16.46 | 25.11 | 2.00 | 82.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.63 | 13.31 | 21.57 | 2.00 | 81.4 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.95 | 11.18 | 21.42 | 0.00 | 31.8 | 0.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.11 | 6.10 | 9.90 | 2.00 | 60.0 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 4.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Julián Álvarez
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.09
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.07) beats the best remaining Triple Captain opportunity (6.89).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 4.37, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.07) beats the best remaining Triple Captain opportunity (6.89).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.49 | 9.54 | 15.80 | 3.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.37 | 3.17 | 5.09 | 0.00 | 36.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.29 | 12.64 | 20.65 | 1.00 | 80.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.87 | 10.70 | 17.19 | 2.00 | 79.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.48 | 10.18 | 16.34 | 2.00 | 78.5 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.24 | 6.46 | 10.48 | 0.00 | 72.3 | 90.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.43 | 6.36 | 10.42 | 6.00 | 73.0 | 90.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.51 | 13.24 | 21.03 | 13.00 | 67.1 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.66 | 11.78 | 18.87 | 8.00 | 71.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.66 | 11.06 | 17.44 | 2.00 | 72.5 | 70.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.07 | 17.01 | 27.06 | 10.00 | 80.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.25 | 12.61 | 23.38 | 0.00 | 21.2 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.02 | 12.36 | 21.14 | 1.00 | 69.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.62 | 12.05 | 19.20 | 6.00 | 44.9 | 76.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.15 | 6.18 | 9.93 | 10.00 | 66.3 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 4.70 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 58.14
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.32) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 8.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.32) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.06 | 9.39 | 15.25 | 1.00 | 79.6 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.51 | 1.32 | 2.37 | 0.00 | 15.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.98 | 11.91 | 19.47 | 1.00 | 78.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.39 | 10.17 | 16.39 | 1.00 | 79.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 2.96 | 9.72 | 15.84 | 1.00 | 77.8 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.27 | 6.99 | 11.26 | 0.00 | 75.1 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.33 | 6.22 | 9.94 | 0.00 | 73.3 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.38 | 15.10 | 24.54 | 18.00 | 82.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.96 | 13.55 | 22.46 | 2.00 | 71.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.45 | 12.48 | 20.24 | 2.00 | 76.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.47 | 16.54 | 26.45 | 9.00 | 82.5 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.39 | 13.15 | 21.79 | 20.00 | 68.5 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.38 | 12.58 | 21.67 | 0.00 | 32.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.92 | 11.85 | 20.43 | 2.00 | 73.2 | 90.0 |
| Bench 4 | Bench Boost | Kobbie Mainoo | MID | 14 | 4.4 | 2.22 | 6.34 | 10.26 | 3.00 | 68.1 | 63.0 |
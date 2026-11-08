# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 252.34
- Total actual points: 285.00
- Average predicted points: 63.08
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Julián Álvarez
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.15
- Actual score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.04 | 8.74 | 14.44 | 11.00 | 74.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.23 | 0.57 | 0.00 | 0.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.62 | 15.68 | 25.22 | 0.00 | 93.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.74 | 12.96 | 20.65 | 2.00 | 97.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.18 | 11.60 | 18.65 | 0.00 | 91.5 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.82 | 7.47 | 11.84 | 8.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.77 | 6.78 | 11.11 | 1.00 | 73.2 | 16.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.09 | 16.30 | 25.87 | 8.00 | 102.4 | 90.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 6.9 | 6.34 | 14.20 | 21.79 | 7.00 | 92.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.47 | 11.26 | 17.40 | 2.00 | 83.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.47 | 20.67 | 33.85 | 16.00 | 103.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 6.03 | 17.31 | 28.41 | 9.00 | 100.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.54 | 16.35 | 26.57 | 7.00 | 85.2 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.17 | 11.96 | 19.56 | 3.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Lewis Miley | MID | 15 | 4.5 | 2.52 | 8.57 | 13.94 | 0.00 | 72.5 | 53.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 62.53
- Actual score: 39.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 6.15, hit 0)
- Autosub: Lewis Miley replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.90 | 10.76 | 17.66 | 3.00 | 92.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.00 | 0.23 | 0.60 | 2.00 | 0.0 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.02 | 13.04 | 21.47 | 6.00 | 94.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 5.15 | 12.40 | 19.47 | 6.00 | 99.7 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.64 | 11.98 | 20.02 | 0.00 | 69.2 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 3.26 | 7.90 | 12.59 | 6.00 | 87.2 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.89 | 5.27 | 8.86 | 0.00 | 51.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.08 | 16.05 | 25.79 | 1.00 | 90.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 5.37 | 12.78 | 19.32 | 2.00 | 94.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.01 | 12.42 | 19.76 | 2.00 | 59.1 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 8.50 | 20.18 | 31.32 | 3.00 | 119.7 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.05 | 17.02 | 26.25 | 2.00 | 100.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 5.05 | 12.92 | 20.68 | 3.00 | 94.6 | 90.0 |
| Bench 2 | Bench | Mohamed Salah | MID | 11 | 13.2 | 3.04 | 11.62 | 21.58 | 0.00 | 26.5 | 0.0 |
| Bench 3 | Autosub In | Lewis Miley | MID | 15 | 4.5 | 2.30 | 7.32 | 12.25 | 2.00 | 62.9 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 2.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Julián Álvarez
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 62.54
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.48) beats the best remaining Triple Captain opportunity (7.69).
- Transfer: Jordan Beyer -> Gabriel dos Santos Magalhães (projected gain 2.91, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.48) beats the best remaining Triple Captain opportunity (7.69).
- Autosub: Jan Paul van Hecke replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.23 | 9.35 | 15.63 | 3.00 | 79.2 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.69 | 3.60 | 5.66 | 0.00 | 35.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.46 | 12.64 | 20.80 | 1.00 | 86.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.47 | 11.51 | 18.32 | 2.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.48 | 10.90 | 17.19 | 2.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.26 | 8.37 | 15.20 | 1.00 | 28.8 | 22.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.0 | 3.11 | 8.16 | 13.02 | 0.00 | 83.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.50 | 14.32 | 23.42 | 7.00 | 74.1 | 90.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 6.9 | 6.05 | 13.00 | 19.85 | 13.00 | 76.0 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.99 | 10.86 | 17.01 | 2.00 | 71.7 | 70.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.48 | 17.10 | 27.05 | 10.00 | 82.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.86 | 12.21 | 18.90 | 6.00 | 54.0 | 76.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.80 | 11.14 | 18.07 | 2.00 | 74.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.25 | 11.07 | 20.80 | 0.00 | 15.1 | 0.0 |
| Bench 3 | Bench | Lewis Miley | MID | 15 | 4.5 | 2.40 | 7.44 | 12.41 | 2.00 | 72.0 | 74.0 |

## GW23

- Train rows: 120213
- Bank: 1.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 62.12
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.97) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Stefan Ortega Moreno -> Martin Dubravka (projected gain 1.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.97) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 4.26 | 10.35 | 17.01 | 1.00 | 111.9 | 90.0 |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.2 | 2.47 | 8.88 | 14.78 | 1.00 | 73.6 | 45.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.90 | 11.84 | 19.59 | 1.00 | 83.3 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 5.6 | 3.18 | 10.20 | 16.64 | 1.00 | 80.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.24 | 10.07 | 16.14 | -1.00 | 84.4 | 90.0 |
| Bench 4 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.36 | 9.49 | 16.44 | 1.00 | 43.2 | 57.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 3.25 | 8.18 | 13.04 | 2.00 | 79.6 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.72 | 16.16 | 26.08 | 18.00 | 91.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.95 | 12.67 | 20.89 | 2.00 | 64.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.18 | 9.14 | 15.41 | 8.00 | 51.8 | 87.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.40 | 16.62 | 26.73 | 9.00 | 84.6 | 78.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.18 | 12.52 | 21.85 | 0.00 | 33.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.25 | 12.50 | 20.65 | 20.00 | 62.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.10 | 11.40 | 18.45 | 11.00 | 79.9 | 90.0 |
| Bench 3 | Bench Boost | Lewis Miley | MID | 15 | 4.5 | 2.97 | 7.05 | 11.23 | 5.00 | 69.6 | 90.0 |
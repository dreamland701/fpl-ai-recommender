# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 238.29
- Total actual points: 292.00
- Average predicted points: 59.57
- Average actual points: 73.00
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
- Predicted score: 61.51
- Actual score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.26 | 8.81 | 14.53 | 11.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.38 | 0.23 | 0.56 | 0.00 | 4.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.21 | 15.66 | 25.19 | 0.00 | 88.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.02 | 13.02 | 20.74 | 2.00 | 86.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.21 | 11.56 | 18.60 | 0.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.56 | 7.45 | 11.81 | 8.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.06 | 6.76 | 11.09 | 1.00 | 79.6 | 16.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.78 | 16.32 | 25.90 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.24 | 14.19 | 21.77 | 7.00 | 80.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.16 | 11.25 | 17.38 | 2.00 | 77.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.29 | 20.65 | 33.82 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.49 | 17.38 | 28.50 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.68 | 16.34 | 26.54 | 7.00 | 88.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.90 | 11.94 | 19.54 | 3.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Lewis Miley | MID | 15 | 4.5 | 2.62 | 8.51 | 13.85 | 0.00 | 72.9 | 53.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 59.88
- Actual score: 39.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 9.06, hit 0)
- Autosub: Jan Paul van Hecke replaced Trent Alexander-Arnold.
- Autosub: Lewis Miley replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.01 | 10.78 | 17.70 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.03 | 0.14 | 0.46 | 2.00 | 2.0 | 82.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.36 | 13.00 | 21.41 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.70 | 12.40 | 19.47 | 6.00 | 87.9 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.26 | 12.04 | 20.12 | 0.00 | 64.8 | 0.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.71 | 7.92 | 12.63 | 6.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.74 | 5.29 | 8.89 | 0.00 | 48.4 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.59 | 16.11 | 25.87 | 1.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.55 | 12.81 | 19.37 | 2.00 | 81.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.29 | 12.34 | 19.64 | 2.00 | 67.9 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.84 | 20.18 | 31.32 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.22 | 16.93 | 26.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.38 | 12.95 | 20.72 | 3.00 | 83.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.82 | 11.70 | 21.70 | 0.00 | 25.8 | 0.0 |
| Bench 3 | Autosub In | Lewis Miley | MID | 15 | 4.5 | 2.44 | 7.23 | 12.11 | 2.00 | 62.4 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 2.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.21
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (7.06).
- Transfer: Jordan Beyer -> Gabriel dos Santos Magalhães (projected gain 2.84, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (7.06).
- Autosub: Jan Paul van Hecke replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.28 | 9.39 | 15.70 | 3.00 | 82.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.8 | 1.57 | 3.60 | 5.66 | 0.00 | 33.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.17 | 12.65 | 20.83 | 1.00 | 83.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.25 | 11.53 | 18.34 | 2.00 | 82.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.05 | 10.91 | 17.20 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.03 | 8.38 | 15.21 | 1.00 | 28.3 | 22.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.69 | 8.18 | 13.06 | 0.00 | 75.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.85 | 14.31 | 23.41 | 7.00 | 80.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.53 | 13.01 | 19.86 | 13.00 | 55.7 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.58 | 10.88 | 17.05 | 2.00 | 68.3 | 70.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.23 | 17.12 | 27.08 | 10.00 | 80.5 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.69 | 12.21 | 18.90 | 6.00 | 36.0 | 76.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.42 | 11.17 | 18.11 | 2.00 | 69.3 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 2.69 | 11.08 | 20.81 | 0.00 | 12.2 | 0.0 |
| Bench 3 | Bench | Lewis Miley | MID | 15 | 4.5 | 2.45 | 7.39 | 12.33 | 2.00 | 72.2 | 74.0 |

## GW23

- Train rows: 120213
- Bank: 1.00 -> 2.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 59.69
- Actual score: 104.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.79) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> Kieran Trippier (projected gain 3.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.93 | 8.85 | 14.74 | 1.00 | 84.9 | 45.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.8 | 0.41 | 1.28 | 2.18 | 0.00 | 9.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.41 | 12.74 | 20.48 | 9.00 | 79.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.88 | 11.87 | 19.64 | 1.00 | 82.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.43 | 10.16 | 16.59 | 1.00 | 82.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.09 | 10.03 | 16.07 | -1.00 | 79.2 | 90.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.98 | 8.18 | 13.04 | 2.00 | 74.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.72 | 16.18 | 26.11 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.63 | 12.70 | 20.94 | 2.00 | 66.4 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.06 | 9.15 | 15.42 | 8.00 | 51.0 | 87.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.60 | 16.59 | 26.69 | 9.00 | 86.5 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.07 | 12.52 | 20.69 | 20.00 | 61.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.53 | 12.46 | 21.76 | 0.00 | 36.5 | 0.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.89 | 11.41 | 18.47 | 11.00 | 76.0 | 90.0 |
| Bench 4 | Bench Boost | Lewis Miley | MID | 15 | 4.5 | 2.34 | 7.06 | 11.26 | 5.00 | 56.7 | 90.0 |
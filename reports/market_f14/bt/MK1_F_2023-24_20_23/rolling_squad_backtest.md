# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 235.84
- Total actual points: 288.00
- Average predicted points: 58.96
- Average actual points: 72.00
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
- Predicted score: 61.54
- Actual score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.36 | 8.74 | 14.44 | 11.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.23 | 0.53 | 1.18 | 0.00 | 10.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.15 | 15.68 | 25.22 | 0.00 | 88.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.11 | 12.96 | 20.65 | 2.00 | 86.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.16 | 11.60 | 18.65 | 0.00 | 89.9 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.52 | 7.47 | 11.84 | 8.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.03 | 6.78 | 11.11 | 1.00 | 79.6 | 16.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.81 | 16.30 | 25.87 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.19 | 14.20 | 21.79 | 7.00 | 80.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.14 | 11.26 | 17.40 | 2.00 | 77.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.25 | 20.67 | 33.85 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.59 | 17.31 | 28.41 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.65 | 16.35 | 26.57 | 7.00 | 88.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.87 | 11.96 | 19.56 | 3.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Lewis Miley | MID | 15 | 4.5 | 2.53 | 8.57 | 13.94 | 0.00 | 72.9 | 53.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 59.96
- Actual score: 39.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 9.19, hit 0)
- Autosub: Jan Paul van Hecke replaced Trent Alexander-Arnold.
- Autosub: Lewis Miley replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.05 | 10.76 | 17.66 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.31 | 0.72 | 1.45 | 0.00 | 8.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.29 | 13.04 | 21.47 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.69 | 12.40 | 19.47 | 6.00 | 87.9 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.38 | 11.98 | 20.02 | 0.00 | 64.9 | 0.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.74 | 7.90 | 12.59 | 6.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.78 | 5.27 | 8.86 | 0.00 | 48.4 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.69 | 16.05 | 25.79 | 1.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.59 | 12.78 | 19.32 | 2.00 | 81.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.14 | 12.42 | 19.76 | 2.00 | 67.8 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.84 | 20.18 | 31.32 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.06 | 17.02 | 26.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.42 | 12.92 | 20.68 | 3.00 | 83.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.96 | 11.62 | 21.58 | 0.00 | 25.9 | 0.0 |
| Bench 3 | Autosub In | Lewis Miley | MID | 15 | 4.5 | 2.28 | 7.32 | 12.25 | 2.00 | 62.3 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 2.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 58.32
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.35) beats the best remaining Bench Boost opportunity (8.12).
- Transfer: Jordan Beyer -> Kyle Walker (projected gain 3.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.35) beats the best remaining Bench Boost opportunity (8.12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.36 | 9.35 | 15.63 | 3.00 | 82.1 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.22 | 0.46 | 1.18 | 0.00 | 7.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.20 | 12.64 | 20.80 | 1.00 | 83.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.27 | 11.51 | 18.32 | 2.00 | 82.3 | 90.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.4 | 3.81 | 11.20 | 17.38 | 0.00 | 68.0 | 0.0 |
| Bench 4 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.05 | 8.37 | 15.20 | 1.00 | 28.3 | 22.0 |
| Bench 2 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.71 | 8.16 | 13.02 | 0.00 | 75.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.83 | 14.32 | 23.42 | 7.00 | 80.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.52 | 13.00 | 19.85 | 13.00 | 55.7 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.61 | 10.86 | 17.01 | 2.00 | 68.3 | 70.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.26 | 17.10 | 27.05 | 10.00 | 80.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.66 | 12.21 | 18.90 | 6.00 | 36.0 | 76.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.47 | 11.14 | 18.07 | 2.00 | 69.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.1 | 2.73 | 11.07 | 20.80 | 0.00 | 12.2 | 0.0 |
| Bench 3 | Bench Boost | Lewis Miley | MID | 15 | 4.5 | 2.37 | 7.44 | 12.41 | 2.00 | 72.1 | 74.0 |

## GW23

- Train rows: 120213
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 56.02
- Actual score: 109.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.75) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Kyle Walker -> Fabian Schär (projected gain 2.78, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (5.75) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Jan Paul van Hecke replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.89 | 8.88 | 14.78 | 1.00 | 84.8 | 45.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.08 | 0.36 | 0.00 | 0.8 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.94 | 11.84 | 19.59 | 1.00 | 82.8 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.3 | 3.83 | 10.88 | 17.41 | 0.00 | 86.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.37 | 10.20 | 16.64 | 1.00 | 82.5 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.64 | 9.49 | 16.44 | 1.00 | 48.1 | 57.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.98 | 8.18 | 13.04 | 2.00 | 74.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.75 | 16.16 | 26.08 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.67 | 12.67 | 20.89 | 2.00 | 66.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.07 | 9.14 | 15.41 | 8.00 | 51.0 | 87.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.55 | 16.62 | 26.73 | 9.00 | 86.5 | 78.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.0 | 3.43 | 12.52 | 21.85 | 0.00 | 36.5 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.11 | 12.50 | 20.65 | 20.00 | 61.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.92 | 11.40 | 18.45 | 11.00 | 76.0 | 90.0 |
| Bench 4 | Bench | Lewis Miley | MID | 15 | 4.5 | 2.37 | 7.05 | 11.23 | 5.00 | 56.7 | 90.0 |
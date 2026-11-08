# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 237.97
- Total actual points: 299.00
- Average predicted points: 59.49
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
- Predicted score: 60.25
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.58 | 9.28 | 15.02 | 11.00 | 78.6 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.26 | 0.96 | 1.82 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.59 | 16.18 | 25.83 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.33 | 12.78 | 20.40 | 2.00 | 88.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.01 | 11.22 | 18.09 | 0.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 2.29 | 7.35 | 11.72 | 1.00 | 79.6 | 16.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.45 | 6.99 | 11.16 | 8.00 | 79.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.86 | 16.03 | 25.43 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.04 | 13.98 | 21.71 | 7.00 | 84.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.07 | 12.72 | 20.36 | 2.00 | 76.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 6.69 | 17.48 | 31.50 | 16.00 | 86.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.43 | 16.13 | 26.22 | 7.00 | 86.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.18 | 15.25 | 24.54 | 3.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.80 | 11.55 | 18.96 | 3.00 | 83.7 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 3.75 | 9.80 | 15.76 | 4.00 | 77.0 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 5.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.41
- Actual score: 39.00
- Transfer: Mohamed Salah -> Phil Foden (projected gain 8.73, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.88 | 10.57 | 17.46 | 3.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.43 | 1.15 | 2.17 | 0.00 | 13.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.50 | 13.45 | 21.65 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.05 | 10.99 | 17.80 | 6.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.11 | 10.20 | 17.97 | 0.00 | 43.4 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.56 | 7.07 | 11.66 | 6.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Jordan Beyer | DEF | 6 | 4.0 | 1.13 | 4.42 | 7.93 | 0.00 | 35.9 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.00 | 16.94 | 26.65 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.25 | 12.91 | 20.17 | 2.00 | 68.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.89 | 12.66 | 20.41 | 2.00 | 75.4 | 82.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.25 | 19.36 | 30.48 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.11 | 17.44 | 26.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 5.00 | 14.11 | 22.81 | 3.00 | 85.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.68 | 10.62 | 20.33 | 2.00 | 64.9 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.88 | 8.82 | 13.91 | 2.00 | 72.0 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 5.40 -> 2.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.62
- Actual score: 80.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.94) beats the best remaining Triple Captain opportunity (6.74).
- Transfer: Jordan Beyer -> Kieran Trippier (projected gain 3.09, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.94) beats the best remaining Triple Captain opportunity (6.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.38 | 9.40 | 15.74 | 3.00 | 78.6 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.43 | 1.09 | 2.15 | 0.00 | 12.8 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.29 | 12.61 | 20.77 | 1.00 | 81.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.91 | 10.75 | 17.43 | 2.00 | 81.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.42 | 10.52 | 17.91 | 7.00 | 72.1 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.18 | 9.82 | 15.74 | 1.00 | 31.1 | 22.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.57 | 7.53 | 12.30 | 0.00 | 76.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.04 | 14.70 | 23.85 | 7.00 | 78.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.37 | 12.86 | 20.39 | 13.00 | 62.2 | 86.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.51 | 11.40 | 18.28 | 8.00 | 66.5 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.94 | 16.80 | 26.82 | 10.00 | 78.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.92 | 12.11 | 20.72 | 1.00 | 64.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.57 | 11.94 | 19.02 | 6.00 | 43.8 | 76.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 3.39 | 10.92 | 17.89 | 2.00 | 70.2 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.8 | 2.69 | 8.30 | 13.82 | 1.00 | 69.7 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 2.70 -> 1.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 62.68
- Actual score: 105.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.32) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alejandro Garnacho -> Cole Palmer (projected gain 1.59, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.32) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.20 | 9.61 | 15.59 | 1.00 | 83.7 | 45.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.28 | 0.77 | 0.00 | 1.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.41 | 12.58 | 20.25 | 9.00 | 81.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.10 | 12.07 | 19.72 | 1.00 | 82.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.53 | 10.38 | 16.71 | 1.00 | 83.4 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.79 | 10.05 | 17.14 | 1.00 | 45.9 | 57.0 |
| Bench 4 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.77 | 7.74 | 12.55 | 2.00 | 77.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.81 | 16.24 | 26.08 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 3.86 | 13.34 | 22.63 | 2.00 | 66.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.45 | 12.49 | 20.22 | 2.00 | 76.1 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.59 | 16.68 | 26.66 | 9.00 | 86.5 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.38 | 13.02 | 21.39 | 20.00 | 66.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.28 | 12.71 | 20.32 | 8.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.96 | 11.95 | 20.52 | 2.00 | 74.5 | 90.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 5 | 6.4 | 3.77 | 11.23 | 18.29 | 11.00 | 79.6 | 90.0 |
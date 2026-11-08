# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 241.54
- Total actual points: 237.00
- Average predicted points: 60.39
- Average actual points: 59.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.57
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: João Pedro Junqueira de Jesus replaced Bryan Mbeumo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.31 | 9.53 | 16.45 | 1.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.01 | 8.64 | 14.13 | 10.00 | 84.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.94 | 15.19 | 25.12 | -1.00 | 95.1 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 4.55 | 13.66 | 22.89 | 4.00 | 87.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.77 | 11.66 | 19.05 | 2.00 | 86.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.94 | 11.46 | 19.01 | 5.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 8 | 5.2 | 3.20 | 9.67 | 15.83 | 0.00 | 82.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.71 | 10.26 | 16.79 | 9.00 | 82.5 | 90.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 3.49 | 9.81 | 15.98 | 2.00 | 63.6 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 3.16 | 8.82 | 13.94 | 2.00 | 59.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.23 | 19.02 | 31.62 | 13.00 | 84.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.44 | 16.42 | 26.66 | 2.00 | 87.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.19 | 15.57 | 25.77 | 17.00 | 90.8 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | 4 | 7.1 | 4.62 | 13.82 | 22.52 | 0.00 | 71.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.3 | 3.65 | 11.19 | 19.42 | 1.00 | 76.3 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.31
- Actual score: 58.00
- Transfer: Bryan Mbeumo -> Pascal Groß (projected gain 2.60, hit 0)
- Autosub: Neal Maupay replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.77 | 9.33 | 15.54 | 10.00 | 86.6 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.10 | 8.95 | 14.84 | 6.00 | 83.8 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 7.0 | 4.87 | 14.22 | 23.96 | 0.00 | 92.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 4.44 | 13.41 | 22.58 | 9.00 | 83.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.13 | 11.83 | 19.61 | 8.00 | 82.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.03 | 11.72 | 19.07 | 7.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 8 | 5.1 | 2.56 | 8.54 | 14.12 | 0.00 | 79.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.70 | 11.04 | 17.96 | 2.00 | 85.5 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 3.28 | 10.33 | 16.59 | 1.00 | 65.5 | 30.0 |
| Bench 2 | Autosub In | Neal Maupay | FWD | 4 | 4.9 | 3.32 | 9.30 | 14.62 | 0.00 | 71.3 | 22.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.58 | 19.89 | 32.98 | 3.00 | 94.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.94 | 17.32 | 27.83 | 3.00 | 90.2 | 88.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.79 | 16.84 | 28.41 | 2.00 | 96.8 | 87.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.3 | 3.56 | 11.83 | 19.56 | 1.00 | 83.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.3 | 3.60 | 10.59 | 17.78 | 14.00 | 70.7 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.20
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.21) beats the best remaining Triple Captain opportunity (7.49).
- Transfer: Kieran Trippier -> Virgil van Dijk (projected gain 2.23, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.21) beats the best remaining Triple Captain opportunity (7.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.37 | 10.32 | 17.46 | 2.00 | 91.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.85 | 9.11 | 15.13 | 2.00 | 84.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.56 | 14.02 | 23.35 | 5.00 | 84.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.61 | 12.76 | 20.52 | 2.00 | 81.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.68 | 11.58 | 18.83 | 2.00 | 89.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.49 | 10.83 | 17.74 | 2.00 | 86.6 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | 8 | 5.0 | 3.02 | 8.61 | 14.00 | 2.00 | 77.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.68 | 10.81 | 17.55 | 1.00 | 77.8 | 85.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.99 | 8.87 | 14.91 | 2.00 | 46.2 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 1.02 | 4.82 | 8.77 | 0.00 | 21.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 5.90 | 18.78 | 31.20 | 7.00 | 85.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.46 | 17.01 | 27.21 | 1.00 | 87.2 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.6 | 5.76 | 16.81 | 27.20 | 7.00 | 83.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 4.76 | 13.39 | 21.63 | 1.00 | 93.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.3 | 4.14 | 12.41 | 20.40 | 7.00 | 85.4 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.47
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.47) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Virgil van Dijk -> Kieran Trippier (projected gain 3.38, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.47) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.38 | 10.15 | 16.96 | 1.00 | 92.6 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 2.64 | 8.76 | 14.71 | 2.00 | 81.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.72 | 14.20 | 23.59 | 8.00 | 85.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.67 | 13.64 | 22.53 | 1.00 | 79.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.22 | 12.52 | 20.07 | 5.00 | 84.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.98 | 11.11 | 18.06 | 1.00 | 87.5 | 90.0 |
| Bench 3 | Bench Boost | Joachim Andersen | DEF | 8 | 5.0 | 2.81 | 8.35 | 13.60 | 1.00 | 78.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.65 | 10.65 | 17.52 | 5.00 | 73.4 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 3.44 | 9.80 | 15.81 | 16.00 | 68.3 | 90.0 |
| Bench 4 | Bench Boost | Neal Maupay | FWD | 4 | 4.9 | 1.58 | 4.67 | 8.12 | 5.00 | 29.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.45 | 19.31 | 32.50 | 3.00 | 91.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.69 | 17.15 | 28.29 | 5.00 | 94.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.71 | 16.12 | 26.03 | 2.00 | 83.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 4.80 | 13.96 | 22.23 | 0.00 | 85.5 | 0.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.3 | 4.26 | 12.33 | 20.46 | 2.00 | 84.8 | 90.0 |
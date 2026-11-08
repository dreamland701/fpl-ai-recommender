# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 241.49
- Total actual points: 233.00
- Average predicted points: 60.37
- Average actual points: 58.25
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
- Predicted score: 55.54
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.62 | 16.27 | 1.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.99 | 8.66 | 14.11 | 10.00 | 84.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.97 | 15.23 | 25.02 | -1.00 | 95.1 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 4.54 | 13.63 | 22.75 | 4.00 | 87.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.73 | 11.52 | 18.83 | 2.00 | 86.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.96 | 11.44 | 19.01 | 5.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Joachim Andersen | DEF | 8 | 5.2 | 3.20 | 9.66 | 15.78 | 0.00 | 82.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.74 | 10.42 | 16.78 | 9.00 | 82.4 | 90.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 3.48 | 9.81 | 15.75 | 2.00 | 63.6 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 3.19 | 8.77 | 13.88 | 2.00 | 59.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.22 | 18.80 | 31.25 | 13.00 | 84.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.40 | 16.34 | 26.39 | 2.00 | 87.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.21 | 15.51 | 25.67 | 17.00 | 90.8 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | 4 | 7.1 | 4.65 | 13.59 | 22.20 | 0.00 | 71.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.3 | 3.64 | 11.13 | 19.38 | 1.00 | 76.3 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.35
- Actual score: 58.00
- Transfer: Bryan Mbeumo -> Pascal Groß (projected gain 2.79, hit 0)
- Autosub outfielders: Neal Maupay.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.77 | 9.30 | 15.44 | 10.00 | 86.6 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.08 | 8.84 | 14.63 | 6.00 | 83.8 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 7.0 | 4.87 | 14.25 | 23.90 | 0.00 | 92.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.45 | 13.44 | 22.59 | 9.00 | 83.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.15 | 11.91 | 19.58 | 8.00 | 82.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.00 | 11.46 | 18.70 | 7.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 8 | 5.1 | 2.57 | 8.55 | 14.10 | 0.00 | 79.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.74 | 11.07 | 17.91 | 2.00 | 85.4 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.23 | 10.10 | 16.23 | 1.00 | 65.6 | 30.0 |
| Bench 2 | Autosub In | Neal Maupay | FWD | 4 | 4.9 | 3.28 | 9.11 | 14.36 | 0.00 | 71.3 | 22.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.59 | 19.67 | 32.44 | 3.00 | 94.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.92 | 17.10 | 27.37 | 3.00 | 90.2 | 88.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.81 | 16.87 | 28.15 | 2.00 | 96.8 | 87.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.3 | 3.52 | 11.84 | 19.56 | 1.00 | 83.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.62 | 10.60 | 17.76 | 14.00 | 70.7 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.02
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.16) beats the best remaining Triple Captain opportunity (7.43).
- Transfer: Kieran Trippier -> Virgil van Dijk (projected gain 2.16, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.16) beats the best remaining Triple Captain opportunity (7.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.40 | 10.31 | 17.25 | 2.00 | 91.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.89 | 9.11 | 15.06 | 2.00 | 84.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 4.52 | 13.95 | 23.18 | 5.00 | 84.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.61 | 12.81 | 20.51 | 2.00 | 81.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.68 | 11.41 | 18.50 | 2.00 | 89.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.45 | 10.68 | 17.49 | 2.00 | 86.6 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | 8 | 5.0 | 3.00 | 8.53 | 13.97 | 2.00 | 77.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.66 | 10.66 | 17.16 | 1.00 | 77.8 | 85.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.97 | 8.79 | 14.49 | 2.00 | 46.2 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 1.02 | 4.78 | 8.68 | 0.00 | 21.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 5.85 | 18.50 | 30.59 | 7.00 | 85.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.47 | 16.77 | 26.64 | 1.00 | 87.2 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.7 | 5.75 | 16.76 | 26.91 | 7.00 | 83.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.81 | 13.54 | 21.80 | 1.00 | 93.8 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.13 | 12.36 | 20.25 | 7.00 | 85.4 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 1.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.58
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.51) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Dominic Solanke (projected gain 4.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.51) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.35 | 10.03 | 16.76 | 1.00 | 92.6 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 2.64 | 8.74 | 14.63 | 2.00 | 81.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 4.70 | 14.11 | 23.32 | 8.00 | 85.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.5 | 4.20 | 12.44 | 19.91 | 5.00 | 84.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.02 | 11.11 | 17.95 | 1.00 | 87.4 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.2 | 3.45 | 10.20 | 16.76 | 7.00 | 81.1 | 90.0 |
| Bench 3 | Bench Boost | Joachim Andersen | DEF | 8 | 5.0 | 2.80 | 8.27 | 13.43 | 1.00 | 78.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.8 | 4.82 | 14.05 | 21.02 | 6.00 | 80.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.62 | 10.60 | 17.38 | 5.00 | 73.4 | 90.0 |
| Bench 4 | Bench Boost | Neal Maupay | FWD | 4 | 4.9 | 1.62 | 4.82 | 8.22 | 5.00 | 29.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.43 | 19.22 | 32.08 | 3.00 | 91.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 5.67 | 17.01 | 27.86 | 5.00 | 94.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.75 | 16.10 | 25.69 | 2.00 | 83.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 4.79 | 13.89 | 21.94 | 0.00 | 85.5 | 0.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.29 | 12.37 | 20.35 | 2.00 | 84.7 | 90.0 |
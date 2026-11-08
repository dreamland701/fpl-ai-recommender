# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 239.65
- Total actual points: 234.00
- Average predicted points: 59.91
- Average actual points: 58.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.46
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cole Palmer replaced Bryan Mbeumo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 3.15 | 9.17 | 15.85 | 1.00 | 86.8 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.28 | 9.07 | 14.74 | 10.00 | 84.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.88 | 15.02 | 24.80 | -1.00 | 93.1 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 4.55 | 13.76 | 23.07 | 4.00 | 88.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.55 | 11.20 | 18.31 | 2.00 | 83.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.92 | 11.08 | 17.97 | 2.00 | 88.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.74 | 10.94 | 18.19 | 5.00 | 80.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 3.69 | 10.41 | 16.71 | 2.00 | 61.9 | 90.0 |
| Bench 3 | Bench | Neal Maupay | FWD | 4 | 4.9 | 3.16 | 9.27 | 14.31 | 2.00 | 55.8 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.90 | 7.84 | 12.58 | 2.00 | 70.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.33 | 19.38 | 32.22 | 13.00 | 87.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.30 | 15.90 | 25.95 | 2.00 | 87.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.17 | 15.53 | 25.78 | 17.00 | 92.0 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | 4 | 7.1 | 4.73 | 14.39 | 23.20 | 0.00 | 69.2 | 0.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.3 | 3.39 | 10.79 | 18.69 | 1.00 | 73.9 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.52
- Actual score: 63.00
- Transfer: Bryan Mbeumo -> Bernardo Veiga de Carvalho e Silva (projected gain 1.03, hit 0)
- Autosub: Virgil van Dijk replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.66 | 9.19 | 15.37 | 10.00 | 85.6 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.18 | 8.85 | 14.57 | 6.00 | 82.6 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 7.0 | 5.21 | 15.00 | 25.14 | 0.00 | 94.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.0 | 4.35 | 13.58 | 22.97 | 9.00 | 85.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.13 | 11.72 | 19.38 | 8.00 | 81.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.87 | 11.34 | 18.47 | 7.00 | 81.8 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.1 | 3.51 | 10.64 | 17.46 | 6.00 | 84.7 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 2.95 | 9.65 | 15.52 | 1.00 | 61.5 | 30.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.96 | 8.65 | 13.70 | 2.00 | 71.1 | 90.0 |
| XI | XI | Neal Maupay | FWD | 4 | 4.9 | 3.04 | 8.41 | 13.25 | 0.00 | 68.6 | 22.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.53 | 20.24 | 33.61 | 3.00 | 96.9 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.6 | 5.94 | 17.14 | 28.81 | 2.00 | 97.3 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.83 | 17.03 | 27.37 | 3.00 | 88.8 | 88.0 |
| XI | XI | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.4 | 4.15 | 11.55 | 18.54 | 2.00 | 86.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.3 | 3.76 | 10.76 | 18.06 | 14.00 | 72.1 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 59.06
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.22) beats the best remaining Triple Captain opportunity (7.50).
- Transfer: João Pedro Junqueira de Jesus -> Matheus Santos Carneiro Da Cunha (projected gain 3.25, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.22) beats the best remaining Triple Captain opportunity (7.50).
- Autosub: Kieran Trippier replaced Bernardo Veiga de Carvalho e Silva.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.37 | 10.17 | 17.17 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.61 | 8.56 | 14.25 | 2.00 | 82.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.44 | 14.01 | 23.49 | 5.00 | 86.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.35 | 11.75 | 18.86 | 2.00 | 81.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.48 | 11.04 | 17.95 | 2.00 | 87.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.31 | 10.50 | 17.26 | 2.00 | 85.9 | 90.0 |
| Bench 2 | Autosub In | Kieran Trippier | DEF | 15 | 6.9 | 2.77 | 9.36 | 17.09 | 2.00 | 41.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.92 | 11.25 | 18.13 | 1.00 | 76.3 | 85.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.57 | 7.64 | 12.25 | 8.00 | 73.8 | 89.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 1.01 | 4.77 | 8.70 | 0.00 | 20.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 5.91 | 19.04 | 31.72 | 7.00 | 88.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.36 | 16.41 | 26.22 | 1.00 | 87.2 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.6 | 5.68 | 16.24 | 26.26 | 7.00 | 87.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 4.55 | 12.65 | 20.38 | 1.00 | 91.4 | 90.0 |
| XI | Bench | Bernardo Veiga de Carvalho e Silva | MID | 13 | 6.4 | 2.86 | 9.68 | 16.25 | 0.00 | 62.7 | 0.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.62
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.67) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bernardo Veiga de Carvalho e Silva -> Pascal Groß (projected gain 1.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.67) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.13 | 9.59 | 16.10 | 1.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 2.45 | 8.34 | 14.06 | 2.00 | 80.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.90 | 14.59 | 24.18 | 8.00 | 86.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.64 | 13.48 | 22.25 | 1.00 | 78.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.09 | 12.13 | 19.45 | 5.00 | 83.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.98 | 11.06 | 17.99 | 1.00 | 86.7 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.1 | 3.52 | 10.36 | 17.09 | 7.00 | 81.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.54 | 10.36 | 17.04 | 5.00 | 70.4 | 90.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 3.29 | 8.92 | 14.44 | 5.00 | 77.2 | 85.0 |
| Bench 4 | Bench Boost | Neal Maupay | FWD | 4 | 4.9 | 1.41 | 4.29 | 7.53 | 5.00 | 26.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.78 | 20.12 | 33.77 | 3.00 | 95.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.68 | 17.06 | 28.16 | 5.00 | 96.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.82 | 16.36 | 26.34 | 2.00 | 83.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 4.53 | 13.24 | 21.11 | 0.00 | 82.0 | 0.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.10 | 11.69 | 19.40 | 2.00 | 84.1 | 90.0 |
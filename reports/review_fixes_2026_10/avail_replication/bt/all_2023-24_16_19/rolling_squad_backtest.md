# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 208.09
- Total actual points: 224.00
- Average predicted points: 52.02
- Average actual points: 56.00
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
- Predicted score: 50.15
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.15 | 8.11 | 12.64 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.86 | 7.32 | 12.44 | 1.00 | 90.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.49 | 12.83 | 21.38 | 4.00 | 91.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 3.77 | 10.90 | 18.44 | -1.00 | 75.6 | 85.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.5 | 2.76 | 8.75 | 14.10 | 2.00 | 83.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.03 | 8.74 | 14.49 | 5.00 | 80.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.06 | 8.55 | 13.83 | 2.00 | 84.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.03 | 8.60 | 13.48 | 9.00 | 82.1 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.85 | 7.46 | 11.69 | 2.00 | 69.1 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.44 | 6.10 | 9.23 | 2.00 | 74.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.30 | 18.36 | 30.38 | 13.00 | 97.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.04 | 15.60 | 25.07 | 2.00 | 98.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.47 | 11.99 | 20.15 | 1.00 | 93.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.80 | 11.46 | 18.24 | 2.00 | 88.2 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 3.71 | 10.22 | 15.90 | 2.00 | 93.5 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 48.72
- Actual score: 63.00
- Transfer: Hwang Hee-chan -> Cole Palmer (projected gain 0.74, hit 0)
- Autosub: Cameron Archer replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.91 | 7.80 | 12.42 | 0.00 | 84.8 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 1.80 | 7.23 | 11.60 | 10.00 | 84.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 3.89 | 13.06 | 21.07 | 9.00 | 94.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.83 | 11.91 | 18.92 | 8.00 | 100.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.35 | 9.69 | 15.55 | 7.00 | 87.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 2.92 | 9.45 | 14.85 | 6.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Kieran Trippier | DEF | 15 | 6.9 | 2.31 | 8.91 | 16.40 | 0.00 | 48.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.88 | 9.16 | 14.94 | 2.00 | 82.1 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.02 | 7.13 | 10.81 | 1.00 | 61.8 | 30.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.40 | 6.19 | 9.62 | 2.00 | 74.4 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.01 | 20.48 | 32.96 | 3.00 | 110.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.12 | 16.16 | 25.80 | 3.00 | 101.2 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.24 | 9.64 | 15.35 | 6.00 | 78.2 | 83.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.3 | 2.53 | 9.40 | 15.91 | 0.00 | 74.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.04 | 8.81 | 15.00 | 14.00 | 75.3 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 51.04
- Actual score: 47.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.68) beats the best remaining Triple Captain opportunity (6.82).
- Transfer: Bruno Borges Fernandes -> Jarrod Bowen (projected gain 4.64, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (4.68) beats the best remaining Triple Captain opportunity (6.82).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.80 | 8.70 | 14.14 | 2.00 | 90.9 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.75 | 5.62 | 9.49 | 0.00 | 49.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 3.47 | 12.12 | 20.16 | 5.00 | 85.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.52 | 10.50 | 16.26 | 2.00 | 89.0 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 5.5 | 2.23 | 10.45 | 16.46 | 2.00 | 89.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.41 | 9.20 | 15.46 | 2.00 | 74.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 2.70 | 8.56 | 14.03 | 2.00 | 84.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.12 | 8.72 | 14.11 | 1.00 | 81.1 | 85.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.37 | 6.65 | 11.00 | 2.00 | 56.7 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.29 | 6.15 | 9.13 | 8.00 | 80.8 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 5.37 | 18.40 | 30.56 | 7.00 | 76.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 4.71 | 15.88 | 24.90 | 1.00 | 98.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.12 | 11.28 | 17.38 | 8.00 | 88.8 | 87.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.46 | 9.72 | 15.50 | 1.00 | 79.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.62 | 9.68 | 15.76 | 2.00 | 75.4 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.60 -> 1.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.19
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.51) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Virgil van Dijk -> Gabriel dos Santos Magalhães (projected gain 0.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.51) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.29 | 7.77 | 12.62 | 1.00 | 91.4 | 90.0 |
| Bench 1 | Bench Boost | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.60 | 5.19 | 8.67 | 2.00 | 34.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 3.96 | 12.81 | 21.32 | 8.00 | 100.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.54 | 10.53 | 18.23 | 1.00 | 62.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.34 | 10.53 | 16.21 | 5.00 | 84.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.51 | 9.78 | 15.23 | 1.00 | 93.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 4.9 | 3.14 | 8.75 | 13.76 | 1.00 | 89.6 | 90.0 |
| Bench 2 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 2.69 | 7.75 | 12.65 | 5.00 | 72.9 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.74 | 7.40 | 11.27 | 5.00 | 81.1 | 85.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.62 | 7.34 | 11.28 | 16.00 | 70.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.75 | 19.91 | 33.54 | 3.00 | 103.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 4.98 | 15.14 | 24.67 | 2.00 | 98.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 3.68 | 12.13 | 18.78 | 6.00 | 91.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.01 | 10.98 | 17.92 | 1.00 | 88.6 | 90.0 |
| Bench 4 | Bench Boost | Cole Palmer | MID | 7 | 5.5 | 2.60 | 9.13 | 14.98 | 0.00 | 68.2 | 0.0 |
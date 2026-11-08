# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 225.08
- Total actual points: 245.00
- Average predicted points: 56.27
- Average actual points: 61.25
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
- Predicted score: 57.51
- Actual score: 61.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 3.33 | 9.39 | 15.26 | 11.00 | 77.4 | 90.0 |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.62 | 9.07 | 15.15 | 1.00 | 83.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 4.91 | 16.06 | 25.74 | 0.00 | 89.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 3.27 | 12.97 | 20.74 | 2.00 | 83.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.19 | 11.23 | 18.19 | 0.00 | 83.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.82 | 11.08 | 17.97 | 1.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.37 | 9.42 | 15.12 | 1.00 | 84.1 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.03 | 10.84 | 16.81 | 2.00 | 80.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.48 | 9.87 | 15.59 | 2.00 | 70.2 | 90.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.77 | 7.63 | 12.53 | 2.00 | 63.5 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.39 | 21.08 | 34.44 | 16.00 | 88.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 6.51 | 17.59 | 28.90 | 9.00 | 86.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 4.00 | 16.37 | 26.65 | 7.00 | 85.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.27 | 15.25 | 24.61 | 3.00 | 90.4 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 4.64 | 9.73 | 15.73 | 4.00 | 84.7 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 55.41
- Actual score: 60.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.36, hit 0)
- Autosub: Chris Wood replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.40 | 11.06 | 18.07 | 3.00 | 84.2 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 1.85 | 7.80 | 13.04 | 2.00 | 67.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 3.50 | 13.78 | 22.23 | 6.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.50 | 12.09 | 20.26 | 0.00 | 71.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 4.22 | 11.33 | 17.91 | 6.00 | 85.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.37 | 11.30 | 18.15 | 6.00 | 83.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.89 | 9.60 | 15.58 | 17.00 | 84.5 | 80.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.52 | 12.57 | 19.17 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Autosub In | Chris Wood | FWD | 16 | 4.9 | 2.98 | 9.33 | 15.25 | 8.00 | 65.8 | 90.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.40 | 6.74 | 11.54 | 2.00 | 57.6 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.79 | 20.01 | 31.40 | 3.00 | 88.5 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 5.07 | 17.87 | 27.22 | 2.00 | 84.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.18 | 14.29 | 23.06 | 2.00 | 84.7 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 4.91 | 11.15 | 21.38 | 0.00 | 62.9 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.75 | 8.67 | 13.78 | 2.00 | 83.7 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.90
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Bukayo Saka
- Effective captain: Jarrod Bowen
- Chip used: triple_captain
- Predicted score: 55.56
- Actual score: 34.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.48) beats the best remaining Triple Captain opportunity (6.14).
- Transfer: Alejandro Garnacho -> Cole Palmer (projected gain 3.39, hit 0)
- Chip used: Triple Captain on Jarrod Bowen. Optimizer chose Triple Captain here because the current estimated captain upside (5.48) beats the best remaining Triple Captain opportunity (6.14).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.64 | 9.66 | 16.04 | 3.00 | 82.6 | 90.0 |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.78 | 8.09 | 13.51 | 1.00 | 82.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.72 | 12.90 | 21.15 | 1.00 | 84.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.89 | 10.88 | 17.56 | 2.00 | 83.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.81 | 10.11 | 16.31 | 2.00 | 79.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 4.13 | 9.95 | 16.05 | 2.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.14 | 8.81 | 15.88 | 1.00 | 61.0 | 22.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.93 | 10.78 | 16.92 | 2.00 | 85.7 | 70.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.27 | 9.01 | 14.63 | 1.00 | 77.0 | 45.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 4.9 | 4.05 | 6.97 | 11.80 | 2.00 | 77.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.41 | 17.07 | 27.21 | 10.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 11 | 13.1 | 2.42 | 11.72 | 22.02 | 0.00 | 20.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.26 | 11.65 | 18.57 | 6.00 | 72.9 | 76.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 8.0 | 5.48 | 11.63 | 19.95 | 1.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.62 | 11.16 | 17.13 | 2.00 | 87.5 | 84.0 |

## GW23

- Train rows: 120213
- Bank: 0.90 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Trent Alexander-Arnold
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 56.60
- Actual score: 90.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.29) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Chris Wood -> Matheus Santos Carneiro Da Cunha (projected gain 3.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.29) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.2 | 3.23 | 9.61 | 15.66 | 1.00 | 80.8 | 45.0 |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.93 | 7.93 | 12.80 | 8.00 | 87.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.07 | 12.16 | 19.95 | 1.00 | 82.2 | 90.0 |
| Bench 3 | Bench Boost | William Saliba | DEF | 1 | 5.6 | 2.62 | 10.32 | 16.71 | 1.00 | 87.9 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 4.18 | 9.82 | 16.75 | 1.00 | 60.0 | 57.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.23 | 9.65 | 15.82 | 1.00 | 85.1 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.56 | 9.65 | 15.55 | -1.00 | 85.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 3.65 | 9.96 | 16.18 | 17.00 | 75.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.69 | 8.62 | 14.81 | 8.00 | 48.7 | 87.0 |
| Bench 2 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.88 | 6.87 | 11.07 | 6.00 | 71.3 | 79.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 3.63 | 16.75 | 26.86 | 9.00 | 87.9 | 78.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.8 | 4.48 | 12.86 | 20.62 | 8.00 | 85.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.18 | 12.67 | 20.98 | 20.00 | 55.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 2.96 | 12.65 | 21.80 | 0.00 | 29.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.84 | 11.57 | 20.04 | 2.00 | 81.7 | 90.0 |
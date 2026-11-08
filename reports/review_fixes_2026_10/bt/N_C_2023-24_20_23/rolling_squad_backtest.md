# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 229.07
- Total actual points: 263.00
- Average predicted points: 57.27
- Average actual points: 65.75
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
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.97
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel dos Santos Magalhães replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.48 | 9.29 | 15.13 | 11.00 | 77.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.06 | 8.86 | 14.52 | 2.00 | 86.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.44 | 15.92 | 25.50 | 0.00 | 93.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.59 | 12.86 | 20.76 | 2.00 | 90.7 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.8 | 3.38 | 11.29 | 19.41 | 0.00 | 76.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.90 | 11.08 | 17.95 | 0.00 | 91.2 | 90.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.09 | 9.19 | 14.70 | 1.00 | 83.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.55 | 9.70 | 15.35 | 2.00 | 74.7 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.32 | 7.66 | 12.33 | 1.00 | 69.9 | 23.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.68 | 7.51 | 12.22 | 2.00 | 58.5 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.32 | 21.03 | 34.34 | 16.00 | 104.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 6.13 | 17.67 | 29.24 | 9.00 | 96.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.03 | 17.19 | 27.60 | 7.00 | 95.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.46 | 15.37 | 24.81 | 3.00 | 97.6 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 3.38 | 10.03 | 16.47 | 1.00 | 80.9 | 73.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 56.83
- Actual score: 53.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 6.85, hit 0)
- Autosub: Cameron Archer replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.14 | 11.18 | 18.13 | 3.00 | 97.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.81 | 8.16 | 13.52 | 9.00 | 86.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.80 | 13.78 | 22.13 | 6.00 | 102.5 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.76 | 12.33 | 20.57 | 0.00 | 67.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.24 | 11.46 | 18.31 | 6.00 | 92.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.47 | 9.78 | 15.77 | 17.00 | 88.8 | 80.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 2.66 | 8.66 | 15.42 | 1.00 | 49.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.21 | 9.22 | 14.76 | 8.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.06 | 7.06 | 11.96 | 2.00 | 55.8 | 90.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.17 | 6.46 | 10.68 | 1.00 | 48.4 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.79 | 20.05 | 31.39 | 3.00 | 119.7 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.81 | 17.78 | 26.87 | 2.00 | 116.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.24 | 14.69 | 23.49 | 2.00 | 93.1 | 90.0 |
| Bench 2 | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.41 | 11.78 | 22.31 | 0.00 | 19.8 | 0.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 2.91 | 8.50 | 14.12 | 1.00 | 71.8 | 27.0 |

## GW22

- Train rows: 119414
- Bank: 2.00 -> 1.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Pedro Porro
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 53.02
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.87) beats the best remaining Triple Captain opportunity (6.65).
- Transfer: Dwight McNeil -> Cole Palmer (projected gain 4.70, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.87) beats the best remaining Triple Captain opportunity (6.65).
- Autosub: Jean-Philippe Mateta replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.35 | 9.59 | 15.81 | 3.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.95 | 8.84 | 14.78 | 10.00 | 90.9 | 90.0 |
| Vice Captain | XI | Pedro Porro | DEF | 18 | 5.8 | 4.45 | 12.75 | 20.65 | 1.00 | 84.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.95 | 10.91 | 17.47 | 2.00 | 83.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.29 | 10.46 | 17.64 | 7.00 | 70.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.57 | 10.08 | 16.08 | 2.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.41 | 8.83 | 15.89 | 1.00 | 29.0 | 22.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 2.97 | 9.13 | 14.75 | 1.00 | 72.6 | 45.0 |
| Bench 2 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.52 | 6.86 | 11.48 | 2.00 | 60.6 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.86 | 5.88 | 9.90 | 1.00 | 40.2 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.87 | 16.79 | 26.50 | 10.00 | 79.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.75 | 11.74 | 19.89 | 1.00 | 59.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.66 | 11.69 | 18.43 | 6.00 | 42.7 | 76.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 3.55 | 11.55 | 17.86 | 2.00 | 55.7 | 84.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 2.88 | 11.41 | 21.71 | 0.00 | 11.5 | 0.0 |

## GW23

- Train rows: 120213
- Bank: 1.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Cole Palmer
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 59.24
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cameron Archer -> Matheus Santos Carneiro Da Cunha (projected gain 3.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.09 | 9.78 | 15.97 | 1.00 | 85.6 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 2.85 | 8.66 | 14.53 | 2.00 | 87.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.54 | 12.65 | 20.48 | 9.00 | 84.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.17 | 12.32 | 20.07 | 1.00 | 85.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.50 | 10.48 | 17.01 | 1.00 | 84.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.22 | 9.88 | 15.99 | -1.00 | 82.4 | 90.0 |
| Bench 2 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.79 | 9.84 | 16.88 | 1.00 | 47.9 | 57.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 3.30 | 10.07 | 16.30 | 17.00 | 74.7 | 90.0 |
| Bench 3 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.48 | 7.08 | 11.37 | 6.00 | 67.7 | 79.0 |
| Bench 4 | Bench Boost | Chris Wood | FWD | 16 | 4.9 | 1.82 | 6.83 | 12.09 | 0.00 | 38.7 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.89 | 17.16 | 27.75 | 9.00 | 91.3 | 78.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.8 | 4.61 | 13.10 | 21.00 | 8.00 | 87.2 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.48 | 12.57 | 21.76 | 0.00 | 35.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.94 | 12.39 | 20.36 | 20.00 | 61.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.66 | 11.73 | 20.19 | 2.00 | 69.6 | 90.0 |
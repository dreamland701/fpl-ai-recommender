# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 251.85
- Total actual points: 297.00
- Average predicted points: 62.96
- Average actual points: 74.25
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.42
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.51 | 9.39 | 15.26 | 11.00 | 78.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.08 | 9.00 | 14.65 | 2.00 | 87.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.75 | 16.06 | 25.74 | 0.00 | 94.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.54 | 12.97 | 20.74 | 2.00 | 92.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.95 | 11.23 | 18.19 | 0.00 | 91.6 | 90.0 |
| Bench 2 | Bench | Kieran Trippier | DEF | 15 | 6.8 | 3.27 | 11.05 | 18.90 | 0.00 | 72.7 | 0.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.15 | 9.42 | 15.12 | 1.00 | 84.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.24 | 10.84 | 16.81 | 2.00 | 80.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.69 | 9.87 | 15.59 | 2.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.43 | 7.82 | 12.52 | 1.00 | 71.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.57 | 21.08 | 34.44 | 16.00 | 103.5 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.92 | 17.59 | 28.90 | 9.00 | 96.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.50 | 16.37 | 26.65 | 7.00 | 89.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.34 | 15.25 | 24.61 | 3.00 | 96.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.84 | 9.73 | 15.73 | 4.00 | 76.0 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Cole Palmer
- Effective captain: Bukayo Saka
- Chip used: wildcard
- Predicted score: 68.57
- Actual score: 49.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Chip used: Wildcard — full rebuild projects +27.79 squad value (threshold 12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.12 | 11.06 | 18.07 | 3.00 | 95.5 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.44 | 9.50 | 14.93 | 6.00 | 82.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.86 | 13.78 | 22.23 | 6.00 | 102.8 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.5 | 3.55 | 12.09 | 20.26 | 0.00 | 66.1 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 4.09 | 11.33 | 17.91 | 6.00 | 91.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.20 | 11.30 | 18.15 | 6.00 | 91.5 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 5.0 | 4.62 | 10.91 | 16.09 | 8.00 | 88.0 | 71.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 6.15 | 17.13 | 27.02 | 1.00 | 101.7 | 90.0 |
| Bench 2 | Bench | Dominic Solanke | FWD | 3 | 7.1 | 4.13 | 12.77 | 20.49 | 2.00 | 79.2 | 82.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.97 | 12.57 | 19.17 | 2.00 | 90.7 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.89 | 20.01 | 31.40 | 3.00 | 119.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 6.95 | 17.87 | 27.22 | 2.00 | 116.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.7 | 7.19 | 16.94 | 25.66 | 10.00 | 118.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.1 | 5.08 | 14.29 | 23.06 | 2.00 | 89.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.64 | 12.66 | 20.47 | 3.00 | 90.2 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 0.00 -> 3.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.84
- Actual score: 64.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.21) beats the best remaining Triple Captain opportunity (7.04).
- Transfer: Trent Alexander-Arnold -> Kyle Walker (projected gain 0.30, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.21) beats the best remaining Triple Captain opportunity (7.04).
- Autosub: Virgil van Dijk replaced Kyle Walker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.45 | 9.66 | 16.04 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 2.99 | 8.57 | 13.68 | 2.00 | 71.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.61 | 12.90 | 21.15 | 1.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.99 | 10.88 | 17.56 | 2.00 | 84.1 | 90.0 |
| XI | Bench | Kyle Walker | DEF | 13 | 5.4 | 3.68 | 10.20 | 16.23 | 0.00 | 75.5 | 0.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.3 | 3.37 | 9.95 | 16.05 | 2.00 | 76.8 | 90.0 |
| Bench 3 | Bench | Pervis Estupiñán | DEF | 5 | 5.0 | 3.23 | 8.87 | 13.46 | 0.00 | 54.8 | 45.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.9 | 4.98 | 14.80 | 23.95 | 7.00 | 78.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.60 | 11.32 | 18.07 | 8.00 | 67.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.92 | 10.78 | 16.92 | 2.00 | 72.7 | 70.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 6.21 | 17.07 | 27.21 | 10.00 | 83.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.66 | 11.65 | 18.57 | 6.00 | 43.0 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.1 | 3.76 | 11.63 | 19.95 | 1.00 | 58.9 | 90.0 |
| Bench 4 | Bench | Cole Palmer | MID | 7 | 5.7 | 3.21 | 11.16 | 17.13 | 2.00 | 55.5 | 84.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.56 | 10.90 | 17.79 | 2.00 | 72.0 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 3.10 -> 1.80
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 64.03
- Actual score: 112.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.29) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Kyle Walker -> Kieran Trippier (projected gain 4.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.29) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.08 | 9.61 | 15.66 | 1.00 | 81.6 | 45.0 |
| Bench 1 | Bench Boost | Alisson Ramses Becker | GK | 11 | 5.7 | 2.58 | 8.39 | 13.64 | 2.00 | 74.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.47 | 12.57 | 20.31 | 9.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.19 | 12.16 | 19.95 | 1.00 | 84.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.40 | 10.32 | 16.71 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.3 | 2.94 | 9.65 | 15.82 | 1.00 | 79.4 | 90.0 |
| Bench 2 | Bench Boost | Pervis Estupiñán | DEF | 5 | 5.0 | 3.01 | 8.49 | 13.45 | 1.00 | 50.1 | 10.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.78 | 16.25 | 26.22 | 18.00 | 93.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.39 | 12.28 | 19.99 | 2.00 | 73.0 | 90.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.76 | 8.62 | 14.81 | 8.00 | 49.2 | 87.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.55 | 16.75 | 26.86 | 9.00 | 87.6 | 78.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.47 | 12.86 | 20.62 | 8.00 | 86.2 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.22 | 12.67 | 20.98 | 20.00 | 62.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.69 | 11.57 | 20.04 | 2.00 | 67.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.72 | 10.97 | 17.98 | 11.00 | 77.0 | 90.0 |
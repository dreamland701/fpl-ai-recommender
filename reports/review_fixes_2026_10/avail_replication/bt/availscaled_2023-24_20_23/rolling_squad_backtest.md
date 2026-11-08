# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 244.21
- Total actual points: 279.00
- Average predicted points: 61.05
- Average actual points: 69.75
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
- Predicted score: 62.33
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.67 | 9.82 | 15.96 | 11.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.14 | 9.19 | 14.95 | 2.00 | 89.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.75 | 16.06 | 25.74 | 0.00 | 96.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.54 | 12.97 | 20.74 | 2.00 | 91.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 4.05 | 11.43 | 18.55 | 1.00 | 86.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.95 | 11.23 | 18.19 | 0.00 | 92.6 | 90.0 |
| Bench 4 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 2.72 | 8.96 | 14.78 | 0.00 | 72.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.38 | 11.21 | 17.37 | 2.00 | 60.5 | 90.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 4.9 | 3.82 | 10.22 | 16.15 | 2.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Jean-Philippe Mateta | FWD | 8 | 4.9 | 3.16 | 8.80 | 14.44 | 2.00 | 67.9 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.57 | 21.08 | 34.44 | 16.00 | 104.5 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.92 | 17.59 | 28.90 | 9.00 | 96.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.55 | 16.52 | 26.89 | 7.00 | 90.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.34 | 15.25 | 24.61 | 3.00 | 98.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 4.03 | 11.79 | 20.08 | 18.00 | 62.6 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 61.30
- Actual score: 53.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.01, hit 0)
- Autosub: Jean-Philippe Mateta replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.12 | 11.06 | 18.07 | 3.00 | 95.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.84 | 8.23 | 13.69 | 9.00 | 87.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.86 | 13.78 | 22.23 | 6.00 | 103.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.69 | 12.59 | 21.09 | 0.00 | 69.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 4.09 | 11.33 | 17.91 | 6.00 | 95.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.20 | 11.30 | 18.15 | 6.00 | 93.5 | 90.0 |
| Bench 2 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 2.33 | 7.93 | 13.34 | 0.00 | 73.8 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.97 | 12.57 | 19.17 | 2.00 | 93.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.44 | 9.81 | 16.04 | 8.00 | 73.6 | 90.0 |
| Bench 3 | Autosub In | Jean-Philippe Mateta | FWD | 8 | 4.9 | 2.25 | 8.10 | 13.88 | 2.00 | 43.5 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.89 | 20.01 | 31.40 | 3.00 | 120.4 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.95 | 17.87 | 27.22 | 2.00 | 115.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 5.39 | 12.70 | 19.25 | 10.00 | 98.3 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 11 | 13.2 | 1.92 | 11.15 | 21.38 | 0.00 | 12.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.80 | 10.69 | 17.25 | 2.00 | 69.4 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 2.00 -> 6.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Martin Ødegaard
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.12
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.41) beats the best remaining Triple Captain opportunity (7.27).
- Transfer: Mohamed Salah -> Martin Ødegaard (projected gain 7.22, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.41) beats the best remaining Triple Captain opportunity (7.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.56 | 9.99 | 16.58 | 3.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.91 | 8.56 | 14.53 | 10.00 | 88.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.66 | 13.03 | 21.37 | 1.00 | 87.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.31 | 12.33 | 22.23 | 1.00 | 17.5 | 22.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.12 | 11.23 | 18.12 | 2.00 | 86.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.53 | 10.42 | 16.80 | 2.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 0.79 | 2.75 | 4.95 | 2.00 | 24.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.16 | 11.45 | 17.97 | 2.00 | 77.7 | 70.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 2.98 | 9.35 | 15.17 | 1.00 | 76.3 | 45.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 4.9 | 3.05 | 7.97 | 13.50 | 2.00 | 71.3 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.41 | 17.62 | 28.09 | 10.00 | 86.6 | 90.0 |
| Vice Captain | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.88 | 13.97 | 22.77 | 2.00 | 80.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.63 | 12.61 | 19.36 | 2.00 | 62.5 | 84.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 8.0 | 2.32 | 7.18 | 12.32 | 1.00 | 38.9 | 90.0 |
| Bench 3 | Bench | Phil Foden | MID | 13 | 7.9 | 2.20 | 6.99 | 11.14 | 6.00 | 23.0 | 76.0 |

## GW23

- Train rows: 120213
- Bank: 6.60 -> 2.70
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 63.46
- Actual score: 93.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.28) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jean-Philippe Mateta -> Ollie Watkins (projected gain 6.49, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.28) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.15 | 9.82 | 16.01 | 1.00 | 83.6 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 2.82 | 8.48 | 14.35 | 2.00 | 86.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.63 | 13.04 | 22.24 | 1.00 | 62.7 | 57.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.24 | 12.29 | 20.16 | 1.00 | 85.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.47 | 10.54 | 17.07 | 1.00 | 84.1 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.2 | 3.04 | 9.98 | 16.35 | 1.00 | 82.4 | 90.0 |
| Bench 3 | Bench Boost | Marcos Senesi | DEF | 3 | 4.5 | 2.74 | 7.56 | 12.20 | 1.00 | 71.5 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.78 | 16.25 | 26.22 | 18.00 | 73.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.26 | 10.20 | 17.52 | 8.00 | 58.2 | 87.0 |
| Bench 4 | Bench Boost | Chris Wood | FWD | 16 | 4.9 | 2.69 | 9.54 | 16.93 | 0.00 | 53.4 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.60 | 16.92 | 27.14 | 9.00 | 88.6 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.65 | 13.96 | 23.11 | 20.00 | 68.1 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.11 | 12.96 | 20.96 | 2.00 | 77.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.47 | 12.86 | 20.62 | 8.00 | 86.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.04 | 12.65 | 21.90 | 2.00 | 73.9 | 90.0 |
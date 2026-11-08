# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 278.78
- Total actual points: 294.00
- Average predicted points: 69.70
- Average actual points: 73.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 121022
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.46
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.96 | 10.86 | 17.61 | 0.00 | 87.2 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.19 | 0.19 | 0.29 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.51 | 12.94 | 20.85 | 4.00 | 85.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.83 | 11.07 | 18.52 | 2.00 | 77.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.72 | 10.09 | 16.06 | 1.00 | 71.7 | 86.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 3.09 | 9.11 | 14.84 | 2.00 | 73.8 | 79.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 10 | 4.4 | 2.97 | 8.20 | 13.41 | 2.00 | 75.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.55 | 18.07 | 27.97 | 13.00 | 69.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.20 | 17.22 | 28.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 5.10 | 13.66 | 22.30 | 1.00 | 89.5 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.17 | 16.18 | 26.55 | 15.00 | 75.6 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.71 | 16.02 | 25.79 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.66 | 13.71 | 22.54 | 2.00 | 84.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.50 | 13.04 | 21.18 | 10.00 | 82.4 | 90.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 5.0 | 3.94 | 10.84 | 17.73 | 2.00 | 77.9 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 99.52
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.08) beats the best remaining Triple Captain opportunity (9.50).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 3.58, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.08) beats the best remaining Triple Captain opportunity (9.50).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.54 | 7.76 | 12.84 | 0.00 | 94.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 3.10 | 5.08 | 7.16 | 5.00 | 71.8 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.57 | 12.59 | 20.60 | 1.00 | 83.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.22 | 11.39 | 18.11 | 6.00 | 86.3 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 6.11 | 10.86 | 16.60 | 1.00 | 128.7 | 154.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | 10 | 4.4 | 2.62 | 7.83 | 12.96 | 5.00 | 73.6 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 2.48 | 7.41 | 12.38 | 0.00 | 64.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.48 | 22.95 | 34.55 | 10.00 | 179.4 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.80 | 14.84 | 25.21 | 13.00 | 80.1 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.45 | 6.85 | 12.70 | 0.00 | 29.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.98 | 17.16 | 26.32 | 5.00 | 161.8 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.00 | 17.02 | 28.08 | 15.00 | 78.7 | 68.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.90 | 11.07 | 17.67 | 3.00 | 148.6 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.35 | 10.63 | 17.99 | 2.00 | 59.0 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.64 | 10.20 | 17.95 | 2.00 | 66.1 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 54.59
- Actual score: 53.00
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 9.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.39 | 12.04 | 19.11 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 6.46 | 10.31 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.89 | 13.03 | 21.06 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.35 | 12.07 | 18.88 | 2.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.29 | 17.27 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.38 | 7.83 | 13.13 | 2.00 | 75.4 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 0.00 | 4.23 | 8.09 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.28 | 23.45 | 35.66 | 5.00 | 90.0 | 74.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.31 | 20.57 | 32.86 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.15 | 6.59 | 12.29 | 0.00 | 23.3 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 7.18 | 20.40 | 31.50 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.38 | 17.90 | 28.39 | 11.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 5.0 | 0.00 | 12.10 | 20.43 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.27 | 18.05 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 9.55 | 16.83 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.40 -> 1.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.22
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.58) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Richarlison de Andrade -> Douglas Luiz Soares de Paulo (projected gain 5.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.46 | 10.19 | 16.93 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.73 | 4.97 | 7.81 | 9.00 | 41.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.47 | 12.86 | 21.20 | 1.00 | 88.7 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.19 | 11.49 | 18.05 | 6.00 | 78.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.60 | 7.67 | 12.70 | 6.00 | 72.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.31 | 6.83 | 11.68 | 5.00 | 44.6 | 90.0 |
| Bench 3 | Bench Boost | Destiny Udogie | DEF | 18 | 4.9 | 0.97 | 3.16 | 6.08 | 2.00 | 18.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.46 | 21.88 | 34.24 | 6.00 | 88.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.76 | 19.73 | 30.73 | 13.00 | 89.3 | 90.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.66 | 3.58 | 7.73 | 0.00 | 9.7 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 6.91 | 19.01 | 31.31 | 7.00 | 80.7 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.43 | 16.35 | 26.36 | 15.00 | 86.4 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 4.49 | 12.60 | 19.75 | 4.00 | 82.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.10 | 8.75 | 15.21 | 5.00 | 47.9 | 90.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 5.0 | 2.22 | 7.53 | 13.12 | 2.00 | 54.1 | 90.0 |
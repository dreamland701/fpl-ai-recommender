# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 280.20
- Total actual points: 294.00
- Average predicted points: 70.05
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
- Predicted score: 60.79
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.55 | 9.67 | 15.70 | 0.00 | 83.6 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.27 | 0.41 | 0.66 | 3.00 | 1.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.76 | 13.82 | 22.37 | 4.00 | 88.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.99 | 11.61 | 19.44 | 2.00 | 78.9 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.76 | 10.25 | 16.28 | 1.00 | 73.3 | 86.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 3.08 | 8.99 | 14.53 | 2.00 | 73.4 | 79.0 |
| Bench 4 | Bench | Antonee Robinson | DEF | 10 | 4.4 | 2.88 | 7.89 | 12.88 | 2.00 | 74.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.70 | 18.28 | 28.16 | 13.00 | 71.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.94 | 16.56 | 27.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.73 | 12.72 | 20.88 | 1.00 | 86.1 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.25 | 16.34 | 26.61 | 15.00 | 75.7 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.61 | 15.33 | 24.44 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.93 | 14.52 | 23.90 | 2.00 | 87.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.87 | 14.28 | 23.21 | 10.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 5.0 | 3.93 | 10.95 | 17.96 | 2.00 | 77.1 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 99.99
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.36) beats the best remaining Triple Captain opportunity (9.67).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 4.14, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.36) beats the best remaining Triple Captain opportunity (9.67).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.12 | 7.14 | 11.86 | 0.00 | 91.2 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 2.94 | 4.82 | 6.74 | 5.00 | 72.5 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.85 | 13.59 | 22.32 | 1.00 | 86.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.40 | 11.94 | 18.99 | 6.00 | 87.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.71 | 10.22 | 15.48 | 1.00 | 127.3 | 154.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | 10 | 4.4 | 2.62 | 7.71 | 12.69 | 5.00 | 74.2 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 2.53 | 7.51 | 12.44 | 0.00 | 64.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.76 | 23.18 | 34.77 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.42 | 13.80 | 23.57 | 13.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.14 | 6.08 | 11.56 | 0.00 | 26.5 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.51 | 28.65 | 15.00 | 78.8 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.75 | 16.60 | 25.25 | 5.00 | 159.1 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.60 | 11.37 | 19.24 | 2.00 | 61.7 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.90 | 11.08 | 19.37 | 2.00 | 67.4 | 70.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.76 | 10.95 | 17.50 | 3.00 | 145.7 | 180.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 54.95
- Actual score: 53.00
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 8.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.14 | 11.26 | 17.82 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.74 | 9.15 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.05 | 13.81 | 22.51 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.53 | 12.59 | 19.71 | 2.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.95 | 16.66 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.41 | 7.73 | 12.88 | 2.00 | 77.0 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 0.00 | 4.10 | 7.81 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.54 | 23.88 | 36.15 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.02 | 19.72 | 31.49 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.88 | 5.97 | 11.42 | 0.00 | 21.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.44 | 21.10 | 32.46 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.40 | 17.57 | 27.65 | 11.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 5.0 | 0.00 | 11.94 | 20.20 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 11.14 | 19.50 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.47 | 18.38 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.40 -> 1.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.46
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Richarlison de Andrade -> Douglas Luiz Soares de Paulo (projected gain 6.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.22 | 9.51 | 15.83 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.25 | 3.67 | 5.73 | 9.00 | 36.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.67 | 13.73 | 22.83 | 1.00 | 90.0 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.38 | 12.01 | 18.87 | 6.00 | 80.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.69 | 7.77 | 12.78 | 6.00 | 74.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.15 | 6.35 | 10.86 | 5.00 | 44.0 | 90.0 |
| Bench 3 | Bench Boost | Destiny Udogie | DEF | 18 | 4.9 | 0.91 | 2.97 | 5.70 | 2.00 | 16.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.65 | 22.16 | 34.51 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.47 | 19.01 | 29.71 | 13.00 | 86.3 | 90.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.67 | 3.78 | 8.18 | 0.00 | 10.5 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.22 | 19.86 | 32.51 | 7.00 | 82.6 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.45 | 16.08 | 25.70 | 15.00 | 87.0 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 4.73 | 13.73 | 21.75 | 4.00 | 84.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.28 | 9.57 | 16.64 | 5.00 | 47.5 | 90.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 5.0 | 2.08 | 7.26 | 12.74 | 2.00 | 52.0 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 279.90
- Total actual points: 298.00
- Average predicted points: 69.97
- Average actual points: 74.50
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
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.23
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.55 | 9.64 | 15.55 | 0.00 | 84.1 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.28 | 0.37 | 0.56 | 3.00 | 2.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.46 | 12.47 | 19.89 | 4.00 | 86.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.82 | 11.06 | 18.35 | 2.00 | 77.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.82 | 10.11 | 16.17 | 1.00 | 74.1 | 86.0 |
| Bench 4 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 3.19 | 9.36 | 15.03 | 2.00 | 75.3 | 79.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.25 | 8.51 | 14.01 | 1.00 | 80.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.57 | 17.52 | 26.80 | 13.00 | 70.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.83 | 16.00 | 26.40 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.84 | 12.51 | 20.48 | 1.00 | 87.0 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.23 | 16.28 | 26.47 | 15.00 | 74.7 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.86 | 15.88 | 25.42 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.91 | 14.34 | 23.56 | 2.00 | 89.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.78 | 13.68 | 21.92 | 10.00 | 84.2 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.9 | 3.57 | 10.47 | 17.19 | 2.00 | 83.5 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.50
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.69) beats the best remaining Triple Captain opportunity (9.47).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 3.85, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.69) beats the best remaining Triple Captain opportunity (9.47).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.09 | 7.21 | 11.96 | 0.00 | 92.7 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 2.94 | 4.70 | 6.50 | 5.00 | 73.6 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.56 | 12.32 | 19.89 | 1.00 | 83.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.42 | 12.02 | 18.89 | 6.00 | 87.5 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.88 | 10.34 | 15.89 | 1.00 | 131.9 | 154.0 |
| Bench 2 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.59 | 8.18 | 13.49 | 2.00 | 81.8 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 2.59 | 7.63 | 12.53 | 0.00 | 65.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.44 | 22.55 | 33.49 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.34 | 13.61 | 23.06 | 13.00 | 75.7 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.11 | 5.87 | 11.20 | 0.00 | 27.4 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.18 | 17.25 | 28.29 | 15.00 | 77.7 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.83 | 17.00 | 26.03 | 5.00 | 164.4 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.54 | 11.13 | 18.90 | 2.00 | 64.2 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.75 | 10.43 | 18.17 | 2.00 | 67.1 | 70.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.58 | 10.14 | 16.37 | 5.00 | 76.4 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.09
- Actual score: 59.00
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 7.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.07 | 10.98 | 17.26 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.51 | 8.64 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.81 | 12.76 | 20.37 | 0.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.29 | 11.98 | 18.74 | 2.00 | 81.0 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.25 | 17.30 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.13 | 8.66 | 14.33 | 6.00 | 80.4 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 0.00 | 4.26 | 8.06 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.37 | 23.43 | 35.29 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.14 | 19.51 | 30.83 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.81 | 5.48 | 10.75 | 0.00 | 21.8 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.61 | 21.16 | 32.21 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.49 | 18.01 | 28.51 | 11.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 4.01 | 11.61 | 17.95 | 2.00 | 80.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.37 | 17.98 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.35 | 18.21 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.07
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.15) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Richarlison de Andrade -> Jarrod Bowen (projected gain 6.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.15) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.16 | 9.36 | 15.49 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.27 | 3.46 | 5.38 | 9.00 | 37.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.45 | 12.73 | 20.92 | 1.00 | 87.0 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.14 | 11.24 | 17.60 | 6.00 | 77.1 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.44 | 7.71 | 13.37 | 1.00 | 76.2 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.29 | 6.65 | 11.50 | 5.00 | 45.5 | 90.0 |
| Bench 3 | Bench Boost | Destiny Udogie | DEF | 18 | 4.9 | 0.91 | 3.06 | 5.94 | 2.00 | 17.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.54 | 22.11 | 34.45 | 6.00 | 88.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.46 | 18.76 | 28.87 | 13.00 | 86.5 | 90.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.68 | 3.62 | 8.01 | 0.00 | 11.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.31 | 19.71 | 32.15 | 7.00 | 82.8 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.62 | 16.75 | 27.31 | 15.00 | 89.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.55 | 12.71 | 20.21 | 5.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 2.57 | 9.42 | 15.07 | 2.00 | 66.6 | 81.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.14 | 9.00 | 15.55 | 5.00 | 46.7 | 90.0 |
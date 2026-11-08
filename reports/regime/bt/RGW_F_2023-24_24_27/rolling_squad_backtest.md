# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 279.95
- Total actual points: 298.00
- Average predicted points: 69.99
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
- Predicted score: 60.15
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.58 | 9.71 | 15.65 | 0.00 | 81.2 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.33 | 0.52 | 0.82 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.46 | 12.49 | 19.94 | 4.00 | 87.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.81 | 11.03 | 18.30 | 2.00 | 78.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.82 | 10.12 | 16.20 | 1.00 | 74.7 | 86.0 |
| Bench 4 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 3.20 | 9.43 | 15.17 | 2.00 | 76.8 | 79.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.23 | 8.47 | 13.93 | 1.00 | 82.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.61 | 17.70 | 27.12 | 13.00 | 71.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.76 | 15.71 | 25.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.78 | 12.22 | 19.92 | 1.00 | 85.7 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.23 | 16.31 | 26.55 | 15.00 | 75.5 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.85 | 15.84 | 25.34 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.92 | 14.41 | 23.70 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.72 | 13.44 | 21.49 | 10.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.9 | 3.54 | 10.35 | 16.95 | 2.00 | 83.1 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.62
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.75) beats the best remaining Triple Captain opportunity (9.51).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.32, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.75) beats the best remaining Triple Captain opportunity (9.51).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.15 | 7.31 | 12.13 | 0.00 | 87.7 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 3.01 | 4.83 | 6.71 | 5.00 | 68.6 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.55 | 12.29 | 19.83 | 1.00 | 85.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.41 | 11.98 | 18.83 | 6.00 | 89.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.93 | 10.44 | 16.06 | 1.00 | 132.1 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.59 | 8.17 | 13.49 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 2.60 | 7.67 | 12.61 | 0.00 | 67.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.50 | 22.66 | 33.69 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.29 | 13.39 | 22.64 | 13.00 | 75.3 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.08 | 5.72 | 10.90 | 0.00 | 26.1 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.23 | 28.26 | 15.00 | 78.7 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.81 | 16.97 | 25.98 | 5.00 | 164.2 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.55 | 11.21 | 19.06 | 2.00 | 65.3 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.69 | 10.21 | 17.77 | 2.00 | 67.4 | 70.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.55 | 10.03 | 16.15 | 5.00 | 75.9 | 90.0 |

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
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 7.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.10 | 11.07 | 17.41 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.59 | 8.77 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.79 | 12.71 | 20.28 | 0.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.28 | 11.94 | 18.68 | 2.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.37 | 17.52 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.12 | 8.65 | 14.32 | 6.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 0.00 | 4.32 | 8.18 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.42 | 23.67 | 35.73 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.10 | 19.34 | 30.52 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.77 | 5.26 | 10.30 | 0.00 | 20.5 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.60 | 21.13 | 32.15 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.50 | 18.03 | 28.55 | 11.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.99 | 11.52 | 17.78 | 2.00 | 79.5 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.43 | 18.36 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.14 | 17.56 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.09
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.17) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Richarlison de Andrade -> Jarrod Bowen (projected gain 6.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.17) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.18 | 9.43 | 15.58 | 2.00 | 85.2 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.29 | 3.51 | 5.45 | 9.00 | 34.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.43 | 12.69 | 20.86 | 1.00 | 88.2 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.12 | 11.18 | 17.52 | 6.00 | 78.5 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.43 | 7.69 | 13.33 | 1.00 | 77.3 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.32 | 6.77 | 11.75 | 5.00 | 46.0 | 90.0 |
| Bench 3 | Bench Boost | Destiny Udogie | DEF | 18 | 4.9 | 0.94 | 3.16 | 6.13 | 2.00 | 18.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.60 | 22.36 | 34.92 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.41 | 18.57 | 28.48 | 13.00 | 86.2 | 90.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.63 | 3.38 | 7.52 | 0.00 | 10.5 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.31 | 19.71 | 32.16 | 7.00 | 84.3 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.63 | 16.78 | 27.36 | 15.00 | 89.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.56 | 12.76 | 20.33 | 5.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 2.56 | 9.36 | 14.96 | 2.00 | 65.9 | 81.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.08 | 8.73 | 15.05 | 5.00 | 46.8 | 90.0 |
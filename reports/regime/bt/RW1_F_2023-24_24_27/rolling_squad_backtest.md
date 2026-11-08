# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 277.79
- Total actual points: 299.00
- Average predicted points: 69.45
- Average actual points: 74.75
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
- Predicted score: 59.89
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.55 | 9.55 | 15.34 | 0.00 | 84.4 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.30 | 0.35 | 0.51 | 3.00 | 2.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.37 | 11.98 | 18.93 | 4.00 | 85.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.74 | 10.84 | 17.97 | 2.00 | 77.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.87 | 10.14 | 16.33 | 1.00 | 75.5 | 86.0 |
| Bench 4 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 3.23 | 9.43 | 15.04 | 2.00 | 76.4 | 79.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.30 | 8.52 | 14.03 | 1.00 | 81.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.41 | 16.57 | 25.02 | 13.00 | 69.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.73 | 15.58 | 25.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.92 | 12.49 | 20.40 | 1.00 | 87.8 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.19 | 16.12 | 26.15 | 15.00 | 73.9 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.97 | 15.80 | 25.07 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.93 | 14.28 | 23.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.79 | 13.63 | 21.70 | 10.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.9 | 3.69 | 10.51 | 17.23 | 2.00 | 84.4 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 95.20
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.31) beats the best remaining Triple Captain opportunity (9.24).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 3.89, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.31) beats the best remaining Triple Captain opportunity (9.24).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.01 | 7.18 | 11.88 | 0.00 | 92.6 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 2.98 | 4.70 | 6.42 | 5.00 | 75.8 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.48 | 12.07 | 18.86 | 6.00 | 89.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.51 | 11.92 | 19.04 | 1.00 | 83.3 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.98 | 10.43 | 16.12 | 1.00 | 135.8 | 154.0 |
| Bench 2 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.65 | 8.21 | 13.56 | 2.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 2.62 | 7.62 | 12.42 | 0.00 | 66.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.06 | 21.73 | 31.75 | 10.00 | 178.4 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.29 | 13.41 | 22.66 | 13.00 | 75.0 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.12 | 5.90 | 11.28 | 0.00 | 27.7 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 16.92 | 27.72 | 15.00 | 76.4 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.67 | 16.76 | 25.64 | 5.00 | 166.0 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.52 | 11.08 | 18.92 | 2.00 | 66.1 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.74 | 10.37 | 17.96 | 2.00 | 68.0 | 70.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.66 | 10.28 | 16.58 | 5.00 | 77.9 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.94
- Actual score: 59.00
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 7.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.04 | 10.77 | 16.84 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.51 | 8.48 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.76 | 12.50 | 19.68 | 0.00 | 89.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.34 | 11.96 | 18.66 | 2.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.57 | 17.90 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.19 | 8.75 | 14.59 | 6.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 0.00 | 4.31 | 8.05 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.17 | 22.67 | 33.79 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.24 | 19.33 | 30.31 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.75 | 5.21 | 10.57 | 0.00 | 21.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.73 | 21.10 | 31.78 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.51 | 17.92 | 28.36 | 11.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 4.03 | 11.72 | 18.05 | 2.00 | 81.9 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.52 | 18.57 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.32 | 17.77 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Erling Haaland
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 63.76
- Actual score: 86.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.21) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Richarlison de Andrade -> Jarrod Bowen (projected gain 6.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.21) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.13 | 9.19 | 15.14 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.28 | 3.31 | 5.15 | 9.00 | 37.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.40 | 12.48 | 20.45 | 1.00 | 86.2 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.13 | 11.14 | 17.60 | 6.00 | 78.3 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.42 | 7.69 | 13.52 | 1.00 | 77.4 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.38 | 6.85 | 11.96 | 5.00 | 46.0 | 90.0 |
| Bench 3 | Bench Boost | Destiny Udogie | DEF | 18 | 4.9 | 0.87 | 2.94 | 5.78 | 2.00 | 17.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.4 | 7.36 | 21.55 | 33.54 | 6.00 | 85.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.45 | 18.63 | 28.35 | 13.00 | 86.6 | 90.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.68 | 3.77 | 8.42 | 0.00 | 13.1 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.38 | 19.54 | 31.77 | 7.00 | 82.4 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.60 | 16.72 | 27.54 | 15.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.62 | 12.71 | 19.93 | 5.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 2.55 | 9.47 | 15.37 | 2.00 | 68.4 | 81.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.13 | 8.98 | 15.63 | 5.00 | 46.0 | 90.0 |
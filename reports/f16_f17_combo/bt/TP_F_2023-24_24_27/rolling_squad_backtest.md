# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 291.98
- Total actual points: 309.00
- Average predicted points: 73.00
- Average actual points: 77.25
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
- Predicted score: 61.91
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.80 | 10.25 | 16.52 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.12 | 0.04 | 0.05 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.84 | 13.83 | 22.22 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.04 | 11.43 | 18.92 | 2.00 | 81.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.67 | 10.72 | 17.14 | 12.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 10 | 4.4 | 3.19 | 8.80 | 14.34 | 2.00 | 83.0 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.96 | 6.81 | 11.17 | 1.00 | 75.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.03 | 19.24 | 29.76 | 13.00 | 79.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.08 | 16.70 | 27.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.75 | 12.36 | 19.98 | 1.00 | 87.2 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.46 | 16.90 | 27.60 | 15.00 | 81.8 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.74 | 15.83 | 25.28 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.86 | 13.89 | 22.55 | 2.00 | 85.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.61 | 13.03 | 20.90 | 10.00 | 79.6 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.9 | 3.35 | 9.96 | 16.07 | 2.00 | 79.3 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 99.79
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.25) beats the best remaining Triple Captain opportunity (10.03).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 2.62, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.25) beats the best remaining Triple Captain opportunity (10.03).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.85 | 7.98 | 13.09 | 0.00 | 112.7 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 2.53 | 4.29 | 5.89 | 5.00 | 58.5 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.91 | 13.44 | 21.89 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.56 | 12.51 | 19.63 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.53 | 12.14 | 19.21 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.94 | 8.61 | 14.15 | 5.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.85 | 6.06 | 10.11 | -1.00 | 75.4 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 16.35 | 23.97 | 36.13 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.60 | 14.07 | 23.79 | 13.00 | 80.9 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 0.75 | 4.85 | 9.73 | 0.00 | 17.6 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.34 | 17.86 | 29.28 | 15.00 | 83.8 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.03 | 17.02 | 25.91 | 5.00 | 161.7 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.56 | 10.82 | 17.99 | 2.00 | 60.5 | 70.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.67 | 9.95 | 17.23 | 2.00 | 62.4 | 70.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.42 | 9.51 | 15.17 | 5.00 | 71.4 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.25
- Actual score: 55.00
- Transfer: Cole Palmer -> Pascal Groß (projected gain 9.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.24 | 8.20 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.00 | 5.05 | 9.80 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.10 | 13.67 | 22.11 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.64 | 12.74 | 19.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.46 | 12.61 | 19.64 | 2.00 | 86.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.74 | 8.69 | 14.45 | 2.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.99 | 5.65 | 9.26 | 1.00 | 67.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.76 | 24.75 | 37.75 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.21 | 20.19 | 32.14 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.51 | 4.66 | 9.31 | 0.00 | 12.7 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.56 | 21.38 | 32.95 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.49 | 18.00 | 28.41 | 11.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.62 | 14.51 | 22.54 | 7.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.91 | 11.06 | 16.97 | 2.00 | 75.4 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 9.69 | 16.98 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.03
- Actual score: 81.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.62) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 7.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.62) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.44 | 9.99 | 16.47 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.23 | 3.33 | 4.99 | 9.00 | 35.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.72 | 13.60 | 22.40 | 1.00 | 90.0 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.51 | 12.23 | 19.09 | 6.00 | 84.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.44 | 12.05 | 18.70 | 6.00 | 83.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 3.00 | 8.64 | 14.15 | 6.00 | 82.3 | 90.0 |
| Bench 2 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.10 | 5.63 | 9.05 | 1.00 | 71.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.86 | 23.01 | 36.10 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.65 | 19.34 | 29.99 | 13.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.33 | 2.58 | 6.21 | 0.00 | 3.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.38 | 20.27 | 33.14 | 7.00 | 86.9 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.57 | 16.55 | 26.52 | 15.00 | 87.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.46 | 12.01 | 19.33 | 1.00 | 76.0 | 31.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 2.51 | 8.96 | 13.94 | 2.00 | 62.2 | 81.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.96 | 5.70 | 10.95 | 0.00 | 25.6 | 0.0 |
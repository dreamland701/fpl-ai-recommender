# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 289.21
- Total actual points: 309.00
- Average predicted points: 72.30
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
- Predicted score: 61.20
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.72 | 10.11 | 16.40 | 0.00 | 89.3 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.26 | 0.24 | 0.29 | 3.00 | 1.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.79 | 13.74 | 22.17 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.96 | 11.31 | 18.83 | 2.00 | 80.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.59 | 10.59 | 17.04 | 12.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 10 | 4.4 | 3.11 | 8.67 | 14.22 | 2.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.91 | 6.73 | 11.10 | 1.00 | 73.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.97 | 19.14 | 29.72 | 13.00 | 78.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.01 | 16.59 | 27.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.69 | 12.29 | 19.96 | 1.00 | 85.7 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.39 | 16.79 | 27.52 | 15.00 | 80.0 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.70 | 15.78 | 25.26 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.81 | 13.84 | 22.52 | 2.00 | 83.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.59 | 13.01 | 20.89 | 10.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.9 | 3.31 | 9.90 | 16.02 | 2.00 | 78.2 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 98.65
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.17) beats the best remaining Triple Captain opportunity (9.98).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 2.55, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.17) beats the best remaining Triple Captain opportunity (9.98).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.60 | 7.78 | 12.90 | 0.00 | 105.9 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 2.91 | 4.58 | 6.22 | 5.00 | 71.0 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.84 | 13.34 | 21.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.49 | 12.41 | 19.55 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.46 | 12.03 | 19.12 | 6.00 | 89.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.86 | 8.48 | 14.03 | 5.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.80 | 5.98 | 10.04 | -1.00 | 74.0 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 16.27 | 23.92 | 36.12 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.51 | 13.94 | 23.70 | 13.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.13 | 5.77 | 10.87 | 0.00 | 26.9 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.27 | 17.78 | 29.25 | 15.00 | 82.0 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.92 | 16.96 | 25.89 | 5.00 | 158.9 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.50 | 10.73 | 17.93 | 2.00 | 58.9 | 70.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.61 | 9.86 | 17.13 | 2.00 | 60.6 | 70.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.38 | 9.45 | 15.12 | 5.00 | 70.3 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.85
- Actual score: 55.00
- Transfer: Cole Palmer -> Pascal Groß (projected gain 8.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.26 | 8.32 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.00 | 4.80 | 9.63 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.03 | 13.55 | 22.00 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.58 | 12.64 | 19.77 | 2.00 | 88.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.39 | 12.50 | 19.56 | 2.00 | 84.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.66 | 8.56 | 14.34 | 2.00 | 83.6 | 90.0 |
| Bench 2 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.93 | 5.57 | 9.19 | 1.00 | 66.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.79 | 24.82 | 37.92 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.16 | 20.11 | 32.10 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.84 | 5.48 | 10.39 | 0.00 | 20.7 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.52 | 21.33 | 32.95 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.50 | 18.02 | 28.48 | 11.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.57 | 14.44 | 22.50 | 7.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.88 | 11.03 | 16.98 | 2.00 | 74.5 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 9.81 | 17.13 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.51
- Actual score: 81.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 7.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.37 | 9.87 | 16.39 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.18 | 3.27 | 4.95 | 9.00 | 34.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.65 | 13.48 | 22.30 | 1.00 | 90.0 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.44 | 12.11 | 19.00 | 6.00 | 82.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.37 | 11.93 | 18.63 | 6.00 | 81.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.92 | 8.50 | 14.04 | 6.00 | 80.2 | 90.0 |
| Bench 2 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.05 | 5.55 | 8.99 | 1.00 | 69.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.87 | 23.04 | 36.22 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.58 | 19.26 | 29.96 | 13.00 | 89.8 | 90.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.65 | 3.36 | 7.24 | 0.00 | 11.1 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.33 | 20.21 | 33.16 | 7.00 | 85.7 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.55 | 16.53 | 26.55 | 15.00 | 87.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.40 | 11.92 | 19.29 | 1.00 | 74.5 | 31.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 2.47 | 8.90 | 13.91 | 2.00 | 60.9 | 81.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.83 | 5.51 | 10.79 | 0.00 | 22.0 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 272.45
- Total actual points: 293.00
- Average predicted points: 68.11
- Average actual points: 73.25
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
- Predicted score: 58.90
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.63 | 10.82 | 17.22 | 0.00 | 79.2 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.04 | 0.00 | 0.00 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.46 | 12.93 | 20.90 | 4.00 | 88.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.59 | 11.40 | 18.93 | 2.00 | 75.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.76 | 11.28 | 17.94 | 2.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.46 | 6.89 | 10.78 | 3.00 | 66.2 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.97 | 5.65 | 9.27 | 0.00 | 69.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.43 | 17.35 | 27.20 | 13.00 | 75.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.61 | 15.98 | 26.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.39 | 11.80 | 19.68 | 1.00 | 88.0 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.51 | 16.48 | 26.61 | 15.00 | 74.5 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.70 | 15.81 | 24.96 | 3.00 | 86.7 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.55 | 14.22 | 23.04 | 2.00 | 81.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.82 | 13.71 | 22.12 | 10.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Sean Longstaff | MID | 15 | 4.8 | 2.81 | 9.17 | 14.84 | 2.00 | 70.4 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 101.61
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.46) beats the best remaining Triple Captain opportunity (9.73).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 5.93, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.46) beats the best remaining Triple Captain opportunity (9.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 7.53 | 13.77 | 20.18 | 11.00 | 120.6 | 180.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 2.97 | 5.12 | 7.21 | 5.00 | 67.8 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 8.74 | 15.21 | 22.74 | 10.00 | 157.0 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.32 | 12.14 | 20.10 | 1.00 | 85.2 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.27 | 7.71 | 13.62 | 0.00 | 52.4 | 0.0 |
| XI | XI | Amari'i Bell | DEF | 12 | 3.9 | 2.88 | 7.00 | 11.03 | 1.00 | 136.9 | 180.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 0.78 | 2.62 | 4.70 | 0.00 | 34.6 | 59.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.86 | 23.54 | 34.79 | 10.00 | 179.3 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.35 | 13.86 | 23.49 | 13.00 | 73.1 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.47 | 6.89 | 12.92 | 0.00 | 36.8 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.03 | 17.62 | 25.34 | 5.00 | 129.8 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.95 | 16.57 | 27.11 | 15.00 | 77.6 | 68.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.32 | 11.18 | 18.38 | 2.00 | 53.2 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.79 | 10.91 | 19.13 | 2.00 | 65.6 | 70.0 |
| XI | XI | Sean Longstaff | MID | 15 | 4.8 | 3.12 | 9.37 | 15.12 | 2.00 | 74.8 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 52.40
- Actual score: 53.00
- Transfer: Sean Longstaff -> Alejandro Garnacho (projected gain 4.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.16 | 12.28 | 19.21 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 4.49 | 7.61 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.76 | 12.64 | 20.78 | 0.00 | 90.0 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 0.00 | 10.46 | 18.06 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 0.00 | 6.51 | 11.99 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.00 | 4.46 | 9.69 | 0.00 | 0.0 | 0.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.52 | 4.34 | 7.25 | 2.00 | 53.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.41 | 24.02 | 36.52 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.75 | 19.24 | 30.68 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.09 | 5.94 | 11.21 | 0.00 | 27.2 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.04 | 19.61 | 30.29 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.34 | 18.07 | 28.48 | 11.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 5.0 | 3.93 | 11.64 | 17.87 | 2.00 | 75.9 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.07 | 18.57 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 9.66 | 17.76 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 59.54
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.22) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Pedro Porro -> William Saliba (projected gain 8.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.22) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.39 | 11.26 | 18.14 | 2.00 | 81.1 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.01 | 3.76 | 5.74 | 9.00 | 32.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.36 | 13.06 | 21.52 | 1.00 | 87.7 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.57 | 12.55 | 19.52 | 6.00 | 80.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 2.55 | 8.46 | 14.26 | 6.00 | 52.4 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 1.49 | 4.47 | 7.41 | -1.00 | 60.3 | 90.0 |
| Bench 4 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 0.80 | 3.40 | 6.46 | 1.00 | 48.3 | 5.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.54 | 22.31 | 34.38 | 6.00 | 87.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 17.78 | 27.87 | 13.00 | 87.3 | 90.0 |
| Bench 3 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.92 | 3.89 | 8.25 | 0.00 | 15.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.00 | 18.44 | 30.22 | 7.00 | 83.8 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.59 | 17.28 | 27.13 | 15.00 | 81.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 5.0 | 2.45 | 9.08 | 14.55 | 2.00 | 64.4 | 81.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 2.82 | 8.35 | 14.68 | 5.00 | 45.1 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.1 | 1.57 | 5.48 | 10.62 | 0.00 | 13.7 | 0.0 |
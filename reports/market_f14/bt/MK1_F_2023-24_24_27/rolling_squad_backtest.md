# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 272.83
- Total actual points: 293.00
- Average predicted points: 68.21
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
- Predicted score: 59.18
- Actual score: 70.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.64 | 10.81 | 17.21 | 0.00 | 79.3 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.05 | 0.00 | 0.00 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.51 | 12.91 | 20.86 | 4.00 | 88.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.66 | 11.36 | 18.87 | 2.00 | 75.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.77 | 11.27 | 17.93 | 2.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.47 | 6.88 | 10.77 | 3.00 | 66.2 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.06 | 5.61 | 9.19 | 0.00 | 69.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.46 | 17.33 | 27.18 | 13.00 | 75.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.64 | 15.97 | 26.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.46 | 11.76 | 19.62 | 1.00 | 88.1 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.46 | 16.50 | 26.65 | 15.00 | 74.5 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.71 | 15.80 | 24.95 | 3.00 | 86.7 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.59 | 14.19 | 23.00 | 2.00 | 81.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.82 | 13.71 | 22.12 | 10.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Sean Longstaff | MID | 15 | 4.8 | 2.86 | 9.14 | 14.80 | 2.00 | 70.5 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 101.27
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.36) beats the best remaining Triple Captain opportunity (9.67).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 5.82, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.36) beats the best remaining Triple Captain opportunity (9.67).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 7.42 | 13.79 | 20.22 | 11.00 | 120.6 | 180.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 3.06 | 5.25 | 7.34 | 5.00 | 67.4 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 8.82 | 15.35 | 22.88 | 10.00 | 156.6 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.36 | 12.13 | 20.07 | 1.00 | 85.2 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.34 | 7.68 | 13.55 | 0.00 | 52.5 | 0.0 |
| XI | XI | Amari'i Bell | DEF | 12 | 3.9 | 2.99 | 6.85 | 10.84 | 1.00 | 137.3 | 180.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 0.88 | 2.57 | 4.60 | 0.00 | 34.7 | 59.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.76 | 23.54 | 34.81 | 10.00 | 179.3 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.36 | 13.85 | 23.49 | 13.00 | 73.1 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.48 | 6.89 | 12.92 | 0.00 | 36.8 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.82 | 17.65 | 25.40 | 5.00 | 129.7 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.99 | 16.54 | 27.06 | 15.00 | 77.6 | 68.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.35 | 11.16 | 18.35 | 2.00 | 53.2 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.75 | 10.94 | 19.18 | 2.00 | 65.6 | 70.0 |
| XI | XI | Sean Longstaff | MID | 15 | 4.8 | 3.14 | 9.36 | 15.10 | 2.00 | 74.8 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 52.70
- Actual score: 53.00
- Transfer: Sean Longstaff -> Alejandro Garnacho (projected gain 4.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.19 | 12.26 | 19.18 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 4.49 | 7.61 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.74 | 12.66 | 20.81 | 0.00 | 90.0 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 0.00 | 10.46 | 18.06 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 0.00 | 6.51 | 12.00 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.00 | 4.46 | 9.68 | 0.00 | 0.0 | 0.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.61 | 4.29 | 7.17 | 2.00 | 53.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.46 | 23.98 | 36.46 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.80 | 19.21 | 30.64 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.09 | 5.94 | 11.21 | 0.00 | 27.2 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.04 | 19.61 | 30.29 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.36 | 18.06 | 28.45 | 11.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 5.0 | 3.96 | 11.62 | 17.84 | 2.00 | 75.9 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.06 | 18.55 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 9.65 | 17.75 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 59.68
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.24) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Pedro Porro -> William Saliba (projected gain 8.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.24) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.36 | 11.28 | 18.17 | 2.00 | 81.1 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.07 | 3.73 | 5.68 | 9.00 | 32.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.40 | 13.04 | 21.48 | 1.00 | 87.8 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.58 | 12.53 | 19.50 | 6.00 | 80.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 2.63 | 8.43 | 14.20 | 6.00 | 52.4 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 1.43 | 4.51 | 7.47 | -1.00 | 60.3 | 90.0 |
| Bench 4 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 0.86 | 3.37 | 6.42 | 1.00 | 48.3 | 5.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.52 | 22.32 | 34.40 | 6.00 | 87.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.00 | 17.74 | 27.80 | 13.00 | 87.3 | 90.0 |
| Bench 3 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.88 | 3.92 | 8.29 | 0.00 | 15.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.00 | 18.43 | 30.21 | 7.00 | 83.8 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.54 | 17.30 | 27.16 | 15.00 | 81.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 5.0 | 2.42 | 9.11 | 14.60 | 2.00 | 64.4 | 81.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 2.87 | 8.32 | 14.63 | 5.00 | 45.1 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.1 | 1.61 | 5.46 | 10.59 | 0.00 | 13.7 | 0.0 |
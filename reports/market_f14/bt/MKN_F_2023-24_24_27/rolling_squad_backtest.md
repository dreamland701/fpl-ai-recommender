# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 270.11
- Total actual points: 270.00
- Average predicted points: 67.53
- Average actual points: 67.50
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
- Captain: Phil Foden
- Vice captain: Erling Haaland
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 62.07
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.41 | 10.81 | 17.21 | 0.00 | 100.4 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.00 | 0.00 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.46 | 12.91 | 20.86 | 4.00 | 87.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.04 | 11.36 | 18.87 | 2.00 | 85.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 4.63 | 11.27 | 17.93 | 2.00 | 100.9 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.77 | 6.88 | 10.77 | 3.00 | 74.4 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.86 | 5.61 | 9.19 | 0.00 | 65.4 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.09 | 17.33 | 27.18 | 13.00 | 66.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.46 | 15.97 | 26.71 | 2.00 | 91.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.12 | 11.76 | 19.62 | 1.00 | 78.3 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.60 | 16.50 | 26.65 | 15.00 | 75.9 | 66.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.56 | 15.80 | 24.95 | 3.00 | 98.8 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 5.44 | 14.19 | 23.00 | 2.00 | 95.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.70 | 13.71 | 22.12 | 10.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Sean Longstaff | MID | 15 | 4.8 | 3.45 | 9.14 | 14.80 | 2.00 | 81.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 83.41
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.44) beats the best remaining Bench Boost opportunity (5.65).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Pedro Porro -> Nathan Aké (projected gain 6.70, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.44) beats the best remaining Bench Boost opportunity (5.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 11 | 5.7 | 4.24 | 8.39 | 13.45 | 0.00 | 88.4 | 0.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 3.02 | 5.25 | 7.34 | 5.00 | 65.8 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 7.79 | 15.35 | 22.88 | 10.00 | 158.3 | 180.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 7.79 | 14.37 | 20.73 | 2.00 | 157.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.13 | 12.13 | 20.07 | 1.00 | 81.8 | 90.0 |
| XI | XI | Amari'i Bell | DEF | 12 | 3.9 | 2.82 | 6.85 | 10.84 | 1.00 | 104.7 | 180.0 |
| Bench 4 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 0.78 | 2.57 | 4.60 | 0.00 | 33.3 | 59.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 10.65 | 23.54 | 34.81 | 10.00 | 139.6 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.39 | 13.85 | 23.49 | 13.00 | 75.0 | 90.0 |
| Bench 3 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.10 | 6.89 | 12.92 | 0.00 | 30.3 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 9.70 | 17.65 | 25.40 | 5.00 | 138.1 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 16.54 | 27.06 | 15.00 | 72.6 | 68.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.10 | 11.16 | 18.35 | 2.00 | 64.3 | 70.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.8 | 2.39 | 10.94 | 19.18 | 2.00 | 61.5 | 70.0 |
| XI | XI | Sean Longstaff | MID | 15 | 4.8 | 3.63 | 9.36 | 15.10 | 2.00 | 84.7 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 55.99
- Actual score: 50.00
- Transfer: Sean Longstaff -> Alejandro Garnacho (projected gain 4.17, hit 0)
- Autosub: Auston Trusty replaced Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.58 | 4.49 | 7.61 | 0.00 | 43.9 | 0.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.34 | 3.34 | 7.30 | 0.00 | 12.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.34 | 12.66 | 20.81 | 0.00 | 85.4 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 1.94 | 10.46 | 18.06 | 0.00 | 67.2 | 0.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 2.95 | 8.21 | 12.88 | 6.00 | 71.2 | 90.0 |
| Bench 4 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.07 | 6.51 | 12.00 | 0.00 | 66.8 | 0.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 1.47 | 4.29 | 7.17 | 2.00 | 50.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.85 | 23.98 | 36.46 | 5.00 | 118.7 | 74.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.36 | 19.21 | 30.64 | 9.00 | 116.7 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.94 | 5.94 | 11.21 | 0.00 | 19.7 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 7.26 | 19.61 | 30.29 | 10.00 | 91.1 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.77 | 18.06 | 28.45 | 11.00 | 113.8 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 5.0 | 4.65 | 11.62 | 17.84 | 2.00 | 88.3 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 1.48 | 10.06 | 18.55 | 0.00 | 34.0 | 0.0 |
| XI | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 1.51 | 9.65 | 17.75 | 0.00 | 29.5 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.50 -> 2.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.63
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.91) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Richarlison de Andrade -> Douglas Luiz Soares de Paulo (projected gain 7.62, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.91) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 1.62 | 3.73 | 5.68 | 9.00 | 46.2 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.35 | 2.26 | 4.87 | 0.00 | 5.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.55 | 13.04 | 21.48 | 1.00 | 92.0 | 51.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 3.84 | 9.74 | 15.65 | 2.00 | 90.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 2.97 | 8.43 | 14.20 | 6.00 | 62.2 | 90.0 |
| Bench 2 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.27 | 4.51 | 7.47 | -1.00 | 55.9 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 0.87 | 3.37 | 6.42 | 1.00 | 47.7 | 5.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.91 | 22.32 | 34.40 | 6.00 | 109.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.71 | 17.74 | 27.80 | 13.00 | 72.4 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.68 | 3.92 | 8.29 | 0.00 | 12.3 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.15 | 18.43 | 30.21 | 7.00 | 72.0 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 7.00 | 17.30 | 27.16 | 15.00 | 106.4 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 4.32 | 12.28 | 19.31 | 4.00 | 79.9 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 5.0 | 2.13 | 9.11 | 14.60 | 2.00 | 59.8 | 81.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 2.61 | 8.32 | 14.63 | 5.00 | 40.0 | 90.0 |
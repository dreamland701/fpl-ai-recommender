# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 290.29
- Total actual points: 297.00
- Average predicted points: 72.57
- Average actual points: 74.25
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
- Predicted score: 58.79
- Actual score: 77.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.55 | 9.64 | 15.54 | 0.00 | 83.6 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.26 | 0.38 | 0.53 | 3.00 | 1.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.58 | 12.91 | 20.84 | 4.00 | 86.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.52 | 10.51 | 17.26 | 12.00 | 79.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.71 | 9.56 | 18.44 | 1.00 | 72.4 | 86.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.09 | 7.12 | 11.87 | 1.00 | 79.0 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.19 | 5.80 | 9.26 | 0.00 | 69.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.80 | 24.79 | 34.60 | 13.00 | 72.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 16.73 | 27.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 3.99 | 10.00 | 19.75 | 5.00 | 71.5 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.76 | 21.04 | 30.48 | 3.00 | 90.0 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 5.05 | 18.85 | 26.84 | 4.00 | 66.6 | 33.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.27 | 16.68 | 27.90 | 15.00 | 75.9 | 66.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.9 | 3.43 | 10.26 | 16.40 | 2.00 | 82.4 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 3.82 | 9.88 | 19.24 | 2.00 | 75.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 109.13
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (21.27) beats the best remaining Triple Captain opportunity (9.80).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (21.27) beats the best remaining Triple Captain opportunity (9.80).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.
- Autosub: Alejandro Garnacho replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.13 | 6.21 | 8.55 | 0.00 | 91.3 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 2.92 | 3.32 | 3.70 | 5.00 | 72.5 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.83 | 16.65 | 1.00 | 84.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 12.11 | 15.52 | 6.00 | 87.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.72 | 8.32 | 15.58 | 1.00 | 127.0 | 154.0 |
| Bench 3 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.94 | 6.32 | 10.54 | -1.00 | 78.0 | 79.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.28 | 3.48 | 4.80 | 0.00 | 37.8 | 59.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.97 | 29.16 | 33.84 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.45 | 14.24 | 24.15 | 13.00 | 76.5 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.64 | 8.55 | 16.47 | 0.00 | 129.6 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.01 | 20.83 | 24.96 | 5.00 | 161.7 | 180.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 9.43 | 18.66 | 22.55 | 2.00 | 110.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.18 | 17.44 | 23.19 | 15.00 | 79.0 | 68.0 |
| Bench 2 | Autosub In | Alejandro Garnacho | MID | 14 | 4.9 | 3.49 | 9.53 | 12.13 | 5.00 | 74.1 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.58 | 8.96 | 17.36 | 3.00 | 143.5 | 180.0 |

## GW26

- Train rows: 122659
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.58
- Actual score: 47.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 4.67 | 6.50 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.00 | 4.21 | 6.99 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.88 | 12.96 | 16.86 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.54 | 12.67 | 16.05 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.94 | 17.79 | 0.00 | 0.0 | 0.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.04 | 5.65 | 9.34 | 1.00 | 69.1 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.78 | 4.86 | 6.35 | 2.00 | 54.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.66 | 23.37 | 28.61 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.05 | 19.04 | 30.61 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 6.62 | 11.67 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.45 | 20.42 | 25.80 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.52 | 17.43 | 21.99 | 11.00 | 90.0 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 5.04 | 14.59 | 18.96 | 0.00 | 67.2 | 6.0 |
| Bench 3 | Bench | Ross Barkley | MID | 12 | 5.0 | 0.00 | 12.86 | 21.19 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.98 | 10.88 | 13.65 | 2.00 | 77.9 | 90.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.78
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.10) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alisson Ramses Becker -> Alphonse Areola (projected gain 21.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.10) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.60 | 9.96 | 16.10 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.23 | 2.11 | 3.92 | 9.00 | 36.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.49 | 8.74 | 17.21 | 1.00 | 88.0 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.39 | 8.02 | 15.36 | 6.00 | 80.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.14 | 7.98 | 12.16 | 5.00 | 43.7 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.17 | 5.87 | 9.37 | 1.00 | 72.9 | 90.0 |
| Bench 3 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 1.51 | 3.27 | 6.44 | -1.00 | 62.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.47 | 18.33 | 28.71 | 13.00 | 86.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.76 | 15.02 | 28.51 | 6.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.35 | 3.66 | 6.61 | 0.00 | 7.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.24 | 13.02 | 25.79 | 7.00 | 82.7 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.58 | 10.90 | 21.05 | 15.00 | 88.1 | 90.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 5.0 | 2.00 | 9.16 | 14.56 | 2.00 | 51.1 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 3.55 | 7.70 | 15.78 | 2.00 | 39.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 2.56 | 5.97 | 11.37 | 2.00 | 64.1 | 81.0 |
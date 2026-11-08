# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 289.76
- Total actual points: 288.00
- Average predicted points: 72.44
- Average actual points: 72.00
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
- Predicted score: 60.93
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.75 | 8.83 | 15.01 | 1.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.26 | 0.38 | 0.59 | 3.00 | 1.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.55 | 13.01 | 20.87 | 4.00 | 86.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.90 | 11.27 | 18.70 | 2.00 | 78.3 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.70 | 9.97 | 15.85 | 1.00 | 72.2 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.17 | 8.48 | 13.86 | 1.00 | 79.7 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.09 | 7.38 | 12.23 | 1.00 | 79.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.24 | 19.24 | 29.93 | 13.00 | 82.3 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 16.52 | 27.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 4.80 | 12.26 | 20.25 | 5.00 | 87.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.26 | 16.38 | 26.62 | 15.00 | 76.3 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.74 | 15.99 | 25.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.88 | 14.32 | 23.39 | 2.00 | 86.9 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.91 | 13.95 | 22.16 | 7.00 | 79.9 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.9 | 4.73 | 13.65 | 21.93 | 10.00 | 83.9 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 111.53
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (22.17) beats the best remaining Triple Captain opportunity (10.78).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 4.43, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (22.17) beats the best remaining Triple Captain opportunity (10.78).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.32 | 14.02 | 2.00 | 78.9 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.90 | 4.75 | 6.64 | 5.00 | 72.0 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.78 | 20.82 | 1.00 | 84.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.40 | 11.97 | 19.01 | 6.00 | 87.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.68 | 10.19 | 15.51 | 1.00 | 126.5 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.47 | 8.09 | 13.27 | 2.00 | 80.3 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.94 | 6.48 | 10.92 | -1.00 | 78.1 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 17.57 | 25.49 | 38.74 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.48 | 13.91 | 23.57 | 13.00 | 77.7 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.62 | 10.28 | 16.03 | 0.00 | 129.6 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.19 | 17.57 | 28.73 | 15.00 | 79.4 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.97 | 17.22 | 26.33 | 5.00 | 162.0 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.32 | 16.01 | 23.95 | 4.00 | 150.6 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.60 | 11.28 | 18.84 | 2.00 | 62.2 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.80 | 10.63 | 18.46 | 2.00 | 67.5 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 53.54
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 7.78 | 12.62 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.93 | 6.83 | 11.61 | 0.00 | 78.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.86 | 13.06 | 21.15 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.51 | 12.57 | 19.67 | 2.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.88 | 16.58 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.02 | 8.48 | 13.93 | 6.00 | 78.8 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.04 | 5.91 | 9.79 | 1.00 | 69.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.63 | 24.41 | 37.09 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.01 | 19.70 | 31.39 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.71 | 8.79 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.38 | 21.01 | 32.31 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.52 | 18.17 | 28.72 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.93 | 18.23 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.59 | 18.47 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.26 | 17.90 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.76
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.70) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 6.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.70) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.51 | 4.29 | 7.69 | 7.00 | 44.1 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.22 | 3.55 | 5.50 | 9.00 | 36.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.49 | 12.99 | 21.43 | 1.00 | 88.2 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.38 | 12.04 | 18.89 | 6.00 | 80.7 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.44 | 7.71 | 13.19 | 1.00 | 74.7 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.13 | 6.28 | 10.76 | 5.00 | 43.6 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.17 | 5.93 | 9.62 | 1.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.07 | 23.56 | 36.77 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.46 | 19.00 | 29.40 | 13.00 | 86.2 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.39 | 2.45 | 5.07 | 0.00 | 8.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.23 | 19.88 | 32.53 | 7.00 | 82.6 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.57 | 16.70 | 26.84 | 15.00 | 88.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.53 | 12.83 | 20.62 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.14 | 8.87 | 15.31 | 5.00 | 46.7 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.95 | 6.04 | 11.72 | 0.00 | 25.5 | 0.0 |
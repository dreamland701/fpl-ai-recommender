# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 285.82
- Total actual points: 290.00
- Average predicted points: 71.45
- Average actual points: 72.50
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
- Predicted score: 60.66
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.82 | 8.91 | 15.05 | 1.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.08 | 0.15 | 0.32 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.61 | 13.09 | 21.00 | 4.00 | 87.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.95 | 11.33 | 18.80 | 2.00 | 79.5 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.76 | 10.09 | 15.95 | 1.00 | 73.8 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.22 | 8.55 | 13.92 | 1.00 | 81.1 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.15 | 7.50 | 12.35 | 1.00 | 80.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.84 | 18.73 | 28.96 | 13.00 | 73.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.01 | 16.58 | 27.39 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 4.04 | 10.58 | 17.21 | 5.00 | 72.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.32 | 16.44 | 26.80 | 15.00 | 77.3 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.80 | 16.09 | 25.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.96 | 14.43 | 23.56 | 2.00 | 88.5 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.97 | 14.06 | 22.30 | 7.00 | 81.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.77 | 13.70 | 22.10 | 10.00 | 84.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 107.63
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.61) beats the best remaining Triple Captain opportunity (9.82).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 3.99, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.61) beats the best remaining Triple Captain opportunity (9.82).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.84 | 8.40 | 14.05 | 2.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 1.65 | 3.98 | 5.90 | 5.00 | 39.0 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.70 | 12.83 | 20.88 | 1.00 | 85.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.47 | 12.07 | 19.12 | 6.00 | 89.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.83 | 10.33 | 15.66 | 1.00 | 129.7 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.53 | 8.19 | 13.37 | 2.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.00 | 6.58 | 11.00 | -1.00 | 79.6 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 16.01 | 23.60 | 35.53 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.52 | 13.92 | 23.60 | 13.00 | 78.4 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.75 | 10.37 | 16.10 | 0.00 | 132.7 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.24 | 17.59 | 28.83 | 15.00 | 80.5 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.12 | 17.30 | 26.47 | 5.00 | 164.3 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.50 | 16.15 | 24.11 | 4.00 | 153.8 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.64 | 11.28 | 18.89 | 2.00 | 63.1 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.86 | 10.71 | 18.59 | 2.00 | 68.6 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 54.00
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.99 | 6.92 | 11.68 | 0.00 | 79.8 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.67 | 8.94 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.93 | 13.18 | 21.27 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.59 | 12.68 | 19.79 | 2.00 | 88.7 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.74 | 16.46 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.08 | 8.57 | 14.02 | 6.00 | 80.3 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.10 | 6.00 | 9.86 | 1.00 | 70.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.62 | 24.34 | 37.03 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.09 | 19.84 | 31.59 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.64 | 8.71 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.48 | 21.13 | 32.52 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.51 | 18.14 | 28.69 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 11.01 | 18.22 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.47 | 18.37 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.13 | 17.77 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.52
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.50) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 6.84, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.50) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.61 | 4.44 | 7.81 | 7.00 | 47.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.28 | 3.65 | 5.60 | 9.00 | 37.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.54 | 13.06 | 21.50 | 1.00 | 89.3 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.45 | 12.13 | 18.98 | 6.00 | 82.2 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.49 | 7.77 | 13.23 | 1.00 | 76.1 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.21 | 6.41 | 10.90 | 5.00 | 45.6 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.23 | 6.01 | 9.68 | 1.00 | 74.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.74 | 22.60 | 35.36 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.52 | 18.99 | 29.42 | 13.00 | 87.6 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 1.12 | 3.27 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.27 | 19.93 | 32.62 | 7.00 | 83.7 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.60 | 16.73 | 26.88 | 15.00 | 88.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.59 | 12.92 | 20.73 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.25 | 9.02 | 15.48 | 5.00 | 49.7 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 2.01 | 6.05 | 11.67 | 0.00 | 27.7 | 0.0 |
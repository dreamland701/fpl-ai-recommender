# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 284.51
- Total actual points: 293.00
- Average predicted points: 71.13
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
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.21
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.80 | 14.97 | 1.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.21 | 0.28 | 0.50 | 3.00 | 0.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.58 | 13.05 | 20.99 | 4.00 | 86.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.92 | 11.21 | 18.56 | 2.00 | 79.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.73 | 9.97 | 15.71 | 1.00 | 74.3 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.18 | 8.42 | 13.67 | 1.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.11 | 7.35 | 12.08 | 1.00 | 80.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.82 | 18.63 | 28.76 | 13.00 | 74.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 16.51 | 27.36 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 4.09 | 10.76 | 17.65 | 5.00 | 75.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.29 | 16.33 | 26.58 | 15.00 | 77.8 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.76 | 16.04 | 25.77 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.91 | 14.37 | 23.53 | 2.00 | 87.2 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.95 | 14.04 | 22.30 | 7.00 | 80.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.74 | 13.65 | 22.06 | 10.00 | 83.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 107.36
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.57) beats the best remaining Triple Captain opportunity (9.80).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 4.16, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.57) beats the best remaining Triple Captain opportunity (9.80).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.24 | 13.77 | 2.00 | 80.6 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.81 | 4.69 | 6.58 | 5.00 | 70.5 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.78 | 20.86 | 1.00 | 84.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 11.98 | 19.07 | 6.00 | 87.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.92 | 10.49 | 16.05 | 1.00 | 134.7 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.48 | 8.10 | 13.30 | 2.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.96 | 6.44 | 10.73 | -1.00 | 79.9 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.97 | 23.59 | 35.55 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.46 | 13.78 | 23.35 | 13.00 | 78.4 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.84 | 10.54 | 16.51 | 0.00 | 137.3 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.20 | 17.49 | 28.64 | 15.00 | 80.9 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.01 | 17.25 | 26.45 | 5.00 | 161.7 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.44 | 16.06 | 23.90 | 4.00 | 155.1 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.68 | 11.43 | 19.29 | 2.00 | 65.4 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.89 | 10.83 | 18.94 | 2.00 | 70.5 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 53.88
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.95 | 6.77 | 11.41 | 0.00 | 80.0 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.68 | 9.03 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.88 | 13.10 | 21.20 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.54 | 12.60 | 19.75 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.93 | 16.66 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.04 | 8.44 | 13.77 | 6.00 | 80.7 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.14 | 6.16 | 10.22 | 1.00 | 73.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.66 | 24.43 | 37.22 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.05 | 19.79 | 31.59 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 5.17 | 9.52 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.45 | 21.10 | 32.55 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.52 | 18.16 | 28.77 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.86 | 18.04 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.57 | 18.48 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.24 | 17.90 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.05
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.39) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 7.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.39) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.44 | 4.17 | 7.57 | 7.00 | 43.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.18 | 3.47 | 5.45 | 9.00 | 35.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.49 | 12.98 | 21.44 | 1.00 | 88.0 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.39 | 12.04 | 18.92 | 6.00 | 80.8 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.46 | 7.64 | 12.97 | 1.00 | 76.4 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.08 | 6.20 | 10.71 | 5.00 | 42.7 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.20 | 5.88 | 9.41 | 1.00 | 74.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.76 | 22.66 | 35.49 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.47 | 18.93 | 29.42 | 13.00 | 86.3 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.30 | 2.25 | 4.85 | 0.00 | 6.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.24 | 19.89 | 32.66 | 7.00 | 82.7 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.58 | 16.71 | 26.91 | 15.00 | 88.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.55 | 12.86 | 20.70 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.34 | 9.34 | 16.07 | 5.00 | 51.4 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.83 | 5.77 | 11.43 | 0.00 | 23.2 | 0.0 |
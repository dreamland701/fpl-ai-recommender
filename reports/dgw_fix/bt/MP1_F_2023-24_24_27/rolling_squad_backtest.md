# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 289.14
- Total actual points: 306.00
- Average predicted points: 72.29
- Average actual points: 76.50
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
- Predicted score: 59.77
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.80 | 14.97 | 1.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.00 | 0.00 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.62 | 13.15 | 21.15 | 4.00 | 87.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.91 | 11.27 | 18.78 | 2.00 | 78.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.65 | 9.87 | 15.67 | 1.00 | 71.0 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.09 | 8.30 | 13.62 | 1.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.00 | 7.19 | 11.95 | 1.00 | 77.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.78 | 18.62 | 28.86 | 13.00 | 72.3 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.92 | 16.44 | 27.25 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 3.93 | 10.38 | 16.95 | 5.00 | 70.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.25 | 16.36 | 26.75 | 15.00 | 75.5 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.66 | 15.79 | 25.39 | 3.00 | 89.9 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.85 | 14.23 | 23.33 | 2.00 | 85.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.90 | 13.90 | 22.09 | 7.00 | 79.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.71 | 13.64 | 22.05 | 10.00 | 83.4 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 107.06
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.83) beats the best remaining Triple Captain opportunity (9.96).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 4.02, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.83) beats the best remaining Triple Captain opportunity (9.96).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.23 | 13.89 | 2.00 | 78.1 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.77 | 4.58 | 6.36 | 5.00 | 69.0 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.64 | 12.74 | 20.81 | 1.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 11.97 | 19.07 | 6.00 | 87.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.73 | 10.24 | 15.57 | 1.00 | 127.2 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.42 | 7.96 | 13.10 | 2.00 | 79.1 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.90 | 6.37 | 10.76 | -1.00 | 77.0 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 16.23 | 23.88 | 36.02 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.34 | 13.56 | 23.15 | 13.00 | 74.0 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.58 | 10.21 | 15.93 | 0.00 | 128.3 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.51 | 28.80 | 15.00 | 78.6 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.95 | 17.16 | 26.31 | 5.00 | 160.3 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.38 | 16.04 | 23.99 | 4.00 | 150.7 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.41 | 10.81 | 18.27 | 2.00 | 57.8 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.70 | 10.39 | 18.19 | 2.00 | 64.7 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.63
- Actual score: 56.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 4.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.90 | 6.75 | 11.49 | 0.00 | 77.6 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.96 | 9.44 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.92 | 13.17 | 21.30 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.51 | 12.56 | 19.69 | 2.00 | 87.0 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.48 | 17.48 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.99 | 8.41 | 13.84 | 6.00 | 78.1 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.01 | 5.83 | 9.65 | 1.00 | 68.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.86 | 24.86 | 37.86 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.07 | 19.82 | 31.61 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.35 | 8.26 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.55 | 21.36 | 32.94 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.57 | 18.25 | 28.89 | 11.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.39 | 13.90 | 21.60 | 7.00 | 85.7 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.78 | 18.03 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.56 | 18.46 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.90 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.67
- Actual score: 93.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.81) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Martin Ødegaard (projected gain 7.08, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.81) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.30 | 3.84 | 7.00 | 7.00 | 39.6 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.10 | 3.27 | 5.09 | 9.00 | 33.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.51 | 13.01 | 21.49 | 1.00 | 88.4 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.38 | 12.04 | 18.91 | 6.00 | 80.6 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.34 | 7.47 | 12.84 | 1.00 | 72.5 | 90.0 |
| Bench 3 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.02 | 6.05 | 10.41 | 5.00 | 41.1 | 90.0 |
| Bench 2 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.14 | 5.84 | 9.47 | 1.00 | 72.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.78 | 22.73 | 35.61 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.44 | 18.90 | 29.37 | 13.00 | 85.7 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.56 | 2.85 | 5.72 | 0.00 | 12.3 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.27 | 20.00 | 32.83 | 7.00 | 83.5 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.55 | 16.63 | 26.78 | 15.00 | 87.3 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.43 | 12.79 | 21.90 | 10.00 | 67.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.06 | 10.97 | 17.74 | 1.00 | 65.6 | 31.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.01 | 8.60 | 14.95 | 5.00 | 43.8 | 90.0 |
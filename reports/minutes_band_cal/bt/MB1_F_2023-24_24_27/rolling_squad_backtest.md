# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 275.77
- Total actual points: 298.00
- Average predicted points: 68.94
- Average actual points: 74.50
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
- Predicted score: 58.74
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.85 | 8.94 | 15.09 | 1.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.21 | 0.28 | 0.50 | 3.00 | 0.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.13 | 11.74 | 19.26 | 4.00 | 79.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.92 | 11.21 | 18.56 | 2.00 | 79.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.73 | 9.97 | 15.71 | 1.00 | 74.3 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.18 | 8.42 | 13.67 | 1.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.11 | 7.35 | 12.08 | 1.00 | 80.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.82 | 18.63 | 28.76 | 13.00 | 74.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.51 | 15.20 | 25.63 | 2.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 4.09 | 10.76 | 17.65 | 5.00 | 75.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.29 | 16.33 | 26.58 | 15.00 | 77.8 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.31 | 14.73 | 24.04 | 3.00 | 82.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.05 | 14.18 | 22.42 | 7.00 | 78.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.84 | 13.79 | 22.18 | 10.00 | 82.4 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.47 | 13.06 | 21.80 | 2.00 | 79.9 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 105.05
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.69) beats the best remaining Triple Captain opportunity (9.26).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.27, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.69) beats the best remaining Triple Captain opportunity (9.26).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.24 | 13.77 | 2.00 | 80.6 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.81 | 4.69 | 6.58 | 5.00 | 70.5 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.76 | 12.91 | 20.96 | 1.00 | 82.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.43 | 12.09 | 18.92 | 6.00 | 84.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.92 | 10.49 | 16.05 | 1.00 | 134.7 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.59 | 8.23 | 13.41 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.96 | 6.44 | 10.73 | -1.00 | 79.9 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.09 | 22.31 | 33.78 | 10.00 | 165.4 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.46 | 13.78 | 23.35 | 13.00 | 78.4 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.84 | 10.54 | 16.51 | 0.00 | 137.3 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.20 | 17.49 | 28.64 | 15.00 | 80.9 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.22 | 17.38 | 26.56 | 5.00 | 158.8 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.44 | 16.06 | 23.90 | 4.00 | 155.1 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.68 | 11.43 | 19.29 | 2.00 | 65.4 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.89 | 10.83 | 18.94 | 2.00 | 70.5 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 51.02
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.95 | 6.77 | 11.41 | 0.00 | 80.0 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 4.42 | 7.18 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.23 | 11.99 | 18.61 | 2.00 | 80.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.45 | 11.84 | 19.35 | 0.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 8.67 | 14.81 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.04 | 8.44 | 13.77 | 6.00 | 80.7 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.14 | 6.16 | 10.22 | 1.00 | 73.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.24 | 23.18 | 35.37 | 5.00 | 82.7 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.62 | 18.54 | 29.74 | 9.00 | 82.7 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 5.17 | 9.52 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.02 | 19.85 | 30.71 | 10.00 | 82.7 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.09 | 16.91 | 26.92 | 11.00 | 82.7 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.86 | 18.04 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.35 | 17.96 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 9.31 | 16.64 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.96
- Actual score: 92.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.39) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Martin Ødegaard (projected gain 7.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.39) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.44 | 4.17 | 7.57 | 7.00 | 43.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.18 | 3.47 | 5.45 | 9.00 | 35.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.06 | 11.71 | 19.53 | 1.00 | 80.7 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.18 | 11.29 | 17.45 | 6.00 | 77.3 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.46 | 7.64 | 12.97 | 1.00 | 76.4 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.08 | 6.20 | 10.71 | 5.00 | 42.7 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.20 | 5.88 | 9.41 | 1.00 | 74.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.33 | 21.39 | 33.58 | 6.00 | 82.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.04 | 17.66 | 27.51 | 13.00 | 79.0 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.30 | 2.25 | 4.85 | 0.00 | 6.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.32 | 19.98 | 32.69 | 7.00 | 81.2 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.15 | 15.44 | 25.00 | 15.00 | 80.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.73 | 13.48 | 23.01 | 10.00 | 75.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.34 | 9.34 | 16.07 | 5.00 | 51.4 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.83 | 5.77 | 11.43 | 0.00 | 23.2 | 0.0 |
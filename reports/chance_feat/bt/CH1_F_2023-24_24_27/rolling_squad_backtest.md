# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 283.28
- Total actual points: 298.00
- Average predicted points: 70.82
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
- Predicted score: 60.11
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.78 | 14.93 | 1.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.27 | 0.44 | 0.72 | 3.00 | 1.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.58 | 13.05 | 20.99 | 4.00 | 86.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.89 | 11.22 | 18.68 | 2.00 | 77.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.71 | 10.04 | 15.96 | 1.00 | 72.5 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.16 | 8.44 | 13.82 | 1.00 | 79.5 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.09 | 7.38 | 12.24 | 1.00 | 79.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.81 | 18.74 | 29.07 | 13.00 | 72.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 16.44 | 27.22 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 3.99 | 10.53 | 17.18 | 5.00 | 71.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.26 | 16.29 | 26.60 | 15.00 | 75.7 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.75 | 16.03 | 25.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.91 | 14.38 | 23.55 | 2.00 | 87.2 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.96 | 14.12 | 22.46 | 7.00 | 80.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.74 | 13.66 | 22.09 | 10.00 | 83.9 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 106.84
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.59) beats the best remaining Triple Captain opportunity (9.81).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.74, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.59) beats the best remaining Triple Captain opportunity (9.81).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.76 | 8.26 | 13.90 | 2.00 | 78.5 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.95 | 4.89 | 6.89 | 5.00 | 73.1 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.76 | 20.82 | 1.00 | 84.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.32 | 11.95 | 18.79 | 6.00 | 85.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.73 | 10.27 | 15.64 | 1.00 | 127.1 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.48 | 8.09 | 13.29 | 2.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.94 | 6.47 | 10.91 | -1.00 | 78.0 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.99 | 23.63 | 35.64 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.44 | 13.72 | 23.34 | 13.00 | 76.2 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.63 | 10.27 | 16.00 | 0.00 | 129.4 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.44 | 28.64 | 15.00 | 78.7 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.01 | 17.25 | 26.44 | 5.00 | 161.6 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.41 | 16.14 | 24.18 | 4.00 | 151.4 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.57 | 11.13 | 18.70 | 2.00 | 61.3 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.78 | 10.54 | 18.38 | 2.00 | 66.4 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 53.40
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.93 | 6.80 | 11.56 | 0.00 | 78.1 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.73 | 9.13 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.88 | 13.09 | 21.19 | 0.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.21 | 12.00 | 18.74 | 2.00 | 78.7 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.95 | 16.70 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.02 | 8.49 | 13.96 | 6.00 | 78.8 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.04 | 5.89 | 9.75 | 1.00 | 69.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.66 | 24.38 | 37.12 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.05 | 19.80 | 31.59 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.59 | 8.60 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.45 | 21.10 | 32.54 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.52 | 18.17 | 28.78 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.80 | 18.02 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.54 | 18.44 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.18 | 17.79 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.93
- Actual score: 92.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.69) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Martin Ødegaard (projected gain 7.29, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.69) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.49 | 4.22 | 7.56 | 7.00 | 43.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.23 | 3.56 | 5.52 | 9.00 | 36.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.49 | 12.97 | 21.42 | 1.00 | 88.0 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.15 | 11.28 | 17.55 | 6.00 | 75.3 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.43 | 7.65 | 13.11 | 1.00 | 74.4 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.13 | 6.27 | 10.73 | 5.00 | 43.5 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.17 | 5.92 | 9.60 | 1.00 | 72.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.75 | 22.58 | 35.34 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.46 | 18.88 | 29.31 | 13.00 | 86.1 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.46 | 3.26 | 6.78 | 0.00 | 10.4 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.23 | 19.84 | 32.57 | 7.00 | 82.6 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.57 | 16.64 | 26.76 | 15.00 | 87.9 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.62 | 13.19 | 22.49 | 10.00 | 71.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.13 | 8.82 | 15.28 | 5.00 | 46.4 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.87 | 5.75 | 11.29 | 0.00 | 23.8 | 0.0 |
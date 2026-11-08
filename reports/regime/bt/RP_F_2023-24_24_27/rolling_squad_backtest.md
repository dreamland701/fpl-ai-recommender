# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 283.46
- Total actual points: 298.00
- Average predicted points: 70.87
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
- Predicted score: 60.03
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.71 | 8.66 | 14.68 | 1.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.31 | 0.51 | 0.81 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.59 | 13.09 | 21.07 | 4.00 | 87.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.89 | 11.23 | 18.72 | 2.00 | 79.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.72 | 10.05 | 15.97 | 1.00 | 73.0 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.15 | 8.44 | 13.82 | 1.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.07 | 7.29 | 12.07 | 1.00 | 79.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.85 | 18.86 | 29.27 | 13.00 | 73.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.87 | 16.18 | 26.75 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 3.92 | 10.23 | 16.62 | 5.00 | 70.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.27 | 16.40 | 26.83 | 15.00 | 76.8 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.74 | 15.98 | 25.67 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.93 | 14.45 | 23.70 | 2.00 | 88.5 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.95 | 14.04 | 22.31 | 7.00 | 80.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.66 | 13.39 | 21.60 | 10.00 | 84.3 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 107.00
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.64) beats the best remaining Triple Captain opportunity (9.84).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.70, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.64) beats the best remaining Triple Captain opportunity (9.84).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.16 | 13.70 | 2.00 | 75.9 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.99 | 4.90 | 6.85 | 5.00 | 67.2 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.65 | 12.76 | 20.83 | 1.00 | 85.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.32 | 11.95 | 18.82 | 6.00 | 87.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.80 | 10.38 | 15.82 | 1.00 | 126.9 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.48 | 8.12 | 13.34 | 2.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.94 | 6.45 | 10.88 | -1.00 | 78.9 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 16.04 | 23.70 | 35.76 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.38 | 13.58 | 23.09 | 13.00 | 76.1 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.51 | 10.05 | 15.59 | 0.00 | 127.0 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.50 | 28.79 | 15.00 | 80.1 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.99 | 17.22 | 26.40 | 5.00 | 161.5 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.44 | 16.17 | 24.24 | 4.00 | 152.2 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.60 | 11.29 | 19.04 | 2.00 | 62.8 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.72 | 10.34 | 18.05 | 2.00 | 67.0 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 53.50
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.92 | 6.77 | 11.48 | 0.00 | 75.4 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.74 | 9.11 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.87 | 13.05 | 21.13 | 0.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.21 | 12.03 | 18.81 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.08 | 16.93 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.02 | 8.50 | 13.99 | 6.00 | 80.0 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.05 | 5.96 | 9.88 | 1.00 | 70.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.73 | 24.68 | 37.68 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.00 | 19.61 | 31.25 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.39 | 8.20 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.43 | 21.07 | 32.50 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.52 | 18.18 | 28.80 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 11.00 | 18.42 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.33 | 18.10 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.31 | 18.02 | 0.00 | 0.0 | 0.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.60) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Martin Ødegaard (projected gain 7.40, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.60) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.51 | 4.29 | 7.67 | 7.00 | 41.3 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.24 | 3.60 | 5.57 | 9.00 | 34.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.48 | 12.95 | 21.39 | 1.00 | 89.1 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.15 | 11.30 | 17.62 | 6.00 | 77.0 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.43 | 7.67 | 13.15 | 1.00 | 75.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.19 | 6.47 | 11.10 | 5.00 | 44.1 | 90.0 |
| Bench 2 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.19 | 5.99 | 9.75 | 1.00 | 74.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.83 | 22.93 | 35.98 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.41 | 18.71 | 28.98 | 13.00 | 85.9 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.28 | 2.04 | 4.35 | 0.00 | 6.3 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.24 | 19.91 | 32.70 | 7.00 | 84.5 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.59 | 16.74 | 26.96 | 15.00 | 88.3 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.63 | 13.25 | 22.59 | 10.00 | 70.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.05 | 8.55 | 14.77 | 5.00 | 46.7 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.90 | 5.92 | 11.63 | 0.00 | 25.7 | 0.0 |
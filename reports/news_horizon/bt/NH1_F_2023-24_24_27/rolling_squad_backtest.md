# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 282.43
- Total actual points: 298.00
- Average predicted points: 70.61
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
- Predicted score: 59.90
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.75 | 8.79 | 14.92 | 1.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.25 | 0.43 | 0.75 | 3.00 | 1.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.55 | 13.04 | 21.02 | 4.00 | 85.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.90 | 11.23 | 18.69 | 2.00 | 77.9 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.69 | 10.03 | 15.98 | 1.00 | 72.1 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.17 | 8.46 | 13.82 | 1.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.10 | 7.39 | 12.23 | 1.00 | 79.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.76 | 18.70 | 29.12 | 13.00 | 71.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.96 | 16.47 | 27.25 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 3.97 | 10.51 | 17.21 | 5.00 | 71.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.26 | 16.30 | 26.60 | 15.00 | 75.8 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.75 | 16.04 | 25.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.89 | 14.37 | 23.58 | 2.00 | 86.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.92 | 14.09 | 22.51 | 7.00 | 79.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.72 | 13.65 | 22.10 | 10.00 | 83.5 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 106.27
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.46) beats the best remaining Triple Captain opportunity (9.73).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.68, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.46) beats the best remaining Triple Captain opportunity (9.73).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.77 | 8.27 | 13.90 | 2.00 | 78.9 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.85 | 4.86 | 6.93 | 5.00 | 70.9 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.64 | 12.76 | 20.86 | 1.00 | 83.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.31 | 11.95 | 18.82 | 6.00 | 85.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.69 | 10.27 | 15.68 | 1.00 | 126.3 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.49 | 8.11 | 13.29 | 2.00 | 80.7 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.95 | 6.48 | 10.90 | -1.00 | 78.3 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.86 | 23.59 | 35.70 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.47 | 13.77 | 23.35 | 13.00 | 77.1 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.60 | 10.27 | 16.04 | 0.00 | 128.8 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.18 | 17.46 | 28.66 | 15.00 | 79.0 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.99 | 17.25 | 26.47 | 5.00 | 161.2 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.35 | 16.14 | 24.24 | 4.00 | 150.1 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.59 | 11.15 | 18.71 | 2.00 | 61.7 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.80 | 10.56 | 18.39 | 2.00 | 66.8 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 53.31
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.94 | 6.82 | 11.56 | 0.00 | 78.5 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.70 | 9.20 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.88 | 13.10 | 21.19 | 0.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.20 | 12.01 | 18.77 | 2.00 | 78.6 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.95 | 16.75 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.03 | 8.50 | 13.96 | 6.00 | 79.0 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.05 | 5.90 | 9.74 | 1.00 | 69.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.61 | 24.37 | 37.21 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.06 | 19.80 | 31.59 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.63 | 8.59 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.43 | 21.09 | 32.57 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.49 | 18.16 | 28.84 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.83 | 18.06 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.56 | 18.43 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.22 | 17.79 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.94
- Actual score: 92.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Martin Ødegaard (projected gain 7.28, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.52 | 4.25 | 7.55 | 7.00 | 44.5 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.21 | 3.57 | 5.58 | 9.00 | 36.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.49 | 12.98 | 21.42 | 1.00 | 88.1 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.15 | 11.29 | 17.59 | 6.00 | 75.2 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.44 | 7.66 | 13.11 | 1.00 | 74.6 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.15 | 6.29 | 10.74 | 5.00 | 43.9 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.18 | 5.93 | 9.59 | 1.00 | 73.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.71 | 22.58 | 35.41 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.45 | 18.88 | 29.32 | 13.00 | 85.9 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.43 | 2.97 | 6.24 | 0.00 | 9.5 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.22 | 19.84 | 32.60 | 7.00 | 82.4 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.58 | 16.66 | 26.81 | 15.00 | 88.0 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.64 | 13.21 | 22.50 | 10.00 | 71.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.15 | 8.84 | 15.27 | 5.00 | 46.8 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.92 | 5.80 | 11.27 | 0.00 | 24.9 | 0.0 |
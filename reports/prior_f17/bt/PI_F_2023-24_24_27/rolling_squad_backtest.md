# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 282.45
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
- Predicted score: 59.94
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.76 | 8.86 | 15.11 | 1.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.35 | 0.70 | 1.24 | 3.00 | 3.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.58 | 13.04 | 20.96 | 4.00 | 86.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.88 | 11.19 | 18.65 | 2.00 | 77.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.71 | 9.98 | 15.82 | 1.00 | 72.1 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.16 | 8.42 | 13.75 | 1.00 | 79.2 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.08 | 7.34 | 12.14 | 1.00 | 78.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.71 | 18.43 | 28.54 | 13.00 | 72.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.99 | 16.59 | 27.49 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 3.98 | 10.48 | 17.07 | 5.00 | 71.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.27 | 16.38 | 26.79 | 15.00 | 76.0 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.73 | 15.97 | 25.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.94 | 14.41 | 23.58 | 2.00 | 86.9 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.02 | 14.25 | 22.66 | 7.00 | 80.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.65 | 13.46 | 21.78 | 10.00 | 84.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 106.59
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.37) beats the best remaining Triple Captain opportunity (9.68).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.62, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.37) beats the best remaining Triple Captain opportunity (9.68).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.77 | 8.35 | 14.11 | 2.00 | 79.3 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 3.10 | 5.10 | 7.28 | 5.00 | 74.8 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.77 | 20.83 | 1.00 | 84.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.32 | 11.91 | 18.71 | 6.00 | 85.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.73 | 10.23 | 15.53 | 1.00 | 126.5 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.48 | 8.06 | 13.20 | 2.00 | 80.1 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.93 | 6.42 | 10.79 | -1.00 | 77.7 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.77 | 23.30 | 35.07 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.47 | 13.88 | 23.65 | 13.00 | 76.4 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.63 | 10.25 | 15.95 | 0.00 | 129.0 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.19 | 17.55 | 28.87 | 15.00 | 79.1 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.00 | 17.22 | 26.40 | 5.00 | 161.6 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.57 | 16.33 | 24.47 | 4.00 | 150.7 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.61 | 11.25 | 18.91 | 2.00 | 61.3 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.71 | 10.41 | 18.23 | 2.00 | 66.8 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 53.22
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.94 | 6.89 | 11.76 | 0.00 | 78.9 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.96 | 9.58 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.88 | 13.07 | 21.15 | 0.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.22 | 12.01 | 18.71 | 2.00 | 78.6 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.89 | 16.56 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.02 | 8.45 | 13.87 | 6.00 | 78.5 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.03 | 5.85 | 9.66 | 1.00 | 68.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.54 | 24.10 | 36.68 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.09 | 19.89 | 31.75 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.65 | 8.69 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.46 | 21.14 | 32.61 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.51 | 18.15 | 28.73 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.86 | 18.16 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.43 | 18.31 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.30 | 17.99 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.69
- Actual score: 92.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Martin Ødegaard (projected gain 7.42, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.51 | 4.35 | 7.84 | 7.00 | 44.7 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.32 | 3.87 | 6.11 | 9.00 | 37.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.48 | 12.96 | 21.39 | 1.00 | 87.9 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.16 | 11.30 | 17.57 | 6.00 | 75.3 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.43 | 7.65 | 13.08 | 1.00 | 74.2 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.13 | 6.26 | 10.71 | 5.00 | 43.5 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.16 | 5.86 | 9.49 | 1.00 | 72.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.59 | 22.25 | 34.85 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.52 | 19.02 | 29.54 | 13.00 | 86.2 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.35 | 2.31 | 4.85 | 0.00 | 7.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.25 | 19.94 | 32.74 | 7.00 | 82.9 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.57 | 16.67 | 26.84 | 15.00 | 88.1 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.65 | 13.31 | 22.70 | 10.00 | 71.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.06 | 8.70 | 15.12 | 5.00 | 46.5 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.92 | 5.93 | 11.60 | 0.00 | 24.1 | 0.0 |
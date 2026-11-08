# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 299.68
- Total actual points: 322.00
- Average predicted points: 74.92
- Average actual points: 80.50
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
- Predicted score: 61.85
- Actual score: 75.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.76 | 8.83 | 15.03 | 1.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.26 | 0.37 | 0.59 | 3.00 | 1.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.57 | 13.03 | 20.93 | 4.00 | 86.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.93 | 11.32 | 18.80 | 2.00 | 78.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.54 | 10.44 | 16.76 | 12.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.10 | 7.42 | 12.29 | 1.00 | 79.2 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.08 | 7.31 | 11.69 | 1.00 | 77.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.49 | 19.76 | 30.38 | 13.00 | 86.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.98 | 16.56 | 27.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 5.20 | 13.95 | 22.30 | 6.00 | 68.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.32 | 16.49 | 26.81 | 15.00 | 76.9 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.76 | 16.04 | 25.73 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.91 | 14.35 | 23.45 | 2.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.9 | 4.75 | 13.69 | 22.01 | 10.00 | 84.1 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 4.90 | 12.08 | 19.90 | 2.00 | 90.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 105.39
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.08) beats the best remaining Triple Captain opportunity (9.71).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.15, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.08) beats the best remaining Triple Captain opportunity (9.71).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.79 | 8.34 | 14.05 | 2.00 | 79.2 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.90 | 4.76 | 6.64 | 5.00 | 72.1 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.80 | 20.87 | 1.00 | 84.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 12.01 | 19.09 | 6.00 | 87.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.31 | 11.94 | 18.77 | 6.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.89 | 7.81 | 12.39 | 2.00 | 77.9 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.95 | 6.49 | 10.94 | -1.00 | 78.1 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.83 | 23.45 | 35.31 | 10.00 | 180.0 | 180.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 10.65 | 16.40 | 24.85 | 5.00 | 142.1 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.52 | 13.98 | 23.68 | 13.00 | 78.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.21 | 17.61 | 28.81 | 15.00 | 79.8 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.04 | 17.27 | 26.43 | 5.00 | 162.5 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.63 | 11.32 | 18.91 | 2.00 | 62.6 | 70.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.86 | 10.73 | 18.63 | 2.00 | 68.0 | 70.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.56 | 10.64 | 16.92 | 3.00 | 143.3 | 180.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.79
- Actual score: 61.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 5.78, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.94 | 6.84 | 11.63 | 0.00 | 78.4 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.68 | 9.04 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.89 | 13.12 | 21.23 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.53 | 12.60 | 19.73 | 2.00 | 87.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.20 | 12.03 | 18.77 | 2.00 | 78.9 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.51 | 7.88 | 12.39 | 9.00 | 79.3 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.04 | 5.92 | 9.79 | 1.00 | 69.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.65 | 24.43 | 37.13 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.01 | 19.73 | 31.43 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 0.00 | 10.39 | 16.12 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.41 | 21.06 | 32.38 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.53 | 18.21 | 28.80 | 11.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.44 | 14.02 | 21.75 | 7.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Ross Barkley | MID | 12 | 5.0 | 0.00 | 11.72 | 19.75 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 9.44 | 17.12 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 1.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 70.66
- Actual score: 95.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.97) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Caoimhin Kelleher -> Alphonse Areola (projected gain 5.73, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.97) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.59 | 9.80 | 15.84 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 1.51 | 4.30 | 7.70 | 7.00 | 44.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.50 | 13.01 | 21.49 | 1.00 | 88.3 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.39 | 12.07 | 18.95 | 6.00 | 80.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.16 | 11.34 | 17.66 | 6.00 | 75.6 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 3.14 | 8.48 | 14.02 | 1.00 | 81.5 | 90.0 |
| Bench 3 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.17 | 5.93 | 9.63 | 1.00 | 73.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.60 | 24.36 | 37.96 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.49 | 19.02 | 29.44 | 13.00 | 86.7 | 90.0 |
| Bench 2 | Bench Boost | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 2.26 | 7.08 | 12.81 | 5.00 | 22.3 | 30.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.22 | 19.88 | 32.61 | 7.00 | 82.9 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.60 | 16.76 | 26.95 | 15.00 | 88.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.25 | 11.42 | 18.40 | 1.00 | 69.6 | 31.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.15 | 8.90 | 15.38 | 5.00 | 46.9 | 90.0 |
| Bench 4 | Bench Boost | Ross Barkley | MID | 12 | 5.0 | 2.03 | 7.00 | 12.23 | 2.00 | 51.7 | 90.0 |
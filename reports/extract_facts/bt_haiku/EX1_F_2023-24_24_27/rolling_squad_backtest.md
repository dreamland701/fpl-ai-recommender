# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 303.46
- Total actual points: 323.00
- Average predicted points: 75.86
- Average actual points: 80.75
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
- Predicted score: 60.75
- Actual score: 83.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.75 | 8.82 | 15.01 | 1.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.26 | 0.38 | 0.59 | 3.00 | 1.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.55 | 13.00 | 20.86 | 4.00 | 86.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.90 | 11.26 | 18.69 | 2.00 | 78.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.52 | 10.39 | 16.67 | 12.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.09 | 7.38 | 12.23 | 1.00 | 79.0 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.06 | 7.28 | 11.65 | 1.00 | 77.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.26 | 19.32 | 29.81 | 13.00 | 82.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 16.50 | 27.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 4.96 | 13.67 | 21.92 | 6.00 | 67.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.25 | 16.36 | 26.60 | 15.00 | 76.3 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.73 | 15.98 | 25.64 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.88 | 14.30 | 23.38 | 2.00 | 86.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.73 | 13.64 | 21.92 | 10.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 5.0 | 4.49 | 11.97 | 19.59 | 2.00 | 90.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 110.16
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (21.76) beats the best remaining Triple Captain opportunity (10.74).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.13, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (21.76) beats the best remaining Triple Captain opportunity (10.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.31 | 14.02 | 2.00 | 78.9 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.90 | 4.75 | 6.64 | 5.00 | 72.0 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.65 | 12.77 | 20.81 | 1.00 | 84.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.40 | 11.96 | 19.01 | 6.00 | 87.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.30 | 11.91 | 18.71 | 6.00 | 85.5 | 90.0 |
| Bench 2 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.89 | 7.80 | 12.39 | 2.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.94 | 6.48 | 10.92 | -1.00 | 78.0 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 17.51 | 25.47 | 38.70 | 10.00 | 180.0 | 180.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 10.64 | 16.39 | 24.83 | 5.00 | 141.8 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.48 | 13.89 | 23.54 | 13.00 | 77.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.18 | 17.55 | 28.69 | 15.00 | 79.4 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.96 | 17.21 | 26.32 | 5.00 | 162.0 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.60 | 11.26 | 18.82 | 2.00 | 62.2 | 70.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.80 | 10.62 | 18.43 | 2.00 | 67.5 | 70.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.54 | 10.60 | 16.86 | 3.00 | 143.0 | 180.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.20
- Actual score: 56.00
- Transfer: Darwin Núñez Ribeiro -> Ivan Toney (projected gain 5.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 7.78 | 12.59 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.93 | 6.83 | 11.61 | 0.00 | 78.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.86 | 13.06 | 21.14 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.51 | 12.57 | 19.67 | 2.00 | 87.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.19 | 12.01 | 18.73 | 2.00 | 78.6 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.50 | 7.86 | 12.36 | 9.00 | 79.1 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.04 | 5.91 | 9.79 | 1.00 | 69.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.63 | 24.39 | 37.06 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.01 | 19.68 | 31.38 | 9.00 | 90.0 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 5.00 | 14.50 | 22.97 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.38 | 20.99 | 32.29 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.51 | 18.16 | 28.71 | 11.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 5.0 | 0.00 | 11.69 | 19.70 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.58 | 18.46 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.26 | 17.90 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 70.35
- Actual score: 93.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.35) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Martin Dubravka -> Alphonse Areola (projected gain 5.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.35) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.59 | 9.78 | 15.80 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.22 | 3.55 | 5.50 | 9.00 | 36.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.49 | 12.98 | 21.42 | 1.00 | 88.2 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.38 | 12.03 | 18.88 | 6.00 | 80.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.15 | 11.32 | 17.61 | 6.00 | 75.4 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 3.13 | 8.47 | 13.99 | 1.00 | 81.4 | 90.0 |
| Bench 2 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.17 | 5.93 | 9.62 | 1.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.10 | 23.57 | 36.66 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.45 | 18.98 | 29.38 | 13.00 | 86.2 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 4.67 | 13.86 | 23.11 | 2.00 | 89.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.22 | 19.85 | 32.51 | 7.00 | 82.6 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.57 | 16.69 | 26.82 | 15.00 | 88.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.14 | 8.86 | 15.30 | 5.00 | 46.7 | 90.0 |
| Bench 3 | Bench Boost | Ross Barkley | MID | 12 | 5.0 | 2.01 | 6.99 | 12.18 | 2.00 | 51.6 | 90.0 |
| Bench 4 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.95 | 6.03 | 11.70 | 0.00 | 25.5 | 0.0 |
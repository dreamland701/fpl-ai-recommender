# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 305.96
- Total actual points: 320.00
- Average predicted points: 76.49
- Average actual points: 80.00
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
- Predicted score: 62.08
- Actual score: 74.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.55 | 9.20 | 15.29 | 0.00 | 67.7 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.12 | 0.16 | 0.33 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.59 | 13.07 | 20.94 | 4.00 | 87.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.98 | 11.39 | 18.84 | 2.00 | 79.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.59 | 10.51 | 16.80 | 12.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.16 | 7.51 | 12.36 | 1.00 | 80.6 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.13 | 7.38 | 11.73 | 1.00 | 79.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.54 | 19.80 | 30.34 | 13.00 | 87.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.02 | 16.61 | 27.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 5.28 | 14.01 | 22.24 | 6.00 | 70.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.36 | 16.54 | 26.82 | 15.00 | 77.9 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.79 | 16.07 | 25.72 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.95 | 14.40 | 23.48 | 2.00 | 88.4 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.9 | 4.78 | 13.73 | 22.03 | 10.00 | 85.0 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 4.89 | 12.06 | 19.86 | 2.00 | 90.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 106.48
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.12) beats the best remaining Triple Captain opportunity (9.74).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.16, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.12) beats the best remaining Triple Captain opportunity (9.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.34 | 9.31 | 15.11 | 3.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 2.53 | 4.47 | 6.32 | 5.00 | 59.7 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.69 | 12.84 | 20.88 | 1.00 | 85.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.47 | 12.08 | 19.12 | 6.00 | 89.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.35 | 11.99 | 18.78 | 6.00 | 86.7 | 90.0 |
| Bench 2 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.94 | 7.87 | 12.41 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.00 | 6.58 | 11.01 | -1.00 | 79.6 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.87 | 23.47 | 35.30 | 10.00 | 180.0 | 180.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 10.76 | 16.45 | 24.87 | 5.00 | 145.4 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.57 | 14.04 | 23.71 | 13.00 | 79.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 17.64 | 28.79 | 15.00 | 80.9 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.12 | 17.31 | 26.43 | 5.00 | 164.7 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.68 | 11.38 | 18.95 | 2.00 | 63.8 | 70.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.92 | 10.82 | 18.71 | 2.00 | 69.6 | 70.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.64 | 10.70 | 16.97 | 3.00 | 145.4 | 180.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.86
- Actual score: 63.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 5.73, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.79 | 10.05 | 16.36 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.67 | 8.94 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.93 | 13.18 | 21.28 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.57 | 12.67 | 19.76 | 2.00 | 88.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.25 | 12.08 | 18.79 | 2.00 | 79.9 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.57 | 7.96 | 12.43 | 9.00 | 80.7 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.10 | 6.01 | 9.86 | 1.00 | 70.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.60 | 24.33 | 36.95 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.04 | 19.76 | 31.42 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 0.00 | 10.58 | 16.13 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.43 | 21.08 | 32.35 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.51 | 18.18 | 28.72 | 11.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.47 | 14.06 | 21.76 | 7.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Ross Barkley | MID | 12 | 5.0 | 0.00 | 11.52 | 19.54 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 9.52 | 17.18 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.54
- Actual score: 94.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.79) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Darwin Núñez Ribeiro -> Ivan Toney (projected gain 5.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.64 | 9.88 | 15.90 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.27 | 3.63 | 5.57 | 9.00 | 37.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.54 | 13.08 | 21.54 | 1.00 | 89.5 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.45 | 12.14 | 18.98 | 6.00 | 82.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.20 | 11.39 | 17.65 | 6.00 | 76.6 | 90.0 |
| Bench 2 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.1 | 3.20 | 8.56 | 14.07 | 1.00 | 83.0 | 90.0 |
| Bench 3 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.23 | 6.01 | 9.69 | 1.00 | 74.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.57 | 24.26 | 37.77 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.53 | 19.06 | 29.44 | 13.00 | 87.9 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 4.86 | 14.04 | 23.46 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.24 | 19.90 | 32.56 | 7.00 | 83.6 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.61 | 16.76 | 26.91 | 15.00 | 88.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.28 | 11.45 | 18.40 | 1.00 | 70.5 | 31.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.25 | 9.05 | 15.51 | 5.00 | 49.9 | 90.0 |
| Bench 4 | Bench Boost | Ross Barkley | MID | 12 | 5.0 | 2.10 | 7.10 | 12.31 | 2.00 | 53.8 | 90.0 |
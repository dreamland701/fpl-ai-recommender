# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 309.93
- Total actual points: 326.00
- Average predicted points: 77.48
- Average actual points: 81.50
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
- Predicted score: 61.05
- Actual score: 82.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.53 | 9.19 | 15.22 | 0.00 | 67.4 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.12 | 0.16 | 0.34 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.58 | 13.04 | 20.88 | 4.00 | 87.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.95 | 11.33 | 18.74 | 2.00 | 79.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.57 | 10.47 | 16.72 | 12.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.14 | 7.47 | 12.30 | 1.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.12 | 7.36 | 11.69 | 1.00 | 78.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.31 | 19.35 | 29.76 | 13.00 | 83.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.00 | 16.56 | 27.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 5.04 | 13.75 | 21.91 | 6.00 | 69.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.29 | 16.41 | 26.63 | 15.00 | 77.4 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.77 | 16.02 | 25.63 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.92 | 14.36 | 23.41 | 2.00 | 88.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.76 | 13.69 | 21.96 | 10.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 5.0 | 4.49 | 11.96 | 19.56 | 2.00 | 90.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 111.07
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (21.72) beats the best remaining Triple Captain opportunity (10.72).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.14, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (21.72) beats the best remaining Triple Captain opportunity (10.72).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.33 | 9.28 | 15.06 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 2.52 | 4.47 | 6.32 | 5.00 | 59.7 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.69 | 12.81 | 20.82 | 1.00 | 85.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.45 | 12.04 | 19.05 | 6.00 | 88.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.34 | 11.96 | 18.73 | 6.00 | 86.5 | 90.0 |
| Bench 2 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.94 | 7.86 | 12.41 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.00 | 6.56 | 10.99 | -1.00 | 79.6 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 17.47 | 25.44 | 38.65 | 10.00 | 180.0 | 180.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 10.75 | 16.44 | 24.84 | 5.00 | 145.1 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.53 | 13.96 | 23.58 | 13.00 | 79.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.23 | 17.59 | 28.69 | 15.00 | 80.6 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.05 | 17.25 | 26.33 | 5.00 | 164.3 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.65 | 11.34 | 18.87 | 2.00 | 63.5 | 70.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.86 | 10.72 | 18.52 | 2.00 | 69.3 | 70.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.62 | 10.66 | 16.91 | 3.00 | 145.1 | 180.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.25
- Actual score: 58.00
- Transfer: Darwin Núñez Ribeiro -> Ivan Toney (projected gain 5.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.78 | 10.03 | 16.33 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 7.72 | 12.45 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.91 | 13.13 | 21.20 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.56 | 12.63 | 19.71 | 2.00 | 88.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.24 | 12.06 | 18.75 | 2.00 | 79.7 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.56 | 7.94 | 12.41 | 9.00 | 80.6 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.10 | 6.00 | 9.85 | 1.00 | 70.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.58 | 24.30 | 36.89 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.04 | 19.72 | 31.37 | 9.00 | 90.0 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 4.99 | 14.48 | 22.92 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.40 | 21.02 | 32.26 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.50 | 18.13 | 28.63 | 11.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 5.0 | 0.00 | 11.49 | 19.49 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.48 | 18.35 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.14 | 17.77 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.57
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.77) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Richarlison de Andrade -> Douglas Luiz Soares de Paulo (projected gain 4.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.77) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.64 | 9.86 | 15.86 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.26 | 3.62 | 5.55 | 9.00 | 37.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.53 | 13.05 | 21.47 | 1.00 | 89.4 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.44 | 12.11 | 18.92 | 6.00 | 82.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.19 | 11.38 | 17.61 | 6.00 | 76.4 | 90.0 |
| Bench 2 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.1 | 3.19 | 8.55 | 14.03 | 1.00 | 82.8 | 90.0 |
| Bench 3 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.23 | 6.01 | 9.68 | 1.00 | 74.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.09 | 23.51 | 36.50 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.50 | 19.03 | 29.40 | 13.00 | 87.5 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 4.69 | 13.83 | 23.01 | 2.00 | 89.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.25 | 19.87 | 32.47 | 7.00 | 83.3 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.58 | 16.69 | 26.79 | 15.00 | 88.3 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 4.55 | 12.77 | 19.87 | 4.00 | 84.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.24 | 9.02 | 15.43 | 5.00 | 49.7 | 90.0 |
| Bench 4 | Bench Boost | Ross Barkley | MID | 12 | 5.0 | 2.08 | 7.09 | 12.26 | 2.00 | 53.7 | 90.0 |
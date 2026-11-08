# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 288.15
- Total actual points: 322.00
- Average predicted points: 72.04
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
- Predicted score: 60.41
- Actual score: 80.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.61 | 9.46 | 15.29 | 0.00 | 83.9 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 0.33 | 0.20 | 0.23 | 3.00 | 2.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.55 | 13.07 | 20.94 | 4.00 | 86.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.92 | 11.22 | 18.75 | 2.00 | 78.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.51 | 10.37 | 16.57 | 12.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 10 | 4.4 | 2.92 | 8.23 | 13.44 | 2.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.03 | 7.17 | 11.85 | 1.00 | 79.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.79 | 18.69 | 28.83 | 13.00 | 73.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 16.40 | 27.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.69 | 12.51 | 20.51 | 1.00 | 86.5 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.25 | 16.33 | 26.64 | 15.00 | 76.4 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.73 | 16.04 | 25.66 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.93 | 14.33 | 23.53 | 2.00 | 87.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.71 | 13.65 | 22.08 | 10.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.9 | 3.49 | 10.74 | 17.40 | 2.00 | 82.6 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 97.84
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.98) beats the best remaining Triple Captain opportunity (9.87).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 3.83, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.98) beats the best remaining Triple Captain opportunity (9.87).
- Autosub: Caoimhin Kelleher replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.14 | 7.05 | 11.75 | 0.00 | 93.6 | 0.0 |
| Bench 1 | Autosub In | Caoimhin Kelleher | GK | 11 | 3.7 | 2.95 | 4.68 | 6.53 | 5.00 | 75.1 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.83 | 20.86 | 1.00 | 84.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.54 | 11.94 | 18.94 | 6.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.44 | 11.94 | 18.71 | 6.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Antonee Robinson | DEF | 10 | 4.4 | 2.73 | 8.14 | 13.31 | 5.00 | 75.1 | 90.0 |
| Bench 3 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.91 | 6.30 | 10.59 | -1.00 | 78.8 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 16.08 | 23.68 | 35.55 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.41 | 13.64 | 23.40 | 13.00 | 77.2 | 90.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.08 | 5.82 | 11.05 | 0.00 | 26.8 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.28 | 17.54 | 28.73 | 15.00 | 78.8 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.09 | 17.35 | 26.47 | 5.00 | 162.8 | 180.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.52 | 11.04 | 18.62 | 2.00 | 62.2 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.87 | 10.74 | 18.77 | 2.00 | 66.7 | 70.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.66 | 10.18 | 16.32 | 5.00 | 74.0 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.17
- Actual score: 55.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 8.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.56 | 8.85 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.00 | 4.06 | 8.31 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.01 | 13.46 | 21.60 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.62 | 12.77 | 19.88 | 2.00 | 88.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.29 | 12.22 | 18.95 | 2.00 | 79.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.53 | 8.16 | 13.60 | 2.00 | 78.0 | 90.0 |
| Bench 2 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.92 | 5.56 | 9.29 | 1.00 | 70.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.66 | 24.52 | 37.30 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.94 | 19.54 | 31.33 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.88 | 5.49 | 10.55 | 0.00 | 21.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.50 | 21.32 | 32.71 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.50 | 18.23 | 28.84 | 11.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.44 | 14.03 | 21.90 | 7.00 | 87.3 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 4.03 | 11.63 | 18.07 | 2.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.57 | 18.50 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 1.40 -> 2.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 67.72
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.49) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alisson Ramses Becker -> Alphonse Areola (projected gain 6.81, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.49) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.58 | 9.78 | 15.82 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.15 | 3.36 | 5.27 | 9.00 | 37.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.49 | 13.19 | 21.69 | 1.00 | 88.2 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.53 | 11.98 | 18.83 | 6.00 | 81.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.29 | 11.30 | 17.58 | 6.00 | 76.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.4 | 2.80 | 8.18 | 13.40 | 6.00 | 75.0 | 90.0 |
| Bench 3 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.00 | 5.53 | 9.05 | 1.00 | 74.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.83 | 22.85 | 35.76 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.52 | 18.77 | 29.08 | 13.00 | 86.1 | 90.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.61 | 3.32 | 7.31 | 0.00 | 10.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.33 | 19.95 | 32.62 | 7.00 | 82.6 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.65 | 16.93 | 27.18 | 15.00 | 88.6 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.27 | 11.48 | 18.56 | 1.00 | 69.6 | 31.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.9 | 2.73 | 9.70 | 15.18 | 2.00 | 64.1 | 81.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.13 | 8.84 | 15.33 | 5.00 | 47.1 | 90.0 |
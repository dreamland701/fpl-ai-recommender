# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 291.53
- Total actual points: 326.00
- Average predicted points: 72.88
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
- Predicted score: 59.57
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.79 | 8.94 | 15.16 | 1.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.09 | 0.04 | 0.07 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.59 | 13.13 | 21.11 | 4.00 | 87.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.83 | 11.21 | 18.73 | 2.00 | 78.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.55 | 10.48 | 16.81 | 12.00 | 78.9 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.05 | 7.28 | 12.03 | 1.00 | 77.0 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.20 | 6.93 | 11.25 | 1.00 | 73.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.69 | 18.39 | 28.56 | 13.00 | 72.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.84 | 16.29 | 27.07 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 2.08 | 5.44 | 8.73 | 13.00 | 45.8 | 74.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.34 | 16.58 | 27.02 | 15.00 | 75.1 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.69 | 15.87 | 25.50 | 3.00 | 89.9 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.81 | 14.25 | 23.39 | 2.00 | 85.9 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.95 | 14.07 | 22.35 | 7.00 | 79.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.79 | 13.84 | 22.30 | 10.00 | 83.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 103.47
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.18) beats the best remaining Triple Captain opportunity (9.99).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.84, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.18) beats the best remaining Triple Captain opportunity (9.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.69 | 8.12 | 13.74 | 2.00 | 78.3 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.92 | 4.97 | 6.94 | 5.00 | 68.5 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.51 | 12.45 | 20.42 | 1.00 | 84.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.32 | 11.97 | 18.83 | 6.00 | 84.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 11.96 | 19.04 | 6.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.49 | 7.15 | 11.62 | 6.00 | 72.9 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.96 | 6.51 | 10.94 | -1.00 | 76.8 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 16.28 | 24.12 | 36.40 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.33 | 13.62 | 23.24 | 13.00 | 74.0 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 2.33 | 6.71 | 10.90 | 8.00 | 55.4 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.26 | 17.70 | 27.12 | 5.00 | 159.4 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.48 | 28.75 | 15.00 | 78.6 | 68.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.45 | 16.32 | 24.42 | 4.00 | 150.5 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.44 | 10.98 | 18.51 | 2.00 | 57.7 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.79 | 10.61 | 18.47 | 2.00 | 64.5 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.32
- Actual score: 54.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 8.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.98 | 6.90 | 11.70 | 0.00 | 77.3 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 6.02 | 9.54 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.95 | 13.20 | 21.35 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.45 | 12.42 | 19.49 | 2.00 | 87.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.13 | 11.87 | 18.57 | 2.00 | 77.7 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.65 | 7.88 | 12.62 | 1.00 | 72.3 | 90.0 |
| Bench 2 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.01 | 5.80 | 9.62 | 1.00 | 68.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.72 | 24.59 | 37.48 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.00 | 19.71 | 31.47 | 9.00 | 90.0 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 2.40 | 7.65 | 12.21 | 2.00 | 59.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.47 | 21.16 | 32.68 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.52 | 18.18 | 28.79 | 11.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.32 | 13.77 | 21.41 | 7.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.74 | 17.98 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.55 | 18.45 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 1.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.17
- Actual score: 99.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.74) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Caoimhin Kelleher -> Alphonse Areola (projected gain 6.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.74) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.64 | 9.92 | 16.05 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 1.29 | 3.87 | 7.04 | 7.00 | 39.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.45 | 12.94 | 21.38 | 1.00 | 88.6 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.44 | 12.08 | 18.96 | 6.00 | 80.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.18 | 11.30 | 17.57 | 6.00 | 74.1 | 90.0 |
| Bench 2 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.34 | 7.25 | 11.76 | 1.00 | 70.0 | 90.0 |
| Bench 3 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.11 | 5.80 | 9.44 | 1.00 | 72.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.78 | 22.81 | 35.76 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.39 | 18.80 | 29.26 | 13.00 | 85.9 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 2.79 | 7.76 | 12.26 | 11.00 | 58.2 | 83.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.32 | 20.02 | 32.84 | 7.00 | 83.4 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.63 | 16.93 | 27.22 | 15.00 | 87.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.07 | 10.99 | 17.78 | 1.00 | 65.5 | 31.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 2.95 | 8.49 | 14.81 | 5.00 | 44.0 | 90.0 |
| Bench 4 | Bench Boost | Diogo Teixeira da Silva | MID | 11 | 8.1 | 0.00 | 0.46 | 4.34 | 0.00 | 0.0 | 0.0 |
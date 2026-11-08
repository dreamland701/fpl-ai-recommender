# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 292.84
- Total actual points: 326.00
- Average predicted points: 73.21
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
- Predicted score: 60.09
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.92 | 15.17 | 1.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.32 | 0.55 | 0.88 | 3.00 | 2.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.62 | 13.23 | 21.29 | 4.00 | 87.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.84 | 11.04 | 18.40 | 2.00 | 75.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.55 | 10.51 | 16.92 | 12.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.02 | 7.14 | 11.83 | 1.00 | 77.7 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.27 | 7.07 | 11.46 | 1.00 | 74.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.82 | 18.79 | 29.18 | 13.00 | 73.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.97 | 16.56 | 27.46 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 2.17 | 5.69 | 9.10 | 13.00 | 46.9 | 74.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.29 | 16.49 | 27.00 | 15.00 | 76.5 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.76 | 16.03 | 25.75 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.94 | 14.41 | 23.57 | 2.00 | 87.9 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.96 | 14.04 | 22.28 | 7.00 | 80.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.76 | 13.70 | 22.14 | 10.00 | 84.4 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 103.10
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.91) beats the best remaining Triple Captain opportunity (9.83).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 4.89, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.91) beats the best remaining Triple Captain opportunity (9.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.80 | 8.41 | 14.16 | 2.00 | 79.3 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 3.05 | 4.96 | 6.93 | 5.00 | 75.4 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.69 | 12.92 | 21.10 | 1.00 | 85.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.43 | 12.05 | 19.18 | 6.00 | 88.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.34 | 12.00 | 18.87 | 6.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.52 | 7.12 | 11.61 | 6.00 | 74.9 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.88 | 6.27 | 10.57 | -1.00 | 76.9 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 16.01 | 23.69 | 35.75 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.46 | 13.89 | 23.65 | 13.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 2.40 | 6.85 | 11.11 | 8.00 | 56.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.19 | 17.58 | 28.93 | 15.00 | 79.2 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.03 | 17.23 | 26.38 | 5.00 | 162.4 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.44 | 16.09 | 24.02 | 4.00 | 152.4 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.61 | 11.26 | 18.91 | 2.00 | 62.4 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.81 | 10.63 | 18.53 | 2.00 | 67.1 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.68
- Actual score: 54.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 8.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.96 | 6.94 | 11.79 | 0.00 | 78.9 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.83 | 9.38 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.90 | 13.21 | 21.41 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.55 | 12.65 | 19.82 | 2.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.23 | 12.06 | 18.81 | 2.00 | 79.5 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.84 | 8.32 | 13.26 | 1.00 | 74.6 | 90.0 |
| Bench 2 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.99 | 5.74 | 9.50 | 1.00 | 68.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.67 | 24.53 | 37.44 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.07 | 19.90 | 31.76 | 9.00 | 90.0 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 2.38 | 7.63 | 12.20 | 2.00 | 60.8 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.44 | 21.12 | 32.60 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.52 | 18.17 | 28.76 | 11.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.44 | 14.03 | 21.79 | 7.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.93 | 18.32 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.58 | 18.58 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 1.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.96
- Actual score: 99.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.10) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Caoimhin Kelleher -> Alphonse Areola (projected gain 5.74, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.10) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.64 | 9.93 | 16.07 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 1.54 | 4.41 | 7.89 | 7.00 | 44.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.51 | 13.09 | 21.65 | 1.00 | 88.6 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.40 | 12.09 | 19.01 | 6.00 | 81.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.18 | 11.40 | 17.74 | 6.00 | 76.1 | 90.0 |
| Bench 2 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.0 | 2.44 | 7.51 | 12.16 | 1.00 | 71.6 | 90.0 |
| Bench 3 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 2.12 | 5.75 | 9.33 | 1.00 | 71.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.76 | 22.77 | 35.75 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.49 | 19.01 | 29.55 | 13.00 | 87.0 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 2.90 | 8.10 | 12.78 | 11.00 | 60.3 | 83.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.24 | 19.92 | 32.70 | 7.00 | 83.0 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.59 | 16.72 | 26.91 | 15.00 | 88.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.24 | 11.40 | 18.39 | 1.00 | 69.5 | 31.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.15 | 8.88 | 15.37 | 5.00 | 46.9 | 90.0 |
| Bench 4 | Bench Boost | Diogo Teixeira da Silva | MID | 11 | 8.1 | 0.00 | 0.69 | 4.61 | 0.00 | 0.0 | 0.0 |
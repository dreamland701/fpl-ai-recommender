# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 255.66
- Total actual points: 276.00
- Average predicted points: 63.92
- Average actual points: 69.00
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
- Bank: 100.00 -> 1.20
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 58.33
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Martin Dubravka replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.52 | 9.56 | 15.52 | 0.00 | 83.3 | 0.0 |
| Bench 1 | Autosub In | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.80 | 14.97 | 1.00 | 85.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.71 | 13.15 | 21.15 | 4.00 | 90.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.86 | 11.27 | 18.78 | 2.00 | 78.8 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 5.6 | 3.44 | 10.33 | 16.61 | 12.00 | 81.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 3.66 | 10.09 | 16.41 | 2.00 | 83.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.77 | 9.87 | 15.67 | 1.00 | 72.4 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.87 | 16.44 | 27.25 | 2.00 | 94.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.86 | 12.40 | 20.24 | 1.00 | 85.0 | 19.0 |
| Bench 2 | Bench | Julián Álvarez | FWD | 13 | 6.8 | 3.77 | 11.19 | 19.09 | 2.00 | 51.1 | 76.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.15 | 16.36 | 26.75 | 15.00 | 75.6 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.84 | 15.79 | 25.39 | 3.00 | 93.1 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.99 | 14.23 | 23.33 | 2.00 | 87.4 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.18 | 13.90 | 22.09 | 7.00 | 83.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.71 | 13.64 | 22.05 | 10.00 | 81.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 1.20 -> 1.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Diogo Teixeira da Silva
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 69.74
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.26) beats the best remaining Bench Boost opportunity (9.21).
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 3.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.26) beats the best remaining Bench Boost opportunity (9.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.24 | 9.69 | 14.77 | 11.00 | 98.6 | 180.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.23 | 13.89 | 2.00 | 79.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.65 | 12.74 | 20.81 | 1.00 | 85.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 5.60 | 12.71 | 19.58 | 10.00 | 118.8 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.42 | 11.97 | 19.07 | 6.00 | 88.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.11 | 10.24 | 15.57 | 1.00 | 93.4 | 154.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.8 | 1.92 | 6.90 | 12.61 | 0.00 | 49.2 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.10 | 13.56 | 23.15 | 13.00 | 70.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.18 | 10.88 | 18.22 | 7.00 | 68.8 | 151.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.42 | 6.77 | 12.48 | 0.00 | 32.3 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.21 | 17.51 | 28.80 | 15.00 | 78.1 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.81 | 17.16 | 26.31 | 5.00 | 109.1 | 180.0 |
| Vice Captain | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 6.78 | 16.04 | 23.99 | 4.00 | 106.0 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.27 | 10.81 | 18.27 | 2.00 | 53.5 | 70.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.8 | 2.45 | 10.39 | 18.19 | 2.00 | 59.7 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 1.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 63.54
- Actual score: 54.00
- Transfer: Richarlison de Andrade -> Martin Ødegaard (projected gain 5.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.17 | 11.38 | 18.00 | 9.00 | 106.5 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.90 | 6.75 | 11.49 | 0.00 | 78.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.96 | 13.17 | 21.30 | 0.00 | 94.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.60 | 12.56 | 19.69 | 2.00 | 89.4 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 3.93 | 12.55 | 20.51 | 0.00 | 99.8 | 0.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 3.35 | 10.48 | 17.48 | 0.00 | 78.6 | 0.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 1.17 | 5.30 | 10.56 | 0.00 | 22.2 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.53 | 19.82 | 31.61 | 9.00 | 118.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.77 | 13.36 | 21.86 | 1.00 | 78.3 | 15.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.12 | 6.27 | 11.72 | 0.00 | 25.1 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.98 | 21.36 | 32.94 | 10.00 | 104.8 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.67 | 18.25 | 28.89 | 11.00 | 110.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 5.54 | 15.57 | 25.11 | 2.00 | 91.4 | 75.0 |
| Bench 2 | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 3.03 | 10.78 | 18.03 | 0.00 | 36.7 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 3.06 | 10.56 | 18.46 | 0.00 | 52.8 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 64.06
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.45) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 7.01, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (7.45) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.17 | 9.35 | 15.57 | 2.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.33 | 3.84 | 7.00 | 7.00 | 40.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.46 | 13.01 | 21.49 | 1.00 | 88.5 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.43 | 12.04 | 18.91 | 6.00 | 82.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 2.74 | 8.23 | 14.00 | 6.00 | 55.2 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.05 | 6.05 | 10.41 | 5.00 | 41.1 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.7 | 0.24 | 2.13 | 5.22 | 0.00 | 7.2 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.47 | 18.90 | 29.37 | 13.00 | 83.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 2.93 | 9.62 | 16.35 | 4.00 | 42.5 | 31.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.81 | 3.89 | 8.18 | 0.00 | 13.6 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.45 | 20.00 | 32.83 | 7.00 | 85.1 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.62 | 16.63 | 26.78 | 15.00 | 88.6 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 4.55 | 12.79 | 21.90 | 10.00 | 68.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.43 | 12.59 | 20.28 | 5.00 | 90.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 2.92 | 8.60 | 14.95 | 5.00 | 42.9 | 90.0 |
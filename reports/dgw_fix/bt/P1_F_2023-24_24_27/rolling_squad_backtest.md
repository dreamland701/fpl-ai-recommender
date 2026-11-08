# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 261.95
- Total actual points: 274.00
- Average predicted points: 65.49
- Average actual points: 68.50
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
- Predicted score: 57.54
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Martin Dubravka replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.51 | 9.56 | 15.52 | 0.00 | 82.7 | 0.0 |
| Bench 1 | Autosub In | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.80 | 14.97 | 1.00 | 83.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.62 | 13.15 | 21.15 | 4.00 | 87.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.91 | 11.27 | 18.78 | 2.00 | 78.1 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 5.6 | 3.49 | 10.33 | 16.61 | 12.00 | 79.2 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 3.63 | 10.09 | 16.41 | 2.00 | 82.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.65 | 9.87 | 15.67 | 1.00 | 71.0 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.92 | 16.44 | 27.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.65 | 12.40 | 20.24 | 1.00 | 85.0 | 19.0 |
| Bench 2 | Bench | Julián Álvarez | FWD | 13 | 6.8 | 3.80 | 11.19 | 19.09 | 2.00 | 52.4 | 76.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.25 | 16.36 | 26.75 | 15.00 | 75.5 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.66 | 15.79 | 25.39 | 3.00 | 89.9 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.85 | 14.23 | 23.33 | 2.00 | 85.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.90 | 13.90 | 22.09 | 7.00 | 79.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.71 | 13.64 | 22.05 | 10.00 | 83.4 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 1.20 -> 1.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Diogo Teixeira da Silva
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 92.44
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.55) beats the best remaining Triple Captain opportunity (7.83).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Alisson Ramses Becker -> Ederson Santana de Moraes (projected gain 3.46, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (15.55) beats the best remaining Triple Captain opportunity (7.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 6.09 | 9.69 | 14.77 | 11.00 | 141.8 | 180.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.23 | 13.89 | 2.00 | 78.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.64 | 12.74 | 20.81 | 1.00 | 83.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 8.28 | 12.71 | 19.58 | 10.00 | 175.6 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 11.97 | 19.07 | 6.00 | 87.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.73 | 10.24 | 15.57 | 1.00 | 127.2 | 154.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.35 | 6.90 | 12.61 | 0.00 | 55.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.34 | 13.56 | 23.15 | 13.00 | 74.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 6.15 | 10.88 | 18.22 | 7.00 | 88.6 | 151.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.50 | 6.77 | 12.48 | 0.00 | 35.1 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.51 | 28.80 | 15.00 | 78.6 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 10.95 | 17.16 | 26.31 | 5.00 | 160.3 | 180.0 |
| Vice Captain | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.38 | 16.04 | 23.99 | 4.00 | 150.7 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.41 | 10.81 | 18.27 | 2.00 | 57.8 | 70.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 2.70 | 10.39 | 18.19 | 2.00 | 64.7 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 1.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 50.29
- Actual score: 54.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Dominic Solanke (projected gain 7.44, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 4.21 | 11.38 | 18.00 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.90 | 6.75 | 11.49 | 0.00 | 77.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.92 | 13.17 | 21.30 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.51 | 12.56 | 19.69 | 2.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 0.00 | 12.55 | 20.51 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.48 | 17.48 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.00 | 5.30 | 10.56 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.07 | 19.82 | 31.61 | 9.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.71 | 13.36 | 21.86 | 1.00 | 77.5 | 15.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.19 | 13.09 | 20.72 | 2.00 | 87.0 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.55 | 21.36 | 32.94 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.57 | 18.25 | 28.89 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.78 | 18.03 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.56 | 18.46 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.09 | 17.67 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 61.68
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.47) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 6.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.47) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Ederson Santana de Moraes | GK | 13 | 5.5 | 3.15 | 9.35 | 15.57 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 1.30 | 3.84 | 7.00 | 7.00 | 39.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.51 | 13.01 | 21.49 | 1.00 | 88.4 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.38 | 12.04 | 18.91 | 6.00 | 80.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 2.70 | 8.23 | 14.00 | 6.00 | 53.6 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.02 | 6.05 | 10.41 | 5.00 | 41.1 | 90.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.7 | 0.62 | 2.13 | 5.22 | 0.00 | 12.9 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.44 | 18.90 | 29.37 | 13.00 | 85.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.51 | 12.83 | 19.68 | 2.00 | 72.2 | 88.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 2.98 | 9.62 | 16.35 | 4.00 | 42.6 | 31.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.27 | 20.00 | 32.83 | 7.00 | 83.5 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.55 | 16.63 | 26.78 | 15.00 | 87.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.43 | 12.59 | 20.28 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.01 | 8.60 | 14.95 | 5.00 | 43.8 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.53 | 5.08 | 10.33 | 0.00 | 16.2 | 0.0 |
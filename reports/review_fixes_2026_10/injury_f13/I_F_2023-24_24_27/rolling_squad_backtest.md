# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 254.07
- Total actual points: 271.00
- Average predicted points: 63.52
- Average actual points: 67.75
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 57.64
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.57 | 8.87 | 14.47 | 0.00 | 70.2 | 90.0 |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.79 | 14.94 | 1.00 | 85.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.72 | 13.14 | 21.11 | 4.00 | 90.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.86 | 11.33 | 18.90 | 2.00 | 78.4 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.6 | 3.75 | 10.61 | 17.92 | 4.00 | 57.9 | 45.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 5.6 | 3.43 | 10.31 | 16.58 | 12.00 | 81.2 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.77 | 9.88 | 15.70 | 1.00 | 71.8 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.87 | 16.42 | 27.21 | 2.00 | 94.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.86 | 12.40 | 20.24 | 1.00 | 85.1 | 19.0 |
| Bench 2 | Bench | Julián Álvarez | FWD | 13 | 6.8 | 3.77 | 11.19 | 19.11 | 2.00 | 51.2 | 76.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.17 | 16.40 | 26.81 | 15.00 | 75.4 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.84 | 15.75 | 25.32 | 3.00 | 93.4 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 5.00 | 14.31 | 23.46 | 2.00 | 86.6 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.19 | 13.91 | 22.07 | 7.00 | 83.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.71 | 13.64 | 22.05 | 10.00 | 82.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.40 -> 2.60
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Diogo Teixeira da Silva
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 68.72
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.81) beats the best remaining Bench Boost opportunity (10.28).
- Transfer: Trent Alexander-Arnold -> Virgil van Dijk (projected gain 5.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.81) beats the best remaining Bench Boost opportunity (10.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.15 | 9.26 | 15.18 | 3.00 | 80.3 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.21 | 13.85 | 2.00 | 79.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.72 | 20.76 | 1.00 | 85.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 5.61 | 12.67 | 19.50 | 10.00 | 118.9 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.42 | 11.95 | 19.02 | 6.00 | 89.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.12 | 10.25 | 15.59 | 1.00 | 92.8 | 154.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.8 | 1.92 | 6.95 | 12.72 | 0.00 | 48.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.11 | 13.56 | 23.13 | 13.00 | 70.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.18 | 10.88 | 18.20 | 7.00 | 68.9 | 151.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.42 | 6.77 | 12.47 | 0.00 | 32.3 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.23 | 17.55 | 28.86 | 15.00 | 77.9 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.80 | 17.12 | 26.23 | 5.00 | 109.4 | 180.0 |
| Vice Captain | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 6.80 | 16.04 | 23.96 | 4.00 | 105.8 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.28 | 10.89 | 18.40 | 2.00 | 52.6 | 70.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.8 | 2.44 | 10.38 | 18.18 | 2.00 | 59.9 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 2.60 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 63.09
- Actual score: 47.00
- Transfer: Richarlison de Andrade -> Martin Ødegaard (projected gain 5.22, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.67 | 10.10 | 16.55 | 2.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.90 | 6.73 | 11.46 | 0.00 | 78.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.97 | 13.15 | 21.26 | 0.00 | 94.2 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 3.94 | 12.53 | 20.46 | 0.00 | 99.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.60 | 12.53 | 19.63 | 2.00 | 89.6 | 90.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 3.36 | 10.52 | 17.54 | 0.00 | 78.0 | 0.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 1.17 | 5.37 | 10.70 | 0.00 | 21.8 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.54 | 19.81 | 31.60 | 9.00 | 118.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.77 | 13.34 | 21.83 | 1.00 | 78.5 | 15.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.13 | 6.26 | 11.70 | 0.00 | 25.2 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 8.00 | 21.40 | 33.00 | 10.00 | 104.6 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.66 | 18.22 | 28.83 | 11.00 | 110.9 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 5.53 | 15.61 | 25.19 | 2.00 | 91.1 | 75.0 |
| Bench 2 | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 3.04 | 10.79 | 18.03 | 0.00 | 36.6 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 3.05 | 10.56 | 18.47 | 0.00 | 53.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 1.40 -> 3.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 64.62
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.47) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Douglas Luiz Soares de Paulo (projected gain 7.03, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (7.47) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.54 | 10.04 | 16.23 | 13.00 | 92.5 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.33 | 3.82 | 6.97 | 7.00 | 40.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.46 | 13.00 | 21.44 | 1.00 | 88.4 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.43 | 12.01 | 18.86 | 6.00 | 82.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 2.74 | 8.20 | 13.94 | 6.00 | 55.2 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.05 | 6.08 | 10.46 | 5.00 | 40.6 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.7 | 0.23 | 2.18 | 5.34 | 0.00 | 6.8 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.48 | 18.91 | 29.39 | 13.00 | 82.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 2.93 | 9.61 | 16.33 | 4.00 | 42.7 | 31.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.81 | 3.87 | 8.15 | 0.00 | 13.8 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.47 | 20.03 | 32.87 | 7.00 | 84.9 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.61 | 16.61 | 26.74 | 15.00 | 88.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 4.54 | 12.83 | 21.98 | 10.00 | 68.3 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 4.55 | 12.63 | 19.78 | 4.00 | 80.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 2.92 | 8.58 | 14.93 | 5.00 | 43.2 | 90.0 |
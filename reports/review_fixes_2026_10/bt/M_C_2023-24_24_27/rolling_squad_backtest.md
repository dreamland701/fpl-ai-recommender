# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 269.11
- Total actual points: 270.00
- Average predicted points: 67.28
- Average actual points: 67.50
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
- Bank: 100.00 -> 1.90
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 59.76
- Actual score: 56.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 3.06 | 10.24 | 17.01 | 0.00 | 75.2 | 90.0 |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 3.10 | 9.73 | 16.58 | 1.00 | 90.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.56 | 13.07 | 21.43 | 4.00 | 87.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.51 | 12.90 | 21.38 | 2.00 | 89.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.52 | 10.66 | 17.49 | 12.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.30 | 10.12 | 16.50 | 12.00 | 81.0 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.5 | 3.50 | 10.08 | 16.45 | 1.00 | 74.1 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 6.30 | 17.92 | 29.61 | 2.00 | 101.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.98 | 14.42 | 24.04 | 2.00 | 71.3 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.67 | 12.96 | 20.98 | 1.00 | 90.7 | 19.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 5.88 | 16.68 | 27.15 | 3.00 | 92.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.62 | 16.64 | 27.42 | 15.00 | 79.6 | 66.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 5.21 | 15.57 | 25.36 | 10.00 | 94.3 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.1 | 5.09 | 14.08 | 23.27 | 2.00 | 86.0 | 90.0 |
| Bench 2 | Bench | Kevin De Bruyne | MID | 13 | 10.7 | 4.62 | 13.23 | 21.45 | 4.00 | 61.5 | 33.0 |

## GW25

- Train rows: 121836
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 80.20
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (22.38) beats the best remaining Bench Boost opportunity (13.34).
- Transfer: Matheus Santos Carneiro Da Cunha -> Darwin Núñez Ribeiro (projected gain 1.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (22.38) beats the best remaining Bench Boost opportunity (13.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.80 | 11.24 | 18.41 | 3.00 | 90.5 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 3.10 | 9.38 | 15.63 | 2.00 | 86.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.76 | 13.41 | 21.83 | 1.00 | 88.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 12.44 | 20.06 | 6.00 | 91.6 | 90.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.27 | 12.31 | 19.81 | 6.00 | 87.5 | 90.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 4.16 | 11.81 | 19.27 | 0.00 | 86.4 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.5 | 4.46 | 11.25 | 17.45 | 1.00 | 99.6 | 154.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.89 | 17.46 | 29.01 | 13.00 | 94.7 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 6.07 | 14.99 | 23.31 | 5.00 | 91.0 | 45.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 5.27 | 13.74 | 22.37 | 7.00 | 89.7 | 151.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.22 | 17.79 | 28.71 | 15.00 | 82.3 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 7.9 | 6.56 | 16.99 | 26.37 | 5.00 | 109.9 | 180.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.73 | 15.18 | 25.47 | 2.00 | 89.9 | 70.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 5.34 | 13.77 | 21.52 | 2.00 | 77.0 | 90.0 |
| Bench 2 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 4.60 | 13.27 | 21.31 | 2.00 | 75.1 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.90
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 62.36
- Actual score: 55.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 2.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.14 | 11.58 | 19.19 | 2.00 | 97.1 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.17 | 7.47 | 12.76 | 0.00 | 83.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.04 | 13.16 | 21.76 | 0.00 | 92.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.32 | 12.62 | 20.11 | 2.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.23 | 12.28 | 19.76 | 2.00 | 87.1 | 90.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.5 | 3.77 | 11.75 | 19.51 | 0.00 | 83.9 | 0.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.86 | 4.92 | 10.55 | 0.00 | 16.1 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.10 | 17.54 | 29.41 | 9.00 | 92.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 5.33 | 15.32 | 25.05 | 1.00 | 89.1 | 15.0 |
| Bench 2 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 3.34 | 11.56 | 19.04 | 0.00 | 35.6 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 7.9 | 7.17 | 20.22 | 31.93 | 11.00 | 120.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.45 | 18.38 | 28.87 | 10.00 | 85.7 | 75.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 4.97 | 14.79 | 24.05 | 0.00 | 68.0 | 6.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.67 | 13.31 | 21.59 | 7.00 | 88.6 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.8 | 3.32 | 11.78 | 20.98 | 0.00 | 55.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.90 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 66.79
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Darwin Núñez Ribeiro -> Dominic Solanke (projected gain 2.59, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.93 | 11.35 | 18.57 | 13.00 | 97.9 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.64 | 4.91 | 8.76 | 7.00 | 47.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.37 | 13.26 | 21.87 | 1.00 | 87.2 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.45 | 12.67 | 20.05 | 6.00 | 87.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.47 | 12.50 | 19.56 | 6.00 | 85.1 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.5 | 2.68 | 7.86 | 13.54 | 5.00 | 52.8 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.14 | 6.35 | 11.06 | 0.00 | 39.5 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.67 | 19.91 | 31.30 | 13.00 | 97.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.57 | 13.16 | 20.23 | 2.00 | 78.5 | 88.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 3.85 | 11.74 | 19.75 | 4.00 | 56.5 | 31.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.73 | 20.22 | 31.75 | 7.00 | 83.3 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.56 | 18.67 | 30.13 | 15.00 | 99.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.17 | 12.67 | 20.27 | 1.00 | 81.4 | 31.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 3.55 | 11.38 | 19.51 | 2.00 | 38.2 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 3.47 | 10.74 | 18.53 | 5.00 | 54.5 | 90.0 |
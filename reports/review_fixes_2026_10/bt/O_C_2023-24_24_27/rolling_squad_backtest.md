# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 269.17
- Total actual points: 270.00
- Average predicted points: 67.29
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
- Predicted score: 59.81
- Actual score: 56.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 3.01 | 10.13 | 16.73 | 0.00 | 75.3 | 90.0 |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 3.13 | 9.67 | 16.06 | 1.00 | 90.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.58 | 13.31 | 21.71 | 4.00 | 87.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.49 | 13.01 | 21.51 | 2.00 | 89.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.56 | 10.77 | 17.72 | 12.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.34 | 10.24 | 16.62 | 12.00 | 80.9 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.5 | 3.52 | 10.15 | 16.48 | 1.00 | 74.1 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 6.32 | 18.19 | 30.03 | 2.00 | 101.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.98 | 14.48 | 23.94 | 2.00 | 71.3 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.64 | 12.91 | 20.81 | 1.00 | 90.7 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.66 | 16.96 | 27.85 | 15.00 | 79.6 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 5.88 | 16.87 | 27.47 | 3.00 | 92.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 5.20 | 15.60 | 25.37 | 10.00 | 94.3 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.1 | 5.07 | 14.02 | 22.86 | 2.00 | 86.0 | 90.0 |
| Bench 2 | Bench | Kevin De Bruyne | MID | 13 | 10.7 | 4.62 | 13.42 | 21.84 | 4.00 | 61.5 | 33.0 |

## GW25

- Train rows: 121836
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 80.13
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (22.41) beats the best remaining Bench Boost opportunity (13.28).
- Transfer: Matheus Santos Carneiro Da Cunha -> Darwin Núñez Ribeiro (projected gain 1.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (22.41) beats the best remaining Bench Boost opportunity (13.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.83 | 11.21 | 18.35 | 3.00 | 90.4 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 3.06 | 9.02 | 15.13 | 2.00 | 86.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.72 | 13.42 | 21.98 | 1.00 | 88.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.39 | 12.54 | 20.39 | 6.00 | 91.6 | 90.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.25 | 12.26 | 19.80 | 6.00 | 87.5 | 90.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 4.21 | 12.01 | 19.64 | 0.00 | 86.4 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.47 | 11.30 | 17.69 | 1.00 | 99.6 | 154.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.89 | 17.75 | 29.44 | 13.00 | 94.7 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 6.05 | 15.08 | 23.43 | 5.00 | 91.0 | 45.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 5.26 | 13.78 | 22.20 | 7.00 | 89.7 | 151.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.20 | 18.12 | 29.29 | 15.00 | 82.3 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.55 | 17.22 | 27.01 | 5.00 | 109.9 | 180.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.74 | 15.16 | 25.36 | 2.00 | 89.9 | 70.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 5.33 | 13.81 | 21.80 | 2.00 | 77.0 | 90.0 |
| Bench 2 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.2 | 4.64 | 13.29 | 21.07 | 2.00 | 75.0 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 62.23
- Actual score: 55.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 2.51, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.11 | 11.47 | 18.97 | 2.00 | 97.1 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.13 | 7.29 | 12.43 | 0.00 | 84.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.00 | 13.05 | 21.80 | 0.00 | 92.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.34 | 12.69 | 20.17 | 2.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.25 | 12.49 | 20.21 | 2.00 | 87.1 | 90.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 3.77 | 11.71 | 19.51 | 0.00 | 83.9 | 0.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.86 | 4.99 | 10.52 | 0.00 | 16.1 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.13 | 17.75 | 29.50 | 9.00 | 92.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 5.30 | 15.26 | 24.79 | 1.00 | 89.1 | 15.0 |
| Bench 2 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.6 | 3.34 | 11.44 | 18.85 | 0.00 | 35.6 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 7.13 | 20.29 | 32.17 | 11.00 | 120.9 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.48 | 18.85 | 29.73 | 10.00 | 85.7 | 75.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 4.93 | 14.78 | 24.20 | 0.00 | 68.0 | 6.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.66 | 13.51 | 22.02 | 7.00 | 88.6 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 5.8 | 3.32 | 11.78 | 20.97 | 0.00 | 55.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 1.00 -> 1.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 67.00
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Darwin Núñez Ribeiro -> Dominic Solanke (projected gain 2.44, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.76) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.92 | 11.20 | 18.38 | 13.00 | 97.9 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.69 | 4.96 | 8.72 | 7.00 | 47.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.41 | 13.28 | 21.80 | 1.00 | 87.2 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.48 | 12.79 | 20.37 | 6.00 | 87.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.50 | 12.57 | 19.70 | 6.00 | 85.1 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.65 | 7.73 | 13.30 | 5.00 | 52.9 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.13 | 6.36 | 11.09 | 0.00 | 39.5 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.68 | 19.79 | 30.85 | 13.00 | 97.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.55 | 13.05 | 20.01 | 2.00 | 78.5 | 88.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 3.87 | 11.79 | 19.64 | 4.00 | 56.5 | 31.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 6.76 | 20.35 | 31.86 | 7.00 | 83.3 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 6.57 | 18.78 | 30.06 | 15.00 | 99.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.17 | 12.73 | 20.25 | 1.00 | 81.4 | 31.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 3.57 | 11.43 | 19.67 | 2.00 | 38.2 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.8 | 3.43 | 10.70 | 18.36 | 5.00 | 54.5 | 90.0 |
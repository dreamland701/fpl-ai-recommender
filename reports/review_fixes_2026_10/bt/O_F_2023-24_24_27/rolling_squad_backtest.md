# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 262.62
- Total actual points: 276.00
- Average predicted points: 65.66
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 58.66
- Actual score: 45.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 3.06 | 9.54 | 15.85 | 1.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.73 | 9.51 | 15.75 | 0.00 | 71.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.58 | 13.38 | 21.82 | 4.00 | 88.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.37 | 12.76 | 21.09 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.6 | 3.53 | 10.71 | 17.60 | 12.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.5 | 3.48 | 10.08 | 17.19 | 4.00 | 57.6 | 45.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.5 | 3.61 | 9.83 | 15.91 | 1.00 | 71.9 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 6.18 | 17.79 | 29.40 | 2.00 | 99.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.66 | 13.32 | 22.20 | 2.00 | 68.8 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 5.09 | 13.20 | 21.30 | 1.00 | 92.6 | 19.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.53 | 17.04 | 27.84 | 15.00 | 75.7 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 5.54 | 15.75 | 25.81 | 3.00 | 90.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 5.13 | 15.67 | 25.30 | 10.00 | 87.7 | 90.0 |
| Bench 2 | Bench | Martin Ødegaard | MID | 1 | 8.5 | 4.39 | 13.56 | 22.09 | 10.00 | 76.2 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.1 | 4.71 | 13.37 | 21.81 | 2.00 | 82.2 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.60 -> 1.20
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 76.87
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.88) beats the best remaining Bench Boost opportunity (12.94).
- Transfer: William Saliba -> Gabriel dos Santos Magalhães (projected gain 1.70, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.88) beats the best remaining Bench Boost opportunity (12.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.58 | 10.54 | 17.27 | 3.00 | 86.2 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 3.00 | 8.86 | 14.86 | 2.00 | 85.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.72 | 13.32 | 21.83 | 1.00 | 89.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.6 | 5.19 | 12.63 | 20.30 | 0.00 | 90.4 | 0.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 4.15 | 11.90 | 19.45 | 0.00 | 85.1 | 0.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.15 | 11.81 | 19.04 | 6.00 | 84.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.37 | 11.10 | 17.38 | 1.00 | 99.1 | 154.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.84 | 17.59 | 29.13 | 13.00 | 91.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 5.32 | 13.98 | 22.47 | 7.00 | 88.1 | 151.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 2.78 | 9.66 | 16.43 | 0.00 | 55.3 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.44 | 18.54 | 29.89 | 15.00 | 80.9 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.79 | 17.82 | 27.90 | 5.00 | 110.0 | 180.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 5.04 | 14.81 | 24.16 | 14.00 | 86.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.15 | 14.07 | 23.65 | 2.00 | 84.1 | 70.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.56 | 13.44 | 21.24 | 2.00 | 71.5 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 1.20 -> 0.90
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 60.78
- Actual score: 48.00
- Transfer: Richarlison de Andrade -> Luis Díaz (projected gain 7.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.88 | 10.83 | 17.92 | 2.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.15 | 7.39 | 12.59 | 0.00 | 84.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.88 | 12.86 | 21.60 | 0.00 | 93.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.25 | 12.39 | 19.64 | 2.00 | 80.6 | 90.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 3.55 | 11.13 | 18.58 | 0.00 | 80.2 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.6 | 0.87 | 5.04 | 10.60 | 0.00 | 6.6 | 0.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.82 | 4.85 | 10.30 | 0.00 | 15.1 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 5.84 | 16.77 | 28.00 | 9.00 | 90.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 5.12 | 14.67 | 23.84 | 1.00 | 85.8 | 15.0 |
| Bench 2 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 2.79 | 8.44 | 14.52 | 0.00 | 36.7 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.95 | 19.72 | 31.24 | 11.00 | 117.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.68 | 19.52 | 30.60 | 10.00 | 83.1 | 75.0 |
| XI | Bench | Luis Díaz | MID | 11 | 7.5 | 5.32 | 15.61 | 24.30 | 0.00 | 92.7 | 0.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 5.27 | 15.52 | 25.41 | 2.00 | 90.3 | 75.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 3.07 | 11.05 | 19.77 | 0.00 | 50.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.90 -> 1.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 66.31
- Actual score: 107.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.03) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Leon Bailey (projected gain 3.82, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (7.03) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.67 | 10.51 | 17.25 | 13.00 | 93.4 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.65 | 4.86 | 8.55 | 7.00 | 46.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.43 | 13.26 | 21.79 | 1.00 | 87.8 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.43 | 12.21 | 19.06 | 6.00 | 82.5 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.48 | 7.30 | 12.60 | 5.00 | 50.2 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.6 | 2.27 | 7.20 | 12.25 | 0.00 | 30.7 | 0.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.13 | 6.36 | 11.08 | 0.00 | 39.3 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 7.03 | 21.37 | 32.90 | 13.00 | 91.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 3.60 | 11.20 | 18.73 | 4.00 | 53.6 | 31.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.17 | 5.31 | 9.78 | 0.00 | 22.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.02 | 20.30 | 31.64 | 7.00 | 82.8 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 6.20 | 17.93 | 28.79 | 15.00 | 96.8 | 90.0 |
| XI | XI | Leon Bailey | MID | 2 | 5.6 | 4.65 | 13.87 | 21.37 | 4.00 | 75.9 | 78.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 4.65 | 13.74 | 22.61 | 10.00 | 75.3 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.5 | 4.08 | 12.10 | 19.16 | 3.00 | 51.9 | 90.0 |
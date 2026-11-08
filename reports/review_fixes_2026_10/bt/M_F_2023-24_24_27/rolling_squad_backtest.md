# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 263.42
- Total actual points: 278.00
- Average predicted points: 65.86
- Average actual points: 69.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 58.64
- Actual score: 58.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.77 | 9.61 | 16.01 | 0.00 | 71.3 | 90.0 |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 3.04 | 9.59 | 16.34 | 1.00 | 89.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.56 | 13.13 | 21.53 | 4.00 | 88.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.39 | 12.62 | 20.94 | 2.00 | 87.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.50 | 10.60 | 17.39 | 12.00 | 82.4 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.18 | 9.96 | 16.20 | 12.00 | 77.9 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 3.50 | 9.78 | 16.08 | 2.00 | 84.1 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 6.17 | 17.52 | 28.98 | 2.00 | 99.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 5.13 | 13.41 | 21.41 | 1.00 | 92.6 | 19.0 |
| Bench 2 | Bench | Julián Álvarez | FWD | 13 | 6.9 | 4.66 | 13.32 | 22.36 | 2.00 | 68.8 | 76.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.50 | 16.60 | 27.28 | 15.00 | 75.7 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 5.54 | 15.61 | 25.54 | 3.00 | 90.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 5.15 | 15.55 | 25.07 | 10.00 | 87.7 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 4.78 | 13.53 | 22.03 | 4.00 | 67.6 | 33.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.1 | 4.74 | 13.36 | 22.16 | 2.00 | 82.1 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 76.05
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.80) beats the best remaining Bench Boost opportunity (13.86).
- Transfer: Virgil van Dijk -> Fabian Schär (projected gain 2.27, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.80) beats the best remaining Bench Boost opportunity (13.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.56 | 10.58 | 17.33 | 3.00 | 86.2 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 3.03 | 9.19 | 15.32 | 2.00 | 85.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.75 | 13.35 | 21.72 | 1.00 | 88.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.38 | 12.28 | 19.76 | 6.00 | 89.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.17 | 11.89 | 19.08 | 6.00 | 84.3 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.9 | 4.11 | 11.68 | 19.07 | 0.00 | 85.2 | 0.0 |
| Bench 3 | Bench Boost | Fabian Schär | DEF | 15 | 5.3 | 3.56 | 10.45 | 17.24 | 3.00 | 85.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.84 | 17.28 | 28.66 | 13.00 | 91.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 5.33 | 13.90 | 22.57 | 7.00 | 88.1 | 151.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 2.75 | 9.62 | 16.57 | 0.00 | 55.3 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.46 | 18.23 | 29.30 | 15.00 | 80.9 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 7.9 | 6.80 | 17.57 | 27.26 | 5.00 | 110.0 | 180.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 5.84 | 15.12 | 23.68 | 2.00 | 83.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.14 | 13.97 | 23.57 | 2.00 | 84.1 | 70.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.1 | 4.52 | 13.25 | 21.23 | 2.00 | 71.5 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 61.53
- Actual score: 48.00
- Transfer: Richarlison de Andrade -> Luis Díaz (projected gain 7.49, hit 0)
- Autosub: Fabian Schär replaced Luis Díaz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.91 | 10.94 | 18.14 | 2.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.19 | 7.56 | 12.92 | 0.00 | 84.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.92 | 13.01 | 21.58 | 0.00 | 93.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.24 | 12.32 | 19.58 | 2.00 | 80.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.25 | 12.28 | 19.72 | 2.00 | 86.0 | 90.0 |
| Bench 3 | Autosub In | Fabian Schär | DEF | 15 | 5.3 | 2.62 | 9.56 | 16.14 | 0.00 | 82.1 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.82 | 4.79 | 10.36 | 0.00 | 15.1 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 5.82 | 16.61 | 28.03 | 9.00 | 90.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 5.15 | 14.74 | 24.13 | 1.00 | 85.8 | 15.0 |
| Bench 2 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 2.77 | 8.37 | 14.79 | 0.00 | 36.8 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 7.9 | 6.99 | 19.65 | 31.03 | 11.00 | 117.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.66 | 18.95 | 29.50 | 10.00 | 83.1 | 75.0 |
| XI | Bench | Luis Díaz | MID | 11 | 7.5 | 5.32 | 15.48 | 24.16 | 0.00 | 92.7 | 0.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 5.22 | 15.42 | 25.09 | 0.00 | 72.1 | 6.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 3.07 | 11.05 | 19.79 | 0.00 | 50.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.70 -> 0.90
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 67.20
- Actual score: 100.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.03) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Leon Bailey (projected gain 3.78, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (7.03) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.67 | 10.66 | 17.47 | 13.00 | 93.4 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.61 | 4.81 | 8.59 | 7.00 | 46.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.39 | 13.25 | 21.92 | 1.00 | 87.8 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.43 | 12.48 | 19.73 | 6.00 | 85.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.40 | 12.13 | 18.98 | 6.00 | 82.6 | 90.0 |
| Bench 2 | Bench | Fabian Schär | DEF | 15 | 5.3 | 3.15 | 9.36 | 15.94 | 12.00 | 80.8 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.14 | 6.34 | 11.03 | 0.00 | 39.3 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 7.03 | 21.47 | 32.77 | 13.00 | 91.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 3.59 | 11.16 | 18.80 | 4.00 | 53.6 | 31.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.15 | 5.30 | 10.22 | 0.00 | 22.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.99 | 20.12 | 31.79 | 7.00 | 82.8 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.19 | 17.83 | 28.86 | 15.00 | 96.8 | 90.0 |
| XI | XI | Leon Bailey | MID | 2 | 5.6 | 4.65 | 13.85 | 21.02 | 4.00 | 75.9 | 78.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.5 | 4.06 | 12.02 | 19.16 | 3.00 | 52.0 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 3.73 | 11.94 | 20.43 | 2.00 | 42.1 | 90.0 |
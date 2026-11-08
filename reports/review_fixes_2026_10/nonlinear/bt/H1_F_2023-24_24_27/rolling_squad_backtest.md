# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 246.75
- Total actual points: 255.00
- Average predicted points: 61.69
- Average actual points: 63.75
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
- Bank: 100.00 -> 0.80
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 58.81
- Actual score: 47.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Martin Dubravka replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.03 | 9.56 | 15.52 | 0.00 | 87.2 | 0.0 |
| Bench 1 | Autosub In | Martin Dubravka | GK | 15 | 4.2 | 3.59 | 8.80 | 14.97 | 1.00 | 83.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.03 | 13.15 | 21.15 | 4.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.9 | 2.96 | 11.27 | 18.78 | 2.00 | 72.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.6 | 5.25 | 10.55 | 17.80 | 4.00 | 61.3 | 45.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.6 | 3.33 | 10.33 | 16.61 | 12.00 | 82.3 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.63 | 9.87 | 15.67 | 1.00 | 77.4 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.67 | 16.44 | 27.25 | 2.00 | 83.8 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 5.42 | 12.40 | 20.24 | 1.00 | 81.7 | 19.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 4.18 | 10.38 | 16.95 | 5.00 | 74.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.40 | 16.36 | 26.75 | 15.00 | 76.2 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 4.98 | 15.79 | 25.39 | 3.00 | 77.2 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.66 | 14.23 | 23.33 | 2.00 | 85.4 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.90 | 13.90 | 22.09 | 7.00 | 67.9 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.9 | 3.71 | 13.64 | 22.05 | 10.00 | 80.5 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.80 -> 3.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Diogo Teixeira da Silva
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 90.21
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.54) beats the best remaining Triple Captain opportunity (6.71).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Trent Alexander-Arnold -> Virgil van Dijk (projected gain 5.07, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (15.54) beats the best remaining Triple Captain opportunity (6.71).
- Autosub: Martin Dubravka replaced Alisson Ramses Becker.
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Autosub In | Martin Dubravka | GK | 15 | 4.2 | 3.72 | 8.23 | 13.89 | 2.00 | 76.0 | 90.0 |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 4.80 | 6.56 | 10.98 | 0.00 | 101.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 5.05 | 12.74 | 20.81 | 1.00 | 79.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 8.52 | 12.71 | 19.58 | 10.00 | 164.1 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.24 | 11.97 | 19.07 | 6.00 | 82.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 6.29 | 10.24 | 15.57 | 1.00 | 158.0 | 154.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.85 | 6.90 | 12.61 | 0.00 | 60.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.61 | 13.56 | 23.15 | 13.00 | 69.2 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.64 | 10.21 | 15.93 | 0.00 | 150.8 | 0.0 |
| Bench 4 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 2.01 | 6.77 | 12.48 | 0.00 | 14.6 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.23 | 17.51 | 28.80 | 15.00 | 58.7 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 10.94 | 17.16 | 26.31 | 5.00 | 158.4 | 180.0 |
| Vice Captain | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 9.91 | 16.04 | 23.99 | 4.00 | 139.7 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.10 | 10.81 | 18.27 | 2.00 | 69.7 | 70.0 |
| Bench 3 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.46 | 10.39 | 18.19 | 2.00 | 75.2 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 3.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Ollie Watkins
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 35.14
- Actual score: 45.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Ivan Toney (projected gain 9.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.73 | 6.75 | 11.49 | 0.00 | 76.9 | 0.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.18 | 3.76 | 7.85 | 0.00 | 2.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.17 | 13.17 | 21.30 | 0.00 | 89.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.95 | 12.56 | 19.69 | 2.00 | 87.0 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 0.06 | 12.55 | 20.51 | 0.00 | 3.5 | 0.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 10.48 | 17.48 | 0.00 | 2.1 | 0.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.14 | 5.30 | 10.56 | 0.00 | 3.4 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.32 | 19.82 | 31.61 | 9.00 | 87.7 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 4.04 | 14.52 | 23.05 | 2.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.35 | 8.26 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 3.96 | 21.36 | 32.94 | 10.00 | 73.6 | 75.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.32 | 18.25 | 28.89 | 11.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.78 | 18.03 | 0.00 | 0.4 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.09 | 10.56 | 18.46 | 0.00 | 1.1 | 0.0 |
| XI | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.04 | 10.09 | 17.67 | 0.00 | 0.6 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 62.59
- Actual score: 92.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.07) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Martin Ødegaard (projected gain 13.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.07) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 1.63 | 3.84 | 7.00 | 7.00 | 44.9 | 90.0 |
| XI | XI | Alisson Ramses Becker | GK | 11 | 5.7 | 2.09 | 2.60 | 5.37 | 0.00 | 29.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.65 | 13.01 | 21.49 | 1.00 | 83.7 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.72 | 12.04 | 18.91 | 6.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 4.03 | 8.23 | 14.00 | 6.00 | 81.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.43 | 6.05 | 10.41 | 5.00 | 78.0 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.7 | 2.08 | 2.13 | 5.22 | 0.00 | 40.7 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.20 | 18.90 | 29.37 | 13.00 | 85.2 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 3.30 | 11.69 | 19.61 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 1.66 | 2.85 | 5.72 | 0.00 | 37.5 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 5.94 | 20.00 | 32.83 | 7.00 | 71.0 | 45.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.37 | 16.63 | 26.78 | 15.00 | 86.5 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.65 | 12.79 | 21.90 | 10.00 | 71.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.77 | 8.60 | 14.95 | 5.00 | 77.7 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.71 | 5.08 | 10.33 | 0.00 | 46.6 | 0.0 |
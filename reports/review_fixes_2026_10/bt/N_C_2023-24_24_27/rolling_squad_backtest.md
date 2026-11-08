# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 257.19
- Total actual points: 268.00
- Average predicted points: 64.30
- Average actual points: 67.00
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
- Captain: Phil Foden
- Vice captain: Ollie Watkins
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 59.71
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Alphonse Areola replaced Alisson Ramses Becker.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 3.59 | 9.75 | 15.82 | 0.00 | 85.7 | 0.0 |
| Bench 1 | Autosub In | Alphonse Areola | GK | 19 | 4.2 | 2.87 | 9.31 | 15.12 | 0.00 | 75.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.80 | 13.26 | 21.33 | 4.00 | 91.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.03 | 11.55 | 19.25 | 2.00 | 81.8 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.6 | 3.64 | 10.74 | 17.31 | 12.00 | 85.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.71 | 10.27 | 16.68 | 2.00 | 85.8 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.35 | 9.92 | 15.78 | 12.00 | 82.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 16.71 | 27.63 | 2.00 | 96.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.35 | 12.09 | 19.52 | 1.00 | 83.2 | 19.0 |
| Bench 3 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 3.58 | 9.79 | 15.97 | 5.00 | 69.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.87 | 17.22 | 28.39 | 15.00 | 86.3 | 66.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.07 | 16.52 | 26.44 | 3.00 | 96.2 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 5.24 | 14.83 | 23.82 | 4.00 | 72.1 | 33.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 5.37 | 14.71 | 24.16 | 2.00 | 91.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.68 | 13.72 | 22.13 | 10.00 | 86.5 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 70.95
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.38) beats the best remaining Bench Boost opportunity (9.73).
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Pedro Porro -> Fabian Schär (projected gain 0.11, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.38) beats the best remaining Bench Boost opportunity (9.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.28 | 9.58 | 15.56 | 3.00 | 84.6 | 90.0 |
| Bench 1 | Bench Boost | Alisson Ramses Becker | GK | 11 | 5.7 | 3.02 | 6.67 | 11.02 | 0.00 | 66.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.64 | 12.96 | 21.04 | 1.00 | 86.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 5.59 | 12.79 | 19.56 | 10.00 | 118.7 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 12.09 | 19.17 | 6.00 | 90.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 4.38 | 11.99 | 18.77 | 6.00 | 88.3 | 90.0 |
| Bench 2 | Bench Boost | Fabian Schär | DEF | 15 | 5.3 | 3.46 | 10.02 | 16.36 | 3.00 | 82.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.59 | 14.44 | 24.59 | 13.00 | 76.6 | 90.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 4.14 | 10.48 | 16.32 | 0.00 | 92.9 | 0.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.58 | 7.06 | 12.94 | 0.00 | 34.5 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.04 | 17.54 | 28.58 | 15.00 | 80.5 | 68.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.67 | 17.02 | 25.95 | 5.00 | 111.2 | 180.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 5.92 | 15.44 | 24.09 | 2.00 | 85.8 | 90.0 |
| Bench 3 | Bench Boost | Cole Palmer | MID | 7 | 5.8 | 3.08 | 11.26 | 19.53 | 2.00 | 64.4 | 70.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.49 | 11.15 | 18.67 | 2.00 | 58.2 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.60 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 63.60
- Actual score: 53.00
- Transfer: Richarlison de Andrade -> Pascal Groß (projected gain 4.77, hit 0)
- Autosub: Fabian Schär replaced Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.74 | 10.24 | 16.74 | 2.00 | 92.8 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.63 | 3.74 | 7.81 | 0.00 | 17.3 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.20 | 13.39 | 21.74 | 0.00 | 94.1 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 3.91 | 12.52 | 20.45 | 0.00 | 99.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.47 | 12.35 | 19.40 | 2.00 | 89.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.13 | 11.68 | 18.27 | 2.00 | 78.3 | 90.0 |
| Bench 2 | Autosub In | Fabian Schär | DEF | 15 | 5.3 | 2.39 | 8.45 | 14.37 | 0.00 | 73.3 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.66 | 20.28 | 32.25 | 9.00 | 120.3 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 1.73 | 5.86 | 10.89 | 0.00 | 24.1 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.69 | 4.31 | 8.19 | 0.00 | 12.3 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.76 | 21.13 | 32.52 | 10.00 | 106.5 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.65 | 18.50 | 29.18 | 11.00 | 113.4 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 4.89 | 14.82 | 24.45 | 0.00 | 67.2 | 6.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 5.39 | 14.66 | 23.12 | 7.00 | 100.5 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 3.04 | 10.54 | 18.42 | 0.00 | 52.5 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 1.30 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 62.93
- Actual score: 94.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.61) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Douglas Luiz Soares de Paulo (projected gain 3.26, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.61) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.73 | 10.41 | 16.82 | 13.00 | 97.8 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 11 | 5.7 | 0.58 | 2.66 | 5.51 | 0.00 | 9.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.46 | 13.16 | 21.55 | 1.00 | 88.8 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.34 | 12.11 | 18.98 | 6.00 | 84.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.08 | 11.21 | 17.29 | 6.00 | 77.6 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.3 | 3.00 | 8.94 | 15.16 | 12.00 | 76.1 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 11 | 6.3 | 2.73 | 8.22 | 14.05 | 6.00 | 55.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.41 | 18.74 | 29.66 | 13.00 | 92.8 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.69 | 4.03 | 8.12 | 0.00 | 13.3 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.42 | 2.81 | 5.78 | 0.00 | 8.1 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 6.61 | 19.86 | 31.59 | 7.00 | 82.0 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.93 | 17.11 | 27.55 | 15.00 | 91.8 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.6 | 4.15 | 11.69 | 18.56 | 4.00 | 82.4 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 3.42 | 11.52 | 19.98 | 2.00 | 37.6 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.57 | 11.39 | 18.59 | 1.00 | 70.1 | 31.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 282.27
- Total actual points: 237.00
- Average predicted points: 70.57
- Average actual points: 59.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW30 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 65.33
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.28 | 9.65 | 15.66 | 7.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.47 | 15.84 | 25.19 | 3.00 | 88.8 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | -0.15 | 14.12 | 24.58 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.16 | 13.53 | 20.43 | 0.00 | 87.5 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.72 | 10.47 | 16.97 | -1.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.49 | 10.25 | 17.10 | 4.00 | 84.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.11 | 17.75 | 28.35 | 2.00 | 86.7 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.46 | 15.65 | 25.41 | 2.00 | 89.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.43 | 15.23 | 24.06 | 4.00 | 88.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.22 | 21.47 | 34.92 | 13.00 | 87.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.67 | 17.26 | 28.21 | 2.00 | 85.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.93 | 15.50 | 23.87 | 3.00 | 88.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.67 | 14.83 | 22.65 | 10.00 | 87.6 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.16 | 12.10 | 18.85 | 2.00 | 90.7 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.98
- Actual score: 70.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.03 | 9.38 | 15.34 | 0.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.42 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.44 | 12.35 | 17.76 | 5.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.81 | 11.70 | 20.16 | 4.00 | 59.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.62 | 11.02 | 18.26 | 9.00 | 78.2 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.49 | 10.43 | 16.29 | 3.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 2.79 | 9.39 | 15.28 | 4.00 | 83.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.66 | 15.18 | 24.86 | 2.00 | 76.5 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.15 | 14.53 | 23.22 | 14.00 | 90.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.58 | 13.29 | 21.03 | 13.00 | 84.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.02 | 21.25 | 34.22 | 4.00 | 88.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.22 | 16.09 | 26.17 | 4.00 | 85.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.21 | 13.12 | 20.69 | 5.00 | 81.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.21 | 11.99 | 18.67 | 6.00 | 91.1 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.66 | 10.74 | 17.15 | 3.00 | 69.0 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 102.49
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.42) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Adrien Truffert -> Marcos Senesi Barón (projected gain 2.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.42) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.86 | 8.37 | 13.91 | 1.00 | 82.9 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.14 | 0.20 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.67 | 14.29 | 20.90 | 6.00 | 178.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.19 | 12.79 | 18.57 | 12.00 | 159.0 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.11 | 12.51 | 20.53 | 8.00 | 88.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.54 | 11.70 | 17.76 | 5.00 | 167.8 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.49 | 10.74 | 19.11 | 0.00 | 68.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.45 | 17.26 | 27.18 | 0.00 | 172.8 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.32 | 13.56 | 22.04 | 2.00 | 87.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.69 | 13.48 | 21.87 | 2.00 | 85.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.33 | 19.41 | 30.05 | 2.00 | 179.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.58 | 18.96 | 31.59 | 6.00 | 88.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.30 | 13.24 | 20.97 | 5.00 | 81.8 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.53 | 13.10 | 19.93 | 16.00 | 177.0 | 180.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.12 | 9.79 | 16.51 | 0.00 | 61.7 | 0.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 57.47
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Gordon -> Declan Rice (projected gain 6.79, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.17 | 9.76 | 15.83 | 1.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.34 | 0.50 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.00 | 17.03 | 26.51 | 4.00 | 89.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.52 | 15.20 | 24.20 | 8.00 | 88.0 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | -0.26 | 12.97 | 20.52 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | -0.32 | 12.65 | 21.04 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | -0.27 | 11.22 | 19.12 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.35 | 18.02 | 28.19 | 10.00 | 90.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.42 | 15.73 | 25.15 | 1.00 | 87.9 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.38 | 18.95 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.38 | 21.09 | 34.77 | 5.00 | 88.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.83 | 14.36 | 22.57 | 1.00 | 88.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.51 | 13.38 | 21.86 | 2.00 | 86.7 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | -0.22 | 13.05 | 21.40 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Cole Palmer | MID | 7 | 10.5 | -0.39 | 12.87 | 22.42 | 0.00 | 0.0 | 0.0 |
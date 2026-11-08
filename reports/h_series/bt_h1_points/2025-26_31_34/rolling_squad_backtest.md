# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 275.75
- Total actual points: 237.00
- Average predicted points: 68.94
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
- Predicted score: 64.07
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.12 | 9.37 | 15.70 | 7.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.05 | 0.22 | 0.00 | 3.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.31 | 16.02 | 25.46 | 3.00 | 90.0 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.03 | 13.50 | 20.35 | 0.00 | 90.0 | 36.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | -0.36 | 13.41 | 23.38 | 0.00 | 0.0 | 0.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.77 | 10.79 | 17.76 | -1.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.35 | 10.54 | 17.27 | 4.00 | 85.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.83 | 17.55 | 28.03 | 2.00 | 90.0 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.35 | 15.79 | 25.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.41 | 15.30 | 24.59 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.16 | 21.87 | 35.45 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.54 | 17.37 | 28.38 | 2.00 | 87.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.85 | 15.33 | 24.13 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.53 | 14.59 | 22.49 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.07 | 12.24 | 19.43 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.20
- Actual score: 70.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.10 | 9.82 | 15.78 | 0.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.15 | 0.25 | 0.38 | 0.00 | 4.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.22 | 11.89 | 17.27 | 5.00 | 88.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.64 | 11.26 | 19.64 | 4.00 | 62.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.54 | 10.91 | 18.01 | 9.00 | 77.5 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.33 | 10.09 | 16.35 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 2.69 | 9.48 | 15.66 | 4.00 | 83.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.34 | 14.70 | 24.20 | 2.00 | 78.3 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.06 | 14.44 | 23.21 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.43 | 13.33 | 21.48 | 13.00 | 85.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.85 | 21.43 | 34.43 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.95 | 15.66 | 25.66 | 4.00 | 86.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.04 | 13.21 | 20.91 | 5.00 | 81.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.19 | 12.09 | 18.57 | 6.00 | 88.9 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.51 | 10.86 | 17.47 | 3.00 | 67.9 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 100.43
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.05) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Adrien Truffert -> Marcos Senesi Barón (projected gain 2.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.05) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.86 | 8.37 | 13.91 | 1.00 | 82.9 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.01 | 0.11 | 0.21 | 0.00 | 4.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.64 | 14.13 | 20.68 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 7.97 | 12.40 | 18.08 | 12.00 | 160.1 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 3.95 | 12.20 | 20.54 | 8.00 | 88.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.46 | 11.66 | 18.13 | 5.00 | 169.6 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.44 | 10.96 | 19.44 | 0.00 | 68.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.19 | 16.94 | 26.67 | 0.00 | 173.7 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.55 | 13.73 | 22.31 | 2.00 | 86.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.23 | 13.72 | 22.14 | 2.00 | 86.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.18 | 19.11 | 30.29 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.33 | 19.01 | 31.57 | 6.00 | 90.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.41 | 13.28 | 20.32 | 16.00 | 175.4 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.07 | 12.79 | 20.58 | 5.00 | 82.7 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 2.94 | 9.95 | 16.91 | 0.00 | 62.0 | 0.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 56.05
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Gordon -> Declan Rice (projected gain 6.92, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.67) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.19 | 9.96 | 16.26 | 1.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.16 | 0.30 | 0.49 | 0.00 | 4.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.91 | 16.96 | 26.75 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.37 | 14.93 | 24.26 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | -0.30 | 12.29 | 19.77 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | -0.44 | 12.04 | 19.76 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | -0.29 | 10.58 | 17.99 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.29 | 17.75 | 28.00 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.27 | 15.79 | 25.45 | 1.00 | 90.0 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.38 | 18.95 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.17 | 20.95 | 34.80 | 5.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.70 | 14.23 | 22.84 | 1.00 | 89.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.39 | 13.52 | 21.83 | 2.00 | 86.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | -0.28 | 12.93 | 22.31 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | -0.30 | 12.48 | 20.66 | 0.00 | 0.0 | 0.0 |
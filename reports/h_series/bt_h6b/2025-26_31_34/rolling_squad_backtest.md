# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 279.54
- Total actual points: 237.00
- Average predicted points: 69.88
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
- Predicted score: 64.12
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.48 | 9.75 | 15.89 | 7.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.05 | 0.22 | 0.00 | 3.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.34 | 15.83 | 24.86 | 3.00 | 90.2 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | -0.09 | 13.36 | 23.43 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.86 | 12.37 | 18.74 | 0.00 | 87.3 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.95 | 10.35 | 17.29 | -1.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.54 | 9.90 | 16.19 | 4.00 | 83.5 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.80 | 16.75 | 26.67 | 2.00 | 85.2 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.23 | 15.38 | 25.05 | 2.00 | 89.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.20 | 14.90 | 23.24 | 4.00 | 86.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.16 | 21.34 | 34.41 | 13.00 | 89.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.61 | 17.33 | 28.89 | 2.00 | 87.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.87 | 14.93 | 23.11 | 3.00 | 87.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.48 | 14.35 | 21.71 | 10.00 | 86.3 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.19 | 12.30 | 18.78 | 2.00 | 89.9 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.63
- Actual score: 70.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.36 | 9.84 | 15.86 | 0.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.15 | 0.25 | 0.38 | 0.00 | 4.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.10 | 12.34 | 21.34 | 4.00 | 66.3 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.35 | 11.55 | 17.43 | 5.00 | 88.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.70 | 11.40 | 18.61 | 9.00 | 80.5 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.30 | 9.15 | 14.96 | 3.00 | 85.8 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 2.75 | 8.89 | 14.53 | 4.00 | 80.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.58 | 14.07 | 23.69 | 2.00 | 75.3 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.95 | 13.84 | 22.27 | 14.00 | 89.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.35 | 12.91 | 20.65 | 13.00 | 81.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.88 | 20.79 | 33.35 | 4.00 | 89.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.97 | 15.68 | 26.34 | 4.00 | 85.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.21 | 12.97 | 20.68 | 5.00 | 81.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.29 | 12.05 | 18.93 | 6.00 | 88.5 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.76 | 10.98 | 17.10 | 3.00 | 70.1 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 102.05
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.90) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Adrien Truffert -> Marcos Senesi Barón (projected gain 1.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.86 | 8.37 | 13.91 | 1.00 | 82.9 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.01 | 0.11 | 0.21 | 0.00 | 4.3 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.31 | 12.94 | 19.17 | 12.00 | 163.2 | 180.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.49 | 12.76 | 19.22 | 6.00 | 176.9 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.17 | 12.43 | 20.40 | 8.00 | 89.7 | 90.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.73 | 11.35 | 19.36 | 0.00 | 70.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.59 | 11.21 | 17.70 | 5.00 | 168.9 | 180.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.41 | 16.85 | 26.62 | 0.00 | 172.1 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.25 | 13.42 | 22.00 | 2.00 | 86.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.44 | 13.09 | 21.27 | 2.00 | 82.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.46 | 18.72 | 30.92 | 6.00 | 90.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.07 | 18.56 | 29.30 | 2.00 | 178.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.63 | 13.39 | 20.23 | 16.00 | 176.4 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.27 | 12.92 | 20.44 | 5.00 | 81.2 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.29 | 10.58 | 17.74 | 0.00 | 65.0 | 0.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 56.74
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.62) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Gordon -> Declan Rice (projected gain 6.58, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.62) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.45 | 10.01 | 16.45 | 1.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.16 | 0.30 | 0.49 | 0.00 | 4.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.85 | 16.70 | 25.79 | 4.00 | 89.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.34 | 14.58 | 23.43 | 8.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | -0.14 | 11.90 | 19.93 | 0.00 | 0.6 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | -0.08 | 11.62 | 19.33 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.07 | 10.20 | 17.78 | 0.00 | 1.5 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.12 | 17.21 | 26.95 | 10.00 | 89.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.07 | 15.33 | 24.22 | 1.00 | 85.7 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.38 | 18.95 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.12 | 20.56 | 34.00 | 5.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.74 | 13.73 | 21.62 | 1.00 | 87.3 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.21 | 13.45 | 22.40 | 0.00 | 2.8 | 0.0 |
| Bench 4 | Bench | Cole Palmer | MID | 7 | 10.5 | -0.17 | 13.33 | 23.47 | 0.00 | 0.0 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.52 | 13.18 | 21.56 | 2.00 | 86.7 | 90.0 |
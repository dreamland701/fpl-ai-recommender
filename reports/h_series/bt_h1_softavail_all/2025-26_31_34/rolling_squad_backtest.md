# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 277.51
- Total actual points: 239.00
- Average predicted points: 69.38
- Average actual points: 59.75
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
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.12 | 9.37 | 15.70 | 7.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.31 | 16.02 | 25.46 | 3.00 | 90.5 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.03 | 13.50 | 20.35 | 0.00 | 89.1 | 36.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | -0.36 | 13.41 | 23.38 | 0.00 | 0.0 | 0.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.77 | 10.79 | 17.76 | -1.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.35 | 10.54 | 17.27 | 4.00 | 87.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.83 | 17.55 | 28.03 | 2.00 | 88.9 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.35 | 15.79 | 25.55 | 2.00 | 90.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.41 | 15.30 | 24.59 | 4.00 | 90.8 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.16 | 21.87 | 35.45 | 13.00 | 89.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.54 | 17.37 | 28.38 | 2.00 | 87.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.85 | 15.33 | 24.13 | 3.00 | 90.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.53 | 14.59 | 22.49 | 10.00 | 89.9 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.07 | 12.24 | 19.43 | 2.00 | 92.3 | 90.0 |

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
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.10 | 9.82 | 15.78 | 0.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.42 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.22 | 11.89 | 17.27 | 5.00 | 89.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.64 | 11.26 | 19.64 | 4.00 | 63.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.54 | 10.91 | 18.01 | 9.00 | 79.2 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.33 | 10.09 | 16.35 | 3.00 | 88.2 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 2.69 | 9.48 | 15.66 | 4.00 | 85.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.34 | 14.70 | 24.20 | 2.00 | 77.7 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.06 | 14.44 | 23.21 | 14.00 | 90.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.43 | 13.33 | 21.48 | 13.00 | 86.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.85 | 21.43 | 34.43 | 4.00 | 90.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.95 | 15.66 | 25.66 | 4.00 | 86.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.04 | 13.21 | 20.91 | 5.00 | 82.8 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.19 | 12.09 | 18.57 | 6.00 | 92.0 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.51 | 10.86 | 17.47 | 3.00 | 70.3 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 100.41
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.04) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Adrien Truffert -> Marcos Senesi Barón (projected gain 2.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.04) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.86 | 8.37 | 13.91 | 1.00 | 82.9 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.14 | 0.20 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.64 | 14.13 | 20.68 | 6.00 | 180.9 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 7.97 | 12.40 | 18.08 | 12.00 | 158.7 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 3.95 | 12.20 | 20.54 | 8.00 | 89.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.46 | 11.66 | 18.13 | 5.00 | 170.6 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.44 | 10.96 | 19.44 | 0.00 | 71.2 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.19 | 16.94 | 26.67 | 0.00 | 174.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.55 | 13.73 | 22.31 | 2.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.23 | 13.72 | 22.14 | 2.00 | 87.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.18 | 19.11 | 30.29 | 2.00 | 180.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.33 | 19.01 | 31.57 | 6.00 | 89.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.41 | 13.28 | 20.32 | 16.00 | 177.9 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.07 | 12.79 | 20.58 | 5.00 | 82.8 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 2.94 | 9.95 | 16.91 | 0.00 | 64.0 | 0.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 57.83
- Actual score: 44.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Marcos Senesi Barón -> Konstantinos Mavropanos (projected gain 12.44, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.67) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.19 | 9.96 | 16.26 | 1.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.34 | 0.50 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.91 | 16.96 | 26.75 | 4.00 | 89.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.37 | 14.93 | 24.26 | 8.00 | 90.8 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.34 | 12.55 | 18.99 | 4.00 | 90.4 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | -0.30 | 12.29 | 19.77 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | -0.29 | 10.58 | 17.99 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.29 | 17.75 | 28.00 | 10.00 | 91.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.27 | 15.79 | 25.45 | 1.00 | 90.1 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.38 | 18.95 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.17 | 20.95 | 34.80 | 5.00 | 90.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.70 | 14.23 | 22.84 | 1.00 | 89.8 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 10.5 | -0.28 | 12.93 | 22.31 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Pascal Groß | MID | 6 | 5.5 | -0.30 | 12.48 | 20.66 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.56 | 7.02 | 13.54 | 0.00 | 35.1 | 0.0 |
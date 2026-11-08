# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 286.05
- Total actual points: 244.00
- Average predicted points: 71.51
- Average actual points: 61.00
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
- Predicted score: 65.45
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.26 | 9.72 | 16.02 | 7.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.52 | 16.27 | 25.85 | 3.00 | 88.9 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | -0.12 | 14.27 | 24.67 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.13 | 13.78 | 20.35 | 0.00 | 87.6 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.83 | 11.03 | 18.09 | -1.00 | 87.1 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.50 | 10.52 | 17.38 | 4.00 | 84.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.18 | 18.26 | 29.17 | 2.00 | 88.9 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.37 | 15.69 | 25.85 | 2.00 | 90.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.41 | 15.48 | 24.41 | 4.00 | 89.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.18 | 21.69 | 35.02 | 13.00 | 88.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.73 | 17.66 | 28.95 | 2.00 | 86.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.96 | 15.79 | 24.30 | 3.00 | 88.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.69 | 15.40 | 23.42 | 10.00 | 88.5 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.19 | 12.26 | 19.22 | 2.00 | 91.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.84
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.16) beats the best remaining Bench Boost opportunity (19.38).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.37, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.16) beats the best remaining Bench Boost opportunity (19.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.09 | 9.83 | 15.57 | 0.00 | 86.9 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.42 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.41 | 12.18 | 17.89 | 5.00 | 88.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.84 | 11.72 | 20.45 | 4.00 | 60.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.58 | 10.95 | 17.88 | 9.00 | 76.4 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.55 | 10.89 | 17.09 | 3.00 | 88.9 | 90.0 |
| Bench 4 | Bench Boost | Adrien Truffert | DEF | 4 | 4.6 | 2.83 | 9.54 | 15.65 | 4.00 | 84.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.58 | 14.97 | 24.58 | 2.00 | 74.9 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.15 | 14.57 | 23.23 | 14.00 | 90.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.59 | 13.38 | 21.33 | 13.00 | 84.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.96 | 21.54 | 34.73 | 4.00 | 90.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.20 | 16.22 | 26.19 | 4.00 | 84.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.11 | 13.24 | 21.12 | 5.00 | 81.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.22 | 11.92 | 18.50 | 6.00 | 90.5 | 90.0 |
| Bench 3 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.47 | 10.88 | 17.17 | 3.00 | 67.6 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 103.91
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.95) beats the best remaining Triple Captain opportunity (6.57).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Adrien Truffert -> Marcos Senesi Barón (projected gain 2.21, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.95) beats the best remaining Triple Captain opportunity (6.57).
- Autosub: Virgil van Dijk replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.86 | 8.37 | 13.91 | 1.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.14 | 0.20 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.79 | 14.36 | 21.40 | 6.00 | 179.2 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.20 | 12.83 | 18.81 | 12.00 | 158.6 | 180.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.3 | 4.12 | 12.50 | 20.95 | 8.00 | 88.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.51 | 11.93 | 18.60 | 5.00 | 168.4 | 180.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.40 | 11.25 | 19.64 | 0.00 | 67.7 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.39 | 17.25 | 27.62 | 0.00 | 172.7 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.27 | 13.74 | 22.38 | 2.00 | 85.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.56 | 13.62 | 22.00 | 2.00 | 85.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.35 | 19.36 | 30.18 | 2.00 | 179.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.57 | 19.16 | 32.07 | 6.00 | 89.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.23 | 13.31 | 21.06 | 5.00 | 80.2 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.48 | 13.17 | 19.99 | 16.00 | 176.4 | 180.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 2.98 | 10.15 | 17.05 | 0.00 | 62.2 | 0.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 49.84
- Actual score: 37.00
- Transfer: Anthony Gordon -> Declan Rice (projected gain 6.90, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.11 | 9.93 | 16.14 | 1.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.34 | 0.50 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.03 | 17.35 | 26.85 | 4.00 | 88.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.58 | 15.53 | 25.18 | 8.00 | 88.8 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | -0.23 | 13.06 | 20.76 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | -0.24 | 12.59 | 20.55 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | -0.16 | 11.30 | 18.76 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.32 | 18.05 | 28.33 | 10.00 | 90.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.31 | 16.00 | 25.40 | 1.00 | 88.7 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.38 | 18.95 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.29 | 21.39 | 35.05 | 5.00 | 88.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.82 | 14.51 | 22.73 | 1.00 | 88.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.45 | 13.50 | 21.87 | 2.00 | 85.9 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | -0.20 | 13.07 | 21.53 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Cole Palmer | MID | 7 | 10.5 | -0.37 | 12.62 | 21.55 | 0.00 | 0.0 | 0.0 |
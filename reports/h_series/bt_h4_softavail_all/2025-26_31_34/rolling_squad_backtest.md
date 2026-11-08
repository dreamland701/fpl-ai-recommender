# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 277.53
- Total actual points: 234.00
- Average predicted points: 69.38
- Average actual points: 58.50
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
- Predicted score: 62.25
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.03 | 9.46 | 15.74 | 7.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.22 | 15.78 | 25.63 | 3.00 | 91.1 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | -0.34 | 13.68 | 23.98 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.00 | 13.49 | 20.34 | 0.00 | 87.9 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.73 | 10.81 | 17.72 | -1.00 | 87.3 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.42 | 10.49 | 17.54 | 4.00 | 86.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.66 | 17.68 | 28.24 | 2.00 | 87.7 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.21 | 15.25 | 25.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.06 | 14.70 | 23.37 | 4.00 | 87.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.91 | 21.34 | 34.68 | 13.00 | 87.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.57 | 17.53 | 28.64 | 2.00 | 87.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.60 | 15.11 | 23.62 | 3.00 | 88.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.33 | 14.61 | 22.47 | 10.00 | 87.8 | 88.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.5 | 3.84 | 11.31 | 18.99 | 5.00 | 76.7 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 64.19
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.47) beats the best remaining Bench Boost opportunity (18.81).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.19, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.47) beats the best remaining Bench Boost opportunity (18.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.11 | 9.93 | 16.11 | 0.00 | 88.3 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.01 | 0.19 | 0.34 | 0.00 | 4.5 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.17 | 11.89 | 17.48 | 5.00 | 88.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.79 | 11.80 | 20.57 | 4.00 | 64.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.40 | 10.87 | 18.37 | 9.00 | 80.0 | 90.0 |
| Bench 3 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.23 | 9.76 | 15.52 | 3.00 | 85.2 | 90.0 |
| Bench 4 | Bench Boost | Adrien Truffert | DEF | 4 | 4.6 | 2.75 | 9.65 | 15.90 | 4.00 | 85.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.46 | 14.88 | 24.63 | 2.00 | 77.8 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.96 | 14.09 | 23.20 | 14.00 | 89.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.35 | 13.48 | 21.55 | 13.00 | 86.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.54 | 20.40 | 33.01 | 4.00 | 85.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.03 | 15.99 | 26.15 | 4.00 | 86.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.30 | 13.67 | 21.89 | 5.00 | 83.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.05 | 11.80 | 19.03 | 4.00 | 81.5 | 90.0 |
| Bench 2 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.48 | 10.70 | 17.41 | 3.00 | 71.2 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 2.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 101.00
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.05) beats the best remaining Triple Captain opportunity (6.13).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 2.48, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (17.05) beats the best remaining Triple Captain opportunity (6.13).
- Autosub: Elliot Anderson replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.86 | 8.37 | 13.91 | 1.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.10 | 1.41 | 1.70 | 0.00 | 7.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.47 | 13.76 | 20.47 | 6.00 | 178.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.11 | 12.88 | 19.19 | 12.00 | 161.7 | 180.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 4.03 | 12.88 | 21.33 | 8.00 | 90.0 | 90.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.6 | 7.65 | 12.08 | 18.84 | 13.00 | 175.5 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.42 | 11.63 | 18.29 | 5.00 | 170.6 | 180.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.22 | 17.27 | 27.02 | 0.00 | 175.7 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.19 | 13.47 | 22.47 | 2.00 | 87.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.39 | 13.36 | 21.78 | 2.00 | 85.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.10 | 18.81 | 29.54 | 2.00 | 179.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.22 | 18.54 | 30.96 | 6.00 | 86.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.17 | 13.21 | 21.00 | 5.00 | 85.1 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.5 | 4.12 | 11.34 | 18.19 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.02 | 9.90 | 17.59 | 0.00 | 66.3 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.50 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 50.10
- Actual score: 38.00
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 17.65, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.01 | 9.79 | 15.82 | 1.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.82 | 16.61 | 26.43 | 4.00 | 90.6 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | -0.32 | 12.58 | 20.30 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | -0.42 | 12.57 | 20.80 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | -0.39 | 12.24 | 20.37 | 0.00 | 0.7 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | -0.23 | 11.32 | 19.01 | 0.00 | 1.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.37 | 17.65 | 26.81 | 2.00 | 89.3 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.03 | 17.45 | 27.40 | 10.00 | 89.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.08 | 15.15 | 24.39 | 1.00 | 85.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.05 | 20.30 | 33.88 | 5.00 | 86.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.62 | 14.16 | 22.55 | 1.00 | 90.5 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 10.5 | -0.54 | 12.64 | 22.14 | 0.00 | 0.0 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.07 | 12.10 | 19.06 | 9.00 | 83.9 | 90.0 |
| XI | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.56 | 7.02 | 13.54 | 0.00 | 35.1 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 296.06
- Total actual points: 251.00
- Average predicted points: 74.01
- Average actual points: 62.75
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
- Predicted score: 67.15
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.31 | 9.10 | 14.60 | 6.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.29 | 0.52 | 0.00 | 3.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.71 | 16.74 | 26.43 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.39 | 24.52 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.46 | 14.22 | 21.66 | 0.00 | 90.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.45 | 12.57 | 19.80 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.94 | 11.17 | 18.07 | -1.00 | 87.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.21 | 18.01 | 28.83 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.47 | 15.34 | 24.24 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.33 | 15.00 | 24.38 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 21.75 | 35.01 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.80 | 17.58 | 28.79 | 2.00 | 88.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.79 | 15.41 | 23.62 | 10.00 | 90.0 | 88.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.11 | 15.33 | 23.96 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.12 | 12.10 | 18.91 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.90
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.85) beats the best remaining Bench Boost opportunity (19.92).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.85) beats the best remaining Bench Boost opportunity (19.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.51 | 7.62 | 12.66 | 0.00 | 78.8 | 0.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.51 | 0.71 | 0.00 | 4.6 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.56 | 12.09 | 18.34 | 5.00 | 88.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.00 | 11.75 | 20.30 | 4.00 | 63.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.84 | 11.40 | 18.95 | 9.00 | 79.1 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.71 | 11.30 | 17.90 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.31 | 10.42 | 17.14 | 4.00 | 82.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.68 | 14.74 | 24.69 | 2.00 | 78.4 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.07 | 13.77 | 22.33 | 14.00 | 88.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.56 | 13.06 | 21.04 | 13.00 | 84.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.08 | 21.32 | 34.45 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.19 | 15.84 | 26.23 | 4.00 | 87.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.32 | 12.83 | 20.68 | 5.00 | 80.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.18 | 11.57 | 18.24 | 6.00 | 87.6 | 90.0 |
| Bench 3 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.58 | 10.75 | 17.34 | 3.00 | 68.4 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 108.56
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.36) beats the best remaining Triple Captain opportunity (6.66).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Anthony Gordon -> Alex Scott (projected gain 0.86, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (17.36) beats the best remaining Triple Captain opportunity (6.66).
- Autosub: Virgil van Dijk replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.83 | 5.47 | 9.32 | 2.00 | 45.2 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.11 | 0.36 | 0.56 | 0.00 | 4.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 9.96 | 14.70 | 22.17 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.43 | 13.14 | 19.52 | 12.00 | 161.0 | 180.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.3 | 4.31 | 12.83 | 21.26 | 8.00 | 89.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.72 | 12.04 | 18.61 | 5.00 | 170.6 | 180.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.67 | 11.29 | 19.70 | 0.00 | 69.5 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.36 | 16.99 | 26.98 | 0.00 | 173.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.67 | 13.43 | 21.98 | 2.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.5 | 4.21 | 12.80 | 21.07 | 2.00 | 84.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.41 | 19.17 | 30.09 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.65 | 19.13 | 31.97 | 6.00 | 90.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.00 | 13.62 | 20.70 | 5.00 | 180.0 | 180.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.38 | 12.95 | 19.82 | 16.00 | 172.7 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.36 | 12.80 | 20.64 | 5.00 | 81.2 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 2.90 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 52.43
- Actual score: 39.00
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 6.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.59 | 7.60 | 12.41 | 3.00 | 72.2 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.26 | 0.55 | 0.88 | 0.00 | 4.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.20 | 17.48 | 27.44 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.75 | 15.58 | 25.14 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.56 | 21.75 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 13.56 | 21.84 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.95 | 19.60 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.61 | 18.10 | 27.67 | 2.00 | 90.0 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.22 | 17.22 | 27.04 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.44 | 15.85 | 25.43 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.35 | 21.02 | 34.80 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.98 | 23.66 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.93 | 13.75 | 22.14 | 1.00 | 88.5 | 90.0 |
| Bench 4 | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.23 | 20.97 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.18 | 21.57 | 0.00 | 0.0 | 0.0 |
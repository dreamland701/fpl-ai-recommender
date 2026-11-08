# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 295.63
- Total actual points: 251.00
- Average predicted points: 73.91
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
- Predicted score: 67.63
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.41 | 9.37 | 15.10 | 6.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.84 | 16.57 | 26.31 | 3.00 | 90.0 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.64 | 14.29 | 21.83 | 0.00 | 90.0 | 36.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.27 | 24.07 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.44 | 12.37 | 19.49 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.88 | 10.94 | 17.92 | -1.00 | 87.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.17 | 17.75 | 28.58 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.40 | 15.03 | 23.77 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.24 | 14.83 | 24.28 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.30 | 21.68 | 34.74 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.85 | 17.72 | 28.80 | 2.00 | 87.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.16 | 15.55 | 24.37 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.87 | 15.33 | 23.51 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.02 | 12.11 | 19.00 | 2.00 | 89.8 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.22
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.53) beats the best remaining Bench Boost opportunity (19.71).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.53) beats the best remaining Bench Boost opportunity (19.71).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.51 | 7.75 | 12.89 | 0.00 | 79.1 | 0.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.09 | 0.37 | 0.60 | 0.00 | 4.1 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.59 | 11.99 | 18.20 | 5.00 | 88.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.79 | 11.49 | 19.94 | 4.00 | 60.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.75 | 11.32 | 18.05 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 3.64 | 11.09 | 18.52 | 9.00 | 77.8 | 90.0 |
| Bench 4 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.33 | 10.31 | 16.95 | 4.00 | 82.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.46 | 14.42 | 24.31 | 2.00 | 78.3 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.97 | 13.63 | 22.12 | 14.00 | 86.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.37 | 12.69 | 20.47 | 13.00 | 83.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.90 | 21.03 | 33.79 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.07 | 15.91 | 26.36 | 4.00 | 84.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.20 | 12.57 | 20.26 | 5.00 | 79.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.18 | 11.62 | 18.42 | 6.00 | 87.2 | 90.0 |
| Bench 3 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.48 | 10.45 | 16.89 | 3.00 | 67.2 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 108.83
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.84) beats the best remaining Triple Captain opportunity (6.32).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Anthony Gordon -> Alex Scott (projected gain 1.08, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (17.84) beats the best remaining Triple Captain opportunity (6.32).
- Autosub: Virgil van Dijk replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.81 | 5.53 | 9.47 | 2.00 | 43.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.34 | 1.67 | 2.11 | 0.00 | 7.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 10.14 | 14.74 | 22.29 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.47 | 13.01 | 19.59 | 12.00 | 163.2 | 180.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.3 | 4.18 | 12.74 | 20.94 | 8.00 | 89.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.77 | 12.15 | 18.93 | 5.00 | 171.2 | 180.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.55 | 11.10 | 19.48 | 0.00 | 71.1 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.52 | 17.11 | 27.14 | 0.00 | 180.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.49 | 12.89 | 21.09 | 2.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.5 | 4.14 | 12.61 | 20.88 | 2.00 | 84.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.54 | 19.25 | 30.56 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.37 | 18.36 | 30.71 | 6.00 | 90.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.00 | 13.76 | 20.96 | 5.00 | 180.0 | 180.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.35 | 12.84 | 19.81 | 16.00 | 173.3 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.30 | 12.65 | 20.33 | 5.00 | 80.6 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 2.90 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 52.95
- Actual score: 39.00
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 5.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.65 | 7.67 | 12.49 | 3.00 | 73.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.35 | 17.81 | 28.02 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.84 | 15.72 | 25.37 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.64 | 22.22 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 13.60 | 22.26 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 12.22 | 20.25 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.73 | 17.98 | 27.62 | 2.00 | 90.0 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.39 | 17.15 | 27.06 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.48 | 15.61 | 24.85 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 20.49 | 34.05 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.82 | 23.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.97 | 13.67 | 22.07 | 1.00 | 88.7 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.33 | 21.97 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.20 | 21.20 | 0.00 | 0.0 | 0.0 |
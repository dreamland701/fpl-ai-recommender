# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 296.18
- Total actual points: 245.00
- Average predicted points: 74.05
- Average actual points: 61.25
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
- Predicted score: 68.07
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.43 | 9.45 | 15.41 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.91 | 16.30 | 26.08 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.47 | 24.06 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.71 | 14.05 | 21.50 | 0.00 | 90.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.46 | 12.20 | 19.24 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.85 | 10.78 | 17.85 | -1.00 | 88.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.24 | 17.86 | 29.02 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.48 | 15.25 | 24.31 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.31 | 15.16 | 25.13 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.30 | 21.47 | 34.35 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.81 | 17.50 | 28.22 | 2.00 | 87.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.24 | 15.83 | 24.91 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.88 | 15.06 | 23.10 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 3.99 | 12.24 | 19.31 | 2.00 | 89.7 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 64.91
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.08) beats the best remaining Bench Boost opportunity (18.90).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.08) beats the best remaining Bench Boost opportunity (18.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.46 | 7.76 | 12.96 | 0.00 | 79.7 | 0.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.04 | 0.18 | 0.00 | 4.1 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.58 | 11.83 | 17.91 | 5.00 | 88.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.64 | 11.17 | 19.56 | 4.00 | 58.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.73 | 11.12 | 17.83 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 3.44 | 10.74 | 18.06 | 9.00 | 76.0 | 90.0 |
| Bench 3 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.33 | 10.13 | 16.66 | 4.00 | 82.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.45 | 14.62 | 24.78 | 2.00 | 78.9 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.97 | 13.77 | 22.49 | 14.00 | 86.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.37 | 12.87 | 20.97 | 13.00 | 83.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.69 | 20.59 | 32.92 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.88 | 15.56 | 25.81 | 4.00 | 82.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.13 | 12.47 | 20.13 | 5.00 | 79.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.24 | 11.87 | 18.97 | 6.00 | 87.5 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.30 | 9.96 | 16.21 | 3.00 | 64.7 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 109.43
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.81) beats the best remaining Triple Captain opportunity (5.94).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Anthony Gordon -> Alex Scott (projected gain 1.65, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (17.81) beats the best remaining Triple Captain opportunity (5.94).
- Autosub: Jarrod Bowen replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.70 | 5.29 | 9.14 | 2.00 | 42.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.18 | 1.42 | 1.76 | 0.00 | 7.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 10.30 | 14.85 | 22.58 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.50 | 13.01 | 19.75 | 12.00 | 163.2 | 180.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.3 | 4.12 | 12.80 | 20.91 | 8.00 | 88.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.76 | 12.22 | 19.13 | 5.00 | 169.7 | 180.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.51 | 11.06 | 19.56 | 0.00 | 73.6 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 11.11 | 17.96 | 28.49 | 0.00 | 180.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.47 | 12.92 | 21.30 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Autosub In | Jarrod Bowen | FWD | 19 | 7.5 | 4.12 | 12.68 | 21.13 | 2.00 | 85.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.51 | 19.03 | 30.49 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.06 | 17.55 | 29.45 | 6.00 | 90.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.20 | 14.28 | 21.89 | 5.00 | 180.0 | 180.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.52 | 13.22 | 20.65 | 16.00 | 174.9 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.28 | 12.70 | 20.43 | 5.00 | 80.9 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 2.90 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 53.77
- Actual score: 39.00
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 5.29, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.67 | 7.68 | 12.49 | 3.00 | 75.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.52 | 18.08 | 28.50 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.92 | 15.80 | 25.62 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.92 | 22.90 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 13.87 | 23.18 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 12.60 | 21.09 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.82 | 17.72 | 27.25 | 2.00 | 90.0 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.62 | 17.38 | 27.64 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.71 | 16.07 | 25.55 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.22 | 19.99 | 33.46 | 5.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.06 | 13.83 | 22.50 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.82 | 22.98 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.63 | 22.28 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.39 | 23.59 | 0.00 | 0.0 | 0.0 |
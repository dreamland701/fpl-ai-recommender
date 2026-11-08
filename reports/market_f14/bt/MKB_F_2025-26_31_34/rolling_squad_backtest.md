# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 293.23
- Total actual points: 246.00
- Average predicted points: 73.31
- Average actual points: 61.50
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
- Predicted score: 67.83
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.40 | 9.35 | 15.01 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.07 | 0.00 | 1.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.79 | 16.91 | 26.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.62 | 14.52 | 22.01 | 0.00 | 90.0 | 36.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.49 | 24.64 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.43 | 12.54 | 19.76 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.85 | 10.98 | 17.83 | -1.00 | 86.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.40 | 18.55 | 29.71 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.55 | 15.60 | 24.74 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.33 | 15.13 | 24.76 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.31 | 21.95 | 35.36 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.63 | 17.08 | 27.95 | 2.00 | 86.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.18 | 15.67 | 24.57 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.88 | 15.57 | 23.82 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.04 | 12.04 | 18.96 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.65
- Actual score: 70.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.53 | 7.73 | 12.90 | 0.00 | 79.8 | 0.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.08 | 0.14 | 0.16 | 0.00 | 2.6 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.60 | 12.15 | 18.40 | 5.00 | 89.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.96 | 11.70 | 20.17 | 4.00 | 62.2 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.70 | 11.27 | 17.84 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.21 | 18.59 | 9.00 | 76.5 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.35 | 10.52 | 17.26 | 4.00 | 82.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.79 | 15.16 | 25.43 | 2.00 | 79.6 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.03 | 13.78 | 22.45 | 14.00 | 88.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.63 | 13.36 | 21.58 | 13.00 | 84.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.95 | 21.00 | 33.98 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.93 | 15.19 | 25.23 | 4.00 | 84.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.27 | 12.83 | 20.74 | 5.00 | 79.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.25 | 11.83 | 18.72 | 6.00 | 88.3 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.46 | 10.41 | 16.76 | 3.00 | 64.3 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 2.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 108.13
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.26) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Anthony Gordon -> Alex Scott (projected gain 1.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.72 | 5.21 | 8.95 | 2.00 | 43.2 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 10.05 | 14.85 | 22.43 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.25 | 12.89 | 19.13 | 12.00 | 163.1 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.25 | 12.64 | 20.92 | 8.00 | 86.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.62 | 11.94 | 18.50 | 5.00 | 172.2 | 180.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.67 | 11.27 | 19.66 | 0.00 | 69.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.80 | 17.70 | 28.18 | 0.00 | 180.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.67 | 13.57 | 22.29 | 2.00 | 84.2 | 90.0 |
| Bench 3 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.5 | 4.19 | 12.91 | 21.35 | 2.00 | 84.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.32 | 19.07 | 29.93 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.44 | 18.63 | 31.25 | 6.00 | 90.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.17 | 14.02 | 21.43 | 5.00 | 180.0 | 180.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.29 | 12.97 | 19.98 | 16.00 | 174.3 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.37 | 12.92 | 20.89 | 5.00 | 80.7 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 2.90 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 60.63
- Actual score: 44.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.89) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 5.96, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.89) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.59 | 7.65 | 12.56 | 3.00 | 73.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.12 | 0.23 | 0.41 | 0.00 | 2.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.38 | 17.95 | 28.12 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.91 | 15.93 | 25.61 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 13.77 | 22.46 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.53 | 21.99 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 12.20 | 20.29 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.71 | 18.36 | 28.09 | 2.00 | 90.0 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.31 | 17.58 | 27.71 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.52 | 16.23 | 26.10 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.39 | 21.17 | 35.08 | 5.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.04 | 14.15 | 22.81 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.60 | 21.94 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.41 | 23.09 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.35 | 22.20 | 0.00 | 0.0 | 0.0 |
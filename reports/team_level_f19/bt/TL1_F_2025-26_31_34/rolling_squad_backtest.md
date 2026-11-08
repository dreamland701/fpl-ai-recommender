# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 285.27
- Total actual points: 237.00
- Average predicted points: 71.32
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
- Predicted score: 63.55
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.71 | 18.15 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 2.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.64 | 16.50 | 26.05 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.64 | 24.82 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.45 | 14.14 | 21.35 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.91 | 11.17 | 18.06 | -1.00 | 86.6 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.74 | 10.85 | 17.66 | 4.00 | 84.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.26 | 18.23 | 29.24 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.61 | 15.73 | 24.80 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.46 | 15.53 | 25.33 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.26 | 21.73 | 35.07 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.67 | 17.22 | 28.16 | 2.00 | 87.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.20 | 15.68 | 24.61 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.83 | 15.51 | 23.61 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.1 | 4.11 | 11.45 | 18.22 | 2.00 | 82.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 1.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.97
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.75) beats the best remaining Bench Boost opportunity (17.61).
- Transfer: Virgil van Dijk -> Jan Paul van Hecke (projected gain 0.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.75) beats the best remaining Bench Boost opportunity (17.61).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.90 | 8.67 | 14.97 | 1.00 | 59.7 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.14 | 0.26 | 0.43 | 0.00 | 4.0 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.60 | 12.14 | 18.32 | 5.00 | 88.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.96 | 11.58 | 20.06 | 4.00 | 62.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.69 | 11.24 | 17.78 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Adrien Truffert | DEF | 4 | 4.6 | 3.08 | 9.83 | 16.24 | 4.00 | 82.9 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 1.96 | 6.49 | 11.06 | 2.00 | 46.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.80 | 15.12 | 25.33 | 2.00 | 78.0 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.14 | 14.09 | 23.06 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.65 | 13.45 | 21.75 | 13.00 | 85.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.14 | 21.45 | 34.52 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.16 | 15.70 | 25.94 | 4.00 | 86.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.38 | 13.10 | 21.22 | 5.00 | 81.1 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 3.67 | 11.32 | 17.95 | 12.00 | 84.6 | 90.0 |
| Bench 2 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.56 | 10.71 | 17.28 | 3.00 | 67.4 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 1.80 -> 0.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 109.54
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.26) beats the best remaining Triple Captain opportunity (6.59).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Anthony Gordon -> Antoine Semenyo (projected gain 3.07, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (17.26) beats the best remaining Triple Captain opportunity (6.59).
- Autosub: Jarrod Bowen replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.90 | 9.27 | 15.67 | 1.00 | 75.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.01 | 0.12 | 0.26 | 0.00 | 3.6 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.35 | 13.02 | 19.31 | 12.00 | 160.7 | 180.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.6 | 7.97 | 12.23 | 19.08 | 13.00 | 173.9 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.70 | 11.93 | 18.53 | 5.00 | 169.6 | 180.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.64 | 11.18 | 19.45 | 0.00 | 68.7 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 3.13 | 9.28 | 15.23 | 1.00 | 74.9 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.54 | 17.44 | 27.66 | 0.00 | 173.8 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.76 | 13.82 | 22.71 | 2.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Jarrod Bowen | FWD | 19 | 7.5 | 4.32 | 13.25 | 21.91 | 2.00 | 86.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.31 | 19.09 | 29.85 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.59 | 19.04 | 31.81 | 6.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 10.09 | 16.21 | 26.07 | 5.00 | 156.0 | 154.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.25 | 14.00 | 21.47 | 5.00 | 180.0 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.45 | 13.17 | 21.31 | 5.00 | 82.2 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.90 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 46.22
- Actual score: 44.00
- Transfer: Malick Thiaw -> Konstantinos Mavropanos (projected gain 4.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.38 | 12.11 | 19.28 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.14 | 0.28 | 0.50 | 0.00 | 4.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.69 | 15.30 | 24.74 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.62 | 22.19 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Adrien Truffert | DEF | 4 | 4.6 | 0.00 | 13.14 | 21.48 | 0.00 | 0.0 | 0.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.69 | 13.06 | 20.70 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 12.09 | 20.19 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.32 | 17.63 | 27.79 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.51 | 16.26 | 26.08 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.50 | 19.13 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.31 | 20.95 | 34.76 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 0.00 | 16.23 | 26.86 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.01 | 14.07 | 22.76 | 1.00 | 89.4 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.96 | 23.95 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.79 | 22.32 | 0.00 | 0.0 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 287.67
- Total actual points: 254.00
- Average predicted points: 71.92
- Average actual points: 63.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 63.15
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.75 | 18.21 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.06 | 0.27 | 0.00 | 3.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.56 | 16.30 | 25.72 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.68 | 24.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.27 | 13.68 | 20.78 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.93 | 11.13 | 18.01 | -1.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.66 | 10.37 | 16.08 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.26 | 18.22 | 29.15 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.51 | 15.50 | 24.51 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.43 | 15.37 | 25.06 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.19 | 21.60 | 34.77 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.70 | 17.25 | 28.16 | 2.00 | 87.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.98 | 16.06 | 25.08 | 10.00 | 90.0 | 88.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.14 | 15.53 | 24.34 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.20 | 12.41 | 19.46 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 69.60
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.16) beats the best remaining Bench Boost opportunity (19.00).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.16) beats the best remaining Bench Boost opportunity (19.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.28 | 9.50 | 16.31 | 1.00 | 71.7 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.31 | 0.43 | 0.56 | 0.00 | 3.8 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.50 | 11.91 | 18.06 | 5.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.02 | 11.79 | 20.29 | 4.00 | 62.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.89 | 11.48 | 18.96 | 9.00 | 79.0 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.64 | 11.11 | 17.59 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.58 | 9.69 | 15.27 | 8.00 | 85.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.83 | 15.25 | 25.44 | 2.00 | 78.8 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.16 | 14.14 | 22.97 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.71 | 13.58 | 21.87 | 13.00 | 85.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.08 | 21.35 | 34.42 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.19 | 15.79 | 26.04 | 4.00 | 87.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.43 | 13.23 | 21.31 | 5.00 | 82.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.27 | 11.90 | 18.84 | 6.00 | 88.8 | 90.0 |
| Bench 3 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.64 | 10.88 | 17.43 | 3.00 | 68.8 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 104.91
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.82) beats the best remaining Triple Captain opportunity (6.70).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.36, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.82) beats the best remaining Triple Captain opportunity (6.70).
- Autosub: Jarrod Bowen replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.97 | 9.43 | 15.94 | 1.00 | 76.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.13 | 0.19 | 0.00 | 3.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.83 | 14.53 | 21.88 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.39 | 12.99 | 21.41 | 8.00 | 89.6 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.25 | 12.89 | 19.08 | 12.00 | 158.8 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.65 | 11.93 | 18.42 | 5.00 | 169.6 | 180.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.80 | 8.00 | 13.86 | 1.00 | 73.4 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.58 | 17.40 | 27.61 | 0.00 | 173.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.84 | 14.01 | 22.89 | 2.00 | 87.0 | 90.0 |
| Bench 2 | Autosub In | Jarrod Bowen | FWD | 19 | 7.5 | 4.32 | 13.24 | 21.81 | 2.00 | 86.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.68 | 19.25 | 32.07 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.22 | 18.91 | 29.62 | 2.00 | 180.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.54 | 13.26 | 20.39 | 16.00 | 175.0 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.50 | 13.26 | 21.40 | 5.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.13 | 10.21 | 17.22 | 0.00 | 62.7 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.60 -> 2.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 50.01
- Actual score: 49.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 9.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.36 | 12.14 | 19.27 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.33 | 0.49 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.08 | 17.16 | 26.93 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 14.06 | 23.04 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.49 | 21.98 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.94 | 19.93 | 0.00 | 0.0 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.73 | 7.72 | 13.19 | 0.00 | 68.0 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.16 | 17.20 | 27.14 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.50 | 16.14 | 25.91 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 11.61 | 20.97 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 20.87 | 34.57 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.62 | 16.18 | 25.73 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.01 | 14.04 | 22.67 | 1.00 | 89.5 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.47 | 22.46 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 11.98 | 21.29 | 0.00 | 0.0 | 0.0 |
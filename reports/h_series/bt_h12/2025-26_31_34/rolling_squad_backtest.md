# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 283.77
- Total actual points: 254.00
- Average predicted points: 70.94
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
- Predicted score: 62.28
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.74 | 18.21 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.58 | 16.48 | 25.81 | 3.00 | 90.5 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | -0.06 | 14.67 | 24.75 | 0.00 | 0.5 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.29 | 13.84 | 20.98 | 0.00 | 89.9 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.81 | 11.08 | 17.81 | -1.00 | 87.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.54 | 10.32 | 15.84 | 1.00 | 89.9 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.19 | 18.23 | 29.03 | 2.00 | 89.7 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.45 | 15.49 | 24.63 | 4.00 | 91.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.31 | 15.30 | 24.85 | 2.00 | 90.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.19 | 21.78 | 34.94 | 13.00 | 90.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.57 | 17.16 | 27.95 | 2.00 | 87.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.07 | 15.58 | 24.29 | 3.00 | 89.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.64 | 15.25 | 23.14 | 10.00 | 89.7 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.10 | 12.33 | 19.36 | 2.00 | 91.3 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.68
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.88) beats the best remaining Bench Boost opportunity (18.61).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.88) beats the best remaining Bench Boost opportunity (18.61).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.84 | 8.78 | 14.95 | 1.00 | 60.3 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.42 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.49 | 11.98 | 18.15 | 5.00 | 89.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.90 | 11.72 | 19.98 | 4.00 | 62.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.70 | 11.22 | 18.48 | 9.00 | 77.8 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.59 | 11.17 | 17.54 | 3.00 | 90.4 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.48 | 9.55 | 15.16 | 8.00 | 86.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.69 | 15.08 | 25.20 | 2.00 | 78.1 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.06 | 14.05 | 22.82 | 14.00 | 90.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.57 | 13.34 | 21.70 | 13.00 | 86.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.02 | 21.33 | 34.43 | 4.00 | 90.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.06 | 15.67 | 25.83 | 4.00 | 86.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.28 | 13.07 | 20.98 | 5.00 | 81.6 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.18 | 11.83 | 18.86 | 6.00 | 90.1 | 90.0 |
| Bench 3 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.51 | 10.68 | 17.13 | 3.00 | 68.5 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 103.95
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.87) beats the best remaining Triple Captain opportunity (6.48).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.95, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.87) beats the best remaining Triple Captain opportunity (6.48).
- Autosub: Virgil van Dijk replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.79 | 9.24 | 15.41 | 1.00 | 75.8 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.14 | 0.20 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.85 | 14.58 | 21.89 | 6.00 | 181.1 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.22 | 12.89 | 18.99 | 12.00 | 160.3 | 180.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.3 | 4.18 | 12.71 | 20.87 | 8.00 | 88.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.58 | 11.94 | 18.31 | 5.00 | 169.9 | 180.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.77 | 7.94 | 13.78 | 1.00 | 73.0 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.56 | 17.42 | 27.54 | 0.00 | 174.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.67 | 13.74 | 22.58 | 2.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.19 | 13.15 | 21.62 | 2.00 | 86.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.27 | 19.08 | 29.81 | 2.00 | 180.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.51 | 19.06 | 31.73 | 6.00 | 90.2 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.46 | 13.21 | 20.33 | 16.00 | 176.6 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.33 | 13.07 | 21.04 | 5.00 | 82.6 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.04 | 10.12 | 16.97 | 0.00 | 62.6 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.60 -> 2.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 49.86
- Actual score: 49.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 9.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.33 | 12.23 | 19.39 | 10.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.34 | 0.50 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.09 | 17.37 | 27.16 | 4.00 | 90.0 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.62 | 21.97 | 0.00 | 0.6 | 0.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | -0.09 | 13.46 | 22.10 | 0.00 | 1.3 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | -0.06 | 11.96 | 19.86 | 0.00 | 0.8 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.74 | 7.74 | 13.22 | 0.00 | 68.2 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.23 | 17.46 | 27.43 | 10.00 | 90.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.43 | 16.12 | 25.99 | 1.00 | 91.2 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.38 | 18.95 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 21.02 | 34.74 | 5.00 | 90.4 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.67 | 16.48 | 26.02 | 13.00 | 90.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.89 | 14.07 | 22.50 | 1.00 | 89.9 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 10.5 | -0.07 | 13.82 | 23.70 | 0.00 | 0.6 | 0.0 |
| Bench 3 | Bench | Pascal Groß | MID | 6 | 5.5 | -0.09 | 13.41 | 22.44 | 0.00 | 1.4 | 0.0 |
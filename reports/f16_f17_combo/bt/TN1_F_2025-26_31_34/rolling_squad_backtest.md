# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 287.93
- Total actual points: 254.00
- Average predicted points: 71.98
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
- Predicted score: 63.24
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.80 | 18.21 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.12 | 0.39 | 0.00 | 4.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.66 | 16.51 | 26.00 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.70 | 24.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.38 | 13.94 | 21.15 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.88 | 11.04 | 17.94 | -1.00 | 86.0 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.71 | 10.42 | 16.12 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.31 | 18.27 | 29.24 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.55 | 15.55 | 24.60 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.46 | 15.43 | 25.13 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.17 | 21.60 | 34.93 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.73 | 17.30 | 28.23 | 2.00 | 88.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.19 | 15.63 | 24.50 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.75 | 15.26 | 23.35 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.23 | 12.44 | 19.49 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.22
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.97) beats the best remaining Bench Boost opportunity (18.79).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.89, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.97) beats the best remaining Bench Boost opportunity (18.79).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.96 | 8.83 | 15.21 | 1.00 | 60.3 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.31 | 0.43 | 0.62 | 0.00 | 4.2 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.46 | 11.88 | 18.10 | 5.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.01 | 11.72 | 20.26 | 4.00 | 62.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.18 | 18.63 | 9.00 | 76.9 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.61 | 11.06 | 17.60 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.54 | 9.60 | 15.22 | 8.00 | 84.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.74 | 15.00 | 25.23 | 2.00 | 77.3 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.09 | 13.98 | 22.85 | 14.00 | 88.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.62 | 13.33 | 21.63 | 13.00 | 84.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.98 | 21.13 | 34.29 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.09 | 15.57 | 25.85 | 4.00 | 85.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.33 | 12.99 | 21.09 | 5.00 | 80.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.22 | 11.82 | 18.81 | 6.00 | 87.6 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.51 | 10.56 | 17.10 | 3.00 | 66.4 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 105.85
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.97) beats the best remaining Triple Captain opportunity (6.67).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.50, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.97) beats the best remaining Triple Captain opportunity (6.67).
- Autosub: Jarrod Bowen replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.00 | 9.45 | 15.91 | 1.00 | 77.6 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.97 | 14.67 | 22.05 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.37 | 12.99 | 19.21 | 12.00 | 161.6 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.36 | 12.87 | 21.21 | 8.00 | 89.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.73 | 11.98 | 18.46 | 5.00 | 171.9 | 180.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.84 | 8.06 | 13.88 | 1.00 | 74.7 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.69 | 17.47 | 27.71 | 0.00 | 176.9 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.82 | 13.88 | 22.68 | 2.00 | 87.3 | 90.0 |
| Bench 2 | Autosub In | Jarrod Bowen | FWD | 19 | 7.5 | 4.34 | 13.24 | 21.78 | 2.00 | 87.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.66 | 19.11 | 31.86 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.37 | 19.07 | 29.84 | 2.00 | 180.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.65 | 13.34 | 20.47 | 16.00 | 177.9 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.49 | 13.21 | 21.30 | 5.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.14 | 10.18 | 17.13 | 0.00 | 63.5 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.60 -> 2.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 50.62
- Actual score: 49.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 10.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.47 | 12.39 | 19.58 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.16 | 0.30 | 0.00 | 0.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.20 | 17.44 | 27.32 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.31 | 21.91 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.30 | 21.79 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.74 | 19.74 | 0.00 | 0.0 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.71 | 7.68 | 13.22 | 0.00 | 67.6 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.29 | 17.52 | 27.58 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.56 | 16.23 | 26.03 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.53 | 19.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.35 | 21.04 | 34.81 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.63 | 16.23 | 25.93 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.05 | 14.13 | 22.77 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.98 | 24.30 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.29 | 22.29 | 0.00 | 0.0 | 0.0 |
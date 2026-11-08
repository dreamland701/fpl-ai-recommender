# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 288.52
- Total actual points: 245.00
- Average predicted points: 72.13
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 64.34
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 11.62 | 19.63 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.10 | 0.29 | 0.00 | 3.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.49 | 16.07 | 25.32 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.28 | 24.27 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.38 | 13.91 | 21.11 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.96 | 11.21 | 18.13 | -1.00 | 87.7 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.75 | 10.52 | 16.29 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.37 | 18.48 | 29.61 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.92 | 16.62 | 26.32 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.76 | 16.26 | 26.48 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.42 | 22.19 | 35.70 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.65 | 17.10 | 27.94 | 2.00 | 86.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.34 | 16.03 | 25.11 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.62 | 14.90 | 22.75 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.43 | 12.93 | 20.26 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.80
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.97) beats the best remaining Bench Boost opportunity (16.76).
- Transfer: Virgil van Dijk -> Jan Paul van Hecke (projected gain 1.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.97) beats the best remaining Bench Boost opportunity (16.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.38 | 10.00 | 17.04 | 1.00 | 65.3 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.29 | 0.39 | 0.49 | 0.00 | 2.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.60 | 12.21 | 18.53 | 5.00 | 89.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.90 | 11.46 | 19.82 | 4.00 | 61.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.63 | 11.10 | 17.56 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.51 | 9.54 | 15.04 | 8.00 | 84.6 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 1.87 | 6.22 | 10.59 | 2.00 | 45.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.87 | 15.35 | 25.68 | 2.00 | 79.4 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.38 | 14.76 | 23.97 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.08 | 14.60 | 23.56 | 13.00 | 89.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.07 | 21.33 | 34.48 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.03 | 15.38 | 25.46 | 4.00 | 84.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.52 | 13.51 | 21.83 | 5.00 | 82.2 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.31 | 12.07 | 19.15 | 6.00 | 89.0 | 90.0 |
| Bench 3 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.29 | 9.96 | 16.04 | 3.00 | 64.9 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 1.90 -> 0.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 105.63
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.69) beats the best remaining Triple Captain opportunity (6.68).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Omar Alderete -> Marcos Senesi Barón (projected gain 3.50, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.69) beats the best remaining Triple Captain opportunity (6.68).
- Autosub: Gabriel dos Santos Magalhães replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.32 | 10.42 | 17.57 | 1.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.10 | 0.13 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.70 | 14.35 | 21.60 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.43 | 13.13 | 19.49 | 12.00 | 161.0 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.63 | 11.91 | 18.42 | 5.00 | 168.5 | 180.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.54 | 10.93 | 19.12 | 0.00 | 68.1 | 90.0 |
| Bench 3 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 3.03 | 9.04 | 14.79 | 1.00 | 74.2 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.74 | 17.64 | 28.06 | 0.00 | 175.5 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.10 | 14.73 | 24.12 | 2.00 | 89.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.47 | 13.65 | 22.49 | 2.00 | 86.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.67 | 19.26 | 32.21 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.09 | 18.74 | 29.38 | 2.00 | 180.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.74 | 13.60 | 20.97 | 16.00 | 176.7 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.55 | 13.45 | 21.76 | 5.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 2.84 | 9.44 | 16.06 | 0.00 | 59.2 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.80 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 50.75
- Actual score: 55.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 9.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 13.39 | 21.25 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.30 | 0.44 | 0.00 | 3.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.57 | 15.10 | 24.36 | 8.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.39 | 21.88 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.01 | 21.34 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.80 | 19.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 2.77 | 8.63 | 14.67 | 2.00 | 76.0 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.39 | 17.79 | 28.03 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.90 | 17.22 | 27.68 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.25 | 18.74 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.38 | 21.21 | 35.19 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.45 | 15.68 | 24.93 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.10 | 14.32 | 23.15 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.68 | 22.86 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.56 | 23.36 | 0.00 | 0.0 | 0.0 |
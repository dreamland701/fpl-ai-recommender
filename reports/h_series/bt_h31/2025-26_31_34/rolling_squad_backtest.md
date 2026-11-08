# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 279.25
- Total actual points: 254.00
- Average predicted points: 69.81
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
- Predicted score: 61.35
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.74 | 18.21 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.43 | 16.22 | 25.69 | 3.00 | 91.4 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | -0.25 | 14.08 | 24.23 | 0.00 | 0.3 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.26 | 13.88 | 21.28 | 0.00 | 93.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.72 | 10.76 | 17.69 | -1.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.51 | 10.31 | 16.01 | 1.00 | 92.1 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.11 | 18.04 | 28.90 | 2.00 | 92.1 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.36 | 15.25 | 24.17 | 4.00 | 92.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.19 | 15.17 | 24.79 | 2.00 | 92.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.18 | 21.84 | 35.34 | 13.00 | 92.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.49 | 17.20 | 27.91 | 2.00 | 89.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.98 | 15.50 | 24.41 | 3.00 | 91.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.45 | 14.71 | 22.57 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.05 | 12.13 | 18.96 | 2.00 | 92.9 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.87
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.49) beats the best remaining Bench Boost opportunity (18.11).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.49) beats the best remaining Bench Boost opportunity (18.11).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.75 | 8.68 | 14.91 | 1.00 | 62.3 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.42 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.47 | 12.17 | 18.42 | 5.00 | 91.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.66 | 11.18 | 19.30 | 4.00 | 62.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.50 | 10.92 | 18.21 | 9.00 | 78.8 | 90.0 |
| Bench 3 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.41 | 10.91 | 17.48 | 3.00 | 91.3 | 90.0 |
| Bench 2 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.44 | 9.61 | 15.50 | 8.00 | 87.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.58 | 14.76 | 24.90 | 2.00 | 79.7 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.00 | 14.13 | 23.12 | 14.00 | 93.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.43 | 13.28 | 21.65 | 13.00 | 87.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.88 | 21.08 | 34.34 | 4.00 | 91.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.94 | 15.51 | 25.59 | 4.00 | 87.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.19 | 12.97 | 21.19 | 5.00 | 84.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.10 | 11.75 | 18.56 | 6.00 | 91.2 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.34 | 10.42 | 16.98 | 3.00 | 70.3 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 103.06
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.79) beats the best remaining Triple Captain opportunity (6.50).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.89, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.79) beats the best remaining Triple Captain opportunity (6.50).
- Autosub: Virgil van Dijk replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.74 | 8.96 | 15.41 | 1.00 | 77.2 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.14 | 0.20 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.74 | 14.50 | 21.79 | 6.00 | 182.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.20 | 12.92 | 19.25 | 12.00 | 162.9 | 180.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.3 | 4.13 | 12.70 | 21.11 | 8.00 | 90.2 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.51 | 11.46 | 17.72 | 5.00 | 170.8 | 180.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.77 | 7.94 | 13.78 | 1.00 | 73.0 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.40 | 17.23 | 27.26 | 0.00 | 175.2 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.66 | 13.73 | 22.88 | 2.00 | 89.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.15 | 13.09 | 21.68 | 2.00 | 88.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.52 | 19.11 | 31.96 | 6.00 | 92.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.19 | 18.91 | 29.75 | 2.00 | 182.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.37 | 13.05 | 20.04 | 16.00 | 177.9 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.22 | 12.79 | 20.86 | 5.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 2.84 | 9.86 | 16.73 | 0.00 | 63.8 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.60 -> 2.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 48.98
- Actual score: 49.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 9.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.22 | 12.07 | 19.42 | 10.00 | 92.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.34 | 0.50 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.07 | 17.33 | 27.28 | 4.00 | 92.0 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | -0.26 | 12.84 | 20.87 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | -0.29 | 12.84 | 21.24 | 0.00 | 1.4 | 0.0 |
| Bench 4 | Bench | James Hill | DEF | 4 | 4.2 | -0.36 | 10.95 | 18.95 | 0.00 | 0.0 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.74 | 7.74 | 13.22 | 0.00 | 68.2 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.23 | 17.69 | 27.81 | 10.00 | 92.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.33 | 15.83 | 25.48 | 1.00 | 92.5 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.38 | 18.95 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.22 | 20.97 | 34.70 | 5.00 | 92.3 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.58 | 16.28 | 25.85 | 13.00 | 92.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.86 | 13.97 | 22.69 | 1.00 | 92.5 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | -0.22 | 13.29 | 22.95 | 0.00 | 0.9 | 0.0 |
| Bench 3 | Bench | Pascal Groß | MID | 6 | 5.5 | -0.33 | 12.69 | 21.25 | 0.00 | 0.1 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 288.01
- Total actual points: 254.00
- Average predicted points: 72.00
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
- Predicted score: 63.27
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.80 | 18.20 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.12 | 0.39 | 0.00 | 4.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.66 | 16.52 | 26.01 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.70 | 24.83 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.38 | 13.95 | 21.15 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.89 | 11.04 | 17.94 | -1.00 | 85.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.72 | 10.43 | 16.13 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.31 | 18.27 | 29.24 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.55 | 15.56 | 24.60 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.47 | 15.43 | 25.13 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.17 | 21.61 | 34.94 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.73 | 17.30 | 28.23 | 2.00 | 88.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.19 | 15.64 | 24.50 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.75 | 15.27 | 23.36 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.24 | 12.45 | 19.49 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.25
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.98) beats the best remaining Bench Boost opportunity (18.79).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.89, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.98) beats the best remaining Bench Boost opportunity (18.79).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.96 | 8.82 | 15.21 | 1.00 | 60.3 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.31 | 0.43 | 0.63 | 0.00 | 4.2 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.47 | 11.88 | 18.11 | 5.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.00 | 11.71 | 20.26 | 4.00 | 62.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.17 | 18.62 | 9.00 | 76.8 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.61 | 11.06 | 17.61 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.54 | 9.60 | 15.22 | 8.00 | 84.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.75 | 15.00 | 25.23 | 2.00 | 77.3 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.09 | 13.98 | 22.85 | 14.00 | 88.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.62 | 13.33 | 21.63 | 13.00 | 83.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.99 | 21.14 | 34.29 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.09 | 15.57 | 25.85 | 4.00 | 85.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.33 | 12.99 | 21.09 | 5.00 | 80.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.23 | 11.82 | 18.81 | 6.00 | 87.6 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.51 | 10.57 | 17.11 | 3.00 | 66.4 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 105.86
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.97) beats the best remaining Triple Captain opportunity (6.67).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.51, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.97) beats the best remaining Triple Captain opportunity (6.67).
- Autosub: Jarrod Bowen replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.00 | 9.45 | 15.90 | 1.00 | 77.6 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.97 | 14.68 | 22.06 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.37 | 13.00 | 19.21 | 12.00 | 161.6 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.36 | 12.87 | 21.21 | 8.00 | 89.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.73 | 11.99 | 18.46 | 5.00 | 171.9 | 180.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.84 | 8.06 | 13.87 | 1.00 | 74.7 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.69 | 17.47 | 27.71 | 0.00 | 176.9 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.82 | 13.88 | 22.68 | 2.00 | 87.3 | 90.0 |
| Bench 2 | Autosub In | Jarrod Bowen | FWD | 19 | 7.5 | 4.35 | 13.24 | 21.78 | 2.00 | 87.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.66 | 19.11 | 31.86 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.37 | 19.07 | 29.84 | 2.00 | 180.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.65 | 13.35 | 20.48 | 16.00 | 178.0 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.49 | 13.21 | 21.30 | 5.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.14 | 10.18 | 17.13 | 0.00 | 63.5 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.60 -> 2.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 50.63
- Actual score: 49.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 11.29, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.47 | 12.39 | 19.58 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.15 | 0.28 | 0.00 | 0.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.20 | 17.45 | 27.32 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.31 | 21.91 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.29 | 21.79 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.73 | 19.74 | 0.00 | 0.0 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.71 | 7.68 | 13.22 | 0.00 | 67.5 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.30 | 17.53 | 27.58 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.56 | 16.23 | 26.04 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.53 | 19.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.35 | 21.05 | 34.81 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.63 | 16.23 | 25.93 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.05 | 14.14 | 22.77 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.99 | 24.33 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.29 | 22.29 | 0.00 | 0.0 | 0.0 |
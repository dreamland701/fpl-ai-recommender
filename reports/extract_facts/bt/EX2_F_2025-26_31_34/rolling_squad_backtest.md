# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 289.31
- Total actual points: 254.00
- Average predicted points: 72.33
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
- Predicted score: 64.50
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.81 | 18.21 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.10 | 0.36 | 0.00 | 3.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.58 | 16.33 | 25.70 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.73 | 24.85 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.57 | 14.28 | 21.82 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.90 | 11.07 | 17.97 | -1.00 | 86.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.71 | 10.42 | 16.09 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.56 | 18.80 | 30.12 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.81 | 16.07 | 25.49 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.45 | 15.40 | 25.04 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.42 | 22.06 | 35.74 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.71 | 17.26 | 28.12 | 2.00 | 87.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.94 | 15.61 | 24.00 | 10.00 | 90.0 | 88.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.15 | 15.53 | 24.31 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.24 | 12.45 | 19.47 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 69.21
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.03) beats the best remaining Bench Boost opportunity (18.90).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.03) beats the best remaining Bench Boost opportunity (18.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.97 | 8.88 | 15.27 | 1.00 | 60.5 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.32 | 0.44 | 0.64 | 0.00 | 4.2 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.44 | 11.81 | 18.00 | 5.00 | 86.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.03 | 11.78 | 20.33 | 4.00 | 62.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.86 | 11.41 | 18.93 | 9.00 | 78.1 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.60 | 11.02 | 17.54 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.54 | 9.62 | 15.23 | 8.00 | 84.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.78 | 15.13 | 25.34 | 2.00 | 77.5 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.10 | 14.03 | 22.87 | 14.00 | 88.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.66 | 13.46 | 21.76 | 13.00 | 84.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.30 | 21.71 | 35.36 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.13 | 15.68 | 25.97 | 4.00 | 85.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.38 | 13.11 | 21.24 | 5.00 | 80.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.23 | 11.81 | 18.78 | 6.00 | 87.5 | 90.0 |
| Bench 3 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.57 | 10.74 | 17.30 | 3.00 | 67.1 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 105.54
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.86) beats the best remaining Triple Captain opportunity (6.74).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.31, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.86) beats the best remaining Triple Captain opportunity (6.74).
- Autosub: Jarrod Bowen replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.04 | 9.54 | 16.03 | 1.00 | 78.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.86 | 14.55 | 21.87 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.43 | 13.03 | 21.43 | 8.00 | 90.0 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.30 | 12.93 | 19.10 | 12.00 | 160.2 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.72 | 11.98 | 18.44 | 5.00 | 171.6 | 180.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.86 | 8.11 | 13.94 | 1.00 | 75.0 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.66 | 17.46 | 27.64 | 0.00 | 175.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.87 | 14.02 | 22.84 | 2.00 | 87.9 | 90.0 |
| Bench 2 | Autosub In | Jarrod Bowen | FWD | 19 | 7.5 | 4.37 | 13.31 | 21.86 | 2.00 | 87.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.71 | 19.27 | 32.03 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.26 | 18.94 | 29.61 | 2.00 | 180.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.63 | 13.33 | 20.43 | 16.00 | 177.5 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.53 | 13.30 | 21.42 | 5.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.17 | 10.26 | 17.22 | 0.00 | 63.8 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.60 -> 2.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 50.05
- Actual score: 49.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 10.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.41 | 12.23 | 19.32 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.05 | 0.13 | 0.25 | 0.00 | 0.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.10 | 17.19 | 26.92 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.62 | 22.64 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.34 | 21.84 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.76 | 19.78 | 0.00 | 0.0 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.71 | 7.66 | 13.19 | 0.00 | 67.4 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.17 | 17.21 | 27.09 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.52 | 16.15 | 25.86 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 7.37 | 15.27 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.28 | 20.88 | 34.51 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.55 | 16.05 | 25.64 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.03 | 14.08 | 22.67 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.32 | 22.32 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 12.50 | 22.35 | 0.00 | 0.0 | 0.0 |
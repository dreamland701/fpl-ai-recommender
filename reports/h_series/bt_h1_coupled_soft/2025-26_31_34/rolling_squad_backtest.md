# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 287.55
- Total actual points: 243.00
- Average predicted points: 71.89
- Average actual points: 60.75
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
- Predicted score: 63.36
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.74 | 18.21 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.64 | 16.49 | 26.00 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.65 | 24.83 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.38 | 13.95 | 21.17 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.89 | 11.07 | 17.94 | -1.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.66 | 10.36 | 16.07 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.29 | 18.26 | 29.27 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.53 | 15.55 | 24.63 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.43 | 15.37 | 25.09 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 21.79 | 35.09 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.70 | 17.25 | 28.21 | 2.00 | 87.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.19 | 15.65 | 24.53 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.76 | 15.30 | 23.41 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.20 | 12.40 | 19.46 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.51
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.77) beats the best remaining Bench Boost opportunity (18.21).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.77) beats the best remaining Bench Boost opportunity (18.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.69 | 8.57 | 14.90 | 1.00 | 60.0 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.42 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.51 | 11.97 | 18.16 | 5.00 | 88.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.66 | 11.15 | 17.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.66 | 11.10 | 18.52 | 9.00 | 77.5 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.35 | 11.07 | 19.55 | 4.00 | 62.2 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.53 | 9.63 | 15.21 | 8.00 | 85.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.61 | 14.92 | 25.12 | 2.00 | 78.3 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.14 | 14.08 | 22.92 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.64 | 13.41 | 21.69 | 13.00 | 85.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.07 | 21.31 | 34.44 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.08 | 15.60 | 25.85 | 4.00 | 86.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.33 | 13.04 | 21.12 | 5.00 | 81.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.27 | 11.90 | 18.86 | 6.00 | 88.9 | 90.0 |
| Bench 2 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.59 | 10.71 | 17.24 | 3.00 | 67.9 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 103.73
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.91) beats the best remaining Triple Captain opportunity (6.62).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.99, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.91) beats the best remaining Triple Captain opportunity (6.62).
- Autosub: Virgil van Dijk replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.78 | 9.15 | 15.63 | 1.00 | 75.7 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.14 | 0.20 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.93 | 14.64 | 22.04 | 6.00 | 180.0 | 180.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.3 | 4.28 | 12.75 | 21.13 | 8.00 | 88.4 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 7.55 | 12.56 | 18.85 | 12.00 | 160.1 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.43 | 11.80 | 18.31 | 5.00 | 169.6 | 180.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.77 | 7.94 | 13.78 | 1.00 | 73.0 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.52 | 17.34 | 27.60 | 0.00 | 173.7 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.75 | 13.79 | 22.64 | 2.00 | 86.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.31 | 13.17 | 21.74 | 2.00 | 86.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.61 | 19.05 | 31.85 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.31 | 19.01 | 29.80 | 2.00 | 180.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.57 | 13.28 | 20.44 | 16.00 | 175.4 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.34 | 13.03 | 21.15 | 5.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.04 | 10.05 | 17.04 | 0.00 | 62.0 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.60 -> 1.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 52.95
- Actual score: 38.00
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 17.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.42 | 12.29 | 19.49 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.34 | 0.50 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.18 | 17.40 | 27.29 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.51 | 22.11 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.48 | 21.98 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.94 | 19.94 | 0.00 | 0.0 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.74 | 7.74 | 13.22 | 0.00 | 68.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.58 | 18.01 | 27.50 | 2.00 | 90.0 | 79.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.29 | 17.51 | 27.59 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.53 | 16.19 | 26.03 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.33 | 21.01 | 34.81 | 5.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.98 | 14.05 | 22.71 | 1.00 | 89.9 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.84 | 23.76 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.48 | 22.49 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.56 | 7.02 | 13.54 | 0.00 | 35.1 | 0.0 |
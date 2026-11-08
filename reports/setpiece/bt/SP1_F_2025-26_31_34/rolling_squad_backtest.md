# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 291.51
- Total actual points: 262.00
- Average predicted points: 72.88
- Average actual points: 65.50
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
- Predicted score: 63.41
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.73 | 18.19 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.09 | 0.31 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.63 | 16.40 | 25.84 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.58 | 24.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.38 | 13.90 | 21.08 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.91 | 11.08 | 17.95 | -1.00 | 86.7 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.66 | 10.37 | 16.10 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.27 | 18.03 | 28.83 | 2.00 | 90.0 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.59 | 16.23 | 26.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.58 | 15.81 | 25.17 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 21.88 | 35.22 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.61 | 16.89 | 27.51 | 2.00 | 86.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.22 | 15.91 | 25.05 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.69 | 15.09 | 22.99 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.17 | 12.31 | 19.26 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.27
- Actual score: 81.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.08) beats the best remaining Bench Boost opportunity (17.66).
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 1.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.08) beats the best remaining Bench Boost opportunity (17.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.94 | 8.79 | 15.11 | 1.00 | 59.9 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.43 | 0.58 | 0.00 | 3.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.98 | 11.63 | 20.08 | 4.00 | 61.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.79 | 11.16 | 18.51 | 9.00 | 77.3 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.66 | 11.15 | 17.66 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.57 | 9.69 | 15.30 | 8.00 | 85.3 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 1.96 | 6.41 | 10.88 | 2.00 | 46.4 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.30 | 14.94 | 24.58 | 14.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.76 | 14.89 | 24.91 | 2.00 | 77.7 | 81.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.71 | 13.71 | 22.29 | 13.00 | 85.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.07 | 21.38 | 34.54 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.06 | 15.38 | 25.35 | 4.00 | 85.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.41 | 13.36 | 21.68 | 5.00 | 82.8 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.4 | 4.45 | 12.91 | 20.81 | 2.00 | 83.2 | 83.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 6 | 5.5 | 4.24 | 11.84 | 18.70 | 6.00 | 89.3 | 90.0 |

## GW33

- Train rows: 186014
- Bank: -0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 100.51
- Actual score: 77.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.39) beats the best remaining Triple Captain opportunity (6.59).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 3.49, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.39) beats the best remaining Triple Captain opportunity (6.59).
- Autosub: Morgan Gibbs-White replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.92 | 9.26 | 15.70 | 1.00 | 75.6 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.15 | 0.22 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.92 | 14.59 | 21.95 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.29 | 12.66 | 20.94 | 8.00 | 88.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.63 | 11.88 | 18.35 | 5.00 | 169.4 | 180.0 |
| Bench 3 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 3.13 | 9.23 | 15.06 | 1.00 | 75.3 | 90.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.77 | 7.96 | 13.83 | 1.00 | 73.0 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.52 | 17.15 | 27.19 | 0.00 | 172.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.82 | 14.05 | 23.17 | 2.00 | 86.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.46 | 14.03 | 23.42 | 2.00 | 88.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.60 | 19.06 | 31.83 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.14 | 18.69 | 29.16 | 2.00 | 180.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.49 | 13.44 | 21.85 | 5.00 | 83.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.47 | 13.18 | 20.22 | 16.00 | 176.1 | 180.0 |
| Bench 2 | Autosub In | Morgan Gibbs-White | MID | 16 | 7.4 | 4.42 | 12.00 | 19.46 | 20.00 | 75.5 | 88.0 |

## GW34

- Train rows: 186843
- Bank: 1.90 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.32
- Actual score: 53.00
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 6.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.41 | 12.24 | 19.41 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.35 | 0.52 | 0.00 | 5.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.17 | 17.31 | 27.12 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.46 | 22.03 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.94 | 19.95 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 2.88 | 8.86 | 14.99 | 2.00 | 77.3 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.74 | 7.75 | 13.26 | 0.00 | 68.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.46 | 18.42 | 29.33 | 10.00 | 90.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.61 | 18.15 | 27.80 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.58 | 16.45 | 26.57 | 1.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.32 | 21.06 | 34.87 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.4 | 5.77 | 16.73 | 26.72 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.06 | 14.40 | 23.38 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.54 | 23.17 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.33 | 22.19 | 0.00 | 0.0 | 0.0 |
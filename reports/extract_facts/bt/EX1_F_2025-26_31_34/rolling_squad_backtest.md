# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 289.44
- Total actual points: 254.00
- Average predicted points: 72.36
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
- Predicted score: 64.70
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.77 | 18.24 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.05 | 0.26 | 0.00 | 3.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.55 | 16.29 | 25.68 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.69 | 24.88 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.58 | 14.29 | 21.84 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.92 | 11.13 | 17.99 | -1.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.66 | 10.35 | 16.04 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.56 | 18.81 | 30.17 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.81 | 16.09 | 25.54 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.42 | 15.35 | 25.02 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.52 | 22.24 | 35.88 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.69 | 17.23 | 28.11 | 2.00 | 86.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.96 | 15.64 | 24.05 | 10.00 | 90.0 | 88.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.15 | 15.53 | 24.33 | 3.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.21 | 12.41 | 19.45 | 2.00 | 90.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 69.92
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.15) beats the best remaining Bench Boost opportunity (18.98).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.88, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.15) beats the best remaining Bench Boost opportunity (18.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.97 | 8.88 | 15.23 | 1.00 | 60.3 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.31 | 0.42 | 0.56 | 0.00 | 3.8 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.49 | 11.92 | 18.06 | 5.00 | 87.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.02 | 11.79 | 20.29 | 4.00 | 62.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.89 | 11.49 | 18.97 | 9.00 | 79.0 | 90.0 |
| Bench 2 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.64 | 11.10 | 17.57 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.57 | 9.68 | 15.25 | 8.00 | 85.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.83 | 15.23 | 25.41 | 2.00 | 78.6 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.16 | 14.13 | 22.94 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.71 | 13.56 | 21.83 | 13.00 | 85.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.41 | 21.90 | 35.50 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.19 | 15.78 | 26.03 | 4.00 | 87.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.44 | 13.23 | 21.33 | 5.00 | 82.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.27 | 11.89 | 18.82 | 6.00 | 88.8 | 90.0 |
| Bench 3 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.63 | 10.87 | 17.40 | 3.00 | 68.6 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 104.85
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.81) beats the best remaining Triple Captain opportunity (6.70).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marcos Senesi Barón (projected gain 1.34, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.81) beats the best remaining Triple Captain opportunity (6.70).
- Autosub: Jarrod Bowen replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.98 | 9.44 | 15.95 | 1.00 | 76.5 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.13 | 0.19 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.82 | 14.52 | 21.86 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.39 | 12.98 | 21.41 | 8.00 | 89.7 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.25 | 12.89 | 19.08 | 12.00 | 158.7 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.65 | 11.93 | 18.41 | 5.00 | 169.5 | 180.0 |
| Bench 4 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.80 | 8.01 | 13.87 | 1.00 | 73.5 | 62.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.55 | 17.37 | 27.57 | 0.00 | 172.9 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.84 | 13.99 | 22.85 | 2.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Jarrod Bowen | FWD | 19 | 7.5 | 4.33 | 13.25 | 21.83 | 2.00 | 86.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.68 | 19.24 | 32.05 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.21 | 18.89 | 29.58 | 2.00 | 180.0 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 8.55 | 13.27 | 20.40 | 16.00 | 175.1 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.51 | 13.27 | 21.41 | 5.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.12 | 10.20 | 17.19 | 0.00 | 62.6 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 2.60 -> 2.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 49.96
- Actual score: 49.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 9.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.35 | 12.13 | 19.24 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.32 | 0.48 | 0.00 | 4.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.07 | 17.14 | 26.88 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.84 | 22.84 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.51 | 22.01 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.95 | 19.96 | 0.00 | 0.0 | 0.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.1 | 2.73 | 7.72 | 13.18 | 0.00 | 68.0 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.16 | 17.18 | 27.07 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.49 | 16.11 | 25.85 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 6.92 | 14.88 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 20.85 | 34.51 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.62 | 16.18 | 25.70 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.01 | 14.03 | 22.65 | 1.00 | 89.4 | 90.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 0.00 | 13.49 | 22.49 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 12.05 | 21.46 | 0.00 | 0.0 | 0.0 |
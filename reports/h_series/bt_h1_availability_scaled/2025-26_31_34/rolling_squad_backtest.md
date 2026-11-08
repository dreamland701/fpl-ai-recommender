# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 257.19
- Total actual points: 197.00
- Average predicted points: 64.30
- Average actual points: 49.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 46.52
- Actual score: 43.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.91 | 8.17 | 13.35 | 2.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 3.3 | 0.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 20.50 | 34.77 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.59 | 16.32 | 25.73 | 3.00 | 90.5 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.29 | 13.70 | 20.80 | 0.00 | 89.1 | 36.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.31 | 9.55 | 15.27 | 1.00 | 81.1 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 3.9 | 3.48 | 9.38 | 15.12 | 6.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.6 | 0.00 | 25.63 | 43.42 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.20 | 18.01 | 28.88 | 2.00 | 88.9 | 77.0 |
| XI | Bench | Marc Guiu Paz | FWD | 7 | 4.1 | 0.17 | 0.54 | 1.07 | 0.00 | 4.8 | 0.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 0.00 | 22.49 | 37.77 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.21 | 21.61 | 34.79 | 13.00 | 89.5 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.4 | 0.00 | 18.41 | 31.65 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Rodrigo 'Rodri' Hernandez Cascante | MID | 13 | 6.3 | 0.00 | 15.73 | 26.10 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.15 | 15.50 | 24.29 | 3.00 | 90.4 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 63.94
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.43) beats the best remaining Bench Boost opportunity (13.73).
- Transfer: Rodrigo 'Rodri' Hernandez Cascante -> Dango Ouattara (projected gain 3.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.43) beats the best remaining Bench Boost opportunity (13.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.02 | 8.26 | 13.39 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.42 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.37 | 12.81 | 22.12 | 4.00 | 63.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.06 | 12.03 | 19.97 | 9.00 | 79.2 | 90.0 |
| Bench 2 | Bench Boost | Joe Rodon | DEF | 11 | 3.9 | 3.05 | 9.01 | 14.40 | 0.00 | 82.9 | 0.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.39 | 8.91 | 14.59 | 6.00 | 79.2 | 90.0 |
| Bench 3 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 1.97 | 6.47 | 10.99 | 2.00 | 46.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.4 | 6.23 | 18.63 | 31.61 | 2.00 | 58.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.09 | 16.07 | 26.94 | 2.00 | 77.7 | 81.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.0 | 0.12 | 0.57 | 0.96 | 0.00 | 5.8 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.00 | 21.09 | 34.08 | 4.00 | 90.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 5.49 | 16.47 | 28.15 | 2.00 | 58.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.63 | 13.82 | 22.33 | 5.00 | 82.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.36 | 13.02 | 23.24 | 4.00 | 52.8 | 90.0 |
| XI | XI | Dango Ouattara | MID | 5 | 6.0 | 3.87 | 12.47 | 21.53 | 2.00 | 56.7 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 107.24
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.35) beats the best remaining Triple Captain opportunity (6.54).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Malick Thiaw -> Marcos Senesi Barón (projected gain 7.97, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.35) beats the best remaining Triple Captain opportunity (6.54).
- Autosub: Joe Rodon replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 5.21 | 8.84 | 14.05 | 4.00 | 169.1 | 180.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.14 | 0.20 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.74 | 14.35 | 21.61 | 6.00 | 180.9 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.19 | 12.88 | 22.47 | 0.00 | 71.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.33 | 12.85 | 21.28 | 8.00 | 89.3 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.0 | 2.89 | 8.50 | 14.11 | 5.00 | 79.3 | 90.0 |
| Bench 2 | Autosub In | Joe Rodon | DEF | 11 | 3.9 | 3.67 | 6.63 | 10.70 | 1.00 | 89.8 | 46.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 14.40 | 21.56 | 33.81 | 13.00 | 178.6 | 180.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.77 | 17.70 | 28.15 | 0.00 | 174.4 | 0.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.0 | 0.28 | 1.80 | 2.33 | 1.00 | 12.6 | 18.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.55 | 18.87 | 31.54 | 6.00 | 89.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 10.87 | 17.52 | 28.18 | 5.00 | 157.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.60 | 13.57 | 21.94 | 5.00 | 82.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 3.81 | 12.32 | 21.64 | 2.00 | 74.1 | 90.0 |
| XI | XI | Dango Ouattara | MID | 5 | 5.9 | 3.99 | 11.95 | 19.83 | 3.00 | 71.3 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 39.49
- Actual score: 27.00
- Transfer: Dango Ouattara -> Alex Scott (projected gain 7.64, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 0.00 | 10.13 | 16.77 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.34 | 0.50 | 0.00 | 4.9 | 0.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 18.92 | 30.96 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.10 | 17.17 | 26.93 | 4.00 | 89.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.64 | 15.25 | 24.57 | 8.00 | 90.8 | 90.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.37 | 9.41 | 15.11 | 2.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 3.9 | 0.00 | 5.99 | 11.05 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.5 | 0.00 | 30.49 | 49.54 | 0.00 | 0.0 | 0.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.38 | 18.95 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Marc Guiu Paz | FWD | 7 | 4.0 | 0.00 | 0.94 | 2.19 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 0.00 | 22.71 | 37.59 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.26 | 20.79 | 34.44 | 5.00 | 90.2 | 90.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 19.07 | 30.87 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.99 | 13.97 | 22.56 | 1.00 | 89.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.70 | 13.41 | 22.13 | 2.00 | 87.4 | 90.0 |
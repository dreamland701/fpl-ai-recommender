# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 265.64
- Total actual points: 197.00
- Average predicted points: 66.41
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
- Predicted score: 46.58
- Actual score: 43.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.98 | 8.35 | 13.64 | 2.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.08 | 0.29 | 0.00 | 3.3 | 0.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 20.50 | 34.77 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.59 | 16.33 | 25.75 | 3.00 | 91.1 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.31 | 13.76 | 20.89 | 0.00 | 87.9 | 36.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.38 | 9.75 | 15.59 | 1.00 | 82.0 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 3.9 | 3.51 | 9.45 | 15.23 | 6.00 | 83.1 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.6 | 0.00 | 25.63 | 43.42 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.20 | 18.00 | 28.86 | 2.00 | 87.7 | 77.0 |
| XI | Bench | Marc Guiu Paz | FWD | 7 | 4.1 | 0.17 | 0.54 | 1.07 | 0.00 | 4.8 | 0.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 0.00 | 22.49 | 37.77 | 0.00 | 1.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.16 | 21.46 | 34.56 | 13.00 | 87.0 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.4 | 0.00 | 18.41 | 31.65 | 0.00 | 2.4 | 0.0 |
| Bench 3 | Bench | Rodrigo 'Rodri' Hernandez Cascante | MID | 13 | 6.3 | 0.00 | 15.73 | 26.10 | 0.00 | 0.1 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.13 | 15.45 | 24.21 | 3.00 | 88.4 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.82
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.41) beats the best remaining Bench Boost opportunity (13.94).
- Transfer: Rodrigo 'Rodri' Hernandez Cascante -> Harry Wilson (projected gain 3.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.41) beats the best remaining Bench Boost opportunity (13.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.99 | 8.19 | 13.28 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.30 | 0.42 | 0.55 | 0.00 | 3.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.08 | 14.90 | 25.72 | 4.00 | 64.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.20 | 12.42 | 20.62 | 9.00 | 80.0 | 90.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.57 | 9.38 | 15.35 | 6.00 | 80.6 | 90.0 |
| Bench 2 | Bench Boost | Joe Rodon | DEF | 11 | 3.9 | 3.02 | 8.92 | 14.26 | 0.00 | 80.5 | 0.0 |
| Bench 3 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 1.97 | 6.47 | 10.99 | 2.00 | 46.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.17 | 21.47 | 36.43 | 2.00 | 60.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.15 | 16.25 | 27.24 | 2.00 | 77.8 | 81.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.0 | 0.12 | 0.57 | 0.96 | 0.00 | 5.8 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.84 | 20.59 | 33.29 | 4.00 | 85.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.02 | 18.06 | 30.87 | 2.00 | 60.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.70 | 14.05 | 22.70 | 5.00 | 83.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.36 | 13.02 | 23.24 | 4.00 | 53.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.1 | 4.16 | 12.82 | 21.67 | 2.00 | 63.7 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 108.22
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.40) beats the best remaining Triple Captain opportunity (6.48).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Malick Thiaw -> Marcos Senesi Barón (projected gain 7.88, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.40) beats the best remaining Triple Captain opportunity (6.48).
- Autosub: Joe Rodon replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 5.27 | 8.94 | 14.21 | 4.00 | 169.3 | 180.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.14 | 0.20 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.69 | 14.28 | 21.50 | 6.00 | 178.0 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.29 | 13.19 | 23.01 | 0.00 | 71.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.35 | 12.93 | 21.42 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | El Hadji Malick Diouf | DEF | 19 | 4.0 | 2.89 | 8.50 | 14.11 | 5.00 | 79.3 | 90.0 |
| Bench 2 | Autosub In | Joe Rodon | DEF | 11 | 3.9 | 3.67 | 6.63 | 10.70 | 1.00 | 89.8 | 46.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 14.45 | 21.65 | 33.95 | 13.00 | 179.8 | 180.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.82 | 17.78 | 28.28 | 0.00 | 175.7 | 0.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.0 | 0.28 | 1.80 | 2.33 | 1.00 | 12.6 | 18.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.50 | 18.72 | 31.29 | 6.00 | 86.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 11.24 | 18.11 | 29.13 | 5.00 | 157.3 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.78 | 14.10 | 22.81 | 5.00 | 85.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.17 | 12.45 | 20.43 | 3.00 | 71.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 3.76 | 12.15 | 21.33 | 2.00 | 72.1 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.10 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 44.03
- Actual score: 29.00
- Transfer: João Pedro Junqueira de Jesus -> Francisco Evanilson de Lima Barbosa (projected gain 20.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 0.00 | 10.13 | 16.77 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.34 | 0.50 | 0.00 | 4.9 | 0.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 18.92 | 30.96 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.12 | 17.22 | 27.01 | 4.00 | 90.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.49 | 14.83 | 23.90 | 8.00 | 85.2 | 90.0 |
| XI | XI | El Hadji Malick Diouf | DEF | 19 | 4.0 | 3.38 | 9.43 | 15.13 | 2.00 | 83.0 | 90.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 3.9 | 0.00 | 5.99 | 11.05 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.5 | 0.00 | 30.49 | 49.54 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 4 | 6.7 | 0.00 | 17.40 | 28.51 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Marc Guiu Paz | FWD | 7 | 4.0 | 0.00 | 0.94 | 2.19 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 0.00 | 22.71 | 37.59 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.19 | 20.60 | 34.12 | 5.00 | 86.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.99 | 13.98 | 22.57 | 1.00 | 90.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.72 | 13.50 | 22.26 | 2.00 | 88.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.77 | 12.82 | 20.11 | 2.00 | 85.3 | 90.0 |
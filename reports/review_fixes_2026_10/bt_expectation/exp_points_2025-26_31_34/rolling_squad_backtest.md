# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 255.07
- Total actual points: 241.00
- Average predicted points: 63.77
- Average actual points: 60.25
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
- Vice captain: Anthony Gordon
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 63.73
- Actual score: 62.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.16 | 9.85 | 17.15 | 0.00 | 75.0 | 0.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.33 | 9.06 | 14.09 | 7.00 | 88.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.31 | 15.32 | 20.99 | 3.00 | 113.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.47 | 13.18 | 19.67 | 0.00 | 111.0 | 36.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 2.89 | 12.81 | 19.42 | 0.00 | 79.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.28 | 11.44 | 18.64 | 1.00 | 95.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.69 | 10.37 | 16.46 | -1.00 | 85.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.87 | 16.75 | 24.72 | 2.00 | 99.2 | 77.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.1 | 3.20 | 9.36 | 13.98 | 12.00 | 69.2 | 82.0 |
| Bench 4 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 2.81 | 8.34 | 12.68 | 1.00 | 65.1 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.12 | 19.90 | 29.95 | 13.00 | 126.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.45 | 15.65 | 24.81 | 2.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.90 | 13.98 | 21.03 | 3.00 | 103.3 | 90.0 |
| Vice Captain | XI | Anthony Gordon | MID | 15 | 7.3 | 6.01 | 13.89 | 20.29 | 10.00 | 108.4 | 88.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 5.19 | 11.96 | 18.69 | 9.00 | 84.7 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 63.77
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.92) beats the best remaining Bench Boost opportunity (19.59).
- Transfer: Harry Wilson -> Pascal Groß (projected gain 3.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.92) beats the best remaining Bench Boost opportunity (19.59).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.23 | 9.13 | 13.58 | 0.00 | 87.3 | 90.0 |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 2.99 | 7.96 | 12.65 | 1.00 | 60.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.47 | 10.62 | 17.46 | 9.00 | 71.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.04 | 10.05 | 15.54 | 4.00 | 62.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.37 | 9.74 | 13.25 | 3.00 | 95.2 | 90.0 |
| Bench 3 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.03 | 9.28 | 14.97 | 4.00 | 81.9 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 1.84 | 6.01 | 9.59 | 2.00 | 39.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.53 | 12.92 | 20.29 | 2.00 | 77.2 | 81.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.1 | 4.44 | 10.95 | 17.24 | 2.00 | 77.4 | 74.0 |
| Bench 2 | Bench Boost | Valentín Castellanos | FWD | 19 | 5.5 | 3.06 | 7.76 | 11.50 | 11.00 | 55.1 | 81.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.54 | 18.74 | 29.08 | 4.00 | 106.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.84 | 13.94 | 23.63 | 4.00 | 83.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.09 | 11.78 | 19.82 | 5.00 | 77.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.34 | 11.21 | 16.95 | 6.00 | 89.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 3.41 | 10.31 | 15.34 | 3.00 | 60.9 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 70.27
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.91) beats the best remaining Triple Captain opportunity (5.89).
- Chip advisory: triple_captain (0.60): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: James Hill -> Jan Paul van Hecke (projected gain 0.92, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.91) beats the best remaining Triple Captain opportunity (5.89).
- Autosub: Malick Thiaw replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.70 | 9.29 | 15.39 | 1.00 | 74.9 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.97 | 8.01 | 13.28 | 1.00 | 84.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.89 | 13.20 | 18.63 | 6.00 | 126.8 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.24 | 11.11 | 18.13 | 0.00 | 65.7 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.6 | 5.23 | 11.10 | 15.69 | 12.00 | 109.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.04 | 10.84 | 16.78 | 8.00 | 84.1 | 90.0 |
| Bench 2 | Autosub In | Malick Thiaw | DEF | 15 | 5.1 | 3.14 | 8.78 | 13.56 | 1.00 | 72.7 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.13 | 14.13 | 22.60 | 0.00 | 118.3 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 5.46 | 10.33 | 14.46 | 8.00 | 90.2 | 81.0 |
| Bench 4 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 2.87 | 9.03 | 13.43 | 2.00 | 67.1 | 83.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.02 | 17.71 | 29.11 | 6.00 | 88.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.31 | 16.80 | 25.49 | 2.00 | 129.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.18 | 12.00 | 19.07 | 5.00 | 78.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 5.16 | 10.80 | 16.11 | 16.00 | 113.5 | 180.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.02 | 9.65 | 15.85 | 0.00 | 58.1 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.30
- Actual score: 46.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 4.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.63 | 11.60 | 18.83 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 3.33 | 9.45 | 14.88 | 1.00 | 92.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.26 | 16.21 | 22.50 | 4.00 | 126.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.55 | 14.08 | 21.51 | 8.00 | 105.5 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.6 | 2.89 | 11.90 | 17.96 | 0.00 | 98.4 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.88 | 11.75 | 17.13 | 0.00 | 101.1 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 2.78 | 8.40 | 14.07 | 2.00 | 78.0 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.7 | 6.53 | 16.50 | 25.97 | 10.00 | 123.0 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.2 | 2.20 | 10.31 | 17.26 | 0.00 | 53.2 | 0.0 |
| XI | XI | Valentín Castellanos | FWD | 19 | 5.5 | 3.25 | 8.98 | 14.02 | 1.00 | 70.4 | 78.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.39 | 19.33 | 29.81 | 5.00 | 123.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.98 | 12.93 | 20.72 | 1.00 | 92.3 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 10.5 | 2.75 | 12.58 | 22.33 | 0.00 | 61.8 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 2.76 | 11.94 | 20.85 | 0.00 | 97.4 | 0.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.10 | 4.85 | 8.89 | 0.00 | 28.8 | 0.0 |
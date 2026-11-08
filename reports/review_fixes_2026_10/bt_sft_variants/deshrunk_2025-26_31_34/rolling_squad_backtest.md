# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 271.98
- Total actual points: 227.00
- Average predicted points: 68.00
- Average actual points: 56.75
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 66.14
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Raúl Jiménez Rodríguez replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.72 | 10.94 | 18.89 | 0.00 | 75.0 | 0.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.81 | 9.69 | 14.82 | 3.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 6.05 | 15.46 | 24.74 | 3.00 | 113.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 6.01 | 14.15 | 21.02 | 0.00 | 111.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.48 | 13.36 | 20.74 | 1.00 | 95.6 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.69 | 12.92 | 22.77 | 0.00 | 79.3 | 0.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.89 | 11.46 | 18.52 | -1.00 | 85.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.48 | 17.48 | 28.46 | 2.00 | 99.2 | 77.0 |
| Bench 3 | Autosub In | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 3.63 | 9.99 | 15.71 | 5.00 | 61.5 | 8.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 3.14 | 8.44 | 13.12 | 5.00 | 60.2 | 17.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.64 | 21.42 | 34.95 | 13.00 | 126.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.84 | 17.37 | 28.35 | 2.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.12 | 15.13 | 23.39 | 3.00 | 103.3 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 4.22 | 14.65 | 25.40 | 0.00 | 73.6 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.96 | 12.93 | 21.20 | 9.00 | 84.7 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 56.76
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (15.72).
- Transfer: Raúl Jiménez Rodríguez -> Danny Welbeck (projected gain 2.67, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (15.72).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.68 | 8.16 | 13.73 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 1.92 | 6.42 | 10.90 | 2.00 | 70.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.49 | 11.62 | 18.58 | 9.00 | 71.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.59 | 10.32 | 18.14 | 4.00 | 62.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.99 | 10.04 | 16.46 | 4.00 | 81.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.36 | 9.58 | 15.23 | 3.00 | 95.2 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 1.68 | 6.27 | 10.63 | 2.00 | 39.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.19 | 13.25 | 22.88 | 2.00 | 77.2 | 81.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 4.33 | 12.05 | 18.86 | 2.00 | 77.4 | 74.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.23 | 7.23 | 11.44 | 6.00 | 49.6 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.39 | 19.75 | 32.37 | 4.00 | 106.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.74 | 15.21 | 25.53 | 4.00 | 83.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.05 | 13.57 | 21.62 | 5.00 | 77.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.17 | 13.50 | 22.31 | 2.00 | 56.2 | 90.0 |
| Bench 2 | Bench | Harry Wilson | MID | 10 | 6.0 | 2.91 | 9.47 | 15.32 | 2.00 | 53.2 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bruno Borges Fernandes
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 80.35
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.79) beats the best remaining Bench Boost opportunity (0.90).
- Transfer: James Hill -> Jan Paul van Hecke (projected gain 1.18, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.79) beats the best remaining Bench Boost opportunity (0.90).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.99 | 9.97 | 16.86 | 1.00 | 74.9 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.9 | 2.77 | 8.76 | 14.63 | 10.00 | 81.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 6.45 | 14.63 | 21.58 | 6.00 | 126.8 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.6 | 5.42 | 12.30 | 18.60 | 12.00 | 109.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.70 | 11.96 | 19.62 | 8.00 | 84.1 | 90.0 |
| Bench 2 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.51 | 11.89 | 20.31 | 0.00 | 65.7 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 3.11 | 9.46 | 15.43 | 1.00 | 72.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.04 | 17.10 | 27.31 | 0.00 | 118.3 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 5.34 | 11.46 | 17.15 | 8.00 | 90.2 | 81.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 4.84 | 10.04 | 15.84 | 10.00 | 93.3 | 137.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.67 | 20.04 | 32.58 | 6.00 | 88.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.84 | 19.24 | 29.93 | 2.00 | 129.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.36 | 15.82 | 25.66 | 5.00 | 109.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.22 | 13.62 | 21.61 | 5.00 | 78.7 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 3.26 | 10.34 | 17.08 | 3.00 | 64.3 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 68.74
- Actual score: 47.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 8.25, hit 0)
- Autosub: Malick Thiaw replaced Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.90 | 13.08 | 20.56 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 3.03 | 8.29 | 14.01 | 7.00 | 80.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 7.35 | 17.11 | 26.90 | 4.00 | 126.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.06 | 15.57 | 24.50 | 8.00 | 105.5 | 90.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.6 | 3.86 | 12.66 | 20.23 | 0.00 | 98.4 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.87 | 12.22 | 20.33 | 0.00 | 101.1 | 0.0 |
| Bench 3 | Autosub In | Malick Thiaw | DEF | 15 | 5.1 | 2.84 | 9.31 | 15.50 | 2.00 | 78.0 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.7 | 7.50 | 18.94 | 29.68 | 10.00 | 123.0 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.2 | 2.94 | 11.18 | 19.00 | 0.00 | 53.2 | 0.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.32 | 9.24 | 16.08 | 0.00 | 59.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 8.26 | 21.13 | 35.30 | 5.00 | 123.9 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 4.70 | 15.56 | 26.12 | 0.00 | 90.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.23 | 14.50 | 23.26 | 1.00 | 92.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 3.68 | 14.40 | 25.87 | 0.00 | 61.8 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 5.06 | 12.45 | 19.54 | 2.00 | 92.5 | 90.0 |
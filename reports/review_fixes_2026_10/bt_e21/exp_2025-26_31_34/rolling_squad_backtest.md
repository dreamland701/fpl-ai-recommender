# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 262.35
- Total actual points: 215.00
- Average predicted points: 65.59
- Average actual points: 53.75
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
- Predicted score: 63.31
- Actual score: 43.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 3.26 | 8.93 | 13.78 | 7.00 | 89.9 | 90.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.86 | 8.79 | 13.37 | 3.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.41 | 14.68 | 22.21 | 3.00 | 105.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.65 | 12.69 | 19.05 | 0.00 | 103.0 | 36.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 2.90 | 12.42 | 20.39 | 0.00 | 59.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.39 | 10.94 | 16.61 | 1.00 | 75.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.90 | 10.16 | 15.65 | -1.00 | 87.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.15 | 16.25 | 24.40 | 2.00 | 96.2 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.11 | 13.54 | 22.75 | 2.00 | 97.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.90 | 8.14 | 12.81 | 5.00 | 60.2 | 17.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.02 | 19.52 | 30.08 | 13.00 | 106.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.59 | 15.14 | 23.25 | 2.00 | 89.5 | 90.0 |
| Bench 2 | Bench | Antoine Semenyo | MID | 13 | 8.3 | 3.63 | 13.93 | 22.74 | 0.00 | 53.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.02 | 13.73 | 20.04 | 3.00 | 102.3 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.20 | 11.75 | 17.38 | 2.00 | 89.7 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 2.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 61.34
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.47) beats the best remaining Triple Captain opportunity (16.10).
- Transfer: Gabriel dos Santos Magalhães -> Jan Paul van Hecke (projected gain 0.97, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.47) beats the best remaining Triple Captain opportunity (16.10).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.10 | 9.04 | 13.62 | 0.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 1.92 | 6.47 | 10.97 | 2.00 | 70.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.51 | 10.65 | 16.50 | 9.00 | 77.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.49 | 10.60 | 15.43 | 3.00 | 93.2 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.58 | 10.60 | 15.07 | 5.00 | 90.6 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.19 | 9.37 | 14.00 | 4.00 | 84.9 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 1.63 | 6.24 | 10.63 | 2.00 | 39.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.58 | 13.06 | 20.05 | 2.00 | 57.2 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.00 | 12.37 | 19.76 | 14.00 | 68.7 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.35 | 7.57 | 12.20 | 6.00 | 49.6 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.47 | 18.84 | 28.89 | 4.00 | 105.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.67 | 13.42 | 20.83 | 4.00 | 63.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.21 | 12.36 | 19.35 | 5.00 | 81.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.43 | 12.08 | 19.92 | 2.00 | 44.2 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.34 | 10.78 | 17.50 | 6.00 | 89.1 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 2.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 80.91
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (21.01) beats the best remaining Bench Boost opportunity (0.65).
- Transfer: Junior Kroupi -> Igor Thiago Nascimento Rodrigues (projected gain 3.85, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (21.01) beats the best remaining Bench Boost opportunity (0.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 2.91 | 8.61 | 14.30 | 1.00 | 84.0 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.9 | 2.57 | 7.60 | 12.51 | 10.00 | 81.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 6.12 | 13.09 | 18.11 | 6.00 | 106.8 | 180.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.00 | 12.17 | 19.42 | 8.00 | 86.1 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 5.50 | 11.36 | 16.32 | 12.00 | 89.7 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 4.97 | 10.30 | 13.96 | 5.00 | 91.9 | 180.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 3.07 | 8.99 | 13.69 | 1.00 | 78.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.44 | 15.22 | 22.85 | 0.00 | 98.3 | 0.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.5 | 4.22 | 12.37 | 19.97 | 2.00 | 85.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.45 | 12.25 | 19.64 | 2.00 | 84.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.33 | 16.75 | 25.25 | 2.00 | 109.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.09 | 16.60 | 26.19 | 6.00 | 68.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.12 | 13.94 | 21.30 | 5.00 | 89.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.24 | 11.72 | 19.19 | 5.00 | 58.7 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 5.53 | 11.38 | 16.70 | 16.00 | 93.5 | 180.0 |

## GW34

- Train rows: 186843
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.79
- Actual score: 27.00
- Transfer: Malick Thiaw -> Marc Guéhi (projected gain 2.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.34 | 9.31 | 14.47 | 1.00 | 91.1 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.66 | 7.87 | 13.05 | 7.00 | 80.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.42 | 15.62 | 22.79 | 4.00 | 114.7 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 2.95 | 12.02 | 19.19 | 0.00 | 76.4 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 2.80 | 11.59 | 17.83 | 0.00 | 78.4 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.87 | 11.33 | 17.98 | 0.00 | 81.1 | 0.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 2.66 | 10.19 | 15.36 | 0.00 | 76.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.52 | 15.81 | 22.79 | 10.00 | 112.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.39 | 14.08 | 21.77 | 1.00 | 92.7 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 1.63 | 8.56 | 15.06 | 0.00 | 13.9 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.43 | 19.07 | 29.90 | 5.00 | 122.9 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 3.61 | 14.04 | 22.44 | 0.00 | 70.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.83 | 12.32 | 19.60 | 1.00 | 91.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 2.97 | 11.88 | 20.63 | 0.00 | 41.8 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 3.02 | 11.59 | 18.78 | 0.00 | 77.4 | 0.0 |
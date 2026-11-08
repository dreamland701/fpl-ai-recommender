# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 249.00
- Total actual points: 216.00
- Average predicted points: 62.25
- Average actual points: 54.00
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
- Predicted score: 60.52
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Raúl Jiménez Rodríguez replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.66 | 10.59 | 18.23 | 0.00 | 75.0 | 0.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.66 | 9.56 | 14.70 | 3.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.52 | 14.25 | 22.93 | 3.00 | 113.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.48 | 13.28 | 19.87 | 0.00 | 111.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.19 | 12.76 | 19.88 | 1.00 | 95.6 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.41 | 12.03 | 21.21 | 0.00 | 79.3 | 0.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.71 | 11.08 | 17.93 | -1.00 | 85.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.84 | 16.01 | 26.19 | 2.00 | 99.2 | 77.0 |
| Bench 2 | Autosub In | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 3.52 | 9.81 | 15.43 | 5.00 | 61.5 | 8.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 3.13 | 8.48 | 13.25 | 5.00 | 60.2 | 17.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.84 | 19.45 | 31.87 | 13.00 | 126.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.34 | 16.11 | 26.32 | 2.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.69 | 14.08 | 21.86 | 3.00 | 103.3 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 3.84 | 13.54 | 23.51 | 0.00 | 73.6 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.58 | 12.27 | 20.19 | 9.00 | 84.7 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 52.33
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.65) beats the best remaining Triple Captain opportunity (14.84).
- Transfer: Raúl Jiménez Rodríguez -> Danny Welbeck (projected gain 1.97, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.65) beats the best remaining Triple Captain opportunity (14.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.64 | 8.07 | 13.53 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.06 | 6.57 | 11.09 | 2.00 | 70.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.36 | 11.31 | 18.08 | 9.00 | 71.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.38 | 9.95 | 17.47 | 4.00 | 62.6 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.89 | 9.80 | 16.09 | 4.00 | 81.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.18 | 9.27 | 14.80 | 3.00 | 95.2 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 1.87 | 6.44 | 10.84 | 2.00 | 39.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 3.84 | 12.54 | 21.72 | 2.00 | 77.2 | 81.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 4.02 | 11.68 | 18.37 | 2.00 | 77.4 | 74.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.29 | 7.27 | 11.51 | 6.00 | 49.6 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.65 | 18.45 | 30.41 | 4.00 | 106.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.36 | 14.48 | 24.38 | 4.00 | 83.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.79 | 13.09 | 20.91 | 5.00 | 77.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.90 | 12.99 | 21.43 | 2.00 | 56.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 2.91 | 9.35 | 15.09 | 2.00 | 53.2 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.40 -> 1.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bruno Borges Fernandes
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 75.53
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.60) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bernd Leno -> Karl Darlow (projected gain 1.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.60) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Karl Darlow | GK | 11 | 3.9 | 4.59 | 10.97 | 16.55 | 8.00 | 118.6 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.08 | 9.82 | 16.47 | 1.00 | 74.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.76 | 13.39 | 20.04 | 6.00 | 126.8 | 180.0 |
| Bench 2 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.47 | 11.37 | 19.26 | 0.00 | 65.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.52 | 11.18 | 18.36 | 8.00 | 84.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 4.52 | 10.46 | 15.99 | 5.00 | 111.9 | 180.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 3.16 | 9.34 | 15.20 | 1.00 | 72.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.28 | 15.30 | 24.74 | 0.00 | 118.3 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 4.85 | 10.71 | 16.26 | 8.00 | 90.2 | 81.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 4.54 | 9.71 | 15.45 | 10.00 | 93.3 | 137.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.01 | 18.02 | 29.40 | 6.00 | 88.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 6.88 | 17.15 | 27.02 | 2.00 | 129.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 5.68 | 14.23 | 23.34 | 5.00 | 109.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.00 | 12.78 | 20.35 | 5.00 | 78.7 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 3.28 | 10.09 | 16.64 | 3.00 | 64.3 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 1.40 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.61
- Actual score: 47.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 7.01, hit 0)
- Autosub: Malick Thiaw replaced Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.47 | 12.43 | 19.66 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 2.62 | 10.23 | 16.52 | 0.00 | 98.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.44 | 15.55 | 24.73 | 4.00 | 126.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.33 | 14.37 | 22.76 | 8.00 | 105.5 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.53 | 11.39 | 19.09 | 0.00 | 101.1 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 3.22 | 9.82 | 16.92 | 0.00 | 96.0 | 0.0 |
| Bench 2 | Autosub In | Malick Thiaw | DEF | 15 | 5.1 | 2.88 | 9.31 | 15.41 | 2.00 | 78.0 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.7 | 6.56 | 17.40 | 27.53 | 10.00 | 123.0 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.2 | 2.86 | 10.86 | 18.42 | 0.00 | 53.2 | 0.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.41 | 9.26 | 15.95 | 0.00 | 59.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.11 | 18.96 | 31.95 | 5.00 | 123.9 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 4.14 | 14.23 | 24.06 | 0.00 | 90.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.72 | 13.62 | 21.97 | 1.00 | 92.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 3.41 | 13.61 | 24.48 | 0.00 | 61.8 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.59 | 11.77 | 18.64 | 2.00 | 92.5 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 220.08
- Total actual points: 216.00
- Average predicted points: 55.02
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
- Predicted score: 54.17
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Raúl Jiménez Rodríguez replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.13 | 9.14 | 15.78 | 0.00 | 75.0 | 0.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.13 | 8.12 | 12.26 | 3.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.99 | 12.81 | 20.49 | 3.00 | 113.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.96 | 11.84 | 17.42 | 0.00 | 111.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.66 | 11.31 | 17.43 | 1.00 | 95.6 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 2.88 | 10.58 | 18.76 | 0.00 | 79.3 | 0.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.18 | 9.64 | 15.49 | -1.00 | 85.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.31 | 14.57 | 23.75 | 2.00 | 99.2 | 77.0 |
| Bench 2 | Autosub In | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 2.99 | 8.36 | 12.99 | 5.00 | 61.5 | 8.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.60 | 7.04 | 10.81 | 5.00 | 60.2 | 17.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.31 | 18.01 | 29.43 | 13.00 | 126.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.81 | 14.67 | 23.87 | 2.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.16 | 12.64 | 19.42 | 3.00 | 103.3 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 3.31 | 12.10 | 21.06 | 0.00 | 73.6 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.05 | 10.83 | 17.75 | 9.00 | 84.7 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 46.66
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.21) beats the best remaining Triple Captain opportunity (13.85).
- Transfer: Raúl Jiménez Rodríguez -> Danny Welbeck (projected gain 1.97, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.21) beats the best remaining Triple Captain opportunity (13.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.21 | 6.77 | 11.32 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 1.62 | 5.27 | 8.87 | 2.00 | 70.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 2.93 | 10.02 | 15.87 | 9.00 | 71.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 2.94 | 8.65 | 15.26 | 4.00 | 62.6 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.45 | 8.50 | 13.87 | 4.00 | 81.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 2.74 | 7.97 | 12.59 | 3.00 | 95.2 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 1.43 | 5.14 | 8.63 | 2.00 | 39.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 3.40 | 11.24 | 19.51 | 2.00 | 77.2 | 81.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 3.58 | 10.39 | 16.16 | 2.00 | 77.4 | 74.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 1.85 | 5.97 | 9.30 | 6.00 | 49.6 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.21 | 17.16 | 28.20 | 4.00 | 106.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 3.92 | 13.18 | 22.17 | 4.00 | 83.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.36 | 11.80 | 18.69 | 5.00 | 77.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.46 | 11.69 | 19.22 | 2.00 | 56.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 2.48 | 8.06 | 12.88 | 2.00 | 53.2 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.40 -> 1.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bruno Borges Fernandes
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 66.72
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.40) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bernd Leno -> Karl Darlow (projected gain 1.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.40) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Karl Darlow | GK | 11 | 3.9 | 4.04 | 9.39 | 13.99 | 8.00 | 118.6 | 180.0 |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 2.53 | 8.24 | 13.91 | 1.00 | 74.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.21 | 11.82 | 17.47 | 6.00 | 126.8 | 180.0 |
| Bench 2 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 2.92 | 9.80 | 16.69 | 0.00 | 65.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 2.97 | 9.61 | 15.79 | 8.00 | 84.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.97 | 8.89 | 13.42 | 5.00 | 111.9 | 180.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 2.61 | 7.77 | 12.64 | 1.00 | 72.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.73 | 13.73 | 22.18 | 0.00 | 118.3 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 4.30 | 9.14 | 13.70 | 8.00 | 90.2 | 81.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 3.99 | 8.14 | 12.89 | 10.00 | 93.3 | 137.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.46 | 16.45 | 26.84 | 6.00 | 88.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 6.33 | 15.58 | 24.45 | 2.00 | 129.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 5.13 | 12.66 | 20.77 | 5.00 | 109.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.45 | 11.21 | 17.79 | 5.00 | 78.7 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 2.73 | 8.52 | 14.08 | 3.00 | 64.3 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 1.40 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 52.53
- Actual score: 47.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 6.59, hit 0)
- Autosub: Malick Thiaw replaced Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.80 | 10.79 | 17.01 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 1.94 | 8.59 | 13.86 | 0.00 | 98.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.77 | 13.92 | 22.08 | 4.00 | 126.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.65 | 12.74 | 20.10 | 8.00 | 105.5 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.85 | 9.76 | 16.43 | 0.00 | 101.1 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 2.54 | 8.18 | 14.26 | 0.00 | 96.0 | 0.0 |
| Bench 2 | Autosub In | Malick Thiaw | DEF | 15 | 5.1 | 2.21 | 7.68 | 12.76 | 2.00 | 78.0 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.7 | 5.89 | 15.77 | 24.88 | 10.00 | 123.0 | 90.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.2 | 2.19 | 9.22 | 15.77 | 0.00 | 53.2 | 0.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.73 | 7.62 | 13.30 | 0.00 | 59.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.43 | 17.33 | 29.30 | 5.00 | 123.9 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 3.47 | 12.60 | 21.41 | 0.00 | 90.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.04 | 11.98 | 19.32 | 1.00 | 92.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 2.74 | 11.97 | 21.82 | 0.00 | 61.8 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 3.91 | 10.13 | 15.99 | 2.00 | 92.5 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 258.39
- Total actual points: 241.00
- Average predicted points: 64.60
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Anthony Gordon
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 66.35
- Actual score: 61.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.16 | 9.85 | 17.15 | 0.00 | 55.0 | 0.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.93 | 9.02 | 13.53 | 3.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.31 | 15.32 | 20.99 | 3.00 | 105.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.47 | 13.18 | 19.67 | 0.00 | 103.0 | 36.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 2.89 | 12.81 | 19.42 | 0.00 | 59.3 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.28 | 11.44 | 18.64 | 1.00 | 93.6 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.80 | 10.45 | 16.59 | -1.00 | 87.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.00 | 16.83 | 24.62 | 2.00 | 96.2 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.05 | 13.86 | 23.11 | 2.00 | 95.1 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.87 | 7.95 | 11.72 | 5.00 | 70.2 | 17.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.22 | 19.79 | 29.97 | 13.00 | 116.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.89 | 16.20 | 25.17 | 2.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.90 | 13.98 | 21.03 | 3.00 | 102.3 | 90.0 |
| Vice Captain | XI | Anthony Gordon | MID | 15 | 7.3 | 6.01 | 13.89 | 20.29 | 10.00 | 98.4 | 88.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 5.09 | 11.92 | 18.44 | 9.00 | 86.7 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 59.85
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.57) beats the best remaining Triple Captain opportunity (15.23).
- Transfer: Harry Wilson -> Elliot Anderson (projected gain 2.45, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.57) beats the best remaining Triple Captain opportunity (15.23).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.99 | 7.96 | 12.65 | 1.00 | 50.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 1.92 | 6.11 | 9.44 | 2.00 | 77.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.47 | 10.62 | 17.46 | 9.00 | 77.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.04 | 10.05 | 15.54 | 4.00 | 48.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.37 | 9.74 | 13.25 | 3.00 | 93.2 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.03 | 9.28 | 14.97 | 4.00 | 84.9 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 1.84 | 6.01 | 9.59 | 2.00 | 25.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.58 | 12.89 | 20.29 | 2.00 | 57.2 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.24 | 12.78 | 20.35 | 14.00 | 89.7 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.34 | 6.90 | 10.28 | 6.00 | 32.6 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.57 | 18.42 | 28.84 | 4.00 | 96.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.84 | 13.94 | 23.63 | 4.00 | 85.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.09 | 11.78 | 19.82 | 5.00 | 81.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.17 | 11.69 | 17.98 | 4.00 | 84.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 3.33 | 10.19 | 15.39 | 3.00 | 70.9 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 74.00
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.31) beats the best remaining Bench Boost opportunity (0.82).
- Transfer: James Hill -> Jan Paul van Hecke (projected gain 0.92, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.31) beats the best remaining Bench Boost opportunity (0.82).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 2.70 | 9.29 | 15.39 | 1.00 | 79.9 | 90.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 2.71 | 7.58 | 12.39 | 10.00 | 84.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.89 | 13.20 | 18.63 | 6.00 | 146.8 | 180.0 |
| Bench 2 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.24 | 11.11 | 18.13 | 0.00 | 74.7 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.6 | 5.23 | 11.10 | 15.69 | 12.00 | 129.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.04 | 10.84 | 16.78 | 8.00 | 86.1 | 90.0 |
| Bench 3 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 3.14 | 8.78 | 13.56 | 1.00 | 78.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.13 | 14.13 | 22.60 | 0.00 | 98.3 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.25 | 12.61 | 19.69 | 2.00 | 85.4 | 90.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 4.39 | 9.13 | 13.37 | 10.00 | 113.3 | 137.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.02 | 17.71 | 29.11 | 6.00 | 89.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.46 | 16.93 | 25.53 | 2.00 | 128.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.18 | 12.00 | 19.07 | 5.00 | 82.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.17 | 10.91 | 16.94 | 2.00 | 79.6 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 2.98 | 9.64 | 15.67 | 0.00 | 69.1 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.19
- Actual score: 52.00
- Transfer: Malick Thiaw -> Marc Guéhi (projected gain 3.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.65 | 11.65 | 18.74 | 10.00 | 97.3 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.86 | 7.76 | 12.07 | 7.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.26 | 16.21 | 22.50 | 4.00 | 116.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.55 | 14.08 | 21.51 | 8.00 | 100.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 2.79 | 11.97 | 16.58 | 0.00 | 76.4 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.6 | 2.89 | 11.90 | 17.96 | 0.00 | 78.4 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.88 | 11.75 | 17.13 | 0.00 | 81.1 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.53 | 16.55 | 26.21 | 10.00 | 122.0 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 1.63 | 9.03 | 13.88 | 0.00 | 16.9 | 0.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.75 | 8.38 | 14.85 | 0.00 | 39.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.40 | 19.20 | 29.75 | 5.00 | 122.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.98 | 12.93 | 20.72 | 1.00 | 91.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 2.75 | 12.58 | 22.33 | 0.00 | 41.8 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.11 | 11.47 | 17.63 | 9.00 | 85.3 | 90.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.05 | 4.82 | 8.82 | 0.00 | 18.8 | 0.0 |
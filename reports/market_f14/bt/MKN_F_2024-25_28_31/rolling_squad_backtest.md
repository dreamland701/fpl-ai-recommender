# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.77
- Total actual points: 177.00
- Average predicted points: 60.69
- Average actual points: 44.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW27 are included before the first simulated week.
- League-average scores were not available for this run.

## GW28

- Train rows: 152512
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 73.93
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.94 | 11.06 | 17.77 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.12 | 0.51 | 0.95 | 0.00 | 6.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.75 | 17.05 | 27.41 | 2.00 | 106.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.23 | 12.12 | 19.45 | 2.00 | 89.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.48 | 11.50 | 18.15 | 6.00 | 85.3 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.97 | 6.58 | 10.79 | 2.00 | 57.9 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.90 | 5.95 | 9.60 | 1.00 | 71.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.14 | 14.58 | 24.94 | 2.00 | 84.4 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.39 | 12.75 | 20.69 | 2.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.61 | 5.95 | 9.85 | 0.00 | 52.3 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.92 | 28.58 | 46.16 | 15.00 | 127.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 7.21 | 18.73 | 30.01 | 1.00 | 96.9 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.21 | 16.62 | 27.22 | 2.00 | 83.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 7.06 | 15.76 | 24.47 | 1.00 | 108.9 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.66 | 13.95 | 22.71 | 5.00 | 87.8 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Justin Kluivert
- Vice captain: Chris Wood
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 52.07
- Actual score: 39.00
- Transfer: Dominik Szoboszlai -> Antoine Semenyo (projected gain 5.14, hit 0)
- Autosub: Paul Onuachu replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.96 | 10.78 | 17.41 | 6.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.18 | 0.61 | 1.14 | 0.00 | 10.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.50 | 12.34 | 19.76 | 5.00 | 95.4 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 2.10 | 11.49 | 20.69 | 0.00 | 42.6 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.78 | 7.01 | 12.67 | 0.00 | 29.0 | 0.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.96 | 6.39 | 10.63 | 0.00 | 59.6 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.15 | 6.15 | 9.85 | 0.00 | 75.2 | 45.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.2 | 6.04 | 18.11 | 28.88 | 2.00 | 99.1 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.24 | 11.24 | 18.79 | 8.00 | 69.3 | 90.0 |
| Bench 3 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 1.80 | 5.39 | 9.02 | 7.00 | 36.3 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 5.22 | 25.01 | 44.84 | 0.00 | 74.3 | 0.0 |
| Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 6.12 | 16.79 | 26.22 | 2.00 | 109.4 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.63 | 15.81 | 26.25 | 6.00 | 89.9 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 3.64 | 14.21 | 25.19 | 0.00 | 55.8 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 4.34 | 11.45 | 17.95 | 1.00 | 90.3 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.92
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.02) beats the best remaining Bench Boost opportunity (5.99).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 9.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.02) beats the best remaining Bench Boost opportunity (5.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.98 | 13.14 | 20.51 | 2.00 | 107.6 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.17 | 0.82 | 1.51 | 0.00 | 12.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.73 | 12.89 | 20.53 | 1.00 | 95.8 | 15.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.50 | 9.21 | 14.83 | 2.00 | 59.0 | 75.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 12 | 7.3 | 1.34 | 5.93 | 12.32 | 0.00 | 16.2 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 1.48 | 4.95 | 8.20 | 0.00 | 59.0 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.07 | 4.12 | 7.28 | 1.00 | 35.7 | 45.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.4 | 6.19 | 16.00 | 24.74 | 9.00 | 98.3 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 2.54 | 9.56 | 16.80 | 5.00 | 59.1 | 90.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.44 | 6.92 | 11.47 | 7.00 | 52.0 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.24 | 22.43 | 38.14 | 3.00 | 80.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.87 | 13.67 | 22.21 | 0.00 | 71.6 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 3.27 | 12.34 | 21.66 | 8.00 | 65.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.34 | 10.82 | 19.27 | 6.00 | 28.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 4.52 | 10.71 | 16.67 | 2.00 | 84.6 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: William Saliba
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 57.85
- Actual score: 33.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.50) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.55, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.50) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.00 | 11.57 | 18.15 | 2.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.22 | 0.69 | 1.29 | 0.00 | 8.3 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.4 | 4.80 | 13.31 | 21.01 | 2.00 | 100.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.01 | 9.38 | 14.64 | 8.00 | 61.4 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.3 | 1.56 | 6.08 | 11.95 | 0.00 | 21.3 | 0.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.55 | 4.94 | 8.30 | 0.00 | 47.5 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.42 | 3.70 | 6.39 | 0.00 | 42.6 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.4 | 4.01 | 12.66 | 19.30 | 2.00 | 59.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.21 | 10.64 | 17.90 | 2.00 | 71.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.59 | 8.01 | 13.13 | 1.00 | 60.6 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.50 | 23.59 | 39.29 | 2.00 | 97.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.57 | 14.47 | 24.24 | 3.00 | 87.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.10 | 14.19 | 24.88 | 1.00 | 58.4 | 31.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.50 | 9.51 | 15.14 | 6.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.15 | 5.67 | 10.90 | 0.00 | 11.7 | 0.0 |
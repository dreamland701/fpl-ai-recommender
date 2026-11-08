# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 253.80
- Total actual points: 182.00
- Average predicted points: 63.45
- Average actual points: 45.50
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
- Predicted score: 73.47
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.76 | 10.93 | 17.71 | 3.00 | 90.9 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.38 | 1.11 | 1.86 | 0.00 | 11.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.30 | 16.51 | 26.67 | 2.00 | 96.8 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.18 | 12.14 | 19.56 | 2.00 | 92.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.64 | 11.75 | 18.50 | 6.00 | 88.5 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.38 | 6.99 | 11.18 | 2.00 | 62.8 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.19 | 9.90 | 1.00 | 75.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.90 | 15.20 | 25.39 | 2.00 | 91.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.92 | 13.28 | 21.22 | 2.00 | 86.0 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.69 | 6.02 | 9.98 | 0.00 | 55.4 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.70 | 29.14 | 47.61 | 15.00 | 128.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.84 | 18.64 | 30.25 | 1.00 | 92.7 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.11 | 17.58 | 28.28 | 2.00 | 91.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.79 | 14.80 | 23.71 | 1.00 | 92.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.64 | 13.88 | 22.60 | 5.00 | 86.4 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 62.41
- Actual score: 40.00
- Transfer: Daniel Muñoz -> Rayan Aït-Nouri (projected gain 2.77, hit 0)
- Autosub: Jacob Greaves replaced Trent Alexander-Arnold.
- Autosub: Paul Onuachu replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.65 | 10.54 | 17.24 | 6.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.32 | 1.10 | 1.91 | 0.00 | 12.3 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 3.95 | 13.43 | 22.94 | 0.00 | 69.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.42 | 12.34 | 19.87 | 5.00 | 97.6 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 4.55 | 11.40 | 17.31 | 2.00 | 94.1 | 79.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.18 | 6.62 | 10.89 | 0.00 | 65.0 | 0.0 |
| Bench 3 | Autosub In | Jacob Greaves | DEF | 10 | 3.9 | 2.05 | 5.99 | 9.60 | 0.00 | 76.0 | 45.0 |
| Vice Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.70 | 18.61 | 29.32 | 2.00 | 106.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.13 | 11.96 | 19.34 | 8.00 | 76.2 | 90.0 |
| Bench 4 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 1.57 | 5.12 | 8.64 | 7.00 | 33.9 | 45.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 8.14 | 26.61 | 45.12 | 0.00 | 101.3 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.84 | 16.84 | 27.17 | 6.00 | 100.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.88 | 16.34 | 25.63 | 2.00 | 104.9 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.49 | 14.96 | 25.77 | 0.00 | 65.9 | 0.0 |
| XI | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 2.52 | 9.36 | 16.72 | 0.00 | 46.4 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.20 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 56.02
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.04) beats the best remaining Bench Boost opportunity (5.94).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.04) beats the best remaining Bench Boost opportunity (5.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.50 | 12.55 | 19.85 | 2.00 | 105.6 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.22 | 1.20 | 2.14 | 0.00 | 13.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.32 | 12.46 | 20.13 | 1.00 | 95.2 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 11.22 | 17.88 | 6.00 | 82.6 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 2.13 | 6.85 | 11.35 | 8.00 | 57.3 | 81.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.76 | 5.31 | 8.64 | 0.00 | 62.6 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.28 | 4.51 | 7.83 | 1.00 | 40.8 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.56 | 10.58 | 17.77 | 5.00 | 70.2 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 1.78 | 7.37 | 13.59 | 0.00 | 23.9 | 0.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.32 | 6.69 | 11.10 | 7.00 | 50.3 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.59 | 23.38 | 39.74 | 3.00 | 88.7 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.67 | 13.60 | 22.30 | 0.00 | 72.0 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.45 | 13.53 | 22.82 | 8.00 | 78.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.18 | 10.71 | 19.29 | 6.00 | 25.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.61 | 8.31 | 14.73 | 3.00 | 47.6 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.89
- Actual score: 33.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Justin Kluivert -> Luis Díaz (projected gain 8.33, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.46) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.90 | 11.51 | 18.23 | 2.00 | 93.4 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.52 | 1.35 | 2.25 | 0.00 | 13.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.16 | 12.16 | 19.07 | 9.00 | 91.5 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.25 | 8.98 | 14.76 | 2.00 | 74.9 | 87.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.84 | 5.36 | 8.82 | 0.00 | 50.8 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 0.57 | 4.44 | 9.04 | 0.00 | 18.4 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.30 | 3.76 | 6.57 | 0.00 | 44.2 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.47 | 11.05 | 18.42 | 2.00 | 73.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.24 | 6.76 | 11.06 | 1.00 | 50.3 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.48 | 5.96 | 12.24 | 0.00 | 18.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.46 | 24.82 | 40.87 | 2.00 | 109.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.85 | 15.46 | 26.63 | 1.00 | 69.6 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.00 | 15.04 | 24.92 | 3.00 | 91.1 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.49 | 13.43 | 22.41 | 6.00 | 74.7 | 35.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.32 | 10.37 | 17.33 | 1.00 | 72.0 | 54.0 |
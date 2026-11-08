# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 252.52
- Total actual points: 166.00
- Average predicted points: 63.13
- Average actual points: 41.50
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
- Predicted score: 73.28
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.89 | 17.64 | 3.00 | 90.6 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.16 | 0.58 | 1.06 | 0.00 | 6.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.33 | 16.56 | 26.74 | 2.00 | 97.3 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.11 | 19.51 | 2.00 | 91.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.60 | 11.65 | 18.34 | 6.00 | 87.7 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.33 | 6.86 | 10.98 | 2.00 | 61.7 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.07 | 6.15 | 9.83 | 1.00 | 75.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.94 | 15.29 | 25.53 | 2.00 | 91.8 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.88 | 13.19 | 21.10 | 2.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.65 | 5.91 | 9.82 | 0.00 | 54.5 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.66 | 29.04 | 47.45 | 15.00 | 127.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.86 | 18.69 | 30.32 | 1.00 | 93.1 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.08 | 17.53 | 28.20 | 2.00 | 90.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.70 | 14.58 | 23.38 | 1.00 | 90.1 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.66 | 13.93 | 22.67 | 5.00 | 86.8 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 62.71
- Actual score: 40.00
- Transfer: Daniel Muñoz -> Rayan Aït-Nouri (projected gain 5.99, hit 0)
- Autosub: Jacob Greaves replaced Trent Alexander-Arnold.
- Autosub: Paul Onuachu replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.65 | 10.54 | 17.22 | 6.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.10 | 0.56 | 1.12 | 0.00 | 7.7 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.01 | 13.55 | 23.12 | 0.00 | 70.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.43 | 12.36 | 19.91 | 5.00 | 97.8 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 4.64 | 11.60 | 17.62 | 2.00 | 95.9 | 79.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.18 | 6.62 | 10.89 | 0.00 | 65.0 | 0.0 |
| Bench 3 | Autosub In | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.98 | 9.59 | 0.00 | 75.9 | 45.0 |
| Vice Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.85 | 19.00 | 29.90 | 2.00 | 109.3 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.11 | 11.93 | 19.32 | 8.00 | 75.9 | 90.0 |
| Bench 4 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 1.55 | 5.06 | 8.54 | 7.00 | 33.4 | 45.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 8.15 | 26.62 | 45.14 | 0.00 | 101.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.92 | 17.03 | 27.47 | 6.00 | 101.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 6.03 | 16.73 | 26.20 | 2.00 | 108.2 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.37 | 14.67 | 25.34 | 0.00 | 63.3 | 0.0 |
| XI | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 2.41 | 9.09 | 16.33 | 0.00 | 44.1 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.20 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 55.17
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.97) beats the best remaining Bench Boost opportunity (5.82).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 13.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.97) beats the best remaining Bench Boost opportunity (5.82).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.58 | 12.73 | 20.11 | 2.00 | 107.1 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.02 | 0.70 | 1.39 | 0.00 | 9.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.51 | 20.20 | 1.00 | 95.6 | 15.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.81 | 11.13 | 18.12 | 2.00 | 88.2 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 2.05 | 6.65 | 11.06 | 8.00 | 55.6 | 81.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.73 | 5.23 | 8.53 | 0.00 | 61.9 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.13 | 4.16 | 7.30 | 1.00 | 37.7 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.45 | 10.30 | 17.36 | 5.00 | 67.7 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 2.09 | 8.14 | 14.76 | 0.00 | 30.5 | 0.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.30 | 6.65 | 11.03 | 7.00 | 49.9 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.47 | 23.09 | 39.29 | 3.00 | 86.3 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.62 | 13.48 | 22.12 | 0.00 | 70.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.38 | 13.35 | 22.55 | 8.00 | 76.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.35 | 11.13 | 19.94 | 6.00 | 29.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.38 | 7.71 | 13.84 | 3.00 | 42.5 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.36
- Actual score: 21.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Aaron Cresswell -> Nikola Milenković (projected gain 13.86, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.94 | 11.60 | 18.36 | 2.00 | 94.2 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.30 | 0.80 | 1.44 | 0.00 | 8.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.84 | 13.42 | 21.26 | 2.00 | 105.9 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.0 | 3.86 | 11.21 | 17.84 | 1.00 | 96.1 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.23 | 8.94 | 14.70 | 2.00 | 74.5 | 87.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 0.86 | 5.16 | 10.13 | 0.00 | 24.6 | 0.0 |
| Bench 2 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.15 | 3.39 | 6.02 | 0.00 | 41.0 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.35 | 10.78 | 18.01 | 2.00 | 71.2 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.76 | 8.04 | 13.00 | 1.00 | 61.2 | 17.0 |
| XI | Bench | Chris Wood | FWD | 16 | 7.1 | 1.54 | 6.11 | 12.46 | 0.00 | 19.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 24.68 | 40.64 | 2.00 | 108.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.90 | 14.80 | 24.56 | 3.00 | 89.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.53 | 14.70 | 25.48 | 1.00 | 63.0 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.20 | 10.07 | 16.87 | 1.00 | 69.5 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 0.72 | 5.20 | 10.36 | 0.00 | 6.8 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 232.53
- Total actual points: 161.00
- Average predicted points: 58.13
- Average actual points: 40.25
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.60
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 3.44 | 9.22 | 14.63 | 10.00 | 81.3 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.32 | 1.01 | 1.78 | 0.00 | 10.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 5.65 | 14.76 | 24.39 | 2.00 | 82.5 | 88.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.83 | 11.09 | 18.07 | 2.00 | 83.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.58 | 10.50 | 17.25 | 1.00 | 79.3 | 86.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 3.11 | 9.00 | 14.45 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.48 | 7.21 | 11.61 | 2.00 | 67.2 | 68.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.26 | 13.45 | 23.11 | 2.00 | 82.5 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.84 | 13.27 | 21.12 | 2.00 | 83.1 | 90.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.49 | 10.94 | 17.24 | 2.00 | 75.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.29 | 27.39 | 45.33 | 15.00 | 82.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.24 | 16.89 | 27.98 | 1.00 | 82.5 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.44 | 15.84 | 26.00 | 2.00 | 82.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.62 | 13.87 | 22.50 | 5.00 | 84.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.13 | 13.05 | 21.44 | 1.00 | 82.5 | 45.0 |

## GW29

- Train rows: 153301
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 49.25
- Actual score: 30.00
- Transfer: Dominik Szoboszlai -> Morgan Gibbs-White (projected gain 5.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 0.00 | 5.93 | 11.18 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.27 | 1.00 | 1.83 | 0.00 | 11.6 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.23 | 11.65 | 18.73 | 1.00 | 82.6 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 11.60 | 20.68 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.53 | 10.37 | 16.89 | 0.00 | 81.5 | 0.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 3.03 | 8.78 | 14.31 | 2.00 | 83.5 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.19 | 6.84 | 11.33 | 0.00 | 67.5 | 0.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 5.72 | 16.78 | 27.06 | 2.00 | 82.6 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.03 | 11.93 | 19.18 | 8.00 | 76.4 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.43 | 10.80 | 17.12 | 2.00 | 69.0 | 79.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 24.77 | 42.87 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.86 | 15.18 | 26.21 | 0.00 | 72.8 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.09 | 15.00 | 24.92 | 6.00 | 82.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.93 | 14.51 | 23.37 | 2.00 | 82.6 | 78.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 6.6 | 4.41 | 12.13 | 19.37 | 5.00 | 82.6 | 88.0 |

## GW30

- Train rows: 154090
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 56.33
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.15) beats the best remaining Bench Boost opportunity (6.88).
- Transfer: Trent Alexander-Arnold -> Gabriel dos Santos Magalhães (projected gain 3.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.15) beats the best remaining Bench Boost opportunity (6.88).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 2.73 | 7.34 | 12.34 | 2.00 | 58.5 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.18 | 1.10 | 2.05 | 0.00 | 12.6 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.15 | 11.18 | 17.75 | 6.00 | 82.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 3.68 | 10.61 | 17.89 | 1.00 | 82.6 | 15.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 2.79 | 8.23 | 13.28 | 2.00 | 79.5 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 2.45 | 7.67 | 13.10 | 0.00 | 56.9 | 2.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.20 | 4.42 | 7.74 | 1.00 | 39.8 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.72 | 10.54 | 17.62 | 5.00 | 74.9 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.56 | 8.41 | 14.18 | 1.00 | 63.6 | 78.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 2.31 | 7.27 | 13.51 | 0.00 | 32.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.10 | 21.53 | 37.50 | 3.00 | 82.6 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.87 | 13.56 | 22.15 | 0.00 | 77.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.79 | 13.49 | 22.69 | 8.00 | 81.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.36 | 10.62 | 19.21 | 6.00 | 27.6 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 6.6 | 3.33 | 9.85 | 16.45 | 3.00 | 71.1 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 59.35
- Actual score: 32.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.92) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 7.39, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.92) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 2.78 | 7.98 | 12.89 | 3.00 | 75.6 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.47 | 1.25 | 2.16 | 0.00 | 12.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.41 | 10.29 | 16.69 | 9.00 | 81.5 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 3.10 | 8.71 | 13.91 | 1.00 | 83.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.86 | 7.85 | 13.16 | 1.00 | 49.7 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.01 | 5.80 | 9.48 | 0.00 | 55.7 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 0.96 | 4.34 | 8.95 | 0.00 | 24.6 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.22 | 13.14 | 19.92 | 2.00 | 65.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.50 | 11.02 | 18.26 | 2.00 | 76.0 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.70 | 9.04 | 15.17 | 2.00 | 68.5 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.92 | 22.95 | 38.50 | 2.00 | 82.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.7 | 4.97 | 15.68 | 27.06 | 1.00 | 73.4 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.40 | 13.17 | 22.54 | 3.00 | 82.7 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 6.6 | 3.66 | 10.85 | 17.93 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.00 | 4.73 | 9.70 | 0.00 | 11.1 | 0.0 |
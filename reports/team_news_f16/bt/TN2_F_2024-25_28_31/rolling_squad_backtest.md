# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 252.57
- Total actual points: 185.00
- Average predicted points: 63.14
- Average actual points: 46.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 73.22
- Actual score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.84 | 11.03 | 17.77 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.00 | 0.33 | 0.69 | 0.00 | 3.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.32 | 16.55 | 26.67 | 2.00 | 90.0 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.88 | 13.10 | 21.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.47 | 11.82 | 18.53 | 6.00 | 87.5 | 90.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 3.10 | 9.08 | 14.59 | 2.00 | 82.1 | 90.0 |
| Bench 4 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.47 | 7.12 | 11.28 | 2.00 | 65.6 | 68.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.94 | 15.27 | 25.44 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.82 | 13.31 | 21.20 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.43 | 10.77 | 16.83 | 2.00 | 72.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.94 | 29.13 | 47.55 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.92 | 18.70 | 30.26 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.10 | 17.61 | 28.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.60 | 13.93 | 22.62 | 5.00 | 86.1 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.5 | 4.45 | 11.33 | 18.16 | 11.00 | 77.6 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 50.16
- Actual score: 31.00
- Transfer: Virgil van Dijk -> Joško Gvardiol (projected gain 6.17, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.63 | 17.29 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.25 | 0.70 | 1.14 | 0.00 | 4.3 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.88 | 13.51 | 21.00 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.35 | 22.85 | 0.00 | 0.0 | 0.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 3.02 | 8.88 | 14.45 | 2.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.55 | 14.41 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.16 | 6.72 | 10.95 | 0.00 | 65.4 | 0.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.37 | 18.64 | 29.33 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.07 | 12.03 | 19.36 | 8.00 | 75.8 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.39 | 10.66 | 16.72 | 2.00 | 66.7 | 79.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.47 | 44.97 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.76 | 16.89 | 27.19 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.58 | 16.36 | 25.62 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.83 | 15.05 | 25.80 | 0.00 | 70.7 | 0.0 |
| Bench 4 | Bench | Ismaïla Sarr | MID | 7 | 5.5 | 0.00 | 9.76 | 16.76 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.03
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.20) beats the best remaining Bench Boost opportunity (5.85).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 9.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.20) beats the best remaining Bench Boost opportunity (5.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.33 | 12.43 | 19.80 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Danny Ward | GK | 11 | 3.9 | 0.18 | 0.74 | 1.29 | 0.00 | 12.9 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.04 | 11.10 | 17.82 | 6.00 | 81.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.87 | 9.99 | 15.96 | 2.00 | 63.7 | 75.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 2.69 | 8.16 | 13.37 | 2.00 | 79.5 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 12 | 7.3 | 1.41 | 5.15 | 11.44 | 0.00 | 21.3 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.25 | 4.48 | 7.86 | 1.00 | 40.9 | 45.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.4 | 5.98 | 16.10 | 24.93 | 9.00 | 90.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.64 | 10.44 | 17.67 | 5.00 | 71.5 | 90.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.35 | 7.85 | 13.45 | 1.00 | 58.3 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.74 | 23.33 | 39.75 | 3.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.80 | 13.46 | 22.22 | 0.00 | 73.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.69 | 13.41 | 22.75 | 8.00 | 81.5 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.6 | 4.88 | 12.19 | 19.60 | 2.00 | 64.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.44 | 10.72 | 19.32 | 6.00 | 29.1 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 0.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.14
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 4.65, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.89 | 11.60 | 18.28 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.05 | 0.52 | 1.01 | 0.00 | 5.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.62 | 13.40 | 21.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 12.22 | 19.08 | 9.00 | 89.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.45 | 10.08 | 15.44 | 8.00 | 68.3 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 3.10 | 8.83 | 14.07 | 1.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.95 | 5.51 | 8.94 | 0.00 | 54.3 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.4 | 4.20 | 13.03 | 19.54 | 2.00 | 63.3 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.54 | 11.14 | 18.47 | 2.00 | 75.6 | 90.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.68 | 8.94 | 14.82 | 2.00 | 66.5 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.61 | 24.88 | 40.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.00 | 15.66 | 26.77 | 1.00 | 72.5 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.10 | 15.13 | 24.96 | 3.00 | 90.0 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.6 | 3.32 | 10.98 | 17.13 | 2.00 | 59.9 | 90.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 0.56 | 4.41 | 9.68 | 0.00 | 5.8 | 0.0 |
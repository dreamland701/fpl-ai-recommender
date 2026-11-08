# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 252.22
- Total actual points: 182.00
- Average predicted points: 63.05
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
- Predicted score: 66.28
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.82 | 11.04 | 17.91 | 3.00 | 92.6 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 3.23 | 8.85 | 14.21 | 10.00 | 80.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 5.67 | 15.63 | 25.40 | 2.00 | 95.8 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.45 | 12.40 | 20.19 | 2.00 | 100.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.26 | 12.25 | 19.79 | 2.00 | 93.9 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.24 | 11.40 | 17.96 | 6.00 | 87.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.68 | 10.77 | 17.80 | 1.00 | 82.9 | 86.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.76 | 10.64 | 16.82 | 2.00 | 73.3 | 90.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.3 | 2.61 | 8.21 | 13.38 | 2.00 | 72.3 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.58 | 5.68 | 9.48 | 0.00 | 51.8 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 9.46 | 27.62 | 45.52 | 15.00 | 129.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.69 | 18.57 | 30.16 | 1.00 | 93.1 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.84 | 17.11 | 27.70 | 2.00 | 91.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.97 | 14.18 | 23.12 | 5.00 | 88.2 | 90.0 |
| Bench 2 | Bench | Mikkel Damsgaard | MID | 4 | 5.1 | 3.48 | 10.64 | 17.43 | 2.00 | 77.8 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 61.26
- Actual score: 35.00
- Transfer: Virgil van Dijk -> Joško Gvardiol (projected gain 5.62, hit 0)
- Autosub: Jamie Vardy replaced Trent Alexander-Arnold.
- Autosub: Paul Onuachu replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.75 | 10.75 | 17.55 | 6.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 2.10 | 7.71 | 13.35 | 0.00 | 61.9 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 5.29 | 13.76 | 21.37 | 1.00 | 109.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.01 | 13.58 | 23.16 | 0.00 | 70.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.54 | 12.60 | 20.25 | 5.00 | 99.0 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.56 | 10.57 | 17.33 | 0.00 | 84.3 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 2.31 | 8.52 | 14.32 | 0.00 | 51.3 | 0.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.60 | 10.58 | 16.65 | 2.00 | 64.1 | 79.0 |
| Bench 2 | Autosub In | Jamie Vardy | FWD | 11 | 5.3 | 3.08 | 8.17 | 12.99 | 2.00 | 77.2 | 90.0 |
| Bench 4 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 1.54 | 4.92 | 8.38 | 7.00 | 32.5 | 45.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 8.18 | 26.73 | 45.31 | 0.00 | 102.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.93 | 17.06 | 27.56 | 6.00 | 103.2 | 90.0 |
| Vice Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 6.27 | 17.03 | 26.68 | 2.00 | 109.7 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.58 | 14.83 | 25.64 | 0.00 | 66.1 | 0.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.37 | 10.14 | 16.87 | 2.00 | 80.0 | 84.0 |

## GW30

- Train rows: 154090
- Bank: 0.40 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: David Raya Martin
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.02
- Actual score: 44.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.52) beats the best remaining Triple Captain opportunity (8.88).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 5.07, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.52) beats the best remaining Triple Captain opportunity (8.88).
- Autosub: Paul Onuachu replaced Justin Kluivert.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 4.69 | 12.90 | 20.44 | 2.00 | 108.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 2.13 | 6.11 | 10.61 | 2.00 | 49.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.44 | 12.67 | 20.52 | 1.00 | 97.2 | 15.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.92 | 11.29 | 18.44 | 2.00 | 89.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.97 | 11.12 | 17.82 | 6.00 | 83.1 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.69 | 9.53 | 15.30 | 2.00 | 64.3 | 75.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.3 | 2.17 | 7.03 | 12.17 | 0.00 | 50.9 | 2.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.3 | 2.80 | 8.36 | 13.49 | 0.00 | 76.5 | 45.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.10 | 7.61 | 12.93 | 1.00 | 52.2 | 78.0 |
| Bench 2 | Autosub In | Paul Onuachu | FWD | 17 | 4.9 | 2.26 | 6.44 | 10.75 | 7.00 | 46.9 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.52 | 23.07 | 39.26 | 3.00 | 85.4 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.15 | 13.35 | 22.63 | 8.00 | 76.6 | 90.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 6.2 | 4.24 | 12.86 | 21.32 | 0.00 | 69.1 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.44 | 10.99 | 19.85 | 6.00 | 30.8 | 90.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.10 | 9.23 | 15.40 | 1.00 | 77.3 | 31.0 |

## GW31

- Train rows: 154881
- Bank: 1.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.66
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.40) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Justin Kluivert -> Luis Díaz (projected gain 5.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.40) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.01 | 11.71 | 18.60 | 2.00 | 95.6 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.6 | 2.49 | 7.48 | 12.29 | 3.00 | 68.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.93 | 13.52 | 21.49 | 2.00 | 106.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.17 | 12.11 | 19.05 | 9.00 | 90.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.33 | 9.53 | 14.78 | 8.00 | 63.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.65 | 7.27 | 12.29 | 1.00 | 43.4 | 90.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 0.89 | 5.21 | 10.31 | 0.00 | 26.0 | 0.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.69 | 8.66 | 14.63 | 2.00 | 64.3 | 64.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.63 | 7.64 | 12.46 | 1.00 | 58.7 | 17.0 |
| Bench 3 | Bench Boost | Jamie Vardy | FWD | 11 | 5.3 | 2.39 | 7.17 | 11.89 | 2.00 | 62.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.38 | 24.59 | 40.57 | 2.00 | 109.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.13 | 14.89 | 24.75 | 3.00 | 88.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.62 | 14.52 | 25.34 | 1.00 | 63.5 | 31.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.35 | 13.06 | 21.91 | 6.00 | 71.7 | 35.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 2.63 | 7.80 | 13.34 | 3.00 | 59.6 | 82.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 241.98
- Total actual points: 149.00
- Average predicted points: 60.49
- Average actual points: 37.25
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
- Predicted score: 71.99
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.16 | 12.02 | 19.47 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Lucas Bergström | GK | 6 | 3.9 | 0.44 | 0.67 | 0.94 | 0.00 | 5.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.11 | 15.96 | 25.75 | 2.00 | 90.0 | 88.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.25 | 11.24 | 17.67 | 6.00 | 83.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.64 | 10.81 | 17.82 | 1.00 | 82.2 | 86.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 7 | 4.7 | 3.55 | 9.74 | 15.55 | 5.00 | 83.5 | 90.0 |
| Bench 4 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.33 | 6.84 | 10.94 | 2.00 | 62.1 | 68.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 5.19 | 16.08 | 26.83 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 5.14 | 14.28 | 22.85 | 2.00 | 87.4 | 90.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.83 | 11.95 | 18.81 | 2.00 | 76.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.41 | 27.68 | 45.28 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.68 | 18.08 | 29.36 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.94 | 17.14 | 27.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.54 | 14.19 | 22.76 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.51 | 13.72 | 22.35 | 5.00 | 85.1 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 50.94
- Actual score: 30.00
- Transfer: Daniel Muñoz -> Rayan Aït-Nouri (projected gain 4.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.05 | 11.59 | 18.95 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Lucas Bergström | GK | 6 | 3.9 | 0.00 | 0.28 | 0.60 | 0.00 | 7.0 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.07 | 22.34 | 0.00 | 0.0 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 4.25 | 11.28 | 17.09 | 2.00 | 89.7 | 79.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.58 | 10.74 | 17.57 | 0.00 | 83.2 | 0.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 7 | 4.7 | 0.00 | 7.71 | 13.39 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.01 | 6.37 | 10.49 | 0.00 | 62.2 | 0.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.62 | 19.40 | 30.62 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.41 | 13.06 | 21.14 | 8.00 | 78.4 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.77 | 11.80 | 18.67 | 2.00 | 70.0 | 79.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 25.55 | 43.43 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.58 | 16.45 | 26.55 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.48 | 16.18 | 25.40 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.59 | 14.49 | 25.02 | 0.00 | 69.2 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.14 | 16.38 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 57.46
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.45) beats the best remaining Bench Boost opportunity (7.62).
- Transfer: Trent Alexander-Arnold -> Gabriel dos Santos Magalhães (projected gain 5.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.45) beats the best remaining Bench Boost opportunity (7.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.76 | 13.63 | 21.61 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Lucas Bergström | GK | 6 | 3.9 | 0.40 | 0.74 | 1.10 | 0.00 | 7.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 4.15 | 12.03 | 19.44 | 1.00 | 90.0 | 15.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.45 | 7.59 | 12.99 | 0.00 | 55.1 | 2.0 |
| Bench 3 | Bench Boost | Rayan Aït-Nouri | DEF | 20 | 4.8 | 2.23 | 6.62 | 11.01 | 8.00 | 59.5 | 81.0 |
| XI | XI | Marc Guéhi | DEF | 7 | 4.7 | 2.48 | 6.36 | 10.95 | 2.00 | 50.4 | 90.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.19 | 4.33 | 7.53 | 1.00 | 39.5 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.07 | 11.63 | 19.48 | 5.00 | 76.7 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.76 | 8.98 | 15.16 | 1.00 | 63.4 | 78.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 2.64 | 8.15 | 14.85 | 0.00 | 36.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.51 | 22.66 | 38.54 | 3.00 | 89.7 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.82 | 13.53 | 22.19 | 0.00 | 75.1 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.58 | 13.11 | 22.15 | 8.00 | 82.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.23 | 10.24 | 18.55 | 6.00 | 28.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.68 | 8.19 | 14.52 | 3.00 | 50.4 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.59
- Actual score: 21.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.28) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 8.14, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.28) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.19 | 12.54 | 19.90 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Lucas Bergström | GK | 6 | 3.9 | 0.23 | 0.73 | 1.13 | 0.00 | 8.9 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 3.16 | 8.80 | 14.50 | 2.00 | 74.1 | 87.0 |
| XI | XI | Marc Guéhi | DEF | 7 | 4.7 | 2.77 | 7.89 | 12.77 | -1.00 | 73.9 | 89.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.74 | 7.52 | 12.67 | 1.00 | 46.3 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.74 | 5.12 | 8.44 | 0.00 | 49.7 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 0.96 | 4.11 | 8.44 | 0.00 | 26.6 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.24 | 13.15 | 19.83 | 2.00 | 62.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.89 | 12.21 | 20.30 | 2.00 | 78.3 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.89 | 9.63 | 16.06 | 2.00 | 67.8 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.28 | 24.05 | 39.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.69 | 14.98 | 25.91 | 1.00 | 70.0 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.86 | 14.52 | 24.11 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.31 | 10.15 | 16.99 | 1.00 | 73.3 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.13 | 4.84 | 9.76 | 0.00 | 14.8 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 253.08
- Total actual points: 274.00
- Average predicted points: 63.27
- Average actual points: 68.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 143668
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 61.09
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.75 | 10.66 | 17.07 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.70 | 8.13 | 13.59 | 2.00 | 82.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.51 | 12.76 | 19.68 | 6.00 | 90.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.18 | 11.65 | 19.31 | 6.00 | 87.4 | 62.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.16 | 9.62 | 16.15 | 7.00 | 64.8 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 4.7 | 3.02 | 9.21 | 14.90 | 1.00 | 80.0 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.23 | 9.01 | 14.43 | 2.00 | 74.0 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.75 | 11.10 | 17.86 | 1.00 | 82.3 | 58.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.66 | 7.04 | 11.37 | 1.00 | 63.0 | 8.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.49 | 1.09 | 1.86 | 1.00 | 3.8 | 8.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.44 | 23.99 | 38.56 | 3.00 | 116.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.26 | 21.85 | 36.96 | 5.00 | 91.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.28 | 18.69 | 29.69 | 3.00 | 90.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.28 | 12.51 | 19.86 | 5.00 | 88.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 3.81 | 12.33 | 21.37 | 9.00 | 81.1 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.88
- Actual score: 46.00
- Transfer: Daniel Muñoz -> Lewis Hall (projected gain 2.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.70 | 10.68 | 17.22 | 3.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.4 | 2.34 | 7.62 | 12.82 | 0.00 | 83.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.93 | 11.52 | 18.37 | 2.00 | 80.7 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.6 | 4.00 | 10.96 | 17.33 | 7.00 | 90.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 3.62 | 10.89 | 18.19 | 0.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.91 | 9.80 | 16.57 | -1.00 | 70.6 | 90.0 |
| Bench 2 | Bench | Milos Kerkez | DEF | 3 | 4.6 | 2.74 | 8.12 | 13.56 | 6.00 | 74.3 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.58 | 9.67 | 16.06 | 2.00 | 70.4 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.59 | 5.10 | 8.82 | 1.00 | 40.4 | 45.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.28 | 1.54 | 2.68 | 0.00 | 8.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.54 | 23.40 | 37.35 | 3.00 | 106.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.87 | 22.53 | 37.45 | 21.00 | 93.7 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.16 | 18.69 | 30.43 | 1.00 | 86.0 | 23.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.75 | 14.09 | 23.52 | 2.00 | 92.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.29 | 11.27 | 17.80 | 3.00 | 72.3 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: wildcard
- Predicted score: 65.67
- Actual score: 67.00
- Transfer: none
- Chip used: Wildcard — full rebuild projects +12.42 squad value (threshold 12).
- Autosub: Nikola Milenković replaced Luis Díaz.
- Autosub: Ali Al-Hamadi replaced Jamie Vardy.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.09 | 11.19 | 17.99 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Łukasz Fabiański | GK | 19 | 4.1 | 3.39 | 9.00 | 14.69 | 2.00 | 91.6 | 35.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.57 | 12.86 | 20.66 | 7.00 | 87.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.61 | 11.98 | 19.15 | 2.00 | 75.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.17 | 11.28 | 17.86 | 6.00 | 74.3 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.0 | 4.12 | 10.89 | 17.38 | 6.00 | 86.1 | 90.0 |
| Bench 2 | Autosub In | Nikola Milenković | DEF | 16 | 4.6 | 3.46 | 9.58 | 15.24 | 6.00 | 80.0 | 90.0 |
| XI | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.60 | 8.82 | 14.72 | 0.00 | 62.3 | 0.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 5.0 | 2.11 | 5.87 | 9.91 | 0.00 | 47.3 | 0.0 |
| Bench 4 | Autosub In | Ali Al-Hamadi | FWD | 10 | 4.8 | 1.03 | 3.75 | 6.22 | 1.00 | 29.5 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 9.57 | 25.60 | 42.19 | 9.00 | 109.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 7.78 | 23.48 | 37.95 | 10.00 | 114.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.87 | 14.28 | 23.66 | 3.00 | 89.7 | 90.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.5 | 5.52 | 13.59 | 21.15 | 0.00 | 84.7 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 4.19 | 12.10 | 19.77 | 2.00 | 88.7 | 68.0 |

## GW19

- Train rows: 145775
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.44
- Actual score: 105.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.74) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Luis Díaz -> Anthony Gordon (projected gain 4.99, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.74) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.80 | 11.05 | 17.89 | 2.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Łukasz Fabiański | GK | 19 | 4.1 | 2.10 | 7.12 | 12.13 | 0.00 | 70.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.17 | 12.54 | 20.79 | 2.00 | 85.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.29 | 12.12 | 19.18 | 15.00 | 74.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.00 | 11.32 | 17.89 | 2.00 | 78.4 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.0 | 3.57 | 10.38 | 16.40 | 8.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Nikola Milenković | DEF | 16 | 4.6 | 3.29 | 9.56 | 15.25 | 6.00 | 88.6 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 1.30 | 5.05 | 8.62 | 2.00 | 25.5 | 90.0 |
| Bench 3 | Bench | Ali Al-Hamadi | FWD | 10 | 4.8 | 1.21 | 3.69 | 6.02 | 1.00 | 20.8 | 1.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.03 | 3.60 | 6.30 | 1.00 | 26.3 | 25.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.74 | 25.37 | 41.18 | 16.00 | 113.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.3 | 7.89 | 23.04 | 37.97 | 2.00 | 105.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.20 | 14.46 | 23.14 | 6.00 | 83.8 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 4.01 | 13.40 | 21.97 | 7.00 | 86.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 4.00 | 11.36 | 18.10 | 11.00 | 77.1 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 242.53
- Total actual points: 237.00
- Average predicted points: 60.63
- Average actual points: 59.25
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
- Captain: Cole Palmer
- Vice captain: Harry Wilson
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 49.25
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.72 | 9.34 | 15.12 | 7.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.53 | 8.66 | 14.07 | 2.00 | 75.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.06 | 16.81 | 26.49 | 3.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.70 | 14.58 | 24.76 | 0.00 | 2.7 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.27 | 14.44 | 21.92 | 0.00 | 85.7 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.23 | 12.61 | 19.83 | 1.00 | 85.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.37 | 11.04 | 17.89 | -1.00 | 66.6 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.7 | 2.24 | 8.14 | 12.81 | 5.00 | 54.5 | 17.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.90 | 7.65 | 11.69 | 16.00 | 44.4 | 81.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 4.9 | 2.18 | 6.26 | 9.82 | 5.00 | 38.6 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 4.07 | 22.01 | 35.43 | 13.00 | 88.6 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 5.13 | 17.17 | 28.07 | 2.00 | 81.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 3.87 | 16.12 | 27.31 | 0.00 | 73.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.47 | 15.64 | 24.52 | 3.00 | 89.5 | 90.0 |
| Vice Captain | XI | Harry Wilson | MID | 10 | 6.0 | 5.05 | 12.93 | 20.85 | 9.00 | 81.5 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 56.28
- Actual score: 64.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.43) beats the best remaining Triple Captain opportunity (17.17).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.79, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.43) beats the best remaining Triple Captain opportunity (17.17).
- Autosub: Marcos Senesi Barón replaced Lyle Foster.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.18 | 9.27 | 15.23 | 0.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.49 | 8.68 | 14.00 | 2.00 | 80.0 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.57 | 12.11 | 18.35 | 5.00 | 84.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.32 | 11.75 | 20.26 | 4.00 | 88.1 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 2.12 | 11.17 | 17.69 | 3.00 | 81.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.92 | 11.12 | 18.47 | 9.00 | 71.5 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.26 | 10.40 | 17.07 | 4.00 | 84.1 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 3.21 | 8.57 | 13.91 | 7.00 | 68.3 | 73.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.7 | 2.95 | 7.57 | 12.20 | 6.00 | 64.3 | 84.0 |
| XI | Bench | Lyle Foster | FWD | 3 | 4.9 | 3.10 | 7.19 | 10.93 | 0.00 | 62.9 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.43 | 21.16 | 34.20 | 4.00 | 82.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.38 | 15.38 | 25.47 | 4.00 | 77.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 2.50 | 13.28 | 22.99 | 8.00 | 45.7 | 89.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.86 | 12.80 | 20.69 | 5.00 | 77.8 | 90.0 |
| Bench 4 | Bench | Harry Wilson | MID | 10 | 6.0 | 1.89 | 9.16 | 15.48 | 2.00 | 59.6 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Dominic Calvert-Lewin
- Vice captain: Cole Palmer
- Effective captain: Dominic Calvert-Lewin
- Chip used: bench_boost
- Predicted score: 95.40
- Actual score: 90.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.20) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Norberto Bercique Gomes Betuncal -> Dominic Calvert-Lewin (projected gain 6.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.20) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.77 | 9.09 | 14.45 | 4.00 | 144.2 | 180.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 5.6 | 3.24 | 8.61 | 14.30 | 1.00 | 86.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 8.51 | 14.92 | 22.47 | 6.00 | 164.9 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 7.93 | 13.06 | 19.35 | 12.00 | 166.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.07 | 12.61 | 20.89 | 8.00 | 74.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 8.41 | 11.99 | 18.52 | 5.00 | 161.4 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 2.89 | 11.30 | 19.69 | 0.00 | 66.2 | 90.0 |
| Captain | Captain | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 10.53 | 13.56 | 19.77 | 8.00 | 154.4 | 180.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 8.25 | 10.34 | 15.99 | 10.00 | 138.1 | 137.0 |
| Bench 4 | Bench Boost | Lyle Foster | FWD | 3 | 4.9 | 2.23 | 4.65 | 7.44 | 2.00 | 62.0 | 44.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.5 | 9.68 | 19.18 | 30.05 | 2.00 | 161.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.55 | 18.85 | 31.54 | 6.00 | 81.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.67 | 15.97 | 27.07 | 10.00 | 73.4 | 90.0 |
| Bench 2 | Bench Boost | Dominik Szoboszlai | MID | 12 | 7.0 | 2.80 | 12.91 | 20.89 | 5.00 | 68.4 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 2.33 | 9.92 | 16.28 | 3.00 | 47.3 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominik Szoboszlai
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 41.60
- Actual score: 23.00
- Transfer: James Hill -> Pascal Struijk (projected gain 0.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 0.10 | 10.75 | 17.73 | 0.00 | 2.5 | 0.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.45 | 9.64 | 15.76 | 1.00 | 85.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.35 | 17.92 | 28.08 | 4.00 | 88.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.63 | 15.84 | 25.50 | 8.00 | 85.5 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.19 | 13.76 | 22.43 | 0.00 | 3.3 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.67 | 13.54 | 22.00 | 0.00 | 2.8 | 0.0 |
| XI | Bench | Pascal Struijk | DEF | 11 | 4.3 | 0.91 | 12.58 | 19.06 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 0.17 | 11.95 | 18.91 | 0.00 | 1.1 | 0.0 |
| XI | Bench | Junior Kroupi | FWD | 4 | 4.6 | 0.22 | 9.02 | 15.60 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 4.9 | 0.06 | 5.45 | 9.67 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.08 | 21.33 | 35.30 | 5.00 | 88.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.0 | 6.58 | 18.98 | 31.35 | 1.00 | 83.9 | 58.0 |
| Vice Captain | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.25 | 14.08 | 22.72 | 1.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 10.5 | 0.08 | 13.57 | 23.32 | 0.00 | 1.3 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 3.70 | 12.93 | 20.29 | 2.00 | 85.2 | 90.0 |
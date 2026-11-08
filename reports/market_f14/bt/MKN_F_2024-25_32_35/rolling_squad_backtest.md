# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 270.21
- Total actual points: 224.00
- Average predicted points: 67.55
- Average actual points: 56.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW31 are included before the first simulated week.
- League-average scores were not available for this run.

## GW32

- Train rows: 155673
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 76.41
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.75) beats the best remaining Bench Boost opportunity (15.09).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.75) beats the best remaining Bench Boost opportunity (15.09).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.14 | 11.66 | 18.65 | 2.00 | 96.1 | 90.0 |
| Bench 1 | Bench Boost | Danny Ward | GK | 11 | 3.9 | 0.30 | 0.63 | 0.89 | 0.00 | 12.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.47 | 12.74 | 20.37 | 1.00 | 99.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 4.83 | 12.31 | 19.03 | -1.00 | 113.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 5.83 | 12.01 | 17.52 | 8.00 | 119.3 | 180.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 3.62 | 9.53 | 15.15 | 2.00 | 87.4 | 90.0 |
| Bench 4 | Bench Boost | Noussair Mazraoui | DEF | 14 | 4.2 | 2.09 | 7.29 | 12.14 | 0.00 | 73.0 | 77.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.12 | 17.22 | 26.88 | 11.00 | 107.5 | 148.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.88 | 13.57 | 21.56 | 7.00 | 82.0 | 81.0 |
| Bench 3 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.46 | 8.28 | 14.00 | 1.00 | 59.6 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.13 | 23.90 | 39.43 | 6.00 | 105.1 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.08 | 14.37 | 24.54 | 4.00 | 58.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 6.90 | 13.96 | 19.93 | 19.00 | 116.6 | 138.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 3.74 | 13.60 | 24.07 | 2.00 | 81.2 | 81.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.70 | 12.36 | 19.81 | 6.00 | 85.4 | 84.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: Mohamed Salah
- Effective captain: Omar Marmoush
- Chip used: triple_captain
- Predicted score: 84.00
- Actual score: 49.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.49) beats the best remaining Triple Captain opportunity (9.63).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Omar Marmoush. Optimizer chose Triple Captain here because the current estimated captain upside (13.49) beats the best remaining Triple Captain opportunity (9.63).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 8.29 | 16.98 | 25.47 | 7.00 | 162.3 | 180.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.08 | 0.31 | 0.47 | 0.00 | 9.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 7.36 | 16.36 | 24.86 | 7.00 | 151.8 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 5.97 | 14.34 | 21.75 | 6.00 | 150.4 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.27 | 10.60 | 17.06 | 0.00 | 99.2 | 90.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.5 | 2.77 | 8.37 | 14.00 | 2.00 | 82.5 | 90.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.2 | 2.47 | 7.29 | 11.87 | 2.00 | 73.1 | 90.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 9.24 | 18.99 | 28.04 | 4.00 | 144.9 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.19 | 16.36 | 27.60 | 2.00 | 87.7 | 75.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.83 | 6.26 | 10.65 | 1.00 | 47.7 | 27.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.8 | 8.42 | 23.11 | 38.06 | 3.00 | 108.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 6.45 | 15.19 | 23.17 | 7.00 | 134.4 | 166.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.15 | 13.57 | 22.99 | 1.00 | 77.6 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 3.89 | 13.35 | 23.24 | 2.00 | 61.1 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.29 | 10.99 | 18.39 | 2.00 | 70.4 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.49
- Actual score: 56.00
- Transfer: Joško Gvardiol -> Rayan Aït-Nouri (projected gain 8.68, hit 0)
- Autosub: Noussair Mazraoui replaced Daniel Muñoz.
- Autosub: Norberto Bercique Gomes Betuncal replaced Omar Marmoush.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 1.74 | 9.91 | 16.96 | 0.00 | 64.4 | 0.0 |
| Bench 1 | Bench | Danny Ward | GK | 11 | 3.9 | 0.16 | 0.30 | 0.57 | 0.00 | 6.5 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 5.0 | 6.04 | 15.37 | 23.47 | 11.00 | 107.5 | 76.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 5.33 | 11.82 | 18.52 | 6.00 | 109.7 | 90.0 |
| XI | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 2.00 | 10.73 | 18.84 | 0.00 | 72.8 | 0.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 3.17 | 8.59 | 14.20 | 0.00 | 88.5 | 90.0 |
| Bench 2 | Autosub In | Noussair Mazraoui | DEF | 14 | 4.2 | 2.00 | 6.70 | 11.30 | 2.00 | 72.1 | 74.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.87 | 19.68 | 31.07 | 6.00 | 108.9 | 76.0 |
| XI | Bench | Omar Marmoush | FWD | 13 | 7.6 | 2.21 | 13.82 | 24.05 | 0.00 | 52.2 | 0.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.70 | 5.82 | 9.98 | 2.00 | 47.9 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.72 | 23.08 | 37.10 | 8.00 | 117.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 6.04 | 16.67 | 27.08 | 3.00 | 94.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.82 | 13.82 | 22.18 | 6.00 | 84.3 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.84 | 13.19 | 22.66 | 4.00 | 71.2 | 90.0 |
| Bench 3 | Bench | Morgan Rogers | MID | 2 | 5.6 | 1.81 | 10.96 | 19.15 | 0.00 | 49.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 1.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 48.31
- Actual score: 45.00
- Transfer: Danny Ward -> Jordan Pickford (projected gain 3.14, hit 0)
- Autosub: Norberto Bercique Gomes Betuncal replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.19 | 10.69 | 17.04 | 2.00 | 98.2 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 2.56 | 7.67 | 13.40 | 1.00 | 60.3 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.15 | 9.12 | 15.01 | 2.00 | 80.0 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.80 | 8.30 | 13.68 | 5.00 | 81.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.66 | 7.68 | 13.18 | 1.00 | 61.7 | 90.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 20 | 5.0 | 0.95 | 6.94 | 12.89 | 2.00 | 36.7 | 90.0 |
| Bench 3 | Bench | Noussair Mazraoui | DEF | 14 | 4.2 | 1.77 | 6.25 | 10.68 | 0.00 | 65.9 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 5.17 | 16.32 | 26.90 | 9.00 | 69.9 | 90.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.19 | 10.62 | 17.66 | 2.00 | 51.9 | 82.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.69 | 6.88 | 11.24 | 6.00 | 56.0 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 6.59 | 21.28 | 35.47 | 2.00 | 96.7 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.61 | 12.70 | 21.88 | 0.00 | 69.9 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 3.57 | 12.56 | 21.40 | 10.00 | 64.5 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.09 | 10.80 | 18.68 | 1.00 | 48.4 | 55.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 2.72 | 8.53 | 15.00 | 3.00 | 46.9 | 90.0 |
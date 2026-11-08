# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 286.65
- Total actual points: 267.00
- Average predicted points: 71.66
- Average actual points: 66.75
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
- Captain: Alexander Isak
- Vice captain: Jacob Murphy
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 95.54
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.03) beats the best remaining Triple Captain opportunity (14.93).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (15.03) beats the best remaining Triple Captain opportunity (14.93).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.36 | 9.71 | 16.01 | 2.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.61 | 1.33 | 2.14 | 0.00 | 11.9 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.31 | 12.39 | 18.99 | -1.00 | 160.1 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.80 | 11.50 | 18.08 | 2.00 | 80.9 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.79 | 10.98 | 16.50 | 8.00 | 155.4 | 180.0 |
| Bench 2 | Bench | Ryan Sessegnon | DEF | 9 | 4.1 | 2.77 | 7.64 | 12.30 | 1.00 | 57.4 | 56.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 1.79 | 5.80 | 9.97 | 1.00 | 82.2 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.16 | 17.10 | 27.01 | 11.00 | 151.5 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.23 | 13.86 | 21.32 | 2.00 | 145.8 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.55 | 8.33 | 14.07 | 1.00 | 65.0 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 7.85 | 22.96 | 38.58 | 6.00 | 83.1 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.35 | 15.24 | 26.21 | 4.00 | 69.7 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.81 | 13.56 | 20.21 | 19.00 | 157.7 | 138.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.31 | 13.28 | 23.34 | 2.00 | 83.1 | 81.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 6.27 | 12.46 | 19.86 | 7.00 | 140.9 | 165.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: William Saliba
- Vice captain: Mohamed Salah
- Effective captain: William Saliba
- Chip used: bench_boost
- Predicted score: 82.81
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.75) beats the best remaining Bench Boost opportunity (7.73).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.75) beats the best remaining Bench Boost opportunity (7.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 7.76 | 12.03 | 18.91 | 7.00 | 166.3 | 180.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.33 | 1.03 | 1.75 | 7.00 | 9.5 | 90.0 |
| Captain | Captain | William Saliba | DEF | 1 | 6.5 | 8.90 | 13.55 | 21.02 | 7.00 | 166.3 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.11 | 11.73 | 18.22 | 6.00 | 166.3 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 2.88 | 9.07 | 14.83 | 0.00 | 83.1 | 90.0 |
| Bench 2 | Bench Boost | Ryan Sessegnon | DEF | 9 | 4.1 | 2.37 | 6.97 | 11.10 | 11.00 | 53.5 | 78.0 |
| Bench 4 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 1.70 | 5.59 | 9.70 | 0.00 | 80.6 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.21 | 15.05 | 25.56 | 2.00 | 83.1 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.78 | 13.18 | 20.25 | 10.00 | 147.0 | 84.0 |
| Bench 3 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.10 | 6.78 | 11.31 | 1.00 | 52.9 | 27.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.8 | 7.86 | 21.81 | 36.69 | 3.00 | 83.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.66 | 14.05 | 24.26 | 2.00 | 74.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.43 | 13.80 | 23.23 | 1.00 | 81.9 | 31.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 7.43 | 12.18 | 19.33 | 3.00 | 166.3 | 117.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.39 | 11.06 | 18.45 | 2.00 | 74.4 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.85
- Actual score: 70.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.73, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 10.63 | 17.63 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Daniel Bentley | GK | 20 | 3.9 | 1.68 | 3.85 | 5.79 | 0.00 | 39.4 | 0.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.5 | 0.00 | 12.09 | 19.85 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 11.17 | 18.83 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ryan Sessegnon | DEF | 9 | 4.1 | 3.93 | 10.25 | 15.53 | 11.00 | 74.4 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.68 | 9.87 | 15.94 | 6.00 | 83.1 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 1.99 | 6.47 | 10.83 | 1.00 | 82.6 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.60 | 17.62 | 28.38 | 6.00 | 83.1 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.12 | 13.05 | 19.66 | 15.00 | 83.1 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.95 | 6.36 | 10.74 | 2.00 | 53.3 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.93 | 21.46 | 35.03 | 8.00 | 83.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.44 | 15.37 | 25.34 | 3.00 | 83.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.52 | 14.04 | 23.61 | 4.00 | 78.4 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.08 | 13.48 | 22.08 | 6.00 | 78.8 | 66.0 |
| Bench 4 | Bench | Ismaïla Sarr | MID | 7 | 5.8 | 0.00 | 9.53 | 16.43 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.45
- Actual score: 44.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 5.44, hit 0)
- Autosub: Ismaïla Sarr replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.75 | 8.01 | 14.03 | 1.00 | 64.3 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.26 | 1.20 | 2.26 | 0.00 | 15.8 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.48 | 9.42 | 15.17 | 2.00 | 81.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.19 | 9.33 | 16.39 | 1.00 | 66.7 | 90.0 |
| Bench 3 | Bench | Ryan Sessegnon | DEF | 9 | 4.1 | 2.35 | 7.52 | 12.71 | 0.00 | 61.8 | 56.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.39 | 7.41 | 13.12 | 1.00 | 65.8 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 1.97 | 6.06 | 10.19 | 1.00 | 79.7 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.32 | 17.26 | 27.67 | 9.00 | 80.4 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.52 | 12.91 | 20.88 | 7.00 | 83.9 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.61 | 6.98 | 11.51 | 6.00 | 58.7 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.08 | 20.75 | 34.47 | 2.00 | 83.1 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.53 | 13.60 | 22.78 | 0.00 | 79.8 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.30 | 13.26 | 22.38 | 10.00 | 75.2 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.19 | 11.96 | 20.04 | 1.00 | 66.3 | 55.0 |
| Bench 2 | Autosub In | Ismaïla Sarr | MID | 7 | 5.7 | 2.39 | 7.50 | 13.07 | 2.00 | 55.9 | 90.0 |
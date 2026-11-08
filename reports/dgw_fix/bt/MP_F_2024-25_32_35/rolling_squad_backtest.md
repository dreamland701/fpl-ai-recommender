# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 295.27
- Total actual points: 257.00
- Average predicted points: 73.82
- Average actual points: 64.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Alexander Isak
- Vice captain: Jacob Murphy
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 97.85
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.25) beats the best remaining Triple Captain opportunity (15.54).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (15.25) beats the best remaining Triple Captain opportunity (15.54).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.91 | 11.38 | 18.44 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.13 | 0.47 | 0.88 | 0.00 | 7.5 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.57 | 14.98 | 21.39 | -1.00 | 166.5 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.82 | 12.65 | 17.75 | 8.00 | 155.0 | 180.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.17 | 12.35 | 19.93 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 3.04 | 8.17 | 13.40 | 0.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.32 | 7.44 | 12.17 | 1.00 | 89.8 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.37 | 21.81 | 32.16 | 11.00 | 155.0 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.19 | 16.24 | 23.34 | 2.00 | 144.0 | 100.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.45 | 7.93 | 13.58 | 1.00 | 60.9 | 26.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.30 | 25.06 | 42.17 | 6.00 | 90.0 | 84.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 9.04 | 15.98 | 22.31 | 19.00 | 161.6 | 138.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.16 | 15.01 | 25.80 | 4.00 | 63.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 4.70 | 14.49 | 24.70 | 2.00 | 90.0 | 81.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 5.89 | 13.89 | 20.54 | 7.00 | 128.8 | 165.0 |

## GW33

- Train rows: 156471
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Joško Gvardiol
- Vice captain: David Raya Martin
- Effective captain: Joško Gvardiol
- Chip used: bench_boost
- Predicted score: 88.89
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.91) beats the best remaining Bench Boost opportunity (7.89).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.91) beats the best remaining Bench Boost opportunity (7.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 8.90 | 12.45 | 19.99 | 7.00 | 180.0 | 180.0 |
| Bench 1 | Bench Boost | Alfie Whiteman | GK | 18 | 3.9 | 0.00 | 0.22 | 0.42 | 0.00 | 4.6 | 0.0 |
| Captain | Captain | Joško Gvardiol | DEF | 13 | 6.2 | 9.20 | 13.29 | 21.36 | 7.00 | 180.0 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 8.42 | 12.34 | 19.29 | 6.00 | 180.0 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.51 | 10.40 | 16.39 | 0.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Toti António Gomes | DEF | 20 | 4.3 | 2.53 | 7.46 | 12.25 | 9.00 | 78.9 | 90.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.25 | 7.19 | 11.82 | 0.00 | 88.3 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.91 | 17.14 | 28.50 | 2.00 | 90.0 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.84 | 11.62 | 18.40 | 10.00 | 147.6 | 84.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.88 | 6.12 | 10.32 | 1.00 | 47.3 | 27.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 8.32 | 23.92 | 40.11 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.46 | 14.10 | 24.18 | 2.00 | 68.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.40 | 13.70 | 23.01 | 1.00 | 81.7 | 31.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.8 | 8.68 | 12.39 | 19.88 | 3.00 | 180.0 | 117.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.41 | 10.54 | 17.23 | 2.00 | 72.7 | 64.0 |

## GW34

- Train rows: 157270
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.97
- Actual score: 64.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 6.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martin | GK | 1 | 5.5 | 0.00 | 9.52 | 18.46 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.9 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 9.99 | 19.43 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.76 | 9.94 | 16.10 | 6.00 | 85.4 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 0.00 | 9.90 | 19.39 | 0.00 | 0.0 | 0.0 |
| XI | XI | Toti António Gomes | DEF | 20 | 4.3 | 2.96 | 7.66 | 12.41 | 5.00 | 75.5 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.08 | 6.77 | 11.20 | 1.00 | 85.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 7.28 | 19.25 | 30.97 | 6.00 | 90.0 | 76.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 5.80 | 14.33 | 21.72 | 15.00 | 90.0 | 88.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.71 | 5.73 | 9.78 | 2.00 | 47.6 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.47 | 23.40 | 38.13 | 8.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.92 | 16.53 | 26.98 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.41 | 13.55 | 22.92 | 4.00 | 75.6 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.11 | 13.19 | 21.72 | 6.00 | 79.0 | 66.0 |
| Bench 4 | Bench | Ismaïla Sarr | MID | 7 | 5.8 | 0.00 | 8.66 | 17.10 | 0.00 | 0.0 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.90 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.55
- Actual score: 50.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 6.40, hit 0)
- Autosub: Dara O'Shea replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 2.51 | 7.87 | 13.77 | 1.00 | 57.2 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.04 | 0.04 | 0.11 | 0.00 | 1.8 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.04 | 9.70 | 16.67 | 8.00 | 67.3 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.56 | 9.31 | 14.96 | 2.00 | 83.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.16 | 7.30 | 12.53 | 1.00 | 59.0 | 90.0 |
| Bench 4 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 2.01 | 6.87 | 11.57 | 2.00 | 74.9 | 90.0 |
| Bench 2 | Autosub In | Dara O'Shea | DEF | 10 | 3.9 | 2.06 | 6.43 | 10.61 | 1.00 | 82.1 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.45 | 17.46 | 28.06 | 9.00 | 82.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.56 | 12.81 | 20.89 | 7.00 | 85.1 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.42 | 6.55 | 10.80 | 6.00 | 53.9 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.59 | 22.77 | 37.45 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 4.43 | 13.27 | 22.32 | 0.00 | 77.4 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.11 | 13.10 | 21.97 | 10.00 | 69.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.15 | 11.61 | 19.25 | 1.00 | 63.2 | 55.0 |
| Bench 3 | Bench | Ismaïla Sarr | MID | 7 | 5.7 | 2.02 | 6.71 | 11.62 | 2.00 | 47.4 | 90.0 |
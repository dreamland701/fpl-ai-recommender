# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 291.58
- Total actual points: 299.00
- Average predicted points: 72.90
- Average actual points: 74.75
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
- Predicted score: 96.22
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.05) beats the best remaining Triple Captain opportunity (14.95).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (15.05) beats the best remaining Triple Captain opportunity (14.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 5.41 | 9.37 | 14.75 | 2.00 | 157.3 | 180.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.9 | 0.10 | 0.65 | 1.31 | 0.00 | 10.9 | 0.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 7.51 | 12.52 | 19.20 | -1.00 | 162.0 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.90 | 11.63 | 18.28 | 2.00 | 81.9 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 6.81 | 10.95 | 16.37 | 8.00 | 157.7 | 180.0 |
| Bench 3 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 3.07 | 8.23 | 13.41 | 0.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Ryan Sessegnon | DEF | 9 | 4.1 | 2.71 | 7.51 | 12.11 | 1.00 | 56.1 | 56.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 9.5 | 11.18 | 17.07 | 26.88 | 11.00 | 153.8 | 148.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 8.25 | 13.83 | 21.18 | 2.00 | 148.1 | 100.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.6 | 4.53 | 13.24 | 21.13 | 7.00 | 79.1 | 81.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 7.71 | 22.60 | 38.21 | 6.00 | 82.6 | 84.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.35 | 15.24 | 26.23 | 4.00 | 69.4 | 90.0 |
| Vice Captain | XI | Jacob Murphy | MID | 15 | 5.2 | 8.83 | 13.53 | 20.07 | 19.00 | 160.0 | 138.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.38 | 12.87 | 21.76 | 9.00 | 68.0 | 90.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 3.78 | 10.22 | 16.61 | 2.00 | 81.1 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Omar Marmoush
- Vice captain: William Saliba
- Effective captain: Omar Marmoush
- Chip used: bench_boost
- Predicted score: 87.25
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.78) beats the best remaining Bench Boost opportunity (9.16).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.78) beats the best remaining Bench Boost opportunity (9.16).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 5.70 | 9.61 | 15.34 | 10.00 | 165.4 | 180.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.9 | 0.29 | 0.70 | 1.19 | 0.00 | 9.2 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.5 | 8.64 | 13.21 | 20.69 | 7.00 | 165.4 | 180.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 6.86 | 11.40 | 17.90 | 6.00 | 165.4 | 180.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 2.75 | 8.74 | 14.50 | 0.00 | 82.7 | 90.0 |
| Bench 3 | Bench Boost | Toti António Gomes | DEF | 20 | 4.3 | 2.55 | 7.49 | 12.23 | 9.00 | 80.8 | 90.0 |
| Bench 4 | Bench Boost | Ryan Sessegnon | DEF | 9 | 4.1 | 2.31 | 6.83 | 10.90 | 11.00 | 52.0 | 78.0 |
| Captain | Captain | Omar Marmoush | FWD | 13 | 7.6 | 10.30 | 15.80 | 24.93 | 4.00 | 165.4 | 180.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.08 | 14.72 | 25.24 | 2.00 | 82.6 | 75.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 7 | 7.8 | 7.78 | 13.14 | 20.11 | 10.00 | 149.1 | 84.0 |
| XI | XI | Mohamed Salah | MID | 12 | 13.8 | 7.74 | 21.48 | 36.36 | 3.00 | 82.7 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 5.51 | 14.31 | 23.55 | 3.00 | 81.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 4.67 | 14.06 | 24.28 | 2.00 | 74.3 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 3.40 | 11.06 | 18.47 | 2.00 | 74.1 | 64.0 |
| Bench 2 | Bench Boost | Enzo Fernández | MID | 6 | 4.7 | 3.38 | 9.91 | 16.36 | 5.00 | 79.1 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.22
- Actual score: 81.00
- Transfer: Jean-Philippe Mateta -> Matheus Santos Carneiro Da Cunha (projected gain 4.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 0.00 | 8.17 | 14.35 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Tom Heaton | GK | 14 | 3.9 | 0.20 | 0.59 | 1.15 | 0.00 | 8.5 | 0.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.5 | 0.00 | 11.73 | 19.47 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.2 | 0.00 | 10.80 | 18.45 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ryan Sessegnon | DEF | 9 | 4.1 | 3.93 | 10.25 | 15.53 | 11.00 | 74.2 | 90.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.78 | 9.99 | 16.11 | 6.00 | 84.0 | 90.0 |
| XI | XI | Toti António Gomes | DEF | 20 | 4.3 | 3.01 | 7.72 | 12.55 | 5.00 | 77.9 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.46 | 17.26 | 28.00 | 6.00 | 82.7 | 76.0 |
| Bench 4 | Bench | Omar Marmoush | FWD | 13 | 7.6 | 0.00 | 13.30 | 21.89 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.0 | 4.98 | 12.69 | 19.28 | 15.00 | 82.7 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.79 | 21.09 | 34.66 | 8.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 5.29 | 15.01 | 24.96 | 3.00 | 82.7 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 5.36 | 14.60 | 23.40 | 7.00 | 82.7 | 75.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 5.08 | 13.44 | 21.96 | 6.00 | 79.8 | 66.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.54 | 10.29 | 16.64 | 6.00 | 80.5 | 90.0 |

## GW35

- Train rows: 158070
- Bank: 0.80 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 50.89
- Actual score: 49.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Yoane Wissa (projected gain 3.69, hit 0)
- Autosub: Omar Marmoush replaced Luis Díaz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 1.89 | 6.17 | 10.93 | 3.00 | 71.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.9 | 0.17 | 0.52 | 1.02 | 0.00 | 8.2 | 0.0 |
| XI | XI | Tino Livramento | DEF | 15 | 4.6 | 3.60 | 9.56 | 15.36 | 2.00 | 82.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.5 | 3.19 | 9.34 | 16.39 | 1.00 | 66.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.2 | 2.39 | 7.42 | 13.12 | 1.00 | 65.7 | 90.0 |
| Bench 3 | Bench | Ryan Sessegnon | DEF | 9 | 4.1 | 2.29 | 7.37 | 12.49 | 0.00 | 60.4 | 56.0 |
| Bench 4 | Bench | Toti António Gomes | DEF | 20 | 4.3 | 2.06 | 6.91 | 11.69 | 2.00 | 77.4 | 90.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 9.5 | 6.32 | 17.21 | 27.55 | 9.00 | 81.3 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 4.64 | 13.04 | 21.08 | 7.00 | 84.9 | 90.0 |
| Bench 2 | Autosub In | Omar Marmoush | FWD | 13 | 7.6 | 2.96 | 9.71 | 17.30 | 2.00 | 42.7 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 6.93 | 20.37 | 34.05 | 2.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 4.30 | 13.26 | 22.38 | 10.00 | 75.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.2 | 4.19 | 11.97 | 20.04 | 1.00 | 66.1 | 55.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.5 | 3.43 | 11.82 | 20.04 | 0.00 | 65.4 | 0.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.07 | 9.92 | 16.27 | 9.00 | 81.0 | 87.0 |
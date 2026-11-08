# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 279.73
- Total actual points: 255.00
- Average predicted points: 69.93
- Average actual points: 63.75
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
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 62.16
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.60 | 9.32 | 14.56 | 3.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.10 | 8.66 | 14.07 | 2.00 | 88.8 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.77 | 16.81 | 26.49 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.58 | 24.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.58 | 14.44 | 21.92 | 0.00 | 90.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.48 | 12.61 | 19.83 | 1.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.89 | 11.04 | 17.89 | -1.00 | 86.3 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.23 | 8.95 | 14.32 | 2.00 | 70.5 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.7 | 2.94 | 8.14 | 12.81 | 5.00 | 60.9 | 17.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.81 | 7.65 | 11.69 | 16.00 | 53.0 | 81.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.36 | 22.01 | 35.43 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.67 | 17.17 | 28.07 | 2.00 | 86.7 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 5.06 | 16.12 | 27.31 | 0.00 | 69.3 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.19 | 15.64 | 24.52 | 3.00 | 90.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.97 | 12.93 | 20.85 | 9.00 | 81.5 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 53.59
- Actual score: 54.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 3.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.18 | 8.68 | 14.00 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.06 | 6.47 | 10.97 | 2.00 | 72.9 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.58 | 12.11 | 18.35 | 5.00 | 89.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.98 | 11.75 | 20.26 | 4.00 | 62.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.67 | 11.17 | 17.69 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.74 | 11.12 | 18.47 | 9.00 | 76.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.31 | 10.40 | 17.07 | 4.00 | 82.7 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.49 | 10.52 | 16.16 | 2.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.89 | 8.57 | 13.91 | 7.00 | 60.3 | 73.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.34 | 7.57 | 12.20 | 6.00 | 49.5 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.01 | 21.16 | 34.20 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.02 | 15.38 | 25.47 | 4.00 | 84.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.33 | 13.28 | 22.99 | 8.00 | 47.4 | 89.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.27 | 12.80 | 20.69 | 5.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Harry Wilson | MID | 10 | 6.0 | 2.95 | 9.16 | 15.48 | 2.00 | 58.3 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 2.70
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Marcos Senesi Barón
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 109.70
- Actual score: 108.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.26) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Gabriel dos Santos Magalhães -> Marc Guéhi (projected gain 0.74, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 5.44 | 9.09 | 14.45 | 4.00 | 175.1 | 180.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.9 | 2.58 | 7.60 | 12.51 | 10.00 | 81.3 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 10.16 | 14.92 | 22.47 | 6.00 | 180.0 | 180.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.46 | 13.28 | 20.85 | 8.00 | 173.7 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.41 | 13.06 | 19.35 | 12.00 | 162.1 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.61 | 20.89 | 8.00 | 87.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.72 | 11.99 | 18.52 | 5.00 | 171.0 | 180.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 8.91 | 13.56 | 19.77 | 8.00 | 166.3 | 180.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 6.72 | 10.34 | 15.99 | 10.00 | 133.6 | 137.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.53 | 7.55 | 13.17 | 9.00 | 53.7 | 72.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.46 | 19.18 | 30.05 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.53 | 18.85 | 31.54 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 5.39 | 15.97 | 27.07 | 10.00 | 74.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.37 | 12.91 | 20.89 | 5.00 | 80.8 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 3.31 | 9.92 | 16.28 | 3.00 | 67.7 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 2.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 54.29
- Actual score: 40.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Norberto Bercique Gomes Betuncal -> Jarrod Bowen (projected gain 9.50, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 0.00 | 10.75 | 17.73 | 0.00 | 0.0 | 0.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 2.72 | 7.87 | 13.05 | 7.00 | 82.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.39 | 17.92 | 28.08 | 4.00 | 90.0 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 13.76 | 22.43 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.1 | 0.00 | 13.55 | 22.06 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.54 | 22.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 12.18 | 20.26 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 6.39 | 17.77 | 27.98 | 10.00 | 90.0 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 0.00 | 11.95 | 18.91 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 0.00 | 9.02 | 15.60 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.46 | 21.33 | 35.30 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.0 | 6.55 | 18.98 | 31.35 | 1.00 | 90.0 | 58.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.03 | 14.08 | 22.72 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.57 | 23.32 | 0.00 | 0.0 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.83 | 12.93 | 20.29 | 2.00 | 89.0 | 90.0 |
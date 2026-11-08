# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 277.80
- Total actual points: 265.00
- Average predicted points: 69.45
- Average actual points: 66.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Anthony Gordon
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 66.50
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Adrien Truffert replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.73 | 9.32 | 14.56 | 3.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.06 | 8.74 | 14.22 | 2.00 | 88.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.99 | 16.81 | 26.49 | 3.00 | 105.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.96 | 14.44 | 21.92 | 0.00 | 103.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.56 | 12.61 | 19.83 | 1.00 | 93.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.97 | 11.27 | 18.26 | -1.00 | 87.6 | 90.0 |
| Bench 2 | Autosub In | Adrien Truffert | DEF | 4 | 4.6 | 3.92 | 11.15 | 18.16 | 4.00 | 86.9 | 90.0 |
| XI | XI | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 4.05 | 11.22 | 18.21 | 5.00 | 71.5 | 8.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 3.53 | 9.44 | 14.42 | 16.00 | 67.0 | 81.0 |
| Bench 4 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 3.19 | 9.34 | 15.54 | 1.00 | 74.1 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.61 | 22.01 | 35.43 | 13.00 | 116.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 5.57 | 17.76 | 30.09 | 0.00 | 69.7 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.81 | 17.17 | 28.07 | 2.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.36 | 15.64 | 24.52 | 3.00 | 102.3 | 90.0 |
| Vice Captain | XI | Anthony Gordon | MID | 15 | 7.3 | 6.29 | 15.57 | 23.83 | 10.00 | 98.4 | 88.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.80
- Actual score: 65.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.44, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.11 | 8.68 | 14.00 | 2.00 | 91.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.12 | 7.13 | 12.09 | 2.00 | 77.6 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.71 | 12.11 | 18.35 | 5.00 | 90.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.73 | 12.10 | 20.09 | 9.00 | 77.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.74 | 11.17 | 17.69 | 3.00 | 93.2 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.36 | 10.74 | 17.64 | 4.00 | 84.9 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.11 | 10.01 | 16.56 | 4.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 2.74 | 10.48 | 18.39 | 1.00 | 27.0 | 10.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 3.43 | 10.12 | 16.43 | 7.00 | 70.6 | 73.0 |
| XI | XI | Valentín Castellanos | FWD | 19 | 5.5 | 3.49 | 9.49 | 15.58 | 11.00 | 67.1 | 81.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.91 | 21.16 | 34.20 | 4.00 | 96.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.0 | 5.57 | 17.21 | 29.79 | 8.00 | 37.7 | 89.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.02 | 15.71 | 26.01 | 4.00 | 85.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.40 | 13.54 | 21.90 | 5.00 | 81.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 3.77 | 11.95 | 19.26 | 3.00 | 70.9 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Danny Welbeck
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 89.20
- Actual score: 102.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.69) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Raúl Jiménez Rodríguez -> Danny Welbeck (projected gain 6.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.69) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 4.62 | 10.98 | 17.45 | 4.00 | 132.9 | 180.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.9 | 2.65 | 7.86 | 12.93 | 10.00 | 84.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 7.32 | 17.04 | 25.66 | 6.00 | 146.8 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 6.94 | 16.05 | 23.79 | 12.00 | 129.7 | 180.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.6 | 6.30 | 14.86 | 23.06 | 13.00 | 113.3 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 6.13 | 14.50 | 22.40 | 5.00 | 131.9 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.16 | 12.88 | 21.34 | 8.00 | 86.1 | 90.0 |
| Vice Captain | XI | Danny Welbeck | FWD | 6 | 6.3 | 7.36 | 16.66 | 25.17 | 8.00 | 89.2 | 81.0 |
| Bench 3 | Bench Boost | Valentín Castellanos | FWD | 19 | 5.5 | 3.26 | 10.05 | 16.42 | 2.00 | 75.1 | 83.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 3.17 | 9.49 | 16.56 | 9.00 | 65.5 | 72.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 8.69 | 21.85 | 34.24 | 2.00 | 128.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.33 | 19.04 | 31.86 | 6.00 | 89.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 5.67 | 17.13 | 29.04 | 10.00 | 79.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.44 | 13.50 | 21.84 | 5.00 | 82.7 | 90.0 |
| Bench 2 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.46 | 11.68 | 19.82 | 0.00 | 69.1 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.30
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 7.53, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 2.78 | 8.23 | 13.63 | 7.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.53 | 8.06 | 13.29 | 0.00 | 90.1 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.77 | 17.92 | 28.08 | 4.00 | 116.7 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.34 | 10.32 | 16.82 | 0.00 | 81.1 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 3.28 | 10.16 | 16.50 | 0.00 | 78.4 | 0.0 |
| XI | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.11 | 9.77 | 15.93 | 0.00 | 79.2 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 2.96 | 9.13 | 15.20 | 0.00 | 76.0 | 0.0 |
| XI | XI | Valentín Castellanos | FWD | 19 | 5.5 | 3.68 | 10.34 | 16.63 | 1.00 | 77.4 | 78.0 |
| XI | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 3.23 | 9.61 | 16.65 | 0.00 | 70.8 | 0.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.3 | 2.18 | 7.04 | 11.84 | 0.00 | 34.2 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.73 | 21.33 | 35.30 | 5.00 | 122.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 6.73 | 18.98 | 31.35 | 1.00 | 96.6 | 58.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 6.04 | 16.55 | 26.29 | 13.00 | 98.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.14 | 14.08 | 22.72 | 1.00 | 91.3 | 90.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 10.5 | 2.69 | 8.83 | 15.17 | 0.00 | 41.8 | 0.0 |
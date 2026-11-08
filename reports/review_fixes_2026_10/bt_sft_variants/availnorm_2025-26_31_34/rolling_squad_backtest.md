# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 255.01
- Total actual points: 256.00
- Average predicted points: 63.75
- Average actual points: 64.00
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
- Predicted score: 63.81
- Actual score: 55.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Adrien Truffert replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.63 | 9.08 | 14.19 | 3.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.34 | 9.03 | 14.53 | 6.00 | 89.3 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.84 | 16.38 | 25.82 | 3.00 | 113.9 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.81 | 14.08 | 21.37 | 0.00 | 111.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.44 | 12.30 | 19.34 | 1.00 | 95.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.87 | 10.99 | 17.80 | -1.00 | 85.6 | 90.0 |
| Bench 2 | Autosub In | Adrien Truffert | DEF | 4 | 4.6 | 3.82 | 10.87 | 17.71 | 4.00 | 85.9 | 90.0 |
| XI | XI | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 3.95 | 10.94 | 17.75 | 5.00 | 61.5 | 8.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.47 | 9.49 | 15.20 | 2.00 | 71.1 | 90.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 3.44 | 9.20 | 14.06 | 16.00 | 54.0 | 81.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.41 | 21.46 | 34.54 | 13.00 | 126.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 5.43 | 17.32 | 29.34 | 0.00 | 70.7 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.66 | 16.74 | 27.36 | 2.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.23 | 15.25 | 23.90 | 3.00 | 103.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 5.12 | 12.87 | 20.75 | 9.00 | 84.7 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 53.20
- Actual score: 58.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (14.54).
- Transfer: Raúl Jiménez Rodríguez -> Danny Welbeck (projected gain 0.96, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (14.54).
- Autosub: Bernd Leno replaced Emiliano Martínez Romero.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.22 | 7.04 | 11.76 | 0.00 | 78.3 | 0.0 |
| Bench 1 | Autosub In | Bernd Leno | GK | 10 | 4.9 | 1.85 | 6.22 | 10.54 | 2.00 | 70.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.25 | 10.54 | 17.51 | 9.00 | 71.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.26 | 9.74 | 15.42 | 3.00 | 95.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.93 | 9.36 | 15.37 | 4.00 | 81.9 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 2.71 | 8.73 | 14.44 | 4.00 | 82.2 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 1.99 | 7.61 | 12.97 | 2.00 | 39.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.2 | 4.13 | 10.78 | 16.93 | 2.00 | 77.4 | 74.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.26 | 9.58 | 14.72 | 2.00 | 80.2 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.99 | 8.82 | 14.32 | 7.00 | 59.6 | 73.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.03 | 18.44 | 29.81 | 4.00 | 106.9 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.0 | 4.86 | 15.00 | 25.97 | 8.00 | 48.7 | 89.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.38 | 13.69 | 22.67 | 4.00 | 83.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.83 | 11.80 | 19.09 | 5.00 | 77.5 | 90.0 |
| Bench 2 | Bench | Harry Wilson | MID | 10 | 6.0 | 2.89 | 9.87 | 16.69 | 2.00 | 53.2 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Danny Welbeck
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 76.93
- Actual score: 109.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.48) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.81, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.48) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 2.28 | 6.75 | 11.11 | 10.00 | 81.2 | 90.0 |
| Bench 1 | Bench Boost | Emiliano Martínez Romero | GK | 2 | 5.1 | 0.95 | 2.87 | 4.97 | 2.00 | 44.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 6.30 | 14.65 | 22.07 | 6.00 | 126.8 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.6 | 5.97 | 13.80 | 20.46 | 12.00 | 109.7 | 180.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.6 | 5.42 | 12.78 | 19.82 | 13.00 | 114.3 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 5.27 | 12.47 | 19.26 | 5.00 | 111.9 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 3.58 | 11.07 | 18.35 | 8.00 | 84.1 | 90.0 |
| Vice Captain | XI | Danny Welbeck | FWD | 6 | 6.2 | 6.33 | 14.32 | 21.64 | 8.00 | 90.2 | 81.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 5.96 | 14.04 | 20.48 | 8.00 | 114.5 | 180.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 2.73 | 8.16 | 14.24 | 9.00 | 52.5 | 72.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.47 | 18.79 | 29.44 | 2.00 | 129.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.44 | 16.37 | 27.39 | 6.00 | 88.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.88 | 14.73 | 24.97 | 10.00 | 74.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.82 | 11.61 | 18.78 | 5.00 | 78.7 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 3.07 | 9.72 | 15.96 | 3.00 | 64.3 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.60 -> 3.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.06
- Actual score: 34.00
- Transfer: Cole Palmer -> Morgan Gibbs-White (projected gain 7.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.79 | 8.25 | 13.67 | 7.00 | 80.4 | 90.0 |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.80 | 8.20 | 13.47 | 3.00 | 73.8 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.78 | 17.96 | 28.14 | 4.00 | 126.7 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.35 | 10.34 | 16.86 | 0.00 | 101.1 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.6 | 3.28 | 10.18 | 16.54 | 0.00 | 98.4 | 0.0 |
| XI | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.12 | 9.79 | 15.97 | 0.00 | 99.2 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 2.96 | 9.16 | 15.23 | 0.00 | 96.0 | 0.0 |
| XI | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.0 | 3.23 | 9.63 | 16.69 | 0.00 | 60.8 | 0.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 2.92 | 8.72 | 13.81 | 0.00 | 82.8 | 0.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.2 | 2.19 | 7.06 | 12.37 | 0.00 | 53.2 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.75 | 21.38 | 35.38 | 5.00 | 123.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 6.75 | 19.03 | 31.42 | 1.00 | 100.6 | 58.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 6.06 | 16.59 | 26.35 | 13.00 | 108.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.16 | 14.11 | 22.77 | 1.00 | 92.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 5.02 | 12.97 | 20.34 | 2.00 | 92.5 | 90.0 |
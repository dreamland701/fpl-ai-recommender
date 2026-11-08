# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 210.57
- Total actual points: 236.00
- Average predicted points: 52.64
- Average actual points: 59.00
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
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 56.23
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.93) beats the best remaining Triple Captain opportunity (13.28).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.93) beats the best remaining Triple Captain opportunity (13.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.33 | 9.84 | 15.03 | 2.00 | 94.6 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.1 | 2.91 | 8.61 | 14.15 | 3.00 | 93.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 3.53 | 11.07 | 16.87 | 1.00 | 97.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 3.16 | 9.46 | 15.58 | 9.00 | 87.6 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.04 | 9.29 | 14.24 | 2.00 | 93.2 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 2.84 | 8.37 | 14.12 | 14.00 | 77.7 | 69.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.5 | 2.65 | 7.91 | 13.09 | 2.00 | 87.3 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 3.04 | 8.55 | 13.14 | 2.00 | 70.2 | 90.0 |
| Bench 2 | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 2.77 | 7.70 | 12.58 | 6.00 | 72.9 | 69.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.9 | 2.12 | 6.90 | 11.93 | 1.00 | 69.2 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.16 | 20.40 | 34.51 | 6.00 | 107.3 | 84.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.7 | 4.71 | 13.77 | 23.02 | 4.00 | 77.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.6 | 3.66 | 11.89 | 20.23 | 2.00 | 92.5 | 81.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.13 | 11.55 | 17.20 | 6.00 | 88.1 | 84.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 3.32 | 11.38 | 19.56 | 9.00 | 70.9 | 90.0 |

## GW33

- Train rows: 156471
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Joško Gvardiol
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.08
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.20) beats the best remaining Bench Boost opportunity (10.05).
- Transfer: Matz Sels -> Nick Pope (projected gain 0.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.20) beats the best remaining Bench Boost opportunity (10.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.37 | 10.12 | 15.43 | 7.00 | 116.8 | 180.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 4.9 | 2.64 | 9.35 | 15.58 | 2.00 | 108.7 | 90.0 |
| Vice Captain | XI | Joško Gvardiol | DEF | 13 | 6.2 | 4.98 | 11.41 | 17.63 | 7.00 | 129.3 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 3.68 | 10.51 | 16.74 | 7.00 | 92.7 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.8 | 2.80 | 9.48 | 15.54 | 5.00 | 78.1 | 81.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 2.56 | 7.65 | 13.41 | 2.00 | 83.0 | 90.0 |
| Bench 3 | Bench Boost | Neco Williams | DEF | 16 | 4.5 | 2.14 | 6.81 | 11.60 | 2.00 | 86.0 | 90.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 3.15 | 9.59 | 15.18 | 2.00 | 67.0 | 90.0 |
| Bench 2 | Bench Boost | Jørgen Strand Larsen | FWD | 20 | 5.4 | 2.32 | 7.99 | 13.74 | 2.00 | 69.0 | 73.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.75 | 5.79 | 9.45 | 1.00 | 60.8 | 27.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 6.60 | 19.28 | 32.67 | 3.00 | 104.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 4.45 | 11.65 | 17.15 | 7.00 | 123.8 | 166.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 3.94 | 11.55 | 19.38 | 3.00 | 77.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 2.97 | 11.02 | 18.66 | 1.00 | 60.0 | 31.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.6 | 3.14 | 10.77 | 18.64 | 2.00 | 44.3 | 90.0 |

## GW34

- Train rows: 157270
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.68
- Actual score: 59.00
- Transfer: Nikola Milenković -> Milos Kerkez (projected gain 1.37, hit 0)
- Autosub: Neco Williams replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 15 | 4.9 | 3.21 | 8.77 | 13.92 | 6.00 | 99.6 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 2.71 | 8.66 | 14.48 | 0.00 | 81.2 | 0.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.9 | 5.51 | 12.88 | 19.30 | 11.00 | 94.2 | 76.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.5 | 4.06 | 11.42 | 18.52 | 2.00 | 96.2 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 5.3 | 3.58 | 10.14 | 16.85 | 2.00 | 96.1 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.2 | 2.78 | 9.51 | 15.71 | 0.00 | 80.8 | 0.0 |
| Bench 3 | Autosub In | Neco Williams | DEF | 16 | 4.5 | 2.48 | 6.97 | 11.41 | 0.00 | 86.5 | 90.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.4 | 3.64 | 9.15 | 14.48 | 6.00 | 76.3 | 76.0 |
| XI | XI | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 3.17 | 8.83 | 14.31 | 2.00 | 76.1 | 69.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 1.34 | 4.63 | 7.63 | 2.00 | 33.2 | 63.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.35 | 19.11 | 31.30 | 8.00 | 111.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.6 | 5.77 | 15.75 | 25.25 | 3.00 | 105.9 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 5.37 | 13.18 | 20.75 | 7.00 | 101.1 | 75.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.89 | 12.69 | 20.64 | 4.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Morgan Rogers | MID | 2 | 5.6 | 2.62 | 9.09 | 15.26 | 0.00 | 61.6 | 0.0 |

## GW35

- Train rows: 158070
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 40.58
- Actual score: 52.00
- Transfer: Morgan Rogers -> Jacob Murphy (projected gain 3.47, hit 0)
- Autosub: Francisco Evanilson de Lima Barbosa replaced Bruno Borges Fernandes.
- Autosub: Rayan Aït-Nouri replaced Luis Díaz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | 15 | 4.9 | 2.10 | 6.72 | 10.44 | 2.00 | 80.5 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 2.04 | 6.49 | 10.85 | 1.00 | 66.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.6 | 2.62 | 8.96 | 14.16 | 6.00 | 82.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.2 | 2.63 | 7.74 | 12.45 | 8.00 | 75.9 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 5.3 | 2.17 | 7.60 | 11.67 | 2.00 | 79.9 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.5 | 2.62 | 6.89 | 10.74 | 5.00 | 87.1 | 90.0 |
| Bench 4 | Autosub In | Rayan Aït-Nouri | DEF | 20 | 4.9 | 0.38 | 4.56 | 8.44 | 2.00 | 20.6 | 90.0 |
| Bench 2 | Bench | Jørgen Strand Larsen | FWD | 20 | 5.4 | 2.07 | 7.64 | 12.31 | 0.00 | 62.3 | 0.0 |
| Bench 3 | Autosub In | Francisco Evanilson de Lima Barbosa | FWD | 3 | 5.8 | 1.47 | 6.98 | 11.35 | 6.00 | 34.6 | 86.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 4.8 | 2.27 | 5.95 | 9.54 | 6.00 | 66.9 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 6.42 | 18.32 | 30.64 | 2.00 | 104.2 | 90.0 |
| Vice Captain | Bench | Bruno Borges Fernandes | MID | 14 | 8.5 | 3.86 | 12.40 | 19.40 | 0.00 | 75.9 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.5 | 3.36 | 11.68 | 18.27 | 10.00 | 72.0 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.3 | 3.31 | 10.44 | 16.37 | 1.00 | 59.4 | 55.0 |
| XI | Bench | Luis Díaz | MID | 12 | 7.5 | 2.81 | 10.27 | 15.84 | 0.00 | 60.2 | 0.0 |
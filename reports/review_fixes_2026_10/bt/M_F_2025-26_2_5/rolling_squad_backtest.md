# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 242.82
- Total actual points: 224.00
- Average predicted points: 60.70
- Average actual points: 56.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.27
- Actual score: 53.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Trafford replaced Marco Bizot.
- Autosub: Pedro Porro Sauceda replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Autosub In | James Trafford | GK | 13 | 5.0 | 3.29 | 10.40 | 17.37 | 2.00 | 84.6 | 90.0 |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 3.74 | 9.88 | 16.03 | 0.00 | 78.8 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 6.74 | 17.41 | 28.15 | 1.00 | 87.7 | 8.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.77 | 11.29 | 18.62 | 3.00 | 84.9 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.60 | 11.27 | 18.72 | 5.00 | 81.2 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 3.96 | 10.60 | 17.07 | 1.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.5 | 3.28 | 9.58 | 15.68 | 0.00 | 78.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.53 | 13.36 | 22.03 | 15.00 | 61.1 | 90.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.08 | 10.62 | 17.23 | 2.00 | 60.7 | 62.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.5 | 2.71 | 7.96 | 13.01 | 0.00 | 74.7 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.55 | 22.18 | 36.75 | 5.00 | 99.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.04 | 17.38 | 28.49 | 0.00 | 84.6 | 0.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 4.85 | 15.20 | 25.39 | 2.00 | 95.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.63 | 14.10 | 23.64 | 2.00 | 84.8 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.82 | 14.07 | 22.84 | 10.00 | 85.2 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.83
- Actual score: 55.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Trai Hume replaced Daniel Ballard.
- Autosub: Norberto Bercique Gomes Betuncal replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | James Trafford | GK | 13 | 5.0 | 2.66 | 8.52 | 14.07 | 2.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.36 | 4.14 | 7.15 | 0.00 | 29.4 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.91 | 11.39 | 18.53 | 4.00 | 79.9 | 70.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.41 | 10.44 | 17.07 | 8.00 | 84.2 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.5 | 3.75 | 9.68 | 15.80 | 0.00 | 38.0 | 0.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.5 | 2.77 | 8.22 | 13.93 | 0.00 | 78.1 | 0.0 |
| Bench 2 | Autosub In | Trai Hume | DEF | 17 | 4.5 | 2.84 | 8.10 | 13.37 | 2.00 | 75.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.69 | 14.02 | 22.96 | 9.00 | 76.7 | 90.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.88 | 8.33 | 13.73 | 2.00 | 52.9 | 64.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.5 | 2.20 | 6.51 | 10.93 | 7.00 | 42.2 | 75.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.74 | 21.08 | 34.80 | 3.00 | 99.7 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.03 | 15.26 | 24.73 | 10.00 | 80.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 4.03 | 13.09 | 19.95 | 2.00 | 74.1 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.16 | 12.86 | 21.44 | 0.00 | 38.4 | 0.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 3.82 | 11.81 | 19.44 | 3.00 | 84.5 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.71
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.48) beats the best remaining Triple Captain opportunity (9.17).
- Transfer: Cole Palmer -> Bryan Mbeumo (projected gain 6.78, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.48) beats the best remaining Triple Captain opportunity (9.17).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | James Trafford | GK | 13 | 5.0 | 2.74 | 8.08 | 13.47 | 0.00 | 82.7 | 0.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.93 | 5.56 | 9.29 | 0.00 | 60.9 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.19 | 11.10 | 17.79 | 6.00 | 71.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.77 | 10.92 | 17.88 | 8.00 | 85.1 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.91 | 7.74 | 12.82 | 6.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.5 | 2.36 | 6.01 | 10.62 | 0.00 | 24.0 | 0.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 1.59 | 4.84 | 8.86 | 0.00 | 35.5 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.61 | 16.24 | 25.58 | 7.00 | 78.5 | 78.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.4 | 2.91 | 8.22 | 13.74 | 2.00 | 55.7 | 74.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.70 | 7.63 | 12.86 | 0.00 | 52.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.45 | 21.06 | 34.57 | 9.00 | 92.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.45 | 14.47 | 24.06 | 2.00 | 81.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.74 | 14.28 | 23.42 | 2.00 | 77.4 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.78 | 12.96 | 20.66 | 3.00 | 76.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.24 | 12.13 | 19.72 | 3.00 | 81.2 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 2.40 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.01
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.33) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Aaron Wan-Bissaka -> Daniel Muñoz Mejía (projected gain 5.55, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.33) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | James Trafford | GK | 13 | 5.0 | 1.00 | 4.28 | 7.72 | 0.00 | 43.7 | 0.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 0.75 | 2.71 | 4.74 | 0.00 | 24.2 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.65 | 13.29 | 19.58 | 2.00 | 79.0 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.34 | 12.84 | 19.45 | 1.00 | 80.7 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.49 | 12.82 | 18.27 | 4.00 | 82.3 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 3.23 | 9.11 | 13.75 | 4.00 | 78.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.5 | 1.41 | 4.28 | 6.76 | 1.00 | 14.2 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.56 | 17.05 | 26.60 | 2.00 | 82.0 | 90.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.4 | 2.62 | 7.94 | 12.90 | 1.00 | 51.5 | 45.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.51 | 4.78 | 7.89 | 1.00 | 25.5 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.01 | 21.00 | 33.80 | 5.00 | 92.7 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.58 | 15.73 | 23.46 | 10.00 | 82.6 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.85 | 14.44 | 23.03 | 3.00 | 75.8 | 69.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.6 | 4.41 | 13.13 | 20.14 | 2.00 | 71.1 | 60.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.58 | 11.67 | 18.50 | 9.00 | 77.8 | 90.0 |
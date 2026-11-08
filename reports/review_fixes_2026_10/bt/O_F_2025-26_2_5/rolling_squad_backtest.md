# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 242.24
- Total actual points: 224.00
- Average predicted points: 60.56
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
- Predicted score: 62.28
- Actual score: 53.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Trafford replaced Marco Bizot.
- Autosub outfielders: Pedro Porro Sauceda.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Autosub In | James Trafford | GK | 13 | 5.0 | 3.32 | 10.41 | 17.24 | 2.00 | 84.6 | 90.0 |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 3.71 | 9.86 | 15.88 | 0.00 | 78.8 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 6.71 | 17.43 | 28.07 | 1.00 | 87.7 | 8.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.78 | 11.26 | 18.44 | 3.00 | 84.9 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.61 | 11.20 | 18.48 | 5.00 | 81.2 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 3.93 | 10.54 | 16.87 | 1.00 | 74.2 | 90.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.5 | 3.27 | 9.52 | 15.47 | 0.00 | 78.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.55 | 13.34 | 21.85 | 15.00 | 61.1 | 90.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.05 | 10.52 | 16.96 | 2.00 | 60.7 | 62.0 |
| Bench 4 | Bench | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.5 | 2.69 | 7.89 | 12.79 | 0.00 | 74.7 | 26.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.57 | 22.15 | 36.56 | 5.00 | 99.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.07 | 17.38 | 28.34 | 0.00 | 84.6 | 0.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 4.88 | 15.26 | 25.34 | 2.00 | 95.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.64 | 14.05 | 23.44 | 2.00 | 84.8 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.83 | 13.98 | 22.56 | 10.00 | 85.2 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.54
- Actual score: 55.00
- Transfer: none
- No transfer was applied this week.
- Autosub outfielders: Trai Hume, Norberto Bercique Gomes Betuncal.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | James Trafford | GK | 13 | 5.0 | 2.64 | 8.59 | 14.05 | 2.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.35 | 4.23 | 7.17 | 0.00 | 29.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.38 | 13.10 | 19.56 | 8.00 | 84.3 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.88 | 11.90 | 18.81 | 4.00 | 79.9 | 70.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.6 | 3.73 | 10.88 | 16.88 | 0.00 | 38.1 | 0.0 |
| Bench 3 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.5 | 2.80 | 8.80 | 14.36 | 0.00 | 78.0 | 0.0 |
| Bench 2 | Autosub In | Trai Hume | DEF | 17 | 4.5 | 2.82 | 8.58 | 13.65 | 2.00 | 75.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.68 | 14.39 | 23.15 | 9.00 | 76.8 | 90.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.86 | 8.59 | 13.82 | 2.00 | 53.0 | 64.0 |
| Bench 4 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.5 | 2.23 | 6.95 | 11.27 | 7.00 | 42.1 | 75.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.71 | 21.77 | 35.28 | 3.00 | 99.8 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.99 | 16.80 | 25.96 | 10.00 | 80.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.01 | 13.58 | 20.29 | 2.00 | 74.1 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.16 | 13.23 | 21.65 | 0.00 | 38.4 | 0.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 3.79 | 12.67 | 20.06 | 3.00 | 84.5 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.55
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.45) beats the best remaining Triple Captain opportunity (9.13).
- Transfer: Cole Palmer -> Bryan Mbeumo (projected gain 6.93, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.45) beats the best remaining Triple Captain opportunity (9.13).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | James Trafford | GK | 13 | 5.0 | 2.75 | 8.20 | 13.45 | 0.00 | 82.7 | 0.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.93 | 5.71 | 9.33 | 0.00 | 61.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.73 | 13.34 | 20.28 | 8.00 | 85.1 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.22 | 12.37 | 18.98 | 6.00 | 71.2 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.90 | 8.47 | 13.41 | 6.00 | 76.1 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.35 | 6.98 | 11.54 | 0.00 | 24.0 | 0.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 1.62 | 5.32 | 9.26 | 0.00 | 35.5 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.59 | 16.89 | 25.99 | 7.00 | 78.5 | 78.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.4 | 2.87 | 8.46 | 13.78 | 2.00 | 55.7 | 74.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.69 | 7.86 | 12.91 | 0.00 | 52.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.42 | 21.52 | 34.81 | 9.00 | 92.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.46 | 16.78 | 26.36 | 2.00 | 81.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.75 | 14.65 | 23.64 | 2.00 | 77.3 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.6 | 4.75 | 13.75 | 21.28 | 3.00 | 76.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.25 | 12.76 | 20.24 | 3.00 | 81.2 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 2.40 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.86
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.30) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Aaron Wan-Bissaka -> Daniel Muñoz Mejía (projected gain 5.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.30) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | James Trafford | GK | 13 | 5.0 | 0.97 | 4.18 | 7.66 | 0.00 | 43.8 | 0.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 0.77 | 2.69 | 4.82 | 0.00 | 24.1 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.68 | 13.39 | 20.70 | 2.00 | 78.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.49 | 13.03 | 20.34 | 4.00 | 82.3 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.33 | 12.98 | 20.77 | 1.00 | 80.7 | 88.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 3.19 | 8.98 | 14.40 | 4.00 | 79.0 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.38 | 4.30 | 7.17 | 1.00 | 14.3 | 53.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.57 | 16.95 | 27.26 | 2.00 | 81.9 | 90.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 9 | 5.4 | 2.63 | 7.89 | 13.15 | 1.00 | 51.5 | 45.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.48 | 4.66 | 7.93 | 1.00 | 25.6 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.01 | 20.82 | 33.99 | 5.00 | 92.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.57 | 16.12 | 25.87 | 10.00 | 82.6 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.84 | 14.31 | 23.25 | 3.00 | 75.8 | 69.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.7 | 4.40 | 12.94 | 20.70 | 2.00 | 71.1 | 60.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.55 | 11.56 | 19.16 | 9.00 | 77.9 | 90.0 |
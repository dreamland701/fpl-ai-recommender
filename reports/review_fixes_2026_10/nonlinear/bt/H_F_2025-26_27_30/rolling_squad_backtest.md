# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 248.49
- Total actual points: 216.00
- Average predicted points: 62.12
- Average actual points: 54.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW27

- Train rows: 181084
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Declan Rice
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 63.95
- Actual score: 32.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.9 | 3.45 | 11.82 | 18.72 | 1.00 | 89.5 | 90.0 |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.51 | 10.86 | 18.74 | 2.00 | 81.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.95 | 15.31 | 20.81 | 2.00 | 85.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 5.26 | 13.92 | 20.21 | 3.00 | 82.1 | 56.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.65 | 12.88 | 19.49 | 2.00 | 85.7 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.8 | 4.95 | 12.80 | 21.25 | 2.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.91 | 10.75 | 19.59 | 11.00 | 85.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.29 | 13.26 | 22.45 | 2.00 | 85.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 4.58 | 12.49 | 23.20 | 4.00 | 82.1 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.38 | 12.00 | 18.17 | 2.00 | 81.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 7.46 | 19.57 | 33.20 | 3.00 | 81.3 | 74.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.6 | 6.32 | 17.29 | 22.26 | 4.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Antoine Semenyo | MID | 13 | 8.0 | 3.66 | 13.93 | 23.49 | 4.00 | 87.3 | 86.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.79 | 13.71 | 22.20 | 2.00 | 86.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.7 | 4.00 | 13.52 | 23.56 | 3.00 | 70.4 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Dominik Szoboszlai
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Dominik Szoboszlai
- Chip used: none
- Predicted score: 55.19
- Actual score: 57.00
- Transfer: Virgil van Dijk -> Joachim Andersen (projected gain 2.60, hit 0)
- Autosub: Mateus Mané replaced Joachim Andersen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.08 | 10.69 | 16.95 | 2.00 | 84.7 | 90.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.9 | 3.05 | 10.58 | 19.28 | 2.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.72 | 16.04 | 24.25 | 9.00 | 86.6 | 90.0 |
| XI | Bench | Joachim Andersen | DEF | 10 | 4.5 | 4.02 | 11.97 | 18.07 | 0.00 | 86.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 3.98 | 11.24 | 18.12 | 6.00 | 83.5 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.20 | 10.34 | 13.37 | 8.00 | 59.7 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.7 | 1.91 | 9.92 | 15.36 | 1.00 | 69.8 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.45 | 12.73 | 22.34 | 6.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.6 | 3.56 | 11.07 | 23.33 | 7.00 | 81.0 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.6 | 3.66 | 10.50 | 16.32 | 2.00 | 84.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.03 | 15.27 | 27.85 | 1.00 | 68.5 | 85.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 5.16 | 15.21 | 22.58 | 5.00 | 81.9 | 75.0 |
| Captain | Captain | Dominik Szoboszlai | MID | 12 | 6.7 | 5.61 | 14.68 | 23.57 | 4.00 | 85.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.77 | 13.32 | 21.43 | 2.00 | 85.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.60 | 11.65 | 20.67 | 8.00 | 86.5 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 1.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bryan Mbeumo
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 61.92
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (7.74).
- Transfer: Declan Rice -> Bryan Mbeumo (projected gain 4.26, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.56) beats the best remaining Triple Captain opportunity (7.74).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.41 | 10.84 | 18.04 | 0.00 | 88.8 | 0.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.9 | 3.22 | 10.53 | 19.33 | 0.00 | 89.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.58 | 12.18 | 21.35 | 11.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.6 | 3.66 | 10.47 | 16.85 | 2.00 | 86.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.07 | 10.39 | 20.89 | 1.00 | 84.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.93 | 10.21 | 16.32 | 13.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Joachim Andersen | DEF | 10 | 4.5 | 3.40 | 8.22 | 13.75 | 0.00 | 71.7 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.81 | 14.16 | 21.78 | 4.00 | 85.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.55 | 12.37 | 23.38 | 2.00 | 86.5 | 90.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.71 | 10.17 | 18.58 | 2.00 | 78.4 | 69.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.11 | 15.83 | 25.40 | 9.00 | 72.2 | 84.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.8 | 4.58 | 15.55 | 23.07 | 5.00 | 82.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.68 | 14.42 | 22.85 | 1.00 | 78.1 | 76.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.56 | 14.09 | 19.05 | 7.00 | 86.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.51 | 12.44 | 22.06 | 1.00 | 74.1 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 67.44
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.48) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Robin Roefs -> Caoimhín Kelleher (projected gain 5.74, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.48) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 4.10 | 11.67 | 16.78 | 1.00 | 85.8 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 1.74 | 5.99 | 12.11 | 3.00 | 57.5 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 3.98 | 11.86 | 18.89 | 2.00 | 84.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.00 | 11.47 | 17.24 | 1.00 | 80.8 | 37.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.09 | 11.47 | 21.67 | 9.00 | 87.5 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 13 | 5.2 | 3.80 | 10.83 | 17.09 | 2.00 | 84.1 | 90.0 |
| Bench 4 | Bench Boost | Joachim Andersen | DEF | 10 | 4.5 | 2.19 | 7.19 | 11.11 | 7.00 | 65.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.46 | 13.50 | 23.27 | 6.00 | 86.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.91 | 12.91 | 22.70 | 6.00 | 82.2 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.74 | 7.77 | 13.48 | 1.00 | 57.2 | 45.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 5.68 | 18.82 | 30.65 | 2.00 | 78.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.8 | 4.98 | 14.15 | 22.54 | 11.00 | 86.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.57 | 13.53 | 19.48 | 2.00 | 81.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.39 | 12.43 | 23.23 | 2.00 | 86.4 | 74.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.12 | 11.82 | 21.45 | 2.00 | 74.5 | 74.0 |
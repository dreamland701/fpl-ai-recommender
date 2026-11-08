# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 255.36
- Total actual points: 246.00
- Average predicted points: 63.84
- Average actual points: 61.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW13 are included before the first simulated week.
- League-average scores were not available for this run.

## GW14

- Train rows: 170850
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Mohamed Salah
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.68
- Actual score: 53.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.15 | 11.53 | 18.38 | 6.00 | 93.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.52 | 9.80 | 15.80 | 1.00 | 86.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.92 | 13.52 | 21.22 | 1.00 | 92.9 | 46.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.65 | 13.06 | 20.51 | 14.00 | 86.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.58 | 12.86 | 20.57 | 1.00 | 89.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.38 | 11.71 | 19.14 | 14.00 | 82.6 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 4.32 | 11.66 | 19.07 | 8.00 | 84.4 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.6 | 3.59 | 11.99 | 19.69 | 1.00 | 69.4 | 23.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.30 | 10.31 | 17.65 | 2.00 | 54.3 | 60.0 |
| Bench 4 | Bench | Zian Flemming | FWD | 3 | 5.3 | 2.90 | 9.17 | 14.55 | 1.00 | 72.8 | 58.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.1 | 5.85 | 18.70 | 32.43 | 1.00 | 62.7 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.15 | 17.21 | 27.48 | 4.00 | 100.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.78 | 16.21 | 26.12 | 2.00 | 89.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.56 | 15.78 | 25.68 | 3.00 | 90.3 | 82.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.93 | 12.98 | 20.76 | 2.00 | 89.2 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.29
- Actual score: 82.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Maxence Lacroix replaced Daniel Muñoz Mejía.
- Autosub: Zian Flemming replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.92 | 11.42 | 18.41 | 2.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.86 | 8.71 | 14.36 | 10.00 | 81.7 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.92 | 14.44 | 22.97 | 0.00 | 93.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.60 | 13.24 | 20.61 | 8.00 | 91.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.04 | 12.33 | 20.21 | 3.00 | 75.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.98 | 11.97 | 19.64 | 6.00 | 84.7 | 90.0 |
| Bench 2 | Autosub In | Maxence Lacroix | DEF | 8 | 5.1 | 3.85 | 11.56 | 18.43 | 2.00 | 85.9 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.6 | 4.07 | 12.12 | 20.69 | 2.00 | 36.5 | 90.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 3.62 | 10.22 | 16.23 | 0.00 | 63.5 | 0.0 |
| Bench 4 | Autosub In | Zian Flemming | FWD | 3 | 5.3 | 3.08 | 8.76 | 14.62 | 5.00 | 60.4 | 4.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 14.1 | 5.94 | 18.13 | 31.54 | 0.00 | 74.0 | 0.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.73 | 16.04 | 26.40 | 18.00 | 91.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.12 | 14.43 | 24.12 | 8.00 | 79.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.06 | 13.08 | 22.87 | 6.00 | 72.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.97 | 12.30 | 20.02 | 4.00 | 76.8 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Declan Rice
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 68.80
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.86) beats the best remaining Triple Captain opportunity (8.57).
- Transfer: Daniel Muñoz Mejía -> Matty Cash (projected gain 3.55, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (7.86) beats the best remaining Triple Captain opportunity (8.57).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 5.04 | 12.76 | 20.08 | 2.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.14 | 9.26 | 15.23 | 6.00 | 88.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 4.91 | 13.83 | 21.92 | 1.00 | 98.4 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 4.9 | 5.22 | 13.71 | 21.43 | 0.00 | 108.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.24 | 12.61 | 20.43 | 6.00 | 92.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.39 | 11.87 | 19.41 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 3.45 | 10.37 | 17.28 | 1.00 | 84.8 | 90.0 |
| XI | XI | Zian Flemming | FWD | 3 | 5.3 | 3.37 | 10.09 | 17.14 | 1.00 | 60.2 | 28.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.5 | 3.08 | 9.99 | 17.16 | 1.00 | 61.1 | 8.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.22 | 4.52 | 8.54 | 5.00 | 23.1 | 12.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 7.86 | 20.57 | 33.61 | 13.00 | 116.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 4.80 | 15.75 | 27.95 | 7.00 | 25.1 | 64.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 5.42 | 14.45 | 23.96 | 2.00 | 85.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.23 | 12.29 | 19.97 | 3.00 | 76.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 3.59 | 11.22 | 19.93 | 2.00 | 56.6 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bruno Borges Fernandes
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 69.60
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.64) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 9.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.64) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.50 | 10.42 | 16.84 | 7.00 | 82.6 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.81 | 8.80 | 14.64 | 4.00 | 83.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 4.87 | 13.29 | 20.91 | 1.00 | 93.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 11.85 | 19.30 | 1.00 | 86.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.02 | 11.66 | 19.28 | 6.00 | 79.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.76 | 10.96 | 17.77 | 1.00 | 85.0 | 90.0 |
| Bench 2 | Bench Boost | Matty Cash | DEF | 2 | 4.9 | 3.06 | 9.86 | 15.51 | 2.00 | 41.0 | 90.0 |
| XI | XI | Zian Flemming | FWD | 3 | 5.3 | 3.13 | 9.80 | 16.72 | 1.00 | 58.0 | 64.0 |
| Bench 3 | Bench Boost | Danny Welbeck | FWD | 6 | 6.5 | 2.89 | 8.88 | 16.10 | 0.00 | 15.3 | 0.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 2.88 | 7.51 | 12.93 | 1.00 | 17.3 | 26.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 6.28 | 19.16 | 31.14 | 1.00 | 88.8 | 45.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 6.81 | 19.03 | 29.36 | 3.00 | 81.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 6.17 | 18.40 | 31.17 | 0.00 | 73.7 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.76 | 14.40 | 23.39 | 11.00 | 78.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.89 | 12.05 | 19.30 | 4.00 | 77.5 | 90.0 |
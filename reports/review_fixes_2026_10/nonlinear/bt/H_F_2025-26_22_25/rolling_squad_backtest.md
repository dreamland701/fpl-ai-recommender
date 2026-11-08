# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 238.05
- Total actual points: 255.00
- Average predicted points: 59.51
- Average actual points: 63.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW21 are included before the first simulated week.
- League-average scores were not available for this run.

## GW22

- Train rows: 177037
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Declan Rice
- Vice captain: Ollie Watkins
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 56.78
- Actual score: 49.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Trevoh Chalobah replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.9 | 3.70 | 11.45 | 17.54 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 3.15 | 9.98 | 19.67 | 10.00 | 87.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.72 | 13.57 | 19.04 | 8.00 | 81.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.68 | 13.32 | 20.15 | 8.00 | 83.9 | 90.0 |
| Bench 3 | Autosub In | Trevoh Chalobah | DEF | 7 | 5.5 | 3.86 | 11.83 | 19.35 | 8.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.54 | 10.98 | 19.45 | 3.00 | 85.5 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.02 | 10.51 | 19.20 | 0.00 | 89.2 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.75 | 14.49 | 18.77 | 2.00 | 83.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.10 | 13.20 | 23.11 | 2.00 | 80.6 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.01 | 12.82 | 22.39 | 2.00 | 79.8 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.3 | 5.31 | 17.67 | 25.81 | 3.00 | 82.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.30 | 14.31 | 21.96 | 2.00 | 85.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.6 | 4.83 | 14.21 | 22.67 | 0.00 | 80.6 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.06 | 14.15 | 21.37 | 10.00 | 78.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 5.01 | 13.51 | 23.19 | 1.00 | 70.9 | 33.0 |

## GW23

- Train rows: 177836
- Bank: 0.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Declan Rice
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 55.71
- Actual score: 50.00
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 4.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 4.36 | 12.07 | 19.22 | 3.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.9 | 3.54 | 10.71 | 16.69 | 1.00 | 89.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 5.05 | 13.02 | 22.70 | 11.00 | 84.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.62 | 12.73 | 20.33 | 1.00 | 83.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.21 | 11.88 | 19.33 | 3.00 | 86.3 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 4.62 | 11.17 | 17.61 | 4.00 | 86.1 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 2.13 | 8.77 | 14.38 | 6.00 | 51.1 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.31 | 12.37 | 18.28 | 2.00 | 84.7 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.88 | 11.56 | 17.46 | 2.00 | 80.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.07 | 11.45 | 18.30 | 8.00 | 75.7 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.3 | 5.12 | 15.62 | 23.57 | 1.00 | 87.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.3 | 4.15 | 15.25 | 24.28 | 5.00 | 81.5 | 90.0 |
| Bench 2 | Bench | Florian Wirtz | MID | 12 | 8.2 | 3.79 | 14.00 | 20.75 | 2.00 | 80.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.01 | 12.96 | 20.74 | 8.00 | 88.1 | 90.0 |
| Bench 3 | Bench | Dominik Szoboszlai | MID | 12 | 6.6 | 3.69 | 12.11 | 20.88 | 13.00 | 78.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 1.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 59.59
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.45) beats the best remaining Triple Captain opportunity (6.69).
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Cristian Romero -> James Tarkowski (projected gain 3.12, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.45) beats the best remaining Triple Captain opportunity (6.69).
- Autosub: Igor Thiago Nascimento Rodrigues replaced Ollie Watkins.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.9 | 3.53 | 11.36 | 20.42 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.6 | 3.32 | 10.47 | 19.02 | 2.00 | 88.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 3.64 | 13.85 | 21.04 | 2.00 | 85.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.24 | 13.63 | 23.61 | 8.00 | 83.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.62 | 13.35 | 18.59 | 3.00 | 87.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.59 | 12.85 | 19.80 | 8.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 3.54 | 10.78 | 16.93 | 3.00 | 84.6 | 90.0 |
| Bench 3 | Autosub In | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.10 | 12.70 | 22.60 | 2.00 | 78.2 | 90.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.8 | 4.07 | 10.78 | 19.29 | 0.00 | 81.0 | 0.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 2.99 | 10.11 | 16.81 | 2.00 | 73.3 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.4 | 5.45 | 15.84 | 22.19 | 10.00 | 83.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.97 | 15.67 | 26.77 | 3.00 | 85.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.6 | 4.45 | 14.03 | 20.16 | 5.00 | 86.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.04 | 13.48 | 20.86 | 7.00 | 87.5 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.07 | 12.08 | 19.80 | 12.00 | 80.9 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 0.30 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Declan Rice
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.97
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.93) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: James Tarkowski -> Nikola Milenković (projected gain 2.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.93) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Robin Roefs | GK | 17 | 4.9 | 2.64 | 11.31 | 19.04 | 1.00 | 88.8 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.6 | 3.57 | 10.69 | 18.99 | 2.00 | 88.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.83 | 13.44 | 20.39 | 2.00 | 87.5 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.43 | 13.12 | 19.67 | 4.00 | 85.9 | 90.0 |
| Bench 3 | Bench Boost | Marc Guéhi | DEF | 8 | 5.2 | 3.16 | 12.78 | 19.03 | 3.00 | 80.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.94 | 12.13 | 20.21 | 6.00 | 83.6 | 90.0 |
| Bench 2 | Bench Boost | Nikola Milenković | DEF | 16 | 5.1 | 3.70 | 11.30 | 17.02 | 1.00 | 86.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.82 | 13.32 | 17.81 | 5.00 | 76.7 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.96 | 10.67 | 16.56 | 7.00 | 76.5 | 90.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.7 | 1.43 | 5.19 | 9.22 | 2.00 | 33.2 | 85.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.5 | 5.49 | 15.69 | 22.39 | 10.00 | 85.9 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.22 | 14.83 | 25.56 | 5.00 | 85.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.6 | 3.93 | 13.50 | 21.78 | 8.00 | 86.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.57 | 13.36 | 21.40 | 2.00 | 81.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.81 | 12.14 | 20.21 | 2.00 | 87.4 | 90.0 |
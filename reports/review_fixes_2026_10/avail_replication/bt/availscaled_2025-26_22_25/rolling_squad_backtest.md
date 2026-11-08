# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 262.18
- Total actual points: 258.00
- Average predicted points: 65.55
- Average actual points: 64.50
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 61.29
- Actual score: 47.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Tarkowski replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 11.18 | 18.17 | 6.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.39 | 9.87 | 16.10 | 1.00 | 87.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.60 | 14.94 | 21.51 | 8.00 | 90.1 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.54 | 12.85 | 20.66 | 0.00 | 93.4 | 0.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.7 | 4.19 | 12.56 | 19.85 | 8.00 | 85.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.51 | 12.02 | 19.38 | 2.00 | 92.4 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 4.13 | 11.61 | 19.60 | 1.00 | 83.9 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.87 | 15.34 | 24.21 | 2.00 | 69.7 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.35 | 13.27 | 20.90 | 2.00 | 82.3 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.1 | 3.63 | 12.96 | 22.22 | 8.00 | 57.4 | 73.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 5.36 | 16.06 | 27.57 | 1.00 | 53.5 | 33.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.85 | 15.79 | 25.15 | 3.00 | 99.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.41 | 15.77 | 25.40 | 2.00 | 97.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.63 | 15.63 | 25.38 | 10.00 | 83.5 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.47 | 14.03 | 23.32 | 1.00 | 61.9 | 45.0 |

## GW23

- Train rows: 177836
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Antoine Semenyo
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 59.33
- Actual score: 51.00
- Transfer: Nathan Collins -> Trevoh Chalobah (projected gain 1.63, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.98 | 11.25 | 18.19 | 1.00 | 91.5 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.22 | 9.41 | 15.56 | 1.00 | 85.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.94 | 13.36 | 21.62 | 4.00 | 91.4 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.56 | 12.48 | 19.29 | 4.00 | 96.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.77 | 11.21 | 18.36 | 9.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 3.54 | 9.77 | 16.91 | 6.00 | 30.5 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 3.35 | 9.62 | 14.42 | 1.00 | 60.2 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.99 | 15.84 | 25.15 | 2.00 | 73.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.1 | 4.34 | 13.14 | 21.56 | 12.00 | 57.4 | 84.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.86 | 11.74 | 18.57 | 2.00 | 78.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.07 | 16.28 | 28.48 | 2.00 | 42.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.75 | 15.71 | 25.01 | 8.00 | 96.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.50 | 15.61 | 25.61 | 2.00 | 85.4 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.7 | 4.93 | 14.01 | 23.93 | 3.00 | 55.5 | 72.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.52 | 13.37 | 21.97 | 0.00 | 75.6 | 0.0 |

## GW24

- Train rows: 178639
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: triple_captain
- Predicted score: 66.55
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.22) beats the best remaining Triple Captain opportunity (7.90).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 2.52, hit 0)
- Chip used: Triple Captain on João Pedro Junqueira de Jesus. Optimizer chose Triple Captain here because the current estimated captain upside (6.22) beats the best remaining Triple Captain opportunity (7.90).
- Autosub: James Tarkowski replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.01 | 11.27 | 18.17 | 6.00 | 92.5 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 2.73 | 8.68 | 14.58 | 10.00 | 84.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.13 | 14.45 | 22.84 | 8.00 | 94.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.94 | 13.04 | 20.19 | 3.00 | 97.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.31 | 12.37 | 19.88 | 4.00 | 91.1 | 90.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.7 | 4.13 | 12.30 | 20.17 | 2.00 | 85.3 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 4.05 | 11.54 | 18.87 | 3.00 | 81.8 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 6.22 | 15.71 | 24.57 | 10.00 | 107.1 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.27 | 13.45 | 21.85 | 2.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.71 | 10.85 | 17.75 | 2.00 | 77.4 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.94 | 16.76 | 26.85 | 7.00 | 100.4 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.0 | 4.93 | 15.44 | 25.77 | 0.00 | 70.1 | 0.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.65 | 14.74 | 23.53 | 8.00 | 93.5 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.56 | 14.04 | 23.71 | 12.00 | 74.3 | 86.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 4.14 | 12.98 | 22.40 | 8.00 | 61.7 | 68.0 |

## GW25

- Train rows: 179450
- Bank: 0.50 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 75.01
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.03) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 7.65, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.03) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.36 | 11.89 | 18.91 | 7.00 | 90.4 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.6 | 3.07 | 9.22 | 15.19 | 1.00 | 83.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.57 | 15.20 | 24.03 | 6.00 | 92.4 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.49 | 12.46 | 19.54 | 4.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 12.20 | 19.30 | 0.00 | 89.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.15 | 12.04 | 19.79 | 2.00 | 84.6 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.2 | 3.77 | 11.12 | 18.32 | 3.00 | 77.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 5.59 | 15.62 | 24.34 | 8.00 | 78.5 | 74.0 |
| Bench 3 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.70 | 12.64 | 20.98 | 5.00 | 68.5 | 90.0 |
| Bench 4 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.49 | 10.55 | 17.76 | 7.00 | 72.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.7 | 6.50 | 17.85 | 26.80 | 10.00 | 87.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.40 | 15.89 | 25.92 | 2.00 | 94.6 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.16 | 15.57 | 25.84 | 2.00 | 88.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.12 | 14.74 | 23.56 | 2.00 | 84.3 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 4.00 | 12.52 | 20.89 | 1.00 | 67.5 | 29.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 213.82
- Total actual points: 235.00
- Average predicted points: 53.46
- Average actual points: 58.75
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
- Bank: 100.00 -> 2.60
- Free transfers: 1 -> 2
- Captain: Bruno Guimarães Rodriguez Moura
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Guimarães Rodriguez Moura
- Chip used: none
- Predicted score: 51.41
- Actual score: 50.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.22 | 9.70 | 15.46 | 6.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Alisson Becker | GK | 12 | 5.4 | 3.02 | 8.46 | 13.99 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.71 | 12.78 | 17.70 | 8.00 | 90.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.69 | 11.06 | 16.95 | 8.00 | 85.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.71 | 10.82 | 17.18 | 2.00 | 92.4 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 8 | 5.3 | 3.24 | 10.55 | 19.26 | 0.00 | 93.4 | 0.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 3.74 | 10.16 | 16.78 | 1.00 | 83.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.47 | 13.24 | 20.31 | 2.00 | 69.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.80 | 12.45 | 19.15 | 2.00 | 77.7 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.31 | 11.44 | 17.55 | 2.00 | 82.3 | 90.0 |
| Captain | Captain | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.35 | 14.79 | 24.15 | 3.00 | 99.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.31 | 13.47 | 21.10 | 2.00 | 97.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.70 | 13.36 | 21.27 | 10.00 | 83.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.36 | 12.91 | 21.00 | 3.00 | 87.2 | 90.0 |
| Bench 2 | Bench | James Garner | MID | 9 | 5.2 | 3.52 | 11.26 | 18.63 | 4.00 | 87.1 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 2.60 -> 3.80
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Antoine Semenyo
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 48.92
- Actual score: 44.00
- Transfer: Gabriel dos Santos Magalhães -> Trevoh Chalobah (projected gain 1.91, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.26 | 9.59 | 15.58 | 1.00 | 91.5 | 90.0 |
| Bench 1 | Bench | Alisson Becker | GK | 12 | 5.4 | 2.43 | 6.83 | 11.26 | 1.00 | 81.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 3.76 | 11.28 | 16.99 | 4.00 | 96.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.64 | 10.86 | 17.62 | 4.00 | 91.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.05 | 9.87 | 16.20 | 9.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.73 | 8.21 | 13.91 | 1.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 2.02 | 5.49 | 9.18 | 6.00 | 30.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.57 | 11.85 | 19.67 | 8.00 | 77.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.39 | 11.84 | 19.15 | 2.00 | 73.4 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 2.94 | 10.05 | 15.20 | 2.00 | 78.0 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.3 | 4.94 | 13.99 | 21.96 | 1.00 | 93.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.55 | 13.71 | 23.91 | 8.00 | 96.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.30 | 13.28 | 21.65 | 2.00 | 85.4 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 4.41 | 12.88 | 19.80 | 2.00 | 90.8 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.12 | 11.97 | 19.87 | 0.00 | 75.6 | 0.0 |

## GW24

- Train rows: 178639
- Bank: 3.80 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 54.78
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.93) beats the best remaining Triple Captain opportunity (7.28).
- Transfer: Bruno Guimarães Rodriguez Moura -> Bruno Borges Fernandes (projected gain 7.98, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.93) beats the best remaining Triple Captain opportunity (7.28).
- Autosub: Marc Guéhi replaced Ollie Watkins.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 2.99 | 8.71 | 14.77 | 6.00 | 92.5 | 90.0 |
| Bench 1 | Bench | Alisson Becker | GK | 12 | 5.4 | 2.52 | 7.31 | 12.65 | 2.00 | 83.9 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 4.44 | 11.84 | 18.19 | 3.00 | 97.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.64 | 10.84 | 17.54 | 2.00 | 85.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.01 | 9.87 | 16.48 | 4.00 | 91.1 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 8 | 5.2 | 2.83 | 8.60 | 14.63 | 3.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.37 | 8.08 | 13.95 | 1.00 | 81.0 | 30.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.8 | 3.49 | 11.55 | 19.15 | 0.00 | 77.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 2.97 | 10.55 | 20.55 | 2.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 2.79 | 8.32 | 13.41 | 2.00 | 77.4 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.5 | 5.93 | 15.53 | 23.16 | 10.00 | 109.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.94 | 14.76 | 25.25 | 7.00 | 100.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.42 | 13.35 | 24.16 | 3.00 | 94.3 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 3.73 | 12.02 | 19.90 | 12.00 | 74.3 | 86.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 3.36 | 10.53 | 16.55 | 4.00 | 83.8 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 1.50 -> 2.70
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Bruno Borges Fernandes
- Effective captain: Declan Rice
- Chip used: bench_boost
- Predicted score: 58.71
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.80) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Ollie Watkins -> João Pedro Junqueira de Jesus (projected gain 4.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.80) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.79 | 10.29 | 16.28 | 7.00 | 90.4 | 90.0 |
| Bench 1 | Bench Boost | Alisson Becker | GK | 12 | 5.4 | 2.45 | 7.20 | 11.83 | 1.00 | 82.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.6 | 3.64 | 10.83 | 16.94 | 4.00 | 88.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.36 | 10.69 | 16.97 | 2.00 | 84.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.25 | 10.40 | 16.60 | 0.00 | 89.6 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 8 | 5.2 | 2.55 | 7.77 | 12.65 | 3.00 | 77.6 | 90.0 |
| Bench 4 | Bench Boost | Nathan Collins | DEF | 5 | 5.0 | 2.35 | 7.00 | 11.97 | 0.00 | 69.1 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.45 | 12.53 | 19.25 | 8.00 | 78.5 | 74.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 2.86 | 10.54 | 17.95 | 5.00 | 68.5 | 90.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 2.46 | 8.04 | 14.56 | 7.00 | 72.7 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.4 | 5.33 | 15.12 | 23.84 | 5.00 | 92.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.6 | 5.00 | 13.95 | 20.85 | 10.00 | 87.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.10 | 13.59 | 21.52 | 2.00 | 94.6 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.00 | 13.09 | 23.85 | 2.00 | 88.1 | 90.0 |
| XI | XI | James Garner | MID | 9 | 5.2 | 3.80 | 11.02 | 17.24 | 4.00 | 83.9 | 90.0 |
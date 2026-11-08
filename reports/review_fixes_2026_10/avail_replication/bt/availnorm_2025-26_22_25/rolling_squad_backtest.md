# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 232.72
- Total actual points: 253.00
- Average predicted points: 58.18
- Average actual points: 63.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 55.75
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Tarkowski replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.45 | 10.04 | 16.36 | 6.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 3.02 | 8.77 | 14.38 | 1.00 | 86.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.08 | 13.52 | 19.45 | 8.00 | 83.1 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.04 | 11.40 | 18.32 | 0.00 | 95.4 | 0.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 9 | 5.7 | 3.72 | 11.16 | 17.57 | 8.00 | 85.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.14 | 11.02 | 17.79 | 2.00 | 90.4 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 5.0 | 3.70 | 10.37 | 17.54 | 1.00 | 81.9 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.34 | 13.84 | 21.85 | 2.00 | 89.7 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.88 | 11.89 | 18.72 | 2.00 | 77.3 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.1 | 3.22 | 11.30 | 19.36 | 8.00 | 41.4 | 73.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 4.83 | 14.46 | 24.78 | 1.00 | 63.5 | 33.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.27 | 14.20 | 22.62 | 3.00 | 100.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.08 | 14.11 | 22.91 | 10.00 | 77.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 4.59 | 13.85 | 23.43 | 10.00 | 58.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.70 | 12.80 | 20.59 | 2.00 | 96.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 51.74
- Actual score: 47.00
- Transfer: Gabriel dos Santos Magalhães -> Jurriën Timber (projected gain 1.24, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.49 | 9.87 | 16.02 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 2.75 | 8.13 | 13.52 | 1.00 | 82.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.36 | 11.75 | 18.99 | 4.00 | 90.4 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.84 | 10.95 | 17.23 | 1.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 3.26 | 9.74 | 15.99 | 9.00 | 85.4 | 90.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 3.28 | 9.39 | 15.62 | 1.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 3.06 | 8.47 | 14.64 | 6.00 | 49.5 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.26 | 13.88 | 22.07 | 2.00 | 93.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.1 | 3.81 | 11.53 | 18.92 | 12.00 | 67.4 | 84.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.31 | 10.11 | 16.00 | 2.00 | 73.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.2 | 5.31 | 15.38 | 24.14 | 5.00 | 85.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 4.46 | 14.22 | 24.78 | 2.00 | 52.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.84 | 13.70 | 22.52 | 2.00 | 80.4 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 3.83 | 11.38 | 18.80 | 0.00 | 75.6 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 3.94 | 10.88 | 18.09 | 10.00 | 77.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 62.48
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.80) beats the best remaining Triple Captain opportunity (8.35).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.65, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.80) beats the best remaining Triple Captain opportunity (8.35).
- Autosub: Marc Guéhi replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.65 | 10.24 | 16.55 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.6 | 2.38 | 7.61 | 12.83 | 10.00 | 80.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.79 | 11.05 | 17.99 | 5.00 | 81.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.77 | 10.85 | 17.48 | 4.00 | 92.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.64 | 10.84 | 17.77 | 2.00 | 83.3 | 90.0 |
| Bench 2 | Autosub In | Marc Guéhi | DEF | 8 | 5.2 | 3.57 | 10.16 | 16.61 | 3.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.50 | 8.23 | 14.04 | 1.00 | 78.0 | 30.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 6.06 | 15.26 | 23.84 | 10.00 | 101.1 | 45.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.72 | 11.79 | 19.22 | 2.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.23 | 9.48 | 15.54 | 2.00 | 72.4 | 84.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.3 | 6.80 | 17.97 | 26.90 | 10.00 | 102.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.27 | 13.72 | 21.88 | 8.00 | 87.5 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.0 | 4.37 | 13.70 | 22.90 | 0.00 | 71.1 | 0.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.00 | 12.37 | 20.92 | 12.00 | 69.3 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 3.82 | 11.46 | 18.79 | 2.00 | 86.3 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 1.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 62.75
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.39) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Trevoh Chalobah (projected gain 1.29, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.39) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.78 | 10.32 | 16.46 | 7.00 | 88.4 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.6 | 2.63 | 7.91 | 13.08 | 1.00 | 81.6 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.27 | 11.46 | 18.48 | 6.00 | 81.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 3.91 | 10.80 | 16.88 | 4.00 | 87.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.56 | 10.46 | 16.56 | 0.00 | 90.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.59 | 10.40 | 17.10 | 2.00 | 82.6 | 90.0 |
| Bench 4 | Bench Boost | Nathan Collins | DEF | 5 | 5.0 | 2.61 | 8.42 | 14.65 | 0.00 | 58.1 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 4.91 | 13.69 | 21.33 | 8.00 | 69.5 | 74.0 |
| Bench 2 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.14 | 10.73 | 17.82 | 5.00 | 65.5 | 90.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.01 | 9.10 | 15.33 | 7.00 | 63.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.4 | 5.74 | 15.70 | 23.52 | 10.00 | 82.7 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.51 | 13.65 | 22.72 | 2.00 | 85.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.47 | 12.88 | 20.54 | 2.00 | 80.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.9 | 3.22 | 10.68 | 18.78 | 0.00 | 24.4 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 3.66 | 10.68 | 17.09 | 2.00 | 80.3 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 250.57
- Total actual points: 193.00
- Average predicted points: 62.64
- Average actual points: 48.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW27 are included before the first simulated week.
- League-average scores were not available for this run.

## GW28

- Train rows: 152512
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.69
- Actual score: 64.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.76 | 10.96 | 17.88 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.4 | 3.05 | 8.72 | 14.34 | 3.00 | 79.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.11 | 19.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.31 | 11.15 | 21.88 | 2.00 | 90.0 | 88.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.75 | 11.04 | 18.26 | 2.00 | 84.1 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.60 | 10.66 | 17.59 | 1.00 | 82.0 | 86.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.39 | 7.55 | 18.10 | 6.00 | 85.6 | 90.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.41 | 10.19 | 15.84 | 2.00 | 71.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.43 | 9.96 | 16.56 | 9.00 | 64.0 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.3 | 2.66 | 8.05 | 13.21 | 2.00 | 73.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.86 | 19.74 | 39.00 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.89 | 18.54 | 30.41 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.05 | 17.27 | 28.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.59 | 13.60 | 22.16 | 5.00 | 85.6 | 90.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.62 | 10.67 | 17.43 | 2.00 | 77.5 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 2.20
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Justin Kluivert
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 53.55
- Actual score: 34.00
- Transfer: Trent Alexander-Arnold -> Ola Aina (projected gain 5.10, hit 0)
- Autosub: Jamie Vardy replaced Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.68 | 10.67 | 20.94 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.4 | 2.87 | 8.35 | 13.69 | 3.00 | 82.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.97 | 13.39 | 25.25 | 1.00 | 90.0 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.73 | 12.78 | 20.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.38 | 23.98 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.55 | 10.54 | 17.18 | 0.00 | 83.9 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 6.72 | 20.10 | 0.00 | 0.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.64 | 10.56 | 17.37 | 1.00 | 72.6 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.34 | 10.09 | 15.63 | 2.00 | 65.3 | 79.0 |
| Bench 2 | Autosub In | Jamie Vardy | FWD | 11 | 5.3 | 3.10 | 8.05 | 12.87 | 2.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 19.21 | 38.84 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bryan Mbeumo | MID | 4 | 8.1 | 5.80 | 16.95 | 27.61 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 5.73 | 16.13 | 25.48 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.64 | 15.04 | 25.87 | 0.00 | 66.3 | 0.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.34 | 9.94 | 16.55 | 2.00 | 78.7 | 84.0 |

## GW30

- Train rows: 154090
- Bank: 2.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.50
- Actual score: 47.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.59) beats the best remaining Triple Captain opportunity (8.96).
- Transfer: Jamie Vardy -> Omar Marmoush (projected gain 6.78, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.59) beats the best remaining Triple Captain opportunity (8.96).
- Autosub: Ola Aina replaced Justin Kluivert.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.46 | 12.65 | 20.26 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.4 | 2.68 | 8.02 | 12.91 | 1.00 | 84.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.77 | 12.97 | 18.93 | 2.00 | 61.7 | 75.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.54 | 20.44 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.09 | 11.18 | 17.83 | 6.00 | 83.0 | 90.0 |
| Bench 2 | Autosub In | Ola Aina | DEF | 16 | 5.4 | 3.20 | 9.23 | 15.12 | 1.00 | 75.1 | 39.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.3 | 2.18 | 7.17 | 12.43 | 0.00 | 50.6 | 2.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.4 | 6.17 | 15.96 | 24.84 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.61 | 10.34 | 16.71 | 2.00 | 67.3 | 71.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.31 | 7.75 | 13.08 | 1.00 | 57.6 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.59 | 23.84 | 40.65 | 3.00 | 86.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.65 | 13.67 | 23.11 | 8.00 | 81.0 | 90.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 6.2 | 4.81 | 13.38 | 21.95 | 0.00 | 74.2 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.59 | 11.26 | 20.21 | 6.00 | 32.4 | 90.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.22 | 9.02 | 15.07 | 1.00 | 78.5 | 31.0 |

## GW31

- Train rows: 154881
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.82
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.18) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 9.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.18) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 15.25 | 18.31 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.4 | 2.59 | 7.78 | 12.61 | 10.00 | 83.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.62 | 17.61 | 21.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.33 | 15.91 | 17.77 | 8.00 | 65.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 15.75 | 18.71 | 9.00 | 88.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.71 | 7.51 | 12.90 | 1.00 | 45.6 | 90.0 |
| Bench 3 | Bench Boost | Ola Aina | DEF | 16 | 5.3 | 1.82 | 6.43 | 11.55 | 0.00 | 52.8 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.4 | 4.15 | 16.02 | 18.15 | 2.00 | 61.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.82 | 9.28 | 15.37 | 1.00 | 61.0 | 27.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.55 | 8.34 | 14.09 | 2.00 | 63.5 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.49 | 25.21 | 41.89 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.96 | 14.69 | 24.31 | 3.00 | 89.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.60 | 13.94 | 24.37 | 1.00 | 63.6 | 31.0 |
| Bench 2 | Bench Boost | Mikkel Damsgaard | MID | 4 | 5.1 | 2.54 | 7.83 | 13.30 | 3.00 | 60.4 | 82.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 6.1 | 1.22 | 5.45 | 10.73 | 0.00 | 15.4 | 0.0 |
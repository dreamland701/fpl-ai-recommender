# G10: bench-boost stopping policy (per-decision, leave-one-season-out)

Each held-out half is played closed loop along the planner's path; the bench boost is additive, so a policy's value is the
bench points of the week it chose. Models are fit on the other seasons only. Planner rule = the live rule (play when this
week's projected bench beats the next four). Value model g = this week's bench points from observable features;
continuation h = best later week's bench points from the same features + weeks left. Policy: play when g >= h (+ margin).

| half | hindsight | planner rule | random | g>=h ridge | g>=h gbm | g>=h gbm, margin -1 | gbm value-threshold |
|---|---|---|---|---|---|---|---|
| 2020-21:1 | 18 | 6 (w2) | 6.3 | 2 (w12) | 1 (w15) | 9 (w14) | 6 (w2) |
| 2020-21:2 | 19 | 7 (w21) | 6.3 | 13 (w32) | 3 (w38) | 3 (w38) | 8 (w20) |
| 2021-22:1 | 22 | 9 (w2) | 5.6 | 0 (w19) | 0 (w19) | 0 (w19) | 9 (w2) |
| 2021-22:2 | 17 | 14 (w23) | 7.5 | 17 (w36) | 14 (w26) | 14 (w26) | 6 (w29) |
| 2022-23:1 | 11 | 0 (w11) | 3.2 | 0 (w11) | 11 (w15) | 11 (w15) | 2 (w19) |
| 2022-23:2 | 13 | 0 (w29) | 2.7 | 0 (w34) | 1 (w35) | 5 (w33) | 6 (w22) |
| 2023-24:1 | 24 | 12 (w2) | 9.9 | 13 (w17) | 7 (w18) | 7 (w18) | 18 (w3) |
| 2023-24:2 | 30 | 30 (w20) | 8.8 | 2 (w34) | 12 (w37) | 12 (w37) | 30 (w20) |
| 2024-25:1 | 24 | 24 (w2) | 6.7 | 2 (w19) | 1 (w18) | 1 (w18) | 24 (w2) |
| 2024-25:2 | 27 | 16 (w24) | 9.2 | 14 (w36) | 14 (w36) | 14 (w36) | 16 (w24) |
| 2025-26:1 | 11 | 5 (w2) | 6.0 | 9 (w15) | 4 (w16) | 5 (w13) | 5 (w2) |
| 2025-26:2 | 29 | 9 (w23) | 8.5 | 4 (w33) | 23 (w36) | 23 (w36) | 8 (w25) |
| **mean of 12** | 20.4 | 11.0 | 6.7 | 6.3 | 7.6 | 8.7 | 11.5 |

Wins / ties vs the planner rule per half: ridge 4/2, gbm 3/1, gbm_m1 4/2, gbm_q 4/6.

Leave-one-season-out R² for this week's bench points: forecast alone -0.014, ridge on all features -0.338, gbm -0.072.

Strongest single correlations with this week's bench points: bench_outlook0 +0.40, bench_p1_sum +0.40, bench_minutes/90 +0.39, bench_p1_2 +0.37, bench_papp_mean +0.37, bench_p1_3 +0.37, bench_outlook_mean_later +0.37, bench_papp_1 +0.35.


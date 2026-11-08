# Forecast decomposition, 2026-27 GW9: Isak vs Thiago, N.Jackson

Contribution = coef × standardised feature (clipped to the training range). Positive = raises the forecast. Rows are the OTHER player's contribution minus the reference's, i.e. where the reference LOSES (negative) or gains (positive) relative to each.

## GW9 points (intercept 1.21)

| family | Isak | Thiago | N.Jackson | Isak − Thiago | Isak − N.Jackson |
|---|---|---|---|---|---|
| availability (16) | +0.96 | +1.39 | +1.16 | -0.43 | -0.21 |
| points form (19) | +0.27 | +0.87 | +0.54 | -0.59 | -0.26 |
| xG form (11) | -0.00 | +0.22 | +0.11 | -0.23 | -0.12 |
| fixtures / F6 (20) | -0.27 | +0.11 | +0.02 | -0.38 | -0.29 |
| market (7) | +1.71 | +0.88 | +1.98 | +0.83 | -0.27 |
| other (2) | +0.00 | +0.00 | +0.00 | +0.00 | +0.00 |
| **total forecast** | 3.89 | 4.69 | 5.03 | -0.80 | -1.14 |

Largest single features, Isak − Thiago: expected_assists_avg_5 -0.89 (0.014 vs 0.232); defensive_contribution_avg_3 -0.82 (0.667 vs 7.67); expected_goal_involvements_avg_3 -0.55 (0.26 vs 0.583); creativity_avg_3 -0.33 (11.4 vs 23.4); minutes_avg_3 -0.30 (51.3 vs 90); bonus_avg_3 -0.30 (2 vs 0); expected_goals_avg_5 +0.33 (0.396 vs 0.296); selected_change_1 +0.37 (2.98 vs 0.17); expected_assists_avg_3 +0.42 (0.0167 vs 0.367); expected_goal_involvements_avg_5 +0.42 (0.41 vs 0.528)

Largest single features, Isak − N.Jackson: selected_change_1 -0.78 (2.98 vs 8.9); influence_avg_3 -0.48 (22.6 vs 41.1); fixture_difficulty_mean -0.40 (4 vs 2); defensive_contribution_avg_3 -0.39 (0.667 vs 4); expected_goal_involvements_avg_3 -0.36 (0.26 vs 0.473); ict_index_avg_5 -0.33 (6.14 vs 8.36); points_avg_8 +0.18 (6.38 vs 4.25); expected_goals_avg_5 +0.26 (0.396 vs 0.318); price_pre_deadline +0.57 (9.1 vs 6.8); ict_index_avg_3 +0.96 (6.6 vs 10.5)

## GW9-13 points (intercept 5.87)

| family | Isak | Thiago | N.Jackson | Isak − Thiago | Isak − N.Jackson |
|---|---|---|---|---|---|
| availability (16) | +4.16 | +5.85 | +4.84 | -1.68 | -0.68 |
| points form (19) | +1.74 | +3.13 | +2.48 | -1.38 | -0.74 |
| xG form (11) | +0.83 | +1.94 | +0.83 | -1.11 | +0.00 |
| fixtures / F6 (20) | -0.16 | +0.25 | +0.09 | -0.41 | -0.24 |
| market (7) | +7.85 | +4.49 | +7.31 | +3.36 | +0.54 |
| other (2) | -0.00 | -0.00 | -0.00 | +0.00 | +0.00 |
| **total forecast** | 20.31 | 21.53 | 21.42 | -1.22 | -1.12 |

Largest single features, Isak − Thiago: expected_assists_avg_5 -3.18 (0.014 vs 0.232); defensive_contribution_avg_3 -1.88 (0.667 vs 7.67); creativity_avg_5 -1.59 (10.1 vs 20.4); expected_goal_involvements_avg_3 -1.57 (0.26 vs 0.583); bonus_avg_5 -1.51 (1.8 vs 0); minutes_avg_3 -1.09 (51.3 vs 90); expected_goal_involvements_avg_5 +1.52 (0.41 vs 0.528); expected_goals_avg_5 +1.54 (0.396 vs 0.296); price_pre_deadline +1.73 (9.1 vs 7.8); points_avg_8 +1.86 (6.38 vs 2.88)

Largest single features, Isak − N.Jackson: selected_change_1 -2.46 (2.98 vs 8.9); influence_avg_3 -1.81 (22.6 vs 41.1); influence_avg_5 -1.66 (20.3 vs 32.1); threat_avg_3 -1.25 (31.7 vs 43.3); expected_goal_involvements_avg_3 -1.04 (0.26 vs 0.473); minutes_avg_3 -1.00 (51.3 vs 87); expected_goals_avg_5 +1.20 (0.396 vs 0.318); ict_index_avg_5 +2.77 (6.14 vs 8.36); price_pre_deadline +3.07 (9.1 vs 6.8); ict_index_avg_3 +3.61 (6.6 vs 10.5)

## minutes (intercept 28.30)

| family | Isak | Thiago | N.Jackson | Isak − Thiago | Isak − N.Jackson |
|---|---|---|---|---|---|
| availability (16) | +28.51 | +43.93 | +34.87 | -15.42 | -6.36 |
| points form (19) | -5.07 | +6.19 | +1.38 | -11.26 | -6.45 |
| xG form (11) | -0.14 | +6.44 | +2.27 | -6.57 | -2.41 |
| fixtures / F6 (20) | +1.02 | +0.65 | +0.86 | +0.37 | +0.16 |
| market (7) | +11.90 | +5.26 | +23.19 | +6.65 | -11.29 |
| other (2) | +0.06 | +0.06 | +0.06 | +0.00 | +0.00 |
| **total forecast** | 64.60 | 90.84 | 90.94 | -26.24 | -26.34 |

Largest single features, Isak − Thiago: expected_goal_involvements_avg_3 -17.14 (0.26 vs 0.583); defensive_contribution_avg_3 -13.55 (0.667 vs 7.67); expected_assists_avg_5 -10.72 (0.014 vs 0.232); threat_avg_3 -10.57 (31.7 vs 19.3); minutes_avg_3 -9.09 (51.3 vs 90); minutes_avg_8 -6.81 (70.9 vs 89); defensive_contribution_avg_5 +6.02 (0.8 vs 5.4); expected_goal_involvements_avg_5 +6.33 (0.41 vs 0.528); creativity_avg_3 +10.65 (11.4 vs 23.4); expected_assists_avg_3 +14.04 (0.0167 vs 0.367)

Largest single features, Isak − N.Jackson: ict_index_avg_3 -31.81 (6.6 vs 10.5); selected_change_1 -11.45 (2.98 vs 8.9); expected_goal_involvements_avg_3 -11.31 (0.26 vs 0.473); minutes_avg_3 -8.39 (51.3 vs 87); ict_index_avg_5 -6.81 (6.14 vs 8.36); defensive_contribution_avg_3 -6.45 (0.667 vs 4); expected_goals_avg_3 +7.01 (0.243 vs 0.383); creativity_avg_3 +8.16 (11.4 vs 20.6); threat_avg_3 +9.99 (31.7 vs 43.3); influence_avg_3 +13.84 (22.6 vs 41.1)

Ungrouped features: defcon_hit_rate_3, defcon_hit_rate_5


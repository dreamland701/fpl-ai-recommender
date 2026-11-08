# Train/live parity audit: live GW7 (2026-10-17T10:00:00Z) vs GW7 of 2023-24, 2024-25, 2025-26

Live rows 667; historical rows 2131. Subsets: all players, and regulars (minutes_avg_5 > 45).

## all players (live n 667, hist n 2131)

| feature | live median | hist median | live mean | hist mean | live zero | hist zero | flag |
|---|---|---|---|---|---|---|---|
| price_pre_deadline | 4.900 | 4.600 | 5.078 | 4.954 | 0.00 | 0.00 |  |
| selected_by_percent_pre_deadline | 0.200 | 0.188 | 2.248 | 2.112 | 0.25 | 0.00 | **zero share 0.25 vs 0.00** |
| transfers_in_prev_event | 819.000 | 690.000 | 26601.978 | 24553.825 | 0.16 | 0.19 |  |
| transfers_out_prev_event | 2411.000 | 1978.000 | 26601.978 | 24553.825 | 0.00 | 0.01 |  |
| transfer_balance_prev_event | -460.000 | -334.000 | 0.000 | 0.000 | 0.00 | 0.01 |  |
| home_fixture_count | 0.000 | 1.000 | 0.474 | 0.521 | 0.53 | 0.48 |  |
| away_fixture_count | 1.000 | 0.000 | 0.526 | 0.518 | 0.47 | 0.50 |  |
| fixture_count | 1.000 | 1.000 | 1.000 | 1.039 | 0.00 | 0.00 |  |
| fixture_difficulty_mean | 3.000 | 3.000 | 3.127 | 2.985 | 0.00 | 0.00 |  |
| fixture_difficulty_min | 3.000 | 3.000 | 3.127 | 2.966 | 0.00 | 0.00 |  |
| team_goals_for_avg_3 | 1.667 | 1.333 | 1.556 | 1.426 | 0.00 | 0.02 |  |
| team_goals_against_avg_3 | 1.333 | 1.333 | 1.536 | 1.445 | 0.06 | 0.00 |  |
| team_goals_for_avg_5 | 1.200 | 1.400 | 1.475 | 1.436 | 0.00 | 0.00 |  |
| team_goals_against_avg_5 | 1.400 | 1.400 | 1.472 | 1.476 | 0.00 | 0.00 |  |
| opponent_goals_for_avg_3 | 1.667 | 1.333 | 1.546 | 1.440 | 0.00 | 0.02 |  |
| opponent_goals_against_avg_3 | 1.333 | 1.333 | 1.505 | 1.444 | 0.05 | 0.00 |  |
| opponent_goals_for_avg_5 | 1.400 | 1.400 | 1.465 | 1.444 | 0.00 | 0.00 |  |
| opponent_goals_against_avg_5 | 1.400 | 1.400 | 1.460 | 1.469 | 0.00 | 0.00 |  |
| opp_def_weakness_3 | -0.200 | 0.017 | -0.029 | -0.005 | 0.00 | 0.00 | **mean ratio 6.00** |
| form_x_opp_weakness_3 | 0.000 | 0.000 | -0.064 | 0.046 | 0.23 | 0.28 |  |
| xgi_x_opp_weakness_3 | 0.000 | 0.000 | 0.002 | 0.000 | 0.51 | 0.55 | **mean ratio 14.67** |
| opp_def_weakness_5 | -0.070 | -0.090 | -0.010 | -0.002 | 0.00 | 0.00 | **mean ratio 4.47** |
| form_x_opp_weakness_5 | -0.014 | 0.000 | 0.050 | 0.014 | 0.20 | 0.27 | **mean ratio 3.61** |
| xgi_x_opp_weakness_5 | 0.000 | 0.000 | 0.001 | -0.001 | 0.45 | 0.50 |  |
| points_avg_1 | 1.000 | 0.762 | 1.562 | 1.373 | 0.27 | 0.32 |  |
| minutes_avg_1 | 0.000 | 0.000 | 29.448 | 27.691 | 0.53 | 0.57 |  |
| appearance_rate_1 | 0.000 | 0.000 | 0.472 | 0.427 | 0.53 | 0.57 |  |
| played_60_rate_1 | 0.000 | 0.000 | 0.309 | 0.286 | 0.69 | 0.71 |  |
| points_avg_3 | 1.000 | 0.889 | 1.647 | 1.399 | 0.23 | 0.28 |  |
| minutes_avg_3 | 6.000 | 2.667 | 29.442 | 27.745 | 0.43 | 0.47 |  |
| appearance_rate_3 | 0.333 | 0.333 | 0.462 | 0.430 | 0.43 | 0.47 |  |
| played_60_rate_3 | 0.000 | 0.000 | 0.307 | 0.288 | 0.60 | 0.62 |  |
| points_avg_5 | 1.195 | 0.980 | 1.641 | 1.410 | 0.20 | 0.27 |  |
| minutes_avg_5 | 9.400 | 7.800 | 29.689 | 27.862 | 0.37 | 0.42 |  |
| appearance_rate_5 | 0.400 | 0.400 | 0.468 | 0.434 | 0.37 | 0.42 |  |
| played_60_rate_5 | 0.000 | 0.000 | 0.312 | 0.289 | 0.56 | 0.56 |  |
| points_avg_8 | 1.262 | 1.000 | 1.649 | 1.420 | 0.19 | 0.26 |  |
| minutes_avg_8 | 12.000 | 9.833 | 29.852 | 28.064 | 0.35 | 0.40 |  |
| appearance_rate_8 | 0.500 | 0.333 | 0.472 | 0.438 | 0.35 | 0.40 |  |
| played_60_rate_8 | 0.000 | 0.000 | 0.314 | 0.292 | 0.52 | 0.54 |  |
| price_change_1 | 0.000 | 0.000 | -0.004 | -0.006 | 0.92 | 0.89 |  |
| selected_change_1 | -0.009 | -0.002 | -0.001 | -0.000 | 0.00 | 0.00 | **mean ratio 95218424523036.16** |
| home_fixture_ratio | 0.000 | 1.000 | 0.474 | 0.511 | 0.53 | 0.48 |  |
| blank_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| double_gw | 0.000 | 0.000 | 0.000 | 0.039 | 1.00 | 0.96 |  |
| bonus_avg_3 | 0.000 | 0.000 | 0.093 | 0.089 | 0.88 | 0.88 |  |
| bonus_avg_5 | 0.000 | 0.000 | 0.095 | 0.089 | 0.83 | 0.83 |  |
| bps_avg_3 | 1.333 | 0.333 | 5.682 | 4.899 | 0.43 | 0.48 |  |
| bps_avg_5 | 1.800 | 1.200 | 5.671 | 4.922 | 0.37 | 0.43 |  |
| influence_avg_3 | 0.867 | 0.200 | 6.963 | 6.423 | 0.46 | 0.49 |  |
| influence_avg_5 | 1.800 | 1.080 | 6.842 | 6.350 | 0.39 | 0.44 |  |
| creativity_avg_3 | 0.133 | 0.000 | 4.780 | 4.282 | 0.46 | 0.52 |  |
| creativity_avg_5 | 0.360 | 0.160 | 4.772 | 4.313 | 0.41 | 0.47 |  |
| threat_avg_3 | 0.000 | 0.000 | 4.186 | 4.022 | 0.54 | 0.59 |  |
| threat_avg_5 | 0.400 | 0.000 | 4.171 | 4.006 | 0.48 | 0.52 |  |
| ict_index_avg_3 | 0.267 | 0.100 | 1.591 | 1.472 | 0.44 | 0.48 |  |
| ict_index_avg_5 | 0.520 | 0.340 | 1.576 | 1.466 | 0.39 | 0.43 |  |
| starts_avg_3 | 0.000 | 0.000 | 0.330 | 0.310 | 0.58 | 0.60 |  |
| starts_avg_5 | 0.000 | 0.000 | 0.332 | 0.311 | 0.54 | 0.54 |  |
| expected_goals_avg_3 | 0.000 | 0.000 | 0.045 | 0.040 | 0.62 | 0.65 |  |
| expected_goals_avg_5 | 0.000 | 0.000 | 0.046 | 0.041 | 0.57 | 0.58 |  |
| expected_assists_avg_3 | 0.000 | 0.000 | 0.027 | 0.026 | 0.55 | 0.58 |  |
| expected_assists_avg_5 | 0.002 | 0.000 | 0.027 | 0.027 | 0.48 | 0.52 |  |
| expected_goal_involvements_avg_3 | 0.000 | 0.000 | 0.072 | 0.065 | 0.51 | 0.55 |  |
| expected_goal_involvements_avg_5 | 0.004 | 0.002 | 0.073 | 0.068 | 0.45 | 0.50 |  |
| expected_goals_conceded_avg_3 | 0.120 | 0.030 | 0.487 | 0.431 | 0.44 | 0.49 |  |
| expected_goals_conceded_avg_5 | 0.178 | 0.142 | 0.499 | 0.450 | 0.39 | 0.44 |  |
| defensive_contribution_avg_3 | 0.333 | 0.000 | 2.310 | 0.720 | 0.49 | 0.84 | **zero share 0.49 vs 0.84; mean ratio 3.21** |
| defensive_contribution_avg_5 | 0.400 | 0.000 | 2.282 | 0.717 | 0.44 | 0.82 | **zero share 0.44 vs 0.82; mean ratio 3.18** |
| defcon_hit_rate_3 | 0.000 | 0.000 | 0.055 | 0.018 | 0.88 | 0.96 | **mean ratio 3.06** |
| defcon_hit_rate_5 | 0.000 | 0.000 | 0.053 | 0.016 | 0.85 | 0.95 | **mean ratio 3.24** |
| expected_data_source_available | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| defensive_data_source_available | 1.000 | 0.000 | 1.000 | 0.349 | 0.00 | 0.65 | **zero share 0.00 vs 0.65; mean ratio 2.87** |
| status_flag_pre_deadline | 0.000 | 0.000 | 0.292 | 0.000 | 0.71 | 1.00 | **zero share 0.71 vs 1.00** |
| news_flag_pre_deadline | 0.000 | 0.000 | 0.292 | 0.000 | 0.71 | 1.00 | **zero share 0.71 vs 1.00** |

## regulars (live n 218, hist n 646)

| feature | live median | hist median | live mean | hist mean | live zero | hist zero | flag |
|---|---|---|---|---|---|---|---|
| price_pre_deadline | 5.300 | 5.000 | 5.487 | 5.446 | 0.00 | 0.00 |  |
| selected_by_percent_pre_deadline | 1.950 | 1.952 | 6.044 | 5.957 | 0.01 | 0.00 |  |
| transfers_in_prev_event | 14976.500 | 15157.000 | 76488.018 | 72811.193 | 0.00 | 0.00 |  |
| transfers_out_prev_event | 25529.500 | 22440.500 | 67814.472 | 63071.582 | 0.00 | 0.00 |  |
| transfer_balance_prev_event | -1209.500 | -314.500 | 8673.546 | 9739.611 | 0.00 | 0.00 |  |
| home_fixture_count | 1.000 | 1.000 | 0.509 | 0.512 | 0.49 | 0.49 |  |
| away_fixture_count | 0.000 | 0.500 | 0.491 | 0.512 | 0.51 | 0.50 |  |
| fixture_count | 1.000 | 1.000 | 1.000 | 1.025 | 0.00 | 0.00 |  |
| fixture_difficulty_mean | 3.000 | 3.000 | 3.156 | 3.012 | 0.00 | 0.00 |  |
| fixture_difficulty_min | 3.000 | 3.000 | 3.156 | 3.000 | 0.00 | 0.00 |  |
| team_goals_for_avg_3 | 1.333 | 1.333 | 1.532 | 1.457 | 0.00 | 0.02 |  |
| team_goals_against_avg_3 | 1.333 | 1.333 | 1.514 | 1.440 | 0.06 | 0.00 |  |
| team_goals_for_avg_5 | 1.300 | 1.400 | 1.469 | 1.459 | 0.00 | 0.00 |  |
| team_goals_against_avg_5 | 1.400 | 1.400 | 1.455 | 1.464 | 0.00 | 0.00 |  |
| opponent_goals_for_avg_3 | 1.667 | 1.333 | 1.532 | 1.432 | 0.00 | 0.02 |  |
| opponent_goals_against_avg_3 | 1.333 | 1.333 | 1.529 | 1.453 | 0.05 | 0.00 |  |
| opponent_goals_for_avg_5 | 1.400 | 1.400 | 1.470 | 1.443 | 0.00 | 0.00 |  |
| opponent_goals_against_avg_5 | 1.400 | 1.400 | 1.466 | 1.477 | 0.00 | 0.00 |  |
| opp_def_weakness_3 | -0.200 | 0.017 | -0.004 | 0.004 | 0.00 | 0.00 |  |
| form_x_opp_weakness_3 | -0.533 | 0.028 | -0.297 | 0.151 | 0.01 | 0.00 |  |
| xgi_x_opp_weakness_3 | -0.005 | 0.000 | 0.004 | 0.004 | 0.08 | 0.09 |  |
| opp_def_weakness_5 | -0.070 | 0.070 | -0.004 | 0.004 | 0.00 | 0.00 |  |
| form_x_opp_weakness_5 | -0.315 | 0.000 | 0.120 | 0.032 | 0.00 | 0.00 | **mean ratio 3.72** |
| xgi_x_opp_weakness_5 | -0.006 | 0.000 | 0.003 | -0.000 | 0.05 | 0.06 | **mean ratio -13.87** |
| points_avg_1 | 2.000 | 2.000 | 3.012 | 2.987 | 0.07 | 0.05 |  |
| minutes_avg_1 | 90.000 | 90.000 | 72.115 | 73.967 | 0.09 | 0.08 |  |
| appearance_rate_1 | 1.000 | 1.000 | 0.913 | 0.921 | 0.09 | 0.08 |  |
| played_60_rate_1 | 1.000 | 1.000 | 0.807 | 0.819 | 0.19 | 0.18 |  |
| points_avg_3 | 3.000 | 2.667 | 3.455 | 3.068 | 0.01 | 0.00 |  |
| minutes_avg_3 | 84.000 | 83.833 | 75.836 | 75.156 | 0.00 | 0.00 |  |
| appearance_rate_3 | 1.000 | 1.000 | 0.943 | 0.938 | 0.00 | 0.00 |  |
| played_60_rate_3 | 1.000 | 1.000 | 0.849 | 0.836 | 0.00 | 0.01 |  |
| points_avg_5 | 3.137 | 2.800 | 3.423 | 3.088 | 0.00 | 0.00 |  |
| minutes_avg_5 | 80.400 | 77.300 | 76.004 | 74.448 | 0.00 | 0.00 |  |
| appearance_rate_5 | 1.000 | 1.000 | 0.949 | 0.937 | 0.00 | 0.00 |  |
| played_60_rate_5 | 1.000 | 0.800 | 0.856 | 0.826 | 0.00 | 0.00 |  |
| points_avg_8 | 3.167 | 2.833 | 3.424 | 3.083 | 0.00 | 0.00 |  |
| minutes_avg_8 | 75.333 | 75.917 | 74.494 | 73.710 | 0.00 | 0.00 |  |
| appearance_rate_8 | 1.000 | 1.000 | 0.940 | 0.933 | 0.00 | 0.00 |  |
| played_60_rate_8 | 0.833 | 0.833 | 0.836 | 0.817 | 0.00 | 0.00 |  |
| price_change_1 | 0.000 | 0.000 | -0.000 | -0.003 | 0.88 | 0.81 | **mean ratio 0.00** |
| selected_change_1 | -0.005 | -0.004 | 0.012 | 0.041 | 0.00 | 0.00 | **mean ratio 0.30** |
| home_fixture_ratio | 1.000 | 0.750 | 0.509 | 0.506 | 0.49 | 0.49 |  |
| blank_gw | 0.000 | 0.000 | 0.000 | 0.000 | 1.00 | 1.00 |  |
| double_gw | 0.000 | 0.000 | 0.000 | 0.025 | 1.00 | 0.98 |  |
| bonus_avg_3 | 0.000 | 0.000 | 0.251 | 0.261 | 0.68 | 0.67 |  |
| bonus_avg_5 | 0.000 | 0.000 | 0.264 | 0.261 | 0.53 | 0.53 |  |
| bps_avg_3 | 14.167 | 12.667 | 14.142 | 13.129 | 0.00 | 0.01 |  |
| bps_avg_5 | 13.600 | 12.400 | 14.131 | 13.131 | 0.00 | 0.00 |  |
| influence_avg_3 | 17.133 | 16.433 | 17.721 | 17.569 | 0.00 | 0.00 |  |
| influence_avg_5 | 16.200 | 16.180 | 17.399 | 17.224 | 0.00 | 0.00 |  |
| creativity_avg_3 | 8.850 | 8.617 | 11.974 | 11.195 | 0.07 | 0.07 |  |
| creativity_avg_5 | 9.990 | 8.530 | 11.999 | 11.185 | 0.06 | 0.06 |  |
| threat_avg_3 | 6.667 | 6.333 | 9.969 | 10.334 | 0.13 | 0.15 |  |
| threat_avg_5 | 7.100 | 7.000 | 9.990 | 10.234 | 0.10 | 0.10 |  |
| ict_index_avg_3 | 3.533 | 3.400 | 3.964 | 3.909 | 0.00 | 0.00 |  |
| ict_index_avg_5 | 3.460 | 3.370 | 3.935 | 3.863 | 0.00 | 0.00 |  |
| starts_avg_3 | 1.000 | 1.000 | 0.885 | 0.872 | 0.00 | 0.00 |  |
| starts_avg_5 | 1.000 | 1.000 | 0.885 | 0.860 | 0.00 | 0.00 |  |
| expected_goals_avg_3 | 0.057 | 0.040 | 0.113 | 0.102 | 0.22 | 0.25 |  |
| expected_goals_avg_5 | 0.054 | 0.047 | 0.113 | 0.107 | 0.17 | 0.16 |  |
| expected_assists_avg_3 | 0.040 | 0.037 | 0.068 | 0.068 | 0.10 | 0.10 |  |
| expected_assists_avg_5 | 0.050 | 0.045 | 0.070 | 0.068 | 0.06 | 0.07 |  |
| expected_goal_involvements_avg_3 | 0.123 | 0.110 | 0.181 | 0.170 | 0.08 | 0.09 |  |
| expected_goal_involvements_avg_5 | 0.129 | 0.119 | 0.183 | 0.175 | 0.05 | 0.06 |  |
| expected_goals_conceded_avg_3 | 1.225 | 1.053 | 1.224 | 1.143 | 0.00 | 0.00 |  |
| expected_goals_conceded_avg_5 | 1.238 | 1.101 | 1.248 | 1.168 | 0.00 | 0.00 |  |
| defensive_contribution_avg_3 | 5.667 | 0.000 | 5.703 | 1.963 | 0.09 | 0.70 | **zero share 0.09 vs 0.70; mean ratio 2.90** |
| defensive_contribution_avg_5 | 5.400 | 0.000 | 5.665 | 1.894 | 0.09 | 0.70 | **zero share 0.09 vs 0.70; mean ratio 2.99** |
| defcon_hit_rate_3 | 0.000 | 0.000 | 0.153 | 0.055 | 0.69 | 0.89 | **mean ratio 2.77** |
| defcon_hit_rate_5 | 0.000 | 0.000 | 0.148 | 0.050 | 0.61 | 0.86 | **zero share 0.61 vs 0.86; mean ratio 2.98** |
| expected_data_source_available | 1.000 | 1.000 | 1.000 | 1.000 | 0.00 | 0.00 |  |
| defensive_data_source_available | 1.000 | 0.000 | 1.000 | 0.334 | 0.00 | 0.67 | **zero share 0.00 vs 0.67; mean ratio 2.99** |
| status_flag_pre_deadline | 0.000 | 0.000 | 0.083 | 0.000 | 0.92 | 1.00 |  |
| news_flag_pre_deadline | 0.000 | 0.000 | 0.083 | 0.000 | 0.92 | 1.00 |  |

Flags: 22 (a flag is a prompt to look, not a verdict; schedule-driven features legitimately differ by week).

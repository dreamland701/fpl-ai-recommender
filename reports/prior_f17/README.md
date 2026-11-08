# F17 prior-season availability features + corrected F13 (2026-10-27)

Question (Wes, 2026-10-27, Calafiori): the model "rates him fairly high, but the minutes he plays are fairly low ... follows
the pattern he has in the last season ... starting fresh from the new season". The minutes/appearance heads are
current-season-only by design (F2b blends quality only, 2026-09-01), so a player's multi-season start record is invisible
once he has a run of starts. `reports/gw9_packet_2026_10/minutes_prior_study.md` measured the residual this leaves on
16,546 nailed-looking player-weeks of walk-forward classic forecasts: prior-season start share is not predictive beyond
the forecast (excess +0.03 ± 0.09 pts; defenders −0.17 ± 0.15), but players with no prior Premier League season are
over-forecast (−0.23 ± 0.09; defenders −0.35 ± 0.14; weeks 1-10 −0.38 ± 0.20).

Bug found on the way: the table's `player_id` is the per-season element id and is re-used by a different player the next
season; `scripts/add_injury_history_features.py` (F13) and `reports/review_fixes_2026_10/injury_pattern.py` keyed cross-season
history on it. Both re-keyed on `code` (memory fpl-player-id-reuse); corrected pattern table
`reports/review_fixes_2026_10/injury_pattern_codekey.md`.

Tables (`scripts/add_prior_season_features.py`, `scripts/add_injury_history_features.py` on the production F6 table):
- PB_F = production table (base); PI_F = F13 re-keyed (inj_absences_38, inj_long_layoff_prev, inj_absences_x_price);
- PP_F = prior_pl_games, no_prior_pl_season, prior_start_share, prior_minutes_share, prior_unknown (2019-20 = table's first season);
- PN_F = PP_F without the two share columns.
Flags FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1; 21 windows
(`scripts/run_prior_f17_chain.sh`, bt/, accuracy/, xpts/).

| config | Δ actual / 21 windows | t | wins-losses-ties | Δ xPts | t | 1GW MAE | 3GW MAE | 5GW MAE |
|---|---|---|---|---|---|---|---|---|
| PB_F (base) | 5,314 | | | 5,127 | | 1.0009 | 2.3908 | 3.6576 |
| PI_F (F13 corrected) | −64 | −1.37 | 3-9-9 | −7 | −0.25 | 0.9999 | 2.3884 | 3.6535 |
| PP_F (F17, all five) | +41 | +0.55 | 11-6-4 | +56 | +1.23 | 1.0037 | 2.3830 | 3.6337 |
| PN_F (F17 without shares) | −31 | −0.50 | 4-6-11 | −8 | −0.20 | 1.0016 | 2.3905 | 3.6567 |

**Verdict.** F13 stays closed on a valid test (accuracy a hair better, decisions −64). F17 is NULL-positive: +41 actual /
+56 xPts over 21 windows (t 0.55 / 1.23), below the noise-floor bar (2σ on the xPts instrument ≈ 85 over 21 windows); the
whole gain is in the two share columns (PN_F is nil), which help the 5GW head (MAE −0.024) and cost the 1GW head a little.
Not shipped; the columns stay in SAFE_FEATURE_COLUMNS (used only when present) so the table variant re-measures with one
command once more 2026-27 weeks exist. If it ever ships it must be ported into dataset.py (keyed on `code`) so the live
frame carries it — a table-copy feature has no live parity.

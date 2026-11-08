# GW10 recommendation (FINAL, Friday 2026-11-06 09:45 PST; deadline 10:30 PST = 18:30 UTC)

Built from the 08:35 PST refresh of `final/` (snapshot 2026-11-06T16:35Z, done 08:50, no failed step). The public API still
shows the pre-transfer squad (Cunha, bank £0.3m, 1 FT) because current-GW transfers are hidden until the deadline; Wes's
confirmed Cunha → Rice (Thursday evening) was replayed from `logs/gw10_hand_edit` by `scripts/apply_hand_edit.py` at 08:35
(Cunha sells 7.8 → Rice 7.4: bank £0.7m, 0 FT; API state kept as `final/entry_state_api.json`). Classic + F6 on the fixed
pipeline decides; the H5 shadow read (GPU, 670 rows, done 08:50) and the F16 Guardian-lineup shadow are logged alongside.
The Guardian predicted-lineups article was published at 16:43Z (08:43 PST), eight minutes after the refresh's Guardian pull,
so the store was re-pulled at 09:40 PST and the F16 shadow replayed on CPU (no-article versions kept as `final/*_noarticle.*`);
the H5 read was not re-run (its prompt had no lineup block; the decision is classic's either way).

**Do:** **Cunha → Rice (confirmed), no further transfer, no chip.** 0 free transfers after the move: every further move
costs 4 and none earns it (Donnarumma → Raya is worth +3.9 now against +6.0 as GW11's free transfer).
XI **Donnarumma; De Cuyper, Konsa, N.Williams; Rogers, Groß, Rice, McGinn; Haaland, Isak, Evanilson.**
Bench **Sels > Cherki > Justin > Mitchell.** Captain **Haaland** (NFO v MCI Sat 17:30Z, GW10 8.82), vice **Rogers**
(MUN v AVL Sun 16:30Z, 6.47). GW10 XI forecast 63.2 including the captain (Thursday evening 62.0 on this route, 60.7 before
the move); hold EV GW10-14 293.6 (Thursday 284.7 before the move).

One change since Thursday evening's bench order: Konsa's knee flag was cleared overnight (d/75% → a/100%; 3.75 → 4.21,
P(appear) 0.81 → 0.92, 83 min) and McGinn (3.36, 74 min) now edges Cherki (3.27, 39 min, P 0.43; Thursday 3.43 / 0.46, ownership
still selling) for the last midfield slot, so Cherki drops to first sub. A 0.09 gap is a coin flip: the Guardian lists both to
start, and the lineup-aware F16 shadow lifts Cherki to 3.43 (+0.16, the largest "XI" move among the top 150) and would start him
over McGinn (64.7 v 64.2). Classic decides, so McGinn starts; swapping them costs nothing measurable either way. The bench order
covers the rest: if a midfielder or forward misses, Cherki comes in if he plays, otherwise Justin; if a defender misses, Justin
(Cherki cannot keep three defenders).

## Routes (GW10-14 value vs holding 293.6, net of hits; exact optimizer + decision sheet)

| route | GW10-14 now | if rolled a week | GW10 XI (hold 63.2) | hit | bank after |
|---|---|---|---|---|---|
| Hold (after Cunha → Rice) | 0 | — | 63.2 | 0 | 0.7 |
| Donnarumma → Raya | +3.9 | +6.0 | 65.1 | −4 | 0.0 |
| Donnarumma + Cherki → Raya + Tavernier | +3.0 | +4.1 | — | −8 | 1.2 |
| Donnarumma + Cherki + Mitchell → Raya + Tavernier + Van Hecke | +3.0 | +3.1 | — | −12 | 0.7 |
| Wildcard (GW10-14) | +25.2 projected (exact), −5.1 on the decision sheet | — | — | — | 0.0 / 0.4 |
| Free Hit (GW10 only) | +6.2 projected (exact, XI 70.5), +0.8 on the decision sheet | — | — | — | 0.0 / 0.6 |

GW10-only exact optimizer: hold (no free move improves this week). Reading: Thursday's Raya pair (+8.7 with Cunha → Rice)
is now just its Raya half, and Donnarumma → Raya is worth more as next week's free transfer (+6.0) than as a hit now (+3.9),
so roll. Two- and three-move routes are worth less than the single move; wildcards have realised at ~0 historically.

## Guardian predicted lineups (published Fri 2026-11-06 16:43Z, 1.8 h before the deadline; 18/20 clubs, EVE v COV not covered)

All 15 squad players are listed in their clubs' XIs (Konsa, Rice at Arsenal; Cherki and Haaland at City; McGinn and Rogers
at Villa; Isak at Liverpool; Evanilson at Bournemouth; De Cuyper at Brighton; Donnarumma, N.Williams, Justin, Mitchell, Sels,
Groß). Nobody in the squad is sub, doubtful or out. Among the top-150 forecasts the article benches J.Timber, Boscagli, Gray
and M.Sangaré and has Calvert-Lewin doubtful; none is ours. Doubts elsewhere: Rashford, Dorgu, Shaw (MUN), Wan-Bissaka (AVL),
Gravenberch (LIV), Igor Jesus (NFO). F16 shadow (classic+F6+Guardian categories, not deciding): the XI tag is worth +0.05 on
average (n 131), sub −0.14, doubtful −0.15; every squad player moves +0.01..+0.06 except Cherki +0.16 (minutes 39 → 43).

## Status check vs Thursday evening

Konsa cleared (knee, 75% → 100%); no other squad flag moved, all 15 are 'a'. League-wide, 10 status/news lines changed:
Konsa and Tosin cleared; Wan-Bissaka out → d/50% (hamstring), Scott out → d/75%, Martínez (CHE) out → d/75% (head), Dorgu out
→ d/75%; Caicedo d/75% (calf); Cairney out (knee, back 21 Nov); Baleba out (hamstring); Rashford out (hip). None in the squad
or among live targets. Fixtures as published: EVE v COV Fri 20:00Z; LEE v TOT Sat 12:30Z; ARS v HUL, FUL v NEW 15:00Z;
NFO v MCI 17:30Z; BHA v BRE, CRY v LIV, IPS v BOU, SUN v CHE Sun 14:00Z; MUN v AVL 16:30Z. No postponements.

## What moved since Thursday evening (Konsa's flag, otherwise ownership momentum; prices unchanged)

| Player | Thursday pm (GW10 / GW10-14, P, min) | Final | why |
|---|---|---|---|
| Konsa | 3.75 / 16.3, 0.81, 73 | 4.21 / 18.0, 0.92, 83 | knee flag cleared |
| Cherki | 3.43 / 17.6, 0.46, 41 | 3.27 / 17.1, 0.43, 39 | 34.7 → 33.7% (sells) |
| Evanilson | 4.44 / 20.1, 0.76, 68 | 4.77 / 21.1, 0.81, 73 | 19.2 → 21.2% |
| Isak | 4.78 / 21.9, 0.76, 68 | 4.98 / 22.6, 0.79, 71 | 22.5 → 23.7% |
| De Cuyper | 5.06 / 22.9, 0.98, 88 | 5.19 / 23.3, 1.00, 90 | 45.5 → 46.3% |
| Rogers | 6.37 / 27.3 | 6.47 / 27.7 | 52.9 → 53.5% |
| Rice | 4.88 / 22.1, 0.97, 88 | 4.96 / 22.4, 0.99, 89 | 12.8 → 13.3% |
| Haaland | 8.80 / 41.1 | 8.82 / 41.2 | 79.1 → 79.2% |
| McGinn | 3.36 / 16.0, 0.82, 74 | unchanged | |
| N.Williams | 3.30 / 15.9 | 3.27 / 15.8 | 5.6 → 5.4% |
| Justin, Mitchell | 3.18 / 15.0; 3.00 / 13.8 | 3.18 / 15.0; 2.99 / 13.8 | unchanged |

Role override `--auto`: Isak only (three straight starts since GW7): 4.98 → 4.46 GW / 22.6 → 20.3 GW10-14 if his history is
restarted at GW7 (lower, because the GW7-9 rows are his lighter minutes); XI unchanged (63.2 → 62.7).

## Classic vs classic + SFT (H5 shadow, `final/side_by_side_h5.md`)

| | Classic | Classic + H5 |
|---|---|---|
| XI | Donnarumma; De Cuyper, Konsa, N.Williams; Rogers, Groß, Rice, McGinn; Haaland, Isak, Evanilson | same |
| Bench | Sels, Cherki, Justin, Mitchell | same |
| C / VC | Haaland / Rogers | same |
| GW10 XI | 63.3 | 62.6 |

The adapter's generic rule this week is delta = +0.085 × classic − 0.307 (−0.14 for a 2-point player, +0.37 for an 8-point
one); every player-specific remainder in the squad is within ±0.31: De Cuyper −0.31 (the PL.com "go BIG in defence" and
"best fixtures" pieces: his midfield role, 69 points so far), Haaland −0.53 against a +0.44 generic lift (net −0.09; "best
replacements for João Pedro", Villa 2-1 City), Rogers −0.23, Konsa −0.18, Justin −0.14. Its availability read is high
everywhere, consistent with the lineups it did not yet have: McGinn 0.82 → 0.95 (Barcelona 3-0 Villa Champions League blog,
"McGinn and Jackson are off"; "the outstanding John McGinn" in Villa 2-1 City), Cherki 0.43 → 0.68 (replaced at half-time in
Villa 2-1 City; a deflected free kick in the Carabao Cup), Evanilson 0.81 → 0.97 ("best forwards": four goals in four), Isak
0.79 → 0.95 (the Liverpool 0-1 Arsenal penalty-denial pieces), Donnarumma 0.88 → 0.96, Sels 0.84 → 0.94. Semenyo (not ours)
1.71 → 1.00, P 0.21 → 0.02 ("until Semenyo returns in mid-December"). Nothing in it changes a pick; the SFT also keeps McGinn
ahead of Cherki (3.31 v 3.22).

## Chips

Planner rule (`reports/chip_line_gw10.md`): **Bench Boost now**, +11.9 (Sels 2.4, Cherki 3.3, Justin 3.2, Mitchell 3.0), the
best bench week in its four-week horizon (+11.0 best in GW11-14); Free Hit +6.2 projected (XI 70.5) / +0.8 on the decision
sheet; Wildcard +25.2 projected / −5.1 on the sheet. No double or blank gameweek is published this half and all three chips
expire after GW19, so three chips have ten gameweeks. **Recommendation: no chip this week.** The "best projected week"
trigger is exactly the rule the chip-timing study found loses, a 12-point bench with a 39-minute Cherki as its second sub is a
weak boost, and the GW11 international break (deadline Sat 2026-11-21 11:00Z, twelve days away) is the natural Wildcard week:
N.Williams, Justin, Mitchell and Sels are the dead money, and a wildcard-built bench is where Bench Boost earns more. Free Hit
realises at ~0 on average; keep it for a congested round (GW13 Tue 12-01 / GW14 Sat 12-05, or GW18-19). Pressing Bench Boost
now is a legitimate alternative worth +11.9 at face value; the difference against the post-wildcard version is a few points,
inside noise.

## Training

H12 (Gemma-4-12B bf16 LoRA on the H6 recipe) finished Thursday 12:48 PST: a tie. Holdout RMSE 3.417 v classic 3.420 / H5
3.415 / H6b 3.402; its delta is a near-constant −0.08 (sd 0.036), corr(Δ, residual) 0.086 live, availability AUC 0.707 v H5
0.776, +9 actual / +14 xPts over 5 windows (noise floor 65). The SFT points line is closed at E4B, 12B and 31B on this corpus.
GPU idle; nothing launches without Wes's word. Candidates: all-player data scaling on E4B (~10%, four GPU days); CPU multi-week
transfer MILP (~40% of a measurable +20-40/half); club-tag evidence matcher + "scored in Europe" fact; minutes head without
market momentum. GW10 is settled with `scripts/gw_status.py --event 10` first (last game MUN v AVL Sun 16:30Z), then the ledger row.

**Files:** `final/README.md`, `logs/gw10_final_refresh.log` (hand-edit line), `final/decide.log`, `final/milp.log`,
`final/route_lineups.log`, `final/role_override_sheet.md`, `final/f16_shadow.md` (Guardian lineups, late replay; no-article
version `final/f16_shadow_noarticle.md`, `logs/gw10_f16_late.log`), `final/side_by_side_h5.md`, `reports/chip_line_gw10.md`;
pre-hand-edit state `final/entry_state_api.json`; forecasts `final/forecasts_new_pipeline.jsonl`, `final/forecasts_f16_shadow.jsonl`;
H5 read `reports/h_series/h5_gw10final_pred.jsonl`; Guardian categories `reports/team_news_f16/gn_feat_live_gw10.json`.

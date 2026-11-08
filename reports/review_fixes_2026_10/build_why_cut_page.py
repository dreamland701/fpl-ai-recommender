"""Build the GW6 'why did the SFT cut?' page from sft_interpret_v2_gw6.json (+ expectation results if present).

usage: build_why_cut_page.py <out.html>
"""
import html
import json
import os
import re
import sys

ROOT = "/home/wescheng/projects/fpl/fpl"
R = f"{ROOT}/reports/review_fixes_2026_10"
ORDER = ["Groß", "Rogers", "B.Fernandes", "Haaland", "De Cuyper", "Isak", "Konsa", "João Pedro"]
CLUB = {"Groß": "Brighton MID", "Rogers": "Chelsea MID", "B.Fernandes": "Man Utd MID", "Haaland": "Man City FWD",
        "De Cuyper": "Brighton DEF", "Isak": "Liverpool FWD", "Konsa": "Arsenal DEF", "João Pedro": "Chelsea FWD"}
ROLE = {"Groß": "your captain", "Rogers": "in the frozen wildcard draft", "B.Fernandes": "yours; sold in the GW7 plan",
        "Haaland": "GW7 target", "De Cuyper": "your GW6 signing", "Isak": "yours; sold in the GW7 plan",
        "Konsa": "yours (bench)", "João Pedro": "yours (bench)"}
ARTICLES = {
    "Groß": ["Guardian live blog, 2 Oct: Brighton swept September's Premier League awards. Groß is Player of the Month, "
             "Hürzeler Manager of the Month, Dunk Goal of the Month. Nothing about fitness or role."],
    "Rogers": ["Guardian, England 3-0 Czechia (6 Oct): the second-string wingers 'put in a fine shift, Morgan Rogers especially'.",
               "Guardian, Croatia 0-7 England (3 Oct): Rogers ran through and rounded the keeper to score, and was later "
               "clipped in the box. Positive form, and two internationals in four days just before GW6."],
    "B.Fernandes": [],
    "Haaland": ["Premier League Scout, 2 Oct: Haaland ranked the most important premium to own (39 points in GW1-5).",
                "Guardian, 4 Oct, 'Haaland limps off': he asked to come off around the 67th minute for Norway. "
                "A real fitness flag."],
    "De Cuyper": ["Premier League, 1 Oct: Brighton assets are popular; De Cuyper among the most-bought players (306k transfers in).",
                  "Guardian Nations League blog, 28 Sep: Olise twice beat De Cuyper for pace in Belgium 0-1 France. "
                  "Mildly negative about his defending, mostly noise."],
    "Isak": ["Premier League Scout, 2 Oct: Isak ranked among the best premium picks (33 points in GW1-5).",
             "Guardian, 27 Sep: Isak returned to Liverpool injured and missed Sweden's remaining Nations League games."],
    "Konsa": ["Guardian, Czechia 0-2 England (29 Sep): Konsa was a forced absence from England's defence.",
              "Guardian, 28 Sep: Konsa 'has lacked consistency' alongside Guéhi; Tuchel paired them in 7 of the last 13."],
    "João Pedro": ["Premier League, 28 Sep, 'injury chaos': João Pedro is one of three injured top-six forwards and the most-sold player.",
                   "Premier League, 6 Oct: price changes; João Pedro among the top transfers out (438k) and a price faller."],
}
SECTION = """
<section class="block" id="conservative"><h2>Is the SFT too conservative?</h2>
<p>No. The small expected adjustments are the honest size of what the text tells it, and the large written cuts are an artefact of how
the number is written. Four pieces of evidence:</p>
<h4>1 · What it was taught: the typical week, not the average week</h4>
<p>Training targets were 35% of the real surprise (actual minus classic), capped at ±2. FPL points are skewed: most weeks a player
scores a bit under his forecast and now and then he hauls. So for high forecasts the typical surprise is well below zero while the
average is close to zero. A model that writes its most likely value learns the typical one.</p>
<div class="tablewrap"><table><thead><tr><th>Classic forecast</th><th class="num">Training rows</th><th class="num">Average surprise</th>
<th class="num">Typical (median) surprise</th><th class="num">Weeks below forecast</th></tr></thead><tbody>
<tr><td>2-3 pts</td><td class="num">16,952</td><td class="num">+0.15</td><td class="num">−0.74</td><td class="num">70%</td></tr>
<tr><td>3-4 pts</td><td class="num">6,733</td><td class="num">+0.22</td><td class="num">−1.14</td><td class="num">66%</td></tr>
<tr><td>4-5 pts</td><td class="num">1,771</td><td class="num">+0.10</td><td class="num">−1.45</td><td class="num">61%</td></tr>
<tr><td>5-6 pts</td><td class="num">612</td><td class="num">−0.12</td><td class="num">−1.85</td><td class="num">60%</td></tr>
<tr><td>6-7 pts</td><td class="num">267</td><td class="num">−0.52</td><td class="num">−1.95</td><td class="num">64%</td></tr>
<tr><td>7+ pts</td><td class="num">267</td><td class="num">−2.39</td><td class="num">−3.43</td><td class="num">72%</td></tr>
</tbody></table></div>
<p class="cap">E20 training split, 35,840 player-weeks from 2022-23 to 2025-26 GW26. Surprise = actual points − classic forecast.
The cuts can look like a "hot players cool off" rule, but they come from this skew: the streak test found no cooling beyond the classic forecast (t = −0.24).</p>
<h4>2 · Scaling the player-specific part up does not help</h4>
<p>Undoing the 35% (multiplying the player-specific part by 2.86) makes forecasts worse on both the 2025-26 holdout and the live season.
The best multiplier is about 1.5 on the holdout and 0.5 to 1 live, and even there the gain is about 0.003 RMSE. The text signal is weak, so
the small size is right.</p>
<h4>3 · The part that reflects the text already costs squad points</h4>
<div class="tablewrap"><table><thead><tr><th>Holdout squad backtest, 2025-26 GW27-38</th><th class="num">Points</th><th class="num">vs classic+F6</th></tr></thead><tbody>
<tr><td>Classic + F6 (what decides now)</td><td class="num">753</td><td class="num">0</td></tr>
<tr><td>SFT points adjustments, as written</td><td class="num">704</td><td class="num cut">−49</td></tr>
<tr><td>Only the shrink every player gets</td><td class="num">752</td><td class="num">−1</td></tr>
<tr><td>Only the player-specific remainder</td><td class="num">715</td><td class="num cut">−38</td></tr>
<tr><td>Only its availability adjustments</td><td class="num">753</td><td class="num">0</td></tr>
</tbody></table></div>
<p class="cap">Three 4-week windows. Noise is about 24 points per window, so −49 is about −1.2 standard deviations: not proof of harm,
but no sign of help either.</p>
<h4>4 · The one genuinely timid part is availability, and fixing it has not paid</h4>
<p>Its appearance-probability adjustments are better calibrated at 1.5 to 2 times their size (Brier 0.124 → 0.109 on the holdout,
0.100 → 0.096 live). Routing them into points looked good on the holdout (+36 and +45) but did not replicate on 18 other windows (−107
and +35) or the live season (−4 and −4).</p>
{EXPECTATION}
<h4>What to change</h4>
<ul class="arts">
<li><b>Read its average, not its most likely value.</b> Done (section 5): +41 squad points over the written numbers across four windows,
level with classic, and the best accuracy. The weekly sheet now shows this view next to the written one.</li>
<li><b>Train for the average.</b> Targets on the average surprise (uncapped or winsorised), or have it output a few probability bins
and take the expectation, so the shrink is not baked in.</li>
<li><b>Give the LLM a narrower job.</b> Extract facts the classic model cannot see (injury wording, rotation, role changes) as features,
and leave the points arithmetic to the classic model. The availability edge is the only consistent signal so far.</li>
</ul>
</section>"""
FACTOR_LABEL = {"forecast": "Forecast level", "playing_time": "Minutes & status", "fixtures": "Fixtures GW6-10",
                "text": "The articles", "name": "His name", "defcon": "DefCon stats"}


def esc(s):
    return html.escape(str(s))


def waterfall_svg(r, lo=-1.3, hi=0.5):
    """Rows: neutral start, six factor steps, expected value; written value marked on its own row."""
    w, left, right, row_h, top = 560, 210, 24, 26, 26
    span = w - left - right
    x = lambda v: left + (min(max(v, lo), hi) - lo) / (hi - lo) * span
    steps = [("Average starter, no news", None, r["fully_neutral"]["mean"])]
    run = r["fully_neutral"]["mean"]
    for f in ["forecast", "playing_time", "fixtures", "text", "name", "defcon"]:
        steps.append((FACTOR_LABEL[f], run, run + r["shapley"][f]))
        run += r["shapley"][f]
    rows = len(steps) + 2
    hgt = top + rows * row_h + 18
    out = [f'<svg viewBox="0 0 {w} {hgt}" role="img" aria-label="Contribution of each input to the expected cut">']
    for t in [v / 10 for v in range(int(lo * 10), int(hi * 10) + 1, 2)]:
        out.append(f'<line x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{top - 6}" y2="{hgt - 18}" class="{"axis0" if abs(t) < 1e-9 else "grid"}"/>')
        out.append(f'<text x="{x(t):.1f}" y="{top - 10}" class="tick" text-anchor="middle">{t:+.1f}</text>')
    for i, (label, a, b) in enumerate(steps):
        y = top + i * row_h
        out.append(f'<text x="{left - 10}" y="{y + 17}" class="lab" text-anchor="end">{esc(label)}</text>')
        if a is None:
            out.append(f'<circle cx="{x(b):.1f}" cy="{y + 13}" r="5" class="dot"/>')
            out.append(f'<text x="{x(b) + 9:.1f}" y="{y + 17}" class="val">{b:+.2f}</text>')
        else:
            x0, x1 = sorted((x(a), x(b)))
            cls = "neg" if b < a else "pos"
            out.append(f'<rect x="{x0:.1f}" y="{y + 6}" width="{max(x1 - x0, 1.5):.1f}" height="14" rx="2" class="{cls}"/>')
            tx, anchor = (x0 - 6, "end") if b < a else (x1 + 6, "start")
            if b < a and x0 - 6 < left + 30:
                tx, anchor = x1 + 6, "start"
            out.append(f'<text x="{tx:.1f}" y="{y + 17}" class="val" text-anchor="{anchor}">{b - a:+.2f}</text>')
    y = top + len(steps) * row_h
    mean = r["original"]["mean"]
    out.append(f'<line x1="{left - 200}" x2="{w - right}" y1="{y + 2}" y2="{y + 2}" class="rule"/>')
    out.append(f'<text x="{left - 10}" y="{y + 19}" class="lab strong" text-anchor="end">Expected (its average)</text>')
    out.append(f'<circle cx="{x(mean):.1f}" cy="{y + 15}" r="6" class="dot strong"/>')
    out.append(f'<text x="{x(mean) + 10:.1f}" y="{y + 19}" class="val strong">{mean:+.2f}</text>')
    y += row_h
    g = r["live_decode"]
    gx = x(g)
    clipped = g < lo
    out.append(f'<text x="{left - 10}" y="{y + 19}" class="lab" text-anchor="end">Written (most likely)</text>')
    out.append(f'<path d="M{gx - 6:.1f},{y + 21} L{gx + 6:.1f},{y + 21} L{gx:.1f},{y + 10} Z" class="written"/>')
    out.append(f'<text x="{gx + 10:.1f}" y="{y + 19}" class="val">{g:+.1f}{" (off scale)" if clipped else ""}</text>')
    out.append("</svg>")
    return "".join(out)


def dist_svg(r):
    probs = {float(k): v for k, v in r["original"]["probs"].items()}
    w, h, left, bottom, top = 560, 150, 10, 26, 14
    vals = [round(-2 + 0.1 * i, 1) for i in range(41)]
    bw = (w - 2 * left) / 41
    pmax = max(probs.values())
    sc = lambda p: (h - bottom - top) * p / pmax
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Probability of each adjustment value">']
    for i, v in enumerate(vals):
        p = probs.get(v, 0.0)
        cls = "neg" if v < 0 else ("zero" if v == 0 else "pos")
        out.append(f'<rect x="{left + i * bw + 1:.1f}" y="{h - bottom - sc(p):.1f}" width="{bw - 2:.1f}" height="{max(sc(p), 0.5):.1f}" class="{cls}"/>')
    xv = lambda v: left + (v + 2.05) / 4.1 * (w - 2 * left)
    for t in (-2, -1, 0, 1, 2):
        out.append(f'<text x="{xv(t):.1f}" y="{h - 8}" class="tick" text-anchor="middle">{t:+d}</text>')
    m = r["original"]["mean"]
    out.append(f'<line x1="{xv(m):.1f}" x2="{xv(m):.1f}" y1="{top - 4}" y2="{h - bottom}" class="meanline"/>')
    out.append(f'<text x="{xv(m) + 5:.1f}" y="{top + 6}" class="val strong">average {m:+.2f}</text>')
    g = r["live_decode"]
    out.append(f'<path d="M{xv(g) - 6:.1f},{h - bottom + 9} L{xv(g) + 6:.1f},{h - bottom + 9} L{xv(g):.1f},{h - bottom + 1} Z" class="written"/>')
    out.append("</svg>")
    return "".join(out)


def sgn(v, nd=2):
    return f"{v:+.{nd}f}".replace("-", "−")


def verdict(name, r):
    s = r["shapley"]; o = r["original"]
    biggest = min(s, key=s.get)
    parts = [f"Writes {sgn(r['live_decode'], 1)} but expects {sgn(o['mean'])} ({o['p_cut']:.0%} chance of any cut)."]
    parts.append(f"The largest push down is {FACTOR_LABEL[biggest].lower()} ({sgn(s[biggest])}).")
    t = s["text"]
    if biggest == "text":
        pass
    elif ARTICLES[name]:
        if abs(t) < 0.05:
            parts.append(f"The articles barely matter ({sgn(t)}).")
        else:
            parts.append(f"The articles {'push it up' if t > 0 else 'pull it down'} ({sgn(t)}).")
    else:
        parts.append("No articles this week, so none of this is about text.")
    return " ".join(parts)


def main() -> None:
    out_path = sys.argv[1]
    d = json.load(open(f"{R}/sft_interpret_v2_gw6.json"))
    news = {}
    for l in open(f"{ROOT}/reports/live_gw6_2627_f6_examples.jsonl"):
        e = json.loads(l)
        if e["metadata"]["player_name"] in ORDER:
            m = re.search(r"Official player news pre-deadline: (.*)", e["prompt"])
            news[e["metadata"]["player_name"]] = m.group(1).strip() if m and m.group(1).strip() != "none" else ""
    players = [p for p in ORDER if p in d]
    exp_log = ""
    if os.path.exists(f"{ROOT}/logs/expectation_chain.log"):
        exp_log = open(f"{ROOT}/logs/expectation_chain.log").read()
    rows = "".join(
        f"<tr><td>{esc(p)}<span class='sub'>{esc(CLUB[p])}</span></td><td class='num'>{d[p]['baseline_points_1gw']:.2f}</td>"
        f"<td class='num cut'>{d[p]['live_decode']:+.1f}</td><td class='num'>{d[p]['original']['mean']:+.2f}</td>"
        f"<td class='num'>{d[p]['original']['p_cut']:.0%}</td><td class='num'>{d[p]['shapley']['forecast']:+.2f}</td>"
        f"<td class='num'>{d[p]['shapley']['text']:+.2f}</td></tr>" for p in players)
    cards = []
    for p in players:
        r = d[p]
        arts = "".join(f"<li>{esc(a)}</li>" for a in ARTICLES[p]) or "<li class='muted'>No articles matched him this week.</li>"
        cards.append(f"""
<section class="player" id="{esc(p).replace('.', '').replace(' ', '-').lower()}">
  <header><h3>{esc(p)}</h3><p class="meta">{esc(CLUB[p])} · {esc(ROLE[p])} · classic {r['baseline_points_1gw']:.2f}
  → SFT wrote {r['baseline_points_1gw'] + r['live_decode']:.2f}, its average {r['baseline_points_1gw'] + r['original']['mean']:.2f}{(' · news: ' + esc(news[p])) if news.get(p) else ''}</p></header>
  <p class="verdict">{esc(verdict(p, r))}</p>
  <div class="cols">
    <div class="col"><h4>What it read</h4><ul class="arts">{arts}</ul>
      <h4>Its spread of possible adjustments</h4>{dist_svg(r)}
      <p class="cap">Bars: probability of each value from −2.0 to +2.0. Line: the average. Triangle: the number it wrote.</p></div>
    <div class="col"><h4>Where the expected adjustment comes from</h4>{waterfall_svg(r)}
      <p class="cap">Each input swapped for a neutral version over all 64 on/off combinations (Shapley values). The steps add up exactly
      to the expected adjustment.</p></div>
  </div>
</section>""")
    exp_block = ""
    if "EXPECTATION CHAIN DONE" in exp_log:
        exp_block = """<h4>5 · Reading its average instead (expectation decoding), tested 9 October</h4>
<p>Same adapter, no retraining: every points adjustment replaced by the average of its own spread, then the same squad backtests.</p>
<div class="tablewrap"><table><thead><tr><th>Squad points</th><th class="num">Classic + F6</th><th class="num">SFT as written</th>
<th class="num">SFT average</th></tr></thead><tbody>
<tr><td>Holdout 2025-26 GW27-30</td><td class="num">266</td><td class="num">225</td><td class="num">224</td></tr>
<tr><td>Holdout 2025-26 GW31-34</td><td class="num">229</td><td class="num">216</td><td class="num">248</td></tr>
<tr><td>Holdout 2025-26 GW35-38</td><td class="num">258</td><td class="num">263</td><td class="num">264</td></tr>
<tr><td>Live 2026-27 GW2-5</td><td class="num">242</td><td class="num">247</td><td class="num">256</td></tr>
<tr><td><b>Four windows</b></td><td class="num"><b>995</b></td><td class="num cut"><b>951</b></td><td class="num"><b>992</b></td></tr>
</tbody></table></div>
<div class="tablewrap"><table><thead><tr><th>1-week accuracy (RMSE, bias)</th><th class="num">Classic + F6</th><th class="num">SFT as written</th>
<th class="num">SFT average</th></tr></thead><tbody>
<tr><td>Holdout, 3,072 player-weeks</td><td class="num">3.025, +0.04</td><td class="num">3.039, −0.44</td><td class="num"><b>2.972, +0.02</b></td></tr>
<tr><td>Live season, 1,024 player-weeks</td><td class="num">3.086, −0.21</td><td class="num">3.151, −0.65</td><td class="num">3.082, −0.20</td></tr>
</tbody></table></div>
<p>Reading the average removes the bias and gives the best accuracy of the three. In squad terms it wins back 41 of the 44 points the
written numbers lose over four windows and finishes level with classic. That makes it a clear improvement on the written numbers, but
still no evidence that the SFT adds decision value on top of classic: with about 24 points of noise per window, a 3-point gap over four windows is noise.</p>"""
    conservative = SECTION.replace("{EXPECTATION}", exp_block)
    page = f"""<title>GW6 SFT Cut Anatomy</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@500;600;700&family=Source+Sans+3:wght@400;600&display=swap">
<style>
/* Layout: one reading column; each player is a two-column card (text + spread | waterfall) that stacks on phones. */
:root {{
  --bg: #f4f6f2; --panel: #ffffff; --ink: #1c2320; --muted: #5d6a63; --line: #d6ddd7;
  --cut: #b5472e; --rise: #1f7a62; --zero: #8d9a92; --accent: #24463c;
  --display: "Barlow Semi Condensed", "Arial Narrow", system-ui, sans-serif;
  --body: "Source Sans 3", "Segoe UI", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #121614; --panel: #1a201d; --ink: #e5ebe7; --muted: #9aa8a0; --line: #2f3833;
  --cut: #e07a5f; --rise: #4fbf9c; --zero: #6f7d75; --accent: #a9d3c3; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --bg: #121614; --panel: #1a201d; --ink: #e5ebe7; --muted: #9aa8a0; --line: #2f3833;
  --cut: #e07a5f; --rise: #4fbf9c; --zero: #6f7d75; --accent: #a9d3c3; color-scheme: dark; }}
body {{ background: var(--bg); color: var(--ink); font: 16px/1.55 var(--body); }}
main {{ max-width: 980px; margin: 0 auto; padding-inline: 16px; padding-block: 28px 56px; display: grid; gap: 28px; }}
h1, h2, h3, h4 {{ font-family: var(--display); text-wrap: balance; margin: 0; letter-spacing: .01em; }}
h1 {{ font-size: 2.3rem; line-height: 1.1; }} h2 {{ font-size: 1.55rem; }} h3 {{ font-size: 1.35rem; }}
h4 {{ font-size: .82rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin-top: 6px; }}
p {{ margin: 0; max-width: 70ch; }} .lede {{ font-size: 1.08rem; }}
.muted, .cap, .meta, .sub {{ color: var(--muted); }} .cap {{ font-size: .85rem; }}
.keys {{ display: grid; gap: 14px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }}
.key {{ background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 14px 16px; display: grid; gap: 6px; min-width: 0; }}
.key b {{ font-family: var(--display); font-size: 1.1rem; }}
.tablewrap {{ overflow-x: auto; }} table {{ border-collapse: collapse; width: 100%; font-variant-numeric: tabular-nums; }}
th, td {{ text-align: left; padding: 7px 10px; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ font: 600 .8rem var(--body); text-transform: uppercase; letter-spacing: .06em; color: var(--muted); }}
td.num, th.num {{ text-align: right; white-space: nowrap; }} td.cut {{ color: var(--cut); font-weight: 600; }}
.sub {{ display: block; font-size: .8rem; }}
.player {{ background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 18px; display: grid; gap: 12px; }}
.player header {{ display: grid; gap: 2px; }} .verdict {{ font-weight: 600; }}
.cols {{ display: grid; grid-template-columns: 1fr 1.15fr; gap: 22px; }} .col {{ min-width: 0; display: grid; gap: 8px; align-content: start; }}
@media (max-width: 760px) {{ .cols {{ grid-template-columns: 1fr; }} }}
ul.arts {{ margin: 0; padding-left: 18px; display: grid; gap: 6px; }}
svg {{ width: 100%; height: auto; display: block; }}
svg .tick {{ font: 12px var(--body); fill: var(--muted); }} svg .lab {{ font: 13.5px var(--body); fill: var(--ink); }}
svg .val {{ font: 13px var(--body); fill: var(--ink); font-variant-numeric: tabular-nums; }}
svg .strong {{ font-weight: 600; }} svg .grid {{ stroke: var(--line); stroke-width: 1; }} svg .axis0 {{ stroke: var(--muted); stroke-width: 1.2; }}
svg .rule {{ stroke: var(--line); stroke-width: 1; }} svg .neg {{ fill: var(--cut); }} svg .pos {{ fill: var(--rise); }}
svg .zero {{ fill: var(--zero); }} svg .dot {{ fill: var(--accent); }} svg .written {{ fill: var(--cut); }}
svg .meanline {{ stroke: var(--accent); stroke-width: 2; }}
section.block {{ display: grid; gap: 12px; }}
pre.res {{ overflow-x: auto; background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 12px; font-size: .82rem; }}
</style>
<main>
<header style="display:grid;gap:10px">
  <p class="muted">FPL · E20 SFT adapter · Gameweek 6 shadow read</p>
  <h1>Why the SFT cut your players</h1>
  <p class="lede">The SFT writes one number per player, but behind it is a full spread of possible adjustments. I read that spread
  directly from the model, then swapped each input for a neutral version to see which ones move it. The scorer reproduces the live
  outputs exactly, so these are the same model's own numbers, not a separate guess.</p>
</header>
<div class="keys">
  <div class="key"><b>The written number is not its belief</b><p>It writes the single most likely value. For these eight players the
  written cuts average −0.92, while the averages of its own spreads average −0.17. Its chance of any cut is 50 to 67% for every one of
  them, close to a coin flip on direction. Writing digit by digit picks "cut" first, then the most likely size of a cut, and drops the
  33 to 50% chance of a rise.</p></div>
  <div class="key"><b>Forecast level drives the expected cut</b><p>The biggest push down is the size of the classic forecast (Haaland
  −0.51, Groß −0.49, Bruno −0.40). It learned that high forecasts usually fall short in a typical week. The articles move it by only
  −0.12 to +0.10, but with sensible signs: praise up (Rogers +0.10, Groß +0.06), worries down (Konsa −0.12, Haaland −0.10).</p></div>
  <div class="key"><b>Too conservative? The opposite</b><p>The written cuts are exaggerated by how the number is written. Reading its
  average instead wins back 41 of the 44 squad points the written numbers lose and ends level with classic. Making the cuts bigger
  would make things worse.</p></div>
</div>
<section class="block"><h2>The eight players at a glance</h2>
<div class="tablewrap"><table><thead><tr><th>Player</th><th class="num">Classic</th><th class="num">Wrote</th><th class="num">Expected</th>
<th class="num">P(cut)</th><th class="num">From forecast level</th><th class="num">From articles</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="cap">Classic and adjustments in FPL points for GW6. Expected = average of the SFT's own probability spread.</p></section>
<section class="block"><h2>Your GW6 XI three ways</h2>
<div class="tablewrap"><table><thead><tr><th></th><th>Classic (decides)</th><th>Classic + SFT as written</th><th>Classic + SFT average</th></tr></thead><tbody>
<tr><td>Goalkeeper</td><td>Sels</td><td>Sels</td><td>Donnarumma</td></tr>
<tr><td>Outfield ten</td><td colspan="3">De Cuyper, N.Williams, Mitchell, Groß, B.Fernandes, Saka, Cherki, Cunha, Isak, Evanilson (same in all three)</td></tr>
<tr><td>Bench order</td><td>Donnarumma, João Pedro, Justin, Konsa</td><td>Donnarumma, Justin, Konsa, João Pedro</td><td>Sels, João Pedro, Konsa, Justin</td></tr>
<tr><td>Captain / vice</td><td colspan="3">Groß / B.Fernandes (same in all three)</td></tr>
<tr><td>Squad total, own forecasts</td><td class="num">53.1</td><td class="num">44.6</td><td class="num">51.9</td></tr>
</tbody></table></div>
<p class="cap">With Bijol → De Cuyper applied. The written numbers shave 8.5 points off the squad; its average shaves 1.2. The goalkeeper call
is a coin flip either way (classic: Sels by 0.01; SFT average: Donnarumma by 0.11).</p></section>
{''.join(cards)}
{conservative}

<section class="block" id="method"><h2>How this was measured</h2>
<p>The adapter writes each delta as sign, digit, point, digit, so the probability of every value from −2.0 to +2.0 can be read off
exactly from one prompt pass plus a few short continuations. For the attribution, six inputs were swapped for neutral versions, and the
average was recomputed for all 64 on/off combinations:</p>
<ul class="arts">
<li><b>Forecast level:</b> classic 1/3/5-week points replaced by an average starter's 4.0 / 11.0 / 18.0.</li>
<li><b>Minutes &amp; status:</b> 85 minutes, 95% chance to appear, status available, no news.</li>
<li><b>Fixtures:</b> every GW6-10 opponent replaced by a difficulty-3 placeholder (home/away kept).</li>
<li><b>Articles:</b> replaced by the standard "no evidence" sentence. <b>Name:</b> "Player A". <b>DefCon stats:</b> line removed, as in 2022-25 prompts.</li>
</ul>
<p>Checks: for all eight players the scored most-likely value equals the live GW6 output, a fresh one-at-a-time decode and a re-run of the
original 16-player batch. The cached shortcut matches full passes to within 0.007 probability. An earlier version of this tool loaded the
model differently and gave wrong spreads; it has been replaced.</p>
<p class="cap">Code: reports/review_fixes_2026_10/sft_interpret_v2.py (attribution), scripts/expectation_decode.py (averages for whole weeks).
Data: sft_interpret_v2_gw6.json.</p>
</section>
</main>"""
    open(out_path, "w").write(page)
    print(f"wrote {out_path} ({len(page) // 1024} KB, {len(players)} players)")


if __name__ == "__main__":
    main()

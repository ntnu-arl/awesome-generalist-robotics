# SPDX-License-Identifier: MIT
"""Render the self-contained GitHub Pages reading interface."""
from collections import Counter
import html

REPO = "https://github.com/ntnu-arl/awesome-generalist-robotics"
SITE = "https://ntnu-arl.github.io/awesome-generalist-robotics/"


def render_site(data):
    esc = html.escape
    entries = sorted(data['entries'], key=lambda e: (-(e['year'] or 0), e['title'].casefold(), e['id']))
    years = sorted({e['year'] for e in entries if e['year']}, reverse=True)
    periods = years + ([None] if any(e['year'] is None for e in entries) else [])
    counts = Counter(e['year'] for e in entries)
    nav = ''.join(f'<a href="#{year or "undated"}" data-year-link="{year or "undated"}"><span>{year or "Undated"}</span><span class="year-count">{counts[year]}</span></a>' for year in periods)
    options = ''.join(f'<option value="{year or "undated"}">{year or "Undated"}</option>' for year in periods)
    sections = []
    for year in periods:
        label = str(year) if year else 'Undated'
        records = []
        for e in entries:
            if e['year'] != year:
                continue
            search = ' '.join([str(e.get(k, '')) for k in ('title', 'summary', 'first_author', 'publication_note')] + e.get('authors', [])).lower()
            authors = e.get('authors', [])
            author_line = ('<details class="authors"><summary>' + str(len(authors)) + (' author' if len(authors) == 1 else ' authors') + '</summary><p>' + esc('; '.join(authors)) + '</p></details>') if authors else '<p class="author-unavailable">' + esc(e.get('authors_note', 'Author list not yet verified.')) + '</p>'
            records.append(f'''<article class="paper" id="{esc(e['id'])}" data-search="{esc(search, quote=True)}">
<div class="paper-meta"><span>{label}</span><span>{esc(e['resource_type'].capitalize())}</span></div>
<h3><a href="{esc(e['url'], quote=True)}">{esc(e['title'])}</a></h3>
{author_line}
<p>{esc(e['summary'])}</p>
<a class="paper-link" href="{esc(e['url'], quote=True)}">Read {"project" if e['resource_type'] == "project" else "paper"} <span aria-hidden="true">↗</span></a>
</article>''')
        sections.append(f'''<section class="year-section" id="{year or 'undated'}" data-year="{year or 'undated'}" aria-labelledby="heading-{year or 'undated'}">
<div class="year-heading"><h2 id="heading-{year or 'undated'}">{label}</h2><span class="section-count">{counts[year]} references</span></div>
{''.join(records)}
</section>''')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome Generalist Robotics</title>
<meta name="description" content="A curated collection of research on generalist robot policies, cross-embodiment learning, and unified embodied autonomy.">
<meta name="theme-color" content="#10243a">
<link rel="canonical" href="{SITE}">
<meta property="og:title" content="Awesome Generalist Robotics">
<meta property="og:description" content="Shared competence. Diverse embodiments. Research on generalist robot policies and unified embodied autonomy.">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/site.css">
<script src="assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#collection">Skip to references</a>
<header class="site-header"><div class="header-inner"><a class="wordmark" href="./" aria-label="Awesome Generalist Robotics home"><span class="mark" aria-hidden="true">G</span>GENERALIST ROBOTICS</a><nav aria-label="Main"><a href="{REPO}">GitHub <span aria-hidden="true">↗</span></a><a href="{REPO}/issues/new/choose">Suggest a paper <span aria-hidden="true">↗</span></a></nav></div></header>
<main>
<section class="hero" aria-labelledby="page-title"><div class="eyebrow">A CURATED RESEARCH COLLECTION</div><h1 id="page-title">Awesome<br>Generalist Robotics<span class="title-dot">.</span></h1><p class="standfirst">Shared competence. Diverse embodiments.</p><p class="intro">Research on generalist robot policies, cross-embodiment learning, and unified embodied autonomy. Explore shared policies, representations, world models, and control across tasks, environments, sensors, and robot bodies.</p><div class="hero-meta"><span><strong>{len(entries)}</strong> references</span><span><strong>{len(years)}</strong> years</span><span>Updated <time datetime="{data['updated']}">{data['updated']}</time></span></div></section>
<div class="collection-layout" id="collection">
<aside class="year-nav"><div class="nav-label">BROWSE BY YEAR</div><nav aria-label="Publication years">{nav}</nav><a class="catalogue-link" href="data/catalog.json" download>Download catalogue ↓</a></aside>
<div class="results-column">
<div class="search-tools" id="search-tools" hidden><form id="search-form" role="search"><div class="search-field"><label for="search">Search the collection</label><input type="search" id="search" placeholder="Search titles, authors, or keywords…" autocomplete="off"></div><div class="year-field"><label for="year-filter">Year</label><select id="year-filter"><option value="all">All years</option>{options}</select></div><button type="button" id="clear" hidden>Clear</button></form><p id="results-status" role="status" aria-live="polite">Showing all {len(entries)} references</p></div>
<noscript><p class="reading-note">All references are available below. Search is available when JavaScript is enabled.</p></noscript>
<p class="reading-note">Newest years first, alphabetical within each year. Dates follow first arXiv submission when available, otherwise the publication record.</p>
<div id="papers">{''.join(sections)}</div>
<p id="empty" class="empty" hidden>No references match your search. Try a different term or year.</p>
</div></div>
<section class="about" id="about"><div class="eyebrow">ABOUT THE COLLECTION</div><h2>A reading list for shared robotic competence.</h2><p>This collection covers manipulation, navigation, locomotion, and multiple robot morphologies, together with directly relevant datasets, benchmarks, and surveys. Entries describe contributions; inclusion does not imply independent replication or universal transfer.</p><div class="about-links"><a href="{REPO}/blob/main/docs/curation.md">Curation policy ↗</a><a href="{REPO}/blob/main/CONTRIBUTING.md">Contribution guide ↗</a><a href="{REPO}/blob/main/README.md">Read on GitHub ↗</a></div></section>
</main>
<footer><div><strong>Awesome Generalist Robotics</strong><p>Original text and artwork: <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Linked works retain their own licenses.</p><p>Initial reference discovery includes <a href="https://github.com/cheryyunl/awesome-generalist-agents">Awesome Generalist Agents</a>. Please cite the original papers for research claims.</p></div><a class="back-top" href="#page-title">Back to top ↑</a></footer>
</body>
</html>
'''

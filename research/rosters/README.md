# ATP-only player universe – 16 November 2026 snapshot

**Goal:** Restrict the private ATP Intelligence `Player Intelligence` records to elite men's singles players, not Challenger/ITF rosters.

## Selection rule (version 1)

1. **ATP Top 100** in the singles ranking effective **2026-11-16**.
2. Independently cross-check each ranking slot against the 2026 men's main-draw season summary. All 100 have at least one main-draw singles match (wins+losses > 0).
3. Do not create active profiles for ranking positions **101+**, retired players, or Challenger-only/ITF-only players.
4. The *analysis target events* are ATP 250/500/Masters 1000/ATP Finals and Grand Slams. A Grand Slam is not administered by the ATP Tour, but is deliberately included as top-level professional singles competition.
5. Historical Challenger notes may inform a **current Top-100** player's longer-term history, but there is no separate live Challenger prediction or low-ranked player profile.

This is a **product scope policy**, not a claim that rank 101 is intrinsically incapable of ATP-level tennis. Rankings change weekly; the eligibility set must be refreshed and tested before live deployment. A Top 100 athlete may play Challenger occasionally and remains eligible.

## Data

[atp_top100_2026_11_16.csv](atp_top100_2026_11_16.csv) contains 100 rows, with rank, full name, country, points, dated ranking, season main-draw W/L, verification flag and both source URLs.

- Ranking: [Tennis.esp.br, ATP 2026-11-16](https://www.tennis.esp.br/en/rankings?date=2026-11-16&tour=ATP).
- Independent season summary: [TennisDB, 2026 ATP rankings and match summary](https://tennis-db.com/seasons-and-rankings?year=2026).
- Ranking top positions also corroborated by [TennisTemple](https://en.tennistemple.com/rankings/atp) and [Tennis Explorer](https://www.tennisexplorer.com/ranking/atp-men/2026/).
- ATP official live rankings: [atptour.com/rankings/singles](https://www.atptour.com/rankings/singles). Dynamic/cached ATP output was stale in the tool session, so it was **not** the downloaded 16 November snapshot.

Minor source spelling variant at rank 100: **Alexander / Aleksandr Shevchenko** (equal rank and points). Stored as Alexander; player ID alignment required when an official ATP player ID becomes available.

**IMPORTANT:** Several web caches reported 9,350 points for Zverev while the chosen 16 November snapshot and TennisDB/TennisTemple report 9,320. The CSV records 9,320, and source edition matters. Do not mix update dates or ATP Race data with 52-week ranking data.

## Current code guard

- [atp_intelligence/roster.py](../../atp_intelligence/roster.py): parses and validates exactly 100 unique players with 2026 main-draw evidence.
- [atp_intelligence/archive.py](../../atp_intelligence/archive.py): imports ONLY Top-100 player mentions and expert observations into the application SQLite archive. Out-of-scope names may remain in **research-source CSV** for bibliographic provenance; they are excluded from persistent active player/observation tables.
- On import, old out-of-scope player/observation records in an existing database are purged. The 100 eligible roster records are recreated.

The source lists, expert opinions and age-old descriptions are **not** current form or mental-state measurements. No live roster updating or paid licensed matchfeed is integrated yet.

## Upgrade path

Refresh weekly with a legally accessible provider, map stable ATP player IDs, reconcile career/retirement/long-term absences, and only use new ranking editions after successful consistency checks. Keep historical snapshots as versioned input data, not as automatically current rankings.

## Clarification: match eligibility vs deep player profile

**This clarification supersedes the overly strict phrasing of selection rule #3 above.** ATP Top 100 is the **full continuously researched profile cohort**, *not* the only players eligible for match analysis.

- **Match eligibility:** men's main draw singles at ATP 250, ATP 500, Masters 1000, ATP Finals, or Grand Slams, regardless of participant rankings (including qualifiers, wild cards, special exemptions, etc. once in the main draw).
- **Tier A deep profiles:** current Top 100 and active top-level participants, with extensive ongoing coaching-history data; v1 code currently uses Top 100 as the conservative primary cohort.
- **Tier B temporary matchup profiles:** outside Top 100, but appearing in a concrete in-scope main-draw match; enough verified information to analyze both players. Not automatically monitored long term.
- **Tier C excluded:** Challenger/ITF-only match coverage, no systematic player profiles.
- The Top100 roster guard currently filters **persistent expert archive profiles**, not event-level match entries. It must **never** be used by itself to hide a qualifying ATP/Grand Slam main draw match from the live application.

**Not implemented yet:** a separate verified event-based match-eligibility checker, and a temporary Tier-B matchup player model. They must be added before enforcing the scope in the Streamlit UI.

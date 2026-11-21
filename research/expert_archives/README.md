# Expert archive: provenance-first, historical, not a live player rating

This folder contains the **first verified source index**, not the complete archives of Damian Kust or Jakub Bobro.

## Dataset as of 2026-11-21

| File | Meaning | Count |
|---|---|---:|
| [sources.csv](sources.csv) | 3 historic podcast episodes and 2 Damian Kust articles (2022–2024) | 5 |
| [player_mentions_2026_11_21.csv](player_mentions_2026_11_21.csv) | Named players, original episode/article, their 2026 competition or retirement status and separate status evidence URL | 21 |
| [historical_observations.csv](historical_observations.csv) | Short attributed Hungarian paraphrases; individual verification labels | 11 |

[Notion archive guide](https://app.notion.com/p/41ff603f0d2e81ffb621da1e4ac4675f)

## Meanings of playing_status

- `competitive_2026_atp_or_challenger`: supported participation during 2026, **not** proof that the player is scheduled today, fit, or will remain active next season.
- `retired_confirmed`: explicit retirement announcement / official recognition (Novak 2025; Berankis 2025; Goffin 2026).
- `on_break_not_retired`: known break from ATP competition; no verified permanent retirement. **Maxime Cressy** (2025 ATP announcement, 2026 beach tennis reporting).
- `limited_2026_activity_atp_status_uncertain`: partial competitive activity, but insufficient evidence for ongoing tour singles participation. **Joris De Loore** (do not equate lack of ATP appearance with retirement).

## Reliability of observations

- `metadata_only`: topic/name present in podcast episode description; **episode audio was not transcribed/listened to**.
- `author_opinion` / `author_observation`: journalist's historical analysis, not an objective fact about the player's current psychology/physical state.
- `requires_match_verification`: described match score/turning point needs official event-level cross-check.
- `historical_only`: never silently promote the observation to current player performance.

## Copyright / source policy

Only own short paraphrases, metadata, athlete names and canonical source links are included. No copied full articles, no audio binaries, no bulk transcript downloads. Podcasts may have listen/download links, but that is not blanket rights clearance for archiving/re-distribution. A player's public match history and personal injury rumor are not equivalent sources.

## Use in the current ATP-only platform

Future ingestion should:
1. Verify the stable player ID and reference URL.
2. Log `observed_at`, `published_at`, `ingested_at`, `verification`.
3. Keep author interpretation separate from direct match observation.
4. Re-check status at inference time; this CSV is just a snapshot at **2026-11-21**.
5. Never treat a retrospective article as proof of live early-shift detection.

[Project master](../../PROJECT_MASTER.md).

## November 2026 active scope update

**Important:** The 21 earlier names, five older sources and 11 earlier candidate notes above are **bibliographic research**. They are not the current operating player database.

- [Current male ATP Top 100 snapshot](../rosters/atp_top100_2026_11_16.csv): 100 players independently checked for 2026 main-draw participation.
- [Seven current expert analysts/podcasters](current_analysts_2026_11_21.csv) and [five dated 2026 publications](current_sources.csv).
- [Eight new 2026 technical/tactical observations](current_atp_observations.csv), kept as attributed historic facts/interpretations.
- `atp_intelligence.archive` imports **100 roster profiles, 7 eligible former source mentions and 13 eligible historical notes** (including the eight new 2026 notes). It **excludes** 14 older-player mentions and 6 out-of-scope notes. Ineligible names remain only in review/forensic CSV, not the active database.
- All future content ingestion must check the Top100 roster before creating player records. Ranking snapshots must be refreshed and reviewed weekly.
- [GitHub scope policy](../rosters/README.md) and [Notion live research summary](https://app.notion.com/p/41ff603f0d2e8146a3c6f3bbdfeaf3e4).

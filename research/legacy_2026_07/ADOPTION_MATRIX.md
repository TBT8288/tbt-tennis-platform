# Legacy tennis project audit — 2026-11-21

**Status:** source review completed; ideas selected for migration. **No legacy engine has been activated or merged into the current runtime.**

## Scope and source provenance

User provided:
- `TBT_ATP_Challenger.pdf` — 16 pages, methodology plus a sample daily audit (2026-07-29).
- `TBT_ATP_Challenger_Modszertan_v1.pdf` and its dated copy — byte-for-byte duplicate pair; compared with the file above, only an extra `DB -> AUDIT -> LEARN -> SXP -> CONTROL` module-flow line differs.
- `Tennis_Intelligence_Platform.pdf` and the dated business-plan copy — byte-for-byte duplicate pair (22 pages).
- `TBTProjekt.zip` — prior code and project notes, ~159 MB compressed; contains old Python and Next.js implementations but predominantly dependency folders (`node_modules`, `venv`) that must NOT be imported.
- The ZIP contains a nested copy `Projekt.zip`, partly duplicating those sources.

These materials are **historical design/reference data, not the live ATP model's ground truth**. The original plan included Challenger and a paid SaaS; the current project deliberately does neither.

## Adoption matrix

| Legacy idea/source | Reuse | Conditions |
|---|---|---|
| Quality win / misleading win / quality loss | Yes: Player Intelligence feature design | Separate opponent strength, surface and event context; define/test objective measurements |
| 7–10-day workload, travel, event-entry paths (Q/LL/WC) | Yes: prematch context | Only sourced and dated public facts; don't infer injury or intent |
| Three evidence classes (confirmed/probable/unverified) | Yes: source provenance | Store evidence separately from speculative causal interpretation |
| `NO SOURCE -> NO SCORE`, `NO PREDICTION`, no double-counting | Yes: engineering rules | Avoid false numerical precision; report missing inputs |
| Evidence age/expiry | As a design candidate | Legacy fixed 21/7-day cutoffs and 1.0/0.35 weights are unvalidated; learn by data type |
| Player snapshot architecture (Player/Match/Source/Observation/RatingSnapshot/Prediction) | Yes | Merge with present data schema and timestamp-based validation |
| Prematch + in-play separation | Yes | Use explicit baseline, online updates and independent A/B changes |
| `Projekt/files/prematch.py` weighted factors (30/15/15/10/10/10/5/5) | Research baseline only | These are hand-set hypotheses, NOT established predictive weights |
| `Projekt/files/engine.py` `LOGIT_SCALE=3.0`, `INPLAY_GAIN=2.2` | Not as a live model | Uncalibrated; backtesting and score-aware baselines required |
| `Projekt/files/inplay.py` score-derived “momentum” | Not adopted as psychological shift | Primarily encodes sets/games/points and assumed fatigue; does not measure an independent break-before-break change |
| `hwk-matrix/tbt/inplay.py` ace/DF/break-point “momentum” | Research comparator only | Aggregate outcome counts are not a time-resolved change-point or mental-state measurement |
| Old `False Leader` heuristic | Yes as a testable hypothesis | Must separately measure serve/return quality and evaluate false positives |
| Old Next.js + FastAPI demo | Can reuse concepts/components after audit | Reported incompatible module interfaces; do not merge blindly into Streamlit core |
| Historic 2026-07-29 example audit | Selected historical observations | Re-check each concrete claim against primary sources and preserve event timestamps |
| Subscription, paywall, Stripe, SaaS, broad Challenger coverage | No | Out of scope for private ATP-only lab |

## Historic player data candidates

The older July 29 audit names Andrés Andrade, Alexei Popyrin, Rafael Jódar, Arthur Fils, Kamil Majchrzak, Tommy Paul, Alex Michelsen, Adrian Mannarino, Cruz Hewitt, Bernard Tomic, Francesco Forti, Hugo Dellien, Pedro Martínez, and other players. These names/observations are **leads** — do not silently insert current player ratings, health statuses or form adjustments based on 2026-07 data.

Independently cross-checked example results:
- Andrade def. Popyrin 7–5, 3–6, 6–1, Vancouver Challenger, 2026-07-28: [ATP results](https://www.atptour.com/es/scores/current-challenger/vancouver/7774/results).
- Jódar def. Fils 7–6(5), 6–3, Washington, 2026-07-28: [ATP report](https://www.atptour.com/en/news/fils-jodar-washington-2026-tuesday).
- Majchrzak def. Paul 7–5, 7–6(4), Washington, 2026-07-28: [TennisDB record](https://tennis-db.com/matches/4572472/kamil-majchrzak-vs-tommy-paul).

The PDF's Elo differences, injury/fitness claims, inferred motives, and data-quality labels have **not** been independently validated. Old medical/fitness rumors must never be promoted to a current fact.

## Expert/podcast archive candidates

The older plan names **Damian Kust** and **Jakub Bobro** as historical Challenger observers. Archived co-hosted episodes exist on [Cracked Racquets](https://crackedracquets.com/episodes-category-sorting/) and [Great Shot Podcast](https://crackedracquets.com/series/great-shot-podcast/). For current use:
1. Store episode/article URL, publication date, author, event date and player identity.
2. Paraphrase only verified, attributed observations; a pundit's expectation is not a measured performance fact.
3. Map an old Challenger insight to today's ATP player only when the same player's later history makes it relevant.
4. Respect publishers' copyright and platform terms; don't mirror entire audio/transcripts.

Other names in the older document: Florian Heer/Tennis TourTalk, Mike Cation, Alex Gruskin/Cracked Racquets, José Morgado; independently verify individual sources before adding them.

## Security and technical findings

**Critical:** The ZIP contains plaintext legacy API credentials (for example `hwk-matrix/env.local`) and a legacy client with a hard-coded RapidAPI key fallback. **Values intentionally not copied into this repository or this audit.** Rotate old credentials if still active and ensure client-side code cannot access them. Current repo was still **Public** at review time.

Old handoff notes also report previous hard-coded browser keys, `corsproxy.io` use and broken backend import contracts. Treat all legacy code as **untrusted research material** until re-reviewed, with no execution using real credentials.

Do NOT upload the 159 MB ZIP, old `venv`/`node_modules`, original proprietary documents, embedded tokens, raw licensed data, or historical speculation to this public repo.

## Implementation sequence

1. Define source-backed `Observation`, `EvidenceLevel`, `Source`, `ObservedAt`, `ExpiresAt` schema in current package (with tests).
2. Build a manual, timestamped player-observation import fixture from **verified** July 2026 records; label historic-only.
3. Keep all momentum definitions independent of match score; score enters only downstream prediction and alert significance.
4. Inspect old FastAPI/Next.js UI only after core API contract is stabilized, not as an automatic migration.
5. Validate against fresh ATP point-level and (when available) shot/video data; preserve real-time timestamps and no-lookahead.

## Source pointers (original archives remain user-supplied; not published here)

- `TBT_ATP_Challenger.pdf`: pp. 4–5 source ranking, 8–10 quality of wins/evidence, 15–16 dated audit examples.
- `Tennis_Intelligence_Platform.pdf`: pp. 6–8 Player Profile/Archive/Prediction and pp. 11–12 data architecture and provider evaluation.
- `TBTProjekt.zip`: `Projekt/files/EGYESITETT_MODSZERTAN.md`, `Projekt/files/evidence.py`, `Projekt/files/prematch.py`, `Projekt/files/engine.py`, `Projekt/files/inplay.py`, `hwk-matrix/tbt/`, `HWK_AI_handoff.md`.

**Remember:** the archive does **not** contain a complete structured historical player database or an archived series of point-level predictions. It contains code, methodological design, a dated manual audit, and references to external reporting.

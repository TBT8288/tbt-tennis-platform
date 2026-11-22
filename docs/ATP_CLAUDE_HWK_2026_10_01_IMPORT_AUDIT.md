# ATP Intelligence – Claude HWK AI / TBT történeti projektbeemelés és eltérésnapló

**Átvizsgálva:** 2026-11-22. **Átvett forrás:** [Notion 10 · ATP – HWK AI // TBT projekt-összefoglaló](https://app.notion.com/p/420f603f0d2e819e90e7d0e988039fe5), Claude által összeállított, a felhasználó által kért forrásdokumentum.  
**Az összefoglaló hivatkozott eredeti alapanyagai:** `tenisz-szakmai-tudasbazis.md` és `hwk-ai-megvalositasi-terv.md`, **2026-10-01-i** állapot. Az eredeti két MD fájlt ezen audit során **nem tudtuk önállóan megnyitni**: a Notionban a Claude-féle 10-es összefoglaló volt elérhető. Minden következtetés a Notionban közölt állításokra korlátozódik.

**Elsőbbségi szabály:** a frissebb [PROJECT_MASTER.md](../PROJECT_MASTER.md), a [régebbi projekteket szűrő adoptálási mátrix](../research/legacy_2026_07/ADOPTION_MATRIX.md) és a felhasználó 2026.11.21–22-i döntései megelőzik a 2026.10.01-i korábbi terveket. A „kész volt a Claude környezetében” NEM egyenlő a mai GitHubon futó kóddal.

## 1. Mi új és mit veszünk át?

| ID | Claude összefoglaló adata | Döntés | Beépülés/hely | Valós jelenlegi állapot |
|---|---|---|---|---|
| C01 | **Zéró hallucináció**; ami nem bizonyított, `None` | **ÁTVESSZÜK**, már meglévő elvvel egyezik | [Evidence + Prematch adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | Dokumentált, fejlesztésnél kötelező |
| C02 | **6 játékstílus-kategória** és 12 név szerinti történeti besorolás | **ÁTVESSZÜK mint osztályozási taxonómia**; 12 egyéni besorolás csak ideiglenes forrásigényes jelölt | [Stílusregiszter](../research/player_profiles/CLAUDE_HWK_2026_10_01_STYLE_CANDIDATES.csv); [Taxonómia](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | Nem írja felül a jelenlegi 150 scouting-profilt |
| C03 | `tactical_matchup`, `mental_clutch`, `court_weather`, `surface_strength`, `serve_return`, `load_travel` | **ÁTVESSZÜK mint feature-jelölteket** | [Modellmérnöki adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | 10%/5%/5% régi súlyok **nem igazolt kalibrációk** |
| C04 | Taktikai párosítás: balkezes kontrázó vs. jobbkezes nagy szerváló 1,95× | **CSAK VERIFIKÁLANDÓ KUTATÁSI ÁLLÍTÁS** | [Tényellenőrzési regiszter](../research/CLAUDE_HWK_RESEARCH_CLAIMS_TO_VALIDATE.csv) | Nincs feltöltött eredeti kutatási bizonyíték; tilos éles szorzóként használni |
| C05 | Nyomáshelyzet `score_mental_clutch` breaklabda-konverzió különbség tanh skálával | **ÁTVESSZÜK mint mérhető statisztikai proxy-ötletet**, nem pszichológiai diagnózist | [Modellmérnöki adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | tanh 0,15 és 5%-os súly nincs új adaton validálva |
| C06 | `fatigue_from_load` 16 game felett gyorsuló görbe | **CSAK VALIDÁLANDÓ JELÖLT** | [Modellmérnöki adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | 16 game-es töréspont nem bizonyított biológiai küszöb |
| C07 | `COMEBACK`, `DOMINANCE` stratégiai rezsimek | **RÉSZBEN ÁTVESSZÜK** – értelmezhető, de nem belső mentális momentum | [Modellmérnöki adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | nem azonos a break előtti technikai/viselkedési jelzővel |
| C08 | ITF Court Pace Rating kategóriák, pályasebesség külön feature | **ADATFORRÁSHOZ KÖTÖTT JELÖLT** | [Modellmérnöki adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | A Notion összefoglalójában szereplő határok forrásauditja még nyitott |
| C09 | Game→set→match valószínűség frissítés minden adatlekérési ciklusban | **ÁTVESSZÜK mint implementációs célt**, helyes input/kalibráció mellett | [Prediction/backtest specifikáció](ATP_CLAUDE_PREDICTION_AND_VALIDATION_REQUIREMENTS.md) | régi `tbt/markets.py` nincs a mai repóban; a mai `atp_intelligence/probability.py` csak baseline |
| C10 | Teljes ATP 1–1000 ranking tábla és országkódok hiányai | **REFERENCIA ADATMINŐSÉGI TANULSÁG** | [Modellmérnöki adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | A mai Top150 fókusz megmarad; régi 1–1000 fájlja nincs a GitHubban |
| C11 | Breakpoint conversion != return games won; Sinner 2025 32,63% említve | **A METRIKA-KÜLÖNBSÉGET átvesszük**; a 32,63%-os konkrét szám validálandó | [Tényellenőrzési regiszter](../research/CLAUDE_HWK_RESEARCH_CLAIMS_TO_VALIDATE.csv) | 2024-es érték nem aktuális forma |
| C12 | Brier vs piaci záróodds, kalibráció; „magas találati arány” félrevezető | **ÁTVESSZÜK és formalizáljuk** | [Prediction/backtest](ATP_CLAUDE_PREDICTION_AND_VALIDATION_REQUIREMENTS.md) | 71,7%-os konkrét Stanford példa forrásellenőrzésig csak történeti állítás |
| C13 | Részletes jelzések: meccsgyőztes, O/U 21,5 gém, H1/H2 hendikep, 2:0/2:1/1:2/0:2, O/U 2,5 szett | **ÁTVESSZÜK opcionális kimeneti sémaként**, külön adatigény és validáció | [Prediction/backtest](ATP_CLAUDE_PREDICTION_AND_VALIDATION_REQUIREMENTS.md) | egyik sem állítható elő garantáltan az élő API egyetlen score-jából |
| C14 | 77 sikeres teszt, `tbt/...` és `evidence.py`/`odds.py` | **TÖRTÉNETI STÁTUSZ, NEM ÁTVETT KÓD** | Ez az audit | Az említett fájlok 2026-11-22-én a jelenlegi `main` ágon 404-et adtak. A 77 korábbi tesztet **nem** nyilvánítjuk jelenleg futónak |
| C15 | Kutatási állítások: nem-kényszerített hiba után ~15% plusz hiba, szerva ütésenkénti 0,83/0,51–0,64, labda- és kick-paraméterek, fiziológia, ITIA/walkover | **FORRÁSOLT KUTATÁSI JELÖLTNEK** minősítjük, eredeti bizonyíték nélkül nem operacionalizáljuk | [Tényellenőrzési regiszter](../research/CLAUDE_HWK_RESEARCH_CLAIMS_TO_VALIDATE.csv) | A közölt számok és oksági állítások nem ellenőrzöttek a Notion összefoglaló alapján |
| C16 | Szezonprioritás-index = pontvédelem, torna, korai kiesés | **ÁTVESSZÜK tervezett, megfigyelhető pre-match feature-ként** | [10 tényezős Pre-Match](ATP_PREMATCH_INTELLIGENCE_10_TENYEZO.md), [Modell adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | Motiváció nem olvasható ki közvetlenül a pontokból |
| C17 | Forrásregiszter, 0 szorzó az ellenőrizetlen állításokra, meccsintegritás | **ÁTMENTJÜK az evidenciakezelési elvet** | [Modell adaptáció](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | Egy fórumos gyanú nem bizonyít manipulációt; nem szabad személyiségi címkére alakítani |
| C18 | Open-source backup tanulság: két sandbox-reset után eltűnt régi kód | **ÁTVESSZÜK** – minden kód GitHub commit + működő build + privát verziózott biztonsági másolat | [Backups/tesztkritériumok](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md) | A mostani repo a folytonosság elsődleges helye |
| C19 | Régi márkajavaslat: CourtVector; elvetett HWK AI/ServeSense | **TÖRTÉNETI ÜZLETI ÖTLET, NEM ÚJ NÉV** | Ez az audit | Az aktuális projekt neve **ATP Intelligence / Live Prediction Lab**, indítókódja `ATP` |
| C20 | Régi 0–6 fázis: védjegy, compliance, G0 backtest, G1 privát, G2 béta, G3 fizetős, G4 osztrák EPU | **G0/G1 metodikai elemek átvéve**; monetizációs szakaszok történetiek, **nem mostani ütemterv** | [Prediction/backtest](ATP_CLAUDE_PREDICTION_AND_VALIDATION_REQUIREMENTS.md) | Jelenleg **privát, minimális költségű, nem SaaS** |
| C21 | Az egykori tanulási fókuszban WTA 125/Challenger, később csak ATP 500/1000 | **FELÜLÍRT SCOPE** | [PROJECT_MASTER](../PROJECT_MASTER.md) | Jelenlegi célmeccsek ATP 250/500/Masters/Finals/GS férfi főtábla, Top150 tartós profil, nem Challenger/WTA célmeccsek |
| C22 | Korábbi „minden meccs elemzése” és csak chatben válaszoló próba | **TÖRTÉNETI MUNKAFOLYAMAT** | Ez az audit | Aktuális cél automatizált meccsszűrés és minden lényeges projektkimenet tartós GitHub-mentése |
| C23 | Claude szerint `ATP-CROSSAI-001` verzió 1 beolvasása sikerült | **KORÁBBI CLAUDE ÁLLÍTÁS: RÖGZÍTVE** | [Kereszt-AI memória](ATP_CROSS_AI_SHARED_MEMORY_MCP_ARCHITECTURE.md) | Notion oldal létezik, ChatGPT-ből olvasható. Claude-oldali siker **felhasználói közlés + Claude oldali összefoglaló**, nem itt lefuttatott Claude-integrációs teszt |

## 2. Kódellenőrzés a mai `TBT8288/tbt-tennis-platform` `main` ágon

**Megtalálható:** `atp_intelligence/probability.py`, `tests/test_core.py`, `PROJECT_MASTER.md`, `research/player_profiles/ATP_COACH_SCOUTING_REGISTER_2026_11_22.csv`.

**Nem található a mostani repó megadott útvonalain:** `tbt/prematch.py`, `tbt/inplay.py`, `tbt/markets.py`, `tbt/court_pace.py`, `tbt/player_styles.py`, `tbt/atp_rankings.py`, `tbt/sources.py`, gyökér-`evidence.py`, gyökér-`odds.py`. Ezek **404-es eredményt adtak**. Nem rekonstruáljuk az algoritmusukat egyetlen Claude-összefoglaló alapján bizonyítottként.

## 3. Forrásállítási státuszok

- **MOST ÁTVETT, MÓDSZERTANKÉNT:** taxonómia, unknown/None elkülönítés, tényezőjelöltek, objektív Brier/kalibráció, részletes kimenet, szezonprioritási logika, második biztonsági mentés.
- **ÚJRA VERIFIKÁLANDÓ:** számszerű taktikai/mentális/fáradási súlyok, régi kutatási statisztikák, 12 játékos stíluscímkéjének friss forrásalátámasztása.
- **TÖRTÉNETI / FELÜLÍRT:** CourtVector márkanév, előfizetéses SaaS és osztrák EPU indulás, csak ATP500/1000 célmeccsek, WTA125/Challenger aktuális fókusz, régi kód „kész” státusza.

## 4. Kötelező ellenőrző feltételek az élő modell előtt

1. Minden felhasznált feature-nek `source_id`, `source_timestamp`, `observed_at`, `cutoff`, `confidence` és hiányjelzés.
2. A kutatási állítás nem kerül kalibráció nélkül éles predikcióba; hiányzó információ **nem nulla**.
3. Az ellenfél/minőség, borítás és 2025–2026 idények figyelembevétele.
4. Szettállás/O-U/hendikep csak megfelelő kimeneti eloszlásból; összeadás/komplementerek ellenőrzése.
5. A 2026.10.01-i korábbi tesztszámokból nem következik a mostani 2026.11.22-i kód minősége.
6. A GitHub commit-szintű integráció elvégzése után a korábbi Claude-állítások önálló tesztet kapnak.

**Hivatkozott korábbi forrás:** [Notion 10](https://app.notion.com/p/420f603f0d2e819e90e7d0e988039fe5). Az eredeti két Project markdown és a pekingi tesztállomány (`tbt-teszt-2026-10-01-peking.md`) **nem érhető el ezen a Notion-oldalon teljes tartalomként**, ezért ezekre nem alapozunk konkrét meccsállítást.

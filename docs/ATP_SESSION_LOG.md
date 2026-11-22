# ATP – tartós munkanapló és döntésnapló
**Cél:** új beszélgetésben azonnal látható legyen, mi történt, milyen bizonyítékokkal, és mi a következő munkafolyamat. A forrásfájlok GitHubban és a privát ChatGPT Space-ben külön megvannak.

## 2026-11-21 – projektalap, kód, játékosadatok
- `PROJECT_MASTER.md` létrejött; kódaudit: létező Streamlit/Sportscore RapidAPI/Gemini/Discord prototípus; `atp_intelligence/` külön B0-val, esemény/SQLite alappal és tesztekkel.
- A végleges, felhasználói cél **privát Top150** ATP férfi egyes profil + korai változásérzékelés, nem SaaS.
- Az időbeli relevancia aktuális + előző év, 2024 és régebbi H2H közvetlen súlya nulla; elkészült a `docs/TEMPORAL_RELEVANCE_POLICY.md`.

## 2026-11-22 – 150 játékos dosszié és tartalmi audit
- 150/150 statisztikai/scouting dosszié és forráshivatkozás a GitHub `research/player_profiles/` útvonalán. Meccsarchívum aktuálisan 2026-11-15-ig. **Nincs** 150/150 többmeccsesen validált technikai, biomechanikai vagy mentális profil, és a teljes appintegráció hiányzik.
- Az áthozott `ATP(1).txt` alapján tételes audit: [az eredeti beszélgetés hiányai](ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md), [kilenc visszanyert követelmény](ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md).
- 30 napos intuíciós/előrejelzési tanulási terv, Blind Prediction 50 próbás sablon, virtuális EV-napló, 10 tényezős pre-match, automatikus szűrés, PWA architektúra **dokumentált**. Ezek nem éles, működő modulok.
- A Tennis API korábban egyeztetett felhasználási engedélyét a felhasználó **ellenőrzött és lezárt** döntésként ismét megerősítette; az API tényleges integrációs státusza ettől külön.
- Korábbi új chat hívószó `ATP-MASTER-150` -> **végleg `ATP`** a felhasználó utasítására.
- **Privát teljes szövegarchívum:** új, kizárólag tulajdonosi hozzáférésű ChatGPT Space `ATP – Privát projektarchívum`; az oldal `ATP – Eredeti beszélgetés teljes szövegarchívuma (ATP(1).txt)` az áthozott 1006 sor szöveges változatával, nem nyilvános GitHubon. Eredeti fájl SHA-256 `ffceb2da5985304084e7d4d26ad9982d260106ae31198eede17d503404d24f01`.
- **Bájthű személyes Library-mentés:** a felhasználó korábban feltöltött eredeti `ATP(1).txt` fájlját 2026-11-22-én a saját ChatGPT Library-jába is feltöltöttük, `/ATP/Conversation_Archive/ATP(1)_eredeti_2026-11-22.txt` néven. Ez az eredeti TXT 36 620 bájtos forrás megőrzését szolgálja, szemben a Space-ben megjelenített, szerkesztett blokkszerkezetű szöveggel. A tartós Library-mentés sikeres visszaigazolást adott; a következő beszélgetésben fájlkereséssel elérhető, ha a hozzáférés rendelkezésre áll.
- **Jelenlegi handoff protokoll:** `docs/ATP_START.md`; új beszélgetésben a `ATP` hívószóra beolvasandó a PROJECT_MASTER, session log, a kilenc pótolt téma, a scouting index és szükség szerint a privát archívum. A további lényeges új döntéseket és munkát **GitHubra írjuk, nem kizárólag chatben hagyjuk**.

## Nyitott feladatok
1. A 12 edzői tudásterület 48 konkrét jelének eredeti, pontos listája még nincs meg ebben az áthozott TXT-ben; nem szabad kitalálni és eredetinek címkézni.
2. A kiválasztott Tennis API provider tényleges technikai végpontjai, feed sémája és live adatminősége auditálandó (az engedély **nem** vitás).
3. A 150 játékos részletes többmeccses technikai/mentális mintáinak és a korai, ponttörténetes modellnek a validálása.
4. A funkciók valódi appintegrációja, időbélyegzett előrejelzés/kalibráció, mobilos használhatóság és értesítések.
5. Újabb hosszú beszélgetés végén a lényeges döntések naplózása kötelező; teljes szó szerinti további chatarchívumhoz új export szükséges, ha a platform nem ad közvetlen olvasási hozzáférést.

## 2026-11-22 – projektutasítás a chatmemória-csúszás megelőzésére
- [Egyszeri ChatGPT-projektutasítás](ATP_PROJECT_INSTRUCTIONS.md) elkészült; a felhasználó az ATP Project utasításaihoz helyezheti, hogy új szálban az **ATP** hívószóra a csatlakozók ténylegesen olvassák be a GitHubot, a privát Library-beszélgetést és a Space-t. A projektutasítást az asszisztens nem tudta automatikusan módosítani a ChatGPT projekt UI-jában; ez egyszeri felhasználói beállítás.

## 2026-11-22 – Teljes szöveg automatikus megőrzése: kötelező új feladat

A felhasználó kérésére új, elsődleges adatbiztonsági követelmény: **minden új ATP-beszélgetés teljes szövegének automatizált, időbélyeges, forrásazonosított eltárolása**, nem csupán kivonat vagy kézi emlékeztető. Megvalósítási terv és egyértelmű ChatGPT webUI-korlát: [ATP_FULL_CONVERSATION_ARCHIVE_ARCHITECTURE.md](ATP_FULL_CONVERSATION_ARCHIVE_ARCHITECTURE.md). Kész alap-archívum van a 2026.11.22-ig áthozott szövegekhez; automatikus minden üzenetes archiválás **még nincs bekötve**. A javasolt megoldás a teljes üzenetet rögzítő saját privát chatfrontend + DB + backup; az Open WebUI ellenőrzött alternatíva, de a tényleges átállás nem történt meg.


## 2026-11-22 – Natív több AI-ból használható ATP Memory Hub kötelező feltétel
- Felhasználó: **„egy saját ATP-felület csak akkor jo ha integralni lehet ide vagy claude ai ban cursorba stb”** – az eredeti döntést szó szerint is rögzítve.
- A külön UI-fejlesztés felfüggesztve addig, amíg a közös memória nem működik a natív ChatGPT/Claude/Cursor kliensekben.
- [Platformfüggetlen memória/MCP terv](ATP_CROSS_AI_SHARED_MEMORY_MCP_ARCHITECTURE.md); ChatGPT aktuális Notion/GitHub plugin hozzáférése már működik, Claude/Cursor remote MCP hivatalos támogatása ismert, de a három kliens közös ATP-memória tényleges próba **még nincs meg**.
- **Szigorú korlát:** natív ChatGPT Plus custom MCP támogatást nem tekintünk bizonyítottnak; a Notion/GitHub app csatorna elsődleges. MCP nem interceptál automatikusan teljes beszélgetéseket. Minden platform teljes beszélgetésrögzítése külön megoldandó.


## 2026-11-22 – Első közös AI memória-kapu Notionban: LÉTREHOZVA ÉS CHATGPT-BŐL VISSZAOLVASVA

Létrehoztuk a meglévő Notion ATP Intelligence projektközpontban a **[09 · ATP – közös AI memória-kapu (ChatGPT / Claude / Cursor)](https://app.notion.com/p/420f603f0d2e81a28c89de2837019cde)** oldalt. Az új oldal `ATP-CROSSAI-001` verzió 1 tesztrekordot, az ATP indítókódot, a 2025–2026 időablakot, a lezárt Tennis API felhasználási engedélyt és a GitHub PROJECT_MASTER/ATP_START/SESSION_LOG forráshivatkozásokat tartalmazza. **ChatGPT Notion visszaolvasási ellenőrzés: PASS**, a rekord, évszabály és API-státusz megtalálható. **Claude: NOT TESTED, Cursor: NOT TESTED.** Ezeket a felhasználónak a megfelelő Notion kapcsolatok csatlakoztatása után ugyanazzal az oldal- és rekordteszttel kell kipróbálnia. A Notion oldalt nem tekintjük egyelőre automatikus, minden natív AI-üzenetet mentő archiválónak; arra külön capture-re van szükség.


## 2026-11-22 – ChatGPT irányítás, Cursor GitHub-szűkítés és Claude HWK import

- Felhasználó kimondta: **ez a ChatGPT-ben futó és GitHubon tárolt ATP a fő projekt**. Claude és Cursor **csak előzetes ChatGPT szakmai engedély + felhasználói jóváhagyás** után kódolhat, végezhet adatgyűjtést vagy módosíthat dokumentációt. Az AI-k felhatalmazását nem kezeljük technikai hozzáférési garanciának; a branch-protection és a felhasználói döntés kikényszerítendő.
- [AI-együttműködési és PR-engedélyezési rend](ATP_AI_COLLABORATION_GOVERNANCE.md) elkészült; `AGENTS.md` első részében az AI-k számára azonos szabály található. A Cursor GitHub-csatlakoztatása a Cursor felületén, **Selected repositories** és kizárólag `TBT8288/tbt-tennis-platform` kiválasztásával történjen. **A kapcsolat megtörténtét és branch-védelmet még nem ellenőriztük**; az első engedély csak olvasási teszt.
- Claude által újonnan feltöltött [Notion 10 – HWK AI/TBT történeti projekt](https://app.notion.com/p/420f603f0d2e819e90e7d0e988039fe5) feldolgozva: [23 pontos tartalmi audit](ATP_CLAUDE_HWK_2026_10_01_IMPORT_AUDIT.md), [feature-ötletek](ATP_CLAUDE_MODEL_FEATURE_ADOPTION.md), [kimeneti és backtest-követelmények](ATP_CLAUDE_PREDICTION_AND_VALIDATION_REQUIREMENTS.md), 12 historikus stílusjelölt, 18 forrásellenőrzendő állítás; külön alap `atp_intelligence/legacy_research.py` és `tests/test_claude_adoption.py` Githubra mentve. A történeti 77 teszt és hiányzó `tbt/` kód nem tekinthető átültetett, validált alkalmazásnak.
- [Notion 11 – import eredménye](https://app.notion.com/p/420f603f0d2e81978957e9cd225a8569) külön közös AI-olvasási kapuként létrejött. Az eredeti Claude forrásoldal megmaradt, a GitHub fő forrás.
- **Nyitott:** felhasználói Cursor-GitHub integráció engedélyezése csak kiválasztott repohoz; `main` branch védelme; első olvasási próba; a Claude-adaptáció új GitHub CI futásának ellenőrzése.


## 2026-11-22 – Cursor GitHub-csatlakozás: FELHASZNÁLÓ JELENTETTE, OLVASÁSI PRÓBA KÖVETKEZIK
- Felhasználó megerősítette: **„Cursor összekötve”**. A GitHub-integráció tényleges Cursor-oldali működését **még nem ellenőriztük**, ezért külön nincs `VERIFIED` státusz.
- Elkészült a [ATP-READ-001 kizárólag olvasási ellenőrzőfeladat](tasks/ATP-READ-001_CURSOR_CONNECTION_CHECK.md). **Csak repo/branch/commit és dokumentált jelenlegi modullista**, nincs kódmódosítás, commit, PR, scraping vagy terminálfuttatás.
- A Cursor első jelentését ide, a fő ChatGPT ATP-projektbe kell visszahozni. A GitHub `main` ágon történő írást/merge-et a felhasználói engedély és megfelelő branch-védelem nélkül továbbra sem engedélyezzük. A tényleges main-ág technikai branchvédelmét **nem állítottuk még be**.


## 2026-11-22 – ATP-READ-001 Cursor első olvasási jelentés értékelése

**Státusz: PASS (olvasási feladat), nincs implementációs ATP GO.**

- A felhasználó bemásolta a Cursor `ATP-READ-001` olvasási jelentését. A Cursor saját állítása szerint `origin = https://github.com/TBT8288/tbt-tennis-platform.git`, `main` branch, lokális `e470bb517b978e805d7ff71cdc7f47f34a27cce3` commit; nem futtatott kódot, nem módosított fájlt, és nem nyitott Pull Requestet.
- **Közvetlen GitHub-ellenőrzés ChatGPT-ből:** a jelzett `e470bb5` commit valóban létezik, és a korábbi `ATP-READ-001` átadási naplóbejegyzéshez tartozik. A repository neve, `main` alapértelmezett ága, valamint `atp_intelligence/probability.py`, `events.py`, `storage.py`, `legacy_research.py`, `tests/test_claude_adoption.py` és `app.py` létezése megerősítve.
- A Cursor cél- és hiányosság-összefoglalója megfelel a GitHub fő projektállapotának: privát ATP férfi egyes; 2025–2026 relevanciaablak; Top150 tartós profil; a korai coach-momentumdetektor, appintegráció és validált előrejelzési előny nincs késznek nyilvánítva.
- **Korlát:** a helyi munkakönyvtár változatlansága és a tényleges Cursor-oldali hozzáférés használata csak a felhasználó által átadott Cursor-jelentésből ismert; ezt a GitHub API nem tudja önmagában igazolni. A commit egyezése és a fájlok megléte viszont ellenőrzött.
- **Következő ellenőrzési pont:** mielőtt a Cursor/Claude első érdemi kódolófeladatot kap, a GitHub `main` ágának branch-védelme/PR-korlátja beállítandó és ellenőrizendő. `ATP GO: <task_id>` szakmai feladatkiadás és a projektgazda külön jóváhagyása nélkül nincs Cursor/Claude kódmódosítás, adat-scraping vagy merge.


## 2026-11-22 – Tényleges kódolás és kutatási stop (PR #14)
- Felhasználói irány: **minden beszerezhető fontos adat legyen átadva, ne legyen napi nulláról induló kutatási ciklus; kezdjük a kódolást**. A 150 master, 2 809 H2H pár és a PR #13 forrásjelöltek alapján `research/player_profiles/ATP_DATA_RESEARCH_FREEZE_2026_11_22.md` elmentve (PR #13 kutatási ág).
- `feature/atp-data-api-core-2026-11-22` új feature branch a PR #13 commitjából (tartalmazza az ellenőrizendő adat-overlayeket). Draft [PR #14](https://github.com/TBT8288/tbt-tennis-platform/pull/14), **merge nélkül**.
- Új: API-Tennis POST adapter / offline mockolás, API-kulcs URL-ből kizárása és sanitized hiba, 150-as player overlay olvasó, H2H formátum-normalizálás + historikus leakage tiltás, magyar offline-first `atp_lab.py` UI, SQLite `live_snapshots.py` saját megfigyelési idővel, automatikus tesztek.
- Az első commitcsoport GitHub Actions tesztje **PASS** volt; utóbbi snapshot-commitok CI eredménye külön vizsgálandó. A tényleges élő provider-kulcs/fiók és live latency nem lett tesztelve, nem szabad PASS-nak jelenteni. A pontszintű történeti eseményidő továbbra nem elérhető a dokumentált mintából; ezt nem hamisítjuk meg.
- Az eredeti `app.py`/Sportscore main verzió változatlan. Indítás: `python3 -m streamlit run atp_lab.py`. Forrás/korlát: [ATP_LAB_V1_KODOLASI_ATADAS_2026_11_22.md](ATP_LAB_V1_KODOLASI_ATADAS_2026_11_22.md).
- A következő munka kódoló/tesztelő jellegű: #14 CI, API valós meccsséma és match/player/tournament ID crosswalk, valódi no-lookahead modellvalidáció; nem szükséges általános Top150 kutatási újraindítás.


## 2026-11-22 – API snapshot, historikus B0 és Mac-indító (folytatás)
- PR #14 további fájlok: `atp_intelligence/live_snapshots.py`, `tests/test_live_snapshots.py`; `atp_intelligence/service_baseline.py`, `tests/test_service_baseline.py`; `START_ATP_LAB.command`. A Streamlit UI megjeleníti a két játékos történeti szervastatisztikai B0-ját és kézi élő lekéréskor helyi pillanatképeket ment.
- A CI-t új commitokon ellenőriztük: eddigi friss Python tesztek PASS; a végső PR-head állapot automatikus CI-jét újra kell olvasni. A vizuális/kattintásos Streamlit és az éles API fiók nem tesztelt.
- Ez a beszélgetés **nem teljesült 100%-os összes funkcióként**; a hiányokat konkrét API és validációs tesztblokkolóként tartjuk nyilván, nem tereljük vissza a projektet korlátlan kutatásba.

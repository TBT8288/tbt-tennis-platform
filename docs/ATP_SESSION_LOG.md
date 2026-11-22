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

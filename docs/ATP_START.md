# ATP – állandó új beszélgetés indítókód és projekt-visszaállítás
**Hívószó:** **ATP** (csak ez, nem ATP-MASTER-150).
**Repo:** `TBT8288/tbt-tennis-platform`
**Állapotkezelés:** verziókezelt GitHub projektállapot + privát ChatGPT Space forrásarchívum.
**Utolsó specifikációfrissítés:** 2026-11-22.

## Kötelező menet, amikor a felhasználó csak ennyit ír: ATP
1. **Ne kezdj nulláról.** Keresd meg az ATP projektet, és ténylegesen olvasd be a kapcsolódó tartós forrásokat. A memória csak támpont, nem megbízható teljes transcript.
2. GitHub `TBT8288/tbt-tennis-platform`: olvasd el `PROJECT_MASTER.md`, `docs/ATP_START.md`, `docs/ATP_SESSION_LOG.md`, `docs/ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md`, `docs/ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md`, `docs/TEMPORAL_RELEVANCE_POLICY.md`, `research/player_profiles/ATP_COACH_SCOUTING_INDEX_2026_11_22.md`; szükség szerint a csatolt forrásokat, a jelenlegi `app.py` és `atp_intelligence/` kódot, és az aktív issue-kat.
3. A **teljes eredeti 1006 soros ATP(1).txt** megvan két tartós, privát helyen: **(a) személyes ChatGPT Library** → `/ATP/Conversation_Archive/ATP(1)_eredeti_2026-11-22.txt` (eredeti nyers UTF-8 fájl, bájthű másolat); **(b) ChatGPT Space**, neve `ATP – Privát projektarchívum`, oldala `ATP – Eredeti beszélgetés teljes szövegarchívuma (ATP(1).txt)` (visszakereshető szöveges átírás). A teljes régi üzenetre vonatkozó kérdésnél elsőként a **Library-fájlt** keresd `files.search` eszközzel, ha elérhető, mert ez őrzi a teljes eredeti TXT-fájlt; második forrás a Space. Ne kérd újból a már archivált szöveget.
4. Különítsd el: **döntés / javaslat / forrásból állított tény / ténylegesen működő kód / validálatlan hipotézis**. Előbb olvasd a legfrissebb dátumozott döntést; egy régi SaaS-ötlet nem írhatja felül a mostani privát appot.
5. Készíts **rövid átadási ellenőrzést**: mit olvastál, legutóbbi commit/fájlfrissítés, mi kész, mi hiányzik, mi a mostani feladat; utána **folytasd a munkát**, ne írd újra a specifikációt minden alkalommal.

## A projekthez megőrzött kötelező keret
- Privát, minimális költségű, mobilon használható **férfi ATP egyes Live Prediction Lab**. Nem most készül fizetős SaaS.
- Célmeccsek ATP 250/500/Masters 1000/ATP Finals/Grand Slam férfi egyes főtáblái; tartós játékosprofil **aktuális Top150**, de nem zárjuk ki a más rangú meccsellenfeleket.
- Az aktuális + előző szezon releváns: 2026-ban 2025–2026, 2027-ben 2026–2027; régebbi H2H közvetlen súlya 0.
- A és B játékos **külön** dinamikus állapot, break előtti változásra törekvés. P/T/F, 0–4 ütés, szerva+1/fogadás+1, lábmunka, taktikai és megfigyelhető viselkedési jelek. Pszichológiai/bio-mechanikai címkék csak megfelelő bizonyítékkal.
- Pre-match 10 tényezős séma, automatikus meccselőszűrés, csak jelentős jelzés; nincs előírva minden meccs videós megfigyelése.
- Blind Prediction (intuíció külön), korábbi 30 napos tanulási terv, 50 próbás üres sablon, külön modell/kombinált értékelés és virtuális EV/odds-napló.
- **Tennis API felhasználási engedély:** a felhasználó által korábban ellenőrzött és 2026-11-22-én megerősített, **lezárt** döntés. Ne kérdezd újra. A tényleges API provider/endpoint kliensét és adatminőségét külön kell ellenőrizni, mert a meglévő kódban Sportscore RapidAPI is szerepel.
- Nincs bizonyított kész, teljesen integrált korai momentum-motor vagy validált predikciós előny. A 150 statisztikai dosszié igen; a 150 teljesen validált technikai/mentális dosszié nem. A 12 edzői tudásterület / 48 jel tételes eredeti listája még nem bizonyítottan rekonstruált.

## Hogyan akadályozzuk meg az újabb adatvesztést?
**Nem az emlékezet a kizárólagos forrás.** Minden **jelentős** új felhasználói döntés, kódbeli implementáció, bizonyíték, adatforrás, hibás feltételezés vagy felülírt terv után:
- A megfelelő részletes GitHub fájlban rögzítsd az új állapotot;
- A `PROJECT_MASTER.md`-ben a jelenlegi állapotot és új fő hivatkozásokat;
- A `docs/ATP_SESSION_LOG.md`-ben a végzett munka tényét, forrását és ellenőrzött commit SHA-t;
- Ne állítsd, hogy a beszélgetés **teljes szövege** automatikusan elmentődik, mert erre nincs az eszközök által garantált folyamatos chat-export hozzáférés. A teljes, új chat-szöveg szó szerinti archívumát külön forrás-exportként lehet majd menteni; a lényeges döntések és tényleges munkák viszont már **folyamatos GitHub-mentéssel** megmaradnak.

## Privát archívum és publikációs védelem
A `TBT8288/tbt-tennis-platform` repó a korábbi ellenőrzés szerint nyilvános. **Ne tölts bele teljes személyes beszélgetéseket, privát e-maileket, belépési adatokat, kulcsokat vagy bizalmas nyers csatolmányokat.** Az eredeti szöveges forrás a privát, jelenleg kizárólag tulajdonosi hozzáférésű `ATP – Privát projektarchívum` Space-ben van. Az eredeti fájl 1006 sor, 36 620 UTF-8 bájt és SHA256 `ffceb2da5985304084e7d4d26ad9982d260106ae31198eede17d503404d24f01`; a Space szöveges átírása nem garantált bájtra azonos archívum, de ellenőrizhető teljes szövegforrás. A nyilvános GitHubba csak technikai/tartalmi összefoglalók, döntések, forráshivatkozások kerüljenek.

## Fontos őszinte korlát
Az `ATP` kód **nem programozott rendszerparancs**, és egy új beszélgetésben a GitHub + ChatGPT Space csatlakozók hozzáférhetősége szükséges. Az AI-nak a fenti olvasási folyamatot **ténylegesen el kell végeznie**. Így minimalizálható az újramagyarázás és az adatvesztés, de semmilyen hívószó sem töltheti vissza garantáltan, automatikusan a platform összes régi chatüzenetét.

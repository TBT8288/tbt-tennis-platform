# ATP-MASTER-150 – új ChatGPT-beszélgetés indítókódja

**Indítókód:** `ATP-MASTER-150`  
**Projekt:** ATP Intelligence / Live Prediction Lab  
**Állapot:** verziókezelt átadási útmutató, létrehozva 2026-11-22.  
**GitHub:** https://github.com/TBT8288/tbt-tennis-platform

## Hogyan használd egy új beszélgetésben?

Másold be ezt a teljes üzenetet:

> **ATP-MASTER-150**
>
> Az ATP Intelligence / Live Prediction Lab korábban megkezdett, privát projektjét folytatjuk. Először nyisd meg és ténylegesen olvasd el a GitHub `TBT8288/tbt-tennis-platform` repó következő dokumentumait:
> 1. `PROJECT_MASTER.md` (a központi projektállapot);
> 2. `docs/ATP_MASTER_150_UJ_BESZELGETES_INDITO.md` (ez az átadási szerződés);
> 3. `docs/ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md` (a régi beszélgetésből pótolt kilenc témakör);
> 4. `docs/ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md` (régi szálból kimaradt dolgok és forrásaik);
> 5. `docs/TEMPORAL_RELEVANCE_POLICY.md` (tárgyév + előző év, régi H2H nulla közvetlen súly);
> 6. `research/player_profiles/ATP_COACH_SCOUTING_INDEX_2026_11_22.md` és a hivatkozott legfrissebb játékos-, H2H- és scouting-regiszter;
> 7. a GitHub aktuális kódját és tesztjeit, **ha megvalósítást vagy készültséget kérdezek**.
>
> Ne kezdd elölről a projektet és ne kérd újra azokat a döntéseket, amelyeket a dokumentáció egyértelműen rögzít. A Tennis API felhasználási engedélyének korábban egyeztetett terjedelmét a felhasználó ellenőrzött, lezárt döntésként megerősítette; az alkalmazásba történő valódi API-bekötést külön kell ellenőrizni. A projekt egyelőre privát, nem SaaS.
>
> Készíts egy **rövid, bizonyíték-alapú átadási jelentést**: mi kész, mi hiányzik, mit kell következőként megcsinálni, és mely fájlokat olvastad el. A még nem implementált terveket ne tüntesd fel kész funkcióként. Utána folytassuk a konkrét munkát onnan, ahol tartottunk.

## Kötelező, stabil projektkövetelmények
- **Egy felhasználós, privát ATP férfi egyes** intelligencia és live prediction labor; minimális költség, mobilon használható.
- Cél: technikai/taktikai változás, észlelhető teljesítményesés vagy javulás **lehetőleg még a break előtt**, nem pusztán állásból vagy favoritstátuszból.
- Mindkét játékost **külön** vizsgáljuk. Dinamikus momentum, 0–4 ütés, Serve+1, Return+1, labdamenet, mozgás, megfigyelt viselkedés, játékkontextus.
- **150 játékos** strukturált, visszakereshető statisztikai/scouting profilja; időponttal és forrással. A forrásos meccstudósítás nem automatikusan validált technikai/mentális diagnózis.
- Kizárólag **tárgyév és előző év** aktív közvetlen forma/H2H (2026-ban 2025–2026, 2027-ben 2026–2027). Régebbi H2H közvetlen súlya 0; történeti Elo csak jelölt háttér.
- Meccs előtti **10 tényezős** játékos- és tornarészletező elemzés, automatikus meccselőszűrés, az elégtelen adat külön megjelölése; videó nem kötelező.
- Három mérési réteg: **intuíció (Blind Prediction)**, **rejtett jelek**, **előrejelzés**. Korábbi tanulási terv: 30 nap + legalább 50 előre lezárt intuíciós próba; objektív statisztika és kombináció külön mérendő.
- Előre lezárt, időbélyeges jóslatok; no-lookahead, Brier/log-loss, kalibráció és fals riasztások; virtuális odds/EV elemzés. Valódi pénzes fogadásautomatizálás nem cél.
- **Tennis API engedély:** felhasználó által korábban ellenőrzött és 2026-11-22-én megerősített terjedelem; **NEM újranyitandó**. Jelenlegi prototípus `tennis_api_client.py` kódja Sportscore RapidAPI-t használ, így a kiválasztott provider tényleges bekötése külön fejlesztési kérdés.
- **Régi szálból még nem teljesen rekonstruált:** a 12 edzői tudásterület mind a 48 konkrét jele. Ne találj ki tételes egyezést.
- Régi technológiai javaslat: React/PWA, FastAPI, PostgreSQL/Supabase; a meglévő Streamlit/Python prototípust csak indokolt, tesztelt migráció esetén váltsuk le.
- Az eredeti `ATP(1).txt` beszélgetésfájl **nem** része a repónak. Az abból kiemelt és ellenőrzött követelmények az audit- és pótlási fájlokban vannak.

## Hivatalos indulási fájlok
1. [PROJECT_MASTER.md](../PROJECT_MASTER.md)
2. [A kilenc pótolt követelmény](ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md)
3. [Régi szál átadási auditja](ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md)
4. [Tennis API jog/technikai státusz](ATP_TENNIS_API_ENGEDÉLY_ES_INTEGRACIO.md)
5. [2025–2026 időablak](TEMPORAL_RELEVANCE_POLICY.md)
6. [Top150 scouting index](../research/player_profiles/ATP_COACH_SCOUTING_INDEX_2026_11_22.md)

## Technikai pontosság
Ez az indítókód **nem jelszó és nem varázs-memória**. A GitHub-fájlok ellenőrizhető olvasására emlékeztető kulcsszó. Egy új beszélgetésben a hozzáférés függ attól, hogy a GitHub-kapcsolat és a megnyitási eszközök elérhetők-e; enélkül a felhasználó megadhatja a linket vagy a fájlt. Az indítókód önmagában nem tölti be automatikusan az előző ChatGPT-beszélgetések szóról szóra teljes tartalmát.

# ATP Intelligence – az eredeti beszélgetés 9 hiányzó területének pótlása

**Rögzítés:** 2026-11-22. **Eredeti forrás:** a felhasználó által a jelen beszélgetésben rendelkezésre bocsátott `ATP(1).txt` (külön nem került publikálásra). A 9 téma `PROJECT_MASTER.md` és a Notion korábbi változatában részben vagy egészében hiányzott.

**Státuszmagyarázat**
- `SPEC_COMPLETE`: a régi beszélgetésből megőrzött követelmény most már elérhető és összefüggő, részletes dokumentumban rögzítve; **nem** jelenti, hogy az alkalmazás funkciója élőben működik.
- `BLANK_TEMPLATE`: kitölthető, de személyes eseményeket és kitalált eredményeket **nem** tartalmazó adatsablon.
- `USER_CONFIRMED`: korábban megbeszélt, a felhasználó által ismét megerősített és nem újból megnyitott döntés.
- `IMPLEMENTATION_OPEN`: a programkód/élő adatlekérés/teszt még nincs kész vagy a valós működés nem igazolt.

## Teljes pótlási jegyzék

| # | Áthozott téma | Pótlás | Dokumentáltság | App-megvalósítás |
|---|---|---|---|---|
| 1 | 30 napos intuíció- és predikciós tréning | [30 napos részletes program](ATP_30_NAPOS_TANULASI_PROGRAM.md) | SPEC_COMPLETE | IMPLEMENTATION_OPEN |
| 2 | Blind Prediction a statisztika/odds előtt | [Blind Prediction protokoll](ATP_BLIND_PREDICTION_50_PROTOCOL.md) | SPEC_COMPLETE | IMPLEMENTATION_OPEN |
| 3 | Min. 50 próba; intuíció vs modell vs kombináció | [50 üres naplóbejegyzés](../research/templates/blind_prediction_50_ures_sor.csv) | SPEC_COMPLETE + BLANK_TEMPLATE | IMPLEMENTATION_OPEN; **0 valódi mérést** nem fogunk 50-nek nevezni |
| 4 | Virtuális fogadási napló, piac és várható érték | [EV-szabályok](ATP_VIRTUAL_PREDICTION_AND_EV.md) és [50 soros virtuális tesztsablon](../research/templates/virtual_ev_naplo_50_ures_sor.csv) | SPEC_COMPLETE + BLANK_TEMPLATE | IMPLEMENTATION_OPEN |
| 5 | Tornaprioritás, játékosmotiváció, terhelés | [Pre-match forrás- és módszertani szabályok](ATP_PREMATCH_INTELLIGENCE_10_TENYEZO.md) | SPEC_COMPLETE | IMPLEMENTATION_OPEN |
| 6 | Kötelező 10 pontos prematch A/B játékosokra | [10 tényező pontos listája](ATP_PREMATCH_INTELLIGENCE_10_TENYEZO.md) + [20 üres sor A/B-hez](../research/templates/prematch_10_tenyezo_A_B_ures_sor.csv) | SPEC_COMPLETE + BLANK_TEMPLATE | IMPLEMENTATION_OPEN |
| 7 | Automatikus meccs-előszűrés, nem kell minden meccset nézni | [Live és prematch screening](ATP_AUTO_MATCH_SCREENING_REQUIREMENTS.md) | SPEC_COMPLETE | IMPLEMENTATION_OPEN |
| 8 | Mobilos PWA, React/FastAPI/Postgres opció | [Mobil architektúra és migrációs alternatívák](ATP_MOBILE_PWA_ARCHITECTURE_OPTIONS.md) | SPEC_COMPLETE (javaslatként) | IMPLEMENTATION_OPEN |
| 9 | Tennis API levelezés és felhasználási engedély | [Felhasználó által megerősített, lezárt engedély és külön technikai integráció](ATP_TENNIS_API_ENGEDÉLY_ES_INTEGRACIO.md) | USER_CONFIRMED | A külön API integráció IMPLEMENTATION_OPEN |

## Nem keverjük össze a szerepeket
- A **felhasználó által megerősített Tennis API felhasználási terjedelmet lezártnak fogadjuk el**, nem „engedély-ellenőrzés függőnek” jelöljük.
- A privát, nem fizetős saját appra vonatkozó döntés **elsőbbséget élvez** a régi SaaS-lehetőséggel szemben.
- Az opcionális 30 napos intuíciós tréningből nem válik automatikusan az app használatának kötelező feltétele.
- A régi architektúrajavaslat **nem** törli felülírás nélkül a működő Streamlit/Python repo-t.
- A 2025–2026 relevanciát és a 2024 előtti H2H nullás közvetlen súlyát változatlanul megtartjuk.
- A 12 tudásterület **48 konkrét jelének tételes listája nem került elő a feltöltött `ATP(1).txt` kivonatból**. Ezt nem állítjuk helyre kitalált pontokkal.
- A 150 játékos statisztikai dossziéja és forráslinkje megvan, de nincs 150 többmeccsesen validált teljes edzői / mentális profil.

## Átvitel és későbbi új beszélgetések
Új ATP-szálban **elsőként** a [központi projektállapotot](../PROJECT_MASTER.md), **másodikként ezt a pótlási jegyzéket**, majd a [részletes beszélgetés-összehasonlítást](ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md) olvassuk be. A fájlok megőrzése nem bizonyítja az app megvalósultságát: az implementációt kód, tesztek, valós adatforrás és valós időbélyegezett audit igazolja.


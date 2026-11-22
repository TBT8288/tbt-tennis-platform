# ATP Intelligence – mobilos PWA és technológiai útvonalak
**Forrás:** `ATP(1).txt` 750–844, 856–884. sor. **Státusz: visszanyert korábbi technológiai javaslat, nem jóváhagyott kényszerű stack-migráció.**

## Céltermék
Egyetlen felhasználó saját, privát ATP-meccselemzője. Mobilon (iPhone kezdőképernyő, böngésző) egyszerűen kezelhető, gyors összehasonlítás; az adatgyűjtést és meccsfigyelést az app végzi, nem a felhasználó. Az első verzió **nem** fizetős SaaS.

## Régi, megőrzendő javasolt stack
| Réteg | Régi javaslat | Milyen problémát old? | Jelenlegi státusz |
|---|---|---|---|
| Frontend | React + PWA | Reszponzív, telepíthető mobil-webfelület | Javaslat, nincs bevezetve |
| Backend | Python + FastAPI | API-végpontok, auth, predikciós modul | Javaslat; `atp_intelligence` Python modul külön már van |
| Database | PostgreSQL / Supabase | Tartós játékosprofil, esemény, előrejelzés, index | Javaslat; jelenleg SQLite alapeszköz |
| Engine | Python | Matchup/B0/B1/B2, trendek és kalibráció | Részben matematikai prototípus |
| Alerts | Web push, opcionális Discord | Csak fontos jelzések | Discord kódrész már létezik |
| Feed | Tennis API | Élő meccs/pont és történeti információ | Az engedély lezárt; **provider-kliens implementációja külön feladat** |

## Tényleges aktuális kód – ne vesszük el
`app.py` Streamlit felület, `tennis_api_client.py` Sportscore RapidAPI integráció, `gemini_client.py`, `discord_client.py`, `atp_intelligence/` B0 + tárolási modulok. **A PWA-ajánlás miatt ezeket nem töröljük**, előbb ellenőrizzük a használható logikát, tesztadatot és adatmodelleket.

## Lehetséges migrációs út – csak mérföldkövekkel
**A: Validálható prototípus folytatása.** A Streamlit+Python kód adatminőség- és B0-tesztje; nincsenek indokolatlan költségek.
**B: Mobil UX prototípus.** Ha a Streamlit a telefonon nem megfelelő, külön reszponzív PWA UI, változatlan, tesztelt Python analitika szerveroldalon.
**C: Backend skálázás.** Igazolt többmeccses eseményigény és auth után FastAPI és tartós Postgres/Supabase, **csak ha a költség és licenc elfogadható**.
**D: Push / opcionális Discord.** Elsőként `WATCH`/ `INSUFFICIENT_DATA` helyes, nem megtévesztő üzenetek, majd validált korai jelzés.
**E: Natív iPhone app.** Csak ha a PWA kézzelfoghatóan kevés.

## Szigorú adatbiztonság
- Tennis API-kulcs kizárólag szerveroldalon/titokkezelőn; **soha nem React bundle-ben, repo-ban vagy chatüzenetben**.
- A repo a korábbi ellenőrzés szerint public volt. Nem publikus felhasználói adatok és API tokenek feltöltése tilos.
- Adatkezelési licenc/szolgáltatói hozzáférés és **aktuális technikai bekötés** külön tervezési adatmezők.
- Egyedi használat esetén kezdéskor a kis költségű opció elsődleges, de nem ronthatja a biztonságot és az adatintegritást.

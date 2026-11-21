# ATP Intelligence — Private Tennis Lab

Privát, edzői szemléletű ATP-teniszelemző projekt. A jelenlegi repo egy Streamlit + Sportscore/RapidAPI + Gemini prototípust és egy **külön tesztelhető, korai fejlesztési állapotú** Python alapmodult tartalmaz.

## Hol tartunk?

- **Meglévő felület:** `app.py` — meccskiválasztás, AI-kommentár, opcionális Discord. Használatához megfelelő kulcsok és telepített csomagok kellenek.
- **Új alapcsomag:** `atp_intelligence/` — szabályos teniszgame valószínűség, időbélyegzett pontesemények és predikciók, egyszerű SQLite-mentés.
- **Teszt:** `python -m unittest discover -s tests -v`.
- **Tervezés és állapot:** [PROJECT_MASTER.md](PROJECT_MASTER.md).
- **Kutatási tudástár:** [Notion – ATP Intelligence](https://app.notion.com/p/41ff603f0d2e8121a7c6c2cc89ff4213).

**Nincs még:** bizonyított momentumdetektor, élő pontfeed integráció, validált előrejelzési előny, teljes edzői videóelemzés.

## Fejlesztői gyorsteszt

Python 3.10+ (a GitHub Actions 3.12-t használja):

```bash
python -m unittest discover -s tests -v
```

Nincs szükség API-kulcsra az alaptesztekhez. A meglévő Streamlit felület külön indítható a `requirements.txt` függőségeivel:

```bash
pip install -r requirements.txt
streamlit run app.py
```

A futó app API-kulcsokat vár (pl. `RAPIDAPI_KEY`, `GEMINI_API_KEY`); a kulcsokat környezeti változóban vagy Streamlit Secrets-ben tároljuk, **nem a repositoryban**.

## Fontos megkülönböztetés

A game-valószínűségi függvény a szerver feltételezett független pontnyerési valószínűségéből számol. Ez nem pszichológiai momentum és nem élő predikciós validáció. A pszichológiai állapotra vonatkozó magyarázatok hipotézisek; az adatokból a ténylegesen megfigyelt teljesítmény- és viselkedésváltozás mérhető.

## Biztonság

A repository legutóbbi ellenőrzéskor **nyilvános** volt. Saját privát fejlesztéshez javasolt Private-ra állítani, a jelszavakat/titkos kulcsokat és licencköteles nyers adatokat pedig soha nem feltölteni.

## Forrásolt szakértői archívum (első adatgyűjtés)

Az első Damian Kust/Jakub Bobro archívum-feldolgozás 5 kiadványt, 21 dátumozott játékosstátuszt és 11 saját szavú történeti megfigyelést tárol:

- [Adatállományok, források, státuszdefiníciók](research/expert_archives/README.md)
- [Notion-kutatási oldal](https://app.notion.com/p/41ff603f0d2e81ffb621da1e4ac4675f)

Az első lokális SQLite játékosarchívum egysoros előállítása:

```bash
python -m atp_intelligence.archive --folder research/expert_archives --db data/expert_archive.sqlite3
```

A mentett állomány a `.gitignore` szerint nem kerül automatikusan a GitHubba. A program a forráslinkeket, eredeti megfigyelési dátumot, ellenőrzési státuszt és a 2026-11-21-i aktivitási pillanatképet megtartja. **Nem frissít automatikusan**, és nem állít elő kész prematch vagy élő predikciót.

## ATP Top 150 – jelenlegi játékosadatbázis

A férfi ATP-egyesranglista **első 150 játékosáról** készítünk tartós Player Intelligence profilt a [2026. november 16-i ranglista](research/rosters/atp_top150_2026_11_16.csv) alapján. A Top 100-as lista korábbi, archivált állapot, többé nem szabja meg az adatimport határát.

- [150 játékos – rangsor, név, ország, ATP-pont, források](research/rosters/atp_top150_2026_11_16.csv)
- [150 szezonstatisztikai rekord, ebből 146 ellenőrzött, 4 forráseltérés miatt jelölt hiány](research/rosters/atp_top150_season_stats_2026.csv)
- [ATPTop150 validáló program](atp_intelligence/roster.py)
- [SQLite szakértői és szezonadat-importáló](atp_intelligence/archive.py)
- [Ranglista-adatminőség és kiválasztási szabályok](research/rosters/README.md)

A program az összes Top 150-es játékost megtartja akkor is, ha egy adott szezonban nincs ATP-főtáblás eredménye. Hiányzó adatot nem azonosítunk 0-val. Eltérő ranglista- és statisztikai források esetén a név/pontszám szerinti, forrásolt egyeztetés az előírás.

**Mérkőzés-hatókör:** ATP 250, ATP 500, Masters 1000, ATP Finals, valamint Grand Slam férfi egyes főtábla. Az alkalmi, Top150-en kívüli ellenfél ideiglenes meccskontextusát kezelhetjük, de nem készítünk róla tartós, külön játékosdossziét. Challenger/ITF nem élő célverseny.

**Még fejlesztendő:** heti ranglistafrissítés, stabil ATP player ID, az összes Top150 játékos edzői erősség-/gyengeségprofilja és az élő Streamlit-integráció. A jelenlegi adatbázis első lépésként rangsor- és szezonstatisztikai pillanatkép.

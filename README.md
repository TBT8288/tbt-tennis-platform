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

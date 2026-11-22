# ATP-DEV-001 – B0 offline Streamlit-demó

**Státusz:** bemutató és tesztelhető alapmodell. **Nem** élő ATP-predikció és **nem** bizonyított előny.  
**GitHub feladat:** [#11](https://github.com/TBT8288/tbt-tennis-platform/issues/11) – a bővebb B0-fejlesztés [#2](https://github.com/TBT8288/tbt-tennis-platform/issues/2) ettől még nyitott.

## Indítás

A repository gyökérkönyvtárában, olyan Python-környezetben, ahol a `requirements.txt` szerinti **Streamlit** már elérhető:

```bash
streamlit run b0_demo.py
```

A különálló `b0_demo.py` **nem** módosítja az eredeti `app.py` alkalmazást. Internet, élő mérkőzésadat, RapidAPI/Tennis API, Gemini, OpenAI, Discord, API-kulcs és fogadási odds **nem szükséges** a demó működéséhez. Maga a helyi Streamlit-kiszolgáló és a böngésző normális helyi működése ettől még technikailag hálózati interfészt használhat, de a demó kódja nem végez külső API-kérést.

## Hogyan értelmezzük a bemenetet?

- **Szerváló feltételezett pontnyerési esélye:** 0–100%, kézzel állítod be. Ez minden *hátralévő* pontra azonos, független pontkimenetel esélyének feltételezése, **nem** játékosprofilból vagy élő adatból becsült érték.
- **Szerváló pontjai / Fogadó pontjai:** az aktuális standard, előnyös gémben megszerzett pontok *darabszáma*, nem a kijelzőn látható 15/30/40.
- **Példák:** 0–0 számláló = 0:0, 3–3 = 40:40, 4–3 = szerválóelőny, 3–4 = fogadóelőny; 4–1 és 1–4 már befejezett gém.
- **Kimenet:** a **szerváló aktuális gémgyőzelmének** és a **fogadó brékjének** esélye. Két, egymást kizáró és teljes kimenet: összegük 100%.

## Gyors ellenőrzések

| Feltételezett szervapont-esély | Szerváló pontjai | Fogadó pontjai | Szerváló gémgyőzelem | Fogadó brék |
| --- | --- | --- | --- | --- |
| 50% | 0 | 0 | 50% | 50% |
| 50% | 4 | 3 | 75% | 25% |
| 50% | 3 | 4 | 25% | 75% |
| 20% | 4 | 1 | 100% (már nyert) | 0% |
| 80% | 1 | 4 | 0% | 100% (már brékelt) |

## Egységtesztek

```bash
python -m unittest discover -s tests -v
```

A `tests/test_b0_demo.py` az alaphelyzetet, kétféle előnyt, szélső esélyeket, hibás bemeneteket és a 100%-os kiegészítő esélyeket teszteli. A tesztek a modell számítási részét ellenőrzik; **nem** mérnek előrejelző pontosságot valós meccseken, és nem pótolják az élő feed és a Streamlit UI kézi funkcionális próbáját.

## Korlátok és mi hiányzik még?

- A `atp_intelligence/probability.py` **meglévő** B0 függvényei dolgoznak; nincs új edzői momentumdetektor, sem A/B játékos-profil, live B1/B2.
- Nem támogatott a tie-break, no-ad, büntetőpont vagy match tie-break, és az eredmény csak **egy aktuális, standard gémre** vonatkozik.
- Hiányzik a megbízható pontesemény-feed, az aktuális szerváló történeti azonosítása és a forrásolt, borításfüggő szerva/fogadás baseline.
- Nincs valódi predikciós modellkalibráció, meccs/szett eloszlás, bizonyított predictive edge, automatikus háttérfrissítés vagy Discord-értesítés.
- A következő kutatási/fejlesztési lépéshez adatlefedettségi audit, időbélyeges input, korábbi szezon és jelenlegi szezon megfelelő adatszeparációja, valamint vakteszt szükséges.

## Változtatások

Kizárólag három új fájl: `b0_demo.py`, `tests/test_b0_demo.py`, `docs/B0_OFFLINE_DEMO.md`. A **`main` ág változatlan** marad a PR jóváhagyásáig.

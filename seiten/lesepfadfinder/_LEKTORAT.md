# Endlektorat – Lesepfadfinder-Seite (`seiten/lesepfadfinder/`), 03.10.2026

Nur Deutsch: Der Store-Eintrag hat kein en-US (API: „Listing for language 'en-US' not found“) → keine `/en/`.

**Umfang:** alle sichtbaren Texte (Titel, Meta-Description, OG-Texte und -Alt, Navigation, Held, Probier-Gabelung
samt Buchausschnitt, So geht’s, Was die App kann, Warum so?, Bücherregal, Bildunterschriften und Alt-Texte,
Für wen, Preise, Fragen, Abschluss, Fußzeile), JSON-LD.

## Faktenabgleich (Prüfpunkt 4)

Produktion **live: 1.0.4 (9)** (Store-Seite zeigt 1.0.4, curl 03.10.); Track `production` enthält bereits
1.1.0 (10) „Fährtenzeichen“, die aber noch in der Google-Prüfung liegt. Code-Stand 1.0.4 = eb-player `f089522`.

| Aussage | Beleg |
|---|---|
| Kinder 7–10, Verzweigungen, ein Buch gratis, Einmalkauf ohne Abo | Live-Store-Text de-DE (API + öffentliche Seite) |
| Vier Bücher, Emmi 1 gratis (`iapProductId: null`), Emmi 2 / Kuboria 1 / Kuboria 2 kaufbar | `assets/books/*.ebk` in `f089522` |
| Enden 10 / 10 / 10 / 8; Kuboria je 8 Bilder + Karte; Emmi ohne Abschnittsbilder | `book.json` (`endingCount`, `image`, `map`) |
| Altersangaben „ab 7“ / Kuboria 2 „ab 8“ | `ageRange` 7-10 bzw. 8-12 |
| Je 2,99 € (DE) | `monetization.onetimeproducts` (API, 03.10.): alle drei ACTIVE, DE 2,99 EUR |
| 2 oder 3 Wege je Entscheidung | `choices` je `knoten`: nur 2 und 3 |
| Vorlesen mit Satz-/Wort-Hervorhebung, Wort antippen, Nachfrage „selbst lesen“ | Store-Text; `tts/VorleseController.kt` (Android-`TextToSpeech`) |
| Lesestufen, Andika, Buchstabenabstand, Papier/Sepia/Nacht | Store-Text; `ui/Theme.kt` (Lesethemen) |
| „Nochmal anders entscheiden“ / „Für heute fertig“ gleichrangig | `ReaderScreen.kt` |
| Eltern-Schranke mit ausgeschriebener Zahl, Kauf nur dort, „Käufe wiederherstellen“ | `ElternScreen.kt` |
| Bildschirmzeit-Hinweis im Eltern-Bereich | `ElternScreen.kt` Abschnitt „Bildschirmzeit“, Screenshot 06 |
| Keine Berechtigungen für Kamera usw., keine Datensammlung | Store-Text, Datenschutzseite (200) |
| Probier-Gabelung | wörtlich aus Emmi 1, Abschnitt A006 (Schluss), A006A und A006B (Anfang) |
| Begleitmaterial: Kl. 3–4, Ideen, Impulse, vier Arbeitsblätter, frei kopierbar | `docs/begleitmaterial/emmi-band-1-lehrkraefte.html`; PDF-URL liefert 200 |
| Kuboria 1 gedruckt + E-Book | amazon.de B0GPHX914R (Taschenbuch) und B0GP95NPPX (eBook), Titel per curl geprüft |
| „Warum so?“ | `docs/03_PAEDAGOGIK_PREISSTRATEGIE.md` §9: NRP 2000; Takacs/Swart/Bus 2015; Furenes/Kucirkova/Bus 2021 – bewusst als „kann ablenken“ formuliert, kein Wirkversprechen |

## Geändert beim Lektorat
- „Text, ein ruhiges Bild, die Entscheidung“ → „in manchen Büchern ein ruhiges Bild“ (Emmi-Bände haben keine Abschnittsbilder).
- „eine Frage mit zwei Wegen“ → „zwei oder drei Wegen“.
- Kuboria 1 „mit Bildern“ → „mit 8 Bildern“ (wie Kuboria 2).
- Alt-Texte der Cover nach Ansicht der Bilder konkretisiert.
- Anrede vereinheitlicht: Eltern werden gesiezt; „Probier eine Fährte“ → „Zum Ausprobieren eine Gabelung“,
  „Welchen Weg nimmst du?“ → „Welcher Weg wird es diesmal?“. Der Leitsatz „Du entscheidest, wie die Geschichte
  weitergeht.“ bleibt als Werbespruch der App (Kurzbeschreibung im Store).
- „die schon lesen können und dranbleiben sollen“ → „die schon lesen können“ (kein Druckton).
- Ausgelassener Absatz in Fortsetzung B wieder eingefügt (Buchtext ohne Lücke).

**Typografie** maschinell geprüft: keine geraden Anführungszeichen/Apostrophe, keine Doppel-Leerzeichen,
kein „ - “ statt Gedankenstrich; „…“ und »…« (Buchtext behält die Guillemets des Buchs), geschützte Leerzeichen vor €.

## Bewusst belassen / weggelassen
- **Screenshots aus 1.0.4** (live im Store), nicht die 1.1.0-Bilder: 1.1.0 ist noch in Prüfung. Die Seite trägt
  trotzdem schon das Gesicht „Fährtenzeichen“ (Register); Hinweis „Die Bilder zeigen den aktuellen Stand im Play Store“.
  Nach Freigabe von 1.1.0: in `_bauen.py` `SATZ = "1.1.0"`, bauen, Alt-Texte prüfen (Regal mit Wegpunkten), hochladen.
- Weggelassen: Wegpunkte unter den Covern (erst 1.1.0), USK-Angabe, Download-Zahlen, iOS-Pläne,
  Aussagen zur Offline-Fähigkeit der Vorlesestimme (hängt von der Android-Sprachausgabe ab).
- „Zusatzeffekte senken nachweislich das Textverständnis“ (Store) auf der Seite vorsichtiger formuliert („können ablenken“).
- Kein Sprachwechsel im Kopf (keine EN-Seite).
- Kontakt überall `kontakt@wunderkammer-apps.de`.

# Endlektorat – Wunderkammer (Play-Entwicklerseite)

## 2026-09-26 – Kopfbild „Sammlerbogen“

**Umfang:** alle Texte im Kopfbild `store/developer_header_4096x2304.png` (erzeugt von
`store/make_developer_page.py`), Werbetext der Entwicklerseite (en-US) geprüft, nicht geändert.

| Text | Befund |
|---|---|
| „Wunderkammer“ | ok |
| „Kleine Apps, sorgfältig gemacht.“ | ok |
| „Lesen · Lernen · Spielen · Entspannen“ | ok, Mittelpunkte mit Leerzeichen, deckt die sechs Kategorien-Etiketten ab |
| „offline · ohne Werbung · ohne Tracker“ | inhaltlich geprüft: keine App zeigt Werbung oder bindet Tracker ein; „offline“ = ohne Internet nutzbar (WLAN-Party von Nenne drei läuft nur im lokalen Netz). Gedankenstriche des Entwurfs durch Mittelpunkte ersetzt, wie in der Zeile darüber |
| Kartenetiketten: Wortgenau/Lesen, Malfeld/Lernen, Lesepfadfinder/Lesen, Mancala Ukoo/Spielen, Nenne drei/Spielen, DeepWave/Entspannen | Namen wie im Store; „Nenne drei …“ ohne Auslassungspunkte, weil die Karte nur den Namen trägt |
| Werbetext en-US „Small apps, carefully made: reading, learning, games, relaxation – offline, no ads, no trackers.“ | ok, stimmt mit dem Bild überein |

**Bewusst belassen:** Das Kopfbild ist nur deutsch (Play zeigt ein Bild für alle Sprachen), der
Werbetext ist englisch als Standard. Entwicklersymbol ohne Text.

## 2026-10-03 – Startseite wunderkammer-apps.de (DE + EN)

**Umfang:** `index.html`, `en/index.html` (erzeugt von `store/make_startseite_en.py`), Alt-Texte,
Meta-/OG-Texte, OG-Bilder `assets/bilder/og-de.png`/`og-en.png`.

**Fakten geprüft:** Store-Status per Play-Seite (200 = öffentlich: Nenne drei, DeepWave, Lesepfadfinder,
Mancala Ukoo; 404 = noch im Test: die übrigen sieben). „Ohne Werbung/Konto/Abo“, „gratis ausprobieren“,
„keine Tracker“ und Einzelangaben (2.002 Aufgaben, > 30 Presets, ein Buch gratis, Kalah + Oware gratis,
WLAN-Party) gegen die Texte der lektorierten App-Seiten in `seiten/<sub>/` abgeglichen.
„Ohne Internet“: auf allen App-Seiten so belegt (Käufe brauchen kurz Verbindung – so formuliert).

**Typografie:** deutsche Anführungen nicht nötig; Gedankenstriche –, Mittelpunkte mit Leerzeichen,
„2.002“ mit Tausenderpunkt, Anrede durchgehend „du“ (Mancala-Seite siezt – bewusst belassen, eigene Seite).

**Englisch:** Namen wie im Store (Guild of Six, The Ninth Notch; Nenne drei, Kopfkarte, Wortgenau,
Mühlenarchiv bleiben deutsch). Rein deutsche Apps sind mit „German“ gekennzeichnet (Lesepfadfinder,
Malfeld, Einsatz), ebenso Datenschutz und Impressum. Nenne drei ohne Screenshot, weil es nur deutsche
Telefonbilder gibt.

**Bewusst belassen:** Markenhinweis im Wortlaut von Google („Google Play-Logo“).

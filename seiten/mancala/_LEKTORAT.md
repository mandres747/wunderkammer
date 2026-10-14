# Endlektorat – Mancala Ukoo, `seiten/mancala/` (DE + EN), 03.10.2026

**Umfang:** alle sichtbaren Texte beider Seiten (Titel, Meta-Description, Open-Graph-Texte und -Alt, Navigation,
Held, Probierbrett samt Statusmeldungen und Bildschirmleser-Beschriftungen, So geht’s, Die Familie, Weg und
Tagesstellung, Bildunterschriften und Alt-Texte, Für wen, Preise, FAQ, Abschluss, Fußzeile), JSON-LD.

**Faktenabgleich (Prüfpunkt 4)** gegen Produktion **13 (0.5.0)** (Track `production`, per API gelesen 03.10.;
öffentliche Store-Seite zeigt 0.5.0), Live-Store-Text de-DE/en-US und Code (`master` = 0.5.0 + nur Link-Änderung
`0760118`, nicht veröffentlicht):

| Aussage | Beleg |
|---|---|
| Elf Spiele, Namen und Herkunftsregionen | `Regelwerk.kt` `Varianten.ALLE`, `Herkunft.region` de/en; alle mit Quelle (`istAuslieferbar`) |
| Kalah + Oware gratis, neun im Kauf | `kostenfrei = true` nur bei Kalah/Oware; Store-Text „Elf Spiele der Familie“ |
| Kauf 2,99 € / $3.49, einmalig | Produkt `alle_varianten_freischalten` (monetization-API, DE/US, ACTIVE) |
| Kalah 1955 patentiert, Vereinfachung für westliches Publikum, als Einstieg ausgewiesen | `Herkunft.quelle` (US-Patent 2.720.362, 1955), `ueberlieferungshinweis` Kalah |
| Oware Abapa mit Fütterpflicht | `ueberlieferungshinweis` Oware, Store-Text |
| Siegbedingung: meist Samen zählen, bei Bao/Omweso/Igisoro letzter Zugfähiger | `Siegbedingung.LetzterZugfaehiger` (Bao, Bao la kujifunza, Omweso, Igisoro) |
| Einführung 5 Schritte, Übungsbrett verkürztes Kalah, Einführung je Spiel „was anders ist“ | `Lernen.EINFUEHRUNG` (Store/Strings „5 Schritte“), `einfuehrungFuer` (alle elf), Strings `einfuehrung_variante_zeile` |
| Drei Spielstärken, zu zweit, kein Online-Spiel | Strings `staerke_*`, `hinweis_hotseat`, `hinweis_computer` |
| Ränge und Schwellen 0/1/3/6/12/21, Strauch gratis erreichbar | `Weg.Rang`, Kommentar „kostenlose Varianten … bis STRAUCH“ |
| Tagesstellung Kalah oder Oware, ohne Serien/Erinnerungen | `Tagesstellung.kt` (VARIANTEN = Kalah, Oware), Versionshinweise 13 |
| Regeln mit Quellen für alle elf gratis lesbar | Regelübersicht aus Einstellungen über `Varianten.ALLE`, ohne Kaufprüfung |
| Internet nur für Käufe | Store-Text „Keine Datenerhebung“; Datenschutzseite |
| Kauf kommt auf neuem Gerät von selbst | `Kaufabwicklung.bestehendeKaeufeUebernehmen()` beim Verbindungsaufbau |
| Zehn Sprachen, maschinell übersetzt, App sagt es selbst | `res/values-*`, String `sprache_hinweis` in den Einstellungen |
| Android 8 | `minSdk = 26`; Tablets: Store-Screenshots 7"/10" |
| Probierbrett = Kalah-Regeln der App | `Spiel.kt` (Fang nur bei besetzter Gegenmulde, Ende wenn Ziehender keinen Zug hat, Rest an den Besitzer); Zufallspartie im Test: Samensumme bleibt 48 |

**Geändert beim Lektorat:**
- „Wer am Ende mehr gesammelt hat, gewinnt“ war für Bao, Omweso und Igisoro falsch → „Wie man gewinnt, regelt jedes
  Spiel anders – meist zählt, wer mehr Samen gesammelt hat; bei Bao, Omweso und Igisoro gewinnt, wer als Letzter noch
  ziehen kann.“ (EN entsprechend).
- Alt-Text Screenshot 3: Bildschirmtext („du gewinnst“) als Zitat in Anführungszeichen, damit die Du-Form der App nicht
  mit der Sie-Anrede der Seite kollidiert.
- Probierbrett: fehlendes Leerzeichen zwischen „noch einmal ziehen.“ und „Unten ist am Zug.“; am Partieende entfällt
  „noch einmal ziehen“.
- FAQ „Testversion“/Unterricht nicht aufgenommen – nicht belegt.

**Typografie geprüft:** „…“ und “…”, Apostroph ’, Gedankenstrich –, geschützte Leerzeichen vor €, keine geraden
Anführungszeichen im sichtbaren Text, keine Doppel-Leerzeichen (maschinell geprüft).

**Bewusst belassen:**
- Anrede **Sie** wie im Store-Eintrag (die App selbst duzt). Bildschirmtexte in Alt-Texten werden zitiert.
- Keine Jahreszahl „1940“ aus der Projekt-CLAUDE.md – belegt ist nur das Patent 1955.
- Die Produktbeschreibung in Play („aktuell Ayoayo und Bao la kujifunza, künftige Varianten eingeschlossen“) ist
  veraltet; die Seite übernimmt daraus nichts, auch nicht das Versprechen künftiger Varianten.
- Ein OG-Bild für beide Sprachen: Play hat nur die deutsche Feature-Grafik (en-US ohne eigene). EN-Alt-Text sagt das.
- Seite immer dunkel wie die App (Palette „immer dunkel“); hell/dunkel geprüft, beide gleich.
- Muldenklang (zweite App im Repo) nicht erwähnt; iOS-Port nicht erwähnt (nicht veröffentlicht).

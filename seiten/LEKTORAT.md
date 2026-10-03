# Endlektorat der App-Seiten

Regeln: `Apps/CLAUDE.md`, Abschnitt „Endlektorat der Texte“. Je Seite ein Abschnitt, neuester oben.

## Lesepfadfinder – Unterseiten `presse/` und `selbst-entscheiden/` (+ Fußzeile/Schule auf `index.html`), 03.10.2026

**Umfang:** alle sichtbaren Texte beider neuen Seiten (Titel, Meta-Description, OG-Texte und -Alt, Brotkrumen,
Kurz- und Langtext, Fakten-Kasten, Bildunterschriften, Alt-Texte, Download-Angaben, Nutzungshinweis, Links,
Pressekontakt, Ratgebertext, Quellen, Markenhinweis, Abschluss, Fußzeile), JSON-LD, `LIESMICH.txt` im
Pressebilder-ZIP, Meldungen von `kopieren.js`; auf `index.html` der Absatz „Schule“ und die Fußzeile.
Anrede **Sie** wie auf `index.html` (Eltern/Presse); Fußzeilenlink „Bücher, in denen du entscheidest“
nimmt bewusst den App-Leitsatz auf (Vorgabe des Auftrags).

**Faktenabgleich (Prüfpunkt 4)** – alle App-Fakten aus `index.html` (dort am 03.10. gegen 1.0.4 (9), API und
Store belegt, siehe `lesepfadfinder/_LEKTORAT.md`), dazu:

| Aussage | Beleg |
|---|---|
| Seit September 2026 bei Google Play | Produktion 1.0.0 seit ~24.09.2026 (Memory/Release-Notiz); Store-Seite zeigt 1.0.4 (curl 03.10.) |
| 4 Bücher, 8–10 Enden, 1 gratis, 3 × 2,99 € Einmalkauf | `index.html` Regal/Preise (Stand Oktober 2026) |
| Vorlesen „über die Sprachausgabe des Geräts“ | FAQ „Wer liest vor?“ auf `index.html` |
| Begleitmaterial CC BY-SA 4.0, frei kopierbar und veränderbar | Live-PDF gelesen 03.10. („Sie dürfen es kopieren, verändern und weitergeben“), Quelle `eb-player/docs/begleitmaterial/emmi-band-1-lehrkraefte.html` Z. 86–88 |
| Pressekontakt Michael Andres | Impressum `wunderkammer-apps.de/impressum/` (curl 03.10.) |
| „1000 Gefahren“ = Reihe bei Ravensburger | Bibliotheks-/Händlerkataloge (Ravensburger, Fabian Lenk, „Du entscheidest selbst!“) |
| „Choose Your Own Adventure“, erster Band 1979 | „The Cave of Time“, Edward Packard, Bantam, Juli 1979 |
| Forschung | nur die drei Quellen von `index.html` (NRP 2000; Takacs/Swart/Bus 2015; Furenes/Kucirkova/Bus 2021), gleiche vorsichtige Formulierung („können ablenken“) |
| Bilddateien, Größen | `_bauen.py presse`: Icon/Feature = Store-Dateien, Screenshots = Satz 1.0.4 (`f089522`), Angaben in KB dezimal gerundet |

**Geändert beim Lektorat:**
- `index.html`, Schule: „frei kopierbar“ → „unter der freien Lizenz CC BY-SA 4.0: frei kopierbar und veränderbar“
  (Lizenz seit 03.10., Link auf die deutsche Lizenzfassung); Presse- und Themenseite nennen die Lizenz ebenso.
- Langtext auf 197 Wörter gekürzt (Satz „Spiele, Punkte oder Tagesziele …“ gestrichen), Umfangsangabe „knapp 200 Wörter“.
- „Choose Your Own Adventure, die seit 1979 erscheint“ → „deren erster Band 1979 erschien“ (Reihe lief nicht durchgehend).
- Seitentitel der Themenseite auf 63 Zeichen gekürzt; Brotkrume „Entscheidungsbücher“ statt des langen Titels (Umbruch bei 390 px).
- Fallback-Meldung des Kopierknopfs ohne „Strg+C“ (auf dem Handy gibt es keine Strg-Taste).
- Geschützte Zeichen: „CC BY‑SA 4.0“ mit geschütztem Bindestrich/Leerzeichen, „1080 × 2340 px“, „190 KB“, „1,3 MB“, „2,99 €“.

**Typografie** maschinell geprüft: keine geraden Anführungszeichen/Apostrophe im sichtbaren Text, keine
Doppel-Leerzeichen, kein „ - “, keine „...“; deutsche Anführungszeichen „…“, Gedankenstrich –, Auslassungspunkte …
(„Du stehst vor einer Tür …“). „z. B.“ kommt nicht vor.

**Bewusst belassen / weggelassen:**
- Lena Bertenstein nur als Name der Autorin genannt, ohne Angaben zur Person (Pseudonym).
- Screenshots im Pressebereich aus dem Live-Satz 1.0.4, App-Symbol und Titelgrafik aber schon die neuen
  („Fährtenzeichen“, 1.1.0 in Prüfung) – wie auf `index.html`. Nach Freigabe 1.1.0: `SATZ = "1.1.0"`, `_bauen.py` neu.
- Keine Altersangaben zu „1000 Gefahren“ (nicht geprüft); keine Wertung der Reihen; Markenhinweis unter dem Text.
- Ratgeber-Aussagen „Verstehen wird gebraucht“ und „Überschaubare Etappen“ sind Begründungen, keine Studienbefunde,
  und stehen ohne Quellenzuordnung; Studien nur dort genannt, wo die drei Quellen es tragen.
- „Ohne Konto, ohne Datensammlung“ wörtlich wie Store/`index.html`; Offline-Angabe mit der Einschränkung „Nur ein Kauf braucht kurz eine Verbindung“.

## Nenne drei – `seiten/nennedrei/` (DE + EN), 03.10.2026

**Umfang:** alle sichtbaren Texte beider Seiten (Titel, Meta-Description, Open-Graph-Texte und -Alt,
Navigation, Held, Probierrunde samt Beispielantworten, So geht’s, Spielarten, Bildunterschriften und
Alt-Texte, Für wen, Preise, FAQ, Abschluss, Fußzeile), JSON-LD.

**Faktenabgleich (Prüfpunkt 4)** gegen Produktion **1.6.0 (20)** (Track `production`, per API gelesen
03.10.), Live-Store-Text de-DE/en-US und Code (`feature/gestaltung` = 1.6.0):

| Aussage | Beleg |
|---|---|
| 2.002 Aufgaben, 25 Rubriken, 130 gratis | Store-Text de/en; `Freemium.kt` (5 je Rubrik, Party mehr); Screenshot „130 Aufgaben kostenlos · 1.872 weitere“ |
| Vollversion 3,99 € / $3.89, schließt Unterricht ein | Produkt `alle_rubriken` (API); `Kauf.kt` `loeseThemenboxenAuf` (Vollversion → Unterricht) |
| Unterricht 2,99 €, „alle Aufgaben mit Jahrgang + Paket Oberstufe/Informatik“ | Produkt `unterricht` (API); String `unterricht_kauf_text` |
| Themenpaket 0,49 €, 50 Aufgaben; Themenbox 1,49 € / $1.39, vier Themen, nur angeboten, solange günstiger | API; `Kauf.kt` `THEMENBOXEN`; String `guide_buy_body` |
| Englisch-Paket Kl. 5–10 gratis, nur deutsch | `PRODUKT_GRATIS`, `thema-englisch-de.json` → nur auf der DE-Seite |
| Unterricht nur bei deutscher App-Sprache | `values-en/bools.xml` `unterricht_verfuegbar=false` → EN-Seite sagt das so |
| 1.846 Unterrichtsaufgaben nach NRW-Lehrplänen | Store-Text de (live) |
| Party im WLAN gratis, iPhone im Browser, Hotspot, „Einer kauft, alle spielen“ | Store-Text; `guide_lan_body` |
| Fernseher gratis spielbar (Vollversion nur als Hinweis) | `TvLobby.kt` (kein Kaufzwang, nur Knopf „Vollversion ansehen“) |
| „Kauf wiederherstellen“ / „Restore purchase“ | `settings_fullversion_restore` de/en |
| Schul-WLAN trennt Geräte → Hotspot | `lobby_nobody_hint`, `unterricht_wlan_hint` |
| Probierrunde: Aufgaben und Beispiele | wörtlich aus `content/de`, `content/en` (`answers`, erste vier) |

**Geändert beim Lektorat:**
- „Für Android-Handys, Tablets und Android TV“ → „Für Android-Handys und -Tablets sowie Android TV“.
- „Eins eröffnet den Raum“ → „Ein Handy eröffnet den Raum“ (eindeutig, Bezug klar).
- Titel „Nenne drei …“: geschütztes Leerzeichen vor den Auslassungspunkten, damit sie nicht allein umbrechen.
- EN: Navigation „Modes“ → „Ways to play“ (gleich wie die Überschrift).
- EN: Alt-Text des Lobby-Bilds nannte die deutschen Spielernamen; englische Aufnahme zeigt Emma, Jack, Noah, Mia.
- EN: „available in the German version“ → „available when the app is set to German“ (es gibt nur eine App).
- Fußzeile: „Datenschutz“ aufgeteilt in „Datenschutz der App“ und „Impressum und Datenschutz der Website“
  (der Website-Datenschutz steht im Impressum); EN mit „(German)“ gekennzeichnet.

**Typografie geprüft:** deutsche Anführungszeichen „…“, englische “…”, Apostroph ’ (So geht’s, kids’),
Gedankenstrich –, Auslassungspunkte …, geschützte Leerzeichen vor €, keine Doppel-Leerzeichen,
keine geraden Anführungszeichen im sichtbaren Text (maschinell geprüft).

**Bewusst belassen:**
- Anrede du, in Gruppensituationen ihr („Seid ihr euch nicht einig …“) – wie im Store-Text.
- „2 bis 8 Spieler“ (Ziffern wie im Store und in der App).
- Preise mit „Stand Oktober 2026“ – anders als im Store-Text (dort bewusst ohne Preise), weil die Seite
  „Preise ehrlich“ zeigen soll; bei jeder Preisänderung hier nachziehen.
- Die Probierrunde zeigt „Nenne drei …“ statt „Nenne {n} …“ – alle gezeigten Aufgaben haben in den Inhaltsdateien `n = 3`.
- Weggelassen, weil nicht in Produktion: neue Spielarten 1.7/1.8 (Branch `feature/familie`, intern),
  Hexen-Paket (`feature/hexen-paket`), Online-Themen (`feature/themen-online`).

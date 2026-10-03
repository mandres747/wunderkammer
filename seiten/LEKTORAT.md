# Endlektorat der App-Seiten

Regeln: `Apps/CLAUDE.md`, Abschnitt „Endlektorat der Texte“. Je Seite ein Abschnitt, neuester oben.

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

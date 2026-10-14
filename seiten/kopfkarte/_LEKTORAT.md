# Endlektorat – Kopfkarte (`seiten/kopfkarte/`, DE + EN), 03.10.2026

Regeln: `Apps/CLAUDE.md`, Abschnitt „Endlektorat der Texte“. Datei beginnt mit `_` und wird nicht hochgeladen.

**Umfang:** alle sichtbaren Texte beider Seiten (Titel, Meta-Description, Open-Graph-Texte und -Alt, Navigation,
Held, Wegkarte samt SVG-Beschriftungen, Probierrunde in `data-texte`, So geht’s, Übungen, Bildunterschriften und
Alt-Texte, Hintergrund mit Belegen, Für wen, Preise, FAQ, Abschluss, Fußzeile), JSON-LD, HTML-Kommentare.

**Stand der App:** **nicht in Produktion.** Per API gelesen (03.10.): `production` leer, `alpha` und `internal`
= 3 (0.2.0). Store-Seite `play.google.com/…?id=de.kopfkarte.app` liefert 404. Deshalb `noindex`, kein Badge
(als Kommentar vorbereitet), „Erscheint bald bei Google Play“, kein `installUrl` im JSON-LD.

**Faktenabgleich (Prüfpunkt 4)** gegen Code 0.2.0 (Commit `ddd5b84`, nur gelesen) und Live-Store-Text de-DE/en-US:

| Aussage | Beleg |
|---|---|
| Zur Einführung alles kostenlos, beliebig viele Paläste | `ALLES_FREI = true` in `app/build.gradle.kts` (0.2.0); Store-Text de/en letzter Satz; String `kauf_einfuehrung` |
| Keine Werbung, kein Abo, kein Konto, Daten auf dem Gerät | String `ueber_text`; Store-Text „Fair und privat“ |
| Vier Übungen, 5–50 Begriffe, 10–100 Ziffern, 5–52 Karten | `Stufen.leiter` in `Auswertung.kt` |
| 380 Begriffe, „vom Anker bis zur Zitrone“ / „from anchor to zebra“ | `Wortbank.PAARE` (380 Paare, Anker/Zitrone/Zebra enthalten) |
| Abruf bei Begriffen mit gleich vielen Ablenkern; Karten erst Farbe, dann Wert | `RundenBauer.woerter`; String `abruf_farbe_waehlen` |
| Eigenes Tempo mit Stoppuhr oder getaktet | Strings `tempo_eigen`, `tempo_getaktet`, `tempo_eigen_hilfe` |
| Stufenvorschlag: fehlerfrei +1, unter 60 % −1, Start mit 5 Begriffen | `Stufen.vorschlag`, `Stufen.empfohlen` |
| Neues Handy: Paläste, Listen, Bildliste, Verlauf gehen mit Sicherung/Übertragung mit | `res/xml/datenrettung.xml` (`kopfkarte.json`) |
| Kein Internet nötig | keine Netzwerkzugriffe im Code, nur Play Billing |
| Probierrunde: Begriffe und Beispielpalast | 40 Paare wörtlich aus `Wortbank`, Stationen aus `beispiel_stationen` DE/EN; 5 Begriffe + 5 Ablenker wie `RundenBauer.woerter` |
| Bildbeschreibungen | gegen die Store-Screenshots DE/EN geprüft (Begriffe „Krawatte“/„hippo“, „Soße/Seide/Sahne“ bzw. „seas/suit/sun“) |

**Gedächtnisforschung – nur belegt, keine Wirkversprechen:**
- Herkunft (Simonides, Regel der Orte): Cicero, *De oratore* II, 351–354.
- Gedächtnissportler und räumliche Strategie: Maguire u. a., *Nature Neuroscience* 6 (2003) 90–95,
  doi:10.1038/nn988 – Abstract (PubMed 12483214) gelesen; die Seite gibt nur dessen Aussage wieder.
- Ausdrücklich: „Kopfkarte verspricht dir kein besseres Gedächtnis.“ Die Store-Formulierung „eine der …
  wirksamsten Merktechniken“ wurde **bewusst nicht** übernommen (kein Beleg auf der Seite).

**Geändert beim Lektorat:**
- Simonides-Satz hatte kein Verb („– und daraus die Regel“) und war ungenau → Hergang nach Cicero (Einsturz,
  Plätze der Toten), Regel als eigener Satz. EN entsprechend.
- „Du tippst die Antwort an – zwischen Ablenkern“ galt nicht für Zahlen und Karten → „bei Begriffen zwischen gleich
  vielen Ablenkern“.
- FAQ Stufenvorschlag präzisiert (60 %-Grenze wie im Code). EN „less than … was correct“ → „fewer than 60 percent of
  the locations were right“.
- Abkürzungen geschützt: „u. a.“, „v. Chr.“ mit schmalem geschütztem Leerzeichen, „S. 90“, „pp. 90“ geschützt.
- FAQ-Karten im Nachtband waren hell auf hell (Kontrast 1,2 : 1) → Textfarbe der Karte gesetzt.

**Typografie geprüft:** „…“ bzw. “…”, Apostroph ’, Gedankenstrich –, Auslassungspunkte …, Bis-Strich 00–99,
geschützte Leerzeichen vor € und %, keine Doppel-Leerzeichen. Anrede durchgehend „du“. Britische Schreibung im
Englischen (memorise, practise) wie im Store-Eintrag und in der App.

**Bewusst belassen:**
- Kein Preis für die Vollversion (Produkt `vollversion` steht in der Console auf 2,99 € / 2,89 $), weil er mit
  `ALLES_FREI` in keiner Version gilt und der Store-Eintrag „Zur Einführung ist alles kostenlos“ sagt.
- „Gedächtnissportler“ (generisches Maskulinum wie in App und Store).
- Datenschutz/Impressum auf Deutsch, auf der EN-Seite als „(German)“ gekennzeichnet.

**Vor dem Produktionsstart zu ändern:** `noindex` raus, Badge-Kommentare einschalten, `installUrl` ins JSON-LD,
„Erscheint bald“ und den Satz zum geschlossenen Test ersetzen, Preise neu gegen Code und API prüfen
(vor allem, wenn `ALLES_FREI` auf `false` geht).

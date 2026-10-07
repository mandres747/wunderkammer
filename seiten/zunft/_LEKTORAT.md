# Endlektorat – Zunft der Sechs (`seiten/zunft/`, DE + EN), 03.10.2026

Regeln: `Apps/CLAUDE.md`, Abschnitt „Endlektorat der Texte“. Datei beginnt mit `_` und wird nicht hochgeladen.

**Umfang:** alle sichtbaren Texte beider Seiten (Titel, Meta-Description, Open-Graph-Texte und -Alt, Navigation,
Held, Probierwurf samt `data-texte` und Würfel-Beschriftungen, So geht’s, Werkstatt, Talisman-Unterschriften,
Geschichte, Bildunterschriften und Alt-Texte, Was dich erwartet, Für wen, Preise, FAQ, Abschluss, Fußzeile),
JSON-LD, HTML-Kommentare.

**Stand der App:** **nicht in Produktion.** Per API gelesen (03.10.): `production` leer, `alpha` = 3 (0.2.0),
`internal` leer. Store-Seite liefert 404. Deshalb `noindex`, kein Badge (als Kommentar vorbereitet),
„Erscheint bald bei Google Play“, kein `installUrl` im JSON-LD.

**Faktenabgleich (Prüfpunkt 4)** gegen Tag `v0.2.0` (nur gelesen) und Live-Store-Text de-DE/en-US:

| Aussage | Beleg |
|---|---|
| Zunftbrief 3,99 € (DE) / 3,79 $ (US), einmalig | Produkt `zunftbrief`, Kaufoption `kauf` ACTIVE (monetization-API, 03.10.) |
| Gratis: Anselm, Wendel, Grade bis Werkmeister, Walz des Tages | `Freischaltung` (`FREIE_GRADE = 2`, `FREIE_LEHRMEISTER`), Kommentar ebd.; Store-Text |
| Zunftbrief: Marthe, Almut, Obermeister bis Meister der Sechs, Ende der Geschichte, künftige Lehrmeister und Gesellenstücke | String `zunftbrief_text`; Store-Text |
| Freispiel-Taten: Station 4 / 3 Straßen auf einer Walz / Fünfling | Strings `lm_schmied_frei`, `lm_glas_frei`, `lm_mond_frei`; `Seiten.kt` (erspielt **und** gekauft) |
| Im geschlossenen Test alles frei | `ALLES_FREI = true` in `app/build.gradle.kts` (v0.2.0) |
| 8 Städte, 21 Rezepte/Talismane, 4 Lehrmeister, 6 Grade, 24 Meisterbriefe, Walz des Tages | Store-Text; Strings `stadt_1…8`, `m0…m5`; `NAECHSTE_SCHRITTE.md` |
| Anselm ohne Besonderheiten, die anderen mit Vor- und Nachteil | Strings `lm_*_text` |
| Händler 3 gleiche gegen 1 beliebigen; Veredeln „die meisten bis Stufe 3“ | Strings `tipp_schmiede`, `rezeptbuch_text` (Hände bis Stufe 2) |
| Probierwurf rechnet wie die App | `deutungen`, `rechne`, `stoffeAus` aus `core/engine` (Grundlagen.kt, Rechnung.kt) nach JS übertragen, ohne Talismane/Gravuren, Lehrmeister Werkstatt; 8 Würfe von Hand gegengerechnet (z. B. 33355 → Full House 59 × 4 = 236, Eisen + Messing) |
| Spielt ohne Internet, keine Daten, Spielstand per Android-Sicherung | Store-Text; `res/xml/datenrettung.xml` (Kauf ausgenommen) |
| „Kauf wiederherstellen“ / „Restore purchase“ | String `zunftbrief_wiederherstellen` |
| KI-Hinweis, Klänge CC0 | String `ueber_ki`; Store-Text letzter Satz |
| Ortsnamen EN (Ashford, Highstone, Sixwells) | `values/strings.xml` `stadt_*` |

**Geändert beim Lektorat:**
- „Jeder Lehrmeister bringt einen Vorteil und einen Nachteil“ stimmte nicht für Anselm → „Anselm spielt ohne
  Besonderheiten. Wendel, Marthe und Almut …“.
- Preisliste zeigte Marthe/Almut nur als „Brief“ – sie brauchen zusätzlich eine Tat → Tat je Lehrmeisterin genannt,
  Fußnote „Wendel, Marthe und Almut spielst du außerdem durch eine Tat frei.“
- „Drei Wertungen je Stadt“ → „je Station“ (Begriff der App, gleich wie im Probierwurf-Text).
- „Talismane lassen sich veredeln, bis Stufe 3“ → „die meisten bis Stufe 3“ (Hände nur bis 2).
- „Die Änderungen bleiben für die ganze Walz“ → „gelten für die ganze Walz“.
- Alt-Texte der Talismane nach Ansicht der Bilder korrigiert (Einserglück mit Kleeblatt, Dreiauge mit drei Augen);
  Spieltisch-Alt „vier gehaltene Einsen“ → „vier Einsen, drei davon gehalten“ (Bild geprüft).

**Typografie geprüft:** „…“ bzw. “…”, Apostroph ’, Gedankenstrich –, Malzeichen ×, geschützte Leerzeichen vor €,
Tausenderpunkt (1.006 / 1,006 je Sprache), keine Doppel-Leerzeichen. Anrede „du“. Markenname „Kniffel“/„Yahtzee“
kommt nicht vor (Regel aus `wuerfelwerkstatt/CLAUDE.md`).

**Bewusst belassen:**
- Seite **immer dunkel** wie die App (Entscheidung 26.09.: alle Kupferstiche auf dunklem Grund, `PatinaTag` ungenutzt);
  `prefers-color-scheme: light` zeigt dieselbe Patina-Nacht.
- „Full House“ im Deutschen groß wie in der App (`k_full_house`).
- Preis des Zunftbriefs genannt, obwohl die App noch im Test ist: Produkt ist aktiv, Store-Eintrag beschreibt den Kauf;
  Hinweis „Im geschlossenen Test ist alles frei“ steht direkt dabei.

**Vor dem Produktionsstart zu ändern:** `noindex` raus, Badge-Kommentare einschalten, `installUrl` ins JSON-LD,
„Erscheint bald“-Kästen und Testsätze ersetzen, Preise und Gratis-Grenzen neu gegen Code (`ALLES_FREI = false`) und
API prüfen.

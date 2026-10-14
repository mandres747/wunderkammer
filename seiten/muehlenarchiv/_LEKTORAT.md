# Endlektorat – Mühlenarchiv, `seiten/muehlenarchiv/` (DE + EN), 03.10.2026

**Status der App:** nicht in Produktion (API 03.10.: `production` leer, `alpha` 0.3.0 (4), `internal` 0.2.0 (3);
öffentliche Store-Seite 404). Die Seite trägt deshalb `noindex`, „Erscheint bald bei Google Play“ statt Badge
(Badge-HTML und JSON-LD als Kommentar), und sagt ausdrücklich, dass sie die Testversion beschreibt.

**Umfang:** alle sichtbaren Texte beider Seiten (Titel, Meta-Description, Open-Graph-Texte und -Alt, Navigation,
Held mit Bald-Hinweis, Probefund samt Meldungen und Bildschirmleser-Beschriftungen, So geht’s, Spielarten,
Bildunterschriften und Alt-Texte, Für wen, Preise, FAQ, Abschluss, Fußzeile).

**Faktenabgleich** gegen den eingereichten Store-Eintrag de-DE/en-US (API), Code `master` = 0.3.0 (4) und Kaufprodukt:

| Aussage | Beleg |
|---|---|
| Sieben Spielarten mit Herkunft | `core/engine/.../Varianten.kt` (`Herkunft.region`), Store-Text |
| Springen strittig, per Schalter | Store-Text; `ArchivModell.neuner()` (`neunerSpringen`) |
| Über 130 Funde in sieben Kästen, je genau eine Lösung | Store-Text; Screenshot „0 von 136 Funden“ |
| Gegnerfiguren Hedwig/Anton/Marlene, Unbesiegbarer nur Dreier/Achi | Store-Text; Audit-Commit `12ffde2` |
| Verkehrte Welt, Geheime Linie, Mühlenmaschine, Wirtshausabende (10), Rundreise (7) | Store-Text de/en, Screenshots |
| Gratis-Umfang (Neuner inkl. Spielweisen, zwei Kästen, erster Abend/Besuch …) | `ArchivModell.istFrei/kastenFrei/abendFrei/besuchFrei`; Store „Gratis und fair“ |
| Kauf „Das ganze Archiv“ 2,99 € / $2.79 | Produkt `archiv_freischalten` (monetization-API, ACTIVE) – als **geplant** gekennzeichnet, weil die Testversion `ALLES_FREI = true` hat |
| Klasse: Beamer, Abstimmung im Browser, selbes WLAN, ohne Namen | Store-Text; Datenschutzseite §5 |
| Kauf wiederherstellen | String `kauf_wiederherstellen` |
| Sprachen DE/EN, Android 8 | `res/values`, `values-de`; `minSdk = 26` |
| Probefund | eigene Stellung der Seite (kein App-Fund), Lösung b6 wird aus den 16 Linien berechnet; einzig mögliche Mühle (im Test geprüft) |

**Geändert beim Lektorat:**
- FAQ „Testversion ausprobieren – schreib uns“ gestrichen (kein zugesagtes Angebot) → „Eine Regel stimmt nicht mit
  meiner Quelle überein“.
- Probefund-Titel „Kreide auf dem Schulhof“ → „Eine Mühle fehlt“ (keine Verwechslung mit echten Funden der App wie
  „Kreide an der Tafel“; Kennzeichnung „Probefund“).
- „Für Android-Handys“ → „Für Android ab Version 8“ (keine Tablet-Bilder im Store, nichts Ungeprüftes behaupten).
- Fakten-Leiste: Trennpunkt am Zeilenende statt am Zeilenanfang (390 px).

**Typografie geprüft:** „…“ und “…”, Apostroph ’ (So geht’s, Z.’s, men’s), Gedankenstrich –, geschütztes
Leerzeichen vor €, keine geraden Anführungszeichen, keine Doppel-Leerzeichen (maschinell).

**Bewusst belassen / beim Start nachziehen:**
- Anrede du wie im Store-Text.
- Beim Produktionsstart: `noindex` entfernen, Badge und JSON-LD einschalten, „geplant“/„Testversion“ streichen, Gratis-
  Umfang und Preis gegen den Produktions-Build (`ALLES_FREI = false`) und Play prüfen; Seite in `MUSTER.md` eintragen.
- Klang/Musik und Gegnerbuch (0.3.0) nicht beworben – Nebensache, Store nennt sie nur in den Versionshinweisen.

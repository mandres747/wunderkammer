# Endlektorat – Die neunte Kerbe, `seiten/kerbe/` (DE + EN), 03.10.2026

Für die Übernahme in `seiten/LEKTORAT.md` durch die Hauptsitzung.

**Umfang:** alle sichtbaren Texte beider Seiten (Titel, Meta-Description, Open-Graph-Texte und -Alt,
Navigation, Held, „Erscheint bald“, Probierseite, So geht’s, Was dich erwartet, Bildunterschriften und
Alt-Texte, Für wen, Preise, FAQ, Abschluss, Fußzeile), JSON-LD, Texte im OG-Bild.

**Stand der App:** **nicht in Produktion.** API 03.10.: nur Track `internal`, 1 (0.1.0); Store-Eintrag leer
(kein Text, kein Icon, keine Grafik). Deshalb `noindex`, „Erscheint bald“ statt Badge (als Kommentar),
kein `installUrl`. Texte stützen sich auf den lektorierten Store-Entwurf `docs/STORE.md` (DE/EN) und den Code.

**Faktenabgleich (Prüfpunkt 4)** gegen `master` (b7e34bf = 0.1.0 (1)):

| Aussage | Beleg |
|---|---|
| „Die ganze Geschichte“ 2,99 € / 2,99 $, Kapitel 3–6, alle Enden, „Das nächste Feuer“ | Produkt `ganze_geschichte` ACTIVE (API), Produktbeschreibung DE/EN |
| Kapitel 1–2 gratis, Kauf nur am Ende von Kapitel 2 | `prototyp/engine.js` (`gekauft`, Kaufkarte nach K2) |
| „Harter Winter“ erst nach dem ersten Ende | Einstellung „Nur nach deinem ersten Ende“ (Screenshot en/08), Store-Text |
| Ruhiges Tempo, große Schrift, hell/dunkel, weniger Bewegung | `strings.xml` (`e_grosse_schrift`, `e_bewegung`), `ui.ruhig.name` |
| Keine Mitteilungen, App sendet nichts, nur Billing | `docs/STORE.md` Datensicherheit (Manifest geprüft) |
| Deutsch und Englisch | `localeFilters += listOf("de", "en")` |
| Ab Android 8 | `minSdk = 26` |
| Probier-Texte (Auftakt, Zeilen, Zustände, Hinweis, Knopf) | wörtlich aus `prototyp/texte_k1k2.<de|en>.json`, `_bauen.py` prüft das |
| „Kauf wiederherstellen“ / „Restore purchase“ | `kauf.wiederherstellen`; Screenshot en/05 |

**Spoiler-Regel (nur Kapitel 1–2):** weggelassen gegenüber dem Store-Entwurf: Wald teilen/Hauberg (K3),
Trupps durch den Wald, „kommt eine Kerbe dazu“; Screenshots nur K1–K2, ohne Kaufkarte, ohne Tagebuch-Seite
mit späteren Zeilen und ohne die Einstellungsseite mit „Testbuild: alle Kapitel frei“. Genannt werden nur
Kapitelzahl, drei Enden und die Wiederspiel-Modi (wie `docs/STORE.md` §Spoiler).

**Geändert beim Lektorat:**
- „Geht das Feuer doch einmal aus, geht das Spiel weiter“ → „… ist das Spiel nicht vorbei“ (Wortdopplung);
  EN entsprechend „the game isn’t over“.
- Bildergröße `sizes` an die tatsächliche Galeriebreite angepasst (kein Text, nur nebenbei).

**Typografie geprüft:** DE „…“ und ’, EN “…” und ’, Geviertstrich ohne Leerzeichen im EN, Halbgeviert mit
Leerzeichen im DE, geschützte Leerzeichen vor €, keine geraden Anführungszeichen (maschinell).

**Bewusst belassen / weggelassen:**
- Spielzeit „gut eine Dreiviertelstunde“ für K1–2 nicht übernommen (in `docs/STORE.md` noch zu bestätigen).
- TalkBack-Zeile weggelassen (Audit H5, wie im Store-Entwurf).
- EN-Datenschutz/Impressum als „(German)“ gekennzeichnet.
- Icon und OG-Bild sind Platzhalter (App-Platzhalter-Icon, OG aus App-Schriften gesetzt) – beim Store-Eintrag
  durch Canva-Material ersetzen (`_bauen.py` sagt wo).

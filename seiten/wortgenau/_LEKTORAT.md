# Endlektorat Wortgenau-Seite – `seiten/wortgenau/` (DE + EN), 03.10.2026

**Umfang:** alle sichtbaren Texte beider Seiten (Titel, Meta-Description, Open-Graph-Texte und -Alt,
Navigation, Held, „Erscheint bald“, RSVP-Probe samt Probetext, Zonen- und Knopftexten, So geht’s,
Forschungsleiste, Funktionen, Bildunterschriften und Alt-Texte, Für wen, Preise, FAQ, Abschluss, Fußzeile), JSON-LD.

**Stand:** Wortgenau ist **nicht öffentlich** bei Google Play (Webseite des Eintrags: „Nicht gefunden“, 03.10.).
Per API steht 1.0.3 (18) im Track `production` – eingereicht 01.10. nach Ablehnung von 17, Prüfung läuft.
Deshalb `noindex`, „Erscheint bald bei Google Play“, Badge als Kommentar.

**Faktenabgleich (Prüfpunkt 4)** gegen 1.0.3 (18) (Branch `master` be7aa15) und Store-Text de-DE/en-US (API):

| Aussage | Beleg |
|---|---|
| 5 eigene Dokumente gratis, Klassiker zählen nicht, nie gesperrt | `Freemium.kt` (`FREE_DOCUMENT_LIMIT`, `UNCOUNTED_ORIGINS`, „Nichts wird gelöscht“) |
| EPUB/PDF/DOCX/FB2/HTML/Ordner nur Vollversion | `Freemium.PRO_ORIGINS` |
| Vorlesen, 2–3 Wörter, Fixations-Hervorhebung, Statistik, Stufen ab 3, Lesezeichen, Sicherung = Vollversion | `ProFeature` |
| Barrierefreiheit nie hinter Kaufschranke | `ProFeature`-Kommentar, Store-Text |
| 24 Klassiker (16 DE, 8 EN), Download von Project Gutenberg | `classics.json`, `ClassicsCatalog.download` |
| 350 / 400 WPM, Voreinstellung 250 | `Timing.kt` `SAFE_WPM`, `GIST_WPM`, `DEFAULT_WPM`; String `wpm_zone_gist` |
| Erkennungspunkt und Zeitregel der Probe | `Orp.kt`, `Timing.durationMs` (ohne Rampe/Seltenheit) nach `probier.js` portiert |
| Augenpausen-Hinweis, Lautstärketasten, TalkBack-Aktionen, Ordner-Verknüpfung | Strings/Code auf `master` |
| Vollversion 4,99 € / $4.89 | `onetimeproducts` `pro_freischaltung` (API, DE/US) |
| „Kauf wiederherstellen“ / „Restore purchase“ | String `pro_restore` |
| Android 8, Oberfläche DE/EN | `minSdk = 26`, `values` + `values-de` |

**Geändert beim Lektorat:**
- FAQ neues Handy: Sicherung als Datei ist Vollversion → „Mit der Vollversion nimmst du auch deine Bibliothek … mit“.
- „Für Android-Handys und -Tablets“ → „Für Android ab Version 8“ (Tablets nicht belegt).
- Für wen/Training: Hinweis ergänzt, dass Stufe 3–10 zur Vollversion gehören.
- FAQ Internet: ehrlich „Klassiker beim ersten Öffnen von Project Gutenberg laden“ (Screenshot-Text sagt
  „direkt in der App“ – auf der Seite nicht übernommen).

**Typografie geprüft:** „…“ bzw. “…”, Apostroph ’, Gedankenstrich –, ≈, geschützte Leerzeichen vor €,
keine geraden Anführungszeichen, keine Doppel-Leerzeichen (maschinell).

**Bewusst belassen / weggelassen:**
- Vokabelblitz (1.1.0, Branch `feature/vokabelblitz`, nicht eingereicht) – weggelassen.
- Seite trägt die Gestaltung „Fokuslinie“ (Store-Icon, Feature-Grafik, Lexend). 1.0.3 hat in der App noch die
  alte blaue Oberfläche mit Systemschrift; Lexend und die neue Palette kommen erst mit 1.1.0. Die Seite behauptet
  nichts über die Oberflächenschrift.
- Probetext ist eigener Text (erklärt die App), keine Inhalte aus dem App-Repo.
- Preise „Stand Oktober 2026“ – bei Erscheinen und bei Preisänderung prüfen.

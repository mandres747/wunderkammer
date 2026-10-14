# Endlektorat – Einsatz, `seiten/einsatz/` (nur DE), 03.10.2026

Für die Übernahme in `seiten/LEKTORAT.md` durch die Hauptsitzung.

**Umfang:** alle sichtbaren Texte (Titel, Meta-Description, Open-Graph-Texte und -Alt, Navigation, Held,
„Erscheint bald“-Kasten, Probierrunde samt Meldungen aus `probier.js`, So geht’s, Spielarten, Tischregeln,
Wörter, Bildunterschriften und Alt-Texte, Für wen, Preise, FAQ, Abschluss, Fußzeile), JSON-LD.
Keine englische Seite: Store-Eintrag nur de-DE, App nur Deutsch (Wörterliste sprachgebunden).

**Stand der App:** **nicht in Produktion.** API 03.10.: nur Track `internal`, 1 (0.1.0) completed.
Store-Eintrag de-DE als Entwurf vorhanden. Deshalb `noindex`, „Erscheint bald bei Google Play“ statt
Badge (Badge-HTML als Kommentar), kein `installUrl` im JSON-LD.

**Faktenabgleich (Prüfpunkt 4)** gegen Code `master` (0919838 = 0.1.0 (1)) und Store-Entwurf (per API gelesen):

| Aussage | Beleg |
|---|---|
| Vollversion 2,99 € einmalig (US 2,89 $) | Produkt `vollversion` ACTIVE, `monetization().onetimeproducts()` |
| Gratis: Computer „Leicht“, zu zweit, WLAN beitreten; Kauf: Mittel, Schwer, Statistik, Tisch eröffnen | `KaufRepository.kt` `Freischaltung`; String `kauf_text` |
| Vier, fünf oder sechs eigene + zwei offene Steine; 4/6/10 Chips | `regeln_steine`, `regeln_ziel`, Store-Text |
| Wort aus eigenen + offenen Steinen, „mindestens die angesagte Länge“ | `regeln_steine`, `regeln_zweifel`; `Woerterbuch.kt` (Teilmengen) |
| Gebot und „Zeig her!“ kosten je einen Chip | `kosten_hinweis`, `regeln_chips` |
| WLAN 2–4, NSD + QR, Hotspot, kein Server | `regeln_wlan`, `tisch_eroeffnen_text`, `ueber_text` |
| „Schwer“ merkt sich, wie oft du blufft | Store-Text, `regeln_tipps` |
| Über 65.000 Wortformen, 2–8 Buchstaben, keine Namen/Abkürzungen, ß → SS | CLAUDE.md (65.514), `regeln_woerter` |
| Zwei-Finger-Zoom, Ton/Vibration abschaltbar | NAECHSTE_SCHRITTE 26.09.; Store-Text |
| „Kauf wiederherstellen“ | String `kauf_wiederherstellen` |
| Ab Android 8 | `minSdk = 26` |
| Probierrunden SILBER, GURKE (Bluff bei 6), LACHEND, PUMA (Bluff bei 5), ROBUSTE | `_bauen.py` prüft gegen `assets/woerter.txt` |

**Geändert beim Lektorat:**
- So geht’s: „fünf verdeckte Steine“ → „vier, fünf oder sechs“ (Tischregel).
- „Klappt es, gehört der Topf ihm … geht an den, der gezweifelt hat“ → geschlechtsneutral wie in der App
  („die ansagende Person“, „wer gezweifelt hat“).

**Typografie geprüft** (maschinell + gelesen): „…“, –, ’, geschütztes Leerzeichen vor €, keine geraden
Anführungszeichen, keine Doppel-Leerzeichen.

**Bewusst belassen / weggelassen:**
- „Zur Einführung ist alles kostenlos freigeschaltet“ (Store-Entwurf, `ALLES_FREI = true` im Build) nicht
  übernommen: Ob das beim Start in Produktion gilt, ist offen. Beim Erscheinen prüfen und ggf. ergänzen.
- Preis mit „Stand Oktober 2026, vor dem Erscheinen“.
- Anrede du.

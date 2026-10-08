# Endlektorat – Malfeld-Seite (`seiten/malfeld/`), 03.10.2026

Nur Deutsch: Der Store-Eintrag hat kein en-US → keine `/en/`.

**Status: noch nicht in Produktion.** Track `production` = 0.8.1 (15), Erstrelease, liegt in der Google-Prüfung;
die öffentliche Store-Seite liefert 404 (curl 03.10.). Deshalb: `<meta name="robots" content="noindex">`,
„Erscheint bald bei Google Play“ statt Badge (Badge-HTML als Kommentar an beiden Stellen), FAQ „Wann gibt es …“.
Code-Stand = malfeld `main` 35f919f (versionCode 15, versionName 0.8.1).

**Umfang:** alle sichtbaren Texte (Titel, Meta-Description, OG-Texte und -Alt, Navigation, Held, Probier-Feld
samt Rückmeldungen in `probier.js`, So geht’s, Was drin ist, Lehrplan-Kasten, Bildunterschriften und Alt-Texte,
Für wen, Preise, Fragen, Abschluss, Fußzeile), JSON-LD.

## Faktenabgleich (Prüfpunkt 4)

| Aussage | Beleg |
|---|---|
| Punktefeld, Zerlegen, Tausch-, Umkehr-, Quadrataufgaben, „Ein Bild, vier Aufgaben“, Vorlesen-Taste | Store-Text de-DE (API); Screenshots 0.8.1 |
| Themen und Klassenangaben (ZR 20 Kl. 1, ZR 100 Kl. 2, Stellenwert 2–6, Schriftlich 3–4, Teiler/Brüche/Negativ 5–6) | `EinstufungScreen.kt` `ModulKarte(…)` |
| Stellenwert- und Bruch-Inhalte, Prozentstreifen als Ausblick Kl. 7 | Store-Text; Versionshinweise 15; `docs/business/12_AUSBAU_STELLENWERT_BRUCH.md` |
| Gratis: Einstufung, Reihen ·1 ·2 ·4 ·5 ·10 + Quadrate, je Thema 3 Karten und 3 Übungen | `billing/Freischaltung.kt` (`FREIE_REIHEN`, `FREIE_KARTEN_JE_MODUL`); `PlusScreen.kt` Umfangszeile |
| Plus monatlich 3,99 € mit 7 Tagen Test | API: `plus_monatlich`/`monatlich` DE 3,99 EUR, Angebot `testphase-7-tage` ACTIVE (P7D frei) |
| Plus jährlich 24,99 €, 7 Tage Test, 1. Jahr 19,99 € | API: `plus_jaehrlich` DE 24,99 EUR; Angebot `start-19-99` ACTIVE: P7D frei, dann P1Y −20 %; Regel „thisSubscription“ = nur Neuabschluss; `BillingManager.bestesAngebot` wählt das Testangebot |
| Einmalkauf „Malfeld komplett“ 39,99 € | API: `einmalkauf_komplett` ACTIVE, DE 39,99 EUR |
| Plus/Einmalkauf für alle Kinder des Geräts, Erwachsenen-Sperre, „Käufe wiederherstellen“ | Store-Text; `ParentalGateway.kt`; `PlusScreen.kt` |
| Familiensprache EN/TR/AR/UK/RU | `didaktik/Zahlwort.kt` `enum class Sprache` |
| Ruhiger Modus „ersetzt keine Förderung“ | `ElternbereichScreen.kt` (wörtlich), Store „keine Therapie“ |
| Umzugskoffer, mehrere Kinder, „Ich kann“-Sätze, Einmaleins-Karte, „Fertig für heute“ | Store-Text; `ElternbereichScreen.kt` |
| Klassenmodus mit Pilot-Code | Store-Text; `KlassenmodusAnsicht.kt` |
| Lehrplan-Zitate | `malfeld-app/docs/business/10_ROADMAP_UND_RECHERCHE.md` §3.1 (wörtlich aus Lehrplan Mathematik Primarstufe NRW 2021; KMK 2022); Sek I: §3.2 und `12_AUSBAU…` §5 |
| Probier-Feld | Mechanik „Teile geschickt“ der App (Screenshot 02); Kernaufgaben ·1 ·2 ·5 ·10 wie `FREIE_REIHEN`/Store-Text |

## Geändert beim Lektorat
- „Mit ‚Merken‘ werden die Aufgaben danach sicher“ → „‚Merken‘ übt die abgeleiteten Aufgaben danach ein“ (kein Erfolgsversprechen).
- „nur beim ersten Abschluss“ → „beim ersten Abschluss des jeweiligen Abos“ (Play-Regel `thisSubscription`).
- Probier-Titel „teile geschickt!“ → „geschickt teilen“ (Seite siezt Erwachsene durchgehend; Nutzerentscheidung 26.09.).
- Formeln mit geschützten Leerzeichen (`4 · 6` brach am Handy zwischen 4 und ·).
- Fakten im Held nicht mehr als umrandete Kästen (wirkten wie Knöpfe), sondern mit Leuchtstift-Unterstrich.
- Dunkles Design: Leuchtstift-Strich unter statt durch die hellen Titelbuchstaben (Lesbarkeit).

**Typografie** maschinell geprüft: keine geraden Anführungszeichen, keine Doppel-Leerzeichen, Gedankenstrich –,
Malpunkt ·, geschützte Leerzeichen vor € und in Formeln.

## Bewusst belassen / weggelassen
- Preise stehen auf der Seite (im Store-Text bewusst nicht) – mit „Stand Oktober 2026“ und Verbindlichkeitssatz.
- Keine Wirkversprechen („vergisst es nicht wieder“ aus dem Store nicht übernommen), Rechenschwäche nur mit „keine Therapie“.
- Lehrwerksnamen nicht genannt (wie im Store, Prüfbericht Eltern 24.09.).
- Plättchenfarben Rot/Blau aus der Canva-Feature-Grafik, nicht die Salbeigrün-Punkte der App-Oberfläche.
- Kein Sprachwechsel (keine EN-Seite). Kontakt überall `kontakt@wunderkammer-apps.de`.

## Wenn die App live ist
1. `curl` auf die Store-Seite (200), Version prüfen.
2. In `index.html`: robots-Zeile + Kommentar oben entfernen, beide „Erscheint bald“-Blöcke durch die auskommentierten
   Badges ersetzen (`.badge` in `stil.css` ergänzen: `display:inline-block; width:230px`), FAQ „Wann gibt es …“ streichen,
   Satz unter den Bildern („zur Veröffentlichung eingereicht“) und Schluss-Vorspann anpassen.
3. `seiten/hochladen.sh malfeld --sauber`.

# Endlektorat DeepWave-Seite – `seiten/deepwave/` (DE + EN), 03.10.2026

**Umfang:** alle sichtbaren Texte beider Seiten (Titel, Meta-Description, Open-Graph-Texte und -Alt,
Navigation, Held, Schwebungs-Probe samt Statustexten und ARIA-Beschriftungen, So geht’s, „Ehrlich gesagt“,
Funktionen, Bildunterschriften und Alt-Texte, Für wen, Preise, FAQ, Abschluss, Fußzeile), JSON-LD.

**Faktenabgleich (Prüfpunkt 4)** gegen Produktion **1.5.0 (12)** (Track `production` per API 03.10.,
Play-Webseite „Aktualisiert am 26.09.2026“), Live-Store-Text de-DE/en-US (API) und Code Tag `v1.5.0`:

| Aussage | Beleg |
|---|---|
| Über 30 Presets, 9 Kategorien | `Preset.kt`: 35 freie Presets in 9 freien Kategorien |
| Atemführung mit vier Mustern Box, 4-7-8, beruhigend, energetisch | `BreathingGuide.kt` `BreathingPattern` |
| Solfeggio 396–963 Hz | `Preset.kt` `carrierOverride` 396…963 |
| Rosa/braunes Rauschen als Hintergrund einer Phase (gratis) | `BackgroundNoise { NONE, PINK, BROWN }` in `Phase` |
| 3 eigene Presets gratis, Premium unbegrenzt | `Access.FREE_CUSTOM_PRESETS = 3` |
| Mixer 8 Klänge, in Echtzeit erzeugt | `AmbientSound.kt` (8 Einträge), `AmbientEngine.kt` „no audio assets“ |
| Premium 3,99 € / $3.79, Klangwecker und Rhythmus-Spur je 1,99 € / $1.89, Komplettpaket 5,99 € / $5.49 | `monetization.onetimeproducts` (API, DE/US) |
| Komplettpaket nur, solange kein Teil besessen wird | `Access.offerBundle = … owned.none { … }` |
| Frühere Käufer behalten Premium | `Access.FREEMIUM_VERSION_CODE`, Store-Text |
| „Kauf wiederherstellen“ / „Restore purchase“ | Strings `wake_restore`, `rhythm_restore` |
| Android 8 | `minSdk = 26` |
| Sprachen DE/EN | `locales_config.xml` |
| Offline, Internet nur für Käufe | Datenschutzerklärung 1.5 (live), Manifest |
| GPL-3.0, Quellcode auf GitHub | Store-Text; https://github.com/mandres747/DeepWave (200) |

**Geändert beim Lektorat:**
- FAQ Internet: „die Klänge des Mixers stecken in der App“ war falsch (sie werden synthetisiert) → „entstehen in Echtzeit auf deinem Gerät“.
- Datenschutz-Links: DE-Seite → `deepwave/datenschutz.html` (deutsche Fassung), EN-Seite → `deepwave/` (englische Fassung, daher ohne „(German)“).
- Wirkung: keine Aussage „besserer Schlaf“/„tiefere Konzentration“ (so steht es noch im Live-Store-Text) und nicht
  „Dein Gehirn folgt dem Rhythmus“ (Onboarding-Text) – stattdessen Anlässe (Einschlafen, Arbeiten, Entspannen)
  und der Abschnitt „Ehrlich gesagt“: Wirkung wissenschaftlich nicht geklärt, kein Medizinprodukt.

**Typografie geprüft** (maschinell + Durchsicht): „…“ bzw. “…”, Apostroph ’, Gedankenstrich –, geschützte
Leerzeichen vor €, keine geraden Anführungszeichen im sichtbaren Text, keine Doppel-Leerzeichen.

**Bewusst belassen / weggelassen:**
- Anglizismen wie in der App: Preset, Session, Sleep-Timer, Ambient-Mixer (ein Ding, ein Wort – wie Store und App).
- Nicht beworben: einzelne Preset-Namen mit fragwürdigen Versprechen (Luzides Träumen, OBE Monroe-Methode),
  „Brain-Entrainment“, F-Droid (Aufnahme noch offen), Tablets (keine Tablet-Screenshots, nicht geprüft).
- Probe auf der Seite: 200 Hz links, 200 Hz + 2–12 Hz rechts, Lautstärke 0,12, Ein-/Ausblenden, Stopp nach 60 s;
  Text sagt nur, was man hört, keine Wirkung.
- Preise „Stand Oktober 2026“ – bei Preisänderung nachziehen.

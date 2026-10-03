# App-Seiten auf eigenen Unterdomains – Muster

Stand 03.10.2026, Pilot: **Nenne drei** → https://nennedrei.wunderkammer-apps.de/ (`seiten/nennedrei/`).

Nutzerentscheidung 03.10.: Jede App bekommt eine Werbe- und Erklärseite auf eigener Unterdomain
(`<sub>.wunderkammer-apps.de`) **im Gestaltungsstil der App**. Dorthin zeigt das Feld „Website“ im
Play-Store-Eintrag. Die Hauptdomain bleibt der Sammlerbogen (Übersicht aller Apps); Datenschutz bleibt
unter `wunderkammer-apps.de/<app>/`, Impressum unter `wunderkammer-apps.de/impressum/`. Nicht verschieben.

## Ablage

```
seiten/
  MUSTER.md          diese Datei
  LEKTORAT.md        Endlektorat aller Seiten (je Seite ein Abschnitt)
  hochladen.sh       seiten/hochladen.sh <sub> [--sauber]
  werkzeug/helfer.py WOFF2-Teilmengen, WebP, Icons (keine Gestaltung)
  <sub>/
    index.html       Deutsch (Hauptsprache)
    en/index.html    Englisch, wenn der Store-Eintrag en-US hat
    stil.css         eigene CSS je App – hier lebt das Gesicht der App
    probier.js       optional, eigenes kleines Skript (kein Fremdcode)
    schrift/         WOFF2 + OFL-Texte der App-Schriften
    bilder/          WebP-Screenshots, Icons, og-<sprache>.png, Google-Play-Badges
    _bauen.py        erzeugt schrift/ und bilder/ aus dem App-Repo (wird nicht hochgeladen)
    _quelle/         Rohdateien, z. B. Badges von Google (wird nicht hochgeladen)
```

Alles, was mit `_` beginnt, bleibt lokal. `seiten/_pruefung/` (Playwright-Bilder) ist gitignoriert.

**Wichtig für den Upload der Hauptdomain:** `seiten/` gehört **nicht** nach `/opt/wunderkammer/sites/www`.
Der Website-Upload schließt deshalb `seiten`, `store`, `docs` und `README.md` aus:

```
cd D:/OneDrive/Apps/wunderkammer
tar --exclude=./seiten --exclude=./store --exclude=./docs --exclude=./README.md --exclude=./.git -czf - . \
  | ssh wunderkammer 'tar -xzf - -C /opt/wunderkammer/sites/www'
```

## Gemeinsames Grundgerüst (klein halten)

Gemeinsam sind nur Abschnittsfolge, Meta-Tags und Fußzeile. Farben, Schriften, Formen, Held-Bild und
Ton kommen aus der Gestaltungslinie der App (`Apps/CLAUDE.md`, Register; `_gestaltung/LEITFADEN.md`).
Nie `stil.css` einer anderen App kopieren und umfärben – sonst gleichen sich die Seiten.

### Abschnitte (in dieser Reihenfolge, Überschriften frei)

1. **Kopf** – Wortmarke mit App-Icon, Sprungmarken, Sprachwechsel (immer sichtbar).
2. **Held** – App-Name als einzige `h1`, ein Satz Versprechen, 3–4 kurze Fakten (gratis, offline …),
   offizielles Google-Play-Badge, eine Zeile „für welche Geräte“. Rechts/unten ein Bild **aus dem Leitmotiv**
   (Nenne drei: Kartenstapel mit Probierrunde echter Aufgaben).
3. **So geht’s** – drei Schritte.
4. **Spielarten/Funktionen** – nur, was in der **Produktionsversion** steckt.
5. **Screenshots** – aus dem Store-Material, WebP, `loading="lazy"`, Bildunterschrift + Alt-Text.
6. **Für wen** – 2–4 Zielgruppen (Familie, Party, Unterricht …).
7. **Preise ehrlich** – was gratis ist, was einmalig kostet, mit Preis und „Stand <Monat Jahr>“ und dem
   Satz „Verbindlich ist der Preis, den Google Play beim Kauf anzeigt“.
8. **Fragen (FAQ)** – `<details>`; Internet, iPhone, Daten, Käufe auf neuem Gerät, Sprachen, Kontakt.
9. **Abschluss** – kurzer Aufruf + Badge.
10. **Fußzeile** – „Weitere Apps“ → https://wunderkammer-apps.de/, Datenschutz der App
    (`https://wunderkammer-apps.de/<app>/`), Impressum und Datenschutz der Website
    (`https://wunderkammer-apps.de/impressum/`), Kontakt-Mail, Satz „keine Cookies, nichts von fremden
    Servern, keine Besuchszählung“, Markenhinweis Google Play.

### Pflicht im `<head>`

- `lang`, `charset`, `viewport`, `<title>` (Name – Gattung für Android), `meta description` (≤ 160 Zeichen)
- `canonical`, `hreflang` de/en/x-default (x-default = deutsche Seite)
- `theme-color` hell/dunkel, Favicon 32 px, Icon 192 px, Apple-Touch 180 px
- Open Graph: `og:type/site_name/locale/title/description/url/image(+width/height/alt)`,
  `twitter:card = summary_large_image`; Bild **1200 × 630** je Sprache (`bilder/og-de.png`, `og-en.png`),
  aus der Canva-Feature-Grafik gesetzt, nicht neu gezeichnet
- JSON-LD `MobileApplication` mit `operatingSystem`, `applicationCategory`, `installUrl`, `offers` (Preis 0).
  **Keine** `aggregateRating`-Angaben erfinden.
- Preload nur für die Titelschrift.

### Regeln

- **Keine Fremdabrufe:** keine Google Fonts, kein CDN, kein Tracking, keine Cookies, keine externen Skripte,
  keine eingebetteten Videos. Schriften als WOFF2-Teilmenge (OFL-Text mitliefern).
- **Google-Play-Badge:** offizielles PNG von Google (`…/badges/static/images/badges/<de|en>_badge_web_generic.png`)
  lokal in `_quelle/`, unverändert verwenden (nicht umfärben, keine Kontur, kein Schatten, Schutzraum ist im
  PNG enthalten), mindestens ~200 px breit, Link direkt auf den Store-Eintrag. Alt-Text: „Jetzt bei
  Google Play“ / „Get it on Google Play“. Markenhinweis in der Fußzeile.
- **Nur Wahres:** jede Zahl, jeder Preis, jede Funktion gegen Code der Produktionsversion **und** Live-Store-Text
  prüfen (`_tools/play_publish.py`-API nur lesend; Preise über `monetization().onetimeproducts()`).
  Funktionen von unveröffentlichten Branches weglassen.
- **Responsiv** 390–1440 px ohne horizontale Seiten-Scrollleiste (Bildstreifen dürfen in sich scrollen,
  dann `tabindex="0"`). Schmale Breiten: Riesentitel mit `clamp()` und `white-space: nowrap` prüfen.
- **Barrierefreiheit:** genau eine `h1`, Sprunglink, sichtbarer Fokus, Kontraste WCAG AA nachgerechnet
  (Fließtext ≥ 4,5 : 1, große Titel ≥ 3 : 1), Farbe nie allein, Touch-Ziele ≥ 48 px,
  `prefers-reduced-motion` (Animationen aus), `prefers-color-scheme` mit eigener dunkler Palette der App,
  Alt-Texte beschreiben, was zu sehen ist (Namen im Bild stimmen je Sprache!).
- **Bildgrößen:** Telefon-Screenshots 360 und 720 px breit (srcset), TV/Tablet 800 und 1600 px, WebP q≈82.
  Gesamtseite möglichst < 2 MB; Bilder unterhalb des Helds `loading="lazy"` + `width/height`.
- **Englisch** unter `/en/`, wenn der Store en-US hat. Store-Bilder nur verwenden, wenn sie die Sprache zeigen
  (Nenne drei: Telefon-Screenshots gibt es nur deutsch → EN-Seite zeigt nur die englischen TV-Bilder).
  Datenschutz/Impressum sind deutsch → Link mit „(German)“ kennzeichnen.

## Ablauf je App (Checkliste)

1. Gestaltungslinie der App lesen (Register in `Apps/CLAUDE.md`, `docs/…GESTALTUNG…`).
2. Fakten sammeln: Live-Store-Text (de-DE, en-US), Track-Stand (welche Version ist in Produktion?),
   Produktpreise DE/US, Code der Produktionsversion für Gratis-Grenzen und Sonderfälle.
3. Unterdomain-Kürzel festlegen (`<sub>`: nur a–z, 0–9, `-`), Ordner `seiten/<sub>/` anlegen.
4. `_bauen.py` nach Vorbild Nenne drei: Schriften, Screenshots, Icons, OG-Bild, Badges.
5. `index.html`, `en/index.html`, `stil.css` schreiben – eigenes Gesicht, gemeinsames Gerüst.
6. Playwright: 390 und 1440 px, hell und dunkel, DE und EN; prüfen: `scrollWidth == innerWidth`, eine `h1`,
   keine Anfragen außer der eigenen Domain, Schriften geladen, keine Konsolenfehler. Bilder ansehen.
7. **Endlektorat** DE/EN nach `Apps/CLAUDE.md`, Abschnitt in `seiten/LEKTORAT.md`.
8. Hochladen: `seiten/hochladen.sh <sub>`; Caddy-Eintrag für die Unterdomain macht die Server-Sitzung
   (`_server/`), danach `curl -sI https://<sub>.wunderkammer-apps.de/` prüfen.
9. Play Console: Feld „Website“ auf `https://<sub>.wunderkammer-apps.de/` (mit Nutzerfreigabe; Store-Änderung
   geht in die Prüfung – nicht mitten in eine laufende Versionsprüfung).
10. Sammlerbogen (Hauptdomain) verlinkt die App-Seite: Karte in `index.html` (Vitrine bei Store-Start, sonst Werkstatt),
    Icon/Screenshot in `store/make_startseite.py`, dann `store/make_startseite_en.py`; Play-Kopfbild in `store/make_developer_page.py`.
11. Commit im wunderkammer-Repo nur mit Pfaden (`seiten/…`).

## Belegte Unterdomains

| Sub | App | Stand |
|---|---|---|
| `nennedrei` | Nenne drei (de.nennedrei.app) | 03.10.2026 gebaut und hochgeladen; Caddy durch Server-Sitzung |

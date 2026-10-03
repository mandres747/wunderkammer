"""Stellt Impressum und Datenschutzerklärungen auf den Sammlerbogen-Stil um.

Der Inhalt jeder Seite bleibt unverändert. Ersetzt werden nur das eingebettete <style>,
dazu kommen Kopf (Wortmarke, Navigation), das angesteckte Blatt um den Text und eine Fußzeile.
Gestaltung: assets/start.css + assets/text.css. Bereits umgestellte Seiten (body.textseite)
werden übersprungen. Aufruf:  python store/make_rechtsseiten.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Ordner -> Farbe der App (oberer Blattrand), wie auf der Startseite
FARBE = {
    "impressum": "var(--nadel)", "blindgitter": "#4A5866", "deepwave": "#8A2E8A",
    "einsatz": "#A9784A", "kopfkarte": "#1F3A68", "lesepfadfinder": "#328538",
    "malfeld": "#C9CF2E", "mancala-ukoo": "#6E4B2E", "muehlenarchiv": "#713A87",
    "nenne-drei": "#FF3D7F", "neuntekerbe": "#326228", "wortgenau": "#6B3FD1",
    "zunft-der-sechs": "#37D3C0",
}

KOPF_LINKS = """<link rel="icon" href="/assets/bilder/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/bilder/apple-touch-icon.png">
<meta name="theme-color" content="#D6DDE2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141A20" media="(prefers-color-scheme: dark)">
<link rel="preload" href="/assets/schrift/ebgaramond.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/start.css">
<link rel="stylesheet" href="/assets/text.css">"""

TEXT = {
    "de": dict(sprung="Zum Text springen", start="/", heim="Wunderkammer – Startseite", nav="Seitenbereiche",
               apps="Alle Apps", impressum="Impressum",
               fuss="Diese Seite setzt keine Cookies, lädt nichts von fremden Servern und zählt keine Besuche."),
    "en": dict(sprung="Skip to text", start="/en/", heim="Wunderkammer – home", nav="Sections",
               apps="All apps", impressum="Legal notice (German)",
               fuss="This site sets no cookies, loads nothing from third-party servers and does not count visits."),
}


def umstellen(pfad: Path) -> str:
    s = pfad.read_text(encoding="utf-8")
    if 'class="textseite"' in s:
        return "schon umgestellt"
    sprache = "en" if re.search(r'<html lang="en"', s) else "de"
    t = TEXT[sprache]
    ordner = pfad.relative_to(ROOT).parts[0]

    s, n = re.subn(r"\s*<style>.*?</style>", "\n" + KOPF_LINKS, s, count=1, flags=re.S)
    assert n == 1, "kein <style>"

    kopf = f"""<a class="sprung" href="#inhalt">{t['sprung']}</a>
<header class="kopf">
  <div class="breite">
    <a class="marke" href="{t['start']}" aria-label="{t['heim']}"><img src="/assets/bilder/icon-192.png" alt="" width="40" height="40">Wunderkammer</a>
    <nav aria-label="{t['nav']}">
      <a href="{t['start']}#sammlung">{t['apps']}</a>
      <a href="/impressum/">{t['impressum']}</a>
    </nav>
  </div>
</header>
"""
    fuss = f"""
<footer class="fuss-text">
  <p><a href="{t['start']}">Wunderkammer</a> · <a href="/impressum/">{t['impressum']}</a> · <a href="mailto:kontakt@wunderkammer-apps.de">kontakt@wunderkammer-apps.de</a></p>
  <p>{t['fuss']}</p>
</footer>
"""
    stil = f' style="--app: {FARBE[ordner]}"'
    m = re.search(r"<body([^>]*)>", s)
    koerper_start, koerper_ende = m.end(), s.rindex("</body>")
    inhalt = s[koerper_start:koerper_ende]
    if "<main" in inhalt:
        inhalt = re.sub(r"<main([^>]*)>", lambda mm: f'<main class="blatt" id="inhalt"{stil}{mm.group(1)}>', inhalt, count=1)
    else:
        inhalt = f'\n<main class="blatt" id="inhalt"{stil}>{inhalt}</main>\n'
    s = s[:m.start()] + '<body class="textseite">\n' + kopf + inhalt + fuss + s[koerper_ende:]
    pfad.write_text(s, encoding="utf-8")
    return f"umgestellt ({sprache})"


if __name__ == "__main__":
    for ordner in FARBE:
        for pfad in sorted((ROOT / ordner).rglob("*.html")):
            print(pfad.relative_to(ROOT), "->", umstellen(pfad))

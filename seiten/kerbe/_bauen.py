"""Baut Schriften und Bilder der Seite „Die neunte Kerbe“ und prüft die Probier-Texte.

Quelle ist nur lesend das App-Repo (Spiele/glut, master = 0.1.0 (1), nur interner Test).
Es gibt noch keinen Store-Eintrag: keine Feature-Grafik, kein Canva-Icon (ab 22.10.).
Deshalb: Icon = Platzhalter der App (ic_launcher_foreground.xml, als SVG in _quelle/kerbstock.svg
nachgezeichnet, gleiche Pfade), OG-Bild aus Schriften + Icon der App gesetzt (Playwright),
Screenshots aus docs/screens (nur Kapitel 1–2, keine Testbuild-Hinweise).
Beim Store-Eintrag: Icon und OG-Bild durch das Canva-Material ersetzen.
Aufruf: python seiten/kerbe/_bauen.py
"""
import json
import re
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import webp, woff2  # noqa: E402

APP = Path(r"D:/OneDrive/Apps/Spiele/glut")
FONTS = APP / "app/src/main/res/font"
SCREENS = APP / "docs/screens"
S = HIER / "schrift"
B = HIER / "bilder"
Q = HIER / "_quelle"

# Schriften: dieselben festen Schnitte wie in der App (OFL)
for name in ["vollkorn_regular", "vollkorn_italic", "vollkorn_semibold", "karla_regular", "karla_semibold", "karla_bold"]:
    woff2(FONTS / f"{name}.ttf", S / f"{name.replace('_', '-')}.woff2")
for lic in ["OFL_Vollkorn.txt", "OFL_Karla.txt"]:
    (S / lic).write_bytes((APP / "app/src/main/assets/licenses" / lic).read_bytes())

# Screenshots: nur Kapitel 1–2, ohne Kaufkarte und ohne „Testbuild“-Zeile (Spoiler-Regel docs/STORE.md)
AUSWAHL = {
    "de": ["01_auftakt_hell", "02_lichtung_start_hell", "04_k2_hell", "09_k2_dunkel", "07_kerbstock_hell", "16_rueckkehr_hell"],
    "en": ["01_erste_sitzung_auftakt", "02_erste_sitzung_lichtung", "03_k2_lichtung", "04_k2_einteilung"],
}
for sprache, namen in AUSWAHL.items():
    ordner = SCREENS if sprache == "de" else SCREENS / "en"
    for n in namen:
        for w in (360, 720):
            print(sprache, n, w, webp(ordner / f"{n}.png", B / f"{sprache}-{n}-{w}.webp", w))

# Icons und OG-Bild per Chromium setzen (keine Fremdabrufe: nur lokale Dateien)
from playwright.sync_api import sync_playwright  # noqa: E402

svg = (Q / "kerbstock.svg").read_text(encoding="utf-8")
OG = """<!doctype html><meta charset="utf-8"><style>
@font-face{font-family:V;src:url('%(s)s/vollkorn-semibold.woff2')}
@font-face{font-family:K;src:url('%(s)s/karla-regular.woff2')}
html,body{margin:0;width:1200px;height:630px;background:#F0F0EB;overflow:hidden}
.t{position:absolute;left:84px;top:150px;width:640px;color:#1A2518}
h1{font:600 92px/1.02 V;margin:0 0 28px}
p{font:400 34px/1.35 K;margin:0;color:#3D4A3A}
.l{position:absolute;left:84px;right:84px;top:520px;height:0;border-top:2px solid #1A2518}
.k{position:absolute;left:84px;top:520px;display:flex;gap:26px}
.k i{display:block;width:3px;height:26px;background:#1A2518}
.k i.n{background:#326228;width:5px;height:34px}
svg{position:absolute;right:40px;top:60px;width:420px;height:420px}
</style><div class="t"><h1>%(titel)s</h1><p>%(satz)s</p></div>
<div class="l"></div><div class="k"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i class="n"></i></div>%(svg)s"""
TEXTE = {
    "de": ("Die neunte Kerbe", "Trag eine alte Glut in den Wald und finde heraus, was die Kerben zählen."),
    "en": ("The Ninth Notch", "Carry an ancient ember into the forest and find out what the notches count."),
}
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": 512, "height": 512})
    pg.set_content(f"<style>html,body{{margin:0}}svg{{display:block;width:512px;height:512px}}</style>{svg}")
    pg.screenshot(path=str(Q / "icon-512.png"))
    for sprache, (titel, satz) in TEXTE.items():
        seite = Q / f"og-{sprache}.html"
        seite.write_text(OG % {"s": S.as_uri(), "titel": titel, "satz": satz, "svg": svg}, encoding="utf-8")
        pg = br.new_page(viewport={"width": 1200, "height": 630})
        pg.goto(seite.as_uri(), wait_until="networkidle")
        pg.screenshot(path=str(B / f"og-{sprache}.png"))
    br.close()

from helfer import png  # noqa: E402
png(Q / "icon-512.png", B / "icon-192.png", 192)
png(Q / "icon-512.png", B / "apple-touch-icon.png", 180)
png(Q / "icon-512.png", B / "favicon-32.png", 32)

# Google-Play-Badges: nur kopieren, nie verändern (für später; die Seite sagt „erscheint bald“)
for sprache in ("de", "en"):
    (B / f"google-play-badge-{sprache}.png").write_bytes((Q / f"google-play-badge-{sprache}.png").read_bytes())

# Probier-Texte müssen wörtlich aus der App stammen (eine Quelle je Sprache, prototyp/texte_k1k2.<sp>.json)
for sprache, datei in (("de", HIER / "index.html"), ("en", HIER / "en/index.html")):
    texte = json.loads((APP / f"prototyp/texte_k1k2.{sprache}.json").read_text(encoding="utf-8"))
    werte = set(texte.values())
    seite = datei.read_text(encoding="utf-8")
    for t in re.findall(r'data-text="([^"]+)"', seite):
        t = t.replace("&quot;", '"').replace("&amp;", "&")
        assert t in werte, (sprache, t)
    print(sprache, "Probier-Texte wörtlich aus der App:", len(re.findall(r'data-text="', seite)))
print("fertig")

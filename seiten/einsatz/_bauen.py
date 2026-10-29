"""Baut Schriften und Bilder der Einsatz-Seite aus dem Store-Material und prueft die Probierrunden.

Quelle ist nur lesend das App-Repo (Spiele/einsatz, master = 0.1.0 (1), nur interner Test).
Aufruf: python seiten/einsatz/_bauen.py   (Ausgabe nach seiten/einsatz/{schrift,bilder})
"""
import html
import json
import re
import sys
from itertools import combinations
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

APP = Path(r"D:/Apps/Spiele/einsatz")
STORE = APP / "store"
FONTS = APP / "app/src/main/res/font"
LIZENZ = STORE / "grafik/fonts"
BADGES = HIER / "_quelle"  # offizielles Google-Play-Badge, unveraendert
S = HIER / "schrift"
B = HIER / "bilder"

# Schriften: dieselben Schnitte wie in der App (Special Elite: Apache 2.0, Courier Prime: OFL)
woff2(FONTS / "special_elite.ttf", S / "special-elite.woff2")
woff2(FONTS / "courier_prime.ttf", S / "courier-prime-regular.woff2")
woff2(FONTS / "courier_prime_bold.ttf", S / "courier-prime-bold.woff2")
(S / "LICENSE-SpecialElite.txt").write_bytes((LIZENZ / "LICENSE-SpecialElite.txt").read_bytes())
(S / "OFL-CourierPrime.txt").write_bytes((LIZENZ / "OFL-CourierPrime.txt").read_bytes())

# Telefon-Screenshots (nur de-DE)
for f in sorted((STORE / "screenshots").glob("*.png")):
    for w in (360, 720):
        print(f.name, w, webp(f, B / f"{f.stem}-{w}.webp", w))

# Icons
png(STORE / "grafik/icon_store_512.png", B / "icon-192.png", 192)
png(STORE / "grafik/icon_store_512.png", B / "apple-touch-icon.png", 180)
png(STORE / "grafik/icon_store_512.png", B / "favicon-32.png", 32)

# Open-Graph-Bild 1200x630 aus der Feature-Grafik (Canva-Motiv)
fg = Image.open(STORE / "grafik/feature_1024x500.png").convert("RGB")
grund = fg.getpixel((4, 4))
hoehe = 600
fg = fg.resize((round(fg.width * hoehe / fg.height), hoehe), Image.LANCZOS)
og = Image.new("RGB", (1200, 630), grund)
og.paste(fg, ((1200 - fg.width) // 2, (630 - hoehe) // 2))
og.save(B / "og-de.png", optimize=True)

# Google-Play-Badge: nur kopieren, nie veraendern (fuer spaeter, solange die Seite "erscheint bald" sagt)
(B / "google-play-badge-de.png").write_bytes((BADGES / "google-play-badge-de.png").read_bytes())

# Probierrunden in index.html gegen die Woerterliste der App pruefen (wie Woerterbuch.kt:
# beliebige Teilmenge aus verdeckten + offenen Steinen, gesperrte Woerter "!" zaehlen als gueltig).
woerter = {}
for z in (APP / "app/src/main/assets/woerter.txt").read_text(encoding="utf-8").split():
    w = z.rstrip("*!")
    woerter.setdefault("".join(sorted(w)), []).append(w)


def laengste(steine: str) -> int:
    for n in range(len(steine), 1, -1):
        if any("".join(c) in woerter for c in set(combinations(sorted(steine), n))):
            return n
    return 0


seite = (HIER / "index.html").read_text(encoding="utf-8")
runden = json.loads(html.unescape(re.search(r"data-runden='([^']+)'", seite).group(1)))
for r in runden:
    steine = r["verdeckt"] + r["offen"]
    n = laengste(steine)
    echt = n >= r["gebot"]
    gelegt = r["wort"]
    assert echt == (r["ausgang"] == "echt"), (r, n)
    assert sorted(gelegt) == sorted(gelegt) and all(steine.count(c) >= gelegt.count(c) for c in gelegt), r
    assert "".join(sorted(gelegt)) in woerter and gelegt in woerter["".join(sorted(gelegt))], r
    assert len(gelegt) == (r["gebot"] if echt else n), (r, n)
    print("Runde ok:", r["verdeckt"], "+", r["offen"], "Gebot", r["gebot"], "->", r["ausgang"], gelegt)
print("fertig")

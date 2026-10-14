"""Baut Schriften und Bilder der Mancala-Ukoo-Seite aus dem Store-Material.

Quelle nur lesend: Apps/Spiele/mancala-ukoo (master = Produktion 13 / 0.5.0, Store-Bilder 0.5.0).
Aufruf: python seiten/mancala/_bauen.py
"""
import sys
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

APP = Path(r"D:/OneDrive/Apps/Spiele/mancala-ukoo")
STORE = APP / "store"

# Schrift: Kurale (einziger Schnitt, Titel); Fliesstext wie in der App: Systemschrift
woff2(APP / "app/src/main/res/font/kurale_regular.ttf", HIER / "schrift" / "kurale-regular.woff2")
(HIER / "schrift" / "OFL-Kurale.txt").write_bytes((APP / "docs/KURALE_OFL.txt").read_bytes())

B = HIER / "bilder"
for sprache, ordner in [("de", "screenshots"), ("en", "screenshots-en")]:
    for i, f in enumerate(sorted((STORE / ordner).glob("*.png")), 1):
        for w in (360, 720):
            print(sprache, f.name, w, webp(f, B / f"telefon-{sprache}-{i}-{w}.webp", w))

png(STORE / "icon_512.png", B / "icon-192.png", 192)
png(STORE / "icon_512.png", B / "apple-touch-icon.png", 180)
png(STORE / "icon_512.png", B / "favicon-32.png", 32)

# Open-Graph-Bild 1200x630 aus der Feature-Grafik. Play hat nur eine (de-DE, Text deutsch):
# beide Sprachen bekommen sie.
fg = Image.open(STORE / "feature_grafik.png").convert("RGB")
grund = fg.getpixel((4, 4))
fg = fg.resize((1200, round(fg.height * 1200 / fg.width)), Image.LANCZOS)
og = Image.new("RGB", (1200, 630), grund)
og.paste(fg, (0, (630 - fg.height) // 2))
for sprache in ("de", "en"):
    og.save(B / f"og-{sprache}.png", optimize=True)

for sprache in ("de", "en"):
    (B / f"google-play-badge-{sprache}.png").write_bytes((HIER / "_quelle" / f"google-play-badge-{sprache}.png").read_bytes())
print("fertig")

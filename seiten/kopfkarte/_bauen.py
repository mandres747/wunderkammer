"""Baut Schriften und Bilder der Kopfkarte-Seite aus dem Store-Material.

Quelle ist nur lesend das App-Repo (Apps/kopfkarte, Stand 0.2.0 (3) im geschlossenen Test,
noch nicht in Produktion). Aufruf: python seiten/kopfkarte/_bauen.py
"""
import sys
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

APP = Path(r"D:/OneDrive/Apps/kopfkarte")
STORE = APP / "store"
FONTS = APP / "app/src/main/res/font"

# Schriften: dieselben festen Schnitte wie in der App (Alegreya, Alegreya SC, Alegreya Sans)
for name in ["alegreya_bold", "alegreya_medium", "alegreya_sc_medium", "alegreya_sc_bold",
             "alegreya_sans_regular", "alegreya_sans_medium", "alegreya_sans_bold"]:
    woff2(FONTS / f"{name}.ttf", HIER / "schrift" / f"{name.replace('_', '-')}.woff2")
(HIER / "schrift" / "OFL-Alegreya.txt").write_bytes((APP / "app/src/main/assets/licenses/alegreya_OFL.txt").read_bytes())

B = HIER / "bilder"
# Telefon-Screenshots je Sprache (Store-Rahmen mit Alegreya, 1080x1920)
for sprache in ("de", "en"):
    for f in sorted((STORE / "screenshots" / sprache).glob("*.png")):
        for w in (360, 720):
            print(sprache, f.name, w, webp(f, B / f"telefon-{sprache}-{f.stem}-{w}.webp", w))

# Icons
ICON = STORE / "grafik/icon_store_512.png"
png(ICON, B / "icon-192.png", 192)
png(ICON, B / "apple-touch-icon.png", 180)
png(ICON, B / "favicon-32.png", 32)

# Open-Graph-Bild 1200x630 aus der Feature-Grafik (Canva) je Sprache
for sprache in ("de", "en"):
    fg = Image.open(STORE / f"grafik/feature_{sprache}_1024x500.png").convert("RGB")
    grund = fg.getpixel((4, 4))
    hoehe = 600
    fg = fg.resize((round(fg.width * hoehe / fg.height), hoehe), Image.LANCZOS)
    og = Image.new("RGB", (1200, 630), grund)
    og.paste(fg, ((1200 - fg.width) // 2, (630 - hoehe) // 2))
    og.save(B / f"og-{sprache}.png", optimize=True)

# Google-Play-Badges: nur kopieren, nie veraendern (erst sichtbar, wenn die App erscheint)
for sprache in ("de", "en"):
    (B / f"google-play-badge-{sprache}.png").write_bytes((HIER / "_quelle" / f"google-play-badge-{sprache}.png").read_bytes())
print("fertig")

"""Baut Schriften und Bilder der Nenne-drei-Seite aus dem Store-Material.

Quelle ist nur lesend das App-Repo (Spiele/nenne-drei, Stand 1.6.0 in Produktion).
Aufruf: python seiten/nennedrei/_bauen.py   (Ausgabe nach seiten/nennedrei/{schrift,bilder})
"""
import sys
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

APP = Path(r"D:/OneDrive/Apps/Spiele/nenne-drei")
STORE = APP / "playstore"
FONTS = APP / "app/src/main/res/font"
BADGES = HIER / "_quelle"  # offizielle Google-Play-Badges, unveraendert

# Schriften: dieselben festen Schnitte wie in der App
for name in ["bricolage_grotesque_extrabold", "figtree_regular", "figtree_semibold", "figtree_bold"]:
    woff2(FONTS / f"{name}.ttf", HIER / "schrift" / f"{name.replace('_', '-')}.woff2")
for lic in ["OFL-BricolageGrotesque.txt", "OFL-Figtree.txt"]:
    (HIER / "schrift" / lic).write_bytes((APP / "app/src/main/assets/licenses" / lic).read_bytes())

B = HIER / "bilder"
# Telefon-Screenshots (de-DE; en-US hat im Store keine eigenen Telefonbilder)
for f in sorted((STORE / "screenshots").glob("*.png")):
    for w in (360, 720):
        print(f.name, w, webp(f, B / f"telefon-{f.stem}-{w}.webp", w))
# Fernseher-Screenshots je Sprache
for sprache, ordner in [("de", "de-DE"), ("en", "en-US")]:
    for f in sorted((STORE / "screenshots-tv" / ordner).glob("*.png")):
        for w in (800, 1600):
            print(sprache, f.name, w, webp(f, B / f"tv-{sprache}-{f.stem}-{w}.webp", w))

# Icons
png(STORE / "icon-512.png", B / "icon-192.png", 192)
png(STORE / "icon-512.png", B / "apple-touch-icon.png", 180)
png(STORE / "icon-512.png", B / "favicon-32.png", 32)

# Open-Graph-Bild 1200x630 aus der Feature-Grafik (Canva) je Sprache
for sprache, datei in [("de", "feature-graphic-1024x500.png"), ("en", "feature-graphic-1024x500-en.png")]:
    fg = Image.open(STORE / datei).convert("RGB")
    grund = fg.getpixel((4, 4))
    hoehe = 600
    fg = fg.resize((round(fg.width * hoehe / fg.height), hoehe), Image.LANCZOS)
    og = Image.new("RGB", (1200, 630), grund)
    og.paste(fg, ((1200 - fg.width) // 2, (630 - hoehe) // 2))
    og.save(B / f"og-{sprache}.png", optimize=True)

# Google-Play-Badges: nur kopieren, nie veraendern (Badge-Richtlinien)
for sprache in ("de", "en"):
    (B / f"google-play-badge-{sprache}.png").write_bytes((BADGES / f"google-play-badge-{sprache}.png").read_bytes())
print("fertig")

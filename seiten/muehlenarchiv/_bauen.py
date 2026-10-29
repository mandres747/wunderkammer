"""Baut Schriften und Bilder der Muehlenarchiv-Seite aus dem Store-Material.

Quelle nur lesend: Apps/Spiele/muehlen (master = 0.3.0 (4), geschlossener Test; noch nicht in Produktion).
Aufruf: python seiten/muehlenarchiv/_bauen.py
"""
import sys
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

APP = Path(r"D:/Apps/Spiele/muehlen")
STORE = APP / "store"
FONTS = APP / "app/src/main/res/font"

for name in ["young_serif_regular", "public_sans_regular", "public_sans_semibold"]:
    woff2(FONTS / f"{name}.ttf", HIER / "schrift" / f"{name.replace('_', '-')}.woff2")
for lic, ziel in [("young_serif_OFL.txt", "OFL-YoungSerif.txt"), ("public_sans_OFL.txt", "OFL-PublicSans.txt")]:
    (HIER / "schrift" / ziel).write_bytes((APP / "app/src/main/assets/licenses" / lic).read_bytes())

B = HIER / "bilder"
# Store-Screenshots 9:16 mit Matrizen-Rahmen (dieselben wie im Play-Eintrag, je Sprache)
for f in sorted((STORE / "screens_store").glob("*.png")):
    for w in (360, 720):
        print(f.name, w, webp(f, B / f"telefon-{f.stem}-{w}.webp", w))

png(STORE / "icon_512.png", B / "icon-192.png", 192)
png(STORE / "icon_512.png", B / "apple-touch-icon.png", 180)
png(STORE / "icon_512.png", B / "favicon-32.png", 32)

for sprache in ("de", "en"):
    fg = Image.open(STORE / f"feature_{sprache}.png").convert("RGB")
    grund = fg.getpixel((1000, 480))
    fg = fg.resize((1200, round(fg.height * 1200 / fg.width)), Image.LANCZOS)
    og = Image.new("RGB", (1200, 630), grund)
    og.paste(fg, (0, (630 - fg.height) // 2))
    og.save(B / f"og-{sprache}.png", optimize=True)

for sprache in ("de", "en"):
    (B / f"google-play-badge-{sprache}.png").write_bytes((HIER / "_quelle" / f"google-play-badge-{sprache}.png").read_bytes())
print("fertig")

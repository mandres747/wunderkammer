"""Baut Schriften und Bilder der Malfeld-Seite aus dem App-Repo (nur lesend).

Produktions-Track: 0.8.1 (15), seit 08.10.2026 live im Store (play_scan.py bestätigt).
Aufruf: python seiten/malfeld/_bauen.py
"""
import sys
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

APP = Path(r"D:/Apps/malfeld")
FONTS = APP / "app/src/main/res/font"
LIZ = APP / "app/src/main/assets/licenses"
SHOTS = APP / "store/assets/screenshots-0.8.1"
B = HIER / "bilder"
S = HIER / "schrift"

# Schriften wie in der App: Playpen Sans (Titel), Atkinson Hyperlegible (Text, Ziffern)
woff2(FONTS / "playpen_sans_bold.ttf", S / "playpen-sans-bold.woff2")
woff2(FONTS / "atkinson_hyperlegible_regular.ttf", S / "atkinson-hyperlegible-regular.woff2")
woff2(FONTS / "atkinson_hyperlegible_bold.ttf", S / "atkinson-hyperlegible-bold.woff2")
for lic in ["PlaypenSans-OFL.txt", "AtkinsonHyperlegible-OFL.txt"]:
    (S / lic).write_bytes((LIZ / lic).read_bytes())

# Telefon-Screenshots (Store-Satz 0.8.1, de-DE)
for f in sorted((SHOTS / "telefon").glob("*.png")):
    for w in (360, 720):
        print(f.name, w, webp(f, B / f"telefon-{f.stem}-{w}.webp", w))
# 10-Zoll-Tablet quer: Reise und Brüche
for stem in ["02_reise", "06_pizza"]:
    for w in (800, 1600):
        print(stem, w, webp(SHOTS / "tablet10" / f"{stem}.png", B / f"tablet-{stem}-{w}.webp", w))

# Icons
icon = APP / "store/assets/icon_512.png"
png(icon, B / "icon-192.png", 192)
png(icon, B / "apple-touch-icon.png", 180)
png(icon, B / "favicon-32.png", 32)

# Open-Graph-Bild 1200x630 aus der Feature-Grafik (auf Höhe 630 skaliert, Ränder beschnitten)
fg = Image.open(APP / "store/assets/feature_1024x500.png").convert("RGB")
fg = fg.resize((round(fg.width * 630 / fg.height), 630), Image.LANCZOS)
links = (fg.width - 1200) // 2
fg.crop((links, 0, links + 1200, 630)).save(B / "og-de.png", optimize=True)

# Google-Play-Badge (offiziell, unverändert)
(B / "google-play-badge-de.png").write_bytes((HIER / "_quelle" / "google-play-badge-de.png").read_bytes())
print("fertig")

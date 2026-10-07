"""Baut Schriften und Bilder der Seite von Zunft der Sechs aus dem Store-Material.

Quelle ist nur lesend das App-Repo (Apps/Spiele/wuerfelwerkstatt, Tag v0.2.0 = 0.2.0 (3) im
geschlossenen Test, noch nicht in Produktion). Aufruf: python seiten/zunft/_bauen.py
"""
import sys
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

APP = Path(r"D:/OneDrive/Apps/Spiele/wuerfelwerkstatt")
STORE = APP / "store"
RES = APP / "app/src/main/res"
FONTS = RES / "font"
BILD = RES / "drawable-nodpi"   # Kupferstiche aus Canva (KI-unterstützt, in der App gekennzeichnet)

# Schriften: dieselben festen Schnitte wie in der App
for name in ["instrument_serif_regular", "instrument_sans_regular", "instrument_sans_semibold",
             "martian_mono_regular", "martian_mono_semibold"]:
    woff2(FONTS / f"{name}.ttf", HIER / "schrift" / f"{name.replace('_', '-')}.woff2")
for lic in ["OFL_InstrumentSerif.txt", "OFL_InstrumentSans.txt", "OFL_MartianMono.txt"]:
    (HIER / "schrift" / lic.replace("_", "-")).write_bytes((APP / "app/src/main/assets/licenses" / lic).read_bytes())

B = HIER / "bilder"
# Telefon-Screenshots je Sprache (1080x1800)
for sprache, ordner in (("de", "de-DE"), ("en", "en-US")):
    for f in sorted((STORE / "screenshots" / ordner).glob("*.png")):
        for w in (360, 720):
            print(sprache, f.name, w, webp(f, B / f"telefon-{sprache}-{f.stem}-{w}.webp", w))

# Kupferstiche (ohne Text, für beide Sprachen)
for name, breiten in (("prolog_1", (540, 1080)), ("karte_walz", (540, 1080))):
    for w in breiten:
        print(name, w, webp(BILD / f"{name}.webp", B / f"{name.replace('_', '-')}-{w}.webp", w))
for name in ("tal_kupfer", "tal_amboss", "tal_einser", "tal_dreiauge"):
    print(name, webp(BILD / f"{name}.webp", B / f"{name.replace('_', '-')}.webp", 256))

# Icons
ICON = STORE / "icon_512.png"
png(ICON, B / "icon-192.png", 192)
png(ICON, B / "apple-touch-icon.png", 180)
png(ICON, B / "favicon-32.png", 32)

# Open-Graph-Bild 1200x630 aus der Feature-Grafik (Canva) je Sprache
for sprache in ("de", "en"):
    fg = Image.open(STORE / f"grafik/feature_{sprache}.png").convert("RGB")
    grund = fg.getpixel((fg.width - 4, 4))
    hoehe = 600
    fg = fg.resize((round(fg.width * hoehe / fg.height), hoehe), Image.LANCZOS)
    og = Image.new("RGB", (1200, 630), grund)
    og.paste(fg, ((1200 - fg.width) // 2, (630 - hoehe) // 2))
    og.save(B / f"og-{sprache}.png", optimize=True)

# Google-Play-Badges: nur kopieren, nie veraendern (erst sichtbar, wenn die App erscheint)
for sprache in ("de", "en"):
    (B / f"google-play-badge-{sprache}.png").write_bytes((HIER / "_quelle" / f"google-play-badge-{sprache}.png").read_bytes())
print("fertig")

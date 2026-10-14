"""Baut Schriften und Bilder der Wortgenau-Seite.

Quellen (nur lesend, nach _quelle/ kopiert bzw. per Play-API geladen):
- Schrift: wortgenau, Branch feature/vokabelblitz: res/font/lexend.ttf (variabel) +
  assets/licenses/OFL-Lexend.txt (Gestaltung "Fokuslinie"; 1.0.3 in Produktion hat noch Roboto)
- Store-Bilder: live per API (edits.images, de-DE/en-US) nach _quelle/store/
- Badges: offizielle Google-Play-Badges, unveraendert
Aufruf: python seiten/deepwave/_bauen.py
"""
import sys
from pathlib import Path

from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

Q = HIER / "_quelle"
S = Q / "store"
B = HIER / "bilder"

# Lexend variabel, auf wght 300-700 beschraenkt (kleiner), dann WOFF2-Teilmenge
from fontTools.ttLib import TTFont  # noqa: E402
from fontTools.varLib import instancer  # noqa: E402
tmp = Q / "_lexend-300-700.ttf"
instancer.instantiateVariableFont(TTFont(Q / "lexend.ttf"), {"wght": (300, 700)}).save(tmp)
woff2(tmp, HIER / "schrift" / "lexend.woff2")
tmp.unlink()
(HIER / "schrift" / "OFL-Lexend.txt").write_bytes((Q / "OFL-Lexend.txt").read_bytes())

for sprache, ordner in [("de", "de-DE"), ("en", "en-US")]:
    for f in sorted(S.glob(f"{ordner}-phoneScreenshots-*.png")):
        nr = f.stem.rsplit("-", 1)[1]
        for w in (360, 720):
            print(sprache, nr, w, webp(f, B / f"telefon-{sprache}-{nr}-{w}.webp", w))

png(S / "de-DE-icon-01.png", B / "icon-192.png", 192)
png(S / "de-DE-icon-01.png", B / "apple-touch-icon.png", 180)
png(S / "de-DE-icon-01.png", B / "favicon-32.png", 32)

# Open-Graph-Bild 1200x630 aus der Feature-Grafik je Sprache (Rand in Grundfarbe der Grafik)
for sprache, ordner in [("de", "de-DE"), ("en", "en-US")]:
    fg = Image.open(S / f"{ordner}-featureGraphic-01.png").convert("RGB")
    grund = fg.getpixel((4, fg.height - 4))
    hoehe = 600
    fg = fg.resize((round(fg.width * hoehe / fg.height), hoehe), Image.LANCZOS)
    og = Image.new("RGB", (1200, 630), grund)
    og.paste(fg, ((1200 - fg.width) // 2, (630 - hoehe) // 2))
    og.save(B / f"og-{sprache}.png", optimize=True)

for sprache in ("de", "en"):
    (B / f"google-play-badge-{sprache}.png").write_bytes((Q / f"google-play-badge-{sprache}.png").read_bytes())
print("fertig")

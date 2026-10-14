"""Baut die Bausteine der Startseite https://wunderkammer-apps.de/ (Sammlerbogen).

Erzeugt unter wunderkammer/assets/:
  schrift/   EB Garamond + Caveat als WOFF2-Teilmenge (OFL-Texte daneben)
  bilder/    App-Icons (aus seiten/<sub>/bilder), je ein Screenshot der Apps im Store,
             Fundstuecke (Canva-Kupferstich, freigestellt), Favicons, og-de.png/og-en.png

Quelle der Fundstuecke: Canva generate-image (Media MAHW-2vZgus), exportiert ueber das
Hilfsdesign DAHW-zBSzjc nach store/startseite_quelle/fundstuecke_canva.png (3840 x 2160).

Aufruf:  python store/make_startseite.py      (braucht fonttools, brotli, pillow)
"""
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SEITEN = ROOT / "seiten"
OUT = ROOT / "assets"
sys.path.insert(0, str(SEITEN / "werkzeug"))
from helfer import webp, woff2  # noqa: E402

import make_developer_page as dev  # noqa: E402  (Farben, Fundkarten-Zeichnung, Schriften)

INK = (28, 38, 48)

# App-Kuerzel = Unterdomain; Icons und Screenshots kommen aus den fertigen App-Seiten.
APPS = ["deepwave", "lesepfadfinder", "mancala", "nennedrei", "wortgenau", "malfeld",
        "kopfkarte", "zunft", "muehlenarchiv", "einsatz", "kerbe"]
SCREENS = {  # nur Apps, die bei Google Play stehen
    "deepwave": "telefon-de-01", "lesepfadfinder": "telefon-01_entscheidung",
    "mancala": "telefon-de-2", "nennedrei": "telefon-1_spiel",
    "malfeld": "telefon-02_reise", "wortgenau": "telefon-de-01",
}
SCREENS_EN = {"deepwave": "telefon-en-01", "mancala": "telefon-en-2", "wortgenau": "telefon-en-01"}

# Fundstuecke im Canva-Export (x0, y0, x1, y1), grosszuegig; danach Zuschnitt auf Inhalt.
FUNDE = {
    "muschel": (250, 20, 1440, 1060), "feder": (1460, 40, 2320, 2060),
    "kaefer": (2560, 90, 3170, 765), "schluessel": (2580, 785, 3620, 1280),
    "kapsel": (400, 1150, 1130, 2090), "seestern": (2080, 1250, 3320, 2160),
}


def schriften():
    ziel = OUT / "schrift"
    woff2(dev.FONTS / "EBGaramond.ttf", ziel / "ebgaramond.woff2")
    woff2(dev.FONTS / "Caveat.ttf", ziel / "caveat.woff2")
    for f in ("OFL-EBGaramond.txt", "OFL-Caveat.txt"):
        shutil.copy(dev.FONTS / f, ziel / f)


def icons_und_screens():
    b = OUT / "bilder"
    b.mkdir(parents=True, exist_ok=True)
    for sub in APPS:
        Image.open(SEITEN / sub / "bilder/icon-192.png").convert("RGBA").save(b / f"icon-{sub}.png", optimize=True)
    for sub, name in {**SCREENS, **{k + "-en": v for k, v in SCREENS_EN.items()}}.items():
        app = sub.removesuffix("-en")
        for w in (360, 720):
            shutil.copy(SEITEN / app / f"bilder/{name}-{w}.webp", b / f"screen-{sub}-{w}.webp")


def groesstes_stueck(alpha):
    """Nur das groesste zusammenhaengende Motiv behalten (Nachbarn ragen in den Zuschnitt)."""
    import numpy as np
    from scipy import ndimage
    a = np.asarray(alpha)
    maske = ndimage.binary_dilation(a > 20, iterations=12)  # Schraffur-Luecken schliessen
    marken, n = ndimage.label(maske)
    if n > 1:
        groessen = ndimage.sum(maske, marken, range(1, n + 1))
        a = np.where(marken == 1 + int(np.argmax(groessen)), a, 0).astype("uint8")
    return Image.fromarray(a)


def badges():
    """Logo unveraendert, nur den durchsichtigen Leerraum ringsum wegschneiden (Apples
    App-Store-Badge-SVG hat keinen -- sonst wirkt Google trotz gleicher CSS-Hoehe kleiner)."""
    for sprache in ("de", "en"):
        quelle = Image.open(SEITEN / f"deepwave/bilder/google-play-badge-{sprache}.png").convert("RGBA")
        quelle.crop(quelle.getbbox()).save(OUT / "bilder" / f"google-play-{sprache}.png", optimize=True)


def fundstuecke():
    """Kupferstich freistellen: Helligkeit -> Deckkraft, Farbe = Tinte."""
    quelle = Image.open(HERE / "startseite_quelle/fundstuecke_canva.png").convert("L")
    grund = 219  # Kartonton des Exports
    for name, box in FUNDE.items():
        g = quelle.crop(box)
        alpha = g.point(lambda v: 0 if v >= grund - 12 else min(255, int((grund - 12 - v) * 255 / 150)))
        alpha = groesstes_stueck(alpha)
        bbox = alpha.getbbox()
        alpha = alpha.crop(bbox)
        stueck = Image.new("RGBA", alpha.size, INK + (0,))
        stueck.putalpha(alpha)
        stueck.thumbnail((520, 520), Image.LANCZOS)
        stueck.save(OUT / "bilder" / f"fund-{name}.webp", "WEBP", quality=86, method=6)


def favicons():
    sym = Image.open(HERE / "canva_symbol.png").convert("RGB")
    for kante, name in ((32, "favicon-32.png"), (180, "apple-touch-icon.png"), (192, "icon-192.png")):
        sym.resize((kante, kante), Image.LANCZOS).save(OUT / "bilder" / name, optimize=True)


def og(sprache):
    """1200 x 630 im Stil des Play-Kopfbilds: Wortmarke links, Fundkarten rechts."""
    W, H = 1200, 630
    img = Image.new("RGBA", (W, H), dev.CARTON + (255,))
    d = ImageDraw.Draw(img)
    for y in range(0, H, 28):
        d.line((0, y, W, y), fill=dev.CARTON_LINE, width=1)
    claim, faecher, fakten = {
        "de": ("Kleine Apps, sorgfältig gemacht.", "Lesen · Lernen · Spielen · Entspannen",
               "ohne Werbung · ohne Tracker · ohne Abo"),
        "en": ("Small apps, made with care.", "Read · Learn · Play · Unwind",
               "no ads · no trackers · no subscriptions"),
    }[sprache]
    d.text((70, 200), "Wunderkammer", font=dev.garamond(92, 700), fill=INK)
    d.text((74, 318), claim, font=dev.caveat(50, 600), fill=INK)
    d.text((74, 374), faecher, font=dev.caveat(42, 500), fill=dev.INK_SOFT)
    d.text((74, 450), fakten, font=dev.garamond(28, 500), fill=INK)
    pos = [("nennedrei", 800, 170, -5), ("deepwave", 1020, 150, 4),
           ("mancala", 820, 450, 3), ("lesepfadfinder", 1040, 430, -4)]
    s = 130
    for sub, x, y, rot in pos:
        karte = Image.new("RGBA", (s + 44, s + 60), dev.CARD + (255,))
        icon = Image.open(OUT / "bilder" / f"icon-{sub}.png").convert("RGBA").resize((s, s), Image.LANCZOS)
        karte.alpha_composite(icon, (22, 22))
        karte = karte.rotate(rot, resample=Image.BICUBIC, expand=True)
        cx, cy = x - karte.width // 2, y - karte.height // 2
        schatten = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        schatten.paste((20, 30, 40, 90), (cx + 5, cy + 9), karte.split()[3])
        img.alpha_composite(schatten.filter(ImageFilter.GaussianBlur(8)))
        img.alpha_composite(karte, (cx, cy))
        d = ImageDraw.Draw(img)
        py = cy + 14
        d.ellipse((x - 10, py - 10, x + 10, py + 10), fill=dev.PIN_DARK)
        d.ellipse((x - 8, py - 9, x + 7, py + 6), fill=dev.PIN)
    img.convert("RGB").save(OUT / "bilder" / f"og-{sprache}.png", optimize=True)


if __name__ == "__main__":
    schriften()
    icons_und_screens()
    badges()
    fundstuecke()
    favicons()
    og("de")
    og("en")
    for p in sorted(OUT.rglob("*")):
        if p.is_file():
            print(f"{p.relative_to(OUT)}  {p.stat().st_size / 1024:.0f} kB")

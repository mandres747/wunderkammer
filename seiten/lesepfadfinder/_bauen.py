"""Baut Schriften und Bilder der Lesepfadfinder-Seite aus dem App-Repo (nur lesend).

Produktion live: 1.0.4 (9) = eb-player f089522; 1.1.0 (10) „Fährtenzeichen“ liegt in der Prüfung.
Die Screenshots kommen deshalb aus dem Satz, der im Store gerade live ist (1.0.4, per git show).
Sobald 1.1.0 live ist: SATZ = "1.1.0" setzen, neu bauen, Alt-Texte prüfen, hochladen.

Aufruf: python seiten/lesepfadfinder/_bauen.py          (alles)
        python seiten/lesepfadfinder/_bauen.py presse   (nur bilder/presse/ für presse/index.html)
"""
import io
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "werkzeug"))
from helfer import png, webp, woff2  # noqa: E402

APP = Path(r"D:/OneDrive/Apps/eb-player")
FONTS = APP / "app/src/main/res/font"
STORE = APP / "docs/store"
PROD = "f089522"            # 1.0.4 (9), Produktion live
SATZ = "1.0.4"              # "1.1.0" -> docs/store/screenshots/play-1.1.0
B = HIER / "bilder"
S = HIER / "schrift"
TMP = HIER / "_quelle" / "tmp"
TMP.mkdir(parents=True, exist_ok=True)


def git_datei(pfad: str) -> bytes:
    return subprocess.run(["git", "-C", str(APP), "show", f"{PROD}:{pfad}"], check=True, capture_output=True).stdout


# --- Pressebilder (presse/index.html): Originale in voller Auflösung + ZIP ---
# Screenshots folgen SATZ (wie die Galerie), Icon und Feature-Grafik sind die Store-Dateien.
PRESSE = B / "presse"
PRESSE_SCREENS = [("01_entscheidung", "1-entscheidung"), ("02_reader", "2-lesen"),
                  ("03_ende", "3-ende"), ("04_lesewege", "4-enden-sammlung")]
PRESSE_LIESMICH = """Lesepfadfinder – Pressebilder
==============================

Frei für die Berichterstattung über Lesepfadfinder.
Quellenangabe bitte: „Bild: Wunderkammer“.

lesepfadfinder-icon-512.png           App-Symbol, 512 × 512 px
lesepfadfinder-feature-1024x500.png   Titelgrafik aus dem Play Store, 1024 × 500 px
lesepfadfinder-screenshot-*.png       Bildschirmfotos vom Smartphone, 1080 × 2340 px

Die Bildschirmfotos zeigen den aktuellen Stand im Play Store.
Pressekontakt: Michael Andres, kontakt@wunderkammer-apps.de
https://lesepfadfinder.wunderkammer-apps.de/presse/
"""


def presse() -> None:
    PRESSE.mkdir(parents=True, exist_ok=True)
    dateien = {
        "lesepfadfinder-icon-512.png": (STORE / "icon_512.png").read_bytes(),
        "lesepfadfinder-feature-1024x500.png": (STORE / "feature_1024x500.png").read_bytes(),
    }
    for n, name in PRESSE_SCREENS:
        if SATZ == "1.0.4":
            roh = git_datei(f"docs/store/screenshots/{n}.png")
        else:
            roh = (STORE / "screenshots/play-1.1.0" / f"{n}.png").read_bytes()
        dateien[f"lesepfadfinder-screenshot-{name}.png"] = roh
    for name, roh in dateien.items():
        (PRESSE / name).write_bytes(roh)  # unverändert, volle Auflösung
    # Vorschau der Feature-Grafik für die Seite (Screenshots nutzen die Galerie-WebPs)
    print("feature", webp(STORE / "feature_1024x500.png", PRESSE / "feature-vorschau-1024.webp", 1024))
    with zipfile.ZipFile(PRESSE / "lesepfadfinder-pressebilder.zip", "w", zipfile.ZIP_STORED) as z:
        z.writestr("LIESMICH.txt", PRESSE_LIESMICH.encode("utf-8"))
        for name, roh in dateien.items():
            z.writestr(name, roh)  # PNG ist schon komprimiert
    for p in sorted(PRESSE.iterdir()):
        print("presse", p.name, p.stat().st_size)


if sys.argv[1:] == ["presse"]:  # nur Pressebilder: python _bauen.py presse
    presse()
    shutil.rmtree(TMP, ignore_errors=True)
    sys.exit(0)


# --- Schriften: Grandstander Bold (Titel, wie in der App) + Andika (Lesetext der App) ---
woff2(FONTS / "grandstander_bold.ttf", S / "grandstander-bold.woff2")
(S / "OFL-Grandstander.txt").write_bytes((APP / "app/src/main/assets/licenses/Grandstander-OFL.txt").read_bytes())
# Andika hat die Reserved Font Names „Andika“ und „SIL“. Eine Teilmenge ist eine veränderte Fassung,
# darf diese Namen also nicht tragen -> interne Namen umbenennen („Pfad Lesetext“).
for schnitt, stil in [("regular", "Regular"), ("bold", "Bold")]:
    ziel = S / f"pfad-lesetext-{schnitt}.woff2"
    woff2(FONTS / f"andika_{schnitt}.ttf", ziel)
    f = TTFont(ziel)
    name = f["name"]
    for rec in list(name.names):
        if rec.nameID in (1, 16):
            rec.string = "Pfad Lesetext"
        elif rec.nameID in (17, 2):
            rec.string = stil
        elif rec.nameID == 4:
            rec.string = f"Pfad Lesetext {stil}"
        elif rec.nameID == 6:
            rec.string = f"PfadLesetext-{stil}"
        elif rec.nameID == 3:
            rec.string = f"Pfad Lesetext {stil}; Teilmenge von Andika (SIL)"
    f.flavor = "woff2"
    f.save(ziel)
lizenz = TTFont(FONTS / "andika_regular.ttf")["name"].getDebugName(13)
grand = (APP / "app/src/main/assets/licenses/Grandstander-OFL.txt").read_text(encoding="utf-8")
ofl_text = grand[grand.index("-----------------------------------------------------------\nSIL OPEN FONT LICENSE"):]
(S / "OFL-Andika.txt").write_text(
    "Pfad Lesetext ist eine Web-Teilmenge (WOFF2) von Andika, umbenannt wegen der Reserved Font Names.\n\n"
    "Copyright (c) 2004-2022 SIL International (http://www.sil.org/) with Reserved Font Names \"Andika\" and \"SIL\".\n\n"
    "This Font Software is licensed under the SIL Open Font License, Version 1.1.\n"
    "This license is copied below, and is also available with a FAQ at:\nhttps://scripts.sil.org/OFL\n\n\n" + ofl_text,
    encoding="utf-8")

# --- Screenshots (Telefon, de-DE; en-US gibt es im Store nicht) ---
NAMEN = ["01_entscheidung", "02_reader", "03_ende", "04_lesewege", "05_bibliothek", "06_eltern"]
for n in NAMEN:
    if SATZ == "1.0.4":
        quelle = TMP / f"{n}.png"
        quelle.write_bytes(git_datei(f"docs/store/screenshots/{n}.png"))
    else:
        quelle = STORE / "screenshots/play-1.1.0" / f"{n}.png"
    for w in (360, 720):
        print(n, w, webp(quelle, B / f"telefon-{n}-{w}.webp", w))

# --- Buchcover aus den Buchpaketen der Produktionsversion ---
for buch in ["emmi-ermittelt-band-1", "emmi-ermittelt-band-2", "kuboria-band-1", "kuboria-band-2"]:
    z = zipfile.ZipFile(io.BytesIO(git_datei(f"app/src/main/assets/books/{buch}.ebk")))
    quelle = TMP / f"cover-{buch}.png"
    Image.open(io.BytesIO(z.read("cover.webp"))).save(quelle)
    for w in (240, 480):
        print(buch, w, webp(quelle, B / f"cover-{buch}-{w}.webp", w))

# --- Icons (Store-Icon ist live) ---
png(STORE / "icon_512.png", B / "icon-192.png", 192)
png(STORE / "icon_512.png", B / "apple-touch-icon.png", 180)
png(STORE / "icon_512.png", B / "favicon-32.png", 32)

# --- Open-Graph-Bild 1200x630 aus der Feature-Grafik (auf Höhe 630 skaliert, Ränder beschnitten) ---
fg = Image.open(STORE / "feature_1024x500.png").convert("RGB")
fg = fg.resize((round(fg.width * 630 / fg.height), 630), Image.LANCZOS)
links = (fg.width - 1200) // 2
fg.crop((links, 0, links + 1200, 630)).save(B / "og-de.png", optimize=True)

# --- Google-Play-Badge: Logo unveraendert, nur den durchsichtigen Leerraum ringsum
# wegschneiden (Apples App-Store-Badge-SVG hat keinen -- sonst wirkt Google kleiner,
# obwohl beide Badges per CSS auf dieselbe Hoehe gesetzt sind) ---
_badge = Image.open(HIER / "_quelle" / "google-play-badge-de.png").convert("RGBA")
_badge.crop(_badge.getbbox()).save(B / "google-play-badge-de.png", optimize=True)
presse()
shutil.rmtree(TMP)  # Zwischenbilder nicht im Repo liegen lassen
print("fertig")

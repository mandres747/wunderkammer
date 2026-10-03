"""Gemeinsame Bauhelfer fuer die App-Seiten (seiten/<sub>/).

Nur Handwerk, keine Gestaltung: Schriften als WOFF2-Teilmenge, Bilder als WebP.
Jede Seite ruft das aus ihrem eigenen _bauen.py auf (siehe MUSTER.md).
Braucht: pip install fonttools brotli pillow
"""
from pathlib import Path

from fontTools import subset
from PIL import Image

# Latein + Westeuropa (de/en/es/pt), Typografie (– … „“ ‚‘ ’ ·), Euro, Pfeile, schmales Leerzeichen.
UNICODES = (
    "U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+02C6,U+02DA,U+02DC,"
    "U+2009,U+200A,U+202F,U+2010-2014,U+2018-201E,U+2022,U+2026,U+2039-203A,"
    "U+20AC,U+2122,U+2190-2193,U+2212,U+00B7"
)


def woff2(ttf: Path, ziel: Path) -> None:
    """TTF -> WOFF2-Teilmenge (Layout-Features bleiben, Hinting fliegt raus)."""
    ziel.parent.mkdir(parents=True, exist_ok=True)
    subset.main([
        str(ttf), f"--unicodes={UNICODES}", "--flavor=woff2",
        "--layout-features=*", "--no-hinting", "--desubroutinize",
        f"--output-file={ziel}",
    ])


def webp(quelle: Path, ziel: Path, breite: int, qualitaet: int = 82) -> tuple[int, int]:
    """Bild auf `breite` verkleinern (nie vergroessern) und als WebP speichern. Gibt (b, h) zurueck."""
    ziel.parent.mkdir(parents=True, exist_ok=True)
    bild = Image.open(quelle).convert("RGB")
    if bild.width > breite:
        bild = bild.resize((breite, round(bild.height * breite / bild.width)), Image.LANCZOS)
    bild.save(ziel, "WEBP", quality=qualitaet, method=6)
    return bild.size


def png(quelle: Path, ziel: Path, kante: int) -> None:
    """Quadratisches Icon (Favicon, Apple-Touch) als PNG."""
    ziel.parent.mkdir(parents=True, exist_ok=True)
    Image.open(quelle).convert("RGBA").resize((kante, kante), Image.LANCZOS).save(ziel, optimize=True)

"""Erzeugt die Play-Console-Entwicklerseite: Entwicklersymbol (512x512) und
Kopfzeilenbild (4096x2304) fuer das Konto "Wunderkammer".

Motiv: eine Wunderkammer ist ein Kabinett mit Faechern, in denen Fundstuecke
liegen. Im Kopfzeilenbild liegen in den Faechern die Symbole der Apps; das
Entwicklersymbol zeigt das Kabinett allein, ohne Text (wird klein angezeigt).

Aufruf:  python make_developer_page.py
Ausgabe: developer_icon_512.png, developer_header_4096x2304.png (24-Bit-PNG,
ohne Transparenz, jeweils unter 1 MB).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).resolve().parent
APPS = HERE.parent.parent  # D:\OneDrive\Apps

# Farbwelt: Tinte, Messing, Pergament
INK = (18, 30, 38)
INK_LIGHT = (28, 46, 57)
BRASS = (201, 143, 63)
BRASS_DARK = (150, 102, 40)
PARCHMENT = (243, 234, 219)
MUTED = (166, 178, 186)

# Sammlerbogen (seit 2026-09-26): Karton, Tinte, Karte, Nadelrot
CARTON = (214, 221, 226)
CARTON_LINE = (204, 212, 218)
INK_C = (28, 38, 48)
INK_SOFT = (70, 84, 98)
CARD = (250, 250, 247)
PIN = (178, 52, 44)
PIN_DARK = (120, 32, 28)
FONTS = HERE / "fonts"  # EB Garamond + Caveat, OFL (Lizenzen daneben)


def garamond(size, wght):
    f = ImageFont.truetype(str(FONTS / "EBGaramond.ttf"), size)
    f.set_variation_by_axes([wght])
    return f


def caveat(size, wght):
    f = ImageFont.truetype(str(FONTS / "Caveat.ttf"), size)
    f.set_variation_by_axes([wght])
    return f


FONT_DIR = Path("C:/Windows/Fonts")
SERIF_BOLD = FONT_DIR / "georgiab.ttf"
SANS = FONT_DIR / "segoeui.ttf"
SANS_SEMI = FONT_DIR / "seguisb.ttf"

# Reihenfolge = Reihenfolge im Kabinett (links oben -> rechts unten)
APP_ICONS = [
    ("Wortgenau", "Lesen", APPS / "wortgenau/docs/store/icon_512.png"),
    ("Malfeld", "Lernen", APPS / "malfeld/store/assets/icon_512.png"),
    ("Lesepfadfinder", "Lesen", APPS / "eb-player/docs/store/icon_512.png"),
    ("Mancala Ukoo", "Spielen", APPS / "Spiele/mancala-ukoo/store/icon_512.png"),
    ("Nenne drei", "Spielen", APPS / "Spiele/nenne-drei/playstore/icon-512.png"),
    ("DeepWave", "Entspannen", APPS / "BinauralBeatsApp/playstore/ic_launcher-playstore.png"),
]


def font(path, size):
    return ImageFont.truetype(str(path), size)


def vertical_gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size, top)
    px = img.load()
    for y in range(h):
        t = y / max(1, h - 1)
        c = tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        for x in range(w):
            px[x, y] = c
    return img


def rounded_icon(path, size, radius):
    """App-Symbol als abgerundetes Quadrat mit weicher Schattenkante."""
    src = Image.open(path)
    if src.mode in ("RGBA", "LA") or "transparency" in src.info:
        # transparente Ecken auf Tintengrund legen statt auf Schwarz
        bg = Image.new("RGB", src.size, INK_LIGHT)
        bg.paste(src.convert("RGBA"), mask=src.convert("RGBA").split()[3])
        src = bg
    src = src.convert("RGB")
    inset = int(src.width * 0.04)  # Randartefakte (Schatten, Rahmen) wegschneiden
    icon = src.crop((inset, inset, src.width - inset, src.height - inset)).resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=255)
    return icon, mask


def draw_cabinet(draw, box, cols, rows, frame, gap, fill_inner):
    """Kabinettrahmen: aeusserer Messingrahmen, innen Faecher mit dunklem Grund."""
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=frame, fill=BRASS)
    draw.rounded_rectangle((x0 + frame // 3, y0 + frame // 3, x1 - frame // 3, y1 - frame // 3),
                           radius=frame // 2, fill=BRASS_DARK)
    inner = (x0 + frame, y0 + frame, x1 - frame, y1 - frame)
    draw.rectangle(inner, fill=BRASS)
    iw = inner[2] - inner[0]
    ih = inner[3] - inner[1]
    cw = (iw - gap * (cols + 1)) / cols
    ch = (ih - gap * (rows + 1)) / rows
    cells = []
    for r in range(rows):
        for c in range(cols):
            cx0 = inner[0] + gap + c * (cw + gap)
            cy0 = inner[1] + gap + r * (ch + gap)
            cell = (round(cx0), round(cy0), round(cx0 + cw), round(cy0 + ch))
            draw.rectangle(cell, fill=fill_inner)
            # feine Innenkante oben/links: Tiefe
            draw.line((cell[0], cell[1], cell[2], cell[1]), fill=INK, width=max(2, gap // 6))
            draw.line((cell[0], cell[1], cell[0], cell[3]), fill=INK, width=max(2, gap // 6))
            cells.append(cell)
    return cells


def make_icon(out):
    """Entwicklersymbol: Canva-Motiv (angesteckte Karte mit Muschel, Design
    DAHWSHzD4Y4, Export canva_symbol.png) auf 512 x 512 gebracht."""
    img = Image.open(HERE / "canva_symbol.png").convert("RGB").resize((512, 512), Image.LANCZOS)
    img.save(out, "PNG", optimize=True)
    return out


def make_header(out):
    """Sammlerbogen: blaugrauer Karton mit feinen Linien, die App-Symbole als
    angesteckte Fundkarten mit handschriftlichem Etikett."""
    W, H = 4096, 2304
    img = Image.new("RGBA", (W, H), CARTON + (255,))
    draw = ImageDraw.Draw(img)
    for y in range(0, H, 96):
        draw.line((0, y, W, y), fill=CARTON_LINE, width=2)

    # Wortmarke links
    left = 300
    draw.text((left, 740), "Wunderkammer", font=garamond(236, 700), fill=INK_C)
    draw.text((left + 10, 1080), "Kleine Apps, sorgfältig gemacht.", font=caveat(128, 600), fill=INK_C)
    draw.text((left + 10, 1220), "Lesen · Lernen · Spielen · Entspannen", font=caveat(112, 500), fill=INK_SOFT)
    draw.text((left + 10, 1440), "offline · ohne Werbung · ohne Tracker", font=garamond(74, 500), fill=INK_C)

    # Fundkarten rechts, versetzt und leicht schraeg
    pos = [(2520, 660, -5), (3080, 600, 4), (3640, 700, -3),
           (2560, 1480, 3), (3120, 1540, -4), (3660, 1440, 5)]
    s = 340
    for (name, kind, path), (x, y, rot) in zip(APP_ICONS, pos):
        card = Image.new("RGBA", (s + 120, s + 290), (0, 0, 0, 0))
        cd = ImageDraw.Draw(card)
        cd.rectangle((0, 0, card.width - 1, card.height - 1), fill=CARD)
        icon, mask = rounded_icon(path, s, radius=s // 6)
        card.paste(icon, (60, 60), mask)
        cd.rounded_rectangle((60, 60, 60 + s - 1, 60 + s - 1), radius=s // 6, outline=CARTON, width=3)
        cd.text((card.width // 2, s + 150), name, font=caveat(80, 600), fill=INK_C, anchor="mm")
        cd.text((card.width // 2, s + 228), kind, font=garamond(46, 500), fill=INK_SOFT, anchor="mm")
        card = card.rotate(rot, resample=Image.BICUBIC, expand=True)
        cx, cy = x - card.width // 2, y - card.height // 2
        shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        shadow.paste((20, 30, 40, 95), (cx + 12, cy + 24), card.split()[3])
        img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(20)))
        img.alpha_composite(card, (cx, cy))
        draw = ImageDraw.Draw(img)
        py = cy + 30
        draw.ellipse((x - 26, py - 26, x + 26, py + 26), fill=PIN_DARK)
        draw.ellipse((x - 22, py - 24, x + 20, py + 18), fill=PIN)
        draw.ellipse((x - 12, py - 16, x - 2, py - 6), fill=(230, 140, 130))

    img.convert("RGB").save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    for name, _, path in APP_ICONS:
        if not path.exists():
            raise SystemExit(f"Symbol fehlt: {name} -> {path}")
    a = make_icon(HERE / "developer_icon_512.png")
    b = make_header(HERE / "developer_header_4096x2304.png")
    for p in (a, b):
        im = Image.open(p)
        print(p.name, im.size, im.mode, f"{p.stat().st_size/1024:.0f} kB")

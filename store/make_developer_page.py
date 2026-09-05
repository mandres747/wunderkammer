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

FONT_DIR = Path("C:/Windows/Fonts")
SERIF_BOLD = FONT_DIR / "georgiab.ttf"
SANS = FONT_DIR / "segoeui.ttf"
SANS_SEMI = FONT_DIR / "seguisb.ttf"

# Reihenfolge = Reihenfolge im Kabinett (links oben -> rechts unten)
APP_ICONS = [
    ("Wortgenau", APPS / "wortgenau/docs/store/icon_512.png"),
    ("Malfeld", APPS / "malfeld/store/assets/icon_512.png"),
    ("Lesepfadfinder", APPS / "eb-player/docs/store/icon_512.png"),
    ("Mancala Ukoo", APPS / "Spiele/mancala-ukoo/store/icon_512.png"),
    ("Nenne drei …", APPS / "Spiele/nenne-drei/playstore/icon-512.png"),
    ("DeepWave", APPS / "BinauralBeatsApp/playstore/ic_launcher-playstore.png"),
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
    S = 512
    img = vertical_gradient((S, S), INK_LIGHT, INK)
    draw = ImageDraw.Draw(img)
    cells = draw_cabinet(draw, (72, 72, S - 72, S - 72), cols=2, rows=2, frame=18, gap=14, fill_inner=INK_LIGHT)
    # Fundstuecke: Kreis, Raute, Quadrat, Sichel - ohne Text, damit es klein lesbar bleibt
    objects = ["circle", "diamond", "square", "ring"]
    for cell, kind in zip(cells, objects):
        cx = (cell[0] + cell[2]) // 2
        cy = (cell[1] + cell[3]) // 2
        r = (cell[2] - cell[0]) // 4
        if kind == "circle":
            draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=PARCHMENT)
        elif kind == "diamond":
            draw.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=BRASS)
        elif kind == "square":
            k = int(r * 0.85)
            draw.rounded_rectangle((cx - k, cy - k, cx + k, cy + k), radius=k // 4, fill=PARCHMENT)
        else:
            draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=BRASS, width=max(6, r // 4))
    img.save(out, "PNG", optimize=True)
    return out


def make_header(out):
    W, H = 4096, 2304
    img = vertical_gradient((W, H), INK_LIGHT, INK)
    draw = ImageDraw.Draw(img)

    # Kabinett rechts: 3 x 2 Faecher mit den App-Symbolen
    cab_w, cab_h = 1620, 1300
    cab_x1 = W - 260
    cab_x0 = cab_x1 - cab_w
    cab_y0 = (H - cab_h) // 2
    cab_y1 = cab_y0 + cab_h
    # weicher Schatten hinter dem Kabinett
    shadow = Image.new("RGB", (W, H), INK)
    ImageDraw.Draw(shadow).rounded_rectangle((cab_x0 + 30, cab_y0 + 50, cab_x1 + 30, cab_y1 + 50), radius=40, fill=(6, 12, 16))
    shadow = shadow.filter(ImageFilter.GaussianBlur(45))
    img = Image.blend(img, shadow, 0.35)
    draw = ImageDraw.Draw(img)
    cells = draw_cabinet(draw, (cab_x0, cab_y0, cab_x1, cab_y1), cols=3, rows=2, frame=44, gap=36, fill_inner=INK_LIGHT)

    label_font = font(SANS_SEMI, 46)
    for cell, (name, path) in zip(cells, APP_ICONS):
        cw = cell[2] - cell[0]
        ch = cell[3] - cell[1]
        size = int(min(cw, ch) * 0.58)
        icon, mask = rounded_icon(path, size, radius=size // 5)
        ix = cell[0] + (cw - size) // 2
        iy = cell[1] + int(ch * 0.10)
        # Schatten unter dem Symbol
        sh = Image.new("RGB", (size + 60, size + 60), INK_LIGHT)
        ImageDraw.Draw(sh).rounded_rectangle((30, 40, size + 30, size + 40), radius=size // 5, fill=(8, 14, 18))
        sh = sh.filter(ImageFilter.GaussianBlur(18))
        img.paste(sh, (ix - 30, iy - 30))
        img.paste(icon, (ix, iy), mask)
        draw = ImageDraw.Draw(img)
        tw = draw.textlength(name, font=label_font)
        draw.text((cell[0] + (cw - tw) / 2, iy + size + int(ch * 0.07)), name, font=label_font, fill=PARCHMENT)

    # Wortmarke links
    title_font = font(SERIF_BOLD, 215)
    sub_font = font(SANS, 84)
    tag_font = font(SANS_SEMI, 66)
    left = 260
    ty = cab_y0 + 150
    draw.text((left, ty), "Wunderkammer", font=title_font, fill=PARCHMENT)
    ty += 215 + 90
    draw.text((left, ty), "Kleine Apps, sorgfältig gemacht.", font=sub_font, fill=MUTED)
    ty += 84 + 24
    draw.text((left, ty), "Lesen · Lernen · Spielen · Entspannen", font=sub_font, fill=MUTED)

    # Messinglinie und drei Versprechen als Plaketten
    ty += 84 + 130
    draw.line((left, ty, left + 1150, ty), fill=BRASS, width=8)
    ty += 80
    x = left
    for tag in ("offline", "ohne Werbung", "ohne Tracker"):
        tw = draw.textlength(tag, font=tag_font)
        pad = 42
        box = (x, ty, x + tw + pad * 2, ty + 66 + pad)
        draw.rounded_rectangle(box, radius=24, outline=BRASS, width=6)
        draw.text((x + pad, ty + pad // 2 + 2), tag, font=tag_font, fill=PARCHMENT)
        x = box[2] + 44

    img.save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    for name, path in APP_ICONS:
        if not path.exists():
            raise SystemExit(f"Symbol fehlt: {name} -> {path}")
    a = make_icon(HERE / "developer_icon_512.png")
    b = make_header(HERE / "developer_header_4096x2304.png")
    for p in (a, b):
        im = Image.open(p)
        print(p.name, im.size, im.mode, f"{p.stat().st_size/1024:.0f} kB")

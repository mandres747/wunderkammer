"""Setzt die statischen Wellenpfade (Unterschied 6 Hz, Phase 0) in index.html und en/index.html ein.
Dieselbe Formel wie probier.js; ohne JavaScript bleibt dieses Bild stehen."""
import math, re
from pathlib import Path
W, M, A, F, N, diff = 600, 130, 58, 6, 160, 6
s, k = diff * 0.2, 2 * math.pi / W
def pfad(fn):
    return "".join(("L" if i else "M") + f"{i/N*W:.1f} {fn(i/N*W):.1f}" for i in range(N + 1))
h = lambda x: 1.15 * A * abs(math.cos(math.pi * s * x / W))
P = {"L": pfad(lambda x: M - A * math.sin(k * F * x)), "R": pfad(lambda x: M - A * math.sin(k * (F + s) * x)),
     "O": pfad(lambda x: M - h(x)), "U": pfad(lambda x: M + h(x))}
cls = {"L": "links", "R": "rechts", "O": "huelle-linie oben", "U": "huelle-linie unten"}
for f in (Path(__file__).parent / "index.html", Path(__file__).parent / "en/index.html"):
    t = f.read_text(encoding="utf-8")
    for key, c in cls.items():
        t = re.sub(rf'(<path class="{c}" d=")[^"]*(")', lambda m: m.group(1) + P[key] + m.group(2), t)
    f.write_text(t, encoding="utf-8")
print("ok")

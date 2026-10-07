// Probierwurf am Spieltisch: fünf Würfel, bis zu drei Würfe, Würfel antippen = halten.
// Gewertet wird nach den Grundregeln der App (core/engine, Stand 0.2.0) – ohne Talismane,
// ohne gravierte Seiten, mit Lehrmeister Werkstatt: (Grundwert + Augen der leuchtenden Würfel) × Kraft,
// dazu die Werkstoffe. Nichts wird gespeichert oder gesendet.
(function () {
  var tisch = document.querySelector("[data-tisch]");
  if (!tisch) return;
  var T = JSON.parse(tisch.getAttribute("data-texte"));
  // Name, Grundwert, Grundkraft, Werkstoffe – wie enum Kombination in Grundlagen.kt
  var K = {
    HOCH: [5, 1, []], PAAR: [10, 2, ["MESSING"]], ZWEI_PAARE: [20, 2, ["MESSING"]], DRILLING: [30, 3, ["EISEN"]],
    KLEINE_STRASSE: [30, 3, ["KRISTALL"]], FULL_HOUSE: [40, 4, ["EISEN", "MESSING"]],
    GROSSE_STRASSE: [40, 4, ["KRISTALL", "KRISTALL"]], VIERLING: [60, 7, ["EISEN", "MONDSTAUB"]], FUENFLING: [100, 10, ["MONDSTAUB"]]
  };
  var FARBE = { SPAN: "#B08968", MESSING: "#D9B650", EISEN: "#8FA3B3", KRISTALL: "#7FDCEB", MONDSTAUB: "#C9B8FF", TAU: "#5FA8F0", GLUT: "#FF7A4B" };

  function deutungen(w) {
    var res = [], werte = [];
    w.forEach(function (v) { if (werte.indexOf(v) < 0) werte.push(v); });
    werte.sort(function (a, b) { return a - b; });
    var gruppen = werte.map(function (v) { return [v, w.map(function (x, i) { return x === v ? i : -1; }).filter(function (i) { return i >= 0; })]; });
    gruppen = gruppen.map(function (g, k) { return [g, k]; }).sort(function (a, b) {
      return (b[0][1].length - a[0][1].length) || (b[0][0] - a[0][0]) || (a[1] - b[1]);
    }).map(function (x) { return x[0]; });
    var max = Math.max.apply(null, w);
    res.push(["HOCH", [w.indexOf(max)]]);
    var paare = gruppen.filter(function (g) { return g[1].length >= 2; });
    if (paare.length) res.push(["PAAR", paare[0][1].slice(0, 2)]);
    if (paare.length >= 2) res.push(["ZWEI_PAARE", paare[0][1].slice(0, 2).concat(paare[1][1].slice(0, 2))]);
    var g0 = gruppen[0][1];
    if (g0.length >= 3) res.push(["DRILLING", g0.slice(0, 3)]);
    if (g0.length >= 4) res.push(["VIERLING", g0.slice(0, 4)]);
    if (g0.length === 5) res.push(["FUENFLING", [0, 1, 2, 3, 4]]);
    if (gruppen.length === 2 && g0.length === 3) res.push(["FULL_HOUSE", [0, 1, 2, 3, 4]]);
    function hat(l) { return l.every(function (v) { return w.indexOf(v) >= 0; }); }
    var kl = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]];
    for (var k = 0; k < kl.length; k++) if (hat(kl[k])) { res.push(["KLEINE_STRASSE", kl[k].map(function (v) { return w.indexOf(v); })]); break; }
    if (hat([1, 2, 3, 4, 5]) || hat([2, 3, 4, 5, 6])) res.push(["GROSSE_STRASSE", [0, 1, 2, 3, 4]]);
    return res;
  }
  function bewerte(w) {
    var beste = null;
    deutungen(w).forEach(function (d) {
      var k = K[d[0]], wert = k[0];
      d[1].forEach(function (i) { wert += w[i]; });
      var punkte = Math.floor(wert * k[1] + 0.5);
      if (!beste || punkte > beste.punkte) beste = { kombi: d[0], idx: d[1], wert: wert, kraft: k[1], punkte: punkte };
    });
    var s = K[beste.kombi][2].slice();
    if (beste.idx.some(function (i) { return w[i] === 1; })) s.push("TAU");
    if (beste.idx.some(function (i) { return w[i] === 6; })) s.push("GLUT");
    if (w.length - beste.idx.length >= 2) s.push("SPAN");
    beste.stoffe = s;
    return beste;
  }

  var knoepfe = tisch.querySelectorAll(".wuerfel");
  var punkte = tisch.querySelectorAll(".zaehlt li");
  var wurfKnopf = tisch.querySelector("[data-wurf]");
  var neuKnopf = tisch.querySelector("[data-neu]");
  var stand = tisch.querySelector("[data-stand]");
  var kombi = tisch.querySelector(".kombi");
  var wert = tisch.querySelector("[data-wert]");
  var kraft = tisch.querySelector("[data-kraft]");
  var summe = tisch.querySelector("[data-punkte]");
  var stoffe = tisch.querySelector(".stoffe");
  var w = [], halten = [], rest = 0;
  var zahl = new Intl.NumberFormat(document.documentElement.lang);
  var ruhig = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function zeige(gerollt) {
    var b = bewerte(w);
    knoepfe.forEach(function (k, i) {
      k.setAttribute("data-augen", w[i]);
      k.setAttribute("aria-pressed", halten[i] ? "true" : "false");
      k.setAttribute("aria-label", T.wuerfel.replace("%1", i + 1).replace("%2", w[i]) + (b.idx.indexOf(i) >= 0 ? ", " + T.zaehlt : ""));
      k.disabled = rest === 0;
      if (gerollt && !halten[i] && !ruhig) { k.classList.remove("rollen"); void k.offsetWidth; k.classList.add("rollen"); }
    });
    punkte.forEach(function (p, i) { p.className = b.idx.indexOf(i) >= 0 ? "ja" : ""; });
    kombi.textContent = T.kombi[b.kombi];
    wert.textContent = zahl.format(b.wert);
    kraft.textContent = zahl.format(b.kraft);
    summe.textContent = zahl.format(b.punkte);
    stoffe.textContent = "";
    var v = document.createElement("li"); v.className = "vorspann-stoffe"; v.textContent = T.dazu; stoffe.appendChild(v);
    b.stoffe.forEach(function (s) {
      var li = document.createElement("li"); li.textContent = T.stoff[s]; li.style.setProperty("--farbe", FARBE[s]); stoffe.appendChild(li);
    });
    var anzahl = halten.filter(function (h) { return !h; }).length;
    wurfKnopf.disabled = rest === 0 || anzahl === 0;
    wurfKnopf.textContent = rest === 0 ? T.keinWurf : T.wurf.replace("%1", anzahl).replace("%2", rest);
    stand.textContent = rest === 0 ? T.fertig : T.stand.replace("%1", 3 - rest);
  }
  function wuerfle() {
    for (var i = 0; i < 5; i++) if (!halten[i]) w[i] = 1 + Math.floor(Math.random() * 6);
    rest--;
    zeige(true);
  }
  function neu() { w = [1, 1, 1, 1, 1]; halten = [false, false, false, false, false]; rest = 3; wuerfle(); }

  knoepfe.forEach(function (k, i) {
    k.addEventListener("click", function () { if (rest > 0) { halten[i] = !halten[i]; zeige(false); } });
  });
  wurfKnopf.addEventListener("click", wuerfle);
  neuKnopf.addEventListener("click", neu);
  tisch.querySelectorAll("[hidden]").forEach(function (e) { e.hidden = false; });
  neu();
})();

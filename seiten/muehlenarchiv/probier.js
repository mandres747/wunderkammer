// Probefund: Neunermühle in der Setzphase. Weiß setzt einen Stein – wo schließt er eine Mühle?
// Ob ein Punkt eine Mühle schließt, wird aus den 16 Linien des Bretts berechnet, nicht hinterlegt.
// Kein Speicher, kein Fremdcode.
(function () {
  var wurzel = document.querySelector("[data-fund]");
  if (!wurzel) return;
  var T = JSON.parse(wurzel.getAttribute("data-fund"));
  var feldflaeche = wurzel.querySelector(".muehle");
  var svg = feldflaeche.querySelector("svg");
  var status = wurzel.querySelector(".fund-status");
  var loesung = wurzel.querySelector("[data-loesung]");
  var neu = wurzel.querySelector("[data-neu]");
  var NS = "http://www.w3.org/2000/svg";
  // 24 Punkte auf einem 7×7-Raster (Spalte a–g, Reihe 7–1)
  var P = ["a7","d7","g7","b6","d6","f6","c5","d5","e5","a4","b4","c4","e4","f4","g4","c3","d3","e3","b2","d2","f2","a1","d1","g1"];
  function xy(n) { return [n.charCodeAt(0) - 97, 7 - Number(n[1])]; }
  var LINIEN = [
    ["a7","d7","g7"],["b6","d6","f6"],["c5","d5","e5"],["a4","b4","c4"],["e4","f4","g4"],["c3","d3","e3"],["b2","d2","f2"],["a1","d1","g1"],
    ["a7","a4","a1"],["b6","b4","b2"],["c5","c4","c3"],["d7","d6","d5"],["d3","d2","d1"],["e5","e4","e3"],["f6","f4","f2"],["g7","g4","g1"]
  ];
  var START = { a7: "w", a4: "w", d6: "w", f6: "w", c3: "w", e3: "w", a1: "s", d3: "s", g4: "s", e5: "s", b2: "s" };
  var stand, felder = {}, fertig;

  function pct(v) { return (5 + v * 15) + "%"; }

  // Matrizenzeichnung
  LINIEN.forEach(function (l) {
    var a = xy(l[0]), b = xy(l[2]);
    var ln = document.createElementNS(NS, "line");
    ln.setAttribute("x1", 5 + a[0] * 15); ln.setAttribute("y1", 5 + a[1] * 15);
    ln.setAttribute("x2", 5 + b[0] * 15); ln.setAttribute("y2", 5 + b[1] * 15);
    ln.setAttribute("class", "linien");
    svg.appendChild(ln);
  });
  P.forEach(function (n) {
    var p = xy(n), c = document.createElementNS(NS, "circle");
    c.setAttribute("cx", 5 + p[0] * 15); c.setAttribute("cy", 5 + p[1] * 15); c.setAttribute("r", 1.1);
    c.setAttribute("class", "punkt");
    svg.appendChild(c);
    var b = document.createElement("button");
    b.type = "button"; b.className = "feld"; b.dataset.p = n;
    b.style.left = pct(p[0]); b.style.top = pct(p[1]);
    feldflaeche.appendChild(b); felder[n] = b;
  });

  function schliesst(n) {
    return LINIEN.filter(function (l) {
      return l.indexOf(n) >= 0 && l.every(function (q) { return q === n || stand[q] === "w"; });
    });
  }
  function zeichnen() {
    P.forEach(function (n) {
      var f = felder[n], s = stand[n] || "";
      f.dataset.stein = s;
      f.disabled = fertig || s === "w" || s === "s";
      var wer = s === "w" ? T.weiss : s === "s" ? T.schwarz : s === "offen" ? T.offen : T.leer;
      f.setAttribute("aria-label", n + ": " + wer);
    });
  }
  function treffer(l) {
    var a = xy(l[0]), b = xy(l[2]);
    var ln = document.createElementNS(NS, "line");
    ln.setAttribute("x1", 5 + a[0] * 15); ln.setAttribute("y1", 5 + a[1] * 15);
    ln.setAttribute("x2", 5 + b[0] * 15); ln.setAttribute("y2", 5 + b[1] * 15);
    ln.setAttribute("class", "treffer"); ln.dataset.treffer = "1";
    svg.appendChild(ln);
  }
  function setzen(n) {
    if (fertig) return;
    P.forEach(function (q) { if (stand[q] === "falsch") delete stand[q]; });
    var m = schliesst(n);
    if (m.length) {
      stand[n] = "w"; fertig = true;
      m.forEach(treffer);
      status.textContent = T.richtig.replace("{p}", n);
    } else {
      stand[n] = "falsch";
      status.textContent = T.falsch.replace("{p}", n);
    }
    zeichnen();
  }
  function neustart() {
    stand = {}; for (var k in START) stand[k] = START[k];
    fertig = false;
    Array.prototype.slice.call(svg.querySelectorAll("[data-treffer]")).forEach(function (e) { e.remove(); });
    status.textContent = T.start;
    zeichnen();
  }
  feldflaeche.addEventListener("click", function (ev) {
    var b = ev.target.closest(".feld");
    if (b && !b.disabled) setzen(b.dataset.p);
  });
  loesung.addEventListener("click", function () {
    if (fertig) return;
    var ziel = P.filter(function (n) { return !stand[n] || stand[n] === "falsch"; }).filter(function (n) { return schliesst(n).length; })[0];
    if (!ziel) return;
    P.forEach(function (q) { if (stand[q] === "falsch") delete stand[q]; });
    stand[ziel] = "offen";
    status.textContent = T.hinweis.replace("{p}", ziel);
    zeichnen();
  });
  neu.addEventListener("click", neustart);
  neustart();
  wurzel.hidden = false;
})();

// Probierbrett: Kalah zu zweit an einem Gerät – dieselben Regeln wie in der App
// (2×6 Mulden, 4 Samen, gegen den Uhrzeigersinn, Extrazug im eigenen Speicher,
// Fang aus eigener leerer Mulde bei besetzter Gegenmulde, Ende wenn der Ziehende keine Samen hat).
// Kein Speicher, keine Wertung, kein Fremdcode.
(function () {
  var wurzel = document.querySelector("[data-kalah]");
  if (!wurzel) return;
  var T = JSON.parse(wurzel.getAttribute("data-kalah"));
  var brett = wurzel.querySelector(".brett");
  var status = wurzel.querySelector(".probe-status");
  var neu = wurzel.querySelector("[data-neu]");
  var punkteU = wurzel.querySelector("[data-punkte-unten]");
  var punkteO = wurzel.querySelector("[data-punkte-oben]");
  var ruhig = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  // 0–5 unten (links→rechts), 6 Speicher unten (rechts), 7–12 oben (rechts→links), 13 Speicher oben (links)
  var m, amZug, laeuft, felder = [];

  function el(tag, cls) { var e = document.createElement(tag); if (cls) e.className = cls; return e; }

  function aufbauen() {
    brett.textContent = "";
    var links = el("div", "loch speicher speicher--links"); links.style.gridColumn = "1"; links.style.gridRow = "1 / 3";
    var rechts = el("div", "loch speicher speicher--rechts"); rechts.style.gridColumn = "8"; rechts.style.gridRow = "1 / 3";
    felder[13] = links; felder[6] = rechts;
    for (var i = 0; i < 6; i++) {
      var unten = el("button", "loch"); unten.type = "button"; unten.style.gridColumn = String(i + 2); unten.style.gridRow = "2";
      unten.dataset.i = String(i); felder[i] = unten;
      var oben = el("button", "loch reihe-oben"); oben.type = "button"; oben.style.gridColumn = String(i + 2); oben.style.gridRow = "1";
      oben.dataset.i = String(12 - i); felder[12 - i] = oben;
    }
    for (var k = 0; k < 14; k++) brett.appendChild(felder[k]);
    brett.addEventListener("click", function (ev) {
      var b = ev.target.closest("button.loch");
      if (b && !b.disabled) ziehen(Number(b.dataset.i));
    });
  }

  function eigen(spieler, i) { return spieler === 0 ? i >= 0 && i <= 5 : i >= 7 && i <= 12; }
  function speicher(spieler) { return spieler === 0 ? 6 : 13; }
  function seiteLeer(spieler) { for (var i = 0; i < 6; i++) if (m[spieler === 0 ? i : 7 + i] > 0) return false; return true; }

  function zeichnen(zuletzt) {
    for (var i = 0; i < 14; i++) {
      var f = felder[i], n = m[i];
      f.textContent = "";
      var gross = i === 6 || i === 13;
      var s;
      if (gross) {
        // Speicher: Samengröße nach verfügbarer Fläche, damit sich nichts überdeckt
        var flaeche = (f.clientWidth * 0.7) * (f.clientHeight * 0.75);
        s = n ? Math.max(3, Math.min(9, Math.floor(Math.sqrt(flaeche / n)) - 2)) : 9;
      } else {
        s = n > 9 ? 5 : n > 4 ? 7 : 9;
      }
      f.style.setProperty("--s", s + "px");
      for (var k = 0; k < n; k++) f.appendChild(el("i"));
      var z = el("span", "zahl"); z.textContent = String(n); z.setAttribute("aria-hidden", "true"); f.appendChild(z);
      f.classList.toggle("zuletzt", i === zuletzt);
      if (!gross) {
        var spielbar = laeuft === false && eigen(amZug, i) && n > 0 && !ende();
        f.disabled = !spielbar;
        f.classList.toggle("spielbar", spielbar);
        var seite = i <= 5 ? T.unten : T.oben;
        var nr = i <= 5 ? i + 1 : 13 - i;
        f.setAttribute("aria-label", T.mulde.replace("{seite}", seite).replace("{nr}", nr).replace("{n}", n));
      } else {
        f.setAttribute("role", "img");
        f.setAttribute("aria-label", T.speicher.replace("{seite}", i === 6 ? T.unten : T.oben).replace("{n}", n));
      }
    }
    punkteU.textContent = m[6]; punkteO.textContent = m[13];
  }

  function ende() { return seiteLeer(amZug); }

  function ziehen(start) {
    laeuft = true;
    var hand = m[start]; m[start] = 0;
    var pos = start, wer = amZug, fremd = speicher(1 - wer);
    var schritte = [];
    while (hand > 0) {
      pos = (pos + 1) % 14;
      if (pos === fremd) continue;
      schritte.push(pos); hand--;
    }
    var i = 0;
    zeichnen(start);
    function schritt() {
      if (i < schritte.length) {
        m[schritte[i]]++; zeichnen(schritte[i]); i++;
        if (ruhig) schritt(); else setTimeout(schritt, 170);
        return;
      }
      abschliessen(wer, pos);
    }
    schritt();
  }

  function abschliessen(wer, letzte) {
    var meldung = "";
    if (letzte === speicher(wer)) {
      meldung = T.nochmal + " ";
    } else {
      var gegen = 12 - letzte;
      if (eigen(wer, letzte) && m[letzte] === 1 && m[gegen] > 0) {
        var beute = m[gegen] + 1;
        m[speicher(wer)] += beute; m[letzte] = 0; m[gegen] = 0;
        meldung = T.fang.replace("{n}", beute) + " ";
      }
      amZug = 1 - wer;
    }
    laeuft = false;
    if (seiteLeer(amZug)) {
      for (var k = 0; k < 6; k++) { m[6] += m[k]; m[k] = 0; m[13] += m[7 + k]; m[7 + k] = 0; }
      zeichnen(-1);
      if (meldung === T.nochmal + " ") meldung = "";
      var u = m[6], o = m[13];
      status.textContent = meldung + (u > o ? T.siegUnten : o > u ? T.siegOben : T.remis).replace("{u}", u).replace("{o}", o);
      neu.hidden = false;
      return;
    }
    zeichnen(letzte);
    status.textContent = meldung + (amZug === 0 ? T.zugUnten : T.zugOben);
  }

  function neuePartie() {
    m = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]; amZug = 0; laeuft = false;
    zeichnen(-1);
    status.textContent = T.start;
  }

  aufbauen();
  neu.addEventListener("click", neuePartie);
  neuePartie();
  neu.hidden = false;
  wurzel.hidden = false;
})();

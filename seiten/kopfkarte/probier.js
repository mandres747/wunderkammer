// Probierrunde auf der Wegkarte: fünf Begriffe aus der Wortbank der App an fünf Stationen
// des Beispielpalasts einprägen, dann den Weg abgehen und aus zehn Begriffen wählen
// (fünf echte, fünf Ablenker – wie in der App). Nichts wird gespeichert oder gesendet.
(function () {
  var wurzel = document.querySelector("[data-probe]");
  if (!wurzel) return;
  var T = JSON.parse(wurzel.getAttribute("data-texte"));
  var bank = JSON.parse(wurzel.getAttribute("data-woerter"));
  var orte = JSON.parse(wurzel.getAttribute("data-orte"));
  var feld = wurzel.querySelector(".probe");
  var stationen = document.querySelectorAll(".wegkarte .station");
  var N = orte.length;
  var stuecke = [], vorrat = [], antworten = [], i = 0, phase = "start";

  function mische(a) {
    a = a.slice();
    for (var k = a.length - 1; k > 0; k--) { var j = Math.floor(Math.random() * (k + 1)); var t = a[k]; a[k] = a[j]; a[j] = t; }
    return a;
  }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function knopf(text, rand, fn, aus) {
    var b = el("button", "knopf" + (rand ? " knopf--rand" : ""), text); b.type = "button";
    if (aus) b.disabled = true; b.addEventListener("click", fn); return b;
  }
  function markiere() {
    for (var k = 0; k < stationen.length; k++) {
      var s = stationen[k];
      s.classList.toggle("jetzt", phase !== "start" && phase !== "ende" && k === i);
      s.classList.toggle("fertig", (phase === "abruf" && antworten[k] != null && k !== i) || (phase === "merken" && k < i) || phase === "ende");
    }
  }
  function kopf(beschriftung) {
    feld.appendChild(el("span", "sc", beschriftung));
    feld.appendChild(el("p", "ort-titel", orte[i]));
  }
  function zeige() {
    feld.textContent = "";
    markiere();
    if (phase === "start") {
      feld.appendChild(el("p", null, T.start));
      var r = el("div", "knoepfe"); r.appendChild(knopf(T.los, false, beginne)); feld.appendChild(r);
      feld.appendChild(el("p", "probe-hinweis", T.hinweis));
    } else if (phase === "merken") {
      kopf(T.station.replace("%1", i + 1).replace("%2", N));
      feld.appendChild(el("div", "merkfeld", stuecke[i]));
      var r2 = el("div", "knoepfe");
      r2.appendChild(knopf(T.zurueck, true, function () { i--; zeige(); fokus(); }, i === 0));
      r2.appendChild(knopf(i < N - 1 ? T.weiter : T.zumAbruf, false, function () {
        if (i < N - 1) { i++; } else { phase = "abruf"; i = 0; }
        zeige(); fokus();
      }));
      feld.appendChild(r2);
    } else if (phase === "abruf") {
      kopf(T.abruf.replace("%1", i + 1).replace("%2", N));
      feld.appendChild(el("p", null, T.frage));
      var ul = el("ul", "auswahl");
      ul.setAttribute("aria-label", T.frage);
      vorrat.forEach(function (w) {
        var li = el("li"), b = el("button", null, w); b.type = "button";
        var hier = antworten[i] === w, woanders = antworten.indexOf(w) >= 0 && !hier;
        b.setAttribute("aria-pressed", hier ? "true" : "false");
        if (woanders) { b.classList.add("verbraucht"); b.setAttribute("aria-describedby", "probe-schon"); }
        b.addEventListener("click", function () {
          var alt = antworten.indexOf(w); if (alt >= 0) antworten[alt] = null;
          antworten[i] = w;
          if (i < N - 1) { i++; zeige(); fokus(); } else { zeige(); }
        });
        li.appendChild(b); ul.appendChild(li);
      });
      feld.appendChild(ul);
      var schon = el("span", null, T.schon); schon.id = "probe-schon"; schon.hidden = true; feld.appendChild(schon);
      var r3 = el("div", "knoepfe");
      r3.appendChild(knopf(T.zurueck, true, function () { i--; zeige(); fokus(); }, i === 0));
      if (i < N - 1) r3.appendChild(knopf(T.weiter, true, function () { i++; zeige(); fokus(); }));
      r3.appendChild(knopf(T.auswerten, false, function () { phase = "ende"; zeige(); fokus(); }));
      feld.appendChild(r3);
    } else {
      var richtig = 0;
      for (var k = 0; k < N; k++) if (antworten[k] === stuecke[k]) richtig++;
      feld.appendChild(el("span", "sc", T.ergebnis));
      feld.appendChild(el("p", "ergebnis-zahl", richtig + " / " + N));
      var liste = el("ul", "ergebnis-liste");
      for (var m = 0; m < N; m++) {
        var ok = antworten[m] === stuecke[m];
        var li2 = el("li", ok ? "ok" : "falsch");
        li2.appendChild(el("span", "zeichen", ok ? "✓" : "✗"));
        var t = el("span", null, (m + 1) + ". " + orte[m] + ": " + stuecke[m]);
        li2.appendChild(t);
        if (!ok) li2.appendChild(el("small", null, antworten[m] ? T.deine.replace("%1", antworten[m]) : T.keine));
        liste.appendChild(li2);
      }
      feld.appendChild(liste);
      feld.appendChild(el("p", "probe-hinweis", T.schluss));
      var r4 = el("div", "knoepfe"); r4.appendChild(knopf(T.nochmal, false, beginne)); feld.appendChild(r4);
    }
  }
  function fokus() { var h = feld.querySelector(".ort-titel, .ergebnis-zahl"); if (h) { h.tabIndex = -1; h.focus({ preventScroll: true }); } }
  function beginne() {
    var w = mische(bank);
    stuecke = w.slice(0, N);
    vorrat = mische(w.slice(0, 2 * N));
    antworten = []; for (var k = 0; k < N; k++) antworten.push(null);
    i = 0; phase = "merken"; zeige(); fokus();
  }
  zeige();
})();

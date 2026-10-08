// Punktefeld zerlegen wie in „Teile geschickt“ der App: a Reihen zu b Plättchen, eine Trennlinie
// teilt in zwei leichtere Malaufgaben. Kein „falsch“, nur zeigende Rückmeldung. Kein Speicher.
(function () {
  var b = document.querySelector("[data-feld]");
  if (!b) return;
  var liste = JSON.parse(b.getAttribute("data-feld"));
  var feld = b.querySelector("[data-punkte]");
  var regler = b.querySelector("[data-regler]");
  var eingabe = regler.querySelector("input");
  var reiheTxt = b.querySelector("[data-reihe]");
  var aufgabe = b.querySelector("[data-aufgabe]");
  var rechnung = b.querySelector("[data-rechnung]");
  var lob = b.querySelector("[data-lob]");
  var naechste = b.querySelector("[data-naechste]");
  var KERN = [1, 2, 5, 10];
  var i = 0, zeilen, spalten;

  function startLinie(a) { return a > 5 ? 5 : a > 2 ? 2 : 1; }
  function zeichne(oben) {
    var html = "";
    for (var r = 0; r < zeilen; r++) {
      if (r === oben) html += '<div class="linie"></div>';
      html += '<div class="reihe' + (r >= oben ? " reihe--unten" : "") + '">' + new Array(spalten + 1).join("<span></span>") + "</div>";
    }
    feld.innerHTML = html;
    feld.style.setProperty("--spalten", spalten);
    var unten = zeilen - oben;
    reiheTxt.textContent = oben;
    eingabe.setAttribute("aria-valuetext", "Oben " + oben + " Reihen, unten " + unten + " Reihen");
    rechnung.innerHTML = '<span class="rot">' + oben + " · " + spalten + '</span> + <span class="blau">' + unten + " · " + spalten +
      "</span> = " + oben * spalten + " + " + unten * spalten + ' = <span class="ergebnis">' + zeilen * spalten + "</span>";
    var k1 = KERN.indexOf(oben) >= 0, k2 = KERN.indexOf(unten) >= 0;
    lob.textContent = k1 && k2 ? "Beide Teile sind Kernaufgaben – sehr geschickt."
      : k1 ? oben + " · " + spalten + " ist eine Kernaufgabe – gut gewählt."
      : k2 ? unten + " · " + spalten + " ist eine Kernaufgabe – gut gewählt."
      : "Stimmt auch. Mit einer Kernaufgabe (·2, ·5) wird es noch leichter.";
  }
  function setze(n) {
    i = n % liste.length;
    zeilen = liste[i][0]; spalten = liste[i][1];
    aufgabe.textContent = zeilen + " · " + spalten;
    eingabe.max = zeilen - 1;
    eingabe.value = startLinie(zeilen);
    zeichne(+eingabe.value);
  }
  eingabe.addEventListener("input", function () { zeichne(+eingabe.value); });
  regler.addEventListener("click", function (e) {
    var k = e.target.closest("[data-schritt]");
    if (!k) return;
    var v = Math.min(+eingabe.max, Math.max(1, +eingabe.value + +k.getAttribute("data-schritt")));
    eingabe.value = v;
    zeichne(v);
  });
  naechste.addEventListener("click", function () { setze(i + 1); });
  regler.hidden = false;
  naechste.hidden = false;
  setze(0);
})();

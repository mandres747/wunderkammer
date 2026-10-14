// Probierrunde am Tisch: Der Computer hat angesagt, du sagst „Zeig her!“.
// Fünf feste Runden, vorab gegen die Wörterliste der App geprüft (_bauen.py). Kein Speicher, keine Wertung.
(function () {
  var tisch = document.querySelector("[data-runden]");
  if (!tisch) return;
  var runden = JSON.parse(tisch.getAttribute("data-runden"));
  var gebot = tisch.querySelector("[data-gebot]");
  var verdeckt = tisch.querySelectorAll("[data-verdeckt]");
  var offen = tisch.querySelector("[data-offen]");
  var legt = tisch.querySelector("[data-legt]");
  var wort = tisch.querySelector("[data-wort]");
  var stempel = tisch.querySelector("[data-stempel]");
  var ausgang = tisch.querySelector("[data-ausgang]");
  var zeig = tisch.querySelector("[data-zeig]");
  var naechste = tisch.querySelector("[data-naechste]");
  var i = 0;

  function steine(ziel, text) {
    ziel.textContent = "";
    for (var k = 0; k < text.length; k++) {
      var s = document.createElement("span");
      s.className = "stein";
      s.textContent = text[k];
      ziel.appendChild(s);
    }
  }

  function setze(n) {
    i = (n + runden.length) % runden.length;
    var r = runden[i];
    gebot.textContent = r.gebot;
    for (var k = 0; k < verdeckt.length; k++) {
      verdeckt[k].textContent = "?";
      verdeckt[k].className = "stein stein--zu";
    }
    steine(offen, r.offen);
    legt.textContent = "";
    wort.textContent = "";
    stempel.hidden = true;
    ausgang.textContent = "";
    zeig.hidden = false;
    naechste.hidden = true;
  }

  zeig.addEventListener("click", function () {
    var r = runden[i];
    for (var k = 0; k < verdeckt.length; k++) {
      verdeckt[k].textContent = r.verdeckt[k];
      verdeckt[k].className = "stein stein--auf";
    }
    var echt = r.ausgang === "echt";
    legt.textContent = echt ? "Computer legt:" : "Länger geht es nicht:";
    steine(wort, r.wort);
    stempel.textContent = echt ? "Echt" : "Geblufft";
    stempel.className = "stempel " + (echt ? "stempel--echt" : "stempel--bluff");
    stempel.hidden = false;
    ausgang.textContent = echt
      ? "Ein Wort mit " + r.gebot + " Buchstaben. Computer bekommt den Topf."
      : "Kein Wort mit " + r.gebot + " Buchstaben. Du bekommst den Topf.";
    zeig.hidden = true;
    naechste.hidden = false;
    naechste.focus();
  });
  naechste.addEventListener("click", function () { setze(i + 1); zeig.focus(); });
  setze(0);
})();

// Probierseite: die ersten Zeilen aus Kapitel 1. Zweimal nachlegen, dann brennt das Feuer hell.
// Texte stehen wörtlich im HTML (aus der App, geprüft von _bauen.py). Kein Speicher.
(function () {
  var blatt = document.querySelector("[data-stufen]");
  if (!blatt) return;
  var stufen = JSON.parse(blatt.getAttribute("data-stufen"));
  var knopf = blatt.querySelector("[data-nachlegen]");
  var holz = blatt.querySelector("[data-holz]");
  var glut = blatt.querySelector("[data-glut]");
  var punkt = blatt.querySelector("[data-punkt]");
  var tipp = blatt.querySelector("[data-tipp]");
  var sperre = blatt.querySelector("[data-sperre]");
  var schritt = 0;
  knopf.addEventListener("click", function () {
    if (schritt >= 2) return;
    schritt += 1;
    blatt.querySelectorAll('[data-schritt="' + schritt + '"]').forEach(function (z) {
      z.hidden = false;
      z.classList.add("neu");
    });
    holz.textContent = 3 - schritt;
    glut.textContent = stufen[schritt];
    punkt.setAttribute("data-stufe", schritt);
    tipp.hidden = true;
    if (schritt === 2) {
      knopf.disabled = true;
      sperre.hidden = false;
    }
  });
  knopf.hidden = false;
})();

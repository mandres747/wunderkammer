// Probier-Fährte: eine echte Gabelung aus „Emmi ermittelt 1“ (Abschnitt A006 und die beiden Fortsetzungen).
// Ohne Wertung, ohne Speicher. Ohne JavaScript bleibt der Ausschnitt mit der Frage stehen.
(function () {
  var f = document.querySelector("[data-faehrte]");
  if (!f) return;
  var wahl = f.querySelector("[data-wahl]");
  var zurueck = f.querySelector("[data-zurueck]");
  var ausblick = f.querySelector("[data-ausblick]");
  var texte = f.querySelectorAll("[data-text]");
  function zeige(weg) {
    f.setAttribute("data-weg", weg || "");
    for (var i = 0; i < texte.length; i++) texte[i].hidden = texte[i].getAttribute("data-text") !== weg;
    wahl.hidden = !!weg;
    zurueck.hidden = !weg;
    ausblick.hidden = !weg;
  }
  wahl.addEventListener("click", function (e) {
    var k = e.target.closest("[data-weg]");
    if (!k) return;
    var weg = k.getAttribute("data-weg");
    zeige(weg);
    f.querySelector('[data-text="' + weg + '"]').focus();
  });
  zurueck.addEventListener("click", function () {
    zeige("");
    wahl.querySelector("button").focus();
  });
  wahl.hidden = false;
})();

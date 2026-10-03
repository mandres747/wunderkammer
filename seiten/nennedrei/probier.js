// Probierrunde im Kartenstapel: echte Aufgaben aus der App, ohne Wertung, ohne Speicher.
(function () {
  var buehne = document.querySelector("[data-aufgaben]");
  if (!buehne) return;
  var liste = JSON.parse(buehne.getAttribute("data-aufgaben"));
  var text = buehne.querySelector(".aufgabe");
  var bsp = buehne.querySelector(".beispiele");
  var uhr = buehne.querySelector(".uhr span");
  var weiter = buehne.querySelector("[data-weiter]");
  var zeigen = buehne.querySelector("[data-zeigen]");
  var i = 0;
  function setze(n) {
    i = (n + liste.length) % liste.length;
    text.textContent = liste[i][0];
    bsp.textContent = "";
    zeigen.setAttribute("aria-expanded", "false");
    if (uhr) { uhr.style.animation = "none"; void uhr.offsetWidth; uhr.style.animation = ""; }
  }
  weiter.addEventListener("click", function () { setze(i + 1); });
  zeigen.addEventListener("click", function () {
    var offen = zeigen.getAttribute("aria-expanded") === "true";
    bsp.textContent = offen ? "" : zeigen.getAttribute("data-praefix") + " " + liste[i][1];
    zeigen.setAttribute("aria-expanded", offen ? "false" : "true");
  });
  buehne.hidden = false;
  weiter.hidden = false;
  zeigen.hidden = false;
})();

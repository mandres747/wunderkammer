// RSVP-Probe: derselbe Erkennungspunkt (Orp.kt) und dieselbe Zeitregel (Timing.kt) wie in der App,
// ohne Rampe und ohne Seltenheitszuschlag. Nichts wird geladen oder gespeichert.
(function () {
  var b = document.querySelector("[data-rsvp]");
  if (!b) return;
  var woerter = b.getAttribute("data-text").split(/\s+/);
  var vor = b.querySelector(".vor"), orp = b.querySelector(".wort .orp"), nach = b.querySelector(".nach");
  var start = b.querySelector("[data-start]"), neu = b.querySelector("[data-neu]");
  var zone = b.querySelector(".zone");
  var i = 0, uhr = null, wpm = 250;

  function orpIndex(t) {
    var lead = t.search(/[\p{L}\p{N}]/u);
    if (lead < 0) return 0;
    var core = t.slice(lead).match(/^[\p{L}\p{N}-]*/u)[0].length;
    return lead + (core <= 1 ? 0 : core <= 4 ? 1 : core <= 8 ? 2 : core <= 12 ? 3 : 4);
  }
  function dauer(t) {
    var len = t.replace(/[^\p{L}\p{N}]/gu, "").length;
    var f = len >= 13 ? 1.6 : len >= 9 ? 1.3 : 1;
    if (/^\d/.test(t)) f *= 1.5;
    var pause = /[.!?…]["»«“”]?$/.test(t) ? 400 : /[,;:–]$/.test(t) ? 200 : 0;
    return 60000 / wpm * f + pause;
  }
  function zeige(t) {
    var k = orpIndex(t);
    vor.textContent = t.slice(0, k); orp.textContent = t.charAt(k); nach.textContent = t.slice(k + 1);
  }
  function schritt() {
    if (i >= woerter.length) { halt(); i = 0; return; }
    var t = woerter[i++]; zeige(t);
    uhr = setTimeout(schritt, dauer(t));
  }
  function setzeKnopf(laeuft) {
    start.setAttribute("aria-pressed", laeuft ? "true" : "false");
    start.querySelector("span").textContent = start.getAttribute(laeuft ? "data-pause" : "data-los");
    start.querySelector(".spiel").style.display = laeuft ? "none" : "";
    start.querySelector(".halt").style.display = laeuft ? "" : "none";
  }
  function halt() { clearTimeout(uhr); uhr = null; setzeKnopf(false); }
  start.addEventListener("click", function () { if (uhr) halt(); else { setzeKnopf(true); schritt(); } });
  neu.addEventListener("click", function () { halt(); i = 0; zeige(woerter[0]); });
  b.querySelectorAll("input[name=tempo]").forEach(function (r) {
    r.addEventListener("change", function () {
      wpm = +r.value;
      var z = wpm <= 350 ? "gruen" : wpm <= 400 ? "gelb" : "rot";
      zone.setAttribute("data-zone", z);
      zone.textContent = zone.getAttribute("data-" + z);
    });
  });
  b.querySelector(".steuer").hidden = false;
})();

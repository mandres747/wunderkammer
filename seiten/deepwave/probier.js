// Schwebung zum Ansehen und Probehören: zwei Sinustöne, links 200 Hz, rechts 200 Hz + Unterschied.
// Nur Web Audio im Browser, nichts wird geladen oder gespeichert. Ton erst nach Tippen, leise, mit Ein-/Ausblenden.
(function () {
  var b = document.querySelector("[data-schwebung]");
  if (!b) return;
  var W = 600, M = 130, A = 58, F = 6, N = 240;
  var pL = b.querySelector(".links"), pR = b.querySelector(".rechts");
  var pO = b.querySelector(".oben"), pU = b.querySelector(".unten");
  var regler = b.querySelector("input"), aus = b.querySelector("output");
  var knopf = b.querySelector(".start"), status = b.querySelector("[data-status]");
  var still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var diff = +regler.value, phi = 0, letzte = 0;

  function pfad(fn) {
    var d = "";
    for (var i = 0; i <= N; i++) { var x = (i / N) * W; d += (i ? "L" : "M") + x.toFixed(1) + " " + fn(x).toFixed(1); }
    return d;
  }
  function zeichne() {
    var s = diff * 0.2, k = 2 * Math.PI / W;
    pL.setAttribute("d", pfad(function (x) { return M - A * Math.sin(k * F * x); }));
    pR.setAttribute("d", pfad(function (x) { return M - A * Math.sin(k * (F + s) * x - phi); }));
    var h = function (x) { return 1.15 * A * Math.abs(Math.cos(Math.PI * s * x / W - phi / 2)); };
    pO.setAttribute("d", pfad(function (x) { return M - h(x); }));
    pU.setAttribute("d", pfad(function (x) { return M + h(x); }));
  }
  function lauf(t) {
    if (letzte) phi = (phi + (t - letzte) / 1000 * diff * 0.3) % (4 * Math.PI);
    letzte = t; zeichne();
    if (!still && !document.hidden) requestAnimationFrame(lauf); else letzte = 0;
  }
  document.addEventListener("visibilitychange", function () { if (!document.hidden && !still) requestAnimationFrame(lauf); });

  var ctx = null, oL = null, oR = null, g = null, uhr = null;
  function setzeTon() {
    if (oR) oR.frequency.setTargetAtTime(200 + diff, ctx.currentTime, 0.05);
  }
  regler.addEventListener("input", function () {
    diff = +regler.value; aus.value = aus.textContent = diff + " Hz"; setzeTon(); if (still) zeichne();
  });
  function stopp() {
    if (!ctx || !g) return;
    clearTimeout(uhr);
    var t = ctx.currentTime, a = oL, c = oR;
    g.gain.cancelScheduledValues(t); g.gain.setValueAtTime(g.gain.value, t); g.gain.linearRampToValueAtTime(0, t + 0.6);
    setTimeout(function () { try { a.stop(); c.stop(); } catch (e) {} }, 700);
    oL = oR = g = null;
    knopf.setAttribute("aria-pressed", "false");
    knopf.setAttribute("aria-label", knopf.getAttribute("data-an"));
    status.textContent = status.getAttribute("data-aus");
  }
  knopf.addEventListener("click", function () {
    if (g) { stopp(); return; }
    var AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) { status.textContent = status.getAttribute("data-fehlt"); return; }
    ctx = ctx || new AC();
    if (ctx.state === "suspended") ctx.resume();
    var m = ctx.createChannelMerger(2);
    g = ctx.createGain(); g.gain.value = 0;
    oL = ctx.createOscillator(); oR = ctx.createOscillator();
    oL.frequency.value = 200; oR.frequency.value = 200 + diff;
    oL.connect(m, 0, 0); oR.connect(m, 0, 1); m.connect(g); g.connect(ctx.destination);
    oL.start(); oR.start();
    g.gain.linearRampToValueAtTime(0.12, ctx.currentTime + 1.2);
    knopf.setAttribute("aria-pressed", "true");
    knopf.setAttribute("aria-label", knopf.getAttribute("data-stopp"));
    status.textContent = status.getAttribute("data-an");
    uhr = setTimeout(stopp, 60000);
  });

  b.querySelector(".steuer").hidden = false;
  zeichne();
  if (!still) requestAnimationFrame(lauf);
})();

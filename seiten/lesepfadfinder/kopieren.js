// Pressebereich: Knöpfe „Text kopieren“. Ohne JavaScript bleiben die Knöpfe verborgen,
// der Text lässt sich dann wie gewohnt markieren. Kein Speicher, keine Anfragen.
(function () {
  var knoepfe = document.querySelectorAll("[data-kopieren]");
  for (var i = 0; i < knoepfe.length; i++) {
    (function (k) {
      var quelle = document.getElementById(k.getAttribute("data-kopieren"));
      var meldung = k.parentNode.querySelector(".kopier-meldung");
      if (!quelle) return;
      function melde(text) {
        if (!meldung) return;
        meldung.textContent = text;
        setTimeout(function () { meldung.textContent = ""; }, 4000);
      }
      function markiere() {
        var r = document.createRange();
        r.selectNodeContents(quelle);
        var s = window.getSelection();
        s.removeAllRanges();
        s.addRange(r);
      }
      k.hidden = false;
      k.addEventListener("click", function () {
        var absaetze = quelle.querySelectorAll("p");
        var teile = [];
        for (var j = 0; j < absaetze.length; j++) teile.push(absaetze[j].textContent.replace(/\s+/g, " ").trim());
        var text = teile.join("\n\n");
        if (navigator.clipboard && window.isSecureContext) {
          navigator.clipboard.writeText(text).then(function () { melde("Kopiert."); },
            function () { markiere(); melde("Der Text ist markiert und lässt sich jetzt kopieren."); });
        } else {
          markiere();
          melde("Der Text ist markiert und lässt sich jetzt kopieren.");
        }
      });
    })(knoepfe[i]);
  }
})();

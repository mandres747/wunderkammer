# App-Store-Start: Werbeseite umschalten

Bis Apple die iOS-Fassung freigibt, steht statt des App-Store-Badges ein Hinweis `<span class="bald">`
(Markierung `<!-- APPSTORE-LIVE ... -->`, je 2× in `index.html` und `en/index.html`).

Sobald die App im App Store sichtbar ist:

1. Je Markierung den Hinweis ersetzen durch
   - DE: `<a class="badge badge--apple" href="https://apps.apple.com/app/id6819707194"><img src="bilder/app-store-badge-de.svg" width="120" height="40" alt="Laden im App Store"></a>`
   - EN: `<a class="badge badge--apple" href="https://apps.apple.com/app/id6819707194"><img src="../bilder/app-store-badge-en.svg" width="120" height="40" alt="Download on the App Store"></a>`
   (im Schlussblock zusätzlich `loading="lazy"`).
2. Hinweistext und FAQ „Gibt es Nenne drei fürs iPhone?“ von „bald“ auf „Ja – im App Store (Link)“ zurückstellen.
3. `python _bauen.py`, dann `seiten/hochladen.sh nennedrei`.

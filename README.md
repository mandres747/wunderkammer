# Wunderkammer

Projektseite der Wunderkammer-Apps: enthaelt ausschliesslich die
Datenschutzerklaerungen und die Uebersichtsseite.

**Bewusst ohne Quelltext.** Die Apps liegen in eigenen Repositories; dieses hier
ist oeffentlich, weil GitHub Pages das verlangt. Nur deshalb steht hier kein
Code und kein Inhalt der Apps.

- Uebersicht: https://mandres747.github.io/wunderkammer/
- Nenne drei: https://mandres747.github.io/wunderkammer/nenne-drei/
- Mancala Ukoo: https://mandres747.github.io/wunderkammer/mancala-ukoo/

Kontakt: wunderkammer-apps@proton.me

## Eigener Server und App-Seiten (seit 03.10.2026)

Die Website laeuft auf dem eigenen Server (https://wunderkammer-apps.de, Doku `Apps/_server/SERVER.md`).
`seiten/<sub>/` enthaelt die Werbe- und Erklaerseiten der einzelnen Apps fuer die Unterdomains
`<sub>.wunderkammer-apps.de` (Muster und Checkliste: `seiten/MUSTER.md`, Upload: `seiten/hochladen.sh <sub>`).

Beim Upload der Hauptdomain bleiben `seiten`, `store`, `docs` und `README.md` draussen:

    tar --exclude=./seiten --exclude=./store --exclude=./docs --exclude=./README.md --exclude=./.git -czf - . \
      | ssh wunderkammer 'tar -xzf - -C /opt/wunderkammer/sites/www'

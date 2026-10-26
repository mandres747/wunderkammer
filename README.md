# Wunderkammer

Projektseite der Wunderkammer-Apps: enthaelt ausschliesslich die
Datenschutzerklaerungen und die Uebersichtsseite.

**Bewusst ohne Quelltext.** Die Apps liegen in eigenen Repositories; hier steht
kein Code und kein Inhalt der Apps.

Veroeffentlicht wird seit dem 03.10.2026 auf dem eigenen Server, nicht mehr
ueber GitHub Pages - der Inhalt geht per `tar | ssh` aus dem Arbeitsordner
dorthin (siehe unten). GitHub Pages lieferte bis zum 26.10.2026 unter
`mandres747.github.io/wunderkammer/` noch einen alten Stand aus und ist seitdem
abgeschaltet; das Repo musste nur dafuer oeffentlich sein.

- Uebersicht: https://wunderkammer-apps.de/
- Nenne drei: https://wunderkammer-apps.de/nenne-drei/
- Mancala Ukoo: https://wunderkammer-apps.de/mancala-ukoo/

Kontakt: kontakt@wunderkammer-apps.de

## Eigener Server und App-Seiten (seit 03.10.2026)

Die Website laeuft auf dem eigenen Server (https://wunderkammer-apps.de, Doku `Apps/_server/SERVER.md`).
`seiten/<sub>/` enthaelt die Werbe- und Erklaerseiten der einzelnen Apps fuer die Unterdomains
`<sub>.wunderkammer-apps.de` (Muster und Checkliste: `seiten/MUSTER.md`, Upload: `seiten/hochladen.sh <sub>`).

Beim Upload der Hauptdomain bleiben `seiten`, `store`, `docs` und `README.md` draussen:

    tar --exclude=./seiten --exclude=./store --exclude=./docs --exclude=./README.md --exclude=./.git -czf - . \
      | ssh wunderkammer 'tar -xzf - -C /opt/wunderkammer/sites/www'

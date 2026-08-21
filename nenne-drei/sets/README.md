# Set-Katalog für »Nenne drei …«

Die App liest `catalog.json` über GitHub Pages:

```
https://mandres747.github.io/wunderkammer/nenne-drei/sets/catalog.json
```

Kein Server, keine Kosten, versionierbar — und über Pages statt `raw.githubusercontent.com`,
weil Pages als Auslieferungsweg gedacht ist und dieselbe Adresse trägt wie die
Datenschutzseiten.

## Format

```json
{
  "schema": 1,
  "sets": [
    {
      "id": "advent-2026",
      "name": "Advent 2026",
      "version": 1,
      "url": "https://mandres747.github.io/wunderkammer/nenne-drei/sets/advent-2026.json",
      "description": "24 Aufgaben rund um Weihnachten und Winter.",
      "taskCount": 24,
      "language": "de"
    }
  ]
}
```

Pflicht sind `id`, `name`, `version` und `url`; `description`, `taskCount` und
`language` (Vorgabe `de`) sind freiwillig. Unbekannte Felder ignoriert die App,
das Schema darf also wachsen.

Ein leerer `sets`-Eintrag ist ein gültiger Zustand: Die App meldet dann »Der
Katalog ist leer« — eine ruhige Aussage, kein Fehler. Genau dafür existiert
diese Datei, auch solange noch nichts darin steht.

## Die eine Regel, die hier nicht verletzt werden darf

**In den Katalog gehören nur Aufgaben, die nicht zum ausgelieferten Bestand der
App zählen.** Die Vollversion verkauft die Tiefe der 25 Rubriken: 25 Aufgaben je
Rubrik sind gratis, der Rest liegt hinter der Kaufschranke. Ein Katalog-Set, das
gesperrte Aufgaben enthielte, würde diese Schranke aushebeln — und zwar
unbemerkt, weil importierte Sets im Code bewusst nie gesperrt werden
(`s.source != 'asset'` in der Kandidaten-Abfrage, damit selbst geschriebene
Aufgaben nicht hinter der eigenen Bezahlschranke landen).

Katalog-Sets sind also **Ergänzungen**: Saisonales, Anlässe, Themenspecials —
nichts, was schon in `content/` liegt.

## Neues Set einstellen

1. Set-Datei nach `nenne-drei/sets/<id>.json` legen (Format wie beim Editor-Export)
2. `tools/validate_sets.py` im App-Repo darüberlaufen lassen
3. Eintrag in `catalog.json` ergänzen, `version` bei jeder Änderung erhöhen
4. Committen und pushen — Pages veröffentlicht innerhalb einer Minute

Die App erkennt Inhaltsänderungen über einen SHA-256 des Rohinhalts, nicht über
`version`. Die Nummer ist für Menschen da; vergessen wird sie trotzdem gern.

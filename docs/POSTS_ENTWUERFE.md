# Wunderkammer – Post-Entwürfe (Bluesky)

Stand 17.11.2026. **Entwürfe, nichts Gesendetes.** Posten bleibt beim Nutzer
(`MONETARISIERUNG.md` §4.9/§11.4) – ich schlage Inhalt, Bild und Zeitpunkt vor, die
Freigabe und das Klicken gehören dir. Jeder Entwurf gehört zu einem Anlass aus
`anlaesse.json`; ist er gepostet, trägt die Sitzung dort `erledigt` nach, und der
Sitzungsstart hört auf zu erinnern.

Bluesky zählt **300 Zeichen** (der Link zählt mit). Die Zeichenzahl unter jedem
Entwurf ist gemessen, nicht geschätzt.

Ton nach `MARKETING.md` §3: ruhig, ehrlich, keine Übertreibung, keine künstliche
Kadenz. Kein Heilversprechen bei Mondraute (`almanach/CLAUDE.md`, Leitplanken) –
darum steht in jedem Entwurf „mit Quelle“ und nirgends eine Wirkung.

---

## Anlass `mondraute-start-bluesky` – Startpost Mondraute

Mondraute steht seit dem **2. November 2026** bei Google Play
(`de.mondraute.app`, Android, DE/AT/CH/LU). iOS liegt noch bei Apple, deshalb
nennt kein Entwurf das iPhone. Der Link trägt `utm_source=bluesky` – die
Werbeseite gibt das an das Play-Abzeichen weiter, also erscheint der Kanal in der
Play Console als eigene Quelle (`almanach/docs/MARKETING.md` §13; `bluesky` steht
in der Allowlist in `website/index.html`).

**Entwurf A – nüchtern (empfohlen)**

> Mondraute ist da: ein ruhiger Almanach für jeden Tag – Mondphase, was im Garten
> dran ist, ein Kraut aus alten Hausbüchern, ehrlich erzählt mit Quelle. Kein Abo,
> keine Werbung, offline. Für Android:
> https://mondraute.com/?utm_source=bluesky&utm_campaign=start

*258 Zeichen.* Empfohlen, weil der erste Satz sagt, was man bekommt, und keine
Zahl behauptet, die später nachgezählt werden müsste.

**Entwurf B – mit Bild der App und Zahlen**

> Jeden Morgen ein Siegel brechen, dann öffnet sich das Tagesblatt: Mond, Garten,
> ein Kraut mit Quelle. 56 Kräuter, 882 Einträge aus alten Hausbüchern. Mondraute
> ist seit dem 2. November bei Google Play. Einmalig, ohne Abo:
> https://mondraute.com/?utm_source=bluesky&utm_campaign=start

*282 Zeichen.* Die beiden Zahlen stehen genauso auf der Werbeseite und werden von
`almanach/werkzeug/zahlen_pruefen.py` gegen den Bestand geprüft – **vor dem Posten
einmal laufen lassen**, falls seither Inhalt dazugekommen ist.

**Bild:** `almanach/website/bilder/tagesblatt.webp` (das Tagesblatt, schon auf der
Werbeseite im Einsatz) – oder die sieben Pinterest-Pins in
`almanach/website/bilder/werbemittel/pinterest/`, die sind aber 1000 × 1500 und
damit hochkant für einen Feed. Der Bild-Anhang ist auf Bluesky der offene Punkt
seit dem 07.10.: das native Dateifenster reagierte nicht auf die Browsersteuerung
(`MARKETING.md` §4), deshalb hängst du das Bild selbst an. Ein eigenes Querformat
(1200 × 630) baue ich auf Zuruf in Canva.

**Alternativtext fürs Bild** (Bluesky verlangt ihn nicht, `MONETARISIERUNG.md`
§1.6 schon): „Das Tagesblatt der App: Mondscheibe mit Phase, darunter die
Gartenübersicht und vier Bildtafeln aus alten Kräuterbüchern.“

---

## Anlass `store-starts-nachholen-bluesky` – der Herbst in einem Post

Seit dem letzten Post (8.10.) sind sieben Store-Ereignisse vorbeigegangen, ohne
angekündigt zu werden (Belege in `anlaesse.json`). Zwei davon sind erst am
17.11.2026 aufgefallen, beim nachgeholten `play_scan.py` und einem öffentlichen
iTunes-Lookup: **Zunft der Sechs steht seit dem 5.11. im App Store**, DeepWave
seit heute. Sieben einzelne Nachposts wären die künstliche Kadenz, die §3
ausdrücklich nicht will – **einer**, der es offen als Nachtrag benennt, ist
ehrlicher.

**Entwurf C – ein Nachtrag, als Nachtrag kenntlich**

> Nachgetragen, weil hier zuletzt der Herbst dazwischenkam: Zunft der Sechs und
> Mancala Ukoo sind bei Google Play, Zunft und DeepWave inzwischen auch im App
> Store, Malfeld und Nenne drei ebenso. Alles ohne Abo, ohne Werbung, ohne
> Tracker. Übersicht: https://wunderkammer-apps.de

*276 Zeichen.* **Vor dem Posten prüfen**, ob Zunft der Sechs 1.1 auf iOS wirklich
beworben werden soll: in dieser Version ist die Werkstatt auf iOS laut
`PROJEKTE.md` eine Sackgasse, und 1.2 soll den Android-Stand nachziehen. Dann
lieber nur Android nennen oder auf 1.2 warten.

**Oder weglassen.** Ein drei bis vier Wochen alter Store-Start ist keine Neuigkeit
mehr; wenn dir der Nachtrag zu bemüht wirkt, ist „entfällt: zu alt, beim nächsten
Release mitnehmen“ in `anlaesse.json` die saubere Antwort – dann erinnert der Hook
nicht weiter. Beides ist richtig, nur das Liegenlassen ohne Entscheidung nicht.

---

## Was hier (noch) nicht steht

- **Pin 3 (Tageskarte)** braucht keinen Entwurf – Titel, Beschreibung, Link und
  Alternativtext stehen fertig in `almanach/docs/PINTEREST_MAPPE.md`. Dort fehlt
  nur das Terminieren im Pin-Builder, und zwar vor dem 2. Dezember.
- **Pinterest-Nachschub** (3–5 Pins für die Rauhnächte, Anlass
  `pinterest-nachschub-rauhnaechte`) ist Bildarbeit in Canva nach dem Rezept aus
  `almanach/docs/MARKETING.md` §13 – Kopie der leeren 1000 × 1500-Grundfläche,
  echtes Website-Bild einsetzen, Titel ersetzen, als PNG exportieren. Sag Bescheid,
  dann baue ich sie; die Werbemittel darf ich nach freigegebenem Kanalplan selbst
  erstellen (`MONETARISIERUNG.md` §4.10), nur hochladen und terminieren nicht.

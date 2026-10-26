# Portfolio-Erlöse Wunderkammer (Play) — Schätzung 2026-09-06

Sieben Apps im Play-Konto „Wunderkammer“, alle ohne Werbung und ohne Datenerhebung: fünf Gratis + Einmalkauf, eine Kauf-App, eine mit Abo. Netto beim Entwickler in Deutschland: Bruttopreis ÷ 1,19 (Umsatzsteuer, führt Google ab) × 0,85 (Play-Gebühr 15 % bis 1 Mio. $ Jahresumsatz) = **71,4 % vom Brutto**. Alle Installations- und Kaufquoten sind **Annahmen**, keine Messwerte: die Apps sind noch im Test, es gibt keine Verkaufsdaten. Die Spannen sind bewusst weit.

## 1. Preismodelle und Netto je Käufer

| App | Modell | Preis (DE brutto) | Netto je Käufer, 1. Jahr | Status | Quelle |
|---|---|---|---|---|---|
| Malfeld | Gratis + Plus (Abo 24,99 €/Jahr, 1. Jahr 19,99 €; 3,99 €/Monat; Einmalkauf 39,99 €) | 24,99 / 19,99 / 3,99 / 39,99 € | 18.85 € | Geschlossener Test läuft, Produktionsantrag nach 14 Tagen | `malfeld-app/docs/business/11_PREISMODELL.md` |
| DeepWave | Kauf-App (Play); FOSS-Variante gratis auf F-Droid | 3,99 € (Rahmen 2,99–5,99 €, in Play noch zu setzen) | 2.85 € | Geschlossener Test beendet, Produktionszugriff beantragt | `BinauralBeatsApp/playstore/RELEASE_CHECKLIST.md, Monetarisierungsstrategie` |
| Wortgenau | Gratis + Pro (Einmalkauf) | 4,99 € | 3.56 € | Testphase | `wortgenau/docs/04_RELEASE_UND_MONETARISIERUNG.md §5.4` |
| Nenne drei | Gratis + Vollversion (Einmalkauf) | 3,99 € | 2.85 € | Testphase | `Spiele/nenne-drei/docs/02_RELEASE_UND_MONETARISIERUNG.md §5` |
| Mancala Ukoo | Gratis (Kalah, Oware) + Einmalkauf für alle Varianten | 2,99 € | 2.14 € | Testphase | `Spiele/mancala-ukoo/docs (Preis vom Autor bestätigt)` |
| Lesepfadfinder | Erstes Buch gratis + Bände als Einmalkauf | 2,99 € je Band, 4,99 € Doppel-Bundle | 2.78 € | Testphase, ein Kaufband im Katalog | `eb-player/docs/01_APP_PLAN.md (Entscheidung 2026-08-18)` |
| Blindgitter | Gratis; freiwillige Unterstützung (konsumierbar), nichts gesperrt | ~2,99 € (Produkt „unterstuetzung“, Preis noch anzulegen) | 2.14 € | Testphase | `Spiele/blindgitter/docs/NAECHSTE_SCHRITTE.md, Nachtrag 2026-08-30` |

Malfeld-Netto ist ein Mix: 60 % Jahresabo zum Einführungspreis (14,28 €), 30 % Einmalkauf (28,56 €), 10 % Monatsabo über sechs Monate (17,10 €). Lesepfadfinder rechnet 1,3 Bände je Käufer (Bundle-Anteil). DeepWave ist eine Kauf-App: jede Installation ist ein Kauf.

## 2. Annahmen je Szenario

Installationen pro Monat (organisch, ohne bezahlte Werbung) und Kaufquote. Konservativ = unbekannter Entwickler, keine Sichtbarkeit. Basis = solide Store-Präsenz nach ein paar Monaten. Optimistisch = ein Sichtbarkeitsschub (Teacher Approved, Presse, Empfehlungen von Lehrkräften).

| App | Installationen/Monat K / B / O | Kaufquote K / B / O |
|---|---|---|
| Malfeld | 150 / 400 / 1500 | 2,5 % / 3,5 % / 4,5 % |
| DeepWave | 5 / 20 / 60 | Kauf-App / Kauf-App / Kauf-App |
| Wortgenau | 100 / 300 / 800 | 3,0 % / 4,0 % / 5,0 % |
| Nenne drei | 100 / 400 / 1500 | 2,0 % / 3,5 % / 5,0 % |
| Mancala Ukoo | 150 / 500 / 2000 | 2,0 % / 3,0 % / 4,0 % |
| Lesepfadfinder | 50 / 200 / 600 | 5,0 % / 8,0 % / 12,0 % |
| Blindgitter | 100 / 300 / 1000 | 0,5 % / 1,0 % / 1,5 % |

Orientierung für die Quoten: Freemium mit Einmalkauf liegt bei Nischen-Apps meist zwischen 2 und 5 % (eigene Herleitung in `nenne-drei/docs/02_…` mit 3,5 % bei 3,99 €). Kinder-Lern-Apps mit klarem Elternnutzen erreichen 3 bis 5 %. Freiwillige Unterstützung ohne Gegenleistung bleibt unter 2 %. Kauf-Apps ohne Marke verkaufen im deutschsprachigen Play Store nur einstellig bis niedrig zweistellig pro Monat.

## 3. Ergebnis: Netto-Erlös im ersten Jahr

| App | Konservativ | Basis | Optimistisch |
|---|---|---|---|
| Malfeld | 848 € (45 Käufe) | 3.167 € (168) | 15.269 € (810) |
| DeepWave | 171 € (60 Käufe) | 684 € (240) | 2.052 € (720) |
| Wortgenau | 128 € (36 Käufe) | 513 € (144) | 1.709 € (480) |
| Nenne drei | 68 € (24 Käufe) | 479 € (168) | 2.565 € (900) |
| Mancala Ukoo | 77 € (36 Käufe) | 385 € (180) | 2.054 € (960) |
| Lesepfadfinder | 83 € (30 Käufe) | 534 € (192) | 2.402 € (864) |
| Blindgitter | 13 € (6 Käufe) | 77 € (36) | 385 € (180) |
| **Portfolio** | **1.389 €** | **5.838 €** | **26.436 €** |
| Käufer gesamt | 237 | 1128 | 4914 |

Malfeld trägt 61 % / 54 % / 58 % des Portfolios. Der Grund ist nicht die Kaufquote, sondern der Preis: rund 19 € Netto je Käufer gegen 2 bis 4 € bei den Einmalkauf-Apps. Ab dem zweiten Jahr kommen Verlängerungen dazu: 24,99 € brutto sind 17,85 € netto je verlängertem Abo; bei 40 % Verlängerungsquote im Basis-Szenario etwa 720 € zusätzlich pro Jahr.

## 4. Was das bedeutet

- **Größenordnung:** Im Basis-Szenario etwa 5.838 € netto im ersten Jahr, rund 487 € im Monat über sieben Apps. Konservativ ein Taschengeld, optimistisch ein Nebenerwerb. Ein Haupterwerb wird daraus nur mit einem anderen Vertriebsweg (Schulen, Verlage, Bundles) oder mit vielfach höheren Installationszahlen.
- **Der Hebel ist Distribution, nicht Preis.** Verdoppelte Installationen verdoppeln den Erlös. Ein Euro mehr am Preis bringt bei sinkender Kaufquote fast nichts (Preistabelle in `nenne-drei/docs/02_…`: 2,99 / 3,99 / 4,99 € ergeben denselben Ertrag). Konkret: Teacher-Approved-Badge und Kinder-Tab für Malfeld und Lesepfadfinder, F-Droid-Listung für DeepWave (Sichtbarkeit, auch wenn dort kein Geld fließt), Lehrkräfte- und Elternkanäle.
- **Malfeld zuerst.** Jede Stunde, die Malfeld Installationen bringt, ist etwa zehnmal so viel wert wie dieselbe Stunde bei einer 2,99-€-App. Die sechs kleinen Apps sind Portfolio-Breite und Reputation, kein Einkommen.
- **Kosten sind vernachlässigbar:** Play-Konto (einmalig 25 $), Domains, TOMMI-Einreichung 299 € zzgl. USt., Testers Community 14 € je App. Kein Server, keine KI-Kosten. Der reale Einsatz ist Arbeitszeit.
- **Steuern:** Google ist in der EU Händler (Merchant of Record) und führt die Umsatzsteuer ab. Die Auszahlungen sind Betriebseinnahmen des Autors (Einkommensteuer, Gewerbe- und Trader-Status nach DSA sind zu klären).

## 5. Was die Schätzung schärfer machen würde

1. Die ersten 90 Tage Produktionsdaten von Malfeld und Nenne drei (Installationen, Kaufquote) statt Annahmen.
2. DeepWave-Preis in der Play Console festlegen (Rahmen 2,99–5,99 €; Empfehlung 3,99 €, weil eine Kauf-App keine Probierphase hat).
3. Blindgitter: das Unterstützungs-Produkt anlegen (2,99 €), sonst bleibt der Erlös null.
4. Lesepfadfinder: erst ab drei bis vier Kaufbänden trägt das Modell, jeder Band erhöht das Netto je Käufer.
5. Nach drei Monaten das Malfeld-Preisexperiment 24,99 gegen 34,99 € (Play Console → Preistests).

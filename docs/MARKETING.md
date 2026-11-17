# Wunderkammer – Marketing-Strategie des Studio-Accounts

Stand 07.10.2026. Nach `Apps/_grundgeruest/MONETARISIERUNG.md` §11 (Marketing-Strategie je
„App“ – hier: je Marke/Konto, da der Bluesky-Account für das ganze Studio steht, nicht für
eine einzelne App). Nutzer-Vorgabe 07.10. abends: „gehört zur Marketingplanung dazu, den
Account zu prüfen und zu bespielen“ – ein Konto braucht laufende Pflege, kein einmaliges Setup.

## 1. Konten
| Plattform | Handle | Zweck | Status |
|---|---|---|---|
| Bluesky | `@wunderkammer-apps.de` (eigene Domain verifiziert) | Cross-Promotion-Hub aller Apps, Lehrkräfte-/Spiele-/Ruhe-Communities | live seit 07.10., 1 Post |
| Instagram | – | ggf. später (Nutzer-Entscheidung 07.10. morgens) | nicht angelegt |

## 2. Prüfen (§11.4, geteilt wie die Werbeseiten-Beobachtung in §11.2)
- **Landezone (seit 17.11.2026):** Der Befund der Cloud-Routine landete bis dahin nur in einer
  Cloud-Sitzung – sieben lückenlose Läufe, die niemand sah. Jetzt läuft `werbecheck.py`
  zusätzlich wöchentlich lokal (geplante Aufgabe, Journal und Laufmarke in `D:\apps-data`), und
  der Sitzungsstart-Hook meldet offene Anlässe, einen ausgebliebenen Lauf und einen überfälligen
  `play_scan.py` (§11.2 der Monetarisierung, §3.1 unten).
- **Cloud, geheimnisfrei, wöchentlich** (Teil der Routine „Wunderkammer Werbeseiten- und
  Bluesky-Beobachtung“, https://claude.ai/code/routines/trig_01WwK1cA55GQhPGwf9gHwfE8): öffentliche Kennzahlen über
  `public.api.bsky.app` ohne Login – Follower-Zahl, Post-Zahl, als Trend. Kein Login nötig, also
  kein Geheimnis in der Cloud.
- **Lokal, auf Zuruf/bei Sitzungsarbeit:** Mitteilungen (Antworten, Erwähnungen, neue
  Follower mit Nachricht) – braucht die angemeldete Sitzung, deshalb nicht in der Cloud-Routine.
  Antworten so wie Rezensionen (§4.8): zeitnah, freundlich, ehrlich.
- Auffälligkeiten (ungewöhnlicher Kommentar, Beschwerde, Presseanfrage) werden gemeldet, nicht
  selbständig beantwortet.

## 3. Bespielen – Inhalte-Plan
**Keine künstliche Kadenz.** Anlässe sind echte Ereignisse, kein „heute ist Dienstag“-Posting:

| Anlass | Beispiel | Häufigkeit (geschätzt) |
|---|---|---|
| App-Start/Store-Freigabe | Samenkiste live, Nenne drei im App Store | selten, aber hoher Wert |
| Neue Version mit sichtbarer Änderung | neue Spielart, Gestaltungs-Update | je nach Projekt, unregelmäßig |
| Saison (§4.6) | Schuljahresbeginn (Samenkiste), Rauhnächte (Almanach) | 4–6 Wochen vor dem Fenster |
| Hinter den Kulissen (sparsam) | ein Gestaltungs-Entwurf, eine Canva-Skizze | gelegentlich, nie Pflichttermin |
| Antwort auf Rückmeldung | Dank für eine Rezension/einen Kommentar (mit Erlaubnis) | anlassbezogen |

- **Entwürfe wie Anschreiben (§4.9):** Ich schlage Text (und ggf. Bild) vor, nenne den Anlass
  und den Bezug zu KONZEPT/Werbeseite. **Posten selbst nur mit ausdrücklicher Freigabe** –
  ein Post ist öffentlich und praktisch nicht vollständig rücknehmbar (Caches, Screenshots),
  dieselbe Grenze wie bei den Anschreiben-Entwürfen.
- **Ton:** ruhig, ehrlich, keine Übertreibung (§6 der Monetarisierung), erster Post als Muster
  (07.10.: Vorstellung, Nutzenversprechen, Link, ohne Bild – Bild-Anhang scheiterte an der
  Browsersteuerung, kann beim nächsten Post nachgeholt werden, idealerweise vom Nutzer selbst
  hochgeladen).
- **Cross-Promotion:** jeder App-Start/jede größere Version ist ein natürlicher Anlass; umgekehrt
  verweist die Werbeseite/Entwicklerseite nicht zwingend auf den Account (kein Pflichtbanner),
  erst wenn er eine gewisse Aktivität zeigt.

### 3.1 Anlass-Register und Wächter (seit 17.11.2026)
„Keine künstliche Kadenz" war richtig – aber ohne Gedächtnis heißt es in der Praxis: kein Post.
Zwischen dem 08.10. und dem 17.11.2026 gingen fünf Store-Ereignisse und der Start von Mondraute
(02.11.) vorbei, ohne dass eine Zeile erschien; das Konto stand unverändert bei zwei Posts. Nicht
weil entschieden wurde, zu schweigen, sondern weil niemand den Anlass vor Augen hatte.

- **`anlaesse.json`** (dieser Ordner) hält jeden Anlass fest: App, Kanal, Art (Start, Version,
  Saison, Frist), was zu tun ist, ab wann er offen ist, eine Frist, die **Fundstelle** und den
  Entwurf. Ohne Fundstelle kein Anlass (`_grundgeruest/BEFUNDE.md`).
- **`_tools/werbecheck.py`** liest es: Teil F im Wochenlauf (montags, geplante Aufgabe) und
  `--hook` beim Sitzungsstart. Offene Anlässe stehen damit vor der Arbeit auf dem Tisch, nicht
  in einer Cloud-Sitzung, die niemand öffnet.
- **Erledigt oder abgewählt – aber entschieden.** Gepostet → `erledigt` mit Datum eintragen.
  Zu alt, unpassend, bewusst übersprungen → `"entfaellt: Grund"`. Beides beendet die Erinnerung;
  nur das Liegenlassen nicht.
- **Entwürfe:** `POSTS_ENTWUERFE.md` (gemessene Zeichenzahl, Bildvorschlag, Alternativtext).
  Posten bleibt beim Nutzer – der Wächter erinnert, er veröffentlicht nichts (§11.4).

## 4. Offen
- Erster Bild-Post (Banner oder Screenshot) – Datei-Upload im Bluesky-Composer hat sich der
  Browsersteuerung entzogen (natives Datei-Fenster reagierte nicht auf simulierte Klicks);
  beim nächsten Mal selbst anhängen oder erneut versuchen.
- Folgen anderer Accounts (Lehrkräfte-/Spiele-Communities) – bewusst noch nicht automatisch
  gemacht, Nutzer entscheidet, wem gefolgt wird.
- Instagram-Entscheidung weiterhin offen (siehe `PROJEKTE.md`).

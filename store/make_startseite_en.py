"""Erzeugt en/index.html aus der deutschen Startseite index.html (Ersetzungsliste).

So bleiben beide Fassungen im Aufbau gleich. Nach jeder Änderung an index.html neu laufen
lassen; fehlt ein Ausgangstext, meldet das Skript ihn und bricht ab.
Aufruf:  python store/make_startseite_en.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

R = [
    ('<html lang="de">', '<html lang="en">'),
    ('<title>Wunderkammer – kleine Apps, sorgfältig gemacht</title>', '<title>Wunderkammer – small apps, made with care</title>'),
    ('content="Apps für Android zum Lesen, Lernen, Spielen und Entspannen: Nenne drei, DeepWave, Lesepfadfinder, Mancala Ukoo und mehr. Ohne Werbung, ohne Konto, ohne Abo."',
     'content="Android apps for reading, learning, playing and unwinding: Nenne drei, DeepWave, Mancala Ukoo and more. No ads, no account, no subscription."'),
    ('<link rel="canonical" href="https://wunderkammer-apps.de/">', '<link rel="canonical" href="https://wunderkammer-apps.de/en/">'),
    ('content="de_DE"', 'content="en_US"'),
    ('<meta property="og:title" content="Wunderkammer – kleine Apps, sorgfältig gemacht">', '<meta property="og:title" content="Wunderkammer – small apps, made with care">'),
    ('content="Apps für Android zum Lesen, Lernen, Spielen und Entspannen. Ohne Werbung, ohne Konto, ohne Abo."',
     'content="Android apps for reading, learning, playing and unwinding. No ads, no account, no subscription."'),
    ('<meta property="og:url" content="https://wunderkammer-apps.de/">', '<meta property="og:url" content="https://wunderkammer-apps.de/en/">'),
    ('og-de.png', 'og-en.png'),
    ('content="Wortmarke Wunderkammer auf blaugrauem Karton, daneben vier angesteckte App-Symbole."',
     'content="The Wunderkammer wordmark on blue-grey card, next to four pinned app icons."'),
    ('Zum Inhalt springen', 'Skip to content'),
    ('href="/" aria-label="Wunderkammer – Startseite"', 'href="/en/" aria-label="Wunderkammer – home"'),
    ('aria-label="Seitenbereiche"', 'aria-label="Sections"'),
    ('href="#werkstatt">Bald</a>', 'href="#werkstatt">Coming soon</a>'),
    ('href="#versprechen">Versprechen</a>', 'href="#versprechen">Our promise</a>'),
    ('<a class="sprache" href="/en/" hreflang="en" lang="en">English</a>', '<a class="sprache" href="/" hreflang="de" lang="de">Deutsch</a>'),
    ('Kleine Apps, sorgfältig gemacht.</p>', 'Small apps, made with care.</p>'),
    ('Eine Sammlung von Android-Apps zum Lesen, Lernen, Spielen und Entspannen. Jede hat ihr eigenes Gesicht – und keine will dich mit Werbung, Abos oder Datensammeln festhalten.',
     'A collection of Android apps for reading, learning, playing and unwinding. Each one has a face of its own – and none of them tries to hold on to you with ads, subscriptions or data collection.'),
    ('aria-label="Was alle Apps gemeinsam haben"', 'aria-label="What all the apps have in common"'),
    ('<li>ohne Werbung</li>', '<li>no ads</li>'),
    ('<li>ohne Konto</li>', '<li>no account</li>'),
    ('<li>ohne Abo</li>', '<li>no subscription</li>'),
    ('<li>gratis ausprobieren</li>', '<li>free to try</li>'),
    ('>Die Sammlung ansehen<', '>See the collection<'),
    ('>Alle Apps bei Google Play<', '>All apps on Google Play<'),
    ('Jetzt bei Google Play</h2>', 'Available on Google Play</h2>'),
    ('vier Fundstücke, frisch angesteckt', 'four finds, freshly pinned'),
    ('google-play-de.png', 'google-play-en.png'),
    (' – jetzt bei Google Play"', ' – get it on Google Play"'),
    # Nenne drei
    ('nennedrei.wunderkammer-apps.de/"', 'nennedrei.wunderkammer-apps.de/en/"'),
    ('Spielen · Quiz &amp; Party', 'Play · Quiz &amp; party'),
    ('Eine Aufgabe, ein Timer, drei Antworten: das Quiz für allein, die Runde am Tisch und den Unterricht.',
     'One task, one timer, three answers: the quiz for playing solo, around the table or in the classroom.'),
    ('<li>2.002 Aufgaben, gratis spielbar</li>', '<li>Free to play</li>'),
    ('<li>Party-Runde im WLAN, jeder am eigenen Gerät</li>', '<li>Wi-Fi party: everyone on their own phone</li>'),
    ('>Mehr über Nenne drei<', '>More about Nenne drei<'),
    # DeepWave
    ('deepwave.wunderkammer-apps.de/"', 'deepwave.wunderkammer-apps.de/en/"'),
    ('screen-deepwave-', 'screen-deepwave-en-'),
    ('Entspannen · Klang', 'Unwind · Sound'),
    ('Binaurale Beats und isochrone Töne, direkt auf dem Handy erzeugt – zum Einschlafen, Konzentrieren und Entspannen.',
     'Binaural beats and isochronic tones generated right on your phone – for falling asleep, focusing and relaxing.'),
    ('<li>Mehr als 30 Klangprogramme</li>', '<li>More than 30 presets</li>'),
    ('<li>Läuft offline, ohne Konto</li>', '<li>Works offline, no account</li>'),
    ('>Mehr über DeepWave<', '>More about DeepWave<'),
    # Lesepfadfinder (nur Deutsch)
    ('Lesen · für Kinder von 7 bis 10', 'Read · ages 7 to 10 · German'),
    ('Lesebücher, in denen Kinder selbst entscheiden, wie die Geschichte weitergeht. Mit Vorlesen zum Mitlesen.',
     'Reading books in which children decide how the story goes on, with read-aloud to follow along. The books are in German.'),
    ('<li>Ein ganzes Buch gratis</li>', '<li>One whole book free</li>'),
    ('<li>Lesen ohne Internet</li>', '<li>No internet needed for reading</li>'),
    ('>Mehr über Lesepfadfinder<', '>More about Lesepfadfinder (German)<'),
    # Mancala
    ('mancala.wunderkammer-apps.de/"', 'mancala.wunderkammer-apps.de/en/"'),
    ('screen-mancala-', 'screen-mancala-en-'),
    ('Mancala ist keine Variante, sondern eine Familie: Kalah, Oware, Bao, Omweso und sieben weitere – mit belegten Regeln.',
     'Mancala is not one game but a family: Kalah, Oware, Bao, Omweso and seven more – with documented rules.'),
    ('<li>Kalah und Oware gratis</li>', '<li>Kalah and Oware free</li>'),
    ('<li>Gegen den Computer oder zu zweit</li>', '<li>Against the computer or with a friend</li>'),
    ('>Mehr über Mancala Ukoo<', '>More about Mancala Ukoo<'),
    ('Spielen · Brettspiel', 'Play · Board game'),
    # Werkstatt
    ('Bald in der Sammlung</h2>', 'Coming soon</h2>'),
    ('noch auf dem Werktisch', 'still on the workbench'),
    ('Diese sieben Apps sind fertig gebaut und gerade im Test. Auf ihren Seiten kannst du sie schon kennenlernen – sobald sie bei Google Play stehen, findest du dort den Link.',
     'These seven apps are built and being tested right now. You can get to know them on their pages – once they are on Google Play, you will find the link there.'),
    ('wortgenau.wunderkammer-apps.de/"', 'wortgenau.wunderkammer-apps.de/en/"'),
    ('<span class="fach">Lesen</span>', '<span class="fach">Read</span>'),
    ('Wort für Wort lesen, an einem festen Punkt, ohne Augensprünge.', 'Read word by word at one fixed point, without eye jumps.'),
    ('<span class="fach">Lernen · Grundschule</span>', '<span class="fach">Learn · Primary · German</span>'),
    ('Das Einmaleins verstehen statt auswendig lernen: am Punktefeld zerlegen, tauschen, umkehren.',
     'Understand times tables instead of memorising them: split, swap and reverse on a dot grid.'),
    ('kopfkarte.wunderkammer-apps.de/"', 'kopfkarte.wunderkammer-apps.de/en/"'),
    ('Lernen · Gedächtnis', 'Learn · Memory'),
    ('Die Loci-Methode zum Üben: Bau deinen eigenen Gedächtnispalast.', 'The method of loci, ready to practise: build your own memory palace.'),
    ('zunft.wunderkammer-apps.de/"', 'zunft.wunderkammer-apps.de/en/"'),
    ('<h3>Zunft der Sechs</h3>', '<h3>Guild of Six</h3>'),
    ('Spielen · Würfel', 'Play · Dice'),
    ('Würfle, fertige Talismane und geh auf die Walz – ein Würfelspiel mit Werkstatt und Geschichte.',
     'Roll dice, craft charms and set out on the road – a dice game with a workshop and a story.'),
    ('muehlenarchiv.wunderkammer-apps.de/"', 'muehlenarchiv.wunderkammer-apps.de/en/"'),
    ('Die ganze Mühle-Familie: sieben Spielarten, Gegner mit Charakter und ein Archiv offener Partien.',
     'The whole nine men’s morris family: seven variants, opponents with character and an archive of unfinished games.'),
    ('Spielen · Wörter &amp; Bluff', 'Play · Words &amp; bluff · German'),
    ('Sag an, wie lang dein Wort ist – oder bluffe. Gegen den Computer, zu zweit oder im WLAN.',
     'Announce how long your word is – or bluff. A German word game against the computer, with a friend or over Wi-Fi.'),
    ('kerbe.wunderkammer-apps.de/"', 'kerbe.wunderkammer-apps.de/en/"'),
    ('<h3>Die neunte Kerbe</h3>', '<h3>The Ninth Notch</h3>'),
    ('Spielen · Textspiel', 'Play · Text game'),
    ('Trag eine alte Glut in den Wald und finde heraus, was die Kerben zählen. Ruhig, in sechs Kapiteln.',
     'Carry an ancient ember into the forest and find out what the notches count. Quiet, in six chapters.'),
    ('>erscheint bald<', '>coming soon<'),
    ('<span class="pfeil">Ansehen</span>', '<span class="pfeil">Take a look</span>'),
    # Versprechen
    ('Was alle gemeinsam haben</h2>', 'What they all have in common</h2>'),
    ('das Kleingedruckte, groß geschrieben', 'the small print, written large'),
    ('<h3>Keine Werbung</h3><p>Kein Banner, kein Video, keine Pop-ups. Du siehst nur die App.</p>',
     '<h3>No ads</h3><p>No banners, no videos, no pop-ups. All you see is the app.</p>'),
    ('<h3>Deine Daten bleiben bei dir</h3><p>Kein Konto, keine Tracker. Was du spielst, liest oder lernst, bleibt auf deinem Gerät.</p>',
     '<h3>Your data stays with you</h3><p>No account, no trackers. What you play, read or learn stays on your device.</p>'),
    ('<h3>Gratis anfangen, einmal kaufen</h3><p>Jede App lässt sich kostenlos ausprobieren. Was mehr kostet, kaufst du einmal – kein Abo.</p>',
     '<h3>Start free, pay once</h3><p>Every app can be tried for free. Anything extra is a one-time purchase – no subscription.</p>'),
    ('<h3>Ohne Internet</h3><p>Die Apps laufen offline. Nur ein Kauf braucht kurz eine Verbindung.</p>',
     '<h3>No internet needed</h3><p>The apps work offline. Only a purchase needs a connection for a moment.</p>'),
    ('<h3>Jede mit eigenem Gesicht</h3><p>Eigene Farben, eigene Schrift, eigenes Motiv – keine App sieht aus wie die andere.</p>',
     '<h3>Each with its own face</h3><p>Its own colours, its own typeface, its own motif – no two apps look alike.</p>'),
    ('<h3>Sorgfältig geprüft</h3><p>Spielregeln mit Quellen, Lerninhalte nach Lehrplan, jeder Text lektoriert.</p>',
     '<h3>Carefully checked</h3><p>Game rules with sources, learning content based on the curriculum, every text proofread.</p>'),
    # Schluss
    ('Neugierig geworden?', 'Curious?'),
    ('Alle Wunderkammer-Apps findest du gesammelt bei Google Play. Fragen, Wünsche oder einen Fehler gefunden? Schreib uns.',
     'You will find all Wunderkammer apps together on Google Play. Questions, wishes, or found a bug? Write to us.'),
    ('>Zu Google Play<', '>Go to Google Play<'),
    # Fuß
    ('<p>Kleine Apps für Android, sorgfältig gemacht.</p>', '<p>Small apps for Android, made with care.</p>'),
    ('>Impressum und Datenschutz dieser Website<', '>Legal notice and website privacy (German)<'),
    ('Datenschutzerklärungen der Apps</h2>', 'App privacy policies (German)</h2>'),
    ('>Die neunte Kerbe</a></li>', '>The Ninth Notch</a></li>'),
    ('>Zunft der Sechs</a></li>', '>Guild of Six</a></li>'),
    ('Diese Seite setzt keine Cookies, lädt nichts von fremden Servern und zählt keine Besuche.',
     'This site sets no cookies, loads nothing from third-party servers and does not count visits.'),
    ('Google Play und das Google Play-Logo sind Marken von Google LLC.', 'Google Play and the Google Play logo are trademarks of Google LLC.'),
]

s = (ROOT / "index.html").read_text(encoding="utf-8")
fehlt = [a for a, _ in R if a not in s]
if fehlt:
    sys.exit("Ausgangstext fehlt:\n" + "\n".join(f[:90] for f in fehlt))
for a, b in R:
    s = s.replace(a, b)
# Nenne drei: Telefon-Screenshots gibt es nur deutsch -> auf Englisch ohne Bild
s, n = re.subn(r'\n        <a class="bild" href="https://nennedrei[^\n]*', '', s)
assert n == 1
s = s.replace('<article class="karte" style="--app: #FF3D7F">', '<article class="karte ohne-bild" style="--app: #FF3D7F">')
(ROOT / "en").mkdir(exist_ok=True)
(ROOT / "en/index.html").write_text(s, encoding="utf-8")
rest = [z for z in re.findall(r">([^<>]*[äöüßÄÖÜ][^<>]*)<", s)]
print("en/index.html geschrieben. Deutsche Reste:", rest)

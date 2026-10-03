#!/usr/bin/env bash
# Laedt eine App-Seite hoch: seiten/<sub>/  ->  wunderkammer:/opt/wunderkammer/sites/apps/<sub>/
# Aufruf (Git Bash):  seiten/hochladen.sh <sub> [--sauber]
#   --sauber  leert den Zielordner vorher (entfernt verwaiste Dateien; der Ordner selbst bleibt,
#             damit ein Bind-Mount im Caddy-Container nicht bricht).
# Nicht hochgeladen werden Dateien/Ordner, die mit "_" beginnen (_bauen.py, _quelle/).
# Caddy (Unterdomain <sub>.wunderkammer-apps.de) richtet die Server-Sitzung ein, nicht dieses Skript.
set -euo pipefail
sub="${1:?Aufruf: seiten/hochladen.sh <sub> [--sauber]}"
case "$sub" in *[!a-z0-9-]*|"") echo "Ungueltiger Name: $sub (nur a-z, 0-9, -)"; exit 1;; esac
hier="$(cd "$(dirname "$0")" && pwd)"
quelle="$hier/$sub"
[ -f "$quelle/index.html" ] || { echo "Keine Seite gefunden: $quelle/index.html"; exit 1; }
ziel="/opt/wunderkammer/sites/apps/$sub"

ssh wunderkammer "test -w /opt/wunderkammer/sites/apps || { echo 'Einmalig: sudo mkdir -p /opt/wunderkammer/sites/apps && sudo chown -R wk:wk /opt/wunderkammer/sites/apps'; exit 1; }; mkdir -p '$ziel'"
if [ "${2:-}" = "--sauber" ]; then
  ssh wunderkammer "find '$ziel' -mindepth 1 -delete"
fi
tar -C "$quelle" --exclude='./_*' --mode='u+rwX,go+rX,go-w' -czf - . \
  | ssh wunderkammer "tar --no-same-owner -xzf - -C '$ziel' && find '$ziel' -type f | wc -l"
echo "Hochgeladen nach $ziel  ->  https://$sub.wunderkammer-apps.de/"

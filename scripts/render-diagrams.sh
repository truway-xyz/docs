#!/usr/bin/env bash
# Renders every diagrams/<lang>/*.mmd into <lang>/.gitbook/assets/<name>.svg with Truway's palette.
# The .mmd files are the source; the SVGs are what the pages show. Never edit an SVG by hand.
#
# Usage: scripts/render-diagrams.sh
# Needs Node and a Chrome or Chromium. Set PUPPETEER_EXECUTABLE_PATH if Chrome is elsewhere.
set -euo pipefail

MMDC="${MMDC:-npx -y @mermaid-js/mermaid-cli@11.4.2}"
CHROME="${PUPPETEER_EXECUTABLE_PATH:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
PUP="$(mktemp)"
printf '{ "executablePath": "%s", "args": ["--no-sandbox"] }' "$CHROME" > "$PUP"

for lang in ${LANGS:-es en}; do
  mkdir -p "$lang/.gitbook/assets"
  for src in diagrams/$lang/*.mmd; do
    name="$(basename "$src" .mmd)"
    $MMDC -q -p "$PUP" -c diagrams/mermaid.json -b '#FFFFFF' -w 1200 \
      -i "$src" -o "$lang/.gitbook/assets/$name.svg"
    echo "rendered $lang/.gitbook/assets/$name.svg"
  done
done
rm -f "$PUP"

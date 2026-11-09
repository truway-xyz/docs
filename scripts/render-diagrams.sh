#!/usr/bin/env bash
# Exports every diagrams/drawio/<lang>/*.drawio to <lang>/.gitbook/assets/<name>.png (2x, white background).
# The .drawio files are the source: edit them in draw.io, or change scripts/drawio_build.py and run it.
# PNG on purpose: GitBook drops the text of SVGs that use HTML labels.
#
# Usage: scripts/render-diagrams.sh          (needs draw.io desktop: brew install --cask drawio)
set -euo pipefail
DRAWIO="${DRAWIO:-/Applications/draw.io.app/Contents/MacOS/draw.io}"
for lang in es en; do
  mkdir -p "$lang/.gitbook/assets"
  for src in diagrams/drawio/$lang/*.drawio; do
    name="$(basename "$src" .drawio)"
    "$DRAWIO" -x -f png -s 2 -b 24 -o "$lang/.gitbook/assets/$name.png" "$src" >/dev/null 2>&1
    echo "exported $lang/.gitbook/assets/$name.png"
  done
done

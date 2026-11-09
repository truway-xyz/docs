#!/usr/bin/env bash
# Writes the deployments table from soroban-contracts/deployments/<network>.json into the
# Deployments pages, between the GENERATED markers. Contract IDs are never typed by hand.
#
# Usage: scripts/deployments-table.sh [path-to-soroban-contracts]   (default: ../soroban-contracts)
set -euo pipefail

SRC_REPO="${1:-../soroban-contracts}"
COMMIT="$(git -C "$SRC_REPO" rev-parse --short HEAD)"
TABLE="$(mktemp)"

{
  for net in testnet mainnet; do
    f="$SRC_REPO/deployments/$net.json"
    [ -f "$f" ] || continue
    explorer="https://stellar.expert/explorer/$( [ "$net" = mainnet ] && echo public || echo testnet )"
    rows="$(jq -r --arg ex "$explorer" '
      .contracts | to_entries[] | select(.value.contract_id != null) |
      "| `\(.key)` | \(.value.version // "") | [`\(.value.contract_id[0:8])…\(.value.contract_id[-4:])`](\($ex)/contract/\(.value.contract_id)) | `\(.value.wasm_hash[0:12])…` | `\(.value.source_commit)` | \(.value.deployed_at) | \(.value.build_verified // false) |"
    ' "$f")"
    echo "**$net**"
    echo
    if [ -z "$rows" ]; then
      echo "No active instances."
    else
      echo "| Contract | Version | Contract ID | WASM hash | Commit | Deployed | Build verified |"
      echo "|---|---|---|---|---|---|---|"
      echo "$rows"
    fi
    echo
  done
  echo "_Generated from \`deployments/\` at soroban-contracts commit \`$COMMIT\`._"
} > "$TABLE"

for page in en/architecture/deployments.md es/arquitectura/despliegues.md; do
  [ -f "$page" ] || { echo "skip $page (missing)"; continue; }
  awk -v table="$TABLE" '
    /<!-- GENERATED:deployments:start -->/ { print; while ((getline line < table) > 0) print line; skip=1; next }
    /<!-- GENERATED:deployments:end -->/ { skip=0 }
    !skip { print }
  ' "$page" > "$page.tmp" && mv "$page.tmp" "$page"
  echo "updated $page"
done
rm -f "$TABLE"

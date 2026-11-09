# Deployments

The source of truth for contract instances is
[`deployments/`](https://github.com/truway-xyz/soroban-contracts/tree/main/deployments) in
`soroban-contracts`. The table below is generated from it by `scripts/deployments-table.sh`; it
is never typed by hand.

<!-- GENERATED:deployments:start -->
**testnet**

| Contract | Version | Contract ID | WASM hash | Commit | Deployed | Build verified |
|---|---|---|---|---|---|---|
| `budget-treasury` | 0.4.0 | [`CCDKD5G2…WWZN`](https://stellar.expert/explorer/testnet/contract/CCDKD5G2OPQUCAWODXWR7JPZJWENNZMKQU5E3J6HSPIUY5ZFWC3QWWZN) | `183dd156444f…` | `6a5acb6` | 2026-11-07 | false |

**mainnet**

No active instances.

_Generated from `deployments/` at soroban-contracts commit `a759b69`._
<!-- GENERATED:deployments:end -->

## Organisation treasuries

Each organisation gets its own `budget-treasury` instance, deployed by the platform from a
single-use account that is not a member. The manifest lists reference instances; an organisation's
contract ID appears on its public programme page. To check that any treasury runs the published
code, compare its WASM hash with the table:

```bash
stellar contract info meta --contract-id <CONTRACT_ID> --network testnet
stellar contract fetch --id <CONTRACT_ID> --network testnet --out-file t.wasm && shasum -a 256 t.wasm
```

## Verified builds

On a version tag, the [release workflow](https://github.com/truway-xyz/soroban-contracts/blob/main/.github/workflows/release.yml)
builds `budget-treasury` on GitHub, attests the WASM and attaches it to the release. Explorers such
as Stellar Lab and Stellar Expert read that attestation and show the commit a deployed WASM was
built from. The source verification specification is still a draft in the Stellar ecosystem.

Only the WASM attached to a release verifies; a local build has a different hash.

## Retired instances

Instances under `retired` in the manifest, and the July 2026 instances of the legacy contracts,
must not be used. The July instances accept writes from any account.

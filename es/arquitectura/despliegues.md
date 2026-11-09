# Despliegues

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Deployments](https://github.com/truway-xyz/docs/blob/main/en/architecture/deployments.md).

La fuente de verdad de las instancias es [`deployments/`](https://github.com/truway-xyz/soroban-contracts/tree/main/deployments) en `soroban-contracts`. La tabla se genera con `scripts/deployments-table.sh`; nunca se escribe a mano.

<!-- GENERATED:deployments:start -->
**testnet**

| Contract | Version | Contract ID | WASM hash | Commit | Deployed | Build verified |
|---|---|---|---|---|---|---|
| `budget-treasury` | 0.4.0 | [`CCDKD5G2…WWZN`](https://stellar.expert/explorer/testnet/contract/CCDKD5G2OPQUCAWODXWR7JPZJWENNZMKQU5E3J6HSPIUY5ZFWC3QWWZN) | `183dd156444f…` | `6a5acb6` | 2026-11-07 | false |

**mainnet**

No active instances.

_Generated from `deployments/` at soroban-contracts commit `a759b69`._
<!-- GENERATED:deployments:end -->

Cada organización tiene su propia instancia, desplegada por una cuenta de un solo uso que no es miembro. Para comprobar que una tesorería corre el código publicado, compara su hash de WASM con la tabla. Las instancias retiradas y las de julio de 2026 no se deben usar.

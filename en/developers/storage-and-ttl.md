---
description: "TTL policy, archival and restoration of contract entries."
cover: ../.gitbook/assets/velo-truway.png
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Storage and TTL

Every storage entry has a time to live (TTL). When it expires, the entry is archived, not deleted.

## Policy

Defined in [`packages/common/src/ttl.rs`](https://github.com/truway-xyz/soroban-contracts/blob/main/packages/common/src/ttl.rs):

| Constant | Value |
|---|---|
| `BUMP_THRESHOLD` | 30 days (518,400 ledgers) |
| `BUMP_TO` | 120 days (2,073,600 ledgers) |

Every write extends the entry it touches and the contract instance, which also extends the code. Reads extend nothing.

## Archived entries

Since protocol 23, an archived entry is restored automatically when a transaction needs it: simulation adds the restore and the submitter pays the rent. An archived entry is **never read as absent**, so a used document cannot be reused even after its `Receipt` entry is archived.

To keep an entry live without writing:

```bash
stellar contract extend --id <CONTRACT_ID> --key-xdr <KEY> --durability persistent --ledgers-to-extend 2073600
```

## Storage changes

In a deployed contract, `DataKey` variants are never renamed, reordered or removed without a migration. New fields are added as `Option<T>`: since `soroban-sdk` 28, a missing optional field reads as `None`.

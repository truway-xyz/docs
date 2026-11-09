# Storage and TTL

Storage on Stellar is rented: every entry has a time to live (TTL) and is archived, not deleted,
when it expires.

## Policy

Defined once in [`packages/common/src/ttl.rs`](https://github.com/truway-xyz/soroban-contracts/blob/main/packages/common/src/ttl.rs)
and applied by every contract:

| Constant | Value |
|---|---|
| `BUMP_THRESHOLD` | 30 days (518,400 ledgers) |
| `BUMP_TO` | 120 days (2,073,600 ledgers) |

Every write extends the entry it touches and the contract instance, which also extends the code.
Reads extend nothing.

## Layout

| Key | Storage | Why there |
|---|---|---|
| `Token`, `TokenSymbol` | Instance | Read by every payment |
| `Members` | Instance, at most 32 entries | Read by every call; the cap keeps the instance small |
| `NextId` | Instance | Read by every proposal |
| `Proposal(id)` | Persistent | One per proposal, kept as the approval record |
| `Line(LineKey)` | Persistent | One per project, line and source |
| `Funds(FundKey)` | Persistent | One per project and source |
| `Receipt(hash)` | Persistent | Enforces single use of each document |

## Entries nobody writes again

Persistent entries that nobody writes for 120 days are archived. Since protocol 23 an archived
entry is restored automatically when a transaction needs it: simulation adds the restore and the
caller pays the rent. **An archived entry is never read as absent**, so a used document cannot be
reused after its `Receipt` entry is archived.

To keep entries live without writing:

```bash
stellar contract extend --id <CONTRACT_ID> --key-xdr <KEY> --durability persistent --ledgers-to-extend 2073600
```

## Changing storage

Variant names and field types are part of the on-ledger encoding. In a deployed contract, a
`DataKey` variant is never renamed, reordered or removed without a migration in the upgraded code.
New stored fields are added as `Option<T>`: since `soroban-sdk` 28, stored structs unpack
tolerantly, and a missing optional field reads as `None`.

# Upgrades and governance

A treasury's code can be replaced. This page says who can do it, how readers find out, and what is
still missing before mainnet.

## How an upgrade works

1. The new WASM is uploaded to the network (`stellar contract upload`) and gets its hash.
2. An admin proposes `Upgrade(wasm_hash)`.
3. A different admin approves it.
4. The contract emits `contract_upgraded` with the hash, the proposer and the approver, **then**
   replaces its code with `update_current_contract`.

Readers must treat events after `contract_upgraded` as coming from the new code. The contract
keeps its ID and its storage; the constructor does not run again.

## Rules for compatible upgrades

- `DataKey` variants are never renamed, reordered or removed without a migration.
- New stored fields are `Option<T>`.
- Event fields are never changed: new information goes in new events, and breaking changes get a
  new standard identifier (`proof-of-spend/2`).
- Error codes are never renumbered.

## Who controls each treasury's code

Each organisation controls its own treasury's upgrades. Truway does not use executable references
(CAP-85), which would let one owner contract upgrade many treasuries at once: that would be a
hidden upgrade path outside each organisation's control.

## Known limits, planned before mainnet

| Limit | Risk | Plan |
|---|---|---|
| One admin approver besides the proposer is enough for membership and code changes | Two colluding admins can replace the code | Approval by a configurable number of admins |
| No timelock | An upgrade takes effect at once | Timelock on upgrades, so readers can react |
| Proposals never expire | An approver may act on stale context (execution still re-checks every rule) | Expiry ledger per proposal |
| No pause | A compromised key cannot be stopped at once (admins can remove the member) | A pause any admin can trigger and only two can lift |
| The code swap is not exercised by unit tests | An incompatible upgrade could reach testnet | Exercise it on testnet before mainnet |

Source: [internal review of 2026-11-07](https://github.com/truway-xyz/soroban-contracts/blob/main/audits/2026-11-07-budget-treasury-internal-review.md), findings BT-07, BT-08, BT-09 and BT-13.

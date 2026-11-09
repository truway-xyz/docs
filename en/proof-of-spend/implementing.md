---
description: "Conformance checklist to implement Proof of Spend in another contract or system."
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

# Implementing the standard

## Conformance checklist

**Declaration**

- [ ] The WASM declares `event_schema = proof-of-spend/1` in its contract meta. In Rust: `contractmeta!(key = "event_schema", val = "proof-of-spend/1")`.

**Events**

- [ ] Emits every event in section 5 of the [specification](specification.md) with its exact name, topics and fields.
- [ ] Emits `contract_upgraded` **before** replacing the code.
- [ ] Documents how optional fields are encoded: since `soroban-sdk` 28, map-format events omit void fields.

**Invariants**

- [ ] Every budget change, expense and payment needs two distinct members.
- [ ] `paid <= budget` on every line, at all times.
- [ ] Every expense is charged to exactly one line.
- [ ] Every expense carries a non-zero `receipt_hash`, used once per contract.
- [ ] Every expense books to its line's `chart`.
- [ ] The contract never runs out of members able to approve.
- [ ] Every amount is greater than zero.

**Privacy**

- [ ] No event carries personal data.

## Testing

`budget-treasury` checks every event against the standard in `events_follow_the_standard` and `governance_events_follow_the_standard` ([`test.rs`](https://github.com/truway-xyz/soroban-contracts/blob/main/contracts/budget-treasury/src/test.rs)). Copy that approach: a renamed field silently breaks every reader.

## Adding a chart of accounts

The chart registry is section 8 of the specification (`CO_PUC`, `CO_CGN`, `PE_PCGE`, `MX_SAT`, `BR_SPED`, `SV_NIIF`, `IFRS`). To add one, open a pull request against [`docs/proof-of-spend.md`](https://github.com/truway-xyz/soroban-contracts/blob/main/docs/proof-of-spend.md).

## Versioning

Breaking changes get a new identifier (`proof-of-spend/2`). New information arrives as new events, never as changed fields. Feedback on the draft goes to [`soroban-contracts` issues](https://github.com/truway-xyz/soroban-contracts/issues).

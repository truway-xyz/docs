# Implementing the standard

Proof of Spend is meant to be implemented by others: another platform, a government system, or a
contract written in a different style. This page is the checklist.

## Conformance checklist

**Declaration**

- [ ] The WASM declares `event_schema = proof-of-spend/1` in its contract meta
  (`contractmeta!(key = "event_schema", val = "proof-of-spend/1")` in Rust).

**Events**

- [ ] Every event in section 5 of the [Specification](specification.md) is emitted with exactly
  its name, topics and data fields, with the types of section 4.
- [ ] `contract_upgraded` is emitted **before** the code is replaced.
- [ ] Readers are told how optional fields are encoded (Soroban map events omit void fields since
  `soroban-sdk` 28).

**Invariants**

- [ ] Every budget change, expense and payment needs two distinct members.
- [ ] `paid <= budget` per line at all times; a budget is never set below what was paid.
- [ ] An expense or payment is charged to exactly one line.
- [ ] Every expense and payment carries a non-zero `receipt_hash`, used at most once per contract.
- [ ] An expense books to its line's `chart`; a payment's line is in the treasury asset and within
  its source's funds.
- [ ] The contract can never be left without enough members to approve.
- [ ] Every amount is greater than zero.

**Privacy**

- [ ] No event carries personal data; identifiers are SHA-256 of opaque references.

## Test it like the reference implementation

`budget-treasury` has conformance tests that check every event's name and data fields against the
standard (`events_follow_the_standard` and `governance_events_follow_the_standard` in
[`src/test.rs`](https://github.com/truway-xyz/soroban-contracts/blob/main/contracts/budget-treasury/src/test.rs)).
Copy that approach: a renamed field silently breaks every reader.

## Adding a chart of accounts

The chart registry is section 8 of the specification (`CO_PUC`, `CO_CGN`, `PE_PCGE`, `MX_SAT`,
`BR_SPED`, `SV_NIIF`, `IFRS`). To add one, open a pull request against
[`docs/proof-of-spend.md`](https://github.com/truway-xyz/soroban-contracts/blob/main/docs/proof-of-spend.md).

## Versioning

Breaking changes produce a new identifier (`proof-of-spend/2`). New information arrives as new
events, never as changed fields. Feedback on the draft: open an issue in
[`soroban-contracts`](https://github.com/truway-xyz/soroban-contracts/issues).

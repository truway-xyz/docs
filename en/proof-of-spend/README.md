# What is Proof of Spend

**Payments prove the money moved. Proof of Spend proves what it bought.**

Proof of Spend (`proof-of-spend/1`) is an open standard for budget execution on Stellar. A
contract that follows it records, for every expense or payment: against which approved budget line,
from which funder, booked to which account, backed by which document, and approved by whom. Anyone
can rebuild a budget execution report or a general ledger from its events, without access to the
organisation's database or its software vendor.

| | |
|---|---|
| Identifier | `proof-of-spend/1` |
| Status | Draft 2, 2026-11-07 |
| Licence | Apache-2.0 |
| Reference implementation | [`budget-treasury`](../architecture/budget-treasury.md) |
| Source | [`soroban-contracts/docs/proof-of-spend.md`](https://github.com/truway-xyz/soroban-contracts/blob/main/docs/proof-of-spend.md) |

## Why a standard and not another platform

Public budgets and restricted grants are executed by many organisations on many systems. Funders,
auditors, oversight bodies and citizens cannot compare or verify execution without asking each
system. Interoperability starts with a shared, public format. Proof of Spend is that format for
the execution step.

## What it covers

**Covered:** budget lines per project and funding source, each with an account code and a
currency; expenses paid outside the ledger and payments made on it, each with its account code and
the fingerprint of its supporting document; the two-person approval behind every change; money held
on the ledger, earmarked by funding source.

**Not covered yet:** procurement and contracting, payments to individual beneficiaries (they need
selective disclosure), milestones and impact.

## How a contract declares it

A conforming contract:

1. declares the contract meta entry `event_schema = proof-of-spend/1` (in its `contractmetav0`
   Wasm section);
2. emits the standard events with exactly their names, topics and fields;
3. enforces every invariant of the standard.

Readers ignore events from contracts that do not declare the meta entry.

## The invariants, in plain words

1. Every budget change, expense and payment was proposed by one member and approved by another.
2. Membership and code changes are approved by an admin.
3. No budget line ever spends more than its budget.
4. An expense is charged to exactly one line, so one funder's money never pays for another's line.
5. Every expense carries a supporting document, and a document backs at most one expense per contract.
6. Every expense books to its line's chart of accounts.
7. The treasury always keeps enough members to approve.
8. Every amount is positive.

Read on: [Specification](specification.md) · [Reading the record](reading-the-record.md) ·
[Implementing the standard](implementing.md).

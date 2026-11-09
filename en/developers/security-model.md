---
description: "What each party can and cannot do, and what a record proves."
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

# Security model

## What each party can do

| Party | Can | Cannot |
|---|---|---|
| `Admin` | Propose any action; approve other members' proposals | Approve their own |
| `Approver` | Approve or reject budgets, expenses and payments | Propose; approve membership or code changes |
| `Operator` | Propose expenses and payments | Approve |
| Truway | Deploy treasuries; build and submit transactions; pay fees; store documents | Move funds, approve, change members or upgrade a treasury |
| Anyone | Fund a project; read everything | Change a record |

## What a record proves

* Two distinct members of that treasury proposed and approved it.
* It fits within the line's budget, and a payment within its source's funds.
* It books to its line's chart of accounts.
* The supporting document has that fingerprint and backs no other record in the same treasury.
* It was produced by code whose WASM hash matches a published build.

## What it does not prove

* That an address belongs to a person: the organization handles that off the ledger.
* That the document is genuine, or that a bank or cash payment happened. `payment_ref` links the external evidence for auditors.
* That another organization did not use the same invoice.
* That two files are different invoices: `receipt_hash` identifies the file.

## Current limits

| Limit | Plan |
|---|---|
| On testnet, the platform holds the demo signers | Per-person signing; demo signers never reach mainnet |
| Truway can delay submitting a signed step | A public submission path |
| The explorer reads Truway's index | Anyone can read the ledger directly: [Verify a record](verify-a-record.md) |
| One admin approver is enough to change members or code | Several admins and a timelock before mainnet |
| Organizations without a treasury still use the earlier server-attested model | Those contracts are frozen and will be removed |

Truway does not hold public money, does not write into government systems and does not store beneficiary data.

---
description: "The treasury asset, payments on the ledger and rails to pesos."
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

# Assets and payments

<figure><img src="../.gitbook/assets/rails.svg" alt="Today public money moves in pesos from the agency to the organization and the supplier by bank or cash, and the receipt is recorded with RecordExpense. On the roadmap, a funder funds the treasury in USDC, the advance goes out through the Stellar Disbursement Platform to the team lead, and an anchor converts it to pesos."><figcaption><p>Today and on the roadmap</p></figcaption></figure>

## The treasury asset

Each treasury holds one asset, set at construction (`token`, `token_symbol`). Any SEP-41 token works, including a classic asset through its Stellar Asset Contract. The testnet instance uses Circle's USDC: `CBIELTK6YBZJU5UP2WWQEUCYKLPU6AUNZ2BQ4WWFEIE3USCIHMXQDAMA`.

Each budget line has its own currency. A line in `COP` records expenses paid in pesos off the ledger; only a line in the treasury asset can pay with `Pay`.

## Payment references

Contract invocations require `MEMO_NONE`. When a payment to an external service needs a reference, it goes in a muxed address (`M...`).

## Rails

| Rail | Purpose | Standard | Availability |
|---|---|---|---|
| `fund` in USDC | Fund the treasury per source | SEP-41 | Built into the contract |
| Stellar Disbursement Platform | Pay an approved advance to the team lead, registered through SEP-24 | SDP, SEP-24 | Coming soon |
| Anchor to Colombian pesos | Move USDC to a bank account or Bre-B | SEP-24, SEP-31 | Coming soon |

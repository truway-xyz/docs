---
description: "What Stellar brings to Truway and what does not move on Stellar."
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

# Stellar in Truway

| Need | What Stellar provides |
|---|---|
| A record no party controls | Public ledger: a written approval cannot be changed or deleted |
| Contract supervision written into the rules | Soroban contracts with per-person `require_auth` and self-approval rejected |
| One invoice, once, across organizations | A shared registry every treasury checks (coming soon) |
| Proof of what money bought | One standard event per expense with line, account and document fingerprint |
| Many small records at low cost | Low, predictable fees |
| Records final in seconds | Ledgers close in about 5 seconds, with no reorganizations |
| Dollars where cooperation money arrives | Circle's USDC, usable from contracts through its Stellar Asset Contract |

## Public money in pesos

Colombian public money leaves each agency's treasury in pesos and reaches suppliers by bank transfer. For that money, Truway records proof of the payment with `RecordExpense`; Stellar is not the payment rail.

Money moves on Stellar where it already arrives in dollars, such as international cooperation funding public programs. See [Assets and payments](assets-and-payments.md).

## Networks

| Network | Status |
|---|---|
| Testnet | In use. See [Deployment](deployment.md) |
| Mainnet | After an independent security review |

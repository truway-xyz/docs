---
icon: star
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

<figure><img src="../.gitbook/assets/stellar-architecture.png" alt="Stellar architecture. Members sign their authorization entry with Privy; the API sends the signed invocation and Truway's submitter account pays the fee through RPC. Each organization has its own budget-treasury instance, deployed from WASM 0.4.0 by a single-use account; the WASM is attested in a GitHub release read by Stellar Expert and Stellar Lab. Contracts emit Proof of Spend events to the ledger, read by the indexer and any reader. Coming soon: USDC to the Stellar Disbursement Platform, an anchor to pesos and a shared document registry."><figcaption><p>Stellar architecture: contracts, accounts and integrations</p></figcaption></figure>

## Public money in pesos

Colombian public money leaves each agency's treasury in pesos and reaches suppliers by bank transfer. For that money, Truway records proof of the payment with `RecordExpense`; Stellar is not the payment rail.

Money moves on Stellar where it already arrives in dollars, such as international cooperation funding public programs. See [Assets and payments](assets-and-payments.md).

## Networks

| Network | Status |
|---|---|
| Testnet | In use. See [Deployment](deployment.md) |
| Mainnet | After an independent security review |

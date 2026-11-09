# Assets, payments and rails

> Status: `Pay` and `fund` are **built in the contract** and used in testnet smoke tests. The rails
> on this page are **roadmap** unless marked otherwise.

## The treasury asset

Each treasury holds one asset, set at construction (`token`, `token_symbol`). Any SEP-41 token
works, including a classic Stellar asset through its Stellar Asset Contract (SAC). The testnet
instance holds **USDC** through Circle's testnet SAC
`CBIELTK6YBZJU5UP2WWQEUCYKLPU6AUNZ2BQ4WWFEIE3USCIHMXQDAMA`.

Budget lines carry their own `currency`. A line in `COP` records expenses paid in pesos outside the
ledger; only a line in the treasury asset can pay with `Pay`.

## Payment references

Soroban invocations must use `MEMO_NONE`. When a payment to an external service needs a
reference, it goes in a muxed address (`M...`), not in a memo.

## Rails

| Rail | What for | Standard | Status |
|---|---|---|---|
| **Stellar Disbursement Platform** (self-hosted) | Pay out an approved field advance to a team lead; receivers are tracked by phone number and register through SEP-24 | SDP, SEP-24 | Roadmap |
| **Anchor to Colombian pesos** | Cash-out of USDC to a bank account or Bre-B | SEP-24 / SEP-31 | Roadmap; partner integration to confirm |
| **USDC from cooperation and philanthropy** | Fund a treasury per funding source with `fund` | SEP-41 | Built in the contract |

## Why public money is not on these rails

Colombian public money leaves the agency in pesos by bank transfer. Truway records that payment
with `RecordExpense` and its evidence. These rails are for money that already arrives in dollars,
such as international cooperation funding a public programme.

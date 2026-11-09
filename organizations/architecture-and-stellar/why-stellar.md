# Why Stellar

Truway does not use Stellar as a database. It uses it for four things a database run by the
agency, the executing organisation or Truway cannot give.

| What the public sector needs | What Stellar gives | Status |
|---|---|---|
| A record nobody controls, not even Truway | A public ledger; once an approval is written, no party can change or delete that history | Live on testnet |
| Contract supervision written into the rules | Soroban contracts that require each person's own authorisation (`require_auth`) and reject self-approval | Live on testnet |
| One invoice, once, across organisations and municipalities | A shared registry that every organisation's contract can check | Design |
| Proof of what money bought, linked to the payment | A standard event per expense with its budget line, account code and document fingerprint | Live on testnet |

## What is not on Stellar today

**Colombian public money does not move on Stellar.** The public budget is in pesos, leaves each
agency's treasury and reaches the contractor by bank transfer. In a 90-day pilot, no agency will
pay a contract in USDC, and no executing organisation will convert public pesos into a digital
asset to pay suppliers. So for public money Truway records proof of the payment
(`RecordExpense`), it is not the payment rail.

Money can move on Stellar where it already arrives in dollars: international cooperation and
philanthropy that fund programmes. That is where field advances through the Stellar Disbursement
Platform and cash-out to pesos come in ([Assets, payments and rails](assets-and-rails.md)).

## Why Stellar and not another network

| Need | Stellar |
|---|---|
| Hundreds of small records per month without the cost mattering | Low, predictable fees; costs per record will be published once measured on testnet |
| Records final within seconds | Ledgers close in about 5 seconds, with no reorganisations |
| Dollars where cooperation money arrives | USDC issued natively by Circle, usable from contracts through its Stellar Asset Contract |
| Local currency in and out | A network of anchors in Latin America |
| Custom rules | Soroban smart contracts in Rust |

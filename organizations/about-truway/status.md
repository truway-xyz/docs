# Current status

Last reviewed: **2026-11-08**. Everything below runs on the Stellar **testnet** with demo data. Nothing is on mainnet, and no pilot with a real contract is running yet.

## What works, and what does not yet

| Capability                                                                                             | Status                                                                                    |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Budget per contract, budget line and funding source, each line with its account code                   | **Live on testnet**                                                                       |
| Field advance (petty cash) assigned to a team, approved by a second person                             | **Live on testnet** (recorded; no money moves yet)                                        |
| Invoice captured from WhatsApp: the assistant reads it and asks which budget line it belongs to        | **Live on testnet**, with a test number                                                   |
| Whoever files an expense cannot approve it                                                             | **Live on testnet**, enforced by the contract                                             |
| A supporting document cannot be used twice in the same organisation                                    | **Live on testnet**, enforced by the contract                                             |
| Public explorer: check one expense by its verification code, no account needed                         | **Live on testnet**                                                                       |
| Public programme page and general ledger download (JSON and CSV)                                       | **Live on testnet**                                                                       |
| Each person signs their own step                                                                       | **Design.** Today the demo uses demo signers held by the platform, labelled _Demo signer_ |
| Bring a contract from Colombia's public procurement portal (SECOP II) by its ID                        | **Design**                                                                                |
| Alerts: expense over the line, invoice already reported elsewhere                                      | **Design**                                                                                |
| A supporting document checked across organisations, and electronic invoices identified by their tax ID | **Design**                                                                                |
| Field advances paid out as money, and cash-out to pesos                                                | **Roadmap**                                                                               |
| Mainnet                                                                                                | **Roadmap**, after an independent security review                                         |
| Donations in USDC                                                                                      | Built, outside the current scope                                                          |

## Versions

| Component                  | Version                                                 | Where                                                     |
| -------------------------- | ------------------------------------------------------- | --------------------------------------------------------- |
| Proof of Spend             | `proof-of-spend/1`, Draft 2 (2026-11-07)                | [Specification](../proof-of-spend/specification.md)       |
| `budget-treasury` contract | `0.4.0`, testnet                                        | [Deployments](../architecture-and-stellar/deployments.md) |
| Security                   | Internal review on 2026-11-07, not an independent audit | [Security](../architecture-and-stellar/security.md)       |

## Adoption

* **6 non-binding letters of intent** from organisations.
* **Pilots paused** for lack of funding in the sector; none is running.
* **11+ organisations interviewed** in **5+ countries**.
* Demand from public officials at a regional workshop of Colombia's National Development Plan (October 2026). Conversations with institutions are verbal so far; none is named here until it is in writing.

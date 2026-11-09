# Architecture

**One sentence:** members of each organisation propose and approve budget changes and expenses in
their own `budget-treasury` contract on Stellar; the Truway platform prepares those transactions
and stores documents; anyone reads the result. **Today no layer moves public money:**
`RecordExpense` records an expense paid by bank or cash; `Pay` can move USDC held in the contract,
and only on testnet.

## Layers

| Layer | What it does | Who controls it | Status |
|---|---|---|---|
| **Members** (admins, approvers, operators) | Propose and approve, each with their own key | The organisation | Live on testnet with demo signers |
| **Truway app** (`app.truway.xyz`) and **WhatsApp channel** | Capture invoices, show budgets, ask for approvals | Truway | Live on testnet |
| **Truway API** | Builds each transaction for the member who must sign it, stores documents and their SHA-256, maps hashed IDs back to names, indexes events | Truway | Live on testnet |
| **`budget-treasury`**, one instance per organisation | Enforces the rules: two signers, budget limits, single-use documents, account codes | Its members; Truway deploys it but is never a member | Live on testnet |
| **Proof of Spend events** | The public interface: budget, expense, payment and governance events | Nobody: they are on the ledger | Live on testnet |
| **Readers** | Funders, auditors, oversight bodies, the public explorer | Anyone | Live on testnet |

## Components

```
 Members ──sign their own step──┐
                                ▼
 WhatsApp ──► Truway API ──builds tx, pays fee──► budget-treasury (one per organisation)
 Web app  ──►    │                                     │
                 │ documents + SHA-256                 │ Proof of Spend events
                 ▼                                     ▼
          private storage                       Stellar ledger ──► Truway indexer ──► Explorer, ledger CSV
                                                       │
                                                       └──────────► any RPC, any indexer, any explorer
```

## What lives on the ledger and what lives off it

| Data | Where | Form | Who can read it |
|---|---|---|---|
| Budget per line and funding source, with chart, account and currency | Ledger | Amounts and codes; IDs as SHA-256 | Anyone |
| Expense: amount, line, account, proposer, approver | Ledger | Addresses and amounts | Anyone |
| Supporting document (invoice, receipt) | Truway's private storage | The file | The organisation; anyone it shares the file with |
| Document fingerprint | Ledger | SHA-256 of the file | Anyone |
| Supplier's tax ID | Truway's database; on the ledger only hashed (`payee_ref`) | SHA-256 | The organisation |
| Names of people, projects and suppliers | Truway's database | Plain text | The organisation and whatever it publishes |
| Who each address belongs to | Truway's database | Mapping | The organisation |

Events never carry personal data. See [Data and guarantees](../public-sector/data-and-guarantees.md).

## Who signs what

| Action | Signs today (testnet) | Signs by design |
|---|---|---|
| Propose a budget line, expense or payment | Demo signer held by the platform | The member, in their browser |
| Approve | A second demo signer | A second member |
| Add or remove members, upgrade the code | Two demo admins | Two admins |
| Pay the network fee and submit | Truway's account | Truway's account |
| Deploy a new treasury | A single-use Truway account that is not a member | Same |

## Design decisions

- [ADR 0003](https://github.com/truway-xyz/soroban-contracts/blob/main/docs/adr/0003-members-sign-proof-of-spend.md):
  members sign, and records follow Proof of Spend. Supersedes ADR 0002 (server-attested records).
- One instance per organisation, so no organisation can touch another's record.
- Narrow contract, business logic above it: the contract enforces money rules; capture, reading
  invoices and reporting happen off chain.

# Lifecycle of an expense

Two paths: an expense paid outside the ledger, which is how public money moves today, and a
payment from funds held in the contract.

## An expense paid by bank transfer or cash

> Status: **Live on testnet** with demo signers.

```
Field team          Truway API                 budget-treasury                 Ledger / readers
    │ photo of the       │                            │                              │
    │ receipt ─────────► │ store file, SHA-256,       │                              │
    │ (WhatsApp or web)  │ read amount, supplier,     │                              │
    │                    │ date with AI (suggests,    │                              │
    │                    │ never decides)             │                              │
Coordinator ─ proposes ► │ build tx ─────────────────►│ propose(RecordExpense)       │
                         │                            │ checks role, line, chart,    │
                         │                            │ room left, document unused ──► proposal_created
Approver ── approves ──► │ build tx ─────────────────►│ approve(id)                  │
                         │                            │ checks again, not the        │
                         │                            │ proposer; adds to line;      │
                         │                            │ marks document used ─────────► expense_recorded
                         │                            │                              ► proposal_executed
                         │ indexer stores events ◄──────────────────────────────────────┘
Anyone ───────────────── explorer: plain-language record, link to the transaction, file check
```

1. The field team pays the supplier and captures the invoice at the moment of payment. The
   platform stores the file and computes its SHA-256.
2. A member proposes `RecordExpense` with the line, source, amount, account code, `receipt_hash`,
   and hashed references to the payment and the supplier.
3. The contract checks the role, that the document was never used, that the line exists in the
   same chart and that the amount fits in what is left.
4. A different member approves. The contract checks everything again, adds the amount to the
   line, marks the document as used and emits `expense_recorded` and `proposal_executed`.
5. The indexer stores the events. The explorer shows the record in plain language.
6. Anyone holding the invoice can hash it and compare it with `receipt_hash`.

### Field advances

In the current demo, a field advance (petty cash for a team) is a budget assignment approved by
two people, and each purchase is legalised against it with its receipt as a `RecordExpense`.
**No money moves on the ledger yet.** Paying the advance out as money is on the
[roadmap](../about/roadmap.md).

## A payment from funds held in the contract

> Status: **Built in the contract**, used on testnet in smoke tests; not part of the app's flow.

1. A funder, or the organisation, calls `fund` to deposit the treasury asset (for example USDC),
   earmarked for a project by a source. The contract emits `project_funded`.
2. A member proposes `Pay` with the destination address, line, source and supporting document.
   Besides the expense checks, the line must be in the treasury asset and the source must hold
   enough funds for the project.
3. A different member approves. The contract transfers the amount, updates the line and the
   source's funds, and emits `payment_executed` and `proposal_executed`.

## States the app shows

| In the app | Meaning |
|---|---|
| *Waiting for approval* | Proposal is `Pending` on the ledger |
| *Approved* | The approval was submitted |
| *Registered · verifiable* | `proposal_executed` is on the ledger and indexed |
| *Rejected* | `proposal_rejected`, with who rejected it |

# Truway in one page

Truway traces payments, their distribution and their impact at the last mile. It starts with
public money executed by third parties: a government agency signs a contract, an organisation
spends it in the field, and anyone can check each expense against the budget it was approved for.

## One path, three roles

```
GOVERNMENT AGENCY         signs a contract and appoints a supervisor        ← champion, approves
      │
      ▼
EXECUTING ORGANISATION    its field team captures each invoice;            ← daily user
      │                   its coordinator files it against a budget line
      ▼
FIELD TEAMS AND SUPPLIERS paid by bank transfer or petty cash advances
      │
      ▼
ANYONE                    oversight groups, councils, comptrollers, citizens ← checks without an account
```

Truway does not distribute subsidies to households and does not handle beneficiaries' data. The
path is always money → executing organisation → field teams and suppliers.

## Four questions about every peso

A movement only counts when each question has a verifiable answer.

| Question | How Truway answers it |
|---|---|
| **Who took part?** | Who proposed the expense and who approved it, two different people, each with their role |
| **Where did the money go?** | Which contract, which budget line, which funding source, which supplier |
| **Who was allowed to do what?** | The role each person held when they acted, enforced by the rules of the record, not by a setting in an app |
| **What had to happen before it counted?** | A second person's approval, a supporting document never used before, and room left in the budget line |

The answers live in a public record that neither Truway, nor the agency, nor the executing
organisation controls.

## What makes it different

- **Two people, always.** Whoever files an expense cannot approve it. The rule is part of the
  record itself.
- **One invoice, once.** A supporting document cannot back two expenses of the same organisation.
  Checking it across organisations is planned (see [Roadmap](roadmap.md)).
- **Booked like an accountant would.** Every budget line and expense carries its account in the
  local chart of accounts, so the execution report and the general ledger come out of the record.
- **An open standard, not a closed platform.** The record follows [Proof of Spend](../proof-of-spend/README.md),
  an open specification any system can implement and anyone can read.

## Where Truway is today

Built and running on the Stellar testnet with demo data. No pilot is running yet: see
[Current status](status.md) for exactly what works and what is planned.

---
description: "Build the execution report and the general ledger from the events."
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

# Reading the record

## Budget execution report

For a project and a period:

1. The latest `budget_set` per `(line, source)` gives the **budget**.
2. The sum of `expense_recorded.amount` and `payment_executed.amount` per `(line, source)` gives what was **spent**.
3. `budget − spent` is what **remains**.
4. Grouping by `source` gives the report for each funder.

Every expense also carries `line_paid` and `line_budget`, so running totals can be checked without replaying history.

| Budget line | Account | Source | Budget | Spent | Remaining |
|---|---|---|---:|---:|---:|
| Tuition | CO_PUC 5135 | Departmental fund | 500,000 | 0 | 500,000 |
| Transport | CO_PUC 5155 | Departmental fund | 200,000 | 62,000 | 138,000 |
| Study materials | CO_PUC 5195 | Corporate partner | 500,000 | 38,500 | 461,500 |

*Demo data in COP.*

## General ledger

Each `expense_recorded` and `payment_executed` is one journal entry:

* **Debit:** `account` in `chart`.
* **Credit:** the account the money came from (cash, bank or the treasury asset).
* **Support:** `receipt_hash`.

Each `project_funded` debits the treasury asset and credits the liability or income account set by the organization.

Truway's public API returns it ready to use:

```bash
curl "https://api.truway.xyz/public/proof/programs/<id>/ledger?format=csv"
```

## Amounts

Fixed point with **7 decimals** in the line's currency. `450000000000` is 45,000.00 COP.

## Identifiers

Projects, lines, sources, payees and payment references are SHA-256 hashes of an identifier chosen by the organization, never the identifier itself.

## History

RPC providers keep events for about 7 days. For longer periods, read from an indexer. See [Events and indexing](../developers/events-and-indexing.md).

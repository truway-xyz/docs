---
description: "Truway terms and their technical equivalent."
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

# Glossary

| Term | Technical equivalent | Meaning |
|---|---|---|
| Program | Project in `budget-treasury` | A contract or agreement with its budget |
| Budget line | `(project, line, source)` | A line of the investment plan, with its account and source |
| Funding source | `source` | Where the money comes from |
| Account code | `chart` and `account` | The chart account, for example PUC `5135` |
| Field advance | Allocation to a team | Money a field team receives and accounts for with receipts |
| Propose | `propose` | First step of any change |
| Approve | `approve` | Second step, always by someone else |
| Public record | Events on the Stellar ledger | Where every approved movement lands |
| Invoice fingerprint | `receipt_hash` (SHA-256) | A code computed from the file |
| Expense code | Record code, for example `PAY-2026-0004` | Used to verify an expense |
| Public program file | Program dashboard | The program's execution, open to all |
| Treasury | `budget-treasury` instance | One per organization |

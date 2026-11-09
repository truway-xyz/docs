---
description: "Public read endpoints, no authentication."
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

# Public API

Base URL: `https://api.truway.xyz`. No authentication. Reads from Truway's index.

| Method | Path | Returns |
|---|---|---|
| `GET` | `/public/proof/{code}` | One expense by its code, for example `PAY-2026-0004` |
| `GET` | `/public/proof/programs/{programId}` | A program's execution per budget line, team and funder |
| `GET` | `/public/proof/programs/{programId}/ledger` | The general ledger as JSON |
| `GET` | `/public/proof/programs/{programId}/ledger?format=csv` | The general ledger as CSV |

## Examples

```bash
curl https://api.truway.xyz/public/proof/PAY-2026-0004
curl "https://api.truway.xyz/public/proof/programs/<programId>/ledger?format=csv" -o general-ledger.csv
```

## Ledger columns

`date`, `code`, `description`, `budget_line`, `chart`, `debit_account`, `debit_name`, `credit_account`, `credit_name`, `amount`, `currency`, `receipt_hash`, `transaction`.

## Errors

```json
{ "error": { "code": "program_not_found", "message": "Program not found" } }
```

| Code | When |
|---|---|
| `proof_not_found` | No expense with that code |
| `program_not_found` | The program does not exist |

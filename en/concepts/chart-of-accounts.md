---
icon: book
description: "How each budget line and expense is booked in the chart of accounts."
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

# Chart of accounts (PUC)

Every budget line and every expense is booked to an account in Colombia's Plan Único de Cuentas (PUC). That is why the general ledger comes straight out of the approved expenses, with nothing retyped.

The base catalogue of four-digit accounts is validated by a public accountant. Six- and eight-digit sub-accounts are accepted under their account (for example `513595` under `5135`).

## Available accounts

| Account | Name | Use |
|---|---|---|
| 1105 | Cash | Where a cash payment comes from |
| 1110 | Banks | Where a transfer comes from |
| 1120 | Savings accounts | Where a transfer comes from |
| 1125 | Funds | Where the money comes from |
| 5105 | Personnel expenses | Expense |
| 5110 | Fees | Expense |
| 5115 | Taxes | Expense |
| 5120 | Leases | Expense |
| 5125 | Contributions and memberships | Expense |
| 5130 | Insurance | Expense |
| 5135 | Services | Expense |
| 5140 | Legal expenses | Expense |
| 5145 | Maintenance and repairs | Expense |
| 5150 | Fitting and installation | Expense |
| 5155 | Travel expenses | Expense |
| 5160 | Depreciation | Expense |
| 5165 | Amortization | Expense |
| 5195 | Miscellaneous | Expense |
| 5205, 5235, 5295 | Personnel, services and miscellaneous (sales) | Expense |
| 5305, 5395 | Financial, other expenses | Expense |

## The journal entry of an expense

Every approved expense is one entry: **debit** the line's account and **credit** the account the money came from, with the invoice as support.

| Debit | Credit | Amount | Support |
|---|---|---:|---|
| 5195 Miscellaneous | 1105 Cash | 38,500 COP | Stationery receipt |

## Other charts

Government agencies keep their books in the General Catalogue of Accounts of Colombia's General Accounting Office. Support for it is on the [roadmap](../about/roadmap.md). The standard already reserves charts for Peru, Mexico, Brazil and El Salvador.

{% hint style="warning" %}
Truway records what was paid. It does not calculate withholding tax, VAT or municipal industry tax.
{% endhint %}

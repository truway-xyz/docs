# Chart of accounts and budget

Four classifications coexist in Colombian public spending, and they are easy to mix up. Truway
keeps each one in its place.

| Classification | Who uses it | In Truway | Status |
|---|---|---|---|
| **PUC** (Plan Único de Cuentas) | Companies; non-profits use it as their reference catalogue | Each budget line and expense carries a PUC account, e.g. `5135` | Base catalogue of four-digit accounts, validated by a public accountant (November 2026); six- and eight-digit sub-accounts accepted under their account |
| **General Catalogue of Accounts** of the General Accounting Office | Government agencies | Reserved | Roadmap: when an agency records directly |
| **Budget classification** and the **budget lines of the contract's investment plan** | The agency (budget) and the supervisor (contract) | The budget line of the file is the line of the investment plan | Live on testnet. Mapping to the official budget code: design |
| **Funding source** | The agency | Each budget line has one source; one source's money never pays another's line | Live on testnet |

## Accounts available today

| Account | Name | Used for |
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
| 5165 | Amortisation | Expense |
| 5195 | Miscellaneous | Expense |
| 5205, 5235, 5295 | Sales personnel, services, miscellaneous | Expense |
| 5305, 5395 | Financial, other expenses | Expense |

## How the general ledger is built

Every approved expense is one journal entry: **debit** the expense account of the line (for
example 5195 Miscellaneous), **credit** the account the money came from (1105 Cash or 1110 Banks),
with the invoice as its support.

| Debit | Credit | Amount | Support |
|---|---|---:|---|
| 5195 Miscellaneous (study materials) | 1105 Cash | 38,500 COP | Stationery receipt |

*Demo data.*

## Out of scope

Withholding taxes, VAT and municipal industry tax. Truway records what was paid; it does not
calculate taxes.

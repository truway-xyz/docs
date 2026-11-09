# Glossary

The public sector pages use everyday words. The technical pages use precise ones. This table maps
one to the other.

| In the public sector pages | In the technical pages | Meaning |
|---|---|---|
| Public record | Stellar ledger, contract events | Where every approved movement is written, readable by anyone |
| Contract file | A project in a `budget-treasury` instance | Everything about one contract: budget lines, expenses, approvals |
| Budget line | Budget line `(project, line, source)` | A line of the contract's investment plan, funded by one source |
| Funding source | `source` | Where the money comes from: national budget, royalties, transfers, own funds, cooperation |
| Account code | `chart` and `account` | The account in the chart of accounts, e.g. PUC `5135` |
| Document fingerprint | `receipt_hash` (SHA-256) | A code computed from the file; any change to the file changes it |
| Verification code | The record's code in the explorer | What you type to find one expense |
| Proposes | `propose` | First person files the expense |
| Approves | `approve` | A different person accepts it and it becomes final |
| Field advance | Budget assignment to a team | Petty cash given to a field team, accounted for with receipts |
| Organisation's record book | `budget-treasury` instance | One per organisation |
| Demo signer | Platform-held testnet key | Stands in for a person until per-person signing ships |

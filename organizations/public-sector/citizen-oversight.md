# For citizen oversight

> Status: **live on testnet** with demo data.

Oversight groups, council members, comptrollers and any citizen can check how a public contract is
being spent, without an account and without asking anyone for permission.

## Read the contract file

The public page of a programme shows, per budget line: what was budgeted, what was spent and what
is left, and every expense with its supplier, account code, who filed it, who approved it and when.
The general ledger can be downloaded as CSV to analyse it in a spreadsheet.

## Check one expense

1. Open `app.truway.xyz/proof/` followed by the **verification code** of the expense.
2. You see the expense in plain language: amount, budget line, funding source, who filed it and who
   approved it.
3. If you have the invoice, **drop the file on the page**. Your browser computes its fingerprint
   and tells you if it matches the one recorded when it was approved. The file never leaves your
   computer.
4. Follow the link to the public record to see the same entry outside Truway.

## What a match proves, and what it does not

| A match proves | It does not prove |
|---|---|
| This exact file is the one that was approved | That the invoice itself is genuine |
| Two different people filed and approved it | Who those people are: the organisation knows that |
| It fits within the approved budget line | That the money was actually paid by bank or cash: that evidence stays with the organisation and its auditors |
| The file backs no other expense of that organisation | That it was not used by another organisation (in design) |

A different photo of the same paper invoice will not match: the fingerprint belongs to the file.

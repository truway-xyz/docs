---
description: "budget-treasury error codes."
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

# Errors

Error codes are part of the public interface and are never renumbered.

| Code | Name | When |
|---:|---|---|
| 1 | `Unauthorized` | The caller is not a member, or their role cannot do this |
| 2 | `SelfApproval` | The approver is the proposer |
| 3 | `NotFound` | Unknown proposal or member |
| 4 | `InvalidAmount` | Zero or negative amount |
| 5 | `BudgetExceeded` | The expense does not fit in what is left of the line |
| 6 | `InsufficientFunds` | The source does not hold enough funds for the project |
| 7 | `InvalidState` | The proposal is no longer pending |
| 8 | `LineNotFound` | The budget line does not exist |
| 9 | `BudgetBelowPaid` | A budget cannot go below what was spent |
| 10 | `ChartMismatch` | The expense uses a different chart from its line |
| 11 | `QuorumLost` | The change would leave the treasury without an admin or two approvers; also at construction with fewer than two distinct admins |
| 12 | `NoAdmins` | The constructor received an empty admin list |
| 13 | `ReceiptAlreadyUsed` | The document already backs another record |
| 14 | `ReceiptRequired` | No supporting document |
| 15 | `CurrencyMismatch` | The currency does not match the line or the treasury asset |
| 16 | `TooManyMembers` | More than 32 members |

In a failed simulation they appear as `Error(Contract, #13)`.

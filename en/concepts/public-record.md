---
description: "What the public record keeps, what it proves and what it does not."
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

# Public record

Every approved allocation and expense lands on a public record. Nobody can change or delete it: not Truway, not the agency, not the organization.

## What each expense keeps

| Field | Example |
|---|---|
| Code | `PAY-2026-0004` |
| Program, budget line and funder | Scholarships · Study materials · Departmental fund |
| Account code | PUC 5195 Miscellaneous |
| Amount and currency | 38,500 COP |
| Who recorded it and who approved it | Two different people |
| Invoice fingerprint | A code computed from the file |
| Date | When it was approved |

## The invoice fingerprint

The fingerprint is a code computed from the invoice file. If the file changes, even by one pixel, the fingerprint changes. The file cannot be rebuilt from it, so the invoice stays private.

To check an invoice, drop it on the expense page: your browser computes its fingerprint and compares it with the recorded one. See [Verify an expense](../guides/verify-an-expense.md).

## What it proves and what it does not

| Proves | Does not prove |
|---|---|
| That this exact file is the one that was approved | That the invoice is genuine |
| That two different people recorded and approved it | Who those people are: the organization knows |
| That it fits within the approved budget line | That the bank or cash payment happened: that evidence stays with the organization and its auditors |
| That the file backs no other expense of the organization | That another organization did not use it |

{% hint style="info" %}
The fingerprint belongs to the file, not the invoice: another photo of the same paper invoice has a different fingerprint. Checking invoices across organizations by their CUFE is on the [roadmap](../about/roadmap.md).
{% endhint %}

## An open standard

The record follows [Proof of Spend](../proof-of-spend/README.md). Any system can read it and build the execution report or the general ledger without Truway.

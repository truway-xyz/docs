---
icon: clock-rotate-left
description: "Versions of the standard, the contract and the platform."
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

# Release notes

## November 2026

### Proof of Spend · Draft 2

* The standard is renamed Proof of Spend (`proof-of-spend/1`).
* Budget lines per funding source, with a currency.
* `expense_recorded` for expenses paid off the ledger.
* `proposal_executed` and `contract_upgraded`.
* A supporting document is required on every expense.

### budget-treasury 0.4.0

* Requires two distinct admins at construction.
* Up to 32 members.
* Validates membership proposals when they are proposed.
* Event conformance tests against the standard.
* `soroban-sdk` 29.0.1 (protocol 29).
* Deployed on testnet. See [Deployment](../developers/deployment.md).

### Platform

* Budget per line with PUC account and funder.
* Field advances to teams with two-person approval.
* WhatsApp capture with budget line selection.
* Public expense explorer and in-browser invoice check.
* Public program dashboard and general ledger as CSV.

{% hint style="info" %}
USDC donations are built but outside the current scope.
{% endhint %}

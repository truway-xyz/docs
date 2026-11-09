---
icon: bolt
description: "Proof of Spend events and how they are indexed."
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

# Events and indexing

| Event | Topics | When |
|---|---|---|
| `budget_set` | `project` | A budget line is created or changed |
| `expense_recorded` | `project` | An expense paid off the ledger is recorded |
| `payment_executed` | `project` | A payment leaves the treasury |
| `project_funded` | `project` | Money enters for a project and source |
| `proposal_created` | `id` | A member opens a proposal |
| `proposal_executed` | `id` | A proposal is approved and executed |
| `proposal_rejected` | `id` | A proposal is rejected or withdrawn |
| `member_added` | `member` | A member is added or their role changes |
| `member_removed` | `member` | A member is removed |
| `contract_upgraded` | `proposal_id` | Right before the code is replaced |

The first topic is the event name as a `Symbol`; the data is a map of the remaining fields. Exact fields are in the [specification](../proof-of-spend/specification.md).

{% hint style="info" %}
Since `soroban-sdk` 28, map-format events omit void fields. No Proof of Spend event has optional fields today; if a future version adds one, a missing key reads as empty.
{% endhint %}

## Retention

RPC providers keep events for about **7 days**. The current state of every line can always be read from the contract (`line`, `funds`, `receipt_use`, `proposal`).

## Truway's indexer

Every 15 seconds, a job on the `treasury-ops` queue reads new events from every treasury, starting at its last cursor, and stores them in `treasury_events`. It runs once even with several API instances. The explorer, dashboard and general ledger are built from those events. See [Public API](public-api.md).

## Index it yourself

| Option | Good for |
|---|---|
| RPC `getEvents` with a contract filter and a cursor | A small, continuous reader |
| Third-party indexers ([directory](https://developers.stellar.org/docs/data/indexers)) | Queries without running infrastructure |
| Galexie or the public Stellar data lake | Full history, independent of any provider |
| Hubble (BigQuery) | Analytics over history |

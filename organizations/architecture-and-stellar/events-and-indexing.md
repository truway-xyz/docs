# Events and indexing

Proof of Spend events are the public interface of a treasury. This page covers how to read them;
their exact fields are in the [Specification](../proof-of-spend/specification.md).

## The events

| Event | Topics | Emitted when |
|---|---|---|
| `budget_set` | `project` | An approved proposal creates or changes a budget line |
| `expense_recorded` | `project` | An expense paid outside the ledger is recorded |
| `payment_executed` | `project` | A payment leaves the treasury |
| `project_funded` | `project` | Money enters the treasury for a project and source |
| `proposal_created` | `id` | A member opens a proposal |
| `proposal_executed` | `id` | Any proposal is approved and executed |
| `proposal_rejected` | `id` | A proposal is rejected or withdrawn |
| `member_added` | `member` | A member is added or their role changes |
| `member_removed` | `member` | A member is removed |
| `contract_upgraded` | `proposal_id` | Right before the code is replaced |

Encoding follows Soroban's `#[contractevent]` default: the first topic is the event name as a
`Symbol`, then the fields marked as topics; the data is a map of the remaining fields keyed by
name.

> **Sparse maps.** Since `soroban-sdk` 28, a map-format event leaves out fields whose value is
> void (`None`). Proof of Spend events have no optional fields today; if a future version adds
> one, readers must treat a missing key as absent.

## Retention: why an indexer is needed

Stellar RPC providers keep events for about **7 days**. Anything older must come from an
indexer or a history archive. The current state of every line can always be read directly from
the contract (`line`, `funds`, `receipt_use`, `proposal`).

## Truway's indexer

> Status: **Live on testnet**.

- Every 15 seconds, a job in the `treasury-ops` queue reads new events of every treasury
  registered in the platform, from its last cursor, and stores them in the `treasury_events`
  table. One run at a time, even with several API instances.
- The explorer, the programme page and the general ledger are built from that table.
- The public read API:

| Endpoint | Returns |
|---|---|
| `GET /public/proof/<code>` | One record by its verification code |
| `GET /public/proof/programs/<id>` | Execution of a programme per line and source |
| `GET /public/proof/programs/<id>/ledger` | General ledger as JSON; `?format=csv` for a spreadsheet |

Base URL: `https://api.truway.xyz`.

## Indexing it yourself

You do not need Truway's index. Options, from simplest to most complete:

| Option | Good for |
|---|---|
| Poll RPC `getEvents` with a contract filter and keep a cursor | A small reader that runs continuously |
| A third-party indexer with Stellar support (see the [indexer directory](https://developers.stellar.org/docs/data/indexers)) | Queries without running infrastructure |
| Galexie, exporting ledgers to your own storage, or the public Stellar data lake | Full history, independent of any provider |
| Hubble (SDF's BigQuery dataset) | Analytics over history |

A read-only reference indexer for Proof of Spend is on the roadmap for `v1.0` of the standard.

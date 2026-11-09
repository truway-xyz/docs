# Platform

The part of Truway that is not on the ledger: the app, the API, the WhatsApp channel and storage.
It is closed source. This page describes its model, not its servers.

## One API, one door to the ledger

All business logic lives in one modular API. The web app and the WhatsApp channel are thin. Only
the API builds transactions for the contracts, which keeps what reaches the ledger easy to audit.

| Module | What it does |
|---|---|
| Projects and budget | Contracts, budget lines with account codes, funding sources, field teams |
| Treasury | Builds proposals and approvals for `budget-treasury`, deploys a treasury per organisation |
| Capture | Receives invoices from the web or WhatsApp; an AI model reads amount, supplier, date and tax IDs |
| Identity and permissions | Sign-in with Google or email; roles per organisation, area or project |
| Indexer | Copies Proof of Spend events into the database for the explorer and reports |
| Public read API | Explorer data, programme execution, general ledger |

## The AI suggests, people decide

The model reads the invoice and proposes the fields. A person reviews them and proposes the
expense; a different person approves it. An expense read by AI and never approved never reaches
the ledger.

## Roles in the app

Seven base roles: organisation admin, project manager, finance operator, finance approver, report
manager, auditor and viewer. Organisations can combine permissions into their own roles.

On testnet, people are enrolled in the treasury with a demo rule: whoever only files expenses is
an `Operator`, whoever only approves is an `Approver`, and whoever does both becomes an `Admin`.
The permanent mapping between app roles and contract roles is being defined.

## Security layers

1. **Authentication:** a short-lived token checked on every request, with a request limit per
   client before the token is even read.
2. **Permissions:** explicit permissions such as `transaction.approve`, granted per organisation,
   area or project. Whatever is not allowed is denied.
3. **Business rules:** for example, whoever files an expense cannot approve it; in the treasury
   the contract enforces this too.
4. **Isolation:** every query is scoped to the organisation. Each organisation's record lives in
   its own contract.

Sensitive actions (approving, reassigning, changing roles) leave an audit log entry with actor,
resource and time. Uploaded files are checked for type and size; HTTP responses carry standard
security headers.

## Infrastructure

The API, its workers and the app run on a major cloud provider, with a managed PostgreSQL
database, a queue system for background jobs and private object storage for supporting
documents, accessed through short-lived signed links. The public website runs on a CDN.

## Code and quality

Four repositories under [`truway-xyz`](https://github.com/truway-xyz): the contracts (public),
the API, the app and the website. The API runs a type check and its unit tests on every change.

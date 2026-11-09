---
icon: plug
description: "Which government systems and tools Truway connects to."
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

# Government integrations

Truway covers contract execution. It reads information that already exists, exports to the organization's tools and publishes the program file. It never writes into a government system.

| System | What Truway does | Availability |
|---|---|---|
| **Electronic invoice (DIAN)** | Reads the tax ID, supplier, date and amount from the photo or PDF | Available |
| **WhatsApp** | Receives the receipt photo and asks for the budget line | Available |
| **Accounting software** (Siigo, Alegra, World Office and others) | Exports the general ledger as CSV or JSON | Available |
| **Open data** | Publishes the program file and its downloads | Available |
| **SECOP II** | Pulls the contract by its ID: agency, contractor, object, value, dates, supervisor and funding source | Coming soon |
| **SECOP II reconciliation** | Compares what SECOP reports as paid with what the file has approved | Coming soon |
| **CUFE validation with DIAN** | Confirms the electronic invoice exists | Coming soon |
| **Banks and Bre-B** | Links the transfer receipt to the expense | Coming soon |
| **Investment projects (BPIN)** | Links the file to the project that funds it | Coming soon |
| **SECOP I** | For municipalities still on the older portal | Coming soon |
| **Public accounting and comptrollers** | Exports in their formats | Coming soon |

## Funding sources

Each budget line is classified by its source: national budget (PGN), transfers (SGP), royalties (SGR), own funds or cooperation. The report per funder comes straight out of the file.

## Chart of accounts and budget

The budget line in the file is the line of the contract's investment plan, and each one carries its PUC account. See [Chart of accounts (PUC)](../concepts/chart-of-accounts.md).

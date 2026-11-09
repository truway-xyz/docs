# Government systems

Officials asked for *"an interoperable system that links the formulation, budget allocation,
contracting, execution and evaluation"* of projects funded with public money. Truway covers
**execution**. This page shows what it connects to before and after, and the status of each
connection.

**Truway reads, exports or publishes. It never writes into a government system.**

| System | Run by | What Truway does with it | Direction | Status |
|---|---|---|---|---|
| **SECOP II** (open data) | Colombia Compra Eficiente | Brings in the contract by its ID: agency, contractor, object, value, dates, supervisor, funding source, invoiced and paid amounts | Reads | Design. The open data source was tested; the connection is not built |
| **SECOP II reconciliation** | | Compares what the portal reports as paid with what the file has approved | Reads | Design |
| **SECOP I** | Colombia Compra Eficiente | The municipalities still on the older portal | Reads | Roadmap |
| **Electronic invoice** (DIAN) | DIAN | Reads the supplier's tax ID, name, date, total and the invoice's unique code (CUFE) from the photo or the PDF | Reads the document | Reading in the WhatsApp assistant. Automatic validation against DIAN: roadmap |
| **Banks and Bre-B** | Banks, Banco de la República | Links the transfer receipt to the expense as payment evidence | Reads | Field available; flow in the app to confirm |
| **Investment projects** (BPIN) | DNP | The file can cite the project that funds the contract | Reference | Roadmap |
| **Funding sources** (national budget, transfers, royalties, own funds, cooperation) | DNP, Ministry of Finance, the agency | Each budget line carries its funding source | Classifies | Live on testnet as free text; official catalogue: design |
| **The agency's budget execution system** | Ministry of Finance, the agency | The execution report per budget line supports the supervisor | Exports | Roadmap |
| **Public accounting and comptroller reporting** | General Accounting Office, comptrollers | Exports that save work for the organisation and the supervisor | Exports | Roadmap; formats to confirm |
| **The organisation's accounting software** (Siigo, Alegra, World Office and others) | The organisation | General ledger as CSV or JSON | Exports | Live on testnet |
| **Open data and oversight** | Citizens | Public file and downloads | Publishes | Live on testnet |
| **WhatsApp Business** | Meta | Capture channel, not the product | Receives | Live with a test number |

## Why this order

The contract already exists in SECOP II, so Truway should bring it in, not ask anyone to type it
again. The organisation's accounting already exists, so Truway exports to it. What did not exist
is the step in between: proof of what the money bought, approved by two people and open to
everyone.

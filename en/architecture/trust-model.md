# Trust model

What you have to trust, what you do not, and the limits we know about. Read this before relying on
any record.

## In one table

| Party | Can | Cannot |
|---|---|---|
| **Admin** of an organisation | Propose anything; approve any proposal of another member | Approve their own proposal |
| **Approver** | Approve or reject budgets, expenses and payments | Propose; approve membership or code changes |
| **Operator** (field coordinator) | Propose expenses and payments | Approve anything |
| **Truway** | Deploy a treasury; build and submit transactions; pay fees; store documents; delay or refuse to submit | Move funds, approve, change members or upgrade a treasury (it is never a member) |
| **Anyone** | Fund a project; read every record | Change any record |

## What a record proves

- Two **distinct** members of that organisation's treasury proposed and approved it.
- It fits within the budget its funding source assigned to that line, and a payment within the
  funds that source holds.
- It books to the chart of accounts of its line.
- Its supporting document hashes to `receipt_hash`, and that document backs no other record **in
  the same treasury**.
- It was produced by the code whose WASM hash you can compare with a published, attested build.

## What a record does not prove

- **That an address is a given person.** Binding addresses to people happens off the ledger, in
  the organisation.
- **That the document is genuine**, or that an expense paid outside the ledger was really paid.
  `RecordExpense` is attested by two members, not proven. `payment_ref` links the external
  evidence for auditors.
- **That the same invoice was not used by another organisation.** Single use is per treasury
  today. A shared registry is planned.
- **That two files are different invoices.** `receipt_hash` identifies the file. Two photos of
  one paper invoice hash differently. Electronic invoices will also be indexed by their tax
  authority ID.

## Where you trust Truway today

These rows are uncomfortable on purpose.

| Today | Why | What changes it |
|---|---|---|
| **On testnet, the platform holds the demo signers.** Whoever holds them can propose and approve in the demo treasury | Per-person signing is not built yet | Per-person signing; demo signers never go to mainnet |
| **Truway can delay a step** by not submitting it | Truway is the submitter and fee payer | Any party can submit a signed transaction through any RPC; a public submission path is not built |
| **The explorer is Truway's** | It reads Truway's index | Read the ledger directly: [Verify it yourself](verify-it-yourself.md) |
| **Two colluding admins can replace the contract code** | One admin approver besides the proposer is enough | Several admins and a timelock before mainnet. Every upgrade emits `contract_upgraded` before the code changes |
| **Organisations without a treasury still use the earlier model**, where the platform key writes records to legacy contracts | The migration is not finished | Legacy contracts are frozen and will be removed |

## What Truway does not do

- It does not hold, move or custody public money.
- It does not write into any government system.
- It does not record data about beneficiaries.

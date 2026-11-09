# How a contract file works

A contract file brings together everything about one public contract: its budget lines, every
expense with its invoice, who filed it, who approved it and how much is left. This page follows
one contract from start to finish.

## The people

| Who | Role in the file |
|---|---|
| **Supervisor** (government agency) | Approves budget lines and expenses |
| **Coordinator** (executing organisation) | Files each expense against a budget line |
| **Field team** | Sends the photo of each invoice or receipt from their phone |
| **Anyone** (oversight group, council, comptroller, citizen) | Reads the file and checks any expense |

## Step by step

| # | What happens | Status |
|---|---|---|
| 1 | The contract is linked by its ID on the public procurement portal (SECOP II); agency, contractor, value, dates, supervisor and funding source fill in automatically | Design. Today the contract is entered by hand |
| 2 | The budget lines of the investment plan are loaded, each with its account code and funding source. **A second person approves them**, and from then on they cannot change quietly | Live on testnet |
| 3 | A field advance (petty cash) is assigned to a team, and a second person approves it | Live on testnet |
| 4 | The team pays a supplier and sends a photo of the invoice by WhatsApp. The assistant reads the amount, supplier and date and asks which budget line it belongs to | Live on testnet |
| 5 | The coordinator reviews it and files it against the line | Live on testnet |
| 6 | A different person approves it. Whoever filed it cannot approve it | Live on testnet |
| 7 | If the invoice was already used for another expense, it is refused | Live on testnet within the same organisation; across organisations is in design |
| 8 | The expense appears in the public file with its verification code | Live on testnet |
| 9 | The execution report per budget line and funding source, and the general ledger, come straight out of the file | Live on testnet |

## Why each step matters

- **Two people, always.** It is contract supervision, written into the rules of the record, not a
  setting someone can switch off.
- **One invoice, once.** No invoice can back two expenses of the same organisation, and checking
  across organisations is coming next.
- **Captured when it is paid.** The invoice arrives the moment the money is spent, not weeks later
  when the report is due.
- **Nothing to install.** WhatsApp works on any phone, which matters in municipalities with poor
  connectivity.

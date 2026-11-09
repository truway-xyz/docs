# Data and guarantees

What Truway keeps, where, in what form, who can read it and for how long. The public record is
public on purpose; personal data never goes into it.

## Where each piece of data lives

| Data | Where it lives | Form | Who can read it | How long |
|---|---|---|---|---|
| Budget per line, with account code and funding source | Public record | Amounts and codes | Anyone | Permanently |
| Each approved expense: amount, line, account, date | Public record | Amounts and codes | Anyone | Permanently |
| Who filed and who approved | Public record | An anonymous account code per person | Anyone; only the organisation knows who each code belongs to | Permanently |
| Fingerprint of the invoice | Public record | A code computed from the file; the file cannot be rebuilt from it | Anyone | Permanently |
| The invoice or receipt file | Truway's private storage | The file | The organisation, and whoever it shares the file with | To be defined before the first pilot |
| Supplier's name and tax ID | Truway's database; in the public record only as a fingerprint | Plain text | The organisation, and what it decides to publish | To be defined before the first pilot |
| Names of people, phone numbers of team leads | Truway's database | Plain text | The organisation | To be defined before the first pilot |
| WhatsApp messages | Truway's database | Text and images | The organisation | To be defined before the first pilot |
| Data about beneficiaries of a programme | **Nowhere** | | | |

**Permanently** means it: the public record cannot be deleted by Truway, the agency or the
organisation. That is why nothing personal goes there.

## What Truway guarantees

- **It does not touch or hold public money.** Payments are made by the agency and the organisation
  through their banks.
- **It does not replace SECOP**, the agency's budget system or anyone's accounting.
- **It never writes into a government system.**
- **Data can be exported at any time**, in open formats (CSV and JSON).
- **No data about beneficiaries.** Programmes that pay households are outside Truway.
- **The AI never decides.** It reads invoices; people approve.

## What the organisation decides

Which names to show next to each expense in the public file, and which documents to share. By
default the public file shows supplier names and amounts, which are public information in a public
contract, and never personal data of individuals.

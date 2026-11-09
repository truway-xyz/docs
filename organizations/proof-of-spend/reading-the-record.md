# Reading the record

How to turn Proof of Spend events into the two documents funders and auditors ask for. The rules are in section 7 of the [Specification](specification.md); this page shows them with an example.

## Budget execution report

For a project and a period:

1. The latest `budget_set` per `(line, source)` gives the **budget**.
2. The sum of `expense_recorded.amount` and `payment_executed.amount` per `(line, source)` gives what was **spent**.
3. `budget − spent` is what **remains**.
4. Grouping by `source` gives the report each funder asks for.

Every expense and payment also carries `line_paid` and `line_budget`, so a reader can check running totals without replaying the whole history.

| Line            | Account      | Source                        |  Budget |  Spent | Remaining |
| --------------- | ------------ | ----------------------------- | ------: | -----: | --------: |
| Tuition         | CO\_PUC 5135 | Departmental education fund   | 500,000 |      0 |   500,000 |
| Transport       | CO\_PUC 5155 | Departmental education fund   | 200,000 | 62,000 |   138,000 |
| Study materials | CO\_PUC 5195 | Corporate scholarship partner | 500,000 | 38,500 |   461,500 |

_Demo data in COP, from the testnet demo programme "Higher-education scholarships, Cundinamarca (sample)". The organisations named are fictitious._

## General ledger

Each `expense_recorded` and `payment_executed` is one journal entry:

* **Debit** `account` in `chart` (the expense).
* **Credit** the account where the organisation booked the money: bank, cash or the treasury asset.
* **Support:** `receipt_hash`.

Each `project_funded` debits the treasury asset and credits the liability or income account set by the organisation's policy.

| Debit                                | Credit     | Amount | Support                                  |
| ------------------------------------ | ---------- | -----: | ---------------------------------------- |
| 5195 Miscellaneous (study materials) | 1105 Cash  | 38,500 | `receipt_hash` of the stationery receipt |
| 5155 Travel (bus passes)             | 1110 Banks | 62,000 | `receipt_hash` of the transport invoice  |

_Demo data._ Truway's public API returns this ledger as JSON or CSV: `GET https://api.truway.xyz/public/proof/programs/<id>/ledger?format=csv`.

## Amounts

Amounts are fixed point with **7 decimals** in the line's currency. `450000000000` is 45,000.00 COP. Divide by 10⁷ before displaying.

## Names and tax IDs

Projects, lines, sources, payees and payment references appear as SHA-256 of an identifier chosen by the organisation, never as the identifier itself. Mapping them back to names happens off the ledger, with whatever the organisation publishes.

## History

RPC providers keep events for about 7 days. To build reports over longer periods, read from an indexer: see [Events and indexing](../architecture-and-stellar/events-and-indexing.md).

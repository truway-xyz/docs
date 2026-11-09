# budget-treasury

> Status: **Live on testnet**, version `0.4.0`. Source: [`contracts/budget-treasury`](https://github.com/truway-xyz/soroban-contracts/tree/main/contracts/budget-treasury).

The reference implementation of [Proof of Spend](../proof-of-spend/proof-of-spend.md). One instance per organisation. It holds the organisation's members and roles, budget lines per project, line and funding source, funds per project and source, proposals, and the supporting documents already used.

**Built with** Rust 1.96.0, `soroban-sdk` 29.0.1 (protocol 29), target `wasm32v1-none`, Stellar CLI 27. The contract declares `event_schema = proof-of-spend/1` in its `contractmetav0` section.

## Roles

| Role       | Can propose           | Can approve or reject          |
| ---------- | --------------------- | ------------------------------ |
| `Admin`    | Anything              | Any proposal of another member |
| `Approver` | Nothing               | Budgets, expenses and payments |
| `Operator` | Expenses and payments | Nothing                        |

Nobody approves their own proposal. Membership and code changes need an admin approver.

## Actions

Everything that changes state is a proposal, approved by a different member.

| Action                    | What it does                                                                                                                             | Moves funds |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `SetBudget(BudgetChange)` | Creates or changes a budget line `(project, line, source)` with its `chart`, `account`, `currency` and amount. Never below what was paid | No          |
| `RecordExpense(Expense)`  | Records an expense paid outside the ledger (bank transfer, cash) with its `receipt_hash`, `payment_ref` and `payee_ref`                  | No          |
| `Pay(Payment)`            | Pays from funds held in the contract to an address                                                                                       | Yes         |
| `AddMember(MemberChange)` | Adds a member or changes a role                                                                                                          | No          |
| `RemoveMember(Address)`   | Removes a member                                                                                                                         | No          |
| `Upgrade(BytesN<32>)`     | Replaces the contract code with an uploaded WASM                                                                                         | No          |

`fund(from, project, source, amount)` is the only call outside proposals: anyone can deposit the treasury asset, earmarked for a project by a funding source.

## Interface

```rust
__constructor(admins: Vec<Address>, token: Address, token_symbol: Symbol)
fund(from: Address, project: BytesN<32>, source: BytesN<32>, amount: i128) -> Result<i128, Error>
propose(proposer: Address, action: Action) -> Result<u64, Error>
approve(approver: Address, id: u64) -> Result<(), Error>
reject(member: Address, id: u64) -> Result<(), Error>

// Read, no authorisation
token() -> Address
token_symbol() -> Symbol
role(member: Address) -> Option<Role>
members() -> Map<Address, Role>
line(project: BytesN<32>, line: BytesN<32>, source: BytesN<32>) -> Option<BudgetLine>
funds(project: BytesN<32>, source: BytesN<32>) -> i128
receipt_use(receipt_hash: BytesN<32>) -> Option<u64>
proposal(id: u64) -> Option<Proposal>
```

## A proposal's life

```
            propose (member with the right role; full validation)
                 │
                 ▼
             ┌─────────┐   approve (different member; validation again; executes)   ┌──────────┐
             │ Pending │ ─────────────────────────────────────────────────────────► │ Executed │
             └─────────┘                                                            └──────────┘
                 │
                 │ reject (an admin, an approver for non-sensitive actions, or the proposer withdrawing)
                 ▼
             ┌──────────┐
             │ Rejected │
             └──────────┘
```

Validation runs twice, when proposing and when approving, because state may change in between.

## Rules the contract enforces

* At least **two distinct admins** at construction, or it fails with `QuorumLost`, so a treasury can never be born locked.
* At most **32 members** (`MAX_MEMBERS`), because members live in instance storage, which every call loads.
* The treasury always keeps at least one admin and two members able to approve.
* For every line, `paid <= budget` at all times.
* A payment never exceeds the funds its source holds for the project, and its line is in the treasury asset.
* An expense or payment books to the `chart` of its line, and carries a non-zero `receipt_hash` that backs no other executed expense or payment **in this treasury**.
* Every amount is greater than zero. Amounts are fixed point with 7 decimals in the line's currency: 45,000 COP is `450000000000`.

## Errors

Error codes are part of the public interface and are never renumbered.

| Code | Name                 | When                                                                                                                            |
| ---: | -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
|    1 | `Unauthorized`       | The caller is not a member, or their role cannot do this                                                                        |
|    2 | `SelfApproval`       | The approver is the proposer                                                                                                    |
|    3 | `NotFound`           | Unknown proposal or member                                                                                                      |
|    4 | `InvalidAmount`      | Amount is zero or negative                                                                                                      |
|    5 | `BudgetExceeded`     | The expense or payment does not fit in what is left of the line                                                                 |
|    6 | `InsufficientFunds`  | The source does not hold enough funds for the project                                                                           |
|    7 | `InvalidState`       | The proposal is no longer pending                                                                                               |
|    8 | `LineNotFound`       | The budget line does not exist                                                                                                  |
|    9 | `BudgetBelowPaid`    | A budget cannot be set below what was paid                                                                                      |
|   10 | `ChartMismatch`      | The expense books to a chart different from its line                                                                            |
|   11 | `QuorumLost`         | The change would leave the treasury without an admin or two approvers; also at construction with fewer than two distinct admins |
|   12 | `NoAdmins`           | The constructor received an empty admin list                                                                                    |
|   13 | `ReceiptAlreadyUsed` | The supporting document already backs another executed record                                                                   |
|   14 | `ReceiptRequired`    | No supporting document                                                                                                          |
|   15 | `CurrencyMismatch`   | The currency does not match the line or the treasury asset                                                                      |
|   16 | `TooManyMembers`     | More than 32 members                                                                                                            |

## Storage

| Key                                         | Storage    | Value                                         |
| ------------------------------------------- | ---------- | --------------------------------------------- |
| `Token`, `TokenSymbol`, `Members`, `NextId` | Instance   | Read by most calls                            |
| `Proposal(id)`                              | Persistent | One per proposal, kept as the approval record |
| `Line(LineKey)`                             | Persistent | One per project, line and source              |
| `Funds(FundKey)`                            | Persistent | One per project and source                    |
| `Receipt(hash)`                             | Persistent | The proposal that used the document           |

TTL policy and archival: [Storage and TTL](storage-and-ttl.md).

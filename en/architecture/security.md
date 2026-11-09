# Security

> Status: pre-release, **testnet only**. The contract has had an **internal review**, not an
> independent audit.

## Reviews

| Date | Scope | Type | Report |
|---|---|---|---|
| 2026-11-07 | `budget-treasury` v0.3, `truway-common`, build and CI; fixes in v0.4 | Internal | [Report](https://github.com/truway-xyz/soroban-contracts/blob/main/audits/2026-11-07-budget-treasury-internal-review.md) |
| 2026-06-30 | Legacy contracts | Internal | [Report](https://github.com/truway-xyz/soroban-contracts/blob/main/audits/2026-06-30-internal-review.md) |
| Planned | `budget-treasury` before mainnet | Independent | |

## Findings of the last review

| ID | Severity | Status | Finding |
|---|---|---|---|
| BT-01 | High | Fixed | A treasury could be created locked |
| BT-02 | Medium | Fixed | Unbounded member list in instance storage |
| BT-03 | Low | Fixed | Membership proposals validated only at execution |
| BT-04 | Low | Fixed | Event conformance with the standard not tested |
| BT-05 | Info | Fixed | SDK behind the network protocol, deprecated upgrade call |
| BT-06 | Info | Fixed | Tooling drift: CLI versions, stub scripts |
| BT-07 | Medium | Open, planned | One admin approver is enough for membership and code changes |
| BT-08 | Low | Open, planned | Proposals never expire |
| BT-09 | Low | Open, planned | No pause |
| BT-10 | Info | Accepted | Anyone can fund under any funding source label |
| BT-11 | Info | Accepted | The asset code is given at construction |
| BT-12 | Info | Accepted | An expense paid outside the ledger is attested by two members, not proven |
| BT-13 | Info | Open | The upgrade path is not exercised by unit tests |
| BT-14 | Info | Documented | One member can veto any proposal they could decide |
| BT-15 | Medium | Fixed | The declared testnet instance ran v0.3 |
| BT-16 | Low | In progress | Builds were not verifiable by explorers |

## What the design rules out

| Class | How |
|---|---|
| Missing authorisation | `require_auth()` on every state-changing call by the acting member |
| Reinitialisation | Atomic `__constructor`; it cannot run again, even on upgrade |
| Self-approval | Checked on every approval (`SelfApproval = 2`) |
| Locked treasury | At least two distinct admins at construction; quorum checked on every membership change |
| Overspending | `paid <= budget` per line; payments within each source's funds |
| Reused documents | `Receipt(hash)` entry per used document, never read as absent after archival |
| Arithmetic overflow | `overflow-checks = true` in the release profile |
| Cross-organisation access | One instance per organisation |
| Cross-contract reentrancy | Blocked by the Soroban host |

## Quality gate

Every change to the contracts runs `rustfmt`, `clippy` with warnings as errors, the unit tests
(including event conformance with the standard), the WASM build, a check that the WASM declares
`event_schema = proof-of-spend/1`, and a check that the committed TypeScript bindings match the
contract. `main` requires a pull request, one approval and these checks.

## Threat model and monitoring

A threat model covering contracts, keys and the platform, and a monitoring plan built on the
events, are planned. Alerts will fire on unexpected `member_added`, `contract_upgraded` and failed
submissions.

## Reporting a vulnerability

Do not open a public issue. Follow
[SECURITY.md](https://github.com/truway-xyz/soroban-contracts/blob/main/SECURITY.md).

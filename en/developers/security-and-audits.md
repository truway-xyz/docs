---
description: "Security reviews, findings and how to report a vulnerability."
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

# Security and audits

{% hint style="warning" %}
`budget-treasury` has had an internal review, not an independent audit. It runs on testnet only.
{% endhint %}

## Reviews

| Date | Scope | Type | Report |
|---|---|---|---|
| 2026-11-07 | `budget-treasury` v0.3, `truway-common`, build and CI; fixes in v0.4 | Internal | [View](https://github.com/truway-xyz/soroban-contracts/blob/main/audits/2026-11-07-budget-treasury-internal-review.md) |
| 2026-06-30 | Earlier contracts | Internal | [View](https://github.com/truway-xyz/soroban-contracts/blob/main/audits/2026-06-30-internal-review.md) |
| Before mainnet | `budget-treasury` | Independent | Planned |

## Findings of the last review

| ID | Severity | Status | Finding |
|---|---|---|---|
| BT-01 | High | Fixed | A treasury could be created locked |
| BT-02 | Medium | Fixed | Unbounded member list in instance storage |
| BT-03 | Low | Fixed | Membership proposals validated only at execution |
| BT-04 | Low | Fixed | Event conformance with the standard not tested |
| BT-05 | Info | Fixed | SDK behind the network protocol |
| BT-06 | Info | Fixed | Tooling version drift |
| BT-07 | Medium | Planned | One admin approver is enough for members and code |
| BT-08 | Low | Planned | Proposals never expire |
| BT-09 | Low | Planned | No pause |
| BT-10 | Info | Accepted | Anyone can fund under any funding source label |
| BT-11 | Info | Accepted | The asset code is given at construction |
| BT-12 | Info | Accepted | An off-ledger expense is attested by two members, not proven |
| BT-13 | Info | Open | The code swap is not covered by unit tests |
| BT-14 | Info | Documented | One member can veto any proposal they could decide |
| BT-15 | Medium | Fixed | The declared testnet instance ran v0.3 |
| BT-16 | Low | In progress | Builds were not verifiable by explorers |

## Controls in the design

| Risk | Control |
|---|---|
| Missing authorization | `require_auth()` on every state-changing call |
| Reinitialization | Atomic `__constructor` that never runs again |
| Self-approval | Checked on every approval (`SelfApproval`) |
| Locked treasury | Two distinct admins at construction and quorum on every membership change |
| Overspending | `paid <= budget` per line and payments within each source's funds |
| Reused documents | A `Receipt(hash)` entry that is never read as absent |
| Overflow | `overflow-checks = true` in the release profile |
| Cross-organization access | One instance per organization |

## Quality gate

Every change runs `rustfmt`, `clippy` with no warnings, the tests (including event conformance), the WASM build, the `event_schema` meta check and the TypeScript bindings comparison. `main` requires a pull request, one approval and these checks.

## Reporting a vulnerability

Do not open a public issue. Follow [SECURITY.md](https://github.com/truway-xyz/soroban-contracts/blob/main/SECURITY.md).

---
description: "Verify a record directly on the ledger with the Stellar CLI."
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

# Verify a record

This guide verifies a record without Truway. For verification in the browser, see [Verify an expense](../guides/verify-an-expense.md).

<figure><img src="../.gitbook/assets/verify-record.svg" alt="Check the contract meta, the WASM hash against the release, the event with getEvents, the document fingerprint against receipt_hash, receipt_use and the proposal."><figcaption><p>Verification steps</p></figcaption></figure>

## 1. The contract

```bash
stellar contract info meta --contract-id <CONTRACT_ID> --network testnet
# event_schema = proof-of-spend/1
```

Compare the WASM hash with the one in [Deployment](deployment.md) and with the release attestation on GitHub.

## 2. The event

```bash
curl -s https://soroban-testnet.stellar.org -H 'content-type: application/json' -d '{
  "jsonrpc": "2.0", "id": 1, "method": "getEvents",
  "params": {
    "startLedger": <LEDGER>,
    "filters": [{ "type": "contract", "contractIds": ["<CONTRACT_ID>"],
                  "topics": [["AAAADwAAABBleHBlbnNlX3JlY29yZGVk", "*"]] }]
  }
}'
```

The first topic is `expense_recorded` as a base64 `ScVal`. For other events: `stellar xdr encode --type ScVal`. RPC keeps events for about 7 days.

## 3. The supporting document

```bash
shasum -a 256 invoice.pdf     # compare with receipt_hash
stellar contract invoke --id <CONTRACT_ID> --network testnet -- receipt_use --receipt_hash <HASH>
```

`receipt_use` returns the proposal that used the document.

## 4. The approvals

The event carries `proposer` and `approver`, always different. `proposal(id)` returns the full proposal with its dates.

## Results

| Result | Meaning |
|---|---|
| Fingerprint matches, meta declared, WASM matches the source | The record is authentic and was produced by the published rules |
| Fingerprint differs | It is not the approved file |
| No `event_schema` meta | The contract does not follow Proof of Spend; ignore its events |
| Entry archived | Simulation restores it, or read the event from an indexer |

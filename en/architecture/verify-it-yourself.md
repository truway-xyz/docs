# Verify it yourself

Three ways to check a record, from no tools at all to the command line. None needs an account, a
permission or Truway's servers, except the first.

## 1. The explorer (no tools)

> Status: **Live on testnet**.

Open `https://app.truway.xyz/proof/<code>` with the verification code of the expense. You see, in
plain language, the amount, the budget line and its account code, the funding source, who
proposed and who approved it, and the link **View on Stellar** to the same record on a block
explorer. Drop the invoice file on the page: your browser computes its SHA-256 and compares it
with the one on the ledger. The file never leaves your browser.

This path trusts Truway's index. The other two do not.

## 2. A block explorer and the public API

Every record links to its transaction on [Stellar Expert](https://stellar.expert/explorer/testnet).
There you can read the event, its fields and both signers. Truway's index is also public:

```bash
# One record by its verification code
curl https://api.truway.xyz/public/proof/<code>

# Execution of a programme, and its general ledger as CSV
curl https://api.truway.xyz/public/proof/programs/<programme-id>
curl "https://api.truway.xyz/public/proof/programs/<programme-id>/ledger?format=csv"
```

## 3. The ledger, with the Stellar CLI

**Check the contract.**

```bash
stellar contract info meta --contract-id <CONTRACT_ID> --network testnet
# expect: event_schema = proof-of-spend/1
```

Compare its WASM hash with the one in [Deployments](deployments.md), and rebuild that commit (or
check its GitHub attestation) to confirm the hash matches the source.

**Find the record.** Each record is an event. Query events of the contract by name:

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

The first topic is the event name `expense_recorded` as a base64 `ScVal` symbol (encode others
with `stellar xdr encode --type ScVal`); `*` matches any project. RPC keeps events for about 7
days: for older records, use an indexer or a history archive ([Events and indexing](events-and-indexing.md)).

**Check the document.**

```bash
shasum -a 256 invoice.pdf          # compare with receipt_hash in the event
stellar contract invoke --id <CONTRACT_ID> --network testnet -- receipt_use --receipt_hash <HASH>
# returns the proposal that used it: the document backs exactly one record in this treasury
```

**Check the approvals.** The event carries `proposer` and `approver`, always two different
addresses. `proposal(id)` returns the full proposal with when it was created and decided.

## Reading the result

| Result | Meaning |
|---|---|
| Hash matches, schema declared, WASM matches the source | The record is authentic and was produced by the published rules |
| Hash differs | The file is not the one that was approved (or it is another copy of the same invoice: see [Trust model](trust-model.md)) |
| No `event_schema` meta | The contract does not claim to follow Proof of Spend; ignore its events |
| Entry archived | Simulation restores it automatically, or read the event from an indexer |

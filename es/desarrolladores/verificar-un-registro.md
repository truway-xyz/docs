---
icon: terminal
description: "Verifica un registro directamente en el ledger con la CLI de Stellar."
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

# Verificar un registro

Esta guía verifica un registro sin pasar por Truway. Para la verificación desde el navegador, ver [Verificar un gasto](../guias/verificar-un-gasto.md).

## 1. El contrato

```bash
stellar contract info meta --contract-id <CONTRACT_ID> --network testnet
# event_schema = proof-of-spend/1
```

Compara el hash del WASM con el de [Despliegue](despliegue.md) y con la atestación del release en GitHub.

## 2. El evento

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

El primer tema es `expense_recorded` como `ScVal` en base64. Para otros eventos: `stellar xdr encode --type ScVal`. El RPC guarda eventos unos 7 días.

## 3. El soporte

```bash
shasum -a 256 factura.pdf     # compara con receipt_hash
stellar contract invoke --id <CONTRACT_ID> --network testnet -- receipt_use --receipt_hash <HASH>
```

`receipt_use` devuelve la propuesta que usó el soporte.

## 4. Las aprobaciones

El evento trae `proposer` y `approver`, siempre distintos. `proposal(id)` devuelve la propuesta completa con sus fechas.

## Resultados

| Resultado | Significado |
|---|---|
| Huella coincide, metadata declarada, WASM igual al código | El registro es auténtico y lo produjeron las reglas publicadas |
| Huella distinta | No es el archivo que se aprobó |
| Sin metadata `event_schema` | El contrato no sigue Proof of Spend; ignora sus eventos |
| Entrada archivada | La simulación la restaura, o lee el evento de un indexador |

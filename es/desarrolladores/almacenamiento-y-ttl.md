---
description: "Política de TTL, archivo y restauración de las entradas del contrato."
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

# Almacenamiento y TTL

Cada entrada del almacenamiento tiene un tiempo de vida (TTL). Cuando vence, la entrada se archiva, no se borra.

## Política

Definida en [`packages/common/src/ttl.rs`](https://github.com/truway-xyz/soroban-contracts/blob/main/packages/common/src/ttl.rs):

| Constante | Valor |
|---|---|
| `BUMP_THRESHOLD` | 30 días (518.400 ledgers) |
| `BUMP_TO` | 120 días (2.073.600 ledgers) |

Cada escritura extiende la entrada que toca y la instancia del contrato, lo que también extiende el código. Las lecturas no extienden nada.

## Entradas archivadas

Desde el protocolo 23, una entrada archivada se restaura sola cuando una transacción la necesita: la simulación agrega la restauración y quien envía paga la renta. Una entrada archivada **nunca se lee como ausente**, así que un soporte usado no se puede reutilizar aunque su entrada `Receipt` esté archivada.

Para mantener una entrada viva sin escribir:

```bash
stellar contract extend --id <CONTRACT_ID> --key-xdr <KEY> --durability persistent --ledgers-to-extend 2073600
```

## Cambios de almacenamiento

En un contrato desplegado, las variantes de `DataKey` nunca se renombran, reordenan ni eliminan sin una migración. Los campos nuevos se agregan como `Option<T>`: desde `soroban-sdk` 28, un campo opcional ausente se lee como `None`.

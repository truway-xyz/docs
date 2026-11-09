---
description: "Lista de conformidad para implementar Proof of Spend en otro contrato o sistema."
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

# Implementar el estándar

## Lista de conformidad

**Declaración**

- [ ] El WASM declara `event_schema = proof-of-spend/1` en su metadata. En Rust: `contractmeta!(key = "event_schema", val = "proof-of-spend/1")`.

**Eventos**

- [ ] Emite cada evento de la sección 5 de la [especificación](especificacion.md) con su nombre, temas y campos exactos.
- [ ] Emite `contract_upgraded` **antes** de reemplazar el código.
- [ ] Documenta cómo codifica los campos opcionales: desde `soroban-sdk` 28, los eventos en formato mapa omiten los campos vacíos.

**Invariantes**

- [ ] Todo cambio de presupuesto, gasto y pago necesita dos miembros distintos.
- [ ] `paid <= budget` en cada rubro, siempre.
- [ ] Cada gasto se carga a un solo rubro.
- [ ] Cada gasto lleva un `receipt_hash` distinto de cero, usado una sola vez por contrato.
- [ ] Cada gasto se asienta en el `chart` de su rubro.
- [ ] El contrato nunca se queda sin miembros suficientes para aprobar.
- [ ] Todo valor es mayor que cero.

**Privacidad**

- [ ] Ningún evento lleva datos personales.

## Pruebas

`budget-treasury` compara cada evento con el estándar en `events_follow_the_standard` y `governance_events_follow_the_standard` ([`test.rs`](https://github.com/truway-xyz/soroban-contracts/blob/main/contracts/budget-treasury/src/test.rs)). Copia ese enfoque: un campo renombrado rompe a todos los lectores sin avisar.

## Agregar un plan de cuentas

El registro de planes es la sección 8 de la especificación (`CO_PUC`, `CO_CGN`, `PE_PCGE`, `MX_SAT`, `BR_SPED`, `SV_NIIF`, `IFRS`). Para agregar uno, abre un pull request contra [`docs/proof-of-spend.md`](https://github.com/truway-xyz/soroban-contracts/blob/main/docs/proof-of-spend.md).

## Versiones

Los cambios incompatibles producen un identificador nuevo (`proof-of-spend/2`). La información nueva llega como eventos nuevos, nunca cambiando campos existentes. Los comentarios sobre el borrador van como [issue en `soroban-contracts`](https://github.com/truway-xyz/soroban-contracts/issues).

---
icon: receipt
description: "El estándar abierto de ejecución presupuestal sobre Stellar que implementa Truway."
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

# Proof of Spend

**Un pago prueba que el dinero se movió. Proof of Spend prueba qué compró.**

Proof of Spend (`proof-of-spend/1`) es un estándar abierto de ejecución presupuestal sobre Stellar. Un contrato que lo implementa registra, por cada gasto o pago, contra qué rubro, de qué financiador, en qué cuenta contable, con qué soporte y quién lo aprobó.

| | |
|---|---|
| Identificador | `proof-of-spend/1` |
| Versión | Borrador 2, 2026-11-07 |
| Licencia | Apache-2.0 |
| Implementación de referencia | [`budget-treasury`](../desarrolladores/budget-treasury.md) |
| Fuente | [`soroban-contracts/docs/proof-of-spend.md`](https://github.com/truway-xyz/soroban-contracts/blob/main/docs/proof-of-spend.md) |

## Qué cubre

* Rubros por proyecto y fuente de financiación, con cuenta contable y moneda.
* Gastos pagados fuera de la red y pagos hechos en ella, con su cuenta y la huella de su soporte.
* La aprobación de dos personas detrás de cada cambio.
* El dinero en la red, separado por fuente.

Todavía no cubre la contratación, los pagos a beneficiarios individuales ni los hitos de impacto.

## Conformidad

Un contrato cumple `proof-of-spend/1` cuando:

1. declara `event_schema = proof-of-spend/1` en su metadata (`contractmetav0`);
2. emite los eventos del estándar con sus nombres, temas y campos exactos;
3. hace cumplir todas sus invariantes.

## Invariantes

1. Cada cambio de presupuesto, gasto y pago lo propone un miembro y lo aprueba otro.
2. Los cambios de miembros y de código los aprueba un administrador.
3. Ningún rubro gasta más que su presupuesto.
4. Cada gasto se carga a un solo rubro.
5. Todo gasto lleva soporte, y un soporte respalda como máximo un gasto por contrato.
6. Todo gasto se asienta en el plan de cuentas de su rubro.
7. La tesorería siempre conserva miembros suficientes para aprobar.
8. Todo valor es positivo.

## Siguiente

* [Especificación](especificacion.md)
* [Leer el registro](leer-el-registro.md)
* [Implementar el estándar](implementar.md)

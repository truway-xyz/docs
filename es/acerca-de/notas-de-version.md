---
description: "Versiones del estándar, del contrato y de la plataforma."
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

# Notas de versión

## Noviembre de 2026

### Proof of Spend · borrador 2

* El estándar pasa a llamarse Proof of Spend (`proof-of-spend/1`).
* Rubros por fuente de financiación, con moneda.
* `expense_recorded` para gastos pagados fuera de la red.
* `proposal_executed` y `contract_upgraded`.
* Soporte obligatorio en todo gasto.

### budget-treasury 0.4.0

* Exige dos administradores distintos al crearse.
* Máximo de 32 miembros.
* Valida las propuestas de miembros al proponerlas.
* Pruebas de conformidad de eventos con el estándar.
* `soroban-sdk` 29.0.1 (protocolo 29).
* Desplegado en testnet. Ver [Despliegue](../desarrolladores/despliegue.md).

### Plataforma

* Presupuesto por rubro con cuenta del PUC y financiador.
* Anticipos a equipos con doble aprobación.
* Captura por WhatsApp con selección de rubro.
* Explorador público de gastos y verificación de facturas en el navegador.
* Tablero público del programa y libro diario en CSV.

{% hint style="info" %}
Las donaciones en USDC están construidas, pero fuera del alcance actual.
{% endhint %}

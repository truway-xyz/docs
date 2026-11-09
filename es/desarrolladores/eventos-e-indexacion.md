---
icon: bolt
description: "Los eventos de Proof of Spend y cómo se indexan."
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

# Eventos e indexación

| Evento | Temas | Cuándo |
|---|---|---|
| `budget_set` | `project` | Se crea o cambia un rubro |
| `expense_recorded` | `project` | Se registra un gasto pagado fuera de la red |
| `payment_executed` | `project` | Sale un pago de la tesorería |
| `project_funded` | `project` | Entra dinero para un proyecto y una fuente |
| `proposal_created` | `id` | Un miembro abre una propuesta |
| `proposal_executed` | `id` | Se aprueba y ejecuta una propuesta |
| `proposal_rejected` | `id` | Se rechaza o retira una propuesta |
| `member_added` | `member` | Se agrega un miembro o cambia su rol |
| `member_removed` | `member` | Se quita un miembro |
| `contract_upgraded` | `proposal_id` | Justo antes de reemplazar el código |

El primer tema es el nombre del evento como `Symbol`; los datos son un mapa con los demás campos. Los campos exactos están en la [especificación](../proof-of-spend/especificacion.md).

{% hint style="info" %}
Desde `soroban-sdk` 28, los eventos en formato mapa omiten los campos vacíos. Hoy ningún evento de Proof of Spend tiene campos opcionales; si una versión futura los agrega, una clave ausente se lee como vacía.
{% endhint %}

## Retención

Los proveedores de RPC guardan eventos unos **7 días**. El estado actual de cada rubro siempre se puede leer del contrato (`line`, `funds`, `receipt_use`, `proposal`).

## Indexador de Truway

Cada 15 segundos, un trabajo de la cola `treasury-ops` lee los eventos nuevos de cada tesorería desde su último cursor y los guarda en `treasury_events`. Corre una sola vez aunque haya varias instancias de la API. Con esos eventos se arman el explorador, el tablero y el libro diario. Ver [API pública](api-publica.md).

## Indexar por tu cuenta

| Opción | Para qué |
|---|---|
| `getEvents` del RPC con filtro por contrato y un cursor | Un lector pequeño y continuo |
| Indexadores de terceros ([directorio](https://developers.stellar.org/docs/data/indexers)) | Consultas sin operar infraestructura |
| Galexie o el data lake público de Stellar | Historia completa, sin depender de un proveedor |
| Hubble (BigQuery) | Análisis sobre la historia |

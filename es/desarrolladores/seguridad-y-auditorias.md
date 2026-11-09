---
description: "Revisiones de seguridad, hallazgos y cómo reportar una vulnerabilidad."
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

# Seguridad y auditorías

{% hint style="warning" %}
`budget-treasury` tuvo una revisión interna, no una auditoría independiente. Solo corre en testnet.
{% endhint %}

## Revisiones

| Fecha | Alcance | Tipo | Informe |
|---|---|---|---|
| 2026-11-07 | `budget-treasury` v0.3, `truway-common`, build y CI; correcciones en v0.4 | Interna | [Ver](https://github.com/truway-xyz/soroban-contracts/blob/main/audits/2026-11-07-budget-treasury-internal-review.md) |
| 2026-06-30 | Contratos anteriores | Interna | [Ver](https://github.com/truway-xyz/soroban-contracts/blob/main/audits/2026-06-30-internal-review.md) |
| Antes de mainnet | `budget-treasury` | Independiente | Planeada |

## Hallazgos de la última revisión

| ID | Severidad | Estado | Hallazgo |
|---|---|---|---|
| BT-01 | Alta | Corregido | Una tesorería podía crearse bloqueada |
| BT-02 | Media | Corregido | Lista de miembros sin límite en el almacenamiento de instancia |
| BT-03 | Baja | Corregido | Las propuestas de miembros solo se validaban al ejecutarse |
| BT-04 | Baja | Corregido | No se probaba la conformidad de los eventos con el estándar |
| BT-05 | Info | Corregido | SDK detrás del protocolo de la red |
| BT-06 | Info | Corregido | Versiones de herramientas desalineadas |
| BT-07 | Media | Planeado | Un administrador aprobador basta para miembros y código |
| BT-08 | Baja | Planeado | Las propuestas no vencen |
| BT-09 | Baja | Planeado | No hay pausa |
| BT-10 | Info | Aceptado | Cualquiera puede fondear bajo cualquier etiqueta de fuente |
| BT-11 | Info | Aceptado | El código del activo se pasa al crear la tesorería |
| BT-12 | Info | Aceptado | Un gasto pagado fuera de la red queda atestado por dos miembros, no probado |
| BT-13 | Info | Abierto | La actualización de código no está cubierta por pruebas unitarias |
| BT-14 | Info | Documentado | Un miembro puede vetar cualquier propuesta que podría decidir |
| BT-15 | Media | Corregido | La instancia declarada en testnet corría la v0.3 |
| BT-16 | Baja | En curso | Los builds no eran verificables por los exploradores |

## Controles en el diseño

| Riesgo | Control |
|---|---|
| Falta de autorización | `require_auth()` en cada llamada que cambia estado |
| Reinicialización | `__constructor` atómico que no vuelve a correr |
| Autoaprobación | Revisada en cada aprobación (`SelfApproval`) |
| Tesorería bloqueada | Dos administradores distintos al crearla y quórum en cada cambio de miembros |
| Gasto excedido | `paid <= budget` por rubro y pagos dentro de los fondos de cada fuente |
| Soporte reutilizado | Entrada `Receipt(hash)` que nunca se lee como ausente |
| Desbordamiento | `overflow-checks = true` en el perfil de release |
| Acceso entre organizaciones | Una instancia por organización |

## Control de calidad

Cada cambio pasa por `rustfmt`, `clippy` sin advertencias, las pruebas (incluida la conformidad de eventos), el build del WASM, la revisión de la metadata `event_schema` y la comparación de los bindings de TypeScript. `main` exige pull request, una aprobación y estos controles.

## Reportar una vulnerabilidad

No abras un issue público. Sigue [SECURITY.md](https://github.com/truway-xyz/soroban-contracts/blob/main/SECURITY.md).

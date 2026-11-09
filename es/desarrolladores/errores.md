---
icon: triangle-exclamation
description: "Códigos de error de budget-treasury."
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

# Errores

Los códigos son parte de la interfaz pública y nunca se renumeran.

| Código | Nombre | Cuándo |
|---:|---|---|
| 1 | `Unauthorized` | Quien llama no es miembro, o su rol no puede hacerlo |
| 2 | `SelfApproval` | Quien aprueba es quien propuso |
| 3 | `NotFound` | Propuesta o miembro desconocido |
| 4 | `InvalidAmount` | Valor cero o negativo |
| 5 | `BudgetExceeded` | El gasto no cabe en lo que queda del rubro |
| 6 | `InsufficientFunds` | La fuente no tiene fondos suficientes para el proyecto |
| 7 | `InvalidState` | La propuesta ya no está pendiente |
| 8 | `LineNotFound` | El rubro no existe |
| 9 | `BudgetBelowPaid` | El presupuesto no puede quedar por debajo de lo ejecutado |
| 10 | `ChartMismatch` | El gasto usa un plan de cuentas distinto al del rubro |
| 11 | `QuorumLost` | El cambio dejaría la tesorería sin administrador o sin dos aprobadores; también al crearla con menos de dos administradores distintos |
| 12 | `NoAdmins` | El constructor recibió una lista de administradores vacía |
| 13 | `ReceiptAlreadyUsed` | El soporte ya respalda otro registro |
| 14 | `ReceiptRequired` | Falta el soporte |
| 15 | `CurrencyMismatch` | La moneda no coincide con el rubro o con el activo de la tesorería |
| 16 | `TooManyMembers` | Más de 32 miembros |

En una simulación fallida aparecen como `Error(Contract, #13)`.

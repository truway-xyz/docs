---
icon: star
description: "Qué aporta Stellar a Truway y qué no se mueve por Stellar."
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

# Stellar en Truway

| Necesidad | Lo que aporta Stellar |
|---|---|
| Un registro que no controla ninguna de las partes | Ledger público: una aprobación escrita no se puede cambiar ni borrar |
| La supervisión del contrato escrita en las reglas | Contratos Soroban con `require_auth` por persona y rechazo de la autoaprobación |
| Una factura, una sola vez, entre organizaciones | Un registro compartido que consulta cada tesorería (próximamente) |
| Prueba de qué compró el dinero | Un evento estándar por gasto con rubro, cuenta y huella del soporte |
| Muchos registros pequeños a bajo costo | Comisiones bajas y predecibles |
| Registros en firme en segundos | Ledgers de unos 5 segundos, sin reorganizaciones |
| Dólares donde llega la cooperación | USDC de Circle, usable desde contratos por su Stellar Asset Contract |

<figure><img src="../.gitbook/assets/arquitectura-stellar.png" alt="Arquitectura en Stellar. Los miembros firman su entrada de autorización con Privy; la API envía la invocación firmada y la cuenta remitente de Truway paga la comisión a través del RPC. Cada organización tiene su instancia de budget-treasury, desplegada desde el WASM 0.4.0 por una cuenta de un solo uso; el WASM está atestado en un release de GitHub que leen Stellar Expert y Stellar Lab. Los contratos emiten eventos Proof of Spend al ledger, que lee el indexador y cualquier lector. Próximamente: USDC hacia la Stellar Disbursement Platform, un anchor a pesos y un registro compartido de soportes."><figcaption><p>Arquitectura en Stellar: contratos, cuentas e integraciones</p></figcaption></figure>

## Dinero público en pesos

El dinero público colombiano sale en pesos de la tesorería de cada entidad y llega por transferencia bancaria. Para ese dinero, Truway registra la prueba del pago con `RecordExpense`; Stellar no es el riel del pago.

El dinero se mueve en Stellar donde ya llega en dólares, como la cooperación internacional que financia programas públicos. Ver [Activos y pagos](activos-y-pagos.md).

## Redes

| Red | Estado |
|---|---|
| Testnet | En uso. Ver [Despliegue](despliegue.md) |
| Mainnet | Después de una revisión de seguridad independiente |

---
icon: coins
description: "El activo de la tesorería, los pagos en la red y los rieles a pesos."
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

# Activos y pagos

## El activo de la tesorería

Cada tesorería guarda un activo, fijado al crearla (`token`, `token_symbol`). Sirve cualquier token SEP-41, incluido un activo clásico por su Stellar Asset Contract. La instancia de testnet usa USDC de Circle: `CBIELTK6YBZJU5UP2WWQEUCYKLPU6AUNZ2BQ4WWFEIE3USCIHMXQDAMA`.

Cada rubro tiene su moneda. Un rubro en `COP` registra gastos pagados en pesos fuera de la red; solo un rubro en el activo de la tesorería puede pagar con `Pay`.

## Referencias de pago

Las invocaciones de contrato exigen `MEMO_NONE`. Cuando un pago a un servicio externo necesita una referencia, va en una dirección *muxed* (`M...`).

## Rieles

| Riel | Para qué | Estándar | Disponibilidad |
|---|---|---|---|
| `fund` en USDC | Fondear la tesorería por fuente | SEP-41 | Construido en el contrato |
| Stellar Disbursement Platform | Pagar un anticipo aprobado a la líder del equipo, registrada por SEP-24 | SDP, SEP-24 | Próximamente |
| Anchor a pesos colombianos | Pasar de USDC a una cuenta bancaria o Bre-B | SEP-24, SEP-31 | Próximamente |

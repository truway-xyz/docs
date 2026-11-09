---
icon: arrow-up-from-bracket
description: "Cómo se actualiza el código de una tesorería y qué falta antes de mainnet."
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

# Actualizaciones del contrato

1. Se sube el nuevo WASM (`stellar contract upload`) y se obtiene su hash.
2. Un administrador propone `Upgrade(wasm_hash)`.
3. Otro administrador lo aprueba.
4. El contrato emite `contract_upgraded` y **después** reemplaza su código con `update_current_contract`.

Los eventos posteriores a `contract_upgraded` vienen del código nuevo. El contrato conserva su ID y su almacenamiento; el constructor no vuelve a correr.

## Reglas de compatibilidad

* Las variantes de `DataKey` no se renombran, reordenan ni eliminan sin migración.
* Los campos nuevos guardados son `Option<T>`.
* Los campos de los eventos no cambian; los cambios incompatibles llevan un identificador nuevo del estándar.
* Los códigos de error no se renumeran.

Cada organización controla las actualizaciones de su propia tesorería. Truway no usa referencias ejecutables (CAP-85).

## Pendiente antes de mainnet

| Pendiente | Hallazgo |
|---|---|
| Aprobación de varios administradores para miembros y código | BT-07 |
| Vencimiento de propuestas | BT-08 |
| Pausa que activa cualquier administrador y levantan dos | BT-09 |
| Timelock en las actualizaciones | BT-07 |
| Probar el cambio de código en testnet | BT-13 |

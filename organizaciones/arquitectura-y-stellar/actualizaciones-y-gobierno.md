# Actualizaciones y gobierno

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Upgrades and governance](https://github.com/truway-xyz/docs/blob/main/en/architecture/upgrades-and-governance.md).

El código de una tesorería se puede reemplazar: un administrador propone `Upgrade(wasm_hash)`, otro lo aprueba, y el contrato emite `contract_upgraded` **antes** de cambiar el código. Cada organización controla sus propias actualizaciones; Truway no usa referencias ejecutables (CAP-85).

Pendiente antes de la red principal: aprobación de varios administradores, espera obligatoria (timelock), vencimiento de propuestas y pausa.

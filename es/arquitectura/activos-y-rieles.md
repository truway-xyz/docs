# Activos, pagos y rieles

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Assets and rails](https://github.com/truway-xyz/docs/blob/main/en/architecture/assets-and-rails.md).

Cada tesorería guarda un activo, fijado al crearla; sirve cualquier token SEP-41, incluido un activo clásico por su Stellar Asset Contract. La instancia de testnet usa **USDC**. Los rubros llevan su propia moneda: uno en `COP` registra gastos pagados en pesos fuera de la red; solo uno en el activo de la tesorería puede pagar con `Pay`.

En la hoja de ruta: anticipos pagados por la Stellar Disbursement Platform (registro SEP-24) y salida a pesos con un anchor (SEP-24 o SEP-31). Las invocaciones de contrato exigen `MEMO_NONE`; las referencias de pago van en direcciones *muxed*.

# Verifícalo tú mismo

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Verify it yourself](https://github.com/truway-xyz/docs/blob/main/en/architecture/verify-it-yourself.md).

Tres caminos, sin cuenta ni permiso:

1. **El explorador:** `app.truway.xyz/proof/<código>`. Suelta la factura y tu navegador calcula su SHA-256 y la compara con la del registro. Este camino confía en el índice de Truway.
2. **Un explorador de bloques y la API pública:** cada registro enlaza a su transacción en Stellar Expert; `GET https://api.truway.xyz/public/proof/<código>`.
3. **El ledger, con la CLI de Stellar:** `stellar contract info meta` para confirmar `event_schema = proof-of-spend/1`; `getEvents` del RPC para encontrar el evento; `shasum -a 256` para comparar el soporte con `receipt_hash`; `receipt_use` para confirmar que respalda un solo registro.

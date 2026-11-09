# Ciclo de vida de un gasto

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Lifecycle](https://github.com/truway-xyz/docs/blob/main/en/architecture/lifecycle.md).

1. El equipo de campo paga y captura la factura en el momento del pago. La plataforma guarda el archivo y calcula su SHA-256.
2. Un miembro propone `RecordExpense` con rubro, fuente, valor, cuenta, `receipt_hash` y la huella (SHA-256) de las referencias del pago y del proveedor.
3. El contrato revisa el rol, que el soporte no se haya usado, que el rubro exista en el mismo plan de cuentas y que haya saldo.
4. Otro miembro aprueba. El contrato revisa todo de nuevo, suma el valor al rubro, marca el soporte como usado y emite `expense_recorded` y `proposal_executed`.
5. El indexador guarda los eventos y el explorador los muestra en lenguaje claro.

Los anticipos de caja menor hoy son una asignación aprobada por dos personas, legalizada con recibos. **Todavía no se mueve dinero en la red.**

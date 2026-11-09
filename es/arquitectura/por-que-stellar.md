# Por qué Stellar

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Why stellar](https://github.com/truway-xyz/docs/blob/main/en/architecture/why-stellar.md).

Truway no usa Stellar como base de datos. Lo usa para cuatro cosas que no da una base de datos de la alcaldía, del ejecutor o de Truway:

| Lo que necesita el sector público | Lo que da Stellar | Estado |
|---|---|---|
| Un registro que nadie controla, ni Truway | Un ledger público: una aprobación escrita no la cambia ni la borra nadie | En testnet |
| La supervisión del contrato escrita en las reglas | Contratos Soroban que exigen la autorización de cada persona y rechazan la autoaprobación | En testnet |
| Una factura, una sola vez, entre organizaciones y municipios | Un registro compartido que consulta el contrato de cada organización | En diseño |
| Prueba de qué compró el dinero, enlazada al pago | Un evento estándar por gasto con rubro, cuenta y huella del soporte | En testnet |

**Lo que no está en Stellar hoy:** el dinero público colombiano. Sale en pesos de la tesorería de cada entidad y llega por transferencia bancaria. Para ese dinero Truway registra la prueba del pago (`RecordExpense`); no es el riel del pago. El dinero sí puede moverse en Stellar donde ya llega en dólares: cooperación internacional y filantropía que financian programas.

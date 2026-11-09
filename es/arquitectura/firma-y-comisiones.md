# Firma y comisiones

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Signing and fees](https://github.com/truway-xyz/docs/blob/main/en/architecture/signing-and-fees.md).

Cada miembro autoriza solo su propio paso; Truway arma la transacción, paga la comisión y la envía, pero no puede cambiar lo que el miembro firmó ni firmar por él. **Hoy en testnet la plataforma custodia firmantes de demostración** mientras se construye la firma por persona.

En el diseño, el navegador firma con la llave de la persona (guardada por Privy, sin ventanas ni frases semilla) solo la entrada de autorización de su invocación, con vencimiento de unas 720 ledgers. Truway paga todas las comisiones: los miembros no necesitan XLM.

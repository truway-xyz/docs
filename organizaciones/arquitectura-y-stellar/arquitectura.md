# Arquitectura

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Overview](https://github.com/truway-xyz/docs/blob/main/en/architecture/overview.md).

Los miembros de cada organización proponen y aprueban presupuestos y gastos en su propio contrato `budget-treasury` en Stellar; la plataforma de Truway prepara esas transacciones y guarda los documentos; cualquiera lee el resultado. **Hoy ninguna capa mueve dinero público:** `RecordExpense` registra un gasto pagado por banco o en efectivo; `Pay` puede mover USDC que esté en el contrato, y solo en testnet.

| Capa | Qué hace | Quién la controla |
|---|---|---|
| Miembros (administradores, aprobadores, operadores) | Proponen y aprueban, cada uno con su llave | La organización |
| App de Truway y canal de WhatsApp | Capturan facturas, muestran presupuestos, piden aprobaciones | Truway |
| API de Truway | Arma cada transacción para quien debe firmarla, guarda documentos y su SHA-256, indexa eventos | Truway |
| `budget-treasury`, una instancia por organización | Hace cumplir las reglas: dos firmantes, límites del rubro, soporte de un solo uso, cuentas contables | Sus miembros; Truway la despliega pero nunca es miembro |
| Eventos de Proof of Spend | La interfaz pública | Nadie: están en el ledger |

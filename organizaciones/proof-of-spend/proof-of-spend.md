# Qué es Proof of Spend

**Un pago prueba que el dinero se movió. Proof of Spend prueba qué compró.**

Proof of Spend (`proof-of-spend/1`) es un estándar abierto de ejecución presupuestal sobre Stellar. Un contrato que lo sigue registra, en cada gasto o pago: contra qué rubro aprobado, de qué financiador, en qué cuenta contable, con qué soporte y quién lo aprobó. Cualquiera puede rehacer el informe de ejecución presupuestal o el libro diario a partir de sus eventos, sin entrar a la base de datos de la organización ni depender de su proveedor de software.

|                              |                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Identificador                | `proof-of-spend/1`                                                                                                             |
| Estado                       | Borrador 2, 2026-11-07                                                                                                         |
| Licencia                     | Apache-2.0                                                                                                                     |
| Implementación de referencia | [`budget-treasury`](../arquitectura-y-stellar/budget-treasury.md)                                                              |
| Fuente                       | [`soroban-contracts/docs/proof-of-spend.md`](https://github.com/truway-xyz/soroban-contracts/blob/main/docs/proof-of-spend.md) |

## Por qué un estándar y no otra plataforma

Los presupuestos públicos y las donaciones con destino específico los ejecutan muchas organizaciones en muchos sistemas. Financiadores, auditores, entes de control y ciudadanos no pueden comparar ni verificar la ejecución sin preguntarle a cada sistema. La interoperabilidad empieza por un formato común y público. Proof of Spend es ese formato para el paso de la ejecución.

## Qué cubre

**Cubre:** rubros por proyecto y fuente de financiación, cada uno con cuenta contable y moneda; gastos pagados fuera de la red y pagos hechos en ella, cada uno con su cuenta y la huella de su soporte; la aprobación de dos personas detrás de cada cambio; el dinero en la red, separado por fuente.

**Todavía no cubre:** la contratación, los pagos a beneficiarios individuales (necesitan divulgación selectiva), los hitos y el impacto.

## Cómo lo declara un contrato

1. Declara en su metadata `event_schema = proof-of-spend/1` (sección `contractmetav0` del Wasm).
2. Emite los eventos del estándar con sus nombres, temas y campos exactos.
3. Hace cumplir todas las invariantes del estándar.

Los lectores ignoran los eventos de contratos que no declaran la metadata.

## Las invariantes, en palabras simples

1. Cada cambio de presupuesto, gasto y pago lo propuso un miembro y lo aprobó otro.
2. Los cambios de miembros y de código los aprueba un administrador.
3. Ningún rubro gasta nunca más que su presupuesto.
4. Un gasto se carga a un solo rubro, así que el dinero de un financiador nunca paga el rubro de otro.
5. Todo gasto lleva soporte, y un soporte respalda como máximo un gasto por contrato.
6. Todo gasto se asienta en el plan de cuentas de su rubro.
7. La tesorería siempre conserva miembros suficientes para aprobar.
8. Todo valor es positivo.

Sigue con: [Especificación](especificacion.md) · [Leer el registro](leer-el-registro.md) · [Implementar el estándar](implementar.md).

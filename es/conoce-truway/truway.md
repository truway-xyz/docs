# Truway en una página

Truway hace trazables los pagos, su distribución y el impacto en la última milla. Empieza por el
dinero público que ejecutan terceros: una entidad firma un contrato, una organización lo ejecuta
en campo, y cualquiera puede comprobar cada gasto contra el rubro para el que se aprobó.

## Un recorrido, tres papeles

```
ENTIDAD PÚBLICA           firma el contrato y designa al supervisor         ← campeona, aprueba
      │
      ▼
ORGANIZACIÓN EJECUTORA    su equipo de campo captura cada factura;         ← usuaria diaria
      │                   su coordinador la propone contra un rubro
      ▼
EQUIPOS DE CAMPO Y        se les paga por transferencia o con anticipos de caja menor
PROVEEDORES
      │
      ▼
CUALQUIERA                veedurías, concejos, contralorías, ciudadanos    ← comprueban sin cuenta
```

Truway no distribuye subsidios a hogares ni maneja datos de beneficiarios. El recorrido es siempre
dinero → organización ejecutora → equipos de campo y proveedores.

## Cuatro preguntas sobre cada peso

Un movimiento solo cuenta cuando cada pregunta tiene una respuesta verificable.

| Pregunta | Cómo la responde Truway |
|---|---|
| **¿Quién participó?** | Quién propuso el gasto y quién lo aprobó: dos personas distintas, cada una con su rol |
| **¿A dónde fue el dinero?** | Qué contrato, qué rubro, qué fuente de financiación, qué proveedor |
| **¿Quién podía hacer qué?** | El rol de cada persona cuando actuó, impuesto por las reglas del registro y no por un ajuste en una app |
| **¿Qué tuvo que pasar antes de que contara?** | La aprobación de una segunda persona, un soporte nunca usado antes y saldo disponible en el rubro |

Las respuestas quedan en un registro público que no controla Truway, ni la entidad, ni la
organización ejecutora.

## Qué lo hace distinto

- **Siempre dos personas.** Quien propone un gasto no puede aprobarlo. La regla es parte del
  registro.
- **Una factura, una sola vez.** Un soporte no puede respaldar dos gastos de la misma organización.
  Comprobarlo entre organizaciones es lo siguiente ([Hoja de ruta](hoja-de-ruta.md)).
- **Como lo asentaría un contador.** Cada rubro y cada gasto llevan su cuenta del plan de cuentas,
  así que el informe de ejecución y el libro diario salen del registro.
- **Un estándar abierto, no una plataforma cerrada.** El registro sigue [Proof of Spend](../proof-of-spend/README.md),
  una especificación abierta que cualquier sistema puede implementar y cualquiera puede leer.

## Dónde está hoy

Construido y funcionando en la red de pruebas de Stellar con datos de demostración. Todavía no hay
un piloto con un contrato real: el detalle está en [Estado actual](estado-actual.md).

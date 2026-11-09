# Cómo funciona un expediente

Un expediente reúne todo lo de un contrato público: sus rubros, cada gasto con su factura, quién lo
propuso, quién lo aprobó y cuánto queda. Esta página sigue un contrato de principio a fin.

## Las personas

| Quién | Su papel en el expediente |
|---|---|
| **Supervisor** (entidad pública) | Aprueba rubros y gastos |
| **Coordinador** (organización ejecutora) | Propone cada gasto contra un rubro |
| **Equipo de campo** | Manda la foto de cada factura o recibo desde su celular |
| **Cualquiera** (veeduría, concejo, contraloría, ciudadano) | Lee el expediente y comprueba cualquier gasto |

## Paso a paso

| # | Qué pasa | Estado |
|---|---|---|
| 1 | El contrato se vincula por su ID de SECOP II; entidad, contratista, valor, fechas, supervisor y fuente se llenan solos | En diseño. Hoy el contrato se carga a mano |
| 2 | Se cargan los rubros del plan de inversión, cada uno con su cuenta contable y su fuente. **Una segunda persona los aprueba**, y desde ahí no pueden cambiar en silencio | En testnet |
| 3 | Se asigna un anticipo de caja menor a un equipo, y una segunda persona lo aprueba | En testnet |
| 4 | El equipo le paga a un proveedor y manda la foto de la factura por WhatsApp. El asistente lee el valor, el proveedor y la fecha, y pregunta a qué rubro pertenece | En testnet |
| 5 | El coordinador la revisa y la propone en el rubro | En testnet |
| 6 | Otra persona la aprueba. Quien la propuso no puede aprobarla | En testnet |
| 7 | Si la factura ya se usó en otro gasto, se rechaza | En testnet dentro de la misma organización; entre organizaciones, en diseño |
| 8 | El gasto aparece en el expediente público con su código de verificación | En testnet |
| 9 | El informe de ejecución por rubro y por fuente, y el libro diario, salen directamente del expediente | En testnet |

## Por qué importa cada paso

- **Siempre dos personas.** Es la supervisión del contrato escrita en las reglas del registro, no un
  ajuste que alguien pueda apagar.
- **Una factura, una sola vez.** Ninguna factura respalda dos gastos de la misma organización, y la
  comprobación entre organizaciones es lo siguiente.
- **Se captura cuando se paga.** La factura llega en el momento del gasto, no semanas después cuando
  hay que entregar el informe.
- **Nada que instalar.** WhatsApp funciona en cualquier celular, y eso pesa en municipios con poca
  conectividad.

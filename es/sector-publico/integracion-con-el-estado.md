# Integración con el Estado

Los funcionarios pidieron *"un sistema interoperable que articule formulación, asignación
presupuestal, contratación, ejecución y evaluación"* de los proyectos con recursos públicos.
Truway cubre la **ejecución**. Esta página muestra con qué se conecta antes y después, y en qué
estado está cada conexión.

**Truway lee, exporta o publica. Nunca escribe en un sistema del Estado.**

| Sistema | Quién lo opera | Qué hace Truway con él | Dirección | Estado |
|---|---|---|---|---|
| **SECOP II** (datos abiertos) | Colombia Compra Eficiente | Trae el contrato por su ID: entidad, contratista, objeto, valor, fechas, supervisor, fuente de los recursos, facturado y pagado | Lee | En diseño. La fuente de datos abiertos se probó; la conexión no está construida |
| **Conciliación con SECOP II** | | Compara lo que el portal reporta como pagado con lo que el expediente tiene aprobado | Lee | En diseño |
| **SECOP I** | Colombia Compra Eficiente | Los municipios que siguen en el portal anterior | Lee | En la hoja de ruta |
| **Factura electrónica** | DIAN | Lee de la foto o del PDF el NIT del emisor, la razón social, la fecha, el total y el CUFE | Lee el documento | Lectura en el asistente de WhatsApp. Validación automática contra la DIAN: en la hoja de ruta |
| **Bancos y Bre-B** | Bancos, Banco de la República | Enlaza el comprobante de la transferencia al gasto como evidencia del pago | Lee | Campo disponible; el flujo en la app está por confirmar |
| **Proyectos de inversión** (BPIN) | DNP | El expediente puede citar el proyecto que financia el contrato | Referencia | En la hoja de ruta |
| **Fuentes de financiación** (PGN, SGP, regalías, propios, cooperación) | DNP, Minhacienda, la entidad | Cada rubro lleva su fuente | Clasifica | En testnet como texto libre; catálogo oficial: en diseño |
| **Ejecución presupuestal de la entidad** | Minhacienda, la entidad | El informe de ejecución por rubro sirve de soporte al supervisor | Exporta | En la hoja de ruta |
| **Contabilidad pública y rendición a contralorías** | Contaduría General, contralorías | Exportaciones que le ahorran trabajo al ejecutor y al supervisor | Exporta | En la hoja de ruta; formatos por confirmar |
| **Software contable del ejecutor** (Siigo, Alegra, World Office y otros) | El ejecutor | Libro diario en CSV o JSON | Exporta | En testnet |
| **Datos abiertos y control social** | La ciudadanía | Expediente público y descargas | Publica | En testnet |
| **WhatsApp Business** | Meta | Canal de captura, no el producto | Recibe | Con un número de prueba |

## Por qué en este orden

El contrato ya existe en SECOP II, así que Truway debe traerlo y no pedirle a nadie que lo vuelva a
escribir. La contabilidad del ejecutor ya existe, así que Truway exporta hacia ella. Lo que no
existía es el paso del medio: la prueba de qué compró el dinero, aprobada por dos personas y
abierta a todos.

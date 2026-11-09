# Plan de cuentas y presupuesto

En el gasto público colombiano conviven cuatro clasificaciones que es fácil confundir. Truway pone
cada una en su lugar.

| Clasificación | Quién la usa | En Truway | Estado |
|---|---|---|---|
| **PUC** (Plan Único de Cuentas) | Empresas; las ESAL lo usan como catálogo de referencia | Cada rubro y cada gasto llevan una cuenta del PUC, por ejemplo `5135` | Catálogo base de cuentas de cuatro dígitos; las subcuentas de seis y ocho dígitos se aceptan bajo su cuenta. Pendiente la revisión de un contador público |
| **Catálogo General de Cuentas** de la Contaduría General de la Nación | Entidades públicas | Reservado | En la hoja de ruta: cuando una entidad registre directamente |
| **Clasificación presupuestal** y **rubros del plan de inversión** del contrato | La entidad (presupuesto) y el supervisor (contrato) | El rubro del expediente es el rubro del plan de inversión | En testnet. Relación con el código presupuestal oficial: en diseño |
| **Fuente de financiación** | La entidad | Cada rubro tiene una fuente; el dinero de una fuente nunca paga el rubro de otra | En testnet |

## Cuentas disponibles hoy

| Cuenta | Nombre | Para qué |
|---|---|---|
| 1105 | Caja | De dónde sale un pago en efectivo |
| 1110 | Bancos | De dónde sale una transferencia |
| 1120 | Cuentas de ahorro | De dónde sale una transferencia |
| 1125 | Fondos | De dónde sale el dinero |
| 5105 | Gastos de personal | Gasto |
| 5110 | Honorarios | Gasto |
| 5115 | Impuestos | Gasto |
| 5120 | Arrendamientos | Gasto |
| 5125 | Contribuciones y afiliaciones | Gasto |
| 5130 | Seguros | Gasto |
| 5135 | Servicios | Gasto |
| 5140 | Gastos legales | Gasto |
| 5145 | Mantenimiento y reparaciones | Gasto |
| 5150 | Adecuación e instalación | Gasto |
| 5155 | Gastos de viaje | Gasto |
| 5160 | Depreciaciones | Gasto |
| 5165 | Amortizaciones | Gasto |
| 5195 | Diversos | Gasto |
| 5205, 5235, 5295 | Personal, servicios y diversos (ventas) | Gasto |
| 5305, 5395 | Financieros, gastos diversos | Gasto |

## Cómo se arma el libro diario

Cada gasto aprobado es un asiento: **débito** a la cuenta de gasto del rubro (por ejemplo 5195
Diversos), **crédito** a la cuenta de donde salió el dinero (1105 Caja o 1110 Bancos), con la
factura como soporte.

| Débito | Crédito | Valor | Soporte |
|---|---|---:|---|
| 5195 Diversos (materiales de estudio) | 1105 Caja | 38.500 COP | Recibo de la papelería |

*Datos de demostración.*

## Fuera de alcance

Retención en la fuente, IVA e ICA. Truway registra lo que se pagó; no liquida impuestos.

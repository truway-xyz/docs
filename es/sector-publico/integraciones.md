---
icon: plug
description: "Con qué sistemas del Estado y herramientas se conecta Truway."
cover: ../.gitbook/assets/velo-truway.png
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Integraciones con el Estado

Truway cubre la ejecución del contrato. Lee la información que ya existe, exporta a las herramientas de la organización y publica el expediente. Nunca escribe en un sistema del Estado.

| Sistema | Qué hace Truway | Disponibilidad |
|---|---|---|
| **Factura electrónica (DIAN)** | Lee de la foto o del PDF el NIT, el proveedor, la fecha y el valor | Disponible |
| **WhatsApp** | Recibe la foto del recibo y pregunta el rubro | Disponible |
| **Software contable** (Siigo, Alegra, World Office y otros) | Exporta el libro diario en CSV o JSON | Disponible |
| **Datos abiertos** | Publica el expediente del programa y sus descargas | Disponible |
| **SECOP II** | Trae el contrato por su ID: entidad, contratista, objeto, valor, fechas, supervisor y fuente de los recursos | Próximamente |
| **Conciliación con SECOP II** | Compara lo que reporta SECOP como pagado con lo aprobado en el expediente | Próximamente |
| **Validación del CUFE ante la DIAN** | Confirma que la factura electrónica existe | Próximamente |
| **Bancos y Bre-B** | Enlaza el comprobante de la transferencia al gasto | Próximamente |
| **Proyectos de inversión (BPIN)** | Asocia el expediente al proyecto que lo financia | Próximamente |
| **SECOP I** | Para los municipios que siguen en el portal anterior | Próximamente |
| **Contabilidad pública y contralorías** | Exportaciones en sus formatos | Próximamente |

## Fuentes de financiación

Cada rubro se clasifica por su fuente: presupuesto nacional (PGN), transferencias (SGP), regalías (SGR), recursos propios o cooperación. Así el informe por financiador sale directo del expediente.

## Plan de cuentas y presupuesto

El rubro del expediente es el rubro del plan de inversión del contrato, y cada uno lleva su cuenta del PUC. Ver [Plan de cuentas (PUC)](../conceptos/plan-de-cuentas.md).

---
icon: shield-halved
description: "Qué puede y qué no puede hacer cada parte, y qué prueba un registro."
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

# Modelo de seguridad

## Qué puede hacer cada parte

| Parte | Puede | No puede |
|---|---|---|
| `Admin` | Proponer cualquier acción; aprobar propuestas de otros | Aprobar lo propio |
| `Approver` | Aprobar o rechazar presupuestos, gastos y pagos | Proponer; aprobar cambios de miembros o de código |
| `Operator` | Proponer gastos y pagos | Aprobar |
| Truway | Desplegar tesorerías; armar y enviar transacciones; pagar comisiones; guardar documentos | Mover fondos, aprobar, cambiar miembros o actualizar una tesorería |
| Cualquiera | Fondear un proyecto; leer todo | Cambiar un registro |

## Qué prueba un registro

* Que dos miembros distintos de esa tesorería lo propusieron y lo aprobaron.
* Que cabe en el presupuesto del rubro, y un pago en los fondos de su fuente.
* Que se asienta en el plan de cuentas de su rubro.
* Que el soporte tiene esa huella y no respalda otro registro de la misma tesorería.
* Que lo produjo el código cuyo hash de WASM coincide con un build publicado.

## Qué no prueba

* Que una dirección corresponda a una persona: eso lo resuelve la organización fuera de la red.
* Que el documento sea auténtico, ni que un pago por banco o en efectivo haya ocurrido. `payment_ref` enlaza la evidencia externa para auditores.
* Que otra organización no haya usado la misma factura.
* Que dos archivos sean facturas distintas: `receipt_hash` identifica el archivo.

## Límites actuales

| Límite | Plan |
|---|---|
| En testnet, la plataforma custodia los firmantes de demostración | Firma por persona; los firmantes de demostración no pasan a mainnet |
| Truway puede demorar el envío de un paso firmado | Ruta pública de envío |
| El explorador lee el índice de Truway | Cualquiera puede leer el ledger directamente: [Verificar un registro](verificar-un-registro.md) |
| Un administrador aprobador basta para cambiar miembros o código | Varios administradores y timelock antes de mainnet |
| Las organizaciones sin tesorería siguen en el modelo anterior de registros atestados por el servidor | Esos contratos están congelados y se retirarán |

Truway no custodia dinero público, no escribe en sistemas del Estado y no guarda datos de beneficiarios.

---
icon: shield-check
description: Qué queda en el registro público, qué prueba y qué no.
cover: ../.gitbook/assets/velo-truway.png
coverY: 0
layout:
  width: default
  cover:
    visible: true
    size: full
    mask: none
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
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
  anchors:
    visible: true
---

# Registro público

Cada asignación y cada gasto aprobado quedan en un registro público. Nadie puede cambiarlo ni borrarlo: ni Truway, ni la entidad, ni la organización.

## Qué guarda cada gasto

| Dato                                | Ejemplo                                             |
| ----------------------------------- | --------------------------------------------------- |
| Código                              | `PAY-2026-0004`                                     |
| Programa, rubro y financiador       | Becas · Materiales de estudio · Fondo departamental |
| Cuenta contable                     | PUC 5195 Diversos                                   |
| Valor y moneda                      | 38.500 COP                                          |
| Quién lo registró y quién lo aprobó | Dos personas distintas                              |
| Huella de la factura                | Un código calculado a partir del archivo            |
| Fecha                               | Cuando se aprobó                                    |

## La huella de la factura

La huella es un código que se calcula a partir del archivo de la factura. Si el archivo cambia, aunque sea un píxel, la huella cambia. Con la huella no se puede reconstruir el archivo, así que la factura sigue siendo privada.

Para comprobar una factura, suéltala en la página del gasto: tu navegador calcula su huella y la compara con la registrada. Ver [Verificar un gasto](../guias/verificar-un-gasto.md).

## Qué prueba y qué no

| Prueba                                                   | No prueba                                                                                            |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Que ese archivo es exactamente el que se aprobó          | Que la factura sea auténtica                                                                         |
| Que dos personas distintas lo registraron y lo aprobaron | Quiénes son esas personas: eso lo sabe la organización                                               |
| Que cabe en el rubro aprobado                            | Que el pago se hizo por banco o en efectivo: esa evidencia queda con la organización y sus auditores |
| Que el archivo no respalda otro gasto de la organización | Que otra organización no lo haya usado                                                               |

{% hint style="info" %}
La huella es del archivo, no de la factura: otra foto de la misma factura en papel da otra huella. La comprobación de facturas entre organizaciones, por su CUFE, está en la [hoja de ruta](../acerca-de/hoja-de-ruta.md).
{% endhint %}

## Un estándar abierto

El registro sigue [Proof of Spend](../proof-of-spend/proof-of-spend.md). Cualquier sistema puede leerlo y armar el informe de ejecución o el libro diario sin pasar por Truway.

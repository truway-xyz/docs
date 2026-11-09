---
description: "Qué datos guarda Truway, dónde, quién los ve y por cuánto tiempo."
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

# Datos y privacidad

El registro público solo guarda valores, códigos y huellas. Los datos personales y los archivos se quedan en el almacenamiento privado de Truway.

## Dónde vive cada dato

| Dato | Dónde | Quién lo ve | Cuánto tiempo |
|---|---|---|---|
| Presupuesto por rubro, cuenta y fuente | Registro público | Cualquiera | Permanente |
| Gastos aprobados: valor, rubro, cuenta, fecha | Registro público | Cualquiera | Permanente |
| Quién propuso y quién aprobó | Registro público, como un código anónimo por persona | Cualquiera; solo la organización sabe de quién es cada código | Permanente |
| Huella de la factura | Registro público | Cualquiera | Permanente |
| Archivo de la factura o del recibo | Almacenamiento privado | La organización y a quien ella lo comparta | Se definirá antes del primer piloto |
| Nombre y NIT del proveedor | Base de datos de Truway; en el registro solo como huella | La organización | Se definirá antes del primer piloto |
| Nombres de personas y celulares | Base de datos de Truway | La organización | Se definirá antes del primer piloto |
| Mensajes de WhatsApp | Base de datos de Truway | La organización | Se definirá antes del primer piloto |
| Datos de beneficiarios | Truway no los recibe | | |

## Compromisos

* Truway no toca ni custodia dinero público. Los pagos los hacen la entidad y la organización por sus bancos.
* Truway no escribe en sistemas del Estado.
* Los datos se exportan cuando se quiera, en CSV y JSON.
* La IA lee las facturas, pero nunca aprueba: cada gasto lo aprueba una persona.

## Qué decide la organización

Qué nombres se muestran junto a cada gasto en el expediente público y qué documentos comparte. Por defecto se muestran el proveedor y el valor, que son información pública en un contrato público.

# Leer el registro

Cómo convertir los eventos de Proof of Spend en los dos documentos que piden financiadores y
auditores. La versión completa, con ejemplos, está en inglés: [Reading the record](https://github.com/truway-xyz/docs/blob/main/en/proof-of-spend/reading-the-record.md).

## Informe de ejecución presupuestal

Para un proyecto y un periodo: el último `budget_set` por `(rubro, fuente)` da el **presupuesto**;
la suma de `expense_recorded.amount` y `payment_executed.amount` por `(rubro, fuente)` da lo
**ejecutado**; la diferencia es lo **disponible**. Agrupar por fuente da el informe de cada
financiador.

## Libro diario

Cada `expense_recorded` y `payment_executed` es un asiento: débito a `account` en `chart`, crédito a
la cuenta de donde salió el dinero (caja, bancos o el activo de la tesorería), con `receipt_hash`
como soporte. La API pública de Truway lo entrega en CSV:
`GET https://api.truway.xyz/public/proof/programs/<id>/ledger?format=csv`.

## Valores

Punto fijo con **7 decimales** en la moneda del rubro: `450000000000` son 45.000,00 COP.

## Historia

Los proveedores de RPC guardan los eventos unos 7 días. Para periodos más largos hay que leer de un
indexador: ver [Eventos e indexación](../arquitectura/eventos-e-indexacion.md).

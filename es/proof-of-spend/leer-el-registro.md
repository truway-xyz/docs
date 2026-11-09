---
description: "Arma el informe de ejecución y el libro diario a partir de los eventos."
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

# Leer el registro

## Informe de ejecución presupuestal

Para un proyecto y un periodo:

1. El último `budget_set` por `(line, source)` da el **presupuesto**.
2. La suma de `expense_recorded.amount` y `payment_executed.amount` por `(line, source)` da lo **ejecutado**.
3. `presupuesto − ejecutado` es lo **disponible**.
4. Agrupar por `source` da el informe de cada financiador.

Cada gasto trae también `line_paid` y `line_budget`, para revisar los acumulados sin recorrer toda la historia.

| Rubro | Cuenta | Fuente | Presupuesto | Ejecutado | Disponible |
|---|---|---|---:|---:|---:|
| Matrícula | CO_PUC 5135 | Fondo departamental | 500.000 | 0 | 500.000 |
| Transporte | CO_PUC 5155 | Fondo departamental | 200.000 | 62.000 | 138.000 |
| Materiales de estudio | CO_PUC 5195 | Aliado corporativo | 500.000 | 38.500 | 461.500 |

*Datos de demostración en COP.*

## Libro diario

Cada `expense_recorded` y `payment_executed` es un asiento:

* **Débito:** `account` en `chart`.
* **Crédito:** la cuenta de donde salió el dinero (caja, bancos o el activo de la tesorería).
* **Soporte:** `receipt_hash`.

Cada `project_funded` debita el activo de la tesorería y acredita la cuenta de pasivo o ingreso que defina la organización.

La API pública de Truway lo entrega listo:

```bash
curl "https://api.truway.xyz/public/proof/programs/<id>/ledger?format=csv"
```

## Valores

Punto fijo con **7 decimales** en la moneda del rubro. `450000000000` son 45.000,00 COP.

## Identificadores

Proyectos, rubros, fuentes, proveedores y referencias de pago van como SHA-256 de un identificador que elige la organización, nunca el identificador en claro.

## Historia

Los proveedores de RPC guardan eventos unos 7 días. Para periodos más largos, lee de un indexador. Ver [Eventos e indexación](../desarrolladores/eventos-e-indexacion.md).

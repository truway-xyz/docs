---
description: "Endpoints públicos de lectura, sin autenticación."
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

# API pública

Base: `https://api.truway.xyz`. No requiere autenticación. Lee del índice de Truway.

| Método | Ruta | Devuelve |
|---|---|---|
| `GET` | `/public/proof/{code}` | Un gasto por su código, por ejemplo `PAY-2026-0004` |
| `GET` | `/public/proof/programs/{programId}` | La ejecución de un programa por rubro, equipo y financiador |
| `GET` | `/public/proof/programs/{programId}/ledger` | El libro diario en JSON |
| `GET` | `/public/proof/programs/{programId}/ledger?format=csv` | El libro diario en CSV |

## Ejemplos

```bash
curl https://api.truway.xyz/public/proof/PAY-2026-0004
curl "https://api.truway.xyz/public/proof/programs/<programId>/ledger?format=csv" -o libro-diario.csv
```

## Columnas del libro diario

`date`, `code`, `description`, `budget_line`, `chart`, `debit_account`, `debit_name`, `credit_account`, `credit_name`, `amount`, `currency`, `receipt_hash`, `transaction`.

## Errores

```json
{ "error": { "code": "program_not_found", "message": "Program not found" } }
```

| Código | Cuándo |
|---|---|
| `proof_not_found` | No hay un gasto con ese código |
| `program_not_found` | No existe el programa |

# budget-treasury

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Budget treasury](https://github.com/truway-xyz/docs/blob/main/en/architecture/budget-treasury.md).

La implementación de referencia de Proof of Spend, versión `0.4.0` en testnet, una instancia por organización. Guarda los miembros y sus roles (`Admin`, `Approver`, `Operator`), los rubros por proyecto, rubro y fuente, los fondos por proyecto y fuente, las propuestas y los soportes ya usados.

- Todo cambio es una propuesta que aprueba otro miembro: `SetBudget`, `RecordExpense`, `Pay`, `AddMember`, `RemoveMember`, `Upgrade`.
- Exige al menos dos administradores distintos al crearse y admite como máximo 32 miembros.
- Nunca deja que un rubro gaste más que su presupuesto, ni que un soporte respalde dos gastos de la misma tesorería.
- Sus 16 códigos de error son parte de la interfaz pública y nunca se renumeran.

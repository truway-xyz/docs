# Implementar el estándar

Proof of Spend está hecho para que otros lo implementen: otra plataforma, un sistema del Estado o un
contrato escrito de otra forma. La lista de conformidad completa está en inglés:
[Implementing the standard](https://github.com/truway-xyz/docs/blob/main/en/proof-of-spend/implementing.md).

## En resumen

- **Declaración:** `event_schema = proof-of-spend/1` en la metadata del contrato.
- **Eventos:** los de la sección 5 de la [especificación](especificacion.md), con nombres, temas y
  campos exactos; `contract_upgraded` siempre antes de cambiar el código.
- **Invariantes:** dos miembros distintos, nunca más gasto que presupuesto, un rubro por gasto,
  soporte obligatorio y de un solo uso, cuenta del plan del rubro, quórum garantizado, valores
  positivos.
- **Privacidad:** ningún evento lleva datos personales.
- **Pruebas:** copia las pruebas de conformidad de `budget-treasury`, que comparan cada evento con
  el estándar.
- **Nuevo plan de cuentas:** un pull request contra la sección 8 de la especificación.

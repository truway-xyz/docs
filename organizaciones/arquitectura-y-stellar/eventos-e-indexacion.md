# Eventos e indexación

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Events and indexing](https://github.com/truway-xyz/docs/blob/main/en/architecture/events-and-indexing.md).

Los eventos de Proof of Spend son la interfaz pública: `budget_set`, `expense_recorded`, `payment_executed`, `project_funded`, `proposal_created`, `proposal_executed`, `proposal_rejected`, `member_added`, `member_removed` y `contract_upgraded`.

Los proveedores de RPC guardan eventos unos **7 días**. Truway los copia cada 15 segundos a su base (`treasury_events`) y los sirve en su API pública. Cualquiera puede indexarlos por su cuenta: con `getEvents` del RPC, con un indexador de terceros, con Galexie o con Hubble.

# Plataforma

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Platform](https://github.com/truway-xyz/docs/blob/main/en/architecture/platform.md).

La parte de Truway que no está en el ledger: la app, la API, el canal de WhatsApp y el almacenamiento. Es de código cerrado.

- Una sola API concentra la lógica y es la única que arma transacciones para los contratos.
- **La IA sugiere, las personas deciden:** un gasto leído por IA y nunca aprobado no llega al registro.
- Siete roles base en la app; en testnet se inscriben en la tesorería con una regla de demostración.
- Capas de seguridad: autenticación con token corto y límite de peticiones, permisos explícitos, reglas de negocio como el doble control, y aislamiento por organización.
- Infraestructura en un proveedor de nube, con PostgreSQL administrado, colas para trabajos en segundo plano y almacenamiento privado de soportes con enlaces firmados de corta duración.

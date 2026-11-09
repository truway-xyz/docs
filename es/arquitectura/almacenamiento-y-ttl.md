# Almacenamiento y TTL

> Resumen en español. La versión completa, con cada parámetro y referencia, está en inglés:
> [Storage and ttl](https://github.com/truway-xyz/docs/blob/main/en/architecture/storage-and-ttl.md).

El almacenamiento en Stellar se arrienda: cada entrada tiene un tiempo de vida y se archiva, no se borra, cuando vence. La política de Truway extiende las entradas a 120 días cuando les quedan menos de 30, en cada escritura. Desde el protocolo 23 una entrada archivada se restaura sola cuando una transacción la necesita, y **nunca se lee como ausente**: un soporte usado no se puede reusar aunque su entrada esté archivada.

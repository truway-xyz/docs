# Para la entidad y el supervisor

> Estado: las aprobaciones están **en testnet**. Traer contratos de SECOP II y las alertas están
> **en diseño**.

## Qué pone la entidad

- El **supervisor** del contrato, que aprueba rubros y gastos.
- Un **punto focal** que acompaña el piloto.

Truway pone todo lo demás. La entidad no instala software, no cambia sus procedimientos ni entrega
ningún sistema.

## Qué hace el supervisor

1. **Aprueba los rubros** del plan de inversión una vez. Desde ahí, cualquier cambio pide una nueva
   aprobación y deja rastro.
2. **Aprueba cada gasto** que propone el coordinador, viendo la factura, el rubro, su cuenta
   contable y lo que queda.
3. **Rechaza** un gasto cuando algo no cuadra. El rechazo también queda registrado; registrar el
   motivo está planeado.

El supervisor nunca puede aprobar un gasto que él mismo propuso.

## Qué ve el supervisor

| | |
|---|---|
| Contratado frente a ejecutado, por rubro | En testnet |
| Cada gasto con su factura, proveedor, quién lo propuso y cuándo | En testnet |
| Alerta: el gasto supera lo que queda del rubro | En diseño (hoy el gasto se rechaza) |
| Alerta: esta factura ya se reportó en otro contrato | En diseño |
| Conciliación: "SECOP reporta pagado X; el expediente tiene aprobado Y" | En diseño |

## Qué gana la entidad

- Evidencia de cada pago que autoriza.
- Menos tiempo armando informes: el informe de ejecución sale del expediente.
- Un expediente público que veedurías y contralorías pueden comprobar sin pedirle nada a nadie.

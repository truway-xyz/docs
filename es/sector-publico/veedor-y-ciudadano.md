# Para el veedor y el ciudadano

> Estado: **en testnet** con datos de demostración.

Veedurías, concejales, contralorías y cualquier ciudadano pueden comprobar cómo se gasta un contrato
público, sin cuenta y sin pedirle permiso a nadie.

## Lee el expediente

La página pública de un programa muestra, por rubro, lo presupuestado, lo gastado y lo que queda, y
cada gasto con su proveedor, cuenta contable, quién lo propuso, quién lo aprobó y cuándo. El libro
diario se descarga en CSV para analizarlo en una hoja de cálculo.

## Comprueba un gasto

1. Abre `app.truway.xyz/proof/` seguido del **código de verificación** del gasto.
2. Ves el gasto en lenguaje claro: valor, rubro, fuente, quién lo propuso y quién lo aprobó.
3. Si tienes la factura, **suelta el archivo en la página**. Tu navegador calcula su huella y te
   dice si coincide con la que quedó registrada al aprobarlo. El archivo nunca sale de tu computador.
4. Sigue el enlace al registro público para ver la misma entrada fuera de Truway.

## Qué prueba una coincidencia y qué no

| Una coincidencia prueba | No prueba |
|---|---|
| Que este archivo exacto es el que se aprobó | Que la factura en sí sea auténtica |
| Que dos personas distintas lo propusieron y lo aprobaron | Quiénes son esas personas: eso lo sabe la organización |
| Que cabe en el rubro aprobado | Que el dinero de verdad se pagó por banco o en efectivo: esa evidencia queda con la organización y sus auditores |
| Que el archivo no respalda otro gasto de esa organización | Que no lo haya usado otra organización (en diseño) |

Otra foto de la misma factura en papel no va a coincidir: la huella es del archivo.

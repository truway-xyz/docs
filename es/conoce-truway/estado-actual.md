# Estado actual

Revisado el **2026-11-08**. Todo lo de abajo corre en la red de pruebas (**testnet**) de Stellar con
datos de demostración. Nada está en la red principal y todavía no hay un piloto con un contrato real.

## Qué funciona y qué todavía no

| Capacidad | Estado |
|---|---|
| Presupuesto por contrato, rubro y fuente de financiación, cada rubro con su cuenta contable | **En testnet** |
| Anticipo de caja menor asignado a un equipo y aprobado por una segunda persona | **En testnet** (queda registrado; todavía no se mueve dinero) |
| Factura capturada por WhatsApp: el asistente la lee y pregunta a qué rubro pertenece | **En testnet**, con un número de prueba |
| Quien propone un gasto no puede aprobarlo | **En testnet**, impuesto por el contrato |
| Un soporte no se puede usar dos veces en la misma organización | **En testnet**, impuesto por el contrato |
| Explorador público: comprobar un gasto con su código de verificación, sin cuenta | **En testnet** |
| Página pública del programa y descarga del libro diario (JSON y CSV) | **En testnet** |
| Cada persona firma su propio paso | **En diseño.** Hoy la demo usa firmantes de demostración custodiados por la plataforma, marcados *Demo signer* |
| Traer un contrato de SECOP II por su ID | **En diseño** |
| Alertas: gasto mayor que el rubro, factura ya reportada en otra parte | **En diseño** |
| Soporte comprobado entre organizaciones, y facturas electrónicas identificadas por su CUFE | **En diseño** |
| Anticipos pagados como dinero y salida a pesos | **En la hoja de ruta** |
| Red principal | **En la hoja de ruta**, después de una revisión de seguridad independiente |
| Donaciones en USDC | Construido, fuera del alcance actual |

## Versiones

| Componente | Versión | Dónde |
|---|---|---|
| Proof of Spend | `proof-of-spend/1`, borrador 2 (2026-11-07) | [Especificación](../proof-of-spend/especificacion.md) |
| Contrato `budget-treasury` | `0.4.0`, testnet | [Despliegues](../arquitectura/despliegues.md) |
| Seguridad | Revisión interna del 2026-11-07; no es una auditoría independiente | [Seguridad](../arquitectura/seguridad.md) |

## Adopción

- **6 cartas de intención no vinculantes** de organizaciones.
- **Pilotos en pausa** por falta de financiación en el sector; ninguno está corriendo.
- **Más de 11 organizaciones entrevistadas** en **más de 5 países**.
- Demanda de funcionarios públicos en un taller regional del Plan Nacional de Desarrollo de
  Colombia (octubre de 2026). Las conversaciones con instituciones son verbales por ahora; ninguna
  se nombra aquí hasta que conste por escrito.

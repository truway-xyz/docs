---
description: "Componentes de Truway, quién controla cada uno y qué vive en la red."
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

# Arquitectura

Los miembros de cada organización proponen y aprueban en su propio contrato `budget-treasury` en Stellar. La plataforma de Truway arma esas transacciones, guarda los documentos e indexa los eventos. Cualquiera puede leer el resultado.

## Mapa de la documentación técnica

<figure><img src="../.gitbook/assets/mapa-documentacion.svg" alt="Mapa de la documentación técnica: Proof of Spend, arquitectura, contrato, firma y seguridad, y datos."><figcaption></figcaption></figure>

## Contexto

<figure><img src="../.gitbook/assets/contexto.svg" alt="Supervisor, coordinador y equipo de campo usan la app y WhatsApp; la API de Truway envía a budget-treasury los pasos que firma cada miembro; los eventos quedan en el ledger público, que lee el indexador de Truway y cualquier explorador de terceros."><figcaption><p>Personas, Truway y Stellar</p></figcaption></figure>

## Componentes

<figure><img src="../.gitbook/assets/componentes.svg" alt="La app web y WhatsApp llegan a la API de Truway, con módulos de identidad, programas, captura, tesorería, API pública e indexador; la API usa PostgreSQL, Redis y almacenamiento de soportes, y se comunica con budget-treasury a través del RPC de Stellar."><figcaption><p>Componentes de la plataforma</p></figcaption></figure>

| Capa | Qué hace | Quién la controla |
|---|---|---|
| **Miembros** (administradores, aprobadores, operadores) | Proponen y aprueban, cada uno con su llave | La organización |
| **App web y canal de WhatsApp** | Capturan facturas, muestran presupuestos y piden aprobaciones | Truway |
| **API de Truway** | Arma cada transacción para quien debe firmarla, guarda documentos y su SHA-256, indexa eventos | Truway |
| **`budget-treasury`** | Hace cumplir las reglas: dos firmantes, límite del rubro, soporte de un solo uso, cuenta contable | Sus miembros; Truway lo despliega pero nunca es miembro |
| **Eventos Proof of Spend** | La interfaz pública | Nadie: están en el ledger |

`RecordExpense` registra un gasto pagado por banco o en efectivo y no mueve fondos. `Pay` paga desde fondos que tenga el contrato.

## Qué vive en la red y qué fuera

| Dato | Dónde | Forma |
|---|---|---|
| Presupuesto por rubro y fuente, con plan, cuenta y moneda | Ledger | Valores y códigos; identificadores como SHA-256 |
| Gasto: valor, rubro, cuenta, proponente, aprobador | Ledger | Direcciones y valores |
| Huella del soporte | Ledger | SHA-256 del archivo |
| Archivo del soporte | Almacenamiento privado de Truway | Archivo |
| NIT del proveedor | Base de datos de Truway; en el ledger como `payee_ref` | SHA-256 |
| Nombres de personas, proyectos y proveedores | Base de datos de Truway | Texto |

Los eventos nunca llevan datos personales.

## Decisiones de diseño

* [ADR 0003](https://github.com/truway-xyz/soroban-contracts/blob/main/docs/adr/0003-members-sign-proof-of-spend.md): firman los miembros y los registros siguen Proof of Spend. Reemplaza al ADR 0002, de registros atestados por el servidor.
* Una instancia por organización: ninguna organización puede tocar el registro de otra.
* Contrato estrecho y lógica de negocio encima: el contrato hace cumplir las reglas del dinero; la captura, la lectura de facturas y los informes viven fuera.

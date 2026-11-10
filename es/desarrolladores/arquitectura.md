---
icon: sitemap
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

Código abierto bajo Apache-2.0. El repositorio contiene `budget-treasury`, la implementación de referencia de Proof of Spend.

<a href="https://github.com/truway-xyz/soroban-contracts" class="button primary">Ver los contratos en GitHub</a>

## Contexto

<figure><img src="../.gitbook/assets/c4-contexto.png" alt="Diagrama de contexto C4. Supervisor, coordinación, equipo de campo y veedor usan Truway. Truway envía propuestas y aprobaciones firmadas a Stellar y lee sus eventos, recibe mensajes de WhatsApp Business, usa Privy para la sesión y la firma, Google Gemini para leer facturas, y leerá contratos de SECOP II."><figcaption><p>Contexto del sistema (C4, nivel 1)</p></figcaption></figure>

## Componentes

<figure><img src="../.gitbook/assets/componentes.png" alt="Diagrama de componentes UML. La app web tiene panel, explorador público y firmante de Privy. La API tiene identidad, programas, prueba pública, almacenamiento, captura por WhatsApp, lectura de facturas con Gemini, tesorería, cliente Soroban e indexador. El cliente Soroban usa los bindings para hablar con el RPC de Stellar y con budget-treasury; los datos van a PostgreSQL, Redis y almacenamiento de objetos."><figcaption><p>Componentes (UML)</p></figcaption></figure>

| Capa | Qué hace | Quién la controla |
|---|---|---|
| **Miembros** (administradores, aprobadores, operadores) | Proponen y aprueban, cada uno con su llave | La organización |
| **App web y canal de WhatsApp** | Capturan facturas, muestran presupuestos y piden aprobaciones | Truway |
| **API de Truway** | Arma cada transacción para quien debe firmarla, guarda documentos y su SHA-256, indexa eventos | Truway |
| **`budget-treasury`** | Hace cumplir las reglas: dos firmantes, límite del rubro, soporte de un solo uso, cuenta contable | Sus miembros; Truway lo despliega pero nunca es miembro |
| **Eventos Proof of Spend** | La interfaz pública | Nadie: están en el ledger |

`RecordExpense` registra un gasto pagado por banco o en efectivo y no mueve fondos. `Pay` paga desde fondos que tenga el contrato.

## Arquitectura en Stellar

<figure><img src="../.gitbook/assets/arquitectura-stellar.png" alt="Arquitectura en Stellar. Los miembros firman su entrada de autorización con Privy; la API envía la invocación firmada y la cuenta remitente de Truway paga la comisión a través del RPC. Cada organización tiene su instancia de budget-treasury, desplegada desde el WASM 0.4.0 por una cuenta de un solo uso; el WASM está atestado en un release de GitHub que leen Stellar Expert y Stellar Lab. Los contratos emiten eventos Proof of Spend al ledger, que lee el indexador y cualquier lector. Próximamente: USDC hacia la Stellar Disbursement Platform, un anchor a pesos y un registro compartido de soportes."><figcaption><p>Arquitectura en Stellar: contratos, cuentas e integraciones</p></figcaption></figure>

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

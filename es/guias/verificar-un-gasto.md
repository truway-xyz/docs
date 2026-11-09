---
description: "Comprueba un gasto y su factura sin cuenta y sin pedir permiso."
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

# Verificar un gasto

Cualquier persona puede verificar un gasto: veedurías, concejales, contralorías o ciudadanos. No necesitas cuenta.

<figure><img src="../.gitbook/assets/verificar-gasto.svg" alt="Con el código del gasto abres la página de verificación; si tienes la factura la sueltas para comparar la huella, y si no, revisas rubro, cuenta y aprobadores. Desde ahí puedes ver el mismo registro fuera de Truway."><figcaption><p>Cómo se verifica un gasto</p></figcaption></figure>

## Pasos

1. Abre [app.truway.xyz/proof](https://app.truway.xyz/proof).
2. En **Código del gasto**, escribe el código, por ejemplo `PAY-2026-0004`, y presiona **Verificar**.
3. Revisa el gasto: valor, **Rubro**, **Cuenta contable**, **Financiado por**, **Registrado por** y **Aprobó**.
4. Si tienes la factura, suéltala en **Comprueba la factura** o presiona **Elegir archivo**.
   * **La factura coincide**: es exactamente el archivo que se aprobó.
   * **Esta no es la factura aprobada**: el archivo es distinto.
5. Para ver el mismo registro fuera de Truway, presiona **Ver en Stellar**.

El archivo se comprueba en tu navegador y no se sube a ningún lado.

{% hint style="info" %}
Otra foto de la misma factura en papel no va a coincidir: la huella es del archivo. Ver [Registro público](../conceptos/registro-publico.md).
{% endhint %}

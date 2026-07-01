# Sesión 5: Expresiones Regulares + Introducción a NumPy

## 🎯 Objetivos

Al terminar esta sesión podrás:

- Construir patrones con expresiones regulares para validar datos bancarios (CLABE, RFC, correo)
- Usar el módulo `re` para buscar, validar y sustituir texto
- Crear arreglos y matrices NumPy
- Realizar operaciones vectorizadas sobre datos financieros

---

## 1.5.1 Patrones de Expresiones Regulares

Las expresiones regulares (regex) son patrones que describen la *forma* que debe tener un texto. Son perfectas para validar que un dato tiene el formato correcto: ¿esta cadena es un RFC válido? ¿Tiene 18 dígitos la CLABE?

### Metacaracteres Fundamentales

| Símbolo | Significa | Ejemplo |
|---------|-----------|---------|
| `\d` | Un dígito (0-9) | `\d\d\d` → "123" |
| `\w` | Letra, dígito o guión bajo | `\w+` → "hola123" |
| `\s` | Espacio en blanco | `\s` → " " |
| `.` | Cualquier carácter | `a.c` → "abc", "a1c" |
| `^` | Inicio de la cadena | `^Banco` → empieza con "Banco" |
| `$` | Fin de la cadena | `\d$` → termina en dígito |
| `{n}` | Exactamente n veces | `\d{18}` → exactamente 18 dígitos |
| `{n,m}` | Entre n y m veces | `\d{8,10}` → 8 a 10 dígitos |
| `+` | Uno o más | `\d+` → uno o más dígitos |
| `*` | Cero o más | `\d*` → cero o más dígitos |
| `?` | Cero o uno | `[-]?` → guión opcional |
| `[abc]` | Cualquiera de a, b, c | `[AEIOU]` → una vocal |
| `[^abc]` | Ninguno de a, b, c | `[^0-9]` → no dígito |
| `(abc)` | Grupo de captura | `(\d{3})-(\d{4})` |

### Construyendo Patrones Bancarios

```python
# 💡 CONCEPTO — Diseñar patrones para datos del banco

# ── CLABE Interbancaria ──────────────────────────────────────────
# Regla: exactamente 18 dígitos
# Patrón: ^\d{18}$
#   ^      → inicio de la cadena
#   \d{18} → 18 dígitos consecutivos
#   $      → fin (no puede haber nada más)
#
# Válido:   "032180000118359719"
# Inválido: "03218000011835971"   (17 dígitos)
#           "0321800001183597AB"  (contiene letras)

# ── RFC con Homoclave ────────────────────────────────────────────
# Regla: 4 letras + 6 dígitos (AAMMDD) + 3 alfanuméricos
# Patrón: ^[A-ZÑ&]{4}\d{6}[A-Z0-9]{3}$
#   [A-ZÑ&]{4} → 4 letras mayúsculas (persona física)
#   \d{6}      → 6 dígitos de fecha (AAMMDD)
#   [A-Z0-9]{3}→ 3 caracteres alfanuméricos (homoclave)
#
# Válido: "GARA850312XY3"

# ── Correo Electrónico ───────────────────────────────────────────
# Patrón básico: ^[\w.\-]+@[\w\-]+\.[a-z]{2,6}$

# ── Teléfono México (10 dígitos) ─────────────────────────────────
# Patrón: ^\d{10}$

# ── Número de tarjeta (solo formato, 16 dígitos) ─────────────────
# Patrón: ^\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}$
```

---

## 1.5.2 Módulo `re`

```python
# 💡 CONCEPTO — Las funciones más importantes del módulo re

import re

# re.fullmatch() — la cadena completa debe coincidir (ideal para validar)
# re.search()    — busca en cualquier parte de la cadena
# re.findall()   — devuelve TODAS las coincidencias como lista
# re.sub()       — sustituye coincidencias por otro texto

# ── Validar CLABE ────────────────────────────────────────────────
def validar_clabe(clabe):
    return bool(re.fullmatch(r'^\d{18}$', clabe))

print(validar_clabe("032180000118359719"))   # True
print(validar_clabe("0321800001183597"))     # False (16 dígitos)
print(validar_clabe("03218000011835971X"))   # False (letra al final)


# ── Validar RFC (persona física) ─────────────────────────────────
def validar_rfc(rfc):
    return bool(re.fullmatch(r'^[A-ZÑ&]{4}\d{6}[A-Z0-9]{3}$', rfc.upper()))

print(validar_rfc("GARA850312XY3"))    # True
print(validar_rfc("GARA850312"))       # False


# ── Extraer datos de un texto ────────────────────────────────────
texto = """
Estimado cliente, su transferencia por $15,000.00 fue procesada.
Número de referencia: REF-2024-00891.
Contacto: soporte@banco.mx | Tel: 5512348765
"""

montos      = re.findall(r'\$[\d,]+\.?\d*', texto)
referencias = re.findall(r'REF-\d{4}-\d{5}', texto)
correos     = re.findall(r'[\w.\-]+@[\w\-]+\.[a-z]{2,5}', texto)

print(f"Montos:      {montos}")         # ['$15,000.00']
print(f"Referencias: {referencias}")   # ['REF-2024-00891']
print(f"Correos:     {correos}")        # ['soporte@banco.mx']


# ── Limpiar y sustituir ──────────────────────────────────────────
telefono_raw = "55 1234-5678"
telefono_limpio = re.sub(r'[\s\-]', '', telefono_raw)
print(f"Teléfono limpio: {telefono_limpio}")    # 5512345678

# Enmascarar CLABE (mostrar solo primeros 3 y últimos 2)
clabe = "032180000118359719"
clabe_oculta = re.sub(r'(\d{3})\d{13}(\d{2})', r'\1*************\2', clabe)
print(f"CLABE oculta: {clabe_oculta}")           # 032*************19
```

### ✏️ Ejercicio 1 — Validador de Datos de Clientes

```python
# ✏️ EJERCICIO 1 — Completa las funciones de validación

import re

def validar_correo(correo):
    """Valida que sea un correo con formato user@dominio.ext"""
    patron = ???    # TODO: escribe el patrón
    return bool(re.fullmatch(patron, correo))

def validar_telefono(tel):
    """Valida teléfono de 10 dígitos (con o sin espacios/guiones)"""
    tel_limpio = re.sub(r'[\s\-\(\)]', '', tel)
    patron = ???    # TODO: 10 dígitos exactos
    return bool(re.fullmatch(patron, tel_limpio))

def enmascarar_tarjeta(numero):
    """Convierte '4111111111111234' en '****-****-****-1234'"""
    # TODO: Usa re.sub para reemplazar los primeros 12 dígitos con ****
    pass


# Pruebas
print(validar_correo("usuario@banco.mx"))      # True
print(validar_correo("usuario@"))              # False
print(validar_telefono("55 1234-5678"))        # True
print(validar_telefono("123"))                 # False
print(enmascarar_tarjeta("4111111111111234"))  # ****-****-****-1234
```

<details>
<summary>Ver solución</summary>

```python
import re

def validar_correo(correo):
    patron = r'^[\w.\-]+@[\w\-]+\.[a-z]{2,6}$'
    return bool(re.fullmatch(patron, correo, re.IGNORECASE))

def validar_telefono(tel):
    tel_limpio = re.sub(r'[\s\-\(\)]', '', tel)
    return bool(re.fullmatch(r'^\d{10}$', tel_limpio))

def enmascarar_tarjeta(numero):
    digitos = re.sub(r'\D', '', numero)
    if len(digitos) == 16:
        return f"****-****-****-{digitos[-4:]}"
    return numero
```

</details>

### 🤖 Ejercicio 2 — Con apoyo de IA

Pega este prompt en Claude o Gemini:

```
Soy analista en un banco aprendiendo Python. Crea un script que use el módulo re para:
1. Validar que una cadena es un RFC válido (persona física: 4 letras + 6 dígitos + 3 alfanuméricos)
2. Extraer todos los montos en pesos de un texto libre (formato $X,XXX.XX)
3. Enmascarar un número de cuenta dejando visibles solo los últimos 4 dígitos
4. Limpiar un número de teléfono de cualquier formato y dejarlo en 10 dígitos

Usa ejemplos con datos bancarios mexicanos y comenta el código en español.
```

---

## 1.6.1 Introducción a NumPy — Arreglos y Matrices

### ¿Por qué NumPy?

NumPy (**Num**erical **Py**thon) es la librería fundamental para cálculo numérico en Python. En el banco la usamos para análisis de portafolios, cálculos de riesgo y procesamiento masivo de datos.

```python
# 💡 CONCEPTO — Listas vs NumPy: la diferencia clave

import numpy as np
import time

# Con listas: necesitas un bucle para operar sobre todos los elementos
rendimientos_lista = [0.05, 0.08, 0.03, 0.12, 0.07]
rendimientos_x2    = [r * 2 for r in rendimientos_lista]   # Necesita list comprehension

# Con NumPy: operación directa sobre todo el arreglo a la vez
rendimientos_np    = np.array([0.05, 0.08, 0.03, 0.12, 0.07])
rendimientos_x2_np = rendimientos_np * 2    # Multiplica TODOS de una vez

print(f"Lista:  {rendimientos_x2}")
print(f"NumPy:  {rendimientos_x2_np}")

# NumPy también es mucho más rápido con datos grandes
N = 1_000_000
lista   = list(range(N))
arreglo = np.arange(N)

t0 = time.time()
[x * 2.5 for x in lista]
t1 = time.time()
arreglo * 2.5
t2 = time.time()

print(f"\nTiempo con lista:  {(t1-t0)*1000:.1f} ms")
print(f"Tiempo con NumPy:  {(t2-t1)*1000:.1f} ms")
```

### Crear Arreglos

```python
# 💡 CONCEPTO — Formas de crear arreglos NumPy

import numpy as np

# Desde una lista
precios = np.array([18.50, 19.20, 17.80, 20.10, 19.95])

# Arreglos especiales
ceros   = np.zeros(5)              # [0. 0. 0. 0. 0.]
unos    = np.ones(5)               # [1. 1. 1. 1. 1.]
rango   = np.arange(0, 10, 2)     # [0 2 4 6 8]
espacio = np.linspace(0, 1, 5)    # 5 puntos iguales entre 0 y 1

# Con tipos de dato específicos
tasas   = np.array([0.08, 0.065, 0.12], dtype=float)
meses   = np.array([3, 6, 12, 24],      dtype=int)

print(f"Precios: {precios}")
print(f"Rango:   {rango}")
print(f"Espacio: {espacio}")
print(f"Tipo:    {precios.dtype}")    # float64
print(f"Forma:   {precios.shape}")   # (5,)
print(f"Tamaño:  {precios.size}")    # 5
```

### Matrices (Arreglos 2D)

```python
# 💡 CONCEPTO — Matrices para datos tabulares

import numpy as np

# Rendimientos semanales de 3 activos (filas) durante 5 días (columnas)
rendimientos = np.array([
    [ 0.031,  0.031,  0.031,  0.031,  0.031],   # CETES (constante)
    [ 0.025,  0.027, -0.003,  0.018,  0.022],   # Bono M
    [ 0.045, -0.023,  0.061, -0.018,  0.038],   # Renta Variable
])

print(f"Forma: {rendimientos.shape}")         # (3, 5) → 3 activos, 5 días
print(f"Dimensiones: {rendimientos.ndim}")   # 2

# Acceso [fila, columna]
print(f"Rendimiento CETES lunes:  {rendimientos[0, 0]:.3%}")
print(f"Rendimiento RV miércoles: {rendimientos[2, 2]:.3%}")

# Fila completa (todos los días de un activo)
print(f"\nBono M toda la semana: {rendimientos[1, :]}")

# Columna completa (todos los activos en un día)
activos = ["CETES", "Bono M", "RV"]
print(f"\nRendimientos del viernes:")
for i, activo in enumerate(activos):
    print(f"  {activo:<10}: {rendimientos[i, 4]:.3%}")
```

### Operaciones Vectorizadas

```python
# 💡 CONCEPTO — Sin for loops, operaciones sobre todo el arreglo

import numpy as np

# Cartera de inversión
capital  = np.array([500_000, 300_000, 150_000, 200_000, 100_000])
tasas    = np.array([0.1125,  0.0920,  0.0430,  0.1580,  0.1050])
nombres  = ["CETES 28d", "Bono M 10a", "Udibono 5a", "Fondo RV", "Bono Corp"]

# Calcular rendimientos anuales de TODOS los activos en una sola línea
rendimientos_anuales = capital * tasas          # Multiplicación elemento a elemento
total_cartera        = capital.sum()
ponderaciones        = capital / total_cartera  # Peso de cada activo

# Rendimiento promedio ponderado de la cartera
rendimiento_cartera  = rendimientos_anuales.sum() / total_cartera

print(f"{'Activo':<15} {'Capital':>12} {'Tasa':>8} {'Rendimiento':>14}")
print("─" * 52)
for i, nombre in enumerate(nombres):
    print(f"{nombre:<15} ${capital[i]:>11,.0f} {tasas[i]:>7.2%} ${rendimientos_anuales[i]:>13,.0f}")
print("─" * 52)
print(f"{'TOTAL':<15} ${total_cartera:>11,.0f}          ${rendimientos_anuales.sum():>13,.0f}")
print(f"\nRendimiento promedio ponderado: {rendimiento_cartera:.2%}")

# Estadísticas rápidas
print(f"\nTasa más alta:  {tasas.max():.2%} ({nombres[tasas.argmax()]})")
print(f"Tasa más baja:  {tasas.min():.2%} ({nombres[tasas.argmin()]})")
print(f"Tasa promedio:  {tasas.mean():.2%}")
```

### ✏️ Ejercicio 3 — Análisis de Precios de Acciones

```python
# ✏️ EJERCICIO 3 — Análisis básico con NumPy

import numpy as np

# Precios de cierre de una acción bancaria durante 10 días
precios = np.array([85.50, 86.20, 84.90, 87.30, 88.10,
                    87.50, 89.20, 88.80, 90.10, 91.50])

# TODO 1: Calcula el rendimiento diario (arreglo de 9 elementos)
# Fórmula: (precio_hoy - precio_ayer) / precio_ayer
rendimientos_diarios = ???

# TODO 2: Calcula el rendimiento total del periodo
# Fórmula: (precio_final - precio_inicial) / precio_inicial
rendimiento_total = ???

# TODO 3: Calcula estas estadísticas con funciones NumPy
precio_maximo   = ???    # np.max() o .max()
precio_minimo   = ???    # np.min() o .min()
precio_promedio = ???    # np.mean() o .mean()
volatilidad     = ???    # np.std() de los rendimientos diarios

print(f"Precio inicial:    ${precios[0]:.2f}")
print(f"Precio final:      ${precios[-1]:.2f}")
print(f"Rendimiento total:  {rendimiento_total:.2%}")
print(f"Precio máximo:     ${precio_maximo:.2f}")
print(f"Precio mínimo:     ${precio_minimo:.2f}")
print(f"Precio promedio:   ${precio_promedio:.2f}")
print(f"Volatilidad:        {volatilidad:.4f}")
```

<details>
<summary>Ver solución</summary>

```python
import numpy as np

precios = np.array([85.50, 86.20, 84.90, 87.30, 88.10,
                    87.50, 89.20, 88.80, 90.10, 91.50])

rendimientos_diarios = (precios[1:] - precios[:-1]) / precios[:-1]
rendimiento_total    = (precios[-1] - precios[0]) / precios[0]
precio_maximo        = precios.max()
precio_minimo        = precios.min()
precio_promedio      = precios.mean()
volatilidad          = np.std(rendimientos_diarios)

print(f"Precio inicial:    ${precios[0]:.2f}")
print(f"Precio final:      ${precios[-1]:.2f}")
print(f"Rendimiento total:  {rendimiento_total:.2%}")
print(f"Precio máximo:     ${precio_maximo:.2f}")
print(f"Precio mínimo:     ${precio_minimo:.2f}")
print(f"Precio promedio:   ${precio_promedio:.2f}")
print(f"Volatilidad:        {volatilidad:.4f}")
```

</details>

### 🤖 Ejercicio 4 — Con apoyo de IA

Pega este prompt en Claude o Gemini:

```
Soy analista en un banco aprendiendo NumPy. Necesito un script que:
1. Cree una matriz NumPy de 5x3 donde:
   - Las 5 filas representan 5 clientes del banco
   - Las 3 columnas son: saldo_ahorro, saldo_inversion, saldo_credito
   - Con valores realistas en pesos mexicanos
2. Calcule para cada cliente (por fila):
   - Saldo neto (ahorro + inversión - crédito)
   - Ratio de endeudamiento (crédito / (ahorro + inversión))
3. Calcule por columna:
   - Promedio de cada tipo de saldo en el banco
   - Suma total por tipo
4. Imprima todo formateado en pesos mexicanos

Comenta cada sección en español.
```

---

## 📚 Recursos

- [Regex101](https://regex101.com) — Prueba tus patrones en tiempo real (selecciona "Python")
- [Documentación módulo re](https://docs.python.org/es/3/library/re.html)
- [Documentación oficial NumPy](https://numpy.org/doc/stable/user/)
- [NumPy para principiantes](https://numpy.org/doc/stable/user/absolute_beginners.html)

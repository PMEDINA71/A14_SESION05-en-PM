# PM Título del concepto: compara listas normales de Python contra arreglos de NumPy.
# 💡 CONCEPTO — Listas vs NumPy: la diferencia clave 

# PM Importamos NumPy y le damos el alias np para trabajar con arreglos numéricos.
import numpy as np

# PM Importamos el módulo time para medir tiempos de ejecución.
import time

# PM Explicamos que con listas normalmente se necesita un bucle o comprensión de listas para operar sobre todos los elementos.
# Con listas: necesitas un bucle para operar sobre todos los elementos

# PM Creamos una lista normal de Python con varios rendimientos.
rendimientos_lista = [0.05, 0.08, 0.03, 0.12, 0.07]

# PM Creamos una nueva lista multiplicando cada rendimiento por 2 usando list comprehension.
# PM La variable r toma cada valor de rendimientos_lista y lo multiplica por 2.
rendimientos_x2 = [r * 2 for r in rendimientos_lista]   # Necesita list comprehension

# PM Explicamos que con NumPy se puede operar directamente sobre todo el arreglo.
# Con NumPy: operación directa sobre todo el arreglo a la vez

# PM Creamos un arreglo de NumPy con los mismos rendimientos de la lista anterior.
rendimientos_np = np.array([0.05, 0.08, 0.03, 0.12, 0.07])

# PM Multiplicamos todos los elementos del arreglo NumPy por 2 en una sola operación.
rendimientos_x2_np = rendimientos_np * 2    # Multiplica TODOS de una vez

# PM Imprimimos el resultado obtenido usando lista de Python.
print(f"Lista:  {rendimientos_x2}")

# PM Imprimimos el resultado obtenido usando arreglo de NumPy.
print(f"NumPy:  {rendimientos_x2_np}")

# PM Explicamos que NumPy suele ser mucho más rápido cuando se trabaja con grandes volúmenes de datos.
# NumPy también es mucho más rápido con datos grandes

# PM Definimos la cantidad de elementos que vamos a usar para comparar rendimiento.
# PM 1_000_000 es igual a un millón; el guion bajo solo mejora la lectura.
N = 1_000_000

# PM Creamos una lista normal de Python con números desde 0 hasta N-1.
lista = list(range(N))

# PM Creamos un arreglo NumPy con números desde 0 hasta N-1.
arreglo = np.arange(N)

# PM Guardamos el tiempo actual antes de ejecutar la operación con lista.
t0 = time.time()

# PM Multiplicamos cada elemento de la lista por 2.5 usando list comprehension.
# PM Esta operación recorre los elementos uno por uno.
[x * 2.5 for x in lista]

# PM Guardamos el tiempo actual después de terminar la operación con lista.
t1 = time.time()

# PM Multiplicamos todos los elementos del arreglo NumPy por 2.5 en una sola operación vectorizada.
arreglo * 2.5

# PM Guardamos el tiempo actual después de terminar la operación con NumPy.
t2 = time.time()

# PM Calculamos e imprimimos el tiempo que tomó la operación con lista en milisegundos.
# PM t1 - t0 mide la duración en segundos y se multiplica por 1000 para convertirlo a milisegundos.
print(f"\nTiempo con lista:  {(t1-t0)*1000:.1f} ms")

# PM Calculamos e imprimimos el tiempo que tomó la operación con NumPy en milisegundos.
# PM t2 - t1 mide la duración en segundos y se multiplica por 1000 para convertirlo a milisegundos.
print(f"Tiempo con NumPy:  {(t2-t1)*1000:.1f} ms")

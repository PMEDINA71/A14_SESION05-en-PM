# PM Título del concepto: muestra diferentes formas de crear arreglos usando NumPy.
# 💡 CONCEPTO — Formas de crear arreglos NumPy

# PM Importamos la librería NumPy y le asignamos el alias np.
import numpy as np

# PM Comentario que indica que vamos a crear un arreglo NumPy a partir de una lista de Python.
# Desde una lista

# PM Creamos un arreglo NumPy llamado precios usando una lista de valores decimales.
precios = np.array([18.50, 19.20, 17.80, 20.10, 19.95])

# PM Comentario que indica que vamos a crear arreglos especiales con funciones de NumPy.
# Arreglos especiales

# PM Creamos un arreglo de 5 elementos, todos con valor 0.
ceros = np.zeros(5)              # [0. 0. 0. 0. 0.]

# PM Creamos un arreglo de 5 elementos, todos con valor 1.
unos = np.ones(5)                # [1. 1. 1. 1. 1.]

# PM Creamos un arreglo desde 0 hasta antes de 10, avanzando de 2 en 2.
rango = np.arange(0, 10, 2)      # [0 2 4 6 8]

# PM Creamos un arreglo con 5 valores igualmente espaciados entre 0 y 1.
espacio = np.linspace(0, 1, 5)   # 5 puntos iguales entre 0 y 1

# PM Comentario que indica que vamos a crear arreglos especificando el tipo de dato.
# Con tipos de dato específicos

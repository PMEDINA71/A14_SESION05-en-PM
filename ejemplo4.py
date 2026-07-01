# PM Título del concepto: uso de matrices NumPy para representar datos tabulares.
# 💡 CONCEPTO — Matrices para datos tabulares

# PM Importamos la librería NumPy y le asignamos el alias np.
import numpy as np

# PM Comentario que explica que las filas representan activos y las columnas representan días.
# Rendimientos semanales de 3 activos (filas) durante 5 días (columnas)

# PM Creamos una matriz NumPy llamada rendimientos.
# PM Cada fila representa un activo financiero.
# PM Cada columna representa un día de la semana.
rendimientos = np.array([
    # PM Primera fila: rendimientos diarios de CETES, constantes durante los 5 días.
    [ 0.031,  0.031,  0.031,  0.031,  0.031],   # CETES (constante)

    # PM Segunda fila: rendimientos diarios del Bono M durante 5 días.
    [ 0.025,  0.027, -0.003,  0.018,  0.022],   # Bono M

    # PM Tercera fila: rendimientos diarios de renta variable durante 5 días.
    [ 0.045, -0.023,  0.061, -0.018,  0.038],   # Renta Variable
])

# PM Imprimimos la forma de la matriz.
# PM El resultado (3, 5) significa 3 filas y 5 columnas.
print(f"Forma: {rendimientos.shape}")         # (3, 5) → 3 activos, 5 días

# PM Imprimimos el número de dimensiones del arreglo.
# PM En este caso es 2 porque es una matriz con filas y columnas.
print(f"Dimensiones: {rendimientos.ndim}")   # 2

# PM Comentario que explica que se puede acceder a un valor usando [fila, columna].
# Acceso [fila, columna]

# PM Imprimimos el rendimiento de CETES del lunes.
# PM La posición [0, 0] significa fila 0, columna 0.
# PM :.3% muestra el número como porcentaje con 3 decimales.
print(f"Rendimiento CETES lunes:  {rendimientos[0, 0]:.3%}")

# PM Imprimimos el rendimiento de renta variable del miércoles.
# PM La posición [2, 2] significa fila 2, columna 2.
print(f"Rendimiento RV miércoles: {rendimientos[2, 2]:.3%}")

# PM Comentario que explica que podemos obtener una fila completa de la matriz.
# Fila completa (todos los días de un activo)

# PM Imprimimos toda la fila del Bono M.
# PM La posición [1, :] significa fila 1 y todas las columnas.
print(f"\nBono M toda la semana: {rendimientos[1, :]}")

# PM Comentario que explica que podemos obtener una columna completa de la matriz.
# Columna completa (todos los activos en un día)

# PM Creamos una lista con los nombres de los activos financieros.
activos = ["CETES", "Bono M", "RV"]

# PM Imprimimos un título para mostrar los rendimientos del viernes.
print(f"\nRendimientos del viernes:")

# PM Recorremos la lista de activos usando enumerate.
# PM i guarda la posición del activo y activo guarda el nombre.
for i, activo in enumerate(activos):

    # PM Imprimimos el rendimiento del viernes para cada activo.
    # PM La columna 4 representa el quinto día, es decir, viernes.
    # PM :<10 alinea el nombre del activo a la izquierda en un espacio de 10 caracteres.
    print(f"  {activo:<10}: {rendimientos[i, 4]:.3%}")


# PM Título del siguiente concepto: operaciones vectorizadas en NumPy.
# Operaciones Vectorizadas

# PM Título del concepto: operaciones sobre arreglos completos sin usar for loops.
# 💡 CONCEPTO — Sin for loops, operaciones sobre todo el arreglo

# PM Importamos nuevamente NumPy con el alias np.
# PM En un archivo real, si ya se importó arriba, esta línea podría omitirse.
import numpy as np

# PM Comentario que indica que vamos a trabajar con una cartera de inversión.
# Cartera de inversión

# PM Creamos un arreglo NumPy con el capital invertido en cada activo.
# PM Los guiones bajos en los números solo ayudan a leerlos mejor.
capital = np.array([500_000, 300_000, 150_000, 200_000, 100_000])

# PM Creamos un arreglo NumPy con las tasas anuales de cada activo.
tasas = np.array([0.1125,  0.0920,  0.0430,  0.1580,  0.1050])

# PM Creamos una lista con los nombres de los activos de la cartera.
nombres = ["CETES 28d", "Bono M 10a", "Udibono 5a", "Fondo RV", "Bono Corp"]

# PM Comentario que explica que calcularemos los rendimientos de todos los activos en una sola línea.
# Calcular rendimientos anuales de TODOS los activos en una sola línea

# PM Multiplicamos capital por tasas elemento a elemento.
# PM Esto calcula el rendimiento anual esperado de cada activo.
rendimientos_anuales = capital * tasas          # Multiplicación elemento a elemento

# PM Sumamos todo el capital invertido para obtener el valor total de la cartera.
total_cartera = capital.sum()

# PM Calculamos la ponderación de cada activo dentro de la cartera.
# PM Cada capital individual se divide entre el total de la cartera.
ponderaciones = capital / total_cartera  # Peso de cada activo

# PM Comentario que indica que calcularemos el rendimiento promedio ponderado de la cartera.
# Rendimiento promedio ponderado de la cartera

# PM Sumamos los rendimientos anuales y los dividimos entre el capital total.
# PM Esto da la tasa promedio ponderada de toda la cartera.
rendimiento_cartera = rendimientos_anuales.sum() / total_cartera

# PM Imprimimos el encabezado de la tabla con alineación de columnas.
print(f"{'Activo':<15} {'Capital':>12} {'Tasa':>8} {'Rendimiento':>14}")

# PM Imprimimos una línea separadora para mejorar la lectura de la tabla.
print("─" * 52)

# PM Recorremos la lista de nombres usando enumerate.
# PM i representa la posición y nombre representa el nombre del activo.
for i, nombre in enumerate(nombres):

    # PM Imprimimos una fila por cada activo.
    # PM Mostramos nombre, capital, tasa y rendimiento anual.
    # PM :<15 alinea el nombre a la izquierda.
    # PM :>11,.0f muestra el capital con comas y sin decimales.
    # PM :>7.2% muestra la tasa como porcentaje con 2 decimales.
    # PM :>13,.0f muestra el rendimiento con comas y sin decimales.
    print(f"{nombre:<15} ${capital[i]:>11,.0f} {tasas[i]:>7.2%} ${rendimientos_anuales[i]:>13,.0f}")

# PM Imprimimos otra línea separadora para cerrar el detalle de activos.
print("─" * 52)

# PM Imprimimos el total de capital invertido y el total de rendimiento anual esperado.
print(f"{'TOTAL':<15} ${total_cartera:>11,.0f}          ${rendimientos_anuales.sum():>13,.0f}")

# PM Imprimimos el rendimiento promedio ponderado de la cartera como porcentaje.
print(f"\nRendimiento promedio ponderado: {rendimiento_cartera:.2%}")

# PM Comentario que indica que vamos a calcular estadísticas rápidas sobre las tasas.
# Estadísticas rápidas

# PM Imprimimos la tasa más alta del arreglo tasas.
# PM tasas.max() devuelve el valor máximo.
# PM tasas.argmax() devuelve la posición donde está la tasa más alta.
# PM Usamos esa posición para encontrar el nombre del activo correspondiente.
print(f"\nTasa más alta:  {tasas.max():.2%} ({nombres[tasas.argmax()]})")

# PM Imprimimos la tasa más baja del arreglo tasas.
# PM tasas.min() devuelve el valor mínimo.
# PM tasas.argmin() devuelve la posición donde está la tasa más baja.
# PM Usamos esa posición para encontrar el nombre del activo correspondiente.
print(f"Tasa más baja:  {tasas.min():.2%} ({nombres[tasas.argmin()]})")

# PM Imprimimos la tasa promedio simple de todos los activos.
# PM tasas.mean() calcula el promedio aritmético de las tasas.
print(f"Tasa promedio:  {tasas.mean():.2%}")
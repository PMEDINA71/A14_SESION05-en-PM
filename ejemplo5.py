# 💡 CONCEPTO — Sin for loops, operaciones sobre todo el arreglo
# PM Título del concepto: NumPy permite hacer operaciones sobre arreglos completos sin usar bucles manuales.
# 💡 CONCEPTO — Sin for loops, operaciones sobre todo el arreglo

# PM Importamos la librería NumPy y le damos el alias np para trabajar con arreglos numéricos.
import numpy as np

# PM Comentario que indica que vamos a definir una cartera de inversión.
# Cartera de inversión

# PM Creamos un arreglo NumPy con el capital invertido en cada activo.
# PM Los guiones bajos en los números, como 500_000, solo ayudan a leer mejor el número.
capital = np.array([500_000, 300_000, 150_000, 200_000, 100_000])

# PM Creamos un arreglo NumPy con la tasa anual correspondiente a cada activo.
tasas = np.array([0.1125,  0.0920,  0.0430,  0.1580,  0.1050])

# PM Creamos una lista de Python con los nombres de los activos de inversión.
nombres = ["CETES 28d", "Bono M 10a", "Udibono 5a", "Fondo RV", "Bono Corp"]

# PM Comentario que indica que calcularemos los rendimientos anuales de todos los activos en una sola operación.
# Calcular rendimientos anuales de TODOS los activos en una sola línea

# PM Multiplicamos capital por tasas elemento a elemento.
# PM Esto calcula el rendimiento anual esperado de cada activo.
rendimientos_anuales = capital * tasas          # Multiplicación elemento a elemento

# PM Sumamos todos los capitales para obtener el valor total de la cartera.
total_cartera = capital.sum()

# PM Calculamos el peso o participación de cada activo dentro del total de la cartera.
# PM Cada capital individual se divide entre el total de la cartera.
ponderaciones = capital / total_cartera  # Peso de cada activo

# PM Comentario que indica que calcularemos el rendimiento promedio ponderado de la cartera.
# Rendimiento promedio ponderado de la cartera

# PM Sumamos todos los rendimientos anuales y los dividimos entre el capital total.
# PM Esto calcula la tasa promedio ponderada de toda la cartera.
rendimiento_cartera = rendimientos_anuales.sum() / total_cartera

# PM Imprimimos el encabezado de la tabla con columnas alineadas.
# PM Activo se alinea a la izquierda con 15 espacios.
# PM Capital se alinea a la derecha con 12 espacios.
# PM Tasa se alinea a la derecha con 8 espacios.
# PM Rendimiento se alinea a la derecha con 14 espacios.
print(f"{'Activo':<15} {'Capital':>12} {'Tasa':>8} {'Rendimiento':>14}")

# PM Imprimimos una línea separadora de 52 caracteres para mejorar la presentación.
print("─" * 52)

# PM Recorremos la lista de nombres usando enumerate.
# PM i guarda el índice o posición del activo.
# PM nombre guarda el nombre del activo.
for i, nombre in enumerate(nombres):

    # PM Imprimimos una fila de la tabla para cada activo.
    # PM nombre muestra el nombre del activo alineado a la izquierda.
    # PM capital[i] toma el capital correspondiente al activo actual.
    # PM tasas[i] toma la tasa correspondiente al activo actual.
    # PM rendimientos_anuales[i] toma el rendimiento calculado para ese activo.
    # PM ,.0f muestra números con separador de miles y sin decimales.
    # PM .2% muestra la tasa como porcentaje con 2 decimales.
    print(f"{nombre:<15} ${capital[i]:>11,.0f} {tasas[i]:>7.2%} ${rendimientos_anuales[i]:>13,.0f}")

# PM Imprimimos otra línea separadora antes de mostrar los totales.
print("─" * 52)

# PM Imprimimos la fila de total de la cartera.
# PM total_cartera muestra el capital total invertido.
# PM rendimientos_anuales.sum() muestra la suma total de rendimientos anuales.
print(f"{'TOTAL':<15} ${total_cartera:>11,.0f}          ${rendimientos_anuales.sum():>13,.0f}")

# PM Imprimimos el rendimiento promedio ponderado de la cartera como porcentaje con 2 decimales.
print(f"\nRendimiento promedio ponderado: {rendimiento_cartera:.2%}")

# PM Comentario que indica que vamos a mostrar estadísticas rápidas sobre las tasas.
# Estadísticas rápidas

# PM Imprimimos la tasa más alta de la cartera.
# PM tasas.max() obtiene el valor máximo dentro del arreglo tasas.
# PM tasas.argmax() obtiene la posición donde se encuentra la tasa más alta.
# PM nombres[tasas.argmax()] obtiene el nombre del activo con la tasa más alta.
print(f"\nTasa más alta:  {tasas.max():.2%} ({nombres[tasas.argmax()]})")

# PM Imprimimos la tasa más baja de la cartera.
# PM tasas.min() obtiene el valor mínimo dentro del arreglo tasas.
# PM tasas.argmin() obtiene la posición donde se encuentra la tasa más baja.
# PM nombres[tasas.argmin()] obtiene el nombre del activo con la tasa más baja.
print(f"Tasa más baja:  {tasas.min():.2%} ({nombres[tasas.argmin()]})")

# PM Imprimimos la tasa promedio simple de todos los activos.
# PM tasas.mean() calcula el promedio aritmético de las tasas.
print(f"Tasa promedio:  {tasas.mean():.2%}")
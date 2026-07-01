# 💡 CONCEPTO — Las funciones más importantes del módulo re
# PM Importamos el módulo re, que permite trabajar con expresiones regulares en Python.
import re

# PM re.fullmatch() valida que toda la cadena cumpla exactamente con el patrón definido.
# PM re.search() busca si existe una coincidencia en cualquier parte del texto.
# PM re.findall() busca todas las coincidencias y las devuelve en una lista.
# PM re.sub() reemplaza coincidencias encontradas por otro texto.

# PM Definimos una función para validar si una CLABE tiene el formato correcto.
def validar_clabe(clabe):
    # PM Validamos que la CLABE tenga exactamente 18 dígitos numéricos.
    return bool(re.fullmatch(r'^\d{18}$', clabe))

# PM Probamos una CLABE válida de 18 dígitos; debe devolver True.
print(validar_clabe("032180000118359719"))   # True

# PM Probamos una CLABE inválida porque solo tiene 16 dígitos; debe devolver False.
print(validar_clabe("0321800001183597"))     # False

# PM Probamos una CLABE inválida porque contiene una letra al final; debe devolver False.
print(validar_clabe("03218000011835971X"))   # False


# PM Definimos una función para validar un RFC de persona física.
def validar_rfc(rfc):
    # PM Convertimos el RFC a mayúsculas y validamos su estructura con una expresión regular.
    # PM El patrón espera 4 letras, 6 números de fecha y 3 caracteres alfanuméricos.
    return bool(re.fullmatch(r'^[A-ZÑ&]{4}\d{6}[A-Z0-9]{3}$', rfc.upper()))

# PM Probamos un RFC válido; debe devolver True.
print(validar_rfc("GARA850312XY3"))    # True

# PM Probamos un RFC inválido porque está incompleto; debe devolver False.
print(validar_rfc("GARA850312"))       # False


# PM Creamos una variable de texto que contiene información de una transferencia bancaria.
texto = """
Estimado cliente, su transferencia por $15,000.00 fue procesada.
Número de referencia: REF-2024-00891.
Contacto: soporte@banco.mx | Tel: 5512348765
"""

# PM Buscamos todos los montos en formato de dinero dentro del texto.
montos = re.findall(r'\$[\d,]+\.?\d*', texto)

# PM Buscamos todas las referencias con formato REF-año-número.
referencias = re.findall(r'REF-\d{4}-\d{5}', texto)

# PM Buscamos todos los correos electrónicos dentro del texto.
correos = re.findall(r'[\w.\-]+@[\w\-]+\.[a-z]{2,5}', texto)

# PM Imprimimos la lista de montos encontrados en el texto.
print(f"Montos:      {montos}")         # ['$15,000.00']

# PM Imprimimos la lista de referencias encontradas en el texto.
print(f"Referencias: {referencias}")   # ['REF-2024-00891']

# PM Imprimimos la lista de correos electrónicos encontrados en el texto.
print(f"Correos:     {correos}")        # ['soporte@banco.mx']


# PM Guardamos un número telefónico con espacios y guion.
telefono_raw = "55 1234-5678"

# PM Eliminamos espacios y guiones del número telefónico usando re.sub().
telefono_limpio = re.sub(r'[\s\-]', '', telefono_raw)

# PM Imprimimos el teléfono ya limpio, solo con números.
print(f"Teléfono limpio: {telefono_limpio}")    # 5512345678


# PM Guardamos una CLABE completa para después ocultar parte de ella.
clabe = "032180000118359719"

# PM Enmascaramos la CLABE mostrando solo los primeros 3 dígitos y los últimos 2.
# PM Los 13 dígitos del centro se reemplazan por asteriscos.
clabe_oculta = re.sub(r'(\d{3})\d{13}(\d{2})', r'\1*************\2', clabe)

# PM Imprimimos la CLABE enmascarada.
print(f"CLABE oculta: {clabe_oculta}")           # 032*************19
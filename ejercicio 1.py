# PM Título del ejercicio: completar funciones de validación usando expresiones regulares.
# ✏️ EJERCICIO 1 — Completa las funciones de validación

# PM Importamos el módulo re, que permite usar expresiones regulares en Python.
import re

# PM Definimos la función validar_correo, que recibe como parámetro un correo.
def validar_correo(correo):
    # PM Documentamos que esta función valida un correo con formato usuario@dominio.extensión.
    """Valida que sea un correo con formato user@dominio.ext"""

    # PM Creamos un patrón para validar correos electrónicos básicos.
    # PM ^ indica el inicio del texto.
    # PM [\w.\-]+ permite letras, números, guion bajo, punto y guion antes del @.
    # PM @ exige que exista el símbolo arroba.
    # PM [\w\-]+ permite letras, números, guion bajo y guion para el dominio.
    # PM \. exige que exista un punto antes de la extensión.
    # PM [a-zA-Z]{2,5} valida una extensión de 2 a 5 letras.
    # PM $ indica el final del texto.
    patron = r'^[\w.\-]+@[\w\-]+\.[a-zA-Z]{2,5}$'

    # PM re.fullmatch valida que todo el correo coincida exactamente con el patrón.
    # PM bool convierte el resultado en True si coincide o False si no coincide.
    return bool(re.fullmatch(patron, correo))

# PM Definimos la función validar_telefono, que recibe como parámetro un teléfono.
def validar_telefono(tel):
    # PM Documentamos que esta función valida un teléfono de 10 dígitos.
    """Valida teléfono de 10 dígitos (con o sin espacios/guiones)"""

    # PM Limpiamos el teléfono eliminando espacios, guiones y paréntesis.
    # PM \s representa espacios en blanco.
    # PM \- representa guiones.
    # PM \( y \) representan paréntesis.
    # PM El segundo parámetro '' indica que esos caracteres serán reemplazados por nada.
    tel_limpio = re.sub(r'[\s\-\(\)]', '', tel)

    # PM Creamos un patrón que exige exactamente 10 dígitos numéricos.
    # PM ^ indica el inicio del texto.
    # PM \d representa cualquier dígito del 0 al 9.
    # PM {10} exige exactamente 10 repeticiones.
    # PM $ indica el final del texto.
    patron = r'^\d{10}$'

    # PM Validamos que el teléfono limpio coincida completamente con el patrón.
    # PM Devuelve True si tiene exactamente 10 dígitos o False si no cumple.
    return bool(re.fullmatch(patron, tel_limpio))

# PM Definimos la función enmascarar_tarjeta, que recibe un número de tarjeta.
def enmascarar_tarjeta(numero):
    # PM Documentamos que esta función convierte una tarjeta completa en formato oculto.
    """Convierte '4111111111111234' en '****-****-****-1234'"""

    # ✏️ EJERCICIO 1 — Completa las funciones de validación

import re

def validar_correo(correo):
    """Valida que sea un correo con formato user@dominio.ext"""
    patron = r'^[\w.\-]+@[\w\-]+\.[a-zA-Z]{2,5}$'
    return bool(re.fullmatch(patron, correo))

def validar_telefono(tel):
    """Valida teléfono de 10 dígitos (con o sin espacios/guiones)"""
    tel_limpio = re.sub(r'[\s\-\(\)]', '', tel)
    patron = r'^\d{10}$'
    return bool(re.fullmatch(patron, tel_limpio))

def enmascarar_tarjeta(numero):
    """Convierte '4111111111111234' en '****-****-****-1234'"""
    return re.sub(r'^(\d{12})(\d{4})$', r'****-****-****-\2', numero)


# Pruebas
print(validar_correo("usuario@banco.mx"))      # True
print(validar_correo("usuario@"))              # False
print(validar_telefono("55 1234-5678"))        # True
print(validar_telefono("123"))                 # False
print(enmascarar_tarjeta("4111111111111234"))  # ****-****-****-1234
# Crea un script que solicite una contraseña, analice si es segura y si no lo es
# sugiera una nueva contraseña. Para ello puedes crear un script validador.py
# que contenga una funcion validar_contrasena que reciba una cadena y
# verifique si cumple con los requisitos mínimos de una contraseña segura
# (por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
# minúsculas, números y caracteres especiales). La función debe devolver un
# valor booleano que indique si la contraseña es válida o no. Por otro lado
# puedes crear otro script creador.py con una función llamada
# generar_contrasena que genere contraseñas seguras de forma aleatoria. La
# función debe permitir especificar la longitud de la contraseña y qué tipos de
# caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
# minúsculas, números y caracteres especiales).
# (Para el generador de contraseñas puedes probar a usar los modulos
# random y string)

import random
import string

def generar_contrasena(longitud=12, usar_mayus=True, usar_minus=True, usar_num=True, usar_esp=True):
    caracteres = ""
    
    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_num:
        caracteres += string.digits
    if usar_esp:
        caracteres += string.punctuation

    if not caracteres:
        return "Debes seleccionar al menos un tipo de carácter."

    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
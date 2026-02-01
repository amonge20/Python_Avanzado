# Crea un programa que valide un formulario de registro. Crea una función
# llamada validar_formulario que reciba diferentes campos de un formulario
# (nombre, correo electrónico y número de teléfono) y verifique si los valores
# ingresados cumplen con los requisitos especificados, siendo estos:
# 1. Que el nombre tenga una longitud minima de 3 caracteres
# 2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
# caracteres
# 3. Que el email contenga un “@“ y un “.”

# Funcion para los requisitos del usuario
def usuario(nombre, correo_electronico, numTelf):
    if len(nombre) < 3:
        return "Tiene que tener como minimo 3 caracteres"
    
    if "@" not in correo_electronico or "." not  in correo_electronico:
        return "Correo electronico no valido"
    
    if not numTelf.isdigit() or len(numTelf) != 9:
        return "Numero de telefono no valido"        
    
    return "Registro realizado"

# Resultado    
print(usuario(nombre="Aitor",correo_electronico="aitor@gmail.com",numTelf="123456789"))
print(usuario(nombre="Pa",correo_electronico="paz@gmail.com",numTelf="123456789"))
print(usuario(nombre="Juan",correo_electronico="juangmail.com",numTelf="123456789"))
print(usuario(nombre="Paco",correo_electronico="pacogmailcom",numTelf="123456789"))
print(usuario(nombre="Maria",correo_electronico="maria@gmail.com",numTelf="1234567@$"))
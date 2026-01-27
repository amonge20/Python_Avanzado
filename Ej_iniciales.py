# 1. Define una función llamada "saludar" que tome un parámetro "nombre"
# y muestre un saludo personalizado.
def saludar(nombre):
    print("Hola",nombre)
# 2. Crea una función llamada "suma" que tome dos parámetros "a" y "b" e
# imprima la suma de ambos.
def suma(a,b):
    print(a+b)
# 3. Escribe una función llamada "calcular_area_rectangulo" que tome dos
# parámetros "base" y "altura" y calcule el área de un rectángulo.
def calcular_area_rectangulo(base,altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro
# 4. Define una función llamada "imprimir_lista" que tome una lista como
# parámetro y la imprima en la consola.
def imprimir_lista(lista):
    for numero in lista:
        print(numero)
# 5. Crea una función llamada "es_par" que tome un número como
# parámetro e imprima True si es par, o False si es impar.
def es_par(numero):
    return numero % 2 == 0
# 6. Escribe una función llamada "concatenar_strings" que tome dos
# parámetros "cadena1" y “cadena2" e imprima la concatenación de
# ambas cadenas.
def concatenar_strings(cadena1, cadena2):
    return cadena1 + cadena2

# 7. Define una función llamada "obtener_maximo" que tome una lista de
# números como parámetro y devuelva el número máximo de la lista.
def obtener_maximo(lista):
    return max(lista)
# 8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un
# parámetro "fahrenheit" y devuelva su equivalente en grados Celsius.
def convertir_fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
# 9. Escribe una función llamada "calcular_edad" que tome dos parámetros:
# "año_actual" y "año_nacimiento" y calcule la edad de una persona.
def calcular_edad(año_actual,año_nacimiento):
    return año_actual - año_nacimiento
# 10. Define una función llamada "es_divisible" que tome dos parámetros
# "num" y "divisor" e imprima True si "num" es divisible por "divisor", o
# False si no lo es.
def es_divisible(num, divisor):
    return num % divisor == 0 or divisor % num == 0
# 11. Crea una función llamada "mostrar_info_persona" que tome tres
# argumentos de palabra clave: "nombre", "edad" y "ciudad". La función
# debe imprimir en la consola la información de una persona en un
# formato legible.
def mostrar_info_persona(nombre,edad,ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
# 12. Escribe una función llamada "calcular_promedio" que tome una lista de
# números como parámetro y calcule el promedio de esos números. Si no
# se proporciona una lista, debe usar una lista vacía por defecto.
def calcular_promedio(numeros=[]):
    if len(numeros) == 0:
        return 0
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return promedio
# 13. Crea una función llamada "calcular_potencia" que tome dos
# parámetros "base" y "exponente", y calcule la potencia de la base
# elevada al exponente. Utiliza 2 como valor por defecto para el
# exponente.
def calcular_potencia(base,exponente):
    return base ** exponente
# 14. Define una función llamada "imprimir_info_alumno" que tome un
# argumento posicional “nombre”(y sin valor por defecto) y varios
# argumentos de palabra clave: "edad", "curso" y “promedio" (puedes
# ponerles como valor por defecto None). La función debe imprimir la
# información del alumno en un formato legible.
def imprimir_info_alumno(nombre, edad=None, curso=None, promedio=None):
    print(f"Información del alumno:")
    print(f"Nombre: {nombre}")
    if edad is not None:
        print(f"Edad: {edad}")
    if curso is not None:
        print(f"Curso: {curso}")
    if promedio is not None:
        print(f"Promedio: {promedio}")

# Resultado
saludar("Aitor")
suma(5,2)
a,p = calcular_area_rectangulo(5,3)
print("Área:", a)
print("Perímetro:", p)
numeros = [1,2,3,4,5,6,7,8,9,10]
imprimir_lista(numeros)
print(es_par(4))
print(es_par(5))
resultado = concatenar_strings("Pseudo","codigo")
print(resultado)
print(obtener_maximo(numeros))
print(es_divisible(1,2))
print(es_divisible(2,4))
print(es_divisible(4,2))
print(es_divisible(5,4))
mostrar_info_persona("Aitor",20,"Barcelona")
print(calcular_promedio([10, 20, 30]))  
print(calcular_promedio([5, 15]))       
print(calcular_promedio())              
print(calcular_promedio([]))             
print(calcular_potencia(5,2))
imprimir_info_alumno("Aitor", edad=20, curso="Python Básico", promedio=9.5)
imprimir_info_alumno("Lucía", curso="Matemáticas")
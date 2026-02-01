# Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
# estructura de datos adecuada para almacenar la información de las ventas
# (por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
# agregar el producto vendido con su precio y otro para mostrar las ventas de
# productos con sus respectivos precios.
# (La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
# precio1}, {“Producto”: producto2, “Precio”: precio2}…])

# Lista de productos
Ventas = []

def anadir_producto(fruta, precio):
    producto = {"Producto": fruta, "Precio": precio}
    Ventas.append(producto)

def mostrar_ventas():
    if not Ventas:
        print("No hay ventas registradas")
    else:
        print("Ventas registradas.")
        for item in Ventas:
            print(f"Producto: {item['Producto']} - Precio: ${item['Precio']}")

# Resultado
anadir_producto("Manzana", 0.50)
anadir_producto("Pan", 1.20)
anadir_producto("Leche", 0.95)

mostrar_ventas()
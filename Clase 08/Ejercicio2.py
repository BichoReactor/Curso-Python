"""
Actualización del inventario a partir de un arreglo

En una tienda, es necesario actualizar el inventario cuando se venden productos.
A continuación, te proporcionamos un arreglo con una lista de productos,
donde cada producto tiene un código, una descripción y una cantidad en stock. 
Escribí un programa que permita:

- Seleccionar un producto a partir de su código.
- Ingresar la cantidad vendida (que debe ser mayor que cero).
- Actualizar la cantidad en stock de ese producto restando la cantidad vendida.

El arreglo de productos disponibles es el que ves a continuación.

productos = [["P001", "Manzanas", 50], ["P002", "Peras", 40], ["P003", "Bananas", 30], ["P004", "Naranjas", 60]]

El script que tenés que hacer debe modificar la cantidad en stock de acuerdo a cada venta realizada.
Si la cantidad vendida es mayor que la cantidad disponible en stock, 
el programa debe mostrar un mensaje de error.
"""

productos = [
    ["P001", "Manzanas", 50],
    ["P002", "Peras", 40],
    ["P003", "Bananas", 30], 
    ["P004", "Naranjas", 60],
    ["P005", "Uvas", 50],
    ["P006", "Frutillas", 40],
    ["P007", "Kiwis", 30], 
    ["P008", "Mandarinas", 60],
    ["P009", "Guindas", 30], 
    ["P010", "Duraznos", 60]
]

# Le muestro al usuario los productos existentes:
print("Lista de productos")
print("------------------")

for producto in productos:
    print("Lista de productos", producto)

# Solicito al usuario que ingrese el código del producto:
print("")
producto_codigo = input("Ingrese el código del producto: ")
producto_nombre = ""

codigo_valido = False

for producto in productos:
    if producto[0] == producto_codigo:
        producto_nombre = producto[1]
        codigo_valido = True
        break

if codigo_valido:
    productos_cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {producto_nombre} ({producto_codigo}): "))

    if productos_cantidad_vendida <= 0:
        print("Error: La cantidad vendida debe ser mayor a 0(cero)")
    elif productos_cantidad_vendida > producto[2]:
        print("Error: No se pueden vender más productos de lo que existen en stock.")
    else:
        print(f"Se vendieron {productos_cantidad_vendida} de {producto_nombre}")
        
        # Actualizo el stock:
        for producto in productos:
            if producto[0] == producto_codigo:
                producto[2] = producto[2] - productos_cantidad_vendida
                break
        
        # Muestro cómo quedó el stock:
        print()
        print("Lista de productos")
        print("------------------")

        for producto in productos:
            print("Lista de productos", producto)
else:
    print("Error: El código de producto ingresado no existe.")
        


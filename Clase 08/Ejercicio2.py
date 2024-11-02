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
    ["P004", "Naranjas", 60]
]

producto_codigo = input("Ingrese el código del producto: ")

i = 0
productos_cantidad = len(productos)

codigo_valido = False

while i < productos_cantidad:
    if productos[i] == producto_codigo:
        codigo_valido = True
        producto_indice = i
        break
    i += 1

if codigo_valido:
    productos_cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {productos[producto_indice][1]} ({productos[producto_indice][0]}): "))

    if productos_cantidad_vendida <= 0:
        print("Error: La cantidad vendida debe ser mayor a 0(cero)")
    elif productos_cantidad_vendida > productos[producto_indice][2]:
        print("Error: No se pueden vender más productos de lo que existe en stock.")
else:
    print("Error: El código de producto ingresado no existe.")
        


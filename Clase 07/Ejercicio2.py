"""
Consultar el stock de productos

Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está en stock.
Si el producto está en la lista, el programa debe informarlo, si no, debe mostrar un mensaje indicando que no está disponible.

Tips:
- Usá una lista para almacenar los productos en stock.
- Permití que el usuario ingrese el nombre de un producto a consultar.
- Recorré la lista con un bucle while para verificar si el producto está en stock.
"""

productos_stock = ["Banana", "Frutilla", "Mandarina", "Manzana", "Pera", "Uva"]

producto_a_consultar = input("¿Qué producto desea consultar? ")

i = 0
esta = False

while i < len(productos_stock) and not esta:
    if producto_a_consultar.lower() == productos_stock[i].lower():
        esta = True
    
    i += 1

print()
if esta:
    print(f"El producto {producto_a_consultar.capitalize()} se encuentra disponible.")
else:
    print(f"El producto {producto_a_consultar.capitalize()} NO se encuentra disponible.")
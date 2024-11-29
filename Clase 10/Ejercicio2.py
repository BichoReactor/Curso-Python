"""
Consultar stock en inventario

El inventario de una tienda está almacenado en un diccionario,
donde las claves son los nombres de los productos y los valores son las cantidades disponibles en stock.
Creá un programa que:
- Te permita ingresar el nombre de un producto.
- Utilice el método .get() para buscar el stock disponible. 
Si el producto no existe, deberá mostrar un mensaje diciendo "Producto no encontrado".

Si el producto está disponible, mostrará cuántas unidades quedan en stock.
"""

# Diccionario inicial:
productos = {
    "Manzanas": 50,
    "Naranjas": 30,
    "Peras": 25
}

producto_nombre = input("Ingrese el nombre del producto: ")

producto_stock = productos.get(producto_nombre, 0)

if producto_stock == 0:
    print("Producto no encontrado")
else:
    print(f"Stock disponible de {producto_nombre}: {producto_stock}")
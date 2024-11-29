"""
Gestión de inventario con diccionarios

En un comercio, se necesita gestionar los productos y sus precios.
Desarrollá un programa que permita:
- Ingresar el nombre de tres productos y su precio correspondiente,
guardándolos en un diccionario donde la clave es el nombre del producto y el valor es su precio.
- Una vez ingresados, mostrará todos los productos y sus precios en pantalla.

Ejemplo de salida esperada:
Producto: Manzanas, Precio: 100
Producto: Naranjas, Precio: 150
Producto: Peras, Precio: 120
"""

productos = {}

for _ in range(3):
    producto_nombre = input("Ingresá el nombre del producto: ")
    producto_precio = float(input("Ingresá el precio del producto: "))
    
    productos[producto_nombre] = producto_precio
    
print("Productos:")

for nombre, precio in productos.items():
    print("Producto:", nombre, "- Precio:", precio)
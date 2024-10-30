"""
Registro de productos en un inventario

Vas a implementar un sistema básico para registrar productos en el inventario de una tienda.
El programa debe permitir que el usuario agregue productos a una lista hasta que decida no agregar más.
Luego, deberás mostrar todos los productos ingresados al inventario.

Tips:

Usá una lista para almacenar los productos. Diseña la lista pensando en el TFI.
"""

inventario = []
producto   = ""

while producto.lower() != 'x':
    producto = input("Ingrese un producto (o 'x' si desea finalizar): ")
    
    if producto.lower() != 'x':
        inventario.append(producto)

print(f"Productos en el inventario: {inventario}")
        
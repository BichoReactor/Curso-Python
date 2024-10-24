"""
Control de inventario de una tienda de videojuegos

Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario.
El dueño te pide que escribas un programa que verifique si hay stock suficiente de un videojuego y, 
si no hay, que avise que hay que reponerlo.
El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad, 
mostrar si se necesita hacer un nuevo pedido o no.
"""

UMBRAL_STOCK = 10

stock_actual = int(input("Ingrese el stock actual del producto: "))

if stock_actual < UMBRAL_STOCK:
    print("Bajo stock")
else:
    print("Stock suficiente")
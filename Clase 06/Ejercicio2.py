"""
Validación de precios de productos

Escribí un programa que permita al usuario ingresar el precio de un producto,
pero que sólo acepte valores mayores a 0.
Si el usuario ingresa un valor inválido (negativo o cero),
el programa debe mostrar un mensaje de error,
y volver a pedir el valor hasta que se ingrese uno válido.
Al final, el programa debe mostrar el precio aceptado.

Tips:
- Antes de empezar, pensá si es necesario usar contadores o acumuladores.
- Recordá que input() siempre devuelve cadenas de caracteres.
"""

while True:
    producto_precio = int(input("Ingrese el precio del producto: "))
    
    if producto_precio > 0:
        print(f"El precio del producto es {producto_precio}")
        break
    else:
        print("Error: El precio ingresado no es válido.")


"""
Control de stock de productos

Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y la cantidad en stock que hay de cada uno.
El programa debe seguir pidiendo que ingrese productos hasta que el usuario decida salir, ingresando "salir" como nombre de producto.
Después de que el bucle termine, el programa debe mostrar la cantidad total de productos ingresados.

Tips:
- Vas a necesitar un contador.
- Tené presente las estructuras condicionales.
"""
producto = ""

while True:
    # Menú de opciones:
    producto = input("Ingrese un producto o esciba 'salir' para terminar: ")

    if producto.lower() == "salir":
        print("Hasta luego. Gracias por utilizar nuestro software.")
        break
    else:
        cantidad = int(input("Ingrese el stock del producto: "))
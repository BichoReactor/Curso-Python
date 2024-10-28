lista_productos = []

while True:
    # Menú de opciones:
    print("----------------------------")
    print("Menú de Gestión de Productos")
    print("----------------------------")
    print()
    print("1. Alta de productos nuevos")
    print("2. Consulta de datos de productos")
    print("3. Modificar la cantidad en stock de un producto")
    print("4. Dar de baja productos")
    print("5. Listado completo de productos")
    print("6. Lista de productos con cantidad bajo mínimo")
    print("7. Salir")
    print()
    # Solicitar al usuario que seleccione una opción:
    opcion = int(input("Por favor, seleccione una opción: "))

    # Inicializo las variables:
    producto_nombre = ""
    producto_cantidad = 0
    
    match opcion:
        case 1:
            producto_nombre   = (input(f"Nombre del producto: "))
            producto_cantidad = int(input(f"Cantidad de unidades del producto: "))
            
            lista_productos.append(producto_nombre)
            lista_productos.append(producto_cantidad)
        case 2:
            """Nada"""
        case 3:
            """Nada"""
        case 4:
            """Nada"""
        case 5:
            print(f"Lista de productos: {lista_productos}")
        case 6:
            """Nada"""
        case 7:
            print("Hasta luego. Gracias por utilizar nuestro software.")
            break
        case _:
            print("Opción Incorrecta.")
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

# Mostramos el número de la opción seleccionada:
print(f"Ha seleccionado la opción {opcion}")

match opcion:
    case 1:
        """Nada"""
    case 2:
        """Nada"""
    case 3:
        """Nada"""
    case 4:
        """Nada"""
    case 5:
        """Nada"""
    case 6:
        """Nada"""
    case 7:
        """Nada"""
    case _:
        print("Opción Incorrecta")
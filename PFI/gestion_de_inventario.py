from funciones_db import db_crear_tabla
import funciones_menu

# Conecto con la DB:
db_crear_tabla()

# Declaración de variables globales:
opcion = "0"
    
while opcion != "7":
    # Menú de opciones:
    opcion = funciones_menu.crear_menu()
    
    # En lugar de if-elif-else uso match que me parece más claro.
    match opcion:
        case "1":
            funciones_menu.registrar_producto()
        case "2":
            funciones_menu.mostrar_productos()
        case "3":
            funciones_menu.actualizar_producto()
        case "4":
            funciones_menu.eliminar_producto()
        case "5":
            funciones_menu.buscar_producto()
        case "6":
            funciones_menu.reporte_bajo_stock()
        case "7":
            funciones_menu.salir_de_aplicacion()        
        case _:
            funciones_menu.opcion_incorrecta()    
    
    print("")
    continuar = input("Ingrese 'S' para salir, o cualquier otra letra para continuar: ").lower()
    
    if continuar == 's':    
        print("")
        print("Hasta luego. Gracias por utilizar nuestra app.")
        break
    
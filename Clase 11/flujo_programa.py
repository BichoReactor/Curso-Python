def mostrar_menu():
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Salir")

def agregar_producto():
    print("Producto agregado.")
    
def ver_productos():
    print("Estos son los productos.")
    
def iniciar_programa():
    while True:
        mostrar_menu()
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intentá de nuevo.")

iniciar_programa()
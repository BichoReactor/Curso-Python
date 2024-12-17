from funciones_db import db_insertar_producto, db_mostrar_productos, db_mostrar_producto, db_actualizar_producto, db_eliminar_producto, db_reporte_bajo_stock
from funciones_validacion import get_producto_nombre, get_producto_descripcion, get_producto_categoria, get_producto_precio, get_producto_cantidad, get_id
from colorama import init, Fore, Style

# Inicializo Colorama:
init(autoreset=True)

# Crea el menú de usuario:
def crear_menu():
    print()
    print(Fore.BLUE + "-"*32)
    print(Fore.BLUE + Style.BRIGHT + "| Menú de Gestión de Productos |")
    print(Fore.BLUE + "-"*32)
    print()
    print("1. Agegar producto")
    print("2. Listado de productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de bajo stock")
    print(Style.DIM + "7. Salir")
    print()

    # Solicitar al usuario que seleccione una opción:
    # Aclaración: al no convertir a int el valor de opción salvo el caso en que el usuario ingresa algo que no sea numérico.
    opcion = input(Fore.GREEN + "Por favor, seleccione una opción: ")
    
    return opcion

def registrar_producto():
    # Ingreso de datos:
    print("")
    print(Fore.GREEN + Style.BRIGHT + "Ingrese los datos del producto que desea registrar.")
    print(Fore.GREEN + "-"*51)
    producto_nombre      = get_producto_nombre()
    producto_descripcion = get_producto_descripcion()
    producto_categoria   = get_producto_categoria()
    producto_precio      = get_producto_precio()
    producto_cantidad    = get_producto_cantidad()
        
    # Con los datos ingresados ya validados, armo el "producto" con un diccionario:
    producto = {
        "nombre"      : producto_nombre, 
        "descripcion" : producto_descripcion,
        "categoria"   : producto_categoria,
        "precio"      : producto_precio, 
        "cantidad"    : producto_cantidad
    }

    # Inserto el producto en la DB:
    db_insertar_producto(producto)
    
    print("")
    print(Fore.YELLOW + "Producto agregado con éxito.")

def mostrar_productos():
    productos = db_mostrar_productos()
    
    if not productos:
        print(Fore.YELLOW + "Aún no hay productos.")
    else:
        print("")
        print(Fore.CYAN + "Listado de productos:")
        print(Fore.CYAN + "-"*21)
        for producto in productos:
            mostrar_producto(producto)

def actualizar_producto():
    id = get_id()
    
    producto = db_mostrar_producto(id)
    
    if not producto:
        print(Fore.YELLOW + f"No existe producto con ID {id}")
    else:
        mostrar_producto(producto)

        cantidad = get_producto_cantidad()
        
        db_actualizar_producto(id, cantidad)
        
        print("")
        print(Fore.YELLOW + "Producto actualizado.")
    
def eliminar_producto():
    id = get_id()
    
    producto = db_mostrar_producto(id)
    
    if not producto:
        print(Fore.YELLOW + f"No existe producto con ID {id}")
    else:
        mostrar_producto(producto)

        print("")
        confirmar = input(Fore.MAGENTA + "Ingrese 'E' para confirmar la eliminación, o cualquier otra letra para cancelar: ").lower()
    
        if confirmar == 'e':    
            print("")
            
            db_eliminar_producto(id)
            
            print("")
            print(Fore.YELLOW + "Se eliminó el producto.")                
    
def buscar_producto():
    id = get_id()
    
    producto = db_mostrar_producto(id)
    
    if not producto:
        print(Fore.YELLOW + f"No existe producto con ID {id}")
    else:
        mostrar_producto(producto)
    
def reporte_bajo_stock():
    cantidad = get_producto_cantidad()
    
    print("")
    print(Fore.GREEN + f"Listado de productos con stock menor a {cantidad}:")
    print("-"*21)
    
    productos = db_reporte_bajo_stock(cantidad)
    
    if not productos:
        print(Fore.YELLOW + "No hay productos con bajo stock.")    
    else:
        for producto in productos:
            mostrar_producto(producto)

def salir_de_aplicacion():
    print(Fore.GREEN + "Saliendo de la aplicación.")
    
def opcion_incorrecta():
    print(Fore.MAGENTA + "Opción Incorrecta.")
    
# Auxiliares:
def mostrar_producto(producto):
    print(Fore.GREEN + "°"*60)
    print(f"Nombre: {producto[1]} [ID: {producto[0]}] [Categoría: {producto[3]}]")
    print(f"Descripción: {producto[2]}")
    print(f"Cantidad: {producto[4]} - Precio: {producto[5]}")            
    print(Fore.GREEN + "°"*60)
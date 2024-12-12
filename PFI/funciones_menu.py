from funciones_db import db_insertar_producto

# Crea el menú de usuario:
def crear_menu():
    print()
    print("-"*28)
    print("Menú de Gestión de Productos")
    print("-"*28)
    print()
    print("1. Agegar producto")
    print("2. Listado de productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de bajo stock")
    print("7. Salir")
    print()

    # Solicitar al usuario que seleccione una opción:
    # Aclaración: al no convertir a int el valor de opción salvo el caso en que el usuario ingresa algo que no sea numérico.
    opcion = input("Por favor, seleccione una opción: ")
    
    return opcion

def registrar_producto():
    # Ingreso de datos:
    print("")
    producto_nombre      = input("Ingrese el nombre del producto: ")
    producto_descripcion = input("Ingrese la descripción del producto: ")
    producto_categoria   = input("Ingrese la categoría del producto: ")
    producto_precio      = input("Ingrese el precio unitario del producto: ")
    producto_cantidad    = input("Ingrese la cantidad de unidades del producto: ")
    
    # Validaciones:
    #   Valido que el nombre no esté vacío:
    while producto_nombre == "":
        print("")
        print("Debe ingresar un nombre de producto. Ingrese un nombre.")
        
        producto_nombre = input("Ingrese el nombre del producto: ")
    
    #   Valido que la categoría no esté vacía:
    while producto_categoria == "":
        print("")
        print("Debe ingresar una categoría para el producto. Ingrese una categoría.")
        
        producto_categoria = input("Ingrese la categoría del producto: ")
    
    #   Valido que el precio sea un real mayor a cero:
    while not es_real(producto_precio) or float(producto_precio) <= 0:
        print("")
        print(f"El precio {producto_precio} no es válido. Ingrese un precio válido.")
        
        producto_precio = input("Ingrese el precio unitario del producto: ")
        
    producto_precio = float(producto_precio)       
    
    #   Valido que la cantidad sea un entero mayor a cero:
    while not es_entero(producto_cantidad) or int(producto_cantidad) <= 0:
        print("")
        print(f"La cantidad {producto_cantidad} no es válida. Ingrese una cantidad válida.")
        
        producto_cantidad = input("Ingrese la cantidad de unidades del producto: ")
        
    producto_cantidad = int(producto_cantidad)            
    
    # Con los datos ya valdiados, armo el "producto" con un diccionario:
    producto = {
        "nombre"      : producto_nombre, 
        "descripcion" : producto_descripcion,
        "categoria"   : producto_categoria,
        "precio"      : producto_precio, 
        "cantidad"    : producto_cantidad
    }

    # Inserto el producto en la DB:
    db_insertar_producto(producto)
    
    print("Producto agregado con éxito.")
    
    return producto

def mostrar_productos():
    productos_cantidad = len(productos)
            
    if productos_cantidad == 0:
        print("No hay productos registrados.")
    else:
        print(f"Lista de productos:")
        
        i = 0  
        while i < productos_cantidad:
            print("Producto", 
                  i+1, productos[i]["nombre"], 
                  "- Descripción:", 
                  productos[i]["descripcion"], 
                  "- Categoría:", 
                  productos[i]["categoria"],
                  "- Precio:", 
                  productos[i]["precio"],
                  "- Cantidad:", 
                  productos[i]["cantidad"])
            i +=1

def actualizar_producto():
    print("Producto actualizado.")
    
def eliminar_producto():
    print("Se eliminó el producto.")
    
def buscar_producto():
    print("Producto encontrado.")
    
def reporte_bajo_stock():
    print("Productos con bajo stock.")

def salir_de_aplicacion():
    print("Saliendo de la aplicación.")
    
def opcion_incorrecta():
    print("Opción Incorrecta.")
    
# Funciones auxiliares:
def es_real(str_float):
    try:
        str_float = float(str_float)
        return True
    except ValueError:
        return False

def es_entero(str_int):
    try:
        str_int = int(str_int)
        return True
    except ValueError:
        return False
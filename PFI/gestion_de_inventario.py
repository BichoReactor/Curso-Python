# Declaración de variables globales:
productos = []

opcion = "0"

# Declaración de funciones:
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

def registrar_producto(producto_nombre, producto_descripcion, producto_categoria, producto_precio, producto_cantidad):
    # Valido si el producto ya existe.
    i      = 0
    existe = False
    
    producto = {
        "nombre"      : producto_nombre, 
        "descripcion" : producto_descripcion,
        "categoria"   : producto_categoria,
        "precio"      : producto_precio, 
        "cantidad"    : producto_cantidad
    }
    
    while i < productos_cantidad:
        if producto_nombre.lower() == (productos[i]["nombre"]).lower():
            existe = True
            break
        else:
            i +=1
            
    if existe:
        # Si el producto existe, actualizo la cantidad, el precio, la categoría y la descripción.
        productos[i]["cantidad"]   += producto_cantidad
        productos[i]["descripción"] = producto_descripcion
        productos[i]["categoria"]   = producto_categoria
        productos[i]["precio"]      = producto_precio
    else:
        # Si el producto no existe, lo agrego.
        productos.append(producto)
    
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
    
while opcion != "7":
    # Menú de opciones:
    opcion = crear_menu()
    
    # En lugar de if-elif-else uso match que me parece más claro.
    match opcion:
        case "1":
            productos_cantidad = len(productos)
            
            producto_nombre      = input("Nombre del producto: ")
            producto_descripcion = input("Descripción del producto: ")
            producto_categoria   = input("Categoría del producto: ")
            producto_precio      = float(input("Precio del producto: "))
            producto_cantidad    = int(input(f"Cantidad de unidades del producto: "))
            
            # Tengo que validar que la cantidad sea mayor a cero.
            while producto_cantidad <= 0:
                print("La cantidad ingresada no es válida. Ingrese otra cantidad.")
                producto_cantidad = int(input(f"Cantidad de unidades del producto: "))
            
            # Tengo que validar que el precio sea mayor a cero.
            while producto_precio <= 0:
                print("El precio ingresado no es válido. Ingrese otro precio.")
                producto_precio = float(input(f"Precio del producto: "))
        
            registrar_producto(producto_nombre, producto_descripcion, producto_categoria, producto_precio, producto_cantidad)
        case "2":
            mostrar_productos()
        case "3":
            actualizar_producto()
        case "4":
            eliminar_producto()
        case "5":
            buscar_producto()
        case "6":
            reporte_bajo_stock()
        case "7":
            salir_de_aplicacion()        
        case _:
            opcion_incorrecta()        

print("Hasta luego. Gracias por utilizar nuestra app.")
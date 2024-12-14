def get_producto_nombre():
    while True:
        producto_nombre = input("* Nombre: ").strip()
        
        if not producto_nombre:
            print("--> Error: Debe ingresar un nombre.")
        else:
            return producto_nombre
    
def get_producto_descripcion():
    producto_descripcion = input("* Descripción: ").strip()
    
    return producto_descripcion

def get_producto_categoria():
    while True:
        producto_categoria = input("* Categoría: ").strip()
        
        if not producto_categoria:
            print("--> Error: Debe ingresar una categoría.")
        else:
            return producto_categoria

def get_producto_precio():
    while True:
        try:
            producto_precio = float(input("* Precio unitario: ").strip())
            
            if not producto_precio:
                print("--> Error: Debe ingresar el precio.")
            else:
                if producto_precio > 0:
                    return producto_precio
                else:
                    print("--> Error: El precio debe ser mayor a 0 (cero).")
                    
        except ValueError:
            print("--> Error: El precio del producto no es válido.")
            
def get_producto_cantidad():
    while True:
        try:
            producto_cantidad = int(input("* Cantidad: ").strip())
            
            if not producto_cantidad:
                print("--> Error: Debe ingresar la cantidad.")
            else:
                if producto_cantidad > 0:
                    return producto_cantidad
                else:
                    print("--> Error: La cantidad debe ser mayor a 0 (cero).")
                    
        except ValueError:
            print("--> Error: La cantidad del producto no es válida.")

def get_id():
    while True:
        try:
            id = int(input("* ID: ").strip())
            
            if not id:
                print("--> Error: Debe ingresar el ID.")
            else:
                if id >= 0:
                    return id
                else:
                    print("--> Error: El ID debe ser mayor o igual a 0 (cero).")
                    
        except ValueError:
            print("--> Error: El ID del producto no es válida.")
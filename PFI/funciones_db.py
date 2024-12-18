import sqlite3

# Asumo que el proyecto está dentro de una carpeta llamada PFI
RUTA_DB = "PFI/inventario.db"

# Inicializa la BD.
# Si no existe la BD la crea.
def db_crear_tabla():
    conexion = sqlite3.connect(RUTA_DB)

    cursor = conexion.cursor()

    cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS productos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT NOT NULL,
            descripcion TEXT,
            categoria   TEXT NOT NULL,
            cantidad    INTEGER NOT NULL,
            precio      REAL NOT NULL
    )
    """
    )
    
    conexion.commit()
    conexion.close()

def db_insertar_producto(producto):
    conexion = sqlite3.connect(RUTA_DB)

    cursor = conexion.cursor()
    
    query = """
                INSERT INTO productos (
                    nombre, descripcion, categoria, cantidad, precio)
                VALUES 
                    (?, ?, ?, ?, ?)
            """
    
    datos = (
                producto['nombre'], 
                producto['descripcion'],
                producto['categoria'],
                producto['cantidad'],
                producto['precio']
            )
    
    cursor.execute(query, datos)
    
    conexion.commit()
    conexion.close()
    
    return True

def db_mostrar_productos():
    conexion = sqlite3.connect(RUTA_DB)

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")

    resultados = cursor.fetchall()

    conexion.close()
    
    return resultados

def db_mostrar_producto(id):
    conexion = sqlite3.connect(RUTA_DB)

    cursor = conexion.cursor()

    query = "SELECT * FROM productos WHERE id = ?"
    
    datos = (id,)
    
    cursor.execute(query, datos)

    resultado = cursor.fetchone()

    conexion.close()
    
    return resultado

def db_actualizar_producto(id, cantidad):
    conexion = sqlite3.connect(RUTA_DB)

    cursor = conexion.cursor()
    
    query = "UPDATE productos SET cantidad = ? WHERE id = ?"
    datos = (cantidad, id)
    
    cursor.execute(query, datos)
    
    conexion.commit()
    conexion.close()
    
    return True

def db_eliminar_producto(id ):
    conexion = sqlite3.connect(RUTA_DB)

    cursor = conexion.cursor()
    
    query = "DELETE FROM productos WHERE id = ?"
    datos = (id,)
    
    cursor.execute(query, datos)
    
    conexion.commit()
    conexion.close()
    
    return True

def db_reporte_bajo_stock(cantidad_minima):
    conexion = sqlite3.connect(RUTA_DB)

    cursor = conexion.cursor()

    query = "SELECT * FROM productos WHERE cantidad < ?"
    
    datos = (cantidad_minima,)
    
    cursor.execute(query, datos)

    resultado = cursor.fetchall()

    conexion.close()
    
    return resultado

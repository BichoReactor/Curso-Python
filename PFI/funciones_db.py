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